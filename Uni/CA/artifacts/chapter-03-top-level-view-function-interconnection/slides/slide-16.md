# Slide 16: Interrupt Cycle

*Chapter 3 — A Top-Level View of Computer Function and Interconnection*

- Added to instruction cycle
- Processor checks for interrupt
- Indicated by an interrupt signal
- If no interrupt, fetch next instruction

**If interrupt pending:**
- Suspend execution of current program
- Save context
- Set PC to start address of interrupt handler routine
- Process interrupt
- Restore context and continue interrupted program
