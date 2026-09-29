"""Learner 101 local listener.

Transport only: receives the Notion "Send webhook" POST for a new Sessions row, queues it,
and runs the matching headless Cursor agent. All judgment lives in the agents.

    python listener/listener.py              # listener + ngrok tunnel (if NGROK_DOMAIN set)
    python listener/listener.py --no-tunnel  # listener only
"""

from __future__ import annotations

import argparse
import hmac
import json
import logging
import os
import queue
import re
import shutil
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = ROOT / "state"
LOG_DIR = ROOT / "logs"
STATE_FILE = STATE_DIR / "jobs.json"

SESSIONS_DATA_SOURCE = "b0a0d8e9-4fc8-4400-b36b-551b117cf12b"
NOTION_VERSION = "2025-09-03"

AGENT_SPECS = {
    "decompose": ("Decomposition", "agents/decomposition.md"),
    "teaching": ("Teaching-Analysis", "agents/teaching-analysis.md"),
    "exam": ("Exam-Analysis", "agents/exam-analysis.md"),
}
MAX_ATTEMPTS = 2

log = logging.getLogger("learner101")


# ---------------------------------------------------------------- config

def load_env(path: Path) -> None:
    """Minimal .env loader; real environment variables win."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


class Config:
    def __init__(self) -> None:
        self.port = int(os.environ.get("LISTENER_PORT", "8788"))
        self.secret = os.environ.get("WEBHOOK_SECRET", "")
        self.ngrok_domain = os.environ.get("NGROK_DOMAIN", "").removeprefix("https://").strip("/")
        self.notion_token = os.environ.get("NOTION_TOKEN", "")
        self.agent_path = os.environ.get("AGENT_PATH", "")
        self.agent_model = os.environ.get("AGENT_MODEL", "")
        self.job_timeout = int(os.environ.get("JOB_TIMEOUT_MIN", "45")) * 60


# ---------------------------------------------------------------- payload parsing

_ID_RE = re.compile(r"^[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{12}$")
_SAFE_RE = re.compile(r"[^A-Za-z0-9_-]")
_VERSION_RE = re.compile(r"^(\d{4})\.(\d{1,2})\.(\d{1,2})-[0-9a-f]+$")


def normalize_id(raw: str) -> str | None:
    raw = (raw or "").strip()
    if not _ID_RE.match(raw):
        return None
    return raw.replace("-", "").lower()


def _plain_text(prop: dict) -> str:
    items = prop.get("title") or prop.get("rich_text") or []
    return "".join(i.get("plain_text") or i.get("text", {}).get("content", "") for i in items)


def parse_payload(body: dict) -> dict | None:
    """Extract {page_id, type, marker} from a Notion automation webhook body.

    Automation webhooks send {"source": {...}, "data": <page object>}; integration webhooks send
    {"entity": {"id": ...}}. Type/marker are only present if the automation includes those
    properties; missing values are resolved later.
    """
    data = body.get("data") if isinstance(body.get("data"), dict) else body
    page_id = None
    if data.get("object") == "page" or "properties" in data:
        page_id = normalize_id(str(data.get("id", "")))
    if not page_id and isinstance(body.get("entity"), dict):
        page_id = normalize_id(str(body["entity"].get("id", "")))
    if not page_id:
        return None

    props = data.get("properties") or {}
    job_type = None
    type_prop = props.get("Type") or {}
    if isinstance(type_prop.get("select"), dict):
        job_type = (type_prop["select"].get("name") or "").lower() or None
    marker = _plain_text(props.get("Marker") or {}) or None
    if job_type not in AGENT_SPECS:
        job_type = None
    return {"page_id": page_id, "type": job_type, "marker": marker}


def safe(value: str | None, fallback: str) -> str:
    cleaned = _SAFE_RE.sub("", value or "")[:120]
    return cleaned or fallback


# ---------------------------------------------------------------- state

class JobStore:
    """Persistent dedupe + queue state, keyed by Sessions page id."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.lock = threading.Lock()
        self.jobs: dict[str, dict] = {}
        if path.exists():
            try:
                self.jobs = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                log.warning("state file unreadable, starting fresh")

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.jobs, indent=2), encoding="utf-8")
        tmp.replace(self.path)

    def claim(self, job: dict) -> bool:
        """Register a job; False if it's already queued, running or done."""
        with self.lock:
            existing = self.jobs.get(job["page_id"])
            if existing and existing["status"] in ("queued", "running", "done"):
                return False
            record = existing or {"attempts": 0}
            record.update(
                type=job.get("type") or record.get("type"),
                marker=job.get("marker") or record.get("marker"),
                status="queued",
                updated=_now(),
            )
            self.jobs[job["page_id"]] = record
            self._save()
            return True

    def update(self, page_id: str, **fields) -> None:
        with self.lock:
            self.jobs.setdefault(page_id, {"attempts": 0}).update(fields, updated=_now())
            self._save()

    def get(self, page_id: str) -> dict:
        with self.lock:
            return dict(self.jobs.get(page_id, {}))

    def pending(self) -> list[str]:
        with self.lock:
            return [pid for pid, j in self.jobs.items() if j["status"] in ("queued", "running")]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# ---------------------------------------------------------------- Notion REST (optional transport)

