# Learner 101

Voice-first learning loop: Claude teaches or examines one chapter per session, and local headless
Cursor agents analyse each session and write the next brief into Notion.

```
Claude chat (Project per chapter)            Notion (Learner 101 page)              This machine
────────────────────────────────            ──────────────────────────              ───────────────────────────
decompose-chapter ──► Chapters row (+Source) ─┐
                  └─► Sessions row (decompose) ┤
teacher / examiner ◄── Concept Map, briefs     │ automation "page added"
end-session ──────► Sessions row (+transcript) ┴─► Send webhook ──► ngrok ──► listener.py ──► agent -p (Cursor CLI)
                                                                     (fixed domain)  queue/dedupe      │ Notion MCP
                    Analyses, briefs, registry ◄──────────────────────────────────────────────────────┘
```

Spec and design history: the Learner 101 page in Notion (see "REVISIONS 2026-09-29").

## Layout

| Path | What |
|---|---|
| `skills/*/SKILL.md` | The 4 chat skills (teacher, examiner, end-session, decompose-chapter) |
| `project-instructions.md` | Paste into each chapter's Claude Project instructions |
| `agents/*.md` | Specs the headless Cursor agents follow (`_common.md` = IDs, data model, rubric) |
| `listener/listener.py` | Webhook listener + ngrok supervisor + job queue (stdlib only) |
| `.cursor/mcp.json` | Gives the Cursor agents the Notion MCP |
| `chapters/` | Optional: original chapter files as `<chapter-key>.pdf`; they override the text copy |
| `state/`, `logs/` | Runtime job state and per-session agent logs (git-ignored) |

## One-time setup

1. **Notion MCP login for Cursor** (browser OAuth). Run from this folder:
   ```bash
   agent mcp login notion
   ```
   Then confirm the agent can read Notion:
   ```bash
   agent -p "Using the notion MCP, fetch page 3e9c7e0c664c81e5bb21e8a5af7360a1 and print its title" --approve-mcps --trust
   ```
2. **ngrok static domain**: dashboard.ngrok.com → Domains → claim the free static domain, and put it
   in `.env` as `NGROK_DOMAIN`. `WEBHOOK_SECRET` is already generated in `.env`.
3. **Notion automation** (needs Notion Plus or higher): open the Sessions database → ⚡ Automations → New:
   - Trigger: *Page added*
   - Action: *Send webhook* → URL `https://<NGROK_DOMAIN>/webhook`
   - Custom header: `X-Learner-Secret` = the `WEBHOOK_SECRET` value from `.env`
   - Include properties: `Marker`, `Type`, `Chapter`
4. **Claude skills**: `python scripts/package_skills.py` builds `dist/*.zip`. Upload each at
   claude.ai → Settings → Capabilities → Skills. Enable the Notion connector in your chats.
5. **Per chapter**: create a Claude Project, add the chapter PDF to its knowledge, paste
   `project-instructions.md` into its instructions, then say "decompose chapter".
6. **Optional** `NOTION_TOKEN` in `.env` (an internal integration shared with the Learner 101
   page): lets the listener do the startup catch-up and failure marking over REST instead of
   spending an agent run.

## Running

```bash
python listener/listener.py
```
or `.\start.ps1`. To start it at every logon:
```bash
powershell -ExecutionPolicy Bypass -File scripts/install_autostart.ps1
```

On startup the listener queues every Sessions row still `queued`/`processing` (webhooks that fired
while the machine was off). `GET /health` shows pending jobs; `POST /catchup` (with the secret
header) re-runs the catch-up.

## Test

```bash
python -m pytest -q tests
```

## Verify the Notion trigger first

Notion automations may not fire for pages created through the API/MCP (the end-session skill
creates rows that way). Before relying on it: start the listener, create a Sessions row from a
Claude chat via the Notion connector, and check `logs/listener.log` for `webhook ... accepted=True`.
If nothing arrives, the fallback is the startup catch-up plus `POST /catchup`.
