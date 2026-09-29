# Slide 24: I/O Function

*Chapter 3 — A Top-Level View of Computer Function and Interconnection*

- An I/O module (e.g., a disk controller) can exchange data directly with the processor
- Processor can read data from or write data to an I/O module
- Processor identifies a specific device that is controlled by a particular I/O module
- I/O instructions rather than memory referencing instructions
- In some cases it is desirable to allow I/O exchanges to occur directly with memory
- The processor grants to an I/O module the authority to read from or write to memory so that
- the I/O memory transfer can occur without tying up the processor
- The I/O module issues read or write commands to memory relieving the processor of
- responsibility for the exchange
- This is known as direct memory access (DMA)
