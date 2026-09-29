---
type: concept
parent: "[[Computer System Foundations]]"
depends_on: ["[[Basic Hardware Components]]"]
pages: [7, 8]
coverage: 25
verified: 25
---
# System Bus and Top-Level Organization
**Problem:** The processor, main memory, and I/O modules need a shared communication path.
**Mechanism:** The system bus provides for communication among processors, main memory, and I/O modules. Internally, the CPU exposes registers to this exchange: the program counter (PC), instruction register (IR), memory address register (MAR), memory buffer register (MBR), and I/O address/buffer registers (I/O AR, I/O BR).

## Key points
- [x] The system bus provides communication among processors, main memory, and I/O modules. (p.7)
- [ ] The CPU connects to the bus via MAR (memory address register) and MBR (memory buffer register) for memory access, and I/O AR / I/O BR for I/O access. (p.8)
- [ ] The PC (program counter) and IR (instruction register) are the execution-unit-facing registers shown in the top-level view. (p.8)
- [ ] Figure 1.1 gives the top-level view: CPU, main memory (organized as addressed words/instructions/data), and I/O module all connected via the system bus. (p.8)

## Exam log
- Exam 1: "The system bus provides communication among processors, main memory, and I/O modules. (p.7)" - pass

## Notes
