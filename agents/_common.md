# Learner 101 — shared context for every headless agent

You are running headless (`agent -p`) on Rawad's machine, launched by the local listener.
You have the **Notion MCP** (server name `notion`). Use it for every read and write.
Nobody is watching this run. Never ask questions; never wait for input. If something is
genuinely ambiguous, record why in Notion (see "Failure handling") and stop.

Design principle: ALL judgment is yours. The listener only moved data to you.

## Notion IDs

| Thing | Database (page) id | Data source id |
|---|---|---|
| Learner 101 root page | `3e9c7e0c664c81e5bb21e8a5af7360a1` | — |
| Chapters | `d0e498f53e984dc38de47e738db5f7ff` | `collection://7621b84c-72ad-4888-b394-16e29cfda753` |
| Sessions | `85e2d25828a34b3dbaf047cbdb01f4ae` | `collection://b0a0d8e9-4fc8-4400-b36b-551b117cf12b` |
| Concept Registry | `5b97823f3fc741978fac6116244181f7` | `collection://f2e76ff5-6e72-44f2-bf96-b2d424d7e202` |

## Data model

**Sessions** row = one job. Properties: `Marker` (title), `Chapter` (relation → Chapters),
`Type` (teaching | exam | decompose), `Status` (queued | processing | done | provisional | failed),
`Note` (text), `Created`. For teaching/exam rows the page body is the transcript, written by the
end-session skill, and ends with the sentinel line `=== TRANSCRIPT END <marker> ===`.

**Chapters** row = one chapter. Properties: `Chapter` (title), `Chapter Key` (slug used in markers),
`is_decomposed`, `has_teaching_session`, `has_exam_session` (checkboxes — state, not triggers),
`Decomposition Status` (pending | running | passed | failed), `Decomposition Note`,
`Teaching Brief Status` / `Exam Brief Status` (none | updating | ready | provisional),
`Concepts` (relation → Concept Registry), `Sessions` (relation → Sessions).

Chapter row page body:
- `## Source` section — the chapter text as written by the decompose-chapter skill.
- Child pages, created by decompose-chapter, filled by agents:
  `Concept Map`, `Teaching Analysis`, `Exam Analysis`, `Next Teaching Brief`, `Next Exam Brief`.

**Concept Registry** row = one stable concept across all chapters. Properties: `Concept` (title),
`Concept ID` (auto, e.g. CON-12), `Definition`, `Aliases`, `Chapters` (relation → Chapters).

## Chapter source resolution
1. If a local file `chapters/<Chapter Key>.*` exists in this workspace (pdf, md, txt), it is the
   authoritative source — read it.
2. Otherwise use the `## Source` section of the chapter row page.
3. If neither exists or the source is visibly truncated, fail the job (see below).

## Brief status protocol (the skills depend on this)
- Before editing a brief, set its status property to `updating`.
- When done, set it to `ready`.
- If you could not finish (error, provisional input), restore the status it had before you started
  (use `none` if the brief page is still empty). Never leave `updating` behind.
- Skills only use a brief whose status is `ready`; anything else → free-run / baseline exam.
- `provisional` is reserved: a brief that exists but was built only from provisional sessions.
  Skills treat it as not ready.

## Scoring rubric (guidance, applied with judgment; scale 0–3)
- Coverage (teaching): 0 never touched / 1 named not explained / 2 explained shallowly (what, not why)
  / 3 explained with reasoning + a connection to another concept or an example.
- Accuracy (only concepts actually discussed): 0 contradicts chapter / 1 partially correct with a real
  error / 2 correct but imprecise / 3 correct and precise.
- Retention (exam only): 0 couldn't recall unprompted / 1 heavy hinting / 2 small nudge /
  3 recalled and applied cold to a new question.
- The chapter is the FLOOR, not the ceiling. A correct answer richer than the source, or a valid
  outside connection, is still a 3. Only real errors or contradictions cost points. Still check
  that "beyond" is genuinely correct and relevant, not confident nonsense.
- Store the FULL per-concept matrix. Never collapse to a single chapter score.

## Job lifecycle
1. First action: set the Sessions row `Status` = `processing`.
2. Last action: set `Status` = `done` (or `provisional` / `failed` as your spec says), and put a
   one-line summary in `Note`.

## Failure handling
If you cannot complete the job (missing source, missing transcript, Notion error you can't work
around, genuine ambiguity): set the Sessions row `Status` = `failed`, write the reason in `Note`,
restore any brief status you changed, and exit. Do not guess. The listener retries once.

## Output
When finished, print one line: `RESULT <status> <marker> <short summary>`.
