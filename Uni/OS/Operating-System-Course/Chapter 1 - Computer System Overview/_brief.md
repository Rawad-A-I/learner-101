# Session Brief - Chapter 1 - Computer System Overview - Session 2
Mode: directed
Progress: 37% covered

## Plan (in order)
1. Memory Hierarchy Design Tradeoffs (revisit - failed exam 1) - open key points:
   - Faster access time means greater cost per bit; greater capacity means smaller cost per bit but slower access speed. (p.34)
   Revisit: shaky - got access-time/capacity right, couldn't name the cost-per-bit relationship; examiner ended up stating it
2. Instruction Cycle: Fetch and Execute (revisit - shaky) - open key points:
   - A program consists of a set of instructions stored in memory, executed via two steps: fetch, then execute. (p.13)
   - Figure 1.2 shows the basic instruction cycle as fetch-stage → execute-stage, looping from START to HALT. (p.14)
   - The fetched instruction is loaded into the instruction register (IR); the processor then interprets and executes it. (p.16)
   - Executed instructions fall into four categories of required action: processor-memory, processor-I/O, data processing, and control. (p.16)
   Revisit: shaky - taught a 4-stage fetch/decode/execute/write-back cycle instead of this chapter's simpler two-step fetch-then-execute model; needs re-grounding in the actual p.13/Fig 1.2 framing
3. Multicore Computers (revisit - shaky) - open key points:
   - A multicore computer, also called a chip multiprocessor, combines two or more cores on a single die. (p.57)
   - Each core includes all the components of an independent processor. (p.57)
   - Multicore chips also include L2 cache, and in some cases L3 cache, shared across cores on the chip. (p.57)
   Revisit: shaky - teacher said multicore isn't a deep focus of this chapter, which is wrong; needs a real pass grounded in p.57 and the SMP material around it
4. What an Operating System Does (revisit - under-engaged) - open key points:
   - The OS exploits the hardware resources of one or more processors. (p.2)
   - The OS provides a set of services to system users. (p.2)
   - The OS manages secondary memory and I/O devices. (p.2)
   Revisit: mentioned only - stated in the opening seed but the learner moved straight past it without engaging

## Already covered - do not re-seed
- Instruction Cycle with Interrupts, Programmed I/O, Interrupt-Driven I/O, Direct Memory Access

## Notes
- Threads the learner cared about: kept pushing on "is this a thread, an instruction, or a command?" across DMA and I/O techniques — wants precise vocabulary for where each piece of a mechanism lives (instruction vs. hardware-level action). Also pushed back hard and correctly on a cache-management claim (CPU vs cache controller vs OS) until it was resolved.
- Tangents worth queueing (outside this chapter, but the learner is clearly curious): threads vs. processes, multithreading vs. multiprocessing, OS scheduling and priority, context switching mechanics. Not this chapter's material — worth flagging as a preview for whichever later chapter covers processes/threads.
