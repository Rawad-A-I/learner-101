---
type: concept
parent: "[[IO Techniques]]"
depends_on: ["[[Purpose and Classes of Interrupts]]", "[[Programmed IO]]"]
pages: [50, 51]
coverage: 100
---
# Interrupt-Driven I/O
**Problem:** Programmed I/O wastes the processor on busy-waiting; the processor should be able to do other useful work while I/O is in progress.
**Mechanism:** The processor issues an I/O command to a module and then goes on to do other useful work instead of polling. The I/O module interrupts the processor to request service when it's ready to exchange data; the processor then executes the data transfer and resumes its former processing. It's more efficient than programmed I/O, but still requires active processor intervention to move each unit of data between memory and the I/O module — a drawback that limits transfer rate to how fast the processor can test and service the device, and ties up the processor in executing instructions for each I/O transfer.

## Key points
- [x] The processor issues an I/O command then goes on to do other useful work, instead of polling as in programmed I/O. (p.50)
- [x] The I/O module interrupts the processor when ready to exchange data; the processor executes the transfer, then resumes its former processing. (p.50)
- [x] Interrupt-driven I/O is more efficient than programmed I/O, but still requires active processor intervention to actually move the data. (p.50)
- [x] Drawback: transfer rate is limited by how fast the processor can test and service a device, and a number of instructions must execute for each I/O transfer. (p.51)

## Notes
