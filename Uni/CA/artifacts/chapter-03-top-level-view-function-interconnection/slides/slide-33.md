# Slide 33: Control Bus

*Chapter 3 — A Top-Level View of Computer Function and Interconnection*

- Control and timing information
- Memory read/write signal
- Interrupt request
- Clock signals

**If one module wishes to send data to another, it must:**
- obtain the use of the bus, and
- transfer data via the bus

**If one module wishes to request data from another, it must:**
- obtain the use of the bus, and
- transfer a request to the other module over the appropriate control and address lines
- It must then wait for that second module to send the data
