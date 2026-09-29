---
type: concept
parent: "[[Interrupts]]"
depends_on: ["[[Interrupt Flow of Control]]"]
pages: [26, 27]
coverage: 0
---
# Interrupt Timing and Processor Utilization
**Problem:** Does letting the processor keep working during an I/O wait actually pay off, and does it depend on how long the I/O takes?
**Mechanism:** Figures 1.8 (short I/O wait) and 1.9 (long I/O wait) compare timing diagrams with and without interrupts. Without interrupts, the processor sits idle for the full duration of each I/O operation. With interrupts, the I/O operation runs concurrently with the processor executing other work, so the processor is only pulled away briefly to handle the interrupt itself.

## Key points
- [ ] With a short I/O wait (Fig 1.8), interrupts let I/O happen concurrently with processor execution, rather than the processor idling for the wait. (p.26)
- [ ] With a long I/O wait (Fig 1.9), the same concurrency principle yields a proportionally larger time saving since more processor idle time is reclaimed. (p.27)
- [ ] In both cases, "without interrupts" means the processor waits for the I/O operation to complete before doing anything else. (p.26, p.27)

## Notes
