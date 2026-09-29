---
type: concept
parent: "[[Multiprocessing and Multicore]]"
depends_on: ["[[Symmetric Multiprocessors]]"]
pages: [57]
coverage: 0
---
# Multicore Computers
**Problem:** SMP puts multiple full processors in a system connected by a bus; integrating multiple processors onto one physical chip pushes the same idea further, cutting interconnect distance and cost.
**Mechanism:** A multicore computer (also called a chip multiprocessor) combines two or more processors (cores) on a single piece of silicon (die). Each core has all the components of an independent processor. Multicore chips additionally include shared L2 cache, and in some cases L3 cache, across the cores on the die.

## Key points
- [/] A multicore computer, also called a chip multiprocessor, combines two or more cores on a single die. (p.57)
- [/] Each core includes all the components of an independent processor. (p.57)
- [ ] Multicore chips also include L2 cache, and in some cases L3 cache, shared across cores on the chip. (p.57)

## Notes
- Session 1: shaky - teacher said multicore "might be touched on briefly in Chapter 1, but it's not a deep focus... comes later in the book," which is wrong: this chapter has a dedicated multicore section (p.57) right alongside SMP (p.54-56, Fig 1.19). Teacher answered from general knowledge instead of checking the actual chapter content — worth re-grounding next session with the real SMP/multicore material.
