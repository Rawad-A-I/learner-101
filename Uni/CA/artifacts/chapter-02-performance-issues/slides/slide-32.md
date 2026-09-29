# Slide 32: Amdahl's Law - Speedup

*Chapter 2 — Performance Issues*

- Deals with the potential speedup of a program using multiple processors compared to a single

**processor:**
- 𝑆𝑝𝑒𝑒𝑑𝑢𝑝=
- 𝑇𝑖𝑚𝑒𝑡𝑜𝑒𝑥𝑒𝑐𝑢𝑡𝑒𝑝𝑟𝑜𝑔𝑟𝑎𝑚𝑜𝑛𝑎𝑠𝑖𝑛𝑔𝑙𝑒𝑝𝑟𝑜𝑐𝑒𝑠𝑠𝑜𝑟
- 𝑇𝑖𝑚𝑒𝑡𝑜𝑒𝑥𝑒𝑐𝑢𝑡𝑒𝑝𝑟𝑜𝑔𝑟𝑎𝑚𝑜𝑛𝑁𝑝𝑎𝑟𝑎𝑙𝑙𝑒𝑙𝑝𝑟𝑜𝑐𝑒𝑠𝑠𝑜𝑟𝑠
- Let T be the total execution time using a single processor, and f be the proportion of the program

**that can take advantage of multiple cores and N be the number of cores:**
- 𝑆𝑝𝑒𝑒𝑑𝑢𝑝= 𝑇1 −𝑓+ 𝑇𝑓
- 𝑇1 −𝑓+ 𝑇𝑓
- 𝑁
- =
- 1 −𝑓+ 𝑓
- 𝑁
