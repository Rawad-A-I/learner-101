---
type: concept
parent: "[[Interrupts]]"
depends_on: ["[[Interrupt Processing Mechanics]]"]
pages: [30, 31, 32]
coverage: 50
verified: 50
---
# Multiple Interrupts
**Problem:** An interrupt can occur while another interrupt is already being processed (e.g. a communications line and a printer both need attention at once) — the processor needs a policy for this.
**Mechanism:** Two approaches: (1) disable interrupts while an interrupt is being processed, forcing strictly sequential handling (Fig 1.12a), or (2) use a priority scheme, where a higher-priority interrupt can itself interrupt a lower-priority handler, producing nested interrupt processing (Fig 1.12b). Figure 1.13 shows a concrete timeline where printer, communication, and disk interrupt service routines interleave and nest over time.

## Key points
- [ ] Multiple interrupts arise when an interrupt occurs while another is already being processed, e.g. concurrent communications-line and printer activity. (p.30)
- [x] Approach 1: disable interrupts while one is being processed — interrupts queue up and are handled sequentially, in the order they occurred. (p.30, p.31a)
- [x] Approach 2: use a priority scheme, so a higher-priority interrupt can interrupt a lower-priority handler, giving nested interrupt processing. (p.30, p.31b)
- [ ] Figure 1.13 traces a real timeline of printer, communication, and disk interrupt service routines overlapping and nesting. (p.32)

## Exam log
- Exam 1: "Approach 1: disable interrupts while one is being processed — interrupts queue up and are handled sequentially, in the order they occurred. (p.30, p.31a)" - pass
- Exam 1: "Approach 2: use a priority scheme, so a higher-priority interrupt can interrupt a lower-priority handler, giving nested interrupt processing. (p.30, p.31b)" - pass

## Notes
