# Slide 21: Multiple Interrupts

*Chapter 3 — A Top-Level View of Computer Function and Interconnection*

- Disable interrupts
- Processor will ignore further interrupts whilst processing one interrupt
- Interrupts remain pending and are checked after first interrupt has been processed
- Interrupts handled in sequence as they occur
- Define priorities
- Low priority interrupts can be interrupted by higher priority interrupts
- When higher priority interrupt has been processed, processor returns to previous interrupt
