---
type: concept
parent: "[[Memory Hierarchy and Cache]]"
depends_on: ["[[Basic Hardware Components]]"]
pages: [33, 34, 35, 36]
coverage: 40
verified: 0
---
# Memory Hierarchy Design Tradeoffs
**Problem:** Memory design must balance three competing constraints — how much capacity, how fast, and how expensive — and applications tend to expand to fill whatever capacity is available.
**Mechanism:** Faster access time correlates with greater cost per bit; greater capacity correlates with smaller cost per bit; greater capacity also correlates with slower access speed. No single memory technology optimizes all three, so systems use a hierarchy (Fig 1.14: registers, cache, main memory, disk, optical/tape) that trades decreasing cost per bit and increasing capacity for increasing access time and decreasing access frequency going down the levels. A two-level model (Fig 1.15) shows average access time approaching the faster level's time as the hit ratio (fraction of accesses satisfied by level 1) approaches 1.

## Key points
- [ ] Memory design is constrained by three competing factors: how much capacity, how fast, and how expensive. (p.33)
- [ ] If capacity is available, applications will likely be developed to use it — capacity and cost must still track processor speed. (p.33)
- [x] Faster access time means greater cost per bit; greater capacity means smaller cost per bit but slower access speed. (p.34)
- [x] Going down the memory hierarchy (registers → cache → main memory → storage): cost per bit decreases, capacity increases, access time increases, and frequency of access by the processor decreases. (p.35)
- [ ] In a simple two-level memory, average access time drops toward the faster level's access time as the hit ratio (fraction of accesses satisfied by level 1) increases toward 1. (p.36)

## Exam log
- Exam 1: "Faster access time means greater cost per bit; greater capacity means smaller cost per bit but slower access speed. (p.34)" - fail (said access time and capacity trade off correctly, but couldn't name the third relationship; source says smaller cost per bit correlates with greater capacity, and greater cost per bit correlates with faster access time — the examiner ended up stating this)

## Notes
- Exam 1: shaky - said access time gets faster / capacity gets smaller going toward the CPU (correct), but when asked for the third measurement (cost per bit) could not answer; source says cost per bit is inversely related to capacity and directly related to access speed
