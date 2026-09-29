import json
import sys
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "listener"))
import listener  # noqa: E402

PAGE = "3e9c7e0c-664c-81e5-bb21-e8a5af7360a1"
PAGE_NORM = PAGE.replace("-", "")


def automation_body(job_type="teaching", marker="teaching-session-ch01-20260929-101500-a1b2c3"):
    return {
        "source": {"type": "automation", "attempt": 1},
        "data": {
            "object": "page",
            "id": PAGE,
            "properties": {
                "Type": {"type": "select", "select": {"name": job_type}},
                "Marker": {"type": "title", "title": [{"plain_text": marker}]},
            },
        },
    }


def test_parse_automation_payload():
    job = listener.parse_payload(automation_body())
    assert job == {"page_id": PAGE_NORM, "type": "teaching", "marker": "teaching-session-ch01-20260929-101500-a1b2c3"}


def test_parse_without_properties_leaves_type_for_later():
    job = listener.parse_payload({"data": {"object": "page", "id": PAGE}})
    assert job == {"page_id": PAGE_NORM, "type": None, "marker": None}


def test_parse_integration_webhook_entity():
    job = listener.parse_payload({"type": "page.created", "entity": {"id": PAGE, "type": "page"}})
    assert job["page_id"] == PAGE_NORM


def test_parse_rejects_garbage_and_unknown_type():
    assert listener.parse_payload({"data": {"object": "page", "id": "not-an-id"}}) is None
    assert listener.parse_payload(automation_body(job_type="party"))["type"] is None


def test_prompt_is_single_line_and_unquoted():
    for jt in ("decompose", "teaching", "exam", None):
        prompt = listener.build_prompt(jt, PAGE_NORM, listener.safe('x"; rm -rf', "fallback"))
        assert "\n" not in prompt and '"' not in prompt and "'" not in prompt
    assert "agents/exam-analysis.md" in listener.build_prompt("exam", PAGE_NORM, "m")
    assert "router" in listener.build_prompt(None, PAGE_NORM, "m")


def test_store_dedupes(tmp_path):
    store = listener.JobStore(tmp_path / "jobs.json")
    job = {"page_id": PAGE_NORM, "type": "exam", "marker": "m"}
    assert store.claim(job) is True
    assert store.claim(job) is False  # duplicate webhook while queued
    store.update(PAGE_NORM, status="done")
    assert store.claim(job) is False  # already processed
    store.update(PAGE_NORM, status="failed")
    assert store.claim(job) is True  # failed jobs may be re-queued
    reloaded = listener.JobStore(tmp_path / "jobs.json")
    assert reloaded.get(PAGE_NORM)["status"] == "queued"


@pytest.fixture
def server(tmp_path, monkeypatch):
    cfg = listener.Config()
    cfg.secret = "s3cret"
    worker = listener.Worker(cfg, listener.JobStore(tmp_path / "jobs.json"))  # not started: jobs stay queued
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), listener.make_handler(cfg, worker))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{httpd.server_address[1]}", worker
    httpd.shutdown()


def post(url, body, secret=None):
    headers = {"Content-Type": "application/json"}
    if secret:
        headers["X-Learner-Secret"] = secret
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.loads(resp.read())
    except urllib.error.HTTPError as err:
        return err.code, json.loads(err.read())


def test_webhook_requires_secret(server):
    base, worker = server
    assert post(f"{base}/webhook", automation_body())[0] == 401
    assert post(f"{base}/webhook", automation_body(), secret="wrong")[0] == 401
    assert worker.q.qsize() == 0


def test_webhook_queues_once(server):
    base, worker = server
    assert post(f"{base}/webhook", automation_body(), secret="s3cret") == (202, {"accepted": True})
    assert post(f"{base}/webhook", automation_body(), secret="s3cret") == (202, {"accepted": False})
    assert worker.q.qsize() == 1
    assert post(f"{base}/webhook", {"data": {}}, secret="s3cret")[0] == 400


def test_final_text_reads_result_event():
    stream = "\n".join([
        '{"type":"thinking","subtype":"delta","text":"x"}',
        "not json",
        json.dumps({"type": "result", "subtype": "success", "result": "line one\nRESULT done m 3 concepts"}),
    ])
    assert listener.final_text(stream).splitlines()[-1] == "RESULT done m 3 concepts"
    assert listener.final_text("garbage") == ""


def test_agent_command_prefers_bundled_node(tmp_path, monkeypatch):
    for version in ("2026.09.2-aaa", "2026.09.18-bbb", "2026.10.1-ccc", "dist-package"):
        d = tmp_path / "cursor-agent" / "versions" / version
        d.mkdir(parents=True)
        if version != "2026.10.1-ccc":  # incomplete install must be skipped; dist-package is updater staging
            (d / "node.exe").touch()
            (d / "index.js").touch()
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path))
    monkeypatch.setattr(listener.os, "name", "nt")
    cmd = listener.agent_command(listener.Config())
    assert cmd[0].endswith(str(Path("2026.09.18-bbb") / "node.exe"))
