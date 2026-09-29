---
type: concept
parent: "[[Interrupts]]"
depends_on: ["[[Purpose and Classes of Interrupts]]"]
pages: [21, 22, 23]
coverage: 0
---
# Interrupt Flow of Control
**Problem:** How does control actually move between the user program and the I/O device across a WRITE call, with and without interrupts?
**Mechanism:** Without interrupts (Fig 1.5a), the user program issues WRITE and then blocks, waiting synchronously through the I/O command and completion (END) before continuing. With interrupts (Fig 1.5b/1.5c), the user program issues an I/O command and continues executing; when the I/O program signals completion, an interrupt transfers control to an interrupt handler before returning. The gain is larger when the I/O wait is long (Fig 1.5c) versus short (Fig 1.5b), since more useful processor work fits in the wait window.

## Key points
- [ ] Without interrupts, the user program issues a WRITE, then waits idle through the I/O command and END before the next WRITE. (p.21)
- [ ] With interrupts and a short I/O wait, the user program can do a little useful work between issuing the I/O command and being interrupted by the I/O program's completion signal. (p.22)
- [ ] With interrupts and a long I/O wait, the user program can do substantially more useful work before the interrupt arrives, making the benefit of interrupts larger. (p.23)
- [ ] In both interrupt cases, the I/O program signals completion by causing an interrupt that hands control to an interrupt handler. (p.22, p.23)

## Notes
