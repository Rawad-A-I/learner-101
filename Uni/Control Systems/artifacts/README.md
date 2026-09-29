# ELE 442 Control Systems — Agentic Artifacts

Each PowerPoint is extracted into its **own isolated folder**. No shared slide/index pools.

## Layout

```
artifacts/
  manifest.yaml                          # pointers only
  decks/
    01-ELE442_Topic1_Introduction/       # ← one PPT, fully self-contained
      deck.meta.yaml
      slides.jsonl
      notes.jsonl
      knowledge.md
      completeness.md
      index/{concepts,formulas,glossary}.jsonl
      media/
    02-ELE442_Topic2_Mathematical_Models_Laplace/
    03-ELE442_Topic3_Transfer_Functions_Block_Diagrams/
  extraction/extract_pptx.py
```

## Per-deck entry

1. Open that deck’s folder under `decks/`.
2. `slides.jsonl` = canonical parse unit for that PPT only.
3. Use that deck’s `index/` — not another deck’s.

## Regenerate

```bash
python artifacts/extraction/extract_pptx.py
```
