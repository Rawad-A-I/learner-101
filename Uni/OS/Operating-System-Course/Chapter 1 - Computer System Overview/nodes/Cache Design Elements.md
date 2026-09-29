---
type: concept
parent: "[[Memory Hierarchy and Cache]]"
depends_on: ["[[Cache Memory Principles]]"]
pages: [43, 44, 45, 46, 47]
coverage: 20
verified: 20
---
# Cache Design Elements
**Problem:** Building a cache means making several coupled design decisions, each with its own cost/benefit tradeoff.
**Mechanism:** Key design elements: cache size (small caches significantly impact performance), block size (the unit of data exchanged between cache and main memory), mapping function (determines which cache location a block occupies — more flexible mapping needs more complex search circuitry), replacement algorithm (e.g. LRU: replace the block that's gone longest without a reference, needing hardware to track recency), and write policy (when writes propagate to main memory — every update vs. only on replacement, trading fewer writes against main memory being temporarily obsolete).

## Key points
- [ ] The main cache design categories are: cache size, block size, mapping function, replacement algorithm, write policy, and number of cache levels. (p.43)
- [/] Small caches have a significant impact on performance; block size is the unit of data exchanged between cache and main memory. (p.44)
- [ ] The mapping function determines which cache location a block occupies; more flexible mapping functions require more complex circuitry to search the cache. (p.45)
- [x] When a new block must be loaded and the cache is full, the replacement algorithm chooses which existing block to evict — LRU (Least Recently Used) replaces the block that's gone longest without a reference, requiring hardware to track recency. (p.46)
- [ ] The write policy dictates when a memory write actually happens: on every update (safer, more writes) or only when the block is replaced (minimizes writes but leaves main memory obsolete in the meantime). (p.47)

## Exam log
- Exam 1: "When a new block must be loaded and the cache is full, the replacement algorithm chooses which existing block to evict — LRU (Least Recently Used) replaces the block that's gone longest without a reference, requiring hardware to track recency. (p.46)" - pass

## Notes