def notion_request(cfg: Config, method: str, path: str, payload: dict | None = None) -> dict:
    req = urllib.request.Request(
        f"https://api.notion.com/v1/{path}",
        method=method,
        data=json.dumps(payload).encode() if payload is not None else None,
        headers={
            "Authorization": f"Bearer {cfg.notion_token}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def fetch_session_meta(cfg: Config, page_id: str) -> dict:
    page = notion_request(cfg, "GET", f"pages/{page_id}")
    parsed = parse_payload({"data": page}) or {}
    return {"type": parsed.get("type"), "marker": parsed.get("marker")}


def mark_failed_in_notion(cfg: Config, page_id: str, reason: str) -> None:
    if not cfg.notion_token:
        return
    try:
        notion_request(cfg, "PATCH", f"pages/{page_id}", {"properties": {
            "Status": {"select": {"name": "failed"}},
            "Note": {"rich_text": [{"text": {"content": reason[:1900]}}]},
        }})
    except (urllib.error.URLError, OSError) as exc:
        log.warning("could not mark %s failed in Notion: %s", page_id, exc)


# ---------------------------------------------------------------- agent runner

def _latest_windows_agent() -> list[str] | None:
    """Newest bundled node.exe + index.js of the Cursor CLI.

    Called directly because the cursor-agent.ps1 wrapper hangs when stdout is a pipe. Only
    YYYY.MM.DD-<hash> folders count: the auto-updater stages into other folders (dist-package).
    """
    versions = Path(os.environ.get("LOCALAPPDATA", "")) / "cursor-agent" / "versions"
    candidates = [
        d for d in versions.glob("*")
        if _VERSION_RE.match(d.name) and (d / "node.exe").exists() and (d / "index.js").exists()
    ]
    if not candidates:
        return None
    newest = max(candidates, key=lambda d: [int(x) for x in _VERSION_RE.match(d.name).groups()])
    return [str(newest / "node.exe"), str(newest / "index.js")]


def agent_command(cfg: Config) -> list[str]:
    if cfg.agent_path:
        if cfg.agent_path.lower().endswith(".js"):
            return ["node", cfg.agent_path]
        return [cfg.agent_path]
    if os.name == "nt" and (cmd := _latest_windows_agent()):
        return cmd
    return [shutil.which("agent") or shutil.which("cursor-agent") or "agent"]


def build_prompt(job_type: str | None, page_id: str, marker: str) -> str:
    # Single line, no quotes: it passes through powershell argument parsing on Windows.
    if job_type in AGENT_SPECS:
        name, spec = AGENT_SPECS[job_type]
        return (
            f"You are the Learner 101 {name} agent. Read agents/_common.md and {spec} in this "
            f"workspace and follow them exactly. Job: Sessions row page id {page_id}, marker {marker}. "
            "Run unattended and never ask questions."
        )
    return (
        "You are the Learner 101 job router. Read agents/_common.md in this workspace. Fetch the "
        f"Sessions row with page id {page_id} via the Notion MCP and read its Type property. Then "
        "follow the matching spec exactly: decompose uses agents/decomposition.md, teaching uses "
        "agents/teaching-analysis.md, exam uses agents/exam-analysis.md. If Type is missing or "
        "unknown, set Status to failed with the reason. Run unattended and never ask questions."
    )


def final_text(stream: str) -> str:
    """The agent's final answer from --output-format stream-json output."""
    for line in reversed(stream.splitlines()):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "result":
            return str(event.get("result") or "")
    return ""


def run_agent(cfg: Config, prompt: str, log_path: Path) -> tuple[int, str]:
    """Run one headless agent; returns (exit code, final answer text). Full event stream goes to the log."""
    cmd = agent_command(cfg) + [
        "-p", prompt,
        "--output-format", "stream-json",
        "--force", "--approve-mcps", "--trust",
        "--workspace", str(ROOT),
    ]
    if cfg.agent_model:
        cmd += ["--model", cfg.agent_model]
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(f"\n===== {_now()} =====\n{prompt}\n\n")
        fh.flush()
        try:
            proc = subprocess.run(
                cmd, cwd=ROOT, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, encoding="utf-8", errors="replace", timeout=cfg.job_timeout,
            )
        except subprocess.TimeoutExpired:
            fh.write("TIMEOUT\n")
            return 124, "timeout"
        except OSError as exc:
            fh.write(f"LAUNCH ERROR {exc}\n")
            return 127, str(exc)
        fh.write(proc.stdout or "")
        answer = final_text(proc.stdout or "")
        fh.write(f"\n----- final answer -----\n{answer}\n")
    return proc.returncode, answer


# ---------------------------------------------------------------- worker

class Worker(threading.Thread):
    """Runs jobs one at a time, so sessions that end close together are processed in order."""

    def __init__(self, cfg: Config, store: JobStore) -> None:
        super().__init__(daemon=True)
        self.cfg = cfg
        self.store = store
        self.q: queue.Queue[str] = queue.Queue()

    def submit(self, job: dict) -> bool:
        if not self.store.claim(job):
            return False
        self.q.put(job["page_id"])
        return True

    def run(self) -> None:
        while True:
            page_id = self.q.get()
            try:
                self.process(page_id)
            except Exception:  # keep the worker alive no matter what
                log.exception("job %s crashed", page_id)
                self.store.update(page_id, status="failed")

    def process(self, page_id: str) -> None:
        job = self.store.get(page_id)
        if job.get("status") == "done":
            return
        if not job.get("type") and self.cfg.notion_token:
            try:
                job.update({k: v for k, v in fetch_session_meta(self.cfg, page_id).items() if v})
                self.store.update(page_id, type=job.get("type"), marker=job.get("marker"))
            except (urllib.error.URLError, OSError) as exc:
                log.warning("could not read session %s from Notion: %s", page_id, exc)

        marker = safe(job.get("marker"), page_id)
        prompt = build_prompt(job.get("type"), page_id, marker)
        log_path = LOG_DIR / f"{marker}.log"

        while True:
            attempts = self.store.get(page_id).get("attempts", 0) + 1
            self.store.update(page_id, status="running", attempts=attempts)
            log.info("running %s (%s) attempt %d", marker, job.get("type") or "router", attempts)
            code, answer = run_agent(self.cfg, prompt, log_path)
            result = next((ln for ln in reversed(answer.splitlines()) if ln.startswith("RESULT ")), "")
            if code == 0:
                self.store.update(page_id, status="done", result=result)
                log.info("done %s: %s", marker, result or "(no RESULT line)")
                return
            log.warning("agent exited %d for %s (see %s)", code, marker, log_path)
            if attempts >= MAX_ATTEMPTS:
                self.store.update(page_id, status="failed", result=f"exit {code}")
                mark_failed_in_notion(self.cfg, page_id, f"listener: agent exited {code} after {attempts} attempts; log {log_path.name}")
                return
            time.sleep(30)


# ---------------------------------------------------------------- catch-up (runs once at startup)

def catch_up(cfg: Config, worker: Worker) -> None:
    """Queue Sessions rows that were created while this machine was off (webhook missed)."""
    try:
        _catch_up(cfg, worker)
    except Exception:
        log.exception("catch-up failed; POST /catchup or restart to retry")


def _catch_up(cfg: Config, worker: Worker) -> None:
    for pid in worker.store.pending():  # interrupted locally
        worker.store.update(pid, status="interrupted")
        worker.submit({"page_id": pid})

    rows: list[dict] = []
    if cfg.notion_token:
        try:
            resp = notion_request(cfg, "POST", f"data_sources/{SESSIONS_DATA_SOURCE}/query", {
                "filter": {"or": [
                    {"property": "Status", "select": {"equals": "queued"}},
                    {"property": "Status", "select": {"equals": "processing"}},
                ]},
                "sorts": [{"timestamp": "created_time", "direction": "ascending"}],
            })
            rows = [p for r in resp.get("results", []) if (p := parse_payload({"data": r}))]
        except (urllib.error.URLError, OSError) as exc:
            log.warning("catch-up query failed: %s", exc)
    else:
        prompt = (
            "Read agents/_common.md. Using the Notion MCP, list every row in the Sessions data source "
            "whose Status is queued or processing, oldest first. Change nothing. For each row print "
            "exactly one line: JOB <page id> <Type> <Marker>. Print nothing else."
        )
        code, answer = run_agent(cfg, prompt, LOG_DIR / "catchup.log")
        for line in answer.splitlines():
            parts = line.strip().split()
            if len(parts) >= 2 and parts[0] == "JOB" and (pid := normalize_id(parts[1])):
                jtype = parts[2].lower() if len(parts) > 2 and parts[2].lower() in AGENT_SPECS else None
                rows.append({"page_id": pid, "type": jtype, "marker": parts[3] if len(parts) > 3 else None})
        if code != 0:
            log.warning("catch-up agent exited %d", code)

    queued = sum(worker.submit(r) for r in rows)
    log.info("catch-up: %d row(s) found in Notion, %d newly queued", len(rows), queued)


# ---------------------------------------------------------------- HTTP

def make_handler(cfg: Config, worker: Worker):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):  # route through logging
            log.debug("http %s", fmt % args)

        def _reply(self, code: int, body: dict) -> None:
            raw = json.dumps(body).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

        def _authorized(self) -> bool:
            given = self.headers.get("X-Learner-Secret", "")
            return bool(cfg.secret) and hmac.compare_digest(given.encode(), cfg.secret.encode())

        def do_GET(self):
            if self.path == "/health":
                self._reply(200, {"ok": True, "pending": len(worker.store.pending())})
            else:
                self._reply(404, {"error": "not found"})

        def do_POST(self):
            length = int(self.headers.get("Content-Length") or 0)
            raw = self.rfile.read(min(length, 1_000_000))
            if not self._authorized():
                log.warning("rejected %s: bad or missing X-Learner-Secret", self.path)
                self._reply(401, {"error": "unauthorized"})
                return
            if self.path == "/catchup":
                threading.Thread(target=catch_up, args=(cfg, worker), daemon=True).start()
                self._reply(202, {"ok": True})
                return
            if self.path != "/webhook":
                self._reply(404, {"error": "not found"})
                return
            try:
                job = parse_payload(json.loads(raw or b"{}"))
            except json.JSONDecodeError:
                job = None
            if not job:
                log.warning("webhook without a page id: %s", raw[:300])
                self._reply(400, {"error": "no page id in payload"})
                return
            accepted = worker.submit(job)
            log.info("webhook %s type=%s accepted=%s", job["page_id"], job["type"], accepted)
            self._reply(202, {"accepted": accepted})

    return Handler


# ---------------------------------------------------------------- tunnel

def supervise_ngrok(cfg: Config) -> None:
    """Keep an ngrok tunnel on the fixed domain up; the URL never rotates, so nothing re-registers."""
    ngrok = shutil.which("ngrok")
    if not ngrok:
        log.error("ngrok not found on PATH; tunnel disabled")
        return
    backoff = 5
    while True:
        log.info("starting tunnel https://%s -> localhost:%d", cfg.ngrok_domain, cfg.port)
        started = time.time()
        with (LOG_DIR / "ngrok.log").open("a", encoding="utf-8") as fh:
            proc = subprocess.run(
                [ngrok, "http", f"--url=https://{cfg.ngrok_domain}", str(cfg.port), "--log", "stdout"],
                stdout=fh, stderr=subprocess.STDOUT,
            )
        log.warning("tunnel exited with %d; restarting in %ds", proc.returncode, backoff)
        time.sleep(backoff)
        backoff = 5 if time.time() - started > 300 else min(backoff * 2, 300)


# ---------------------------------------------------------------- main

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--no-tunnel", action="store_true", help="don't start ngrok")
    parser.add_argument("--no-catchup", action="store_true", help="skip the startup catch-up")
    args = parser.parse_args()

    load_env(ROOT / ".env")
    cfg = Config()
    LOG_DIR.mkdir(exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(LOG_DIR / "listener.log", encoding="utf-8")],
    )
    if not cfg.secret:
        log.error("WEBHOOK_SECRET is not set in .env; refusing to start")
        return 1

    worker = Worker(cfg, JobStore(STATE_FILE))
    worker.start()
    server = ThreadingHTTPServer(("127.0.0.1", cfg.port), make_handler(cfg, worker))
    log.info("listening on http://127.0.0.1:%d (POST /webhook, POST /catchup, GET /health)", cfg.port)

    if cfg.ngrok_domain and not args.no_tunnel:
        threading.Thread(target=supervise_ngrok, args=(cfg,), daemon=True).start()
    elif not args.no_tunnel:
        log.warning("NGROK_DOMAIN not set; running without a tunnel (Notion can't reach this machine)")
    if not args.no_catchup:
        threading.Thread(target=catch_up, args=(cfg, worker), daemon=True).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
