---
type: concept
parent: "[[IO Techniques]]"
depends_on: ["[[Interrupt-Driven IO]]"]
pages: [52, 53]
coverage: 100
verified: 50
---
# Direct Memory Access (DMA)
**Problem:** Even interrupt-driven I/O still ties up the processor for every word transferred; large block transfers need the processor out of the loop almost entirely.
**Mechanism:** DMA is performed by a separate module on the system bus (or built into an I/O module). The processor issues one command to the DMA module specifying read/write, the I/O device address, the starting memory location, and the number of words to transfer. The DMA module then transfers the entire block of data directly to/from memory without going through the processor; the processor is involved only at the beginning and end of the transfer (and runs slightly slower during the transfer only when it needs bus access). This makes DMA more efficient than both interrupt-driven and programmed I/O.

## Key points
- [x] DMA is handled by a separate module on the system bus, or built into an I/O module, rather than by the processor executing each transfer step. (p.52)
- [x] To start a DMA transfer, the processor issues one command specifying read/write, the I/O device address, the starting memory location, and the number of words to transfer. (p.52)
- [x] DMA transfers the entire block of data directly to/from memory without going through the processor; the processor is involved only at the beginning and end of the transfer. (p.53)
- [x] Processor execution is only slowed during a DMA transfer when the processor itself needs bus access, and overall DMA is more efficient than interrupt-driven or programmed I/O. (p.53)

## Exam log
- Exam 1: "DMA is handled by a separate module on the system bus, or built into an I/O module, rather than by the processor executing each transfer step. (p.52)" - pass
- Exam 1: "DMA transfers the entire block of data directly to/from memory without going through the processor; the processor is involved only at the beginning and end of the transfer. (p.53)" - pass

## Notes
