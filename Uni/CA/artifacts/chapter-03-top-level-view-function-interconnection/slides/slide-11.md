# Slide 11: Multiple Memory Access

*Chapter 3 — A Top-Level View of Computer Function and Interconnection*

- The execute cycle may involve more than one memory access
- For example the PDP-11 includes the instruction ADD B, A
- PDP-11 has multiple registers rather than a single accumulator

**The instruction cycle would look like this:**
- Fetch the instruction ADD B, A
- Read the contents of memory location A into a register
- Read the contents of memory location B into a different register
- Add the two values
- Write the result from the processor to memory location A
- This results in a more complicated execute cycle
