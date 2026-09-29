---
type: concept
parent: "[[Interrupts]]"
depends_on: ["[[Instruction Cycle with Interrupts]]"]
pages: [28, 29]
coverage: 75
---
# Interrupt Processing Mechanics
**Problem:** When an interrupt fires, the processor must preserve exactly enough state to resume the interrupted program later as if nothing happened.
**Mechanism:** Hardware side (Fig 1.10): a device controller issues an interrupt; the processor finishes the current instruction, signals acknowledgment, pushes the PSW (program status word) and PC onto a control stack, then loads a new PC value based on the interrupt (pointing into the interrupt service routine). Software side: the handler saves the remainder of process state, processes the interrupt, restores process state, then restores the old PSW and PC. Fig 1.11 shows the control stack and general registers changing between "interrupt occurs after instruction at N" and "return from interrupt."

## Key points
- [x] Hardware steps: finish current instruction → signal acknowledgment → push PSW and PC onto the control stack → load new PC pointing to the interrupt service routine. (p.28)
- [x] Software steps: save remaining process state → process the interrupt → restore process state → restore the old PSW and PC. (p.28)
- [x] The processor only switches to the interrupt handler after finishing the instruction it is currently executing, not mid-instruction. (p.28)
- [ ] Figure 1.11 shows the control stack and registers being pushed with (Y, Y+L) values at interrupt time and popped back on return, resuming the user program at N+1. (p.29)

## Notes
