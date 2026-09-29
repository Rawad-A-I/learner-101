---
type: concept
parent: "[[Memory Hierarchy and Cache]]"
depends_on: ["[[Memory Hierarchy Design Tradeoffs]]"]
pages: [37]
coverage: 33
verified: 33
---
# Locality of Reference
**Problem:** For a good hit ratio to actually be achievable in practice (not just theoretically possible), memory accesses need to be predictable enough to cluster in a small, fast layer.
**Mechanism:** Memory references by the processor tend to cluster. Data is organized so that the percentage of accesses to each successively lower level is substantially less than the level above it, and this clustering principle extends across more than two levels of memory.

## Key points
- [x] Memory references by the processor tend to cluster rather than spread uniformly across the address space. (p.37)
- [ ] Data can be organized so each successively lower memory level sees substantially fewer accesses than the level above it. (p.37)
- [ ] This clustering/locality principle applies across more than two levels of the memory hierarchy, not just a two-level model. (p.37)

## Exam log
- Exam 1: "Memory references by the processor tend to cluster rather than spread uniformly across the address space. (p.37)" - pass

## Notes
