---
type: concept
parent: "[[Memory Hierarchy and Cache]]"
depends_on: ["[[Basic Hardware Components]]"]
pages: [38, 39]
coverage: 50
verified: 25
---
# Secondary Memory
**Problem:** Main memory is volatile, so the system needs somewhere to keep programs and data persistently, invisibly to most of what's running.
**Mechanism:** Secondary (auxiliary) memory is external and nonvolatile, used to store program and data files. It is invisible to the OS's direct addressing and interacts with other memory management hardware; the processor must still access main memory at least once per instruction cycle, so processor execution is limited by memory cycle time — a constraint the memory hierarchy exploits via a small, fast memory (cache) close to the processor.

## Key points
- [ ] Secondary memory is also called auxiliary memory: external, nonvolatile, and used to store program and data files. (p.38)
- [ ] Secondary memory itself is invisible to the OS's direct instruction-level access; it interacts through other memory management hardware. (p.39)
- [x] The processor must access memory at least once per instruction cycle, so processor execution speed is limited by memory cycle time. (p.39)
- [x] This limitation motivates exploiting the principle of locality with a small, fast memory (cache) rather than relying on main/secondary memory speed alone. (p.39)

## Exam log
- Exam 1: "This limitation motivates exploiting the principle of locality with a small, fast memory (cache) rather than relying on main/secondary memory speed alone. (p.39)" - pass

## Notes
