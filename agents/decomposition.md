# AGENT — Decomposition

Read `agents/_common.md` first; everything there applies.

Triggered by a Sessions row with `Type` = `decompose` (created by the decompose-chapter skill).

## Purpose
Turn a chapter's source into an atomic concept map, grounded strictly to the source, without
altering the source.

## Steps
1. Set the Sessions row `Status` = `processing`. Follow its `Chapter` relation to the chapter row.
   Set the chapter's `Decomposition Status` = `running`.
2. Resolve the chapter source (see "Chapter source resolution"). Missing → fail the job and set
   `Decomposition Status` = `failed` with the reason in `Decomposition Note`.
3. Extract atomic concepts. One concept may span several pages/slides; one page may hold several
   concepts. Build a SEPARATE concept-map layer that references back to the source (page/slide
   numbers or section headings). Never edit the source.
4. Concept registry check (cross-chapter identity): for each concept, search the Concept Registry
   for an existing match (same idea, even under a different name or alias). If found, reuse it:
   relate it to this chapter and add any new alias. Only create a new registry row if the concept
   is genuinely new.
5. Quality gate (self-check) — re-read the source against your map and verify:
   - Completeness: no source concept missed.
   - Atomicity: no node is really two or three concepts jammed together.
   - Fidelity: every node traces to the source; nothing invented.
   If any check fails, revise and re-run the gate. Max 3 rounds.
6. Gate passed → write the `Concept Map` child page (replace its content) in this format:

   ```
   Gate: passed (completeness / atomicity / fidelity) — <date>

   | Concept | Registry ID | Role | Source refs |
   |---|---|---|---|
   | <name> | CON-n | core or peripheral | p.3–5, slide 12 |

   ### CON-n — <name>
   Key points:
   - [ ] <key point 1, a checkable claim from the source>
   - [ ] <key point 2>
   Related: CON-m (<why>)
   ```
   Then set the chapter's `Concepts` relation to all concept rows used, `is_decomposed` = true,
   `Decomposition Status` = `passed`, and clear `Decomposition Note`.
7. Gate still failing after 3 rounds, or source genuinely ambiguous → leave `is_decomposed` = false,
   set `Decomposition Status` = `failed`, write why in `Decomposition Note`, and set the Sessions row
   `Status` = `failed` with the same reason.
8. Sessions row `Status` = `done` with a one-line summary (concept count, how many reused).

## Guardrails
- Grounded to source only. No invented concepts.
- If the chapter was already decomposed (re-run), rebuild the map from scratch but keep reusing
  existing registry IDs.
