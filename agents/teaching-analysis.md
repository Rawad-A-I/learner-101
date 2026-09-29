# AGENT — Teaching-Analysis

Read `agents/_common.md` first; everything there applies.

Triggered by a Sessions row with `Type` = `teaching` (created by the end-session skill).

## Purpose
Analyze one completed teaching-session transcript against the chapter's concept map, then update
the chapter's Teaching Analysis and BOTH briefs.

## Steps
1. Set the Sessions row `Status` = `processing`. Follow `Chapter` to the chapter row. Read the
   `Concept Map` child page. If the chapter is not decomposed (`is_decomposed` = false), analyze
   against the chapter source directly and say so in the analysis.
2. Read the transcript = the Sessions row page body. The Sessions row IS this session; no search
   is needed (the marker in the title is the identity).
3. Completeness check. The learner ended the session deliberately with end-session, so the session
   itself is complete. What can be incomplete is the WRITE of the transcript. Treat it as
   incomplete only if:
   - the sentinel line `=== TRANSCRIPT END <marker> ===` is missing, or
   - the body is visibly cut off (e.g. ends mid-turn, or the turn count stated in the transcript
     header doesn't match).
   Do NOT use the presence or absence of phrases like "I'm done" as a signal.
4. Incomplete → graceful degradation: still write the per-concept analysis, but label its section
   `PROVISIONAL`, do not touch either brief, set the Sessions row `Status` = `provisional` with the
   reason, and stop. The next complete session folds this data in (step 6 reads it).
5. Analyze per concept (every concept in the map):
   - Coverage 0–3.
   - Accuracy 0–3 for concepts actually discussed (blank if not discussed — don't penalize twice).
   - Misconceptions: claims that contradict the chapter, quoted from the transcript.
   - Gaps: map concepts / key points never discussed.
   - Observations from free-run: what the learner chose to explore, assumed, or avoided.
6. Write to the `Teaching Analysis` child page: INSERT a new section at the top (keep all older
   sections — raw data is never overwritten):

   ```
   ## <marker> — <date> — complete | PROVISIONAL
   Mode: brief-driven | free-run
   | Registry ID | Concept | Coverage | Accuracy | Evidence (short quote or note) |
   |---|---|---|---|---|
   Misconceptions: ...
   Gaps: ...
   Observations: ...
   ```
   Also tick the matching `[ ]` key points in the Concept Map ONLY if you are sure they were covered
   at depth ≥ 2 (change `- [ ]` to `- [x]`); never untick.
7. Update the `Next Teaching Brief` (status protocol from `_common.md`). Briefs COMPOUND: start
   from the current brief, drop items now covered at depth 3 with accuracy ≥ 2, keep unresolved
   ones, add new gaps and misconceptions, and fold in:
   - any PROVISIONAL sections in Teaching Analysis newer than the last complete one, and
   - the latest Exam Analysis section (exam-revealed gaps must reach teaching).
   Format: ranked focus list, each item = Registry ID, concept, why it's on the list, and a
   suggested Socratic entry question.
8. Update the `Next Exam Brief` (same protocol): add concepts that reached coverage ≥ 2 this session
   as "now testable", keep existing exam targets. This seeds an exam brief even when teaching
   happens first.
9. Set chapter `has_teaching_session` = true. Sessions row `Status` = `done`, `Note` = one-line
   summary (e.g. "12 concepts, 5 at depth 3, 2 misconceptions").

## Guardrails
- Everything is relative to the chapter's concept map, not general knowledge.
- Self-correct on the next good session; never require human intervention.
