---
name: end-session
description: Ends a Learner 101 teaching or exam session ONLY when the learner explicitly asks to end it (e.g. "/end-session", "end session"). Mints a unique session marker and writes the session transcript to Notion, which triggers the analysis.
disable-model-invocation: true
---

# End-Session (Learner 101)

## When it runs
ONLY when the learner explicitly asks to end the session ("end session", "/end-session"). Never on
your own initiative, and never from phrasing like "I'm done" alone. If in doubt, ask
"end the session and send it for analysis?" and wait for yes.

## Notion
- Sessions data source: `collection://b0a0d8e9-4fc8-4400-b36b-551b117cf12b`
  (properties: `Marker` title, `Chapter` relation, `Type` select, `Status` select, `Note` text).
- Chapters data source: `collection://7621b84c-72ad-4888-b394-16e29cfda753`
  (property `Chapter Key`).

## Steps
1. Determine the session type (`teaching` or `exam`) from which skill ran this conversation, and
   the chapter. Find the chapter row and read its `Chapter Key`.
2. Mint the marker: `<type>-session-<chapter-key>-<YYYYMMDD-HHMMSS>-<random>` where `<random>` is
   6 random lowercase letters/digits you pick now. The random suffix is required (two sessions can
   end in the same minute).
3. Say the marker in the chat in one line, so it's also in this conversation.
4. Create ONE row in Sessions with: `Marker` = the marker, `Chapter` = the chapter row,
   `Type` = the type, `Status` = `queued`. Creating this row is what triggers the analysis.
   Put the transcript in that row's page body:

   ```
   Marker: <marker>
   Type: <type> · Chapter: <chapter> · Turns: <N>
   Mode: brief-driven | free-run | baseline

   **Learner:** <exactly what he said>
   **Teacher|Examiner:** <what you said>
   ...
   === TRANSCRIPT END <marker> ===
   ```
   Rules for the transcript:
   - Every turn from the start of the session, in order. `Turns` = the number of turns written.
   - Learner turns VERBATIM (voice transcription as-is, including wrong answers).
   - Your turns may be condensed, but keep every question you asked, every hint or nudge you gave,
     and every answer you revealed — the grader needs them.
   - If the transcript is long, create the row with the first part, then append the rest in order
     with further page-content inserts. The sentinel line goes last, only after everything else is
     written. A missing sentinel tells the analysis the write was cut off.
5. Confirm to the learner in one line: session closed, analysis queued, marker.

## Why this design
Claude chats aren't stored on the local machine and don't expose a session id to tools, so the
transcript travels inside the Sessions row. The marker names the row; one row = one session, so
sessions ending close together never overwrite each other.
