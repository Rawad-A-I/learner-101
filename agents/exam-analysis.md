# AGENT — Exam-Analysis

Read `agents/_common.md` first; everything there applies.

Triggered by a Sessions row with `Type` = `exam` (created by the end-session skill).

## Purpose
Grade one completed exam-session transcript against the rubric, then update the chapter's Exam
Analysis and BOTH briefs.

## Steps
1. Set the Sessions row `Status` = `processing`. Follow `Chapter` to the chapter row. Read the
   `Concept Map`. If the chapter is not decomposed, grade against the source and say so.
2. Read the transcript = the Sessions row page body (this row IS the session).
3. Completeness check — identical to Teaching-Analysis step 3: only a missing sentinel line
   `=== TRANSCRIPT END <marker> ===` or a visibly cut-off body makes it incomplete. Never judge by
   end-of-session phrases.
4. Incomplete → write the graded section labelled `PROVISIONAL`, leave both briefs alone, set the
   Sessions row `Status` = `provisional` with the reason, stop.
5. Grade per concept:
   - Tested: was the concept in a question (directly or as a required part of an answer)?
   - Accuracy 0–3 (tested concepts only).
   - Retention 0–3 — judge from how much prompting the examiner gave before the answer.
   - Evidence: the question and a short quote of the answer.
6. Write to the `Exam Analysis` child page: INSERT a new section at the top (never overwrite older
   sections):

   ```
   ## <marker> — <date> — complete | PROVISIONAL
   Mode: brief-driven | baseline
   | Registry ID | Concept | Tested | Accuracy | Retention | Evidence |
   |---|---|---|---|---|---|
   Errors vs chapter: ...
   Untested concepts: ...
   ```
7. Update the `Next Exam Brief` (status protocol). Compound: keep unresolved targets, drop concepts
   answered at accuracy 3 and retention ≥ 2, add weak ones, schedule untested concepts. Fold in
   PROVISIONAL exam sections newer than the last complete one. Format: ranked target list, each =
   Registry ID, concept, why, and one descriptive question to open with.
8. Update the `Next Teaching Brief` (status protocol) EVERY time, not only on baseline: add concepts
   with accuracy ≤ 1 or retention ≤ 1 as teaching focus items, citing the exam evidence. This is how
   exam gaps reach the very next teaching session.
9. Set chapter `has_exam_session` = true. Sessions row `Status` = `done`, `Note` = one-line summary.

## Guardrails
- Relative to the chapter's concept map. Reward correct depth beyond the source.
- No product/design decisions; follow this spec.
