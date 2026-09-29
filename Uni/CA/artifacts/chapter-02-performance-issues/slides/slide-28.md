# Slide 28: MIPS Example

*Chapter 2 — Performance Issues*

- Consider the execution of a program that results in the execution of 2 million instructions on a 400-
- MHz processor.
- The program consists of four major types of instructions.
- The instruction mix and the CPI for each instruction type are given below based on the result of a

**program trace experiment:**
- The average CPI = 0.6 + (2 x 0.18) + (4 x 0.12) + (8 x 0.1) = 2.24
- The corresponding MIPS rate is (400 x 106)/(2.24 x 106) ≈178
- Instruction type
- CPI
- Instruction mix (%)
- Arithmetic and logic
- Load/store with cache hit
- Branch
- Memory reference with cache miss
