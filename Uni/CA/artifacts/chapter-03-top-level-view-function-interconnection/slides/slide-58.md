# Slide 58: PCIe Layers

*Chapter 3 — A Top-Level View of Computer Function and Interconnection*

- Sends packets between two devices
- Adds error checking and address bits to each
- TLP to ensure they arrive at the correct
- device

**Packets fall into the following categories:**
- Flow control - regulate the rate at which
- TLPs and DLLPs can be transmitted
- Power management - manage power
- platform budgeting
- ACK - acknowledge the receipt of a valid
- data packet
- NAK - acknowledge the receipt of an
- invalid data packet; the packet must be
- resent
- Receives read and write requests from the
- software above the TL and creates request
- packets for transmission to a destination via the
- link layer
- Most transactions use a split transaction
- technique
- A request packet is sent out by a source
- PCIe device which then waits for a
- response
- TL messages and some write transactions are
- posted transactions (meaning that no response
- is expected)
- TL packet format supports 32-bit memory
- addressing and extended 64-bit memory
- addressing
- Data Link Layer
- Transaction Layer
