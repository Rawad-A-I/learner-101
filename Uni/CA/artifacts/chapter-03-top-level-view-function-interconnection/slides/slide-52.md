# Slide 52: QPI Link Layer

*Chapter 3 — A Top-Level View of Computer Function and Interconnection*

- Performs two key functions: flow control and error control
- Operate on the level of the flit (flow control unit)
- Each flit consists of a 72- bit message payload and an 8-bit error control code (cyclic
- redundancy check - CRC)
- Flow control function
- Needed to ensure that a sending QPI entity does not overwhelm a receiving QPI entity by
- sending data faster than the receiver can process the data and clear buffers for more
- incoming data
- Error control function
- Detects and recovers from bit errors
