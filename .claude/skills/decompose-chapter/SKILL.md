---
name: decompose-chapter
description: Use when the learner wants to add/decompose a new chapter into the Learner 101 system — e.g. "decompose chapter X". Puts the chapter into Notion and kicks off decomposition into a concept map.
---

# Decompose-Chapter (Learner 101)

## Role
Get the chapter into Notion and trigger decomposition. The reasoning (concept extraction, quality
gate, registry matching) is done afterwards by the local Decomposition agent — not here.

## Notion
- Chapters data source: `collection://7621b84c-72ad-4888-b394-16e29cfda753`
- Sessions data source: `collection://b0a0d8e9-4fc8-4400-b36b-551b117cf12b`

## Steps
1. Confirm the chapter source is in this Claude Project's knowledge. If not, ask him to upload it
   and stop.
2. Pick a `Chapter Key`: short lowercase slug, e.g. `ch03-memory-hierarchy`. Check Chapters for an
   existing row with the same chapter; if one exists, reuse it (this is a re-decomposition).
3. New chapter → create a Chapters row: `Chapter` = chapter title, `Chapter Key`, all three
   checkboxes false, `Decomposition Status` = `pending`, `Teaching Brief Status` = `none`,
   `Exam Brief Status` = `none`. In its page body:
   - `## Source` followed by the FULL chapter text from the project knowledge, faithfully, in
     order, with page/slide numbers as headings (`### p.3` / `### Slide 12`). Describe figures and
     tables in one line each. Don't summarise. If it's long, append in several inserts.
     End the section with the line `=== SOURCE END <chapter-key> ===`.
   - Five empty child pages: `Concept Map`, `Teaching Analysis`, `Exam Analysis`,
     `Next Teaching Brief`, `Next Exam Brief`.
4. Trigger: create a Sessions row with `Marker` = `decompose-<chapter-key>-<YYYYMMDD-HHMMSS>-<6
   random chars>`, `Chapter` = the chapter row, `Type` = `decompose`, `Status` = `queued`. Only
   create it after step 3 is fully written.
5. Tell him: decomposition has started; `is_decomposed` flips true once the quality gate passes,
   usually within a few minutes. He can start a free-run teaching session meanwhile.

## Tip for the learner
Dropping the same PDF into the local `chapters/` folder as `<chapter-key>.pdf` gives the agent the
original file, which beats the text copy.
