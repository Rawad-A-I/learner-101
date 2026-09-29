# Slide 35: CISC vs RISC

*Chapter 1 — Basic Concepts & Computer Evolution*

- CISC: Complex Instruction Set Computers
- E.g. Intel's x86
- RISC: Reduced Instruction Set Computers
- E.g. ARM architecture
- Consider the high level statement: A = B + C
- On a typical CISC machine: add mem(A), mem(B), mem(C)

**On a typical RISC machine:**
- load mem(B), reg(1)
- load mem(C), reg(2)
- add reg(1), reg(1), reg(2)
- store reg(1), mem(A)
