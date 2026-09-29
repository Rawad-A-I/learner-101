---
type: concept
parent: "[[Interrupts]]"
depends_on: ["[[Instruction Cycle Fetch and Execute]]", "[[Purpose and Classes of Interrupts]]"]
pages: [24, 25]
coverage: 100
---
# Instruction Cycle with Interrupts
**Problem:** The instruction cycle needs a defined point where the processor checks whether an interrupt is pending, without corrupting the instruction currently in progress.
**Mechanism:** Transfer of control (Fig 1.6) happens between a user program instruction at position i and i+1: the interrupt handler runs, then control returns. The extended instruction cycle (Fig 1.7) adds an interrupt stage after fetch and execute: with interrupts disabled during fetch/execute, then enabled, the processor checks for a pending interrupt at the end of the cycle and, if present, initiates the interrupt handler before returning to fetch the next instruction (or HALT).

## Key points
- [x] An interrupt transfers control from the user program (after instruction i) to the interrupt handler, which later returns control to instruction i+1. (p.24)
- [x] The instruction cycle gains a third stage — the interrupt stage — after fetch and execute, where the processor checks for a pending interrupt. (p.25)
- [x] If an interrupt is pending at the check point, the processor initiates the interrupt handler; otherwise it proceeds to fetch the next instruction. (p.25)

## Notes
