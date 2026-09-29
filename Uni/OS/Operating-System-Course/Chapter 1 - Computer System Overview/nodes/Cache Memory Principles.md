---
type: concept
parent: "[[Memory Hierarchy and Cache]]"
depends_on: ["[[Memory Hierarchy Design Tradeoffs]]", "[[Locality of Reference]]"]
pages: [40, 41, 42]
coverage: 75
---
# Cache Memory Principles
**Problem:** Main memory is too slow relative to the processor; a fast intermediate memory is needed, but it must stay small (and thus cheap) to be fast.
**Mechanism:** Cache sits between the CPU and main memory, transferring data in blocks (not single words) to exploit locality (Fig 1.16) — real systems often use multiple cache levels (L1 fastest/smallest, L2, L3) trading speed for capacity. Structurally (Fig 1.17), main memory is divided into blocks, and each cache line holds a tag plus one block's worth of words. A cache read (Fig 1.18) checks whether the block containing the requested address is already in cache: on a hit, the word is fetched and delivered directly; on a miss, the whole block is fetched from main memory into a cache slot before delivering the word.

## Key points
- [x] Data moves between cache and main memory in blocks, not single words, so nearby future references (exploiting locality) are already cached. (p.40)
- [x] Multi-level cache organizations (L1/L2/L3) trade off fastest-but-smallest (L1) against slower-but-larger (L3) before reaching main memory. (p.40)
- [ ] Main memory is structured as M blocks; each cache line stores a tag identifying which block it holds plus that block's words (Fig 1.17). (p.41)
- [x] On a cache read: if the block containing the requested address is in cache, the word is fetched and delivered to the CPU directly (hit); if not (miss), the block is loaded into a cache slot from main memory first, then the word is delivered. (p.42)

## Notes
