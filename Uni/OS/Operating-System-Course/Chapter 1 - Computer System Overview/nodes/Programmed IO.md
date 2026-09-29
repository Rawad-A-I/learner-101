---
type: concept
parent: "[[IO Techniques]]"
depends_on: ["[[Instruction Cycle Fetch and Execute]]"]
pages: [48, 49]
coverage: 100
---
# Programmed I/O
**Problem:** The processor needs some way to carry out an I/O instruction, and the simplest possible approach is a good baseline to compare against.
**Mechanism:** When the processor encounters an I/O-related instruction, it issues a command to the appropriate I/O module. The I/O module performs the requested action and then sets status bits in its I/O status register. The processor periodically polls (checks) that status register until it determines the instruction is complete. This busy-waiting severely degrades overall system performance.

## Key points
- [x] The processor executes an I/O instruction by issuing a command to the appropriate I/O module — this framing applies to all three I/O techniques. (p.48)
- [x] Three techniques exist for I/O operations: programmed I/O, interrupt-driven I/O, and DMA. (p.48)
- [x] In programmed I/O, the I/O module performs the action and sets status bits, while the processor periodically polls that status register until the instruction completes. (p.49)
- [x] Programmed I/O severely degrades overall system performance because the processor busy-waits instead of doing other work. (p.49)

## Notes
