---
type: concept
parent: "[[Multiprocessing and Multicore]]"
depends_on: ["[[Basic Hardware Components]]"]
pages: [54, 55, 56]
coverage: 0
---
# Symmetric Multiprocessors (SMP)
**Problem:** A single processor caps performance and creates a single point of failure; a system may want several processors cooperating as one machine.
**Mechanism:** An SMP is a stand-alone computer system with: two or more similar processors of comparable capability, processors sharing the same main memory and interconnected by a bus (Fig 1.19 shows per-processor L1/L2 caches plus a shared system bus, main memory, and I/O adapters), processors sharing access to I/O devices, all processors able to perform the same functions, and one integrated OS controlling interaction between processors and their programs at the job, task, file, and data element levels. Benefits: performance (parallel work speeds up), availability (a single processor's failure doesn't halt the machine), incremental growth (add a processor to boost performance), and scaling (vendors offer a price/performance range).

## Key points
- [ ] An SMP has two or more similar, comparable-capability processors sharing the same main memory, interconnected by a bus, and sharing access to I/O devices. (p.54)
- [ ] All processors in an SMP can perform the same functions, and one integrated OS controls interaction between processors and programs down to the job, task, file, and data element level. (p.54)
- [ ] Performance benefit: work done in parallel across processors yields greater performance. (p.55)
- [ ] Availability benefit: the failure of a single processor does not halt the machine. (p.55)
- [ ] Incremental growth: an additional processor can be added to enhance performance; scaling: vendors can offer a range of products at different price/performance points. (p.55)
- [ ] Figure 1.19 shows each processor with its own L1/L2 cache, all connected via a shared system bus to main memory and I/O adapters/subsystem. (p.56)

## Notes
