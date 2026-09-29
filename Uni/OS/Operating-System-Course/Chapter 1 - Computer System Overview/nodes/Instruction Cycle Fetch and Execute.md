---
type: concept
parent: "[[Instruction Execution]]"
depends_on: ["[[Basic Hardware Components]]", "[[System Bus and Top-Level Organization]]"]
pages: [13, 14, 15, 16]
coverage: 20
---
# Instruction Cycle: Fetch and Execute
**Problem:** A program is just a set of instructions stored in memory; the processor needs a repeatable procedure to run them in order.
**Mechanism:** Processing happens in two steps per instruction: the processor reads (fetches) an instruction from memory, then executes it. The program counter (PC) holds the address of the next instruction to fetch and is incremented after each fetch. The fetched instruction is loaded into the instruction register (IR); the processor interprets it and performs the required action — categorized as processor-memory, processor-I/O, data processing, or control.

## Key points
- [/] A program consists of a set of instructions stored in memory, executed via two steps: fetch, then execute. (p.13)
- [ ] Figure 1.2 shows the basic instruction cycle as fetch-stage → execute-stage, looping from START to HALT. (p.14)
- [x] The PC (program counter) holds the address of the next instruction to be fetched and is incremented after each fetch. (p.15)
- [ ] The fetched instruction is loaded into the instruction register (IR); the processor then interprets and executes it. (p.16)
- [ ] Executed instructions fall into four categories of required action: processor-memory, processor-I/O, data processing, and control. (p.16)

## Notes
- Session 1: shaky - teacher taught a 4-stage fetch/decode/execute/write-back cycle; this chapter's own model is the simpler two-step fetch-then-execute cycle (p.13, Fig 1.2). Not wrong for OS generally, but doesn't match this chapter's stated framing — worth reconciling next session.
