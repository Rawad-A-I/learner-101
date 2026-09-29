# Topic 3: Transfer Functions & Block Diagrams

Source: `ELE442_Topic3_Transfer_Functions_and_Block_Diagrams (1).pptx`
Slides: 96 · Notes: 90 · Media refs: 285

## Learning map

- **formula**: 47 slides
- **example**: 26 slides
- **derivation**: 13 slides
- **diagram**: 7 slides
- **content**: 1 slides
- **definition**: 1 slides
- **figure**: 1 slides

## Slide knowledge cards

### t03-s001 — ELE 442 – Control Systems

Tags: content

Content:
- ELE 442 – Control Systems
- Topic 3: Transfer Functions & Block Diagrams

---

### t03-s002 — 𝑇𝐹=𝐺(𝑠)=(ℒ(𝑜𝑢𝑡𝑝𝑢𝑡))/(ℒ(𝑖𝑛𝑝𝑢𝑡))          𝐼𝐶=0 𝑇𝐹=𝐺(𝑠)=(ℒ(𝑜𝑢𝑡𝑝𝑢𝑡))/(ℒ(𝑖𝑛𝑝𝑢𝑡))          𝐼𝐶=0

Tags: definition, formula, figure

Content:
- 𝑇𝐹=𝐺(𝑠)=(ℒ(𝑜𝑢𝑡𝑝𝑢𝑡))/(ℒ(𝑖𝑛𝑝𝑢𝑡))          𝐼𝐶=0 𝑇𝐹=𝐺(𝑠)=(ℒ(𝑜𝑢𝑡𝑝𝑢𝑡))/(ℒ(𝑖𝑛𝑝𝑢𝑡))          𝐼𝐶=0
- TF is defined for Linear Time-Invariant systems.
- No info about the physical structure of the system.
- TF of spring-mass-damper system
- 𝑀𝑠^{2}𝑌(𝑠)+𝑏𝑠𝑌(𝑠)+𝑘𝑌(𝑠)=𝑅(𝑠)𝑀𝑠^{2}𝑌(𝑠)+𝑏𝑠𝑌(𝑠)+𝑘𝑌(𝑠)=𝑅(𝑠)
- is 𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(1)/(𝑀𝑠^{2}+𝑏𝑠+𝑘)
- Transfer Function

Equations / relations:
- `𝑇𝐹=𝐺(𝑠)=(ℒ(𝑜𝑢𝑡𝑝𝑢𝑡))/(ℒ(𝑖𝑛𝑝𝑢𝑡)) 𝐼𝐶=0`
- `𝑀𝑠^{2}𝑌(𝑠)+𝑏𝑠𝑌(𝑠)+𝑘𝑌(𝑠)=𝑅(𝑠)`
- `𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(1)/(𝑀𝑠^{2}+𝑏𝑠+𝑘)`
- `𝑇𝐹=𝐺(𝑠)=(ℒ(𝑜𝑢𝑡𝑝𝑢𝑡))/(ℒ(𝑖𝑛𝑝𝑢𝑡))          𝐼𝐶=0 𝑇𝐹=𝐺(𝑠)=(ℒ(𝑜𝑢𝑡𝑝𝑢𝑡))/(ℒ(𝑖𝑛𝑝𝑢𝑡))          𝐼𝐶=0`
- `𝑀𝑠^{2}𝑌(𝑠)+𝑏𝑠𝑌(𝑠)+𝑘𝑌(𝑠)=𝑅(𝑠)𝑀𝑠^{2}𝑌(𝑠)+𝑏𝑠𝑌(𝑠)+𝑘𝑌(𝑠)=𝑅(𝑠)`
- `is 𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(1)/(𝑀𝑠^{2}+𝑏𝑠+𝑘)`

Media:
- `media/image2.png`

---

### t03-s003 — Transfer Function

Tags: formula, figure

Content:
- Transfer Function
- If a transfer function is known, the output can be known for a variety of inputs.
- If a transfer function of a system is unknown, it may be determined experimentally by introducing known inputs and studying the output of the system.
- A transfer function gives a full description of the dynamic characteristics of the system.
- 𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))
- G(s)
- R(s)
- Y(s)

Equations / relations:
- `𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))`
- `𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))`
- `G(s)`
- `R(s)`
- `Y(s)`

Media:
- `media/image3.png`

---

### t03-s004 — Given the ODE:

Tags: example, formula, figure

Content:
- Given the ODE:
- (𝑑^{𝑛}𝑦(𝑡))/(𝑑𝑡^{𝑛})+𝑞_{𝑛−1}(𝑑^{𝑛−1}𝑦(𝑡))/(𝑑𝑡^{𝑛−1})+…+𝑞_{0}𝑦(𝑡)(𝑑^{𝑛}𝑦(𝑡))/(𝑑𝑡^{𝑛})+𝑞_{𝑛−1}(𝑑^{𝑛−1}𝑦(𝑡))/(𝑑𝑡^{𝑛−1})+…+𝑞_{0}𝑦(𝑡)
- =𝑝_{𝑛−1}(𝑑^{𝑛−1}𝑟(𝑡))/(𝑑𝑡^{𝑛−1})+𝑝_{𝑛−2}(𝑑^{𝑛−2}𝑟(𝑡))/(𝑑𝑡^{𝑛−2})+…+𝑝_{0}𝑟(𝑡)=𝑝_{𝑛−1}(𝑑^{𝑛−1}𝑟(𝑡))/(𝑑𝑡^{𝑛−1})+𝑝_{𝑛−2}(𝑑^{𝑛−2}𝑟(𝑡))/(𝑑𝑡^{𝑛−2})+…+𝑝_{0}𝑟(𝑡)
- If 𝐼𝐶=0  𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑝(𝑠))/(𝑞(𝑠))=(𝑝_{𝑛−1}𝑠^{𝑛−1}+𝑝_{𝑛−2}𝑠^{𝑛−2}+…+𝑝_{0})/(𝑠^{𝑛}+𝑞_{𝑛−1}𝑠^{𝑛−1}+…+𝑞_{0})
- Transfer Function – Generic Example

Equations / relations:
- `(𝑑^{𝑛}𝑦(𝑡))/(𝑑𝑡^{𝑛})+𝑞_{𝑛−1}(𝑑^{𝑛−1}𝑦(𝑡))/(𝑑𝑡^{𝑛−1})+…+𝑞_{0}𝑦(𝑡)`
- `=𝑝_{𝑛−1}(𝑑^{𝑛−1}𝑟(𝑡))/(𝑑𝑡^{𝑛−1})+𝑝_{𝑛−2}(𝑑^{𝑛−2}𝑟(𝑡))/(𝑑𝑡^{𝑛−2})+…+𝑝_{0}𝑟(𝑡)`
- `𝐼𝐶=0`
- `𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑝(𝑠))/(𝑞(𝑠))=(𝑝_{𝑛−1}𝑠^{𝑛−1}+𝑝_{𝑛−2}𝑠^{𝑛−2}+…+𝑝_{0})/(𝑠^{𝑛}+𝑞_{𝑛−1}𝑠^{𝑛−1}+…+𝑞_{0})`
- `=𝑝_{𝑛−1}(𝑑^{𝑛−1}𝑟(𝑡))/(𝑑𝑡^{𝑛−1})+𝑝_{𝑛−2}(𝑑^{𝑛−2}𝑟(𝑡))/(𝑑𝑡^{𝑛−2})+…+𝑝_{0}𝑟(𝑡)=𝑝_{𝑛−1}(𝑑^{𝑛−1}𝑟(𝑡))/(𝑑𝑡^{𝑛−1})+𝑝_{𝑛−2}(𝑑^{𝑛−2}𝑟(𝑡))/(𝑑𝑡^{𝑛−2})+…+𝑝_{0}𝑟(𝑡)`
- `If 𝐼𝐶=0  𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑝(𝑠))/(𝑞(𝑠))=(𝑝_{𝑛−1}𝑠^{𝑛−1}+𝑝_{𝑛−2}𝑠^{𝑛−2}+…+𝑝_{0})/(𝑠^{𝑛}+𝑞_{𝑛−1}𝑠^{𝑛−1}+…+𝑞_{0})`

Media:
- `media/image4.png`

---

### t03-s005 — Output response = natural response (determined by the initial conditions) + forced response (determined by the input)

Tags: example, formula, figure

Content:
- Output response = natural response (determined by the initial conditions) + forced response (determined by the input)
- 𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))𝑅(𝑠)𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))𝑅(𝑠)
- Transfer Function – Generic Example

Equations / relations:
- `𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))𝑅(𝑠)`
- `Output response = natural response (determined by the initial conditions) + forced response (determined by the input)`
- `𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))𝑅(𝑠)𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))𝑅(𝑠)`

Media:
- `media/image5.png`

---

### t03-s006 — If 𝑅(𝑠)=(𝑛(𝑠))/(𝑑(𝑠)) then 𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))(𝑛(𝑠))/(𝑑(𝑠))=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)

Tags: example, formula, figure

Content:
- If 𝑅(𝑠)=(𝑛(𝑠))/(𝑑(𝑠)) then 𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))(𝑛(𝑠))/(𝑑(𝑠))=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)
- 𝑌_{1}(𝑠) is the partial fraction expansion of the natural response
- 𝑌_{2}(𝑠) is the partial fraction expansion of the terms involving factors of 𝑞(𝑠)
- 𝑌_{3}(𝑠) is the partial fraction expansion of terms involving factors of 𝑑(𝑠)
- ℒ^{−1}  𝑦(𝑡)=𝑦_{1}(𝑡)+𝑦_{2}(𝑡)+𝑦_{3}(𝑡)
- transient response
- steady-state response
- Transfer Function – Generic Example

Equations / relations:
- `𝑅(𝑠)=(𝑛(𝑠))/(𝑑(𝑠))`
- `𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))(𝑛(𝑠))/(𝑑(𝑠))=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)`
- `𝑌_{1}(𝑠)`
- `𝑌_{2}(𝑠)`
- `𝑞(𝑠)`
- `𝑌_{3}(𝑠)`
- `𝑑(𝑠)`
- `ℒ^{−1}`
- `𝑦(𝑡)=𝑦_{1}(𝑡)+𝑦_{2}(𝑡)+𝑦_{3}(𝑡)`
- `If 𝑅(𝑠)=(𝑛(𝑠))/(𝑑(𝑠)) then 𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))(𝑛(𝑠))/(𝑑(𝑠))=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)`
- `ℒ^{−1}  𝑦(𝑡)=𝑦_{1}(𝑡)+𝑦_{2}(𝑡)+𝑦_{3}(𝑡)`

Media:
- `media/image6.png`

---

### t03-s007 — Given the ODE: (𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+4(𝑑𝑦(𝑡))/(𝑑𝑡)+3𝑦(𝑡)=2𝑟(𝑡)

Tags: example, formula, figure

Content:
- Given the ODE: (𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+4(𝑑𝑦(𝑡))/(𝑑𝑡)+3𝑦(𝑡)=2𝑟(𝑡)
- With Initial Conditions: 𝑦(0)=1,   (𝑑𝑦)/(𝑑𝑡)(0)=0,    𝑟(𝑡)=1,    𝑡≥0
- Laplace Transform:
- (𝑠^{2}𝑌(𝑠)−𝑠𝑦(0))+4(𝑠𝑌(𝑠)−𝑦(0))+3𝑌(𝑠)=2𝑅(𝑠)(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0))+4(𝑠𝑌(𝑠)−𝑦(0))+3𝑌(𝑠)=2𝑅(𝑠)
- 𝑌(𝑠)=(𝑠+4)/(𝑠^{2}+4𝑠+3)+(2)/(𝑠(𝑠^{2}+4𝑠+3))𝑌(𝑠)=(𝑠+4)/(𝑠^{2}+4𝑠+3)+(2)/(𝑠(𝑠^{2}+4𝑠+3))
- Solving an ODE – Numeric Example

Equations / relations:
- `(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+4(𝑑𝑦(𝑡))/(𝑑𝑡)+3𝑦(𝑡)=2𝑟(𝑡)`
- `𝑦(0)=1, (𝑑𝑦)/(𝑑𝑡)(0)=0, 𝑟(𝑡)=1, 𝑡≥0`
- `(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0))+4(𝑠𝑌(𝑠)−𝑦(0))+3𝑌(𝑠)=2𝑅(𝑠)`
- `𝑌(𝑠)=(𝑠+4)/(𝑠^{2}+4𝑠+3)+(2)/(𝑠(𝑠^{2}+4𝑠+3))`
- `Given the ODE: (𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+4(𝑑𝑦(𝑡))/(𝑑𝑡)+3𝑦(𝑡)=2𝑟(𝑡)`
- `With Initial Conditions: 𝑦(0)=1,   (𝑑𝑦)/(𝑑𝑡)(0)=0,    𝑟(𝑡)=1,    𝑡≥0`
- `(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0))+4(𝑠𝑌(𝑠)−𝑦(0))+3𝑌(𝑠)=2𝑅(𝑠)(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0))+4(𝑠𝑌(𝑠)−𝑦(0))+3𝑌(𝑠)=2𝑅(𝑠)`
- `𝑌(𝑠)=(𝑠+4)/(𝑠^{2}+4𝑠+3)+(2)/(𝑠(𝑠^{2}+4𝑠+3))𝑌(𝑠)=(𝑠+4)/(𝑠^{2}+4𝑠+3)+(2)/(𝑠(𝑠^{2}+4𝑠+3))`

Media:
- `media/image7.png`

---

### t03-s008 — Laplace Transform:

Tags: example, formula, figure

Content:
- Laplace Transform:
- (𝑠^{2}𝑌(𝑠)−𝑠𝑦(0))+4(𝑠𝑌(𝑠)−𝑦(0))+3𝑌(𝑠)=2𝑅(𝑠)(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0))+4(𝑠𝑌(𝑠)−𝑦(0))+3𝑌(𝑠)=2𝑅(𝑠)
- 𝑌(𝑠)=(𝑠+4)/(𝑠^{2}+4𝑠+3)+(2)/(𝑠(𝑠^{2}+4𝑠+3))𝑌(𝑠)=(𝑠+4)/(𝑠^{2}+4𝑠+3)+(2)/(𝑠(𝑠^{2}+4𝑠+3))
- Where 𝑞(𝑠)=𝑠^{2}+4𝑠+3=(𝑠+1)(𝑠+3)=0 is the characteristic equation
- 𝑑(𝑠)𝑑(𝑠)
- 𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))(𝑛(𝑠))/(𝑑(𝑠))=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))(𝑛(𝑠))/(𝑑(𝑠))=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)
- Solving an ODE – Numeric Example

Equations / relations:
- `(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0))+4(𝑠𝑌(𝑠)−𝑦(0))+3𝑌(𝑠)=2𝑅(𝑠)`
- `𝑌(𝑠)=(𝑠+4)/(𝑠^{2}+4𝑠+3)+(2)/(𝑠(𝑠^{2}+4𝑠+3))`
- `𝑞(𝑠)=𝑠^{2}+4𝑠+3=(𝑠+1)(𝑠+3)=0`
- `𝑑(𝑠)`
- `𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))(𝑛(𝑠))/(𝑑(𝑠))=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)`
- `(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0))+4(𝑠𝑌(𝑠)−𝑦(0))+3𝑌(𝑠)=2𝑅(𝑠)(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0))+4(𝑠𝑌(𝑠)−𝑦(0))+3𝑌(𝑠)=2𝑅(𝑠)`
- `𝑌(𝑠)=(𝑠+4)/(𝑠^{2}+4𝑠+3)+(2)/(𝑠(𝑠^{2}+4𝑠+3))𝑌(𝑠)=(𝑠+4)/(𝑠^{2}+4𝑠+3)+(2)/(𝑠(𝑠^{2}+4𝑠+3))`
- `Where 𝑞(𝑠)=𝑠^{2}+4𝑠+3=(𝑠+1)(𝑠+3)=0 is the characteristic equation`
- `𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))(𝑛(𝑠))/(𝑑(𝑠))=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))(𝑛(𝑠))/(𝑑(𝑠))=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)`

Media:
- `media/image8.png`
- `media/image9.png`
- `media/image910.png`

---

### t03-s009 — Partial Fraction Expansion

Tags: example, figure

Content:
- Partial Fraction Expansion
- 𝑌(𝑠)=((3/2)/(𝑠+1)+(−1/2)/(𝑠+3))+((−1)/(𝑠+1)+(1/3)/(𝑠+3))+(2/3)/(𝑠)=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)𝑌(𝑠)=((3/2)/(𝑠+1)+(−1/2)/(𝑠+3))+((−1)/(𝑠+1)+(1/3)/(𝑠+3))+(2/3)/(𝑠)=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)
- The response: 𝑦(𝑡)=((3)/(2)𝑒^{−𝑡}−(1)/(2)𝑒^{−3𝑡})+(−1𝑒^{−𝑡}+(1)/(3)𝑒^{−3𝑡})+(2)/(3)
- Steady-state response: lim𝑡→∞(𝑦(𝑡)=(2)/(3))
- Solving an ODE – Numeric Example

Equations / relations:
- `𝑌(𝑠)=((3/2)/(𝑠+1)+(−1/2)/(𝑠+3))+((−1)/(𝑠+1)+(1/3)/(𝑠+3))+(2/3)/(𝑠)=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)`
- `𝑦(𝑡)=((3)/(2)𝑒^{−𝑡}−(1)/(2)𝑒^{−3𝑡})+(−1𝑒^{−𝑡}+(1)/(3)𝑒^{−3𝑡})+(2)/(3)`
- `lim𝑡→∞(𝑦(𝑡)=(2)/(3))`
- `𝑌(𝑠)=((3/2)/(𝑠+1)+(−1/2)/(𝑠+3))+((−1)/(𝑠+1)+(1/3)/(𝑠+3))+(2/3)/(𝑠)=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)𝑌(𝑠)=((3/2)/(𝑠+1)+(−1/2)/(𝑠+3))+((−1)/(𝑠+1)+(1/3)/(𝑠+3))+(2/3)/(𝑠)=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)`
- `The response: 𝑦(𝑡)=((3)/(2)𝑒^{−𝑡}−(1)/(2)𝑒^{−3𝑡})+(−1𝑒^{−𝑡}+(1)/(3)𝑒^{−3𝑡})+(2)/(3)`
- `Steady-state response: lim𝑡→∞(𝑦(𝑡)=(2)/(3))`

Media:
- `media/image10.png`

---

### t03-s010 — I deal op-amp  𝑣_{1}=𝑣_{2}=0,    𝑖_{1}=0

Tags: formula, figure

Content:
- I deal op-amp  𝑣_{1}=𝑣_{2}=0,    𝑖_{1}=0
- Input 𝑣_{𝑖𝑛} Output 𝑣_{𝑜}
- KCL at 𝑣_{1}
- (𝑣_{𝑖𝑛}−𝑣_{1})/(𝑅_{1})=(𝑣_{1}−𝑣_{𝑜})/(𝑅_{2})(𝑣_{𝑖𝑛}−𝑣_{1})/(𝑅_{1})=(𝑣_{1}−𝑣_{𝑜})/(𝑅_{2})
- 𝑣_{1}=𝑣_{2}=0 (𝑣_{𝑜})/(𝑣_{𝑖𝑛})=−(𝑅_{2})/(𝑅_{1})
- Transfer Function of an Op-Amp Circuit

Equations / relations:
- `𝑣_{1}=𝑣_{2}=0, 𝑖_{1}=0`
- `𝑣_{𝑖𝑛}`
- `𝑣_{𝑜}`
- `𝑣_{1}`
- `(𝑣_{𝑖𝑛}−𝑣_{1})/(𝑅_{1})=(𝑣_{1}−𝑣_{𝑜})/(𝑅_{2})`
- `𝑣_{1}=𝑣_{2}=0`
- `(𝑣_{𝑜})/(𝑣_{𝑖𝑛})=−(𝑅_{2})/(𝑅_{1})`
- `I deal op-amp  𝑣_{1}=𝑣_{2}=0,    𝑖_{1}=0`
- `(𝑣_{𝑖𝑛}−𝑣_{1})/(𝑅_{1})=(𝑣_{1}−𝑣_{𝑜})/(𝑅_{2})(𝑣_{𝑖𝑛}−𝑣_{1})/(𝑅_{1})=(𝑣_{1}−𝑣_{𝑜})/(𝑅_{2})`
- `𝑣_{1}=𝑣_{2}=0 (𝑣_{𝑜})/(𝑣_{𝑖𝑛})=−(𝑅_{2})/(𝑅_{1})`

Media:
- `media/image11.png`
- `media/image2.jpeg`

---

### t03-s011 — Small jets (A-A) or (B-B) apply reaction forces to rotate the body

Tags: formula, figure

Content:
- Small jets (A-A) or (B-B) apply reaction forces to rotate the body
- Jet thrust is 𝐹/2 and Torque 𝜏(𝑡)= 𝐹𝑙
- Moment of inertia about the center of mass is 𝐽
- Transfer Function - Satellite Attitude Control

Equations / relations:
- `𝐹/2`
- `𝜏(𝑡)= 𝐹𝑙`
- `𝐽`
- `Jet thrust is 𝐹/2 and Torque 𝜏(𝑡)= 𝐹𝑙`

Media:
- `media/image13.png`
- `media/image12.png`

---

### t03-s012 — Find: the TF of this system given that Torque 𝜏(𝑡) is the input and the angular displacement 𝜃(𝑡) is the output

Tags: formula, figure

Content:
- Find: the TF of this system given that Torque 𝜏(𝑡) is the input and the angular displacement 𝜃(𝑡) is the output
- Transfer Function - Satellite Attitude Control

Equations / relations:
- `𝜏(𝑡)`
- `𝜃(𝑡)`

Media:
- `media/image15.png`
- `media/image12.png`

---

### t03-s013 — Solution

Tags: formula, figure

Content:
- Solution
- Write the differential equation of the system 𝐽(𝑑𝜃^{2})/(𝑑𝑡^{2})=𝜏
- Take the Laplace Transform of the differential equation given all ICs are 0 𝐽𝑠^{2}Θ(𝑠)=Τ(𝑠)
- Transfer Function - Satellite Attitude Control

Equations / relations:
- `𝐽(𝑑𝜃^{2})/(𝑑𝑡^{2})=𝜏`
- `𝐽𝑠^{2}Θ(𝑠)=Τ(𝑠)`
- `Write the differential equation of the system 𝐽(𝑑𝜃^{2})/(𝑑𝑡^{2})=𝜏`
- `Take the Laplace Transform of the differential equation given all ICs are 0 𝐽𝑠^{2}Θ(𝑠)=Τ(𝑠)`

Media:
- `media/image16.png`

---

### t03-s014 — Solution

Tags: formula, figure

Content:
- Solution
- 3. Take the ratio of the output Θ(𝑠) to the input Τ(𝑠)
- Transfer Function: (Θ(𝑠))/(Τ(𝑠))=(1)/(𝐽𝑠^{2})
- Transfer Function - Satellite Attitude Control

Equations / relations:
- `Θ(𝑠)`
- `Τ(𝑠)`
- `(Θ(𝑠))/(Τ(𝑠))=(1)/(𝐽𝑠^{2})`
- `Transfer Function: (Θ(𝑠))/(Τ(𝑠))=(1)/(𝐽𝑠^{2})`

Media:
- `media/image17.png`

---

### t03-s015 — A power actuator device that delivers energy to a load

Tags: formula, figure

Content:
- A power actuator device that delivers energy to a load
- Transfer Function – DC Motor

Media:
- `media/image13.jpeg`

---

### t03-s016 — Converts direct current (DC) electrical energy into rotational mechanical energy

Tags: formula, figure

Content:
- Converts direct current (DC) electrical energy into rotational mechanical energy
- Transfer Function – DC Motor

Media:
- `media/image13.jpeg`

---

### t03-s017 — Used in numerous control applications, including robotic manipulators, tape transport mechanisms, disk drives ...

Tags: formula, figure

Content:
- Used in numerous control applications, including robotic manipulators, tape transport mechanisms, disk drives ...
- Transfer Function – DC Motor

Media:
- `media/image13.jpeg`

---

### t03-s018 — Advantages: high torque, speed controllability, portability …

Tags: formula, figure

Content:
- Advantages: high torque, speed controllability, portability …
- Transfer Function – DC Motor

Media:
- `media/image13.jpeg`

---

### t03-s019 — Used for moving loads when: rapid (microseconds) response is not required

Tags: formula, figure

Content:
- Used for moving loads when: rapid (microseconds) response is not required
- Transfer Function – DC Motor

Media:
- `media/image13.jpeg`

---

### t03-s020 — Used for moving loads when: relatively low power is required

Tags: formula, figure

Content:
- Used for moving loads when: relatively low power is required
- Transfer Function – DC Motor

Media:
- `media/image13.jpeg`

---

### t03-s021 — How does a DC motor work?

Tags: formula, figure

Content:
- How does a DC motor work?
- Transfer Function – DC Motor

Media:
- `media/image13.jpeg`

---

### t03-s022 — The input voltage may be applied to the field or armature terminals.

Tags: formula, figure

Content:
- The input voltage may be applied to the field or armature terminals.
- The air-gap flux 𝜙(𝑡) of the motor is proportional to the field current (as long as field is unsaturated)
- 𝜙(𝑡)=𝐾_{𝑓}𝑖_{𝑓}(𝑡)𝜙(𝑡)=𝐾_{𝑓}𝑖_{𝑓}(𝑡)
- The torque developed by the motor is assumed to be related linearly to 𝜙(𝑡) and the armature current
- 𝑇_{𝑚}(𝑡)=𝐾_{1}𝜙(𝑡)𝑖_{𝑎}(𝑡)=𝐾_{1}𝐾_{𝑓}𝑖_{𝑓}(𝑡)𝑖_{𝑎}(𝑡)𝑇_{𝑚}(𝑡)=𝐾_{1}𝜙(𝑡)𝑖_{𝑎}(𝑡)=𝐾_{1}𝐾_{𝑓}𝑖_{𝑓}(𝑡)𝑖_{𝑎}(𝑡)
- Transfer Function – DC Motor

Equations / relations:
- `𝜙(𝑡)`
- `𝜙(𝑡)=𝐾_{𝑓}𝑖_{𝑓}(𝑡)`
- `𝑇_{𝑚}(𝑡)=𝐾_{1}𝜙(𝑡)𝑖_{𝑎}(𝑡)=𝐾_{1}𝐾_{𝑓}𝑖_{𝑓}(𝑡)𝑖_{𝑎}(𝑡)`
- `𝜙(𝑡)=𝐾_{𝑓}𝑖_{𝑓}(𝑡)𝜙(𝑡)=𝐾_{𝑓}𝑖_{𝑓}(𝑡)`
- `𝑇_{𝑚}(𝑡)=𝐾_{1}𝜙(𝑡)𝑖_{𝑎}(𝑡)=𝐾_{1}𝐾_{𝑓}𝑖_{𝑓}(𝑡)𝑖_{𝑎}(𝑡)𝑇_{𝑚}(𝑡)=𝐾_{1}𝜙(𝑡)𝑖_{𝑎}(𝑡)=𝐾_{1}𝐾_{𝑓}𝑖_{𝑓}(𝑡)𝑖_{𝑎}(𝑡)`

Media:
- `media/image19.png`
- `media/image13.jpeg`

---

### t03-s023 — Laplace Transform

Tags: formula, figure

Content:
- Laplace Transform
- 𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑎})𝐼_{𝑓}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑎})𝐼_{𝑓}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)
- The field current is related to the field voltage as
- 𝑉_{𝑓}(𝑠)=(𝑅_{𝑓}+𝐿_{𝑓}𝑠)𝐼_{𝑓}(𝑠)𝑉_{𝑓}(𝑠)=(𝑅_{𝑓}+𝐿_{𝑓}𝑠)𝐼_{𝑓}(𝑠)
- Motor torque
- 𝑇_{𝑚}(𝑠)=𝑇_{𝐿}(𝑠)+𝑇_{𝑑}(𝑠)𝑇_{𝑚}(𝑠)=𝑇_{𝐿}(𝑠)+𝑇_{𝑑}(𝑠)
- Transfer Function – Field-Controlled DC Motor

Equations / relations:
- `𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑎})𝐼_{𝑓}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)`
- `𝑉_{𝑓}(𝑠)=(𝑅_{𝑓}+𝐿_{𝑓}𝑠)𝐼_{𝑓}(𝑠)`
- `𝑇_{𝑚}(𝑠)=𝑇_{𝐿}(𝑠)+𝑇_{𝑑}(𝑠)`
- `𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑎})𝐼_{𝑓}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑎})𝐼_{𝑓}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)`
- `𝑉_{𝑓}(𝑠)=(𝑅_{𝑓}+𝐿_{𝑓}𝑠)𝐼_{𝑓}(𝑠)𝑉_{𝑓}(𝑠)=(𝑅_{𝑓}+𝐿_{𝑓}𝑠)𝐼_{𝑓}(𝑠)`
- `𝑇_{𝑚}(𝑠)=𝑇_{𝐿}(𝑠)+𝑇_{𝑑}(𝑠)𝑇_{𝑚}(𝑠)=𝑇_{𝐿}(𝑠)+𝑇_{𝑑}(𝑠)`

Media:
- `media/image20.png`
- `media/image13.jpeg`

---

### t03-s024 — Load torque for rotating inertia

Tags: formula, figure

Content:
- Load torque for rotating inertia
- 𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)
- 𝑇_{𝐿}(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)𝑇_{𝐿}(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)
- 𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)=𝑇_{𝐿}(𝑠)𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)=𝑇_{𝐿}(𝑠)
- 𝐼_{𝑓}(𝑠)=(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)𝐼_{𝑓}(𝑠)=(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)
- 𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)
- Transfer Function – Field-Controlled DC Motor

Equations / relations:
- `𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)`
- `𝑇_{𝐿}(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)`
- `𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)=𝑇_{𝐿}(𝑠)`
- `𝐼_{𝑓}(𝑠)=(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)`
- `𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)`
- `𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)`
- `𝑇_{𝐿}(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)𝑇_{𝐿}(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)`
- `𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)=𝑇_{𝐿}(𝑠)𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)=𝑇_{𝐿}(𝑠)`
- `𝐼_{𝑓}(𝑠)=(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)𝐼_{𝑓}(𝑠)=(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)`
- `𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)`

Media:
- `media/image21.png`
- `media/image13.jpeg`

---

### t03-s025 — 𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)

Tags: formula, figure

Content:
- 𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)
- The transfer function of the motor–load combination
- (𝜃(𝑠))/(𝑉_{𝑓}(𝑠))=(𝐾_{𝑚})/(𝑠(𝐽𝑠+𝑏)(𝐿_{𝑓}𝑠+𝑅_{𝑓}))=(𝐾_{𝑚}/(𝐽𝐿_{𝑓}))/(𝑠(𝑠+𝑏/𝐽)(𝑠+𝑅_{𝑓}/𝐿_{𝑓}))(𝜃(𝑠))/(𝑉_{𝑓}(𝑠))=(𝐾_{𝑚})/(𝑠(𝐽𝑠+𝑏)(𝐿_{𝑓}𝑠+𝑅_{𝑓}))=(𝐾_{𝑚}/(𝐽𝐿_{𝑓}))/(𝑠(𝑠+𝑏/𝐽)(𝑠+𝑅_{𝑓}/𝐿_{𝑓}))
- Transfer Function – Field-Controlled DC Motor

Equations / relations:
- `𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)`
- `(𝜃(𝑠))/(𝑉_{𝑓}(𝑠))=(𝐾_{𝑚})/(𝑠(𝐽𝑠+𝑏)(𝐿_{𝑓}𝑠+𝑅_{𝑓}))=(𝐾_{𝑚}/(𝐽𝐿_{𝑓}))/(𝑠(𝑠+𝑏/𝐽)(𝑠+𝑅_{𝑓}/𝐿_{𝑓}))`
- `𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)`
- `(𝜃(𝑠))/(𝑉_{𝑓}(𝑠))=(𝐾_{𝑚})/(𝑠(𝐽𝑠+𝑏)(𝐿_{𝑓}𝑠+𝑅_{𝑓}))=(𝐾_{𝑚}/(𝐽𝐿_{𝑓}))/(𝑠(𝑠+𝑏/𝐽)(𝑠+𝑅_{𝑓}/𝐿_{𝑓}))(𝜃(𝑠))/(𝑉_{𝑓}(𝑠))=(𝐾_{𝑚})/(𝑠(𝐽𝑠+𝑏)(𝐿_{𝑓}𝑠+𝑅_{𝑓}))=(𝐾_{𝑚}/(𝐽𝐿_{𝑓}))/(𝑠(𝑠+𝑏/𝐽)(𝑠+𝑅_{𝑓}/𝐿_{𝑓}))`

Media:
- `media/image22.png`
- `media/image13.jpeg`

---

### t03-s026 — Transfer Function

Tags: formula, diagram

Content:
- Transfer Function
- (𝜃(𝑠))/(𝑉_{𝑓}(𝑠))=(𝐾_{𝑚})/(𝑠(𝐽𝑠+𝑏)(𝐿_{𝑓}𝑠+𝑅_{𝑓}))=(𝐾_{𝑚}/(𝐽𝐿_{𝑓}))/(𝑠(𝑠+𝑏/𝐽)(𝑠+𝑅_{𝑓}/𝐿_{𝑓}))(𝜃(𝑠))/(𝑉_{𝑓}(𝑠))=(𝐾_{𝑚})/(𝑠(𝐽𝑠+𝑏)(𝐿_{𝑓}𝑠+𝑅_{𝑓}))=(𝐾_{𝑚}/(𝐽𝐿_{𝑓}))/(𝑠(𝑠+𝑏/𝐽)(𝑠+𝑅_{𝑓}/𝐿_{𝑓}))
- Block Diagram
- Transfer Function – Field-Controlled DC Motor

Equations / relations:
- `(𝜃(𝑠))/(𝑉_{𝑓}(𝑠))=(𝐾_{𝑚})/(𝑠(𝐽𝑠+𝑏)(𝐿_{𝑓}𝑠+𝑅_{𝑓}))=(𝐾_{𝑚}/(𝐽𝐿_{𝑓}))/(𝑠(𝑠+𝑏/𝐽)(𝑠+𝑅_{𝑓}/𝐿_{𝑓}))`
- `(𝜃(𝑠))/(𝑉_{𝑓}(𝑠))=(𝐾_{𝑚})/(𝑠(𝐽𝑠+𝑏)(𝐿_{𝑓}𝑠+𝑅_{𝑓}))=(𝐾_{𝑚}/(𝐽𝐿_{𝑓}))/(𝑠(𝑠+𝑏/𝐽)(𝑠+𝑅_{𝑓}/𝐿_{𝑓}))(𝜃(𝑠))/(𝑉_{𝑓}(𝑠))=(𝐾_{𝑚})/(𝑠(𝐽𝑠+𝑏)(𝐿_{𝑓}𝑠+𝑅_{𝑓}))=(𝐾_{𝑚}/(𝐽𝐿_{𝑓}))/(𝑠(𝑠+𝑏/𝐽)(𝑠+𝑅_{𝑓}/𝐿_{𝑓}))`

Media:
- `media/image23.png`
- `media/image13.jpeg`
- `media/image14.jpeg`

---

### t03-s027 — The armature-controlled DC motor uses the armature current 𝑖_{𝑎} as the control variable.

Tags: formula, figure

Content:
- The armature-controlled DC motor uses the armature current 𝑖_{𝑎} as the control variable.
- The stator field can be established by a field coil and current or a permanent magnet.
- When a constant field current is established in a field coil,the motor torque is
- 𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑓})𝐼_{𝑎}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑓})𝐼_{𝑎}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)
- Transfer Function – Armature-Controlled DC Motor

Equations / relations:
- `𝑖_{𝑎}`
- `𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑓})𝐼_{𝑎}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)`
- `𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑓})𝐼_{𝑎}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑓})𝐼_{𝑎}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)`

Media:
- `media/image18.png`
- `media/image13.jpeg`

---

### t03-s028 — When a permanent magnet is used, we have

Tags: formula, figure

Content:
- When a permanent magnet is used, we have
- 𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)
- The armature current is related to the input voltage applied to the armature by
- 𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)
- 𝑉_{𝑏}(𝑠)=𝐾_{𝑏}𝜔(𝑠)=𝐾_{𝑏}𝑠𝜃(𝑠)𝑉_{𝑏}(𝑠)=𝐾_{𝑏}𝜔(𝑠)=𝐾_{𝑏}𝑠𝜃(𝑠)
- Transfer Function – Armature-Controlled DC Motor

Equations / relations:
- `𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)`
- `𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)`
- `𝑉_{𝑏}(𝑠)=𝐾_{𝑏}𝜔(𝑠)=𝐾_{𝑏}𝑠𝜃(𝑠)`
- `𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)`
- `𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)`
- `𝑉_{𝑏}(𝑠)=𝐾_{𝑏}𝜔(𝑠)=𝐾_{𝑏}𝑠𝜃(𝑠)𝑉_{𝑏}(𝑠)=𝐾_{𝑏}𝜔(𝑠)=𝐾_{𝑏}𝑠𝜃(𝑠)`

Media:
- `media/image26.png`
- `media/image13.jpeg`

---

### t03-s029 — 𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)

Tags: formula, figure

Content:
- 𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)
- 𝑉_{𝑏}(𝑠)=𝐾_{𝑏}𝜔(𝑠)=𝐾_{𝑏}𝑠𝜃(𝑠)𝑉_{𝑏}(𝑠)=𝐾_{𝑏}𝜔(𝑠)=𝐾_{𝑏}𝑠𝜃(𝑠)
- Armature current
- 𝐼_{𝑎}(𝑠)=(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}(𝑠)=(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)
- We know that load torque 𝑇_{𝐿}(𝑠) is represented by
- 𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)
- Transfer Function – Armature-Controlled DC Motor

Equations / relations:
- `𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)`
- `𝑉_{𝑏}(𝑠)=𝐾_{𝑏}𝜔(𝑠)=𝐾_{𝑏}𝑠𝜃(𝑠)`
- `𝐼_{𝑎}(𝑠)=(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)`
- `𝑇_{𝐿}(𝑠)`
- `𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)`
- `𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)`
- `𝑉_{𝑏}(𝑠)=𝐾_{𝑏}𝜔(𝑠)=𝐾_{𝑏}𝑠𝜃(𝑠)𝑉_{𝑏}(𝑠)=𝐾_{𝑏}𝜔(𝑠)=𝐾_{𝑏}𝑠𝜃(𝑠)`
- `𝐼_{𝑎}(𝑠)=(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}(𝑠)=(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)`
- `𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)`

Media:
- `media/image27.png`
- `media/image13.jpeg`

---

### t03-s030 — 𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)

Tags: formula, figure

Content:
- 𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)
- 𝐾_{𝑚}𝐼_{𝑎}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)𝐾_{𝑚}𝐼_{𝑎}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)
- 𝐾_{𝑚}(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)𝐾_{𝑚}(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)
- Transfer function
- 𝐺(𝑠)=(𝜃(𝑠))/(𝑉_{𝑎}(𝑠))=(𝐾_{𝑚})/(𝑠((𝑅_{𝑎}+𝐿_{𝑎}𝑠)(𝐽𝑠+𝑏)+𝐾_{𝑏}𝐾_{𝑚}))𝐺(𝑠)=(𝜃(𝑠))/(𝑉_{𝑎}(𝑠))=(𝐾_{𝑚})/(𝑠((𝑅_{𝑎}+𝐿_{𝑎}𝑠)(𝐽𝑠+𝑏)+𝐾_{𝑏}𝐾_{𝑚}))
- Transfer Function – Armature-Controlled DC Motor

Equations / relations:
- `𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)`
- `𝐾_{𝑚}𝐼_{𝑎}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)`
- `𝐾_{𝑚}(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)`
- `𝐺(𝑠)=(𝜃(𝑠))/(𝑉_{𝑎}(𝑠))=(𝐾_{𝑚})/(𝑠((𝑅_{𝑎}+𝐿_{𝑎}𝑠)(𝐽𝑠+𝑏)+𝐾_{𝑏}𝐾_{𝑚}))`
- `𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)`
- `𝐾_{𝑚}𝐼_{𝑎}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)𝐾_{𝑚}𝐼_{𝑎}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)`
- `𝐾_{𝑚}(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)𝐾_{𝑚}(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)`
- `𝐺(𝑠)=(𝜃(𝑠))/(𝑉_{𝑎}(𝑠))=(𝐾_{𝑚})/(𝑠((𝑅_{𝑎}+𝐿_{𝑎}𝑠)(𝐽𝑠+𝑏)+𝐾_{𝑏}𝐾_{𝑚}))𝐺(𝑠)=(𝜃(𝑠))/(𝑉_{𝑎}(𝑠))=(𝐾_{𝑚})/(𝑠((𝑅_{𝑎}+𝐿_{𝑎}𝑠)(𝐽𝑠+𝑏)+𝐾_{𝑏}𝐾_{𝑚}))`

Media:
- `media/image24.png`
- `media/image13.jpeg`

---

### t03-s031 — Transfer function

Tags: formula, diagram

Content:
- Transfer function
- 𝐺(𝑠)=(𝜃(𝑠))/(𝑉_{𝑎}(𝑠))=(𝐾_{𝑚})/(𝑠((𝑅_{𝑎}+𝐿_{𝑎}𝑠)(𝐽𝑠+𝑏)+𝐾_{𝑏}𝐾_{𝑚}))𝐺(𝑠)=(𝜃(𝑠))/(𝑉_{𝑎}(𝑠))=(𝐾_{𝑚})/(𝑠((𝑅_{𝑎}+𝐿_{𝑎}𝑠)(𝐽𝑠+𝑏)+𝐾_{𝑏}𝐾_{𝑚}))
- Block diagram
- Transfer Function – Armature-Controlled DC Motor

Equations / relations:
- `𝐺(𝑠)=(𝜃(𝑠))/(𝑉_{𝑎}(𝑠))=(𝐾_{𝑚})/(𝑠((𝑅_{𝑎}+𝐿_{𝑎}𝑠)(𝐽𝑠+𝑏)+𝐾_{𝑏}𝐾_{𝑚}))`
- `𝐺(𝑠)=(𝜃(𝑠))/(𝑉_{𝑎}(𝑠))=(𝐾_{𝑚})/(𝑠((𝑅_{𝑎}+𝐿_{𝑎}𝑠)(𝐽𝑠+𝑏)+𝐾_{𝑏}𝐾_{𝑚}))𝐺(𝑠)=(𝜃(𝑠))/(𝑉_{𝑎}(𝑠))=(𝐾_{𝑚})/(𝑠((𝑅_{𝑎}+𝐿_{𝑎}𝑠)(𝐽𝑠+𝑏)+𝐾_{𝑏}𝐾_{𝑚}))`

Media:
- `media/image29.png`
- `media/image13.jpeg`
- `media/image15.jpeg`

---

### t03-s032 — DC Motor Model

Tags: formula, figure

Content:
- DC Motor Model
- Mechanical Load
- 𝑇_{𝐿} : load torque
- 𝐽 : rotor inertia
- 𝐵 : viscous friction
- 𝜃 : angular position
- 𝜔 : angular velocity
- 𝑉_{𝑎} : applied voltage
- 𝑖_{𝑎} : armature current
- 𝑉_{𝑏} : back EMF
- V_{b}V_{b}
- Transfer Function – DC Motor

Equations / relations:
- `𝑇_{𝐿}`
- `𝐽`
- `𝐵`
- `𝜃`
- `𝜔`
- `𝑉_{𝑎}`
- `𝑖_{𝑎}`
- `𝑉_{𝑏}`
- `V_{b}`

Media:
- `media/image25.png`
- `media/image281.png`
- `media/image291.png`
- `media/image30.png`

---

### t03-s033 — (untitled slide 33)

Tags: formula, diagram

Content:
- A block diagram is a pictorial representation of the functions performed by each component in the system and the flow of signals.
- A block diagram depicts the relationships that exist amongst the various components.
- In a block diagram all variables are linked to each other through functional blocks.
- A functional block is a symbol for the mathematical operation on the input signal that produces the output.
- Transfer Function G(s)
- Signal in
- Signal out = Signal in G(s)
- Block Diagrams

Equations / relations:
- `Transfer Function G(s)`
- `Signal out = Signal in G(s)`

---

### t03-s034 — Block diagrams for a system are not unique.

Tags: figure

Content:
- Block diagrams for a system are not unique.
- A number of different block diagrams can be drawn for a system depending on the point of view of the analysis.
- 𝐺(𝑠)𝐺(𝑠)
- 𝑅(𝑠)𝑅(𝑠)
- 𝑌(𝑠)𝑌(𝑠)
- 𝐸(𝑠)𝐸(𝑠)
- +
- -
- Block Diagrams

Equations / relations:
- `𝐺(𝑠)`
- `𝑅(𝑠)`
- `𝑌(𝑠)`
- `𝐸(𝑠)`

Media:
- `media/image140.png`
- `media/image150.png`
- `media/image160.png`
- `media/image170.png`

---

### t03-s035 — A Summing point is a point at which two or more inputs are added or subtracted.

Tags: formula, figure

Content:
- A Summing point is a point at which two or more inputs are added or subtracted.
- A branch/pickoff point is a point from which the signal from a block goes concurrently to other blocks or summing points.
- 𝑎 𝑎
- 𝑎−𝑏 𝑎−𝑏
- +
- -
- 𝑏 𝑏
- Block Diagrams

Equations / relations:
- `𝑎`
- `𝑎−𝑏`
- `𝑏`

Media:
- `media/image180.png`
- `media/image190.png`
- `media/image200.png`

---

### t03-s036 — Reference 𝑅(𝑠), output 𝑌(𝑠), actuating error 𝐸(𝑠), and transfer function 𝐺(𝑠).

Tags: formula, comparison, figure

Content:
- Reference 𝑅(𝑠), output 𝑌(𝑠), actuating error 𝐸(𝑠), and transfer function 𝐺(𝑠).
- Output 𝑌(𝑠) is fed back to the summing point and compared to the reference input 𝑅(𝑠).
- 𝐺(𝑠)𝐺(𝑠)
- 𝑅(𝑠)𝑅(𝑠)
- 𝑌(𝑠)𝑌(𝑠)
- 𝐸(𝑠)𝐸(𝑠)
- +
- -
- Summing point
- Branch point
- Block Diagrams – Closed Loop

Equations / relations:
- `𝑅(𝑠)`
- `𝑌(𝑠)`
- `𝐸(𝑠)`
- `𝐺(𝑠)`

Media:
- `media/image32.png`
- `media/image140.png`
- `media/image150.png`
- `media/image220.png`
- `media/image170.png`

---

### t03-s037 — (untitled slide 37)

Tags: formula, figure

Content:
- When comparing the output 𝑌(𝑠) to the reference 𝑅(𝑠), we must make sure they have the same form (e.g., temperature-control system).
- This is done by using a feedback element with a transfer function 𝐻(𝑠) to get 𝐵(𝑠)=𝐻(𝑠)𝑌(𝑠).
- In cases where 𝐻(𝑠)=1, the system is called a unity feedback system and 𝐸(𝑠) is called the error signal.
- 𝐺(𝑠)𝐺(𝑠)
- 𝑅(𝑠)𝑅(𝑠)
- 𝑌(𝑠)𝑌(𝑠)
- 𝐸(𝑠)𝐸(𝑠)
- +
- -
- 𝐵(𝑠)𝐵(𝑠)
- 𝐻(𝑠)𝐻(𝑠)
- Block Diagrams – Feedback

Equations / relations:
- `𝑌(𝑠)`
- `𝑅(𝑠)`
- `𝐻(𝑠)`
- `𝐵(𝑠)=𝐻(𝑠)𝑌(𝑠)`
- `𝐻(𝑠)=1`
- `𝐸(𝑠)`
- `𝐺(𝑠)`
- `𝐵(𝑠)`
- `This is done by using a feedback element with a transfer function 𝐻(𝑠) to get 𝐵(𝑠)=𝐻(𝑠)𝑌(𝑠).`
- `In cases where 𝐻(𝑠)=1, the system is called a unity feedback system and 𝐸(𝑠) is called the error signal.`

Media:
- `media/image33.png`
- `media/image240.png`
- `media/image250.png`
- `media/image260.png`
- `media/image270.png`
- `media/image280.png`
- `media/image290.png`

---

### t03-s038 — The Open loop transfer function is the ratio of the feedback signal 𝐵(𝑠) to the actuating error signal 𝐸(𝑠).

Tags: formula, comparison, figure

Content:
- The Open loop transfer function is the ratio of the feedback signal 𝐵(𝑠) to the actuating error signal 𝐸(𝑠).
- 𝑂𝐿𝑇𝐹=(𝐵(𝑠))/(𝐸(𝑠))=𝐺(𝑠)𝐻(𝑠)𝑂𝐿𝑇𝐹=(𝐵(𝑠))/(𝐸(𝑠))=𝐺(𝑠)𝐻(𝑠)
- 𝐺(𝑠)𝐺(𝑠)
- 𝑅(𝑠)𝑅(𝑠)
- 𝑌(𝑠)𝑌(𝑠)
- 𝐸(𝑠)𝐸(𝑠)
- +
- -
- 𝐵(𝑠)𝐵(𝑠)
- 𝐻(𝑠)𝐻(𝑠)
- Block Diagrams – Open-Loop TF

Equations / relations:
- `𝐵(𝑠)`
- `𝐸(𝑠)`
- `𝑂𝐿𝑇𝐹=(𝐵(𝑠))/(𝐸(𝑠))=𝐺(𝑠)𝐻(𝑠)`
- `𝐺(𝑠)`
- `𝑅(𝑠)`
- `𝑌(𝑠)`
- `𝐻(𝑠)`
- `𝑂𝐿𝑇𝐹=(𝐵(𝑠))/(𝐸(𝑠))=𝐺(𝑠)𝐻(𝑠)𝑂𝐿𝑇𝐹=(𝐵(𝑠))/(𝐸(𝑠))=𝐺(𝑠)𝐻(𝑠)`

Media:
- `media/image34.png`
- `media/image240.png`
- `media/image250.png`
- `media/image310.png`
- `media/image270.png`
- `media/image280.png`
- `media/image290.png`

---

### t03-s039 — The feed-forward transfer function is the ratio of the output signal 𝑌(𝑠) to the actuating error signal 𝐸(𝑠).

Tags: formula, figure

Content:
- The feed-forward transfer function is the ratio of the output signal 𝑌(𝑠) to the actuating error signal 𝐸(𝑠).
- Feed-forward TF=(𝑌(𝑠))/(𝐸(𝑠))=𝐺(𝑠)
- 𝐺(𝑠)𝐺(𝑠)
- 𝑅(𝑠)𝑅(𝑠)
- 𝑌(𝑠)𝑌(𝑠)
- 𝐸(𝑠)𝐸(𝑠)
- +
- -
- 𝐵(𝑠)𝐵(𝑠)
- 𝐻(𝑠)𝐻(𝑠)
- Block Diagrams – Feed-Forward TF

Equations / relations:
- `𝑌(𝑠)`
- `𝐸(𝑠)`
- `=(𝑌(𝑠))/(𝐸(𝑠))=𝐺(𝑠)`
- `𝐺(𝑠)`
- `𝑅(𝑠)`
- `𝐵(𝑠)`
- `𝐻(𝑠)`
- `Feed-forward TF=(𝑌(𝑠))/(𝐸(𝑠))=𝐺(𝑠)`

Media:
- `media/image35.png`
- `media/image240.png`
- `media/image250.png`
- `media/image330.png`
- `media/image270.png`
- `media/image280.png`
- `media/image290.png`

---

### t03-s040 — The closed-loop transfer function is the transfer function relating the output signal 𝑌(𝑠) to the reference signal 𝑅(𝑠).

Tags: formula, comparison, figure

Content:
- The closed-loop transfer function is the transfer function relating the output signal 𝑌(𝑠) to the reference signal 𝑅(𝑠).
- Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))
- 𝐺(𝑠)𝐺(𝑠)
- 𝑅(𝑠)𝑅(𝑠)
- 𝑌(𝑠)𝑌(𝑠)
- 𝐸(𝑠)𝐸(𝑠)
- +
- -
- 𝐵(𝑠)𝐵(𝑠)
- 𝐻(𝑠)𝐻(𝑠)
- Block Diagrams – Closed-Loop TF

Equations / relations:
- `𝑌(𝑠)`
- `𝑅(𝑠)`
- `=(𝑌(𝑠))/(𝑅(𝑠))`
- `𝐺(𝑠)`
- `𝐸(𝑠)`
- `𝐵(𝑠)`
- `𝐻(𝑠)`
- `Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))`

Media:
- `media/image36.png`
- `media/image240.png`
- `media/image250.png`
- `media/image330.png`
- `media/image270.png`
- `media/image280.png`
- `media/image290.png`

---

### t03-s041 — Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))

Tags: formula, comparison, figure

Content:
- Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))
- 𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)
- 𝐺(𝑠)𝐺(𝑠)
- 𝑅(𝑠)𝑅(𝑠)
- 𝑌(𝑠)𝑌(𝑠)
- 𝐸(𝑠)𝐸(𝑠)
- +
- -
- 𝐵(𝑠)𝐵(𝑠)
- 𝐻(𝑠)𝐻(𝑠)
- Block Diagrams – Closed-Loop TF

Equations / relations:
- `=(𝑌(𝑠))/(𝑅(𝑠))`
- `𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)`
- `𝐺(𝑠)`
- `𝑅(𝑠)`
- `𝑌(𝑠)`
- `𝐸(𝑠)`
- `𝐵(𝑠)`
- `𝐻(𝑠)`
- `Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))`
- `𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)`

Media:
- `media/image37.png`
- `media/image240.png`
- `media/image250.png`
- `media/image330.png`
- `media/image270.png`
- `media/image280.png`
- `media/image290.png`

---

### t03-s042 — Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))

Tags: formula, comparison, figure

Content:
- Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))
- 𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)
- 𝐺(𝑠)𝐺(𝑠)
- 𝑅(𝑠)𝑅(𝑠)
- 𝑌(𝑠)𝑌(𝑠)
- 𝐸(𝑠)𝐸(𝑠)
- +
- -
- 𝐵(𝑠)𝐵(𝑠)
- 𝐻(𝑠)𝐻(𝑠)
- Block Diagrams – Closed-Loop TF

Equations / relations:
- `=(𝑌(𝑠))/(𝑅(𝑠))`
- `𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)`
- `𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)`
- `𝐺(𝑠)`
- `𝑅(𝑠)`
- `𝑌(𝑠)`
- `𝐸(𝑠)`
- `𝐵(𝑠)`
- `𝐻(𝑠)`
- `Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))`
- `𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)`

Media:
- `media/image38.png`
- `media/image240.png`
- `media/image250.png`
- `media/image330.png`
- `media/image270.png`
- `media/image280.png`
- `media/image290.png`

---

### t03-s043 — Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))

Tags: formula, comparison, figure

Content:
- Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))
- 𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))
- 𝐺(𝑠)𝐺(𝑠)
- 𝑅(𝑠)𝑅(𝑠)
- 𝑌(𝑠)𝑌(𝑠)
- 𝐸(𝑠)𝐸(𝑠)
- +
- -
- 𝐵(𝑠)𝐵(𝑠)
- 𝐻(𝑠)𝐻(𝑠)
- Block Diagrams – Closed-Loop TF

Equations / relations:
- `=(𝑌(𝑠))/(𝑅(𝑠))`
- `𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)`
- `𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)`
- `𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))`
- `𝐺(𝑠)`
- `𝑅(𝑠)`
- `𝑌(𝑠)`
- `𝐸(𝑠)`
- `𝐵(𝑠)`
- `𝐻(𝑠)`
- `Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))`
- `𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))`

Media:
- `media/image39.png`
- `media/image240.png`
- `media/image250.png`
- `media/image330.png`
- `media/image270.png`
- `media/image280.png`
- `media/image290.png`

---

### t03-s044 — Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))

Tags: formula, comparison, figure

Content:
- Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))
- 𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)
- 𝐺(𝑠)𝐺(𝑠)
- 𝑅(𝑠)𝑅(𝑠)
- 𝑌(𝑠)𝑌(𝑠)
- 𝐸(𝑠)𝐸(𝑠)
- +
- -
- 𝐵(𝑠)𝐵(𝑠)
- 𝐻(𝑠)𝐻(𝑠)
- Block Diagrams – Closed-Loop TF

Equations / relations:
- `=(𝑌(𝑠))/(𝑅(𝑠))`
- `𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)`
- `𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)`
- `𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))`
- `𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)`
- `𝐺(𝑠)`
- `𝑅(𝑠)`
- `𝑌(𝑠)`
- `𝐸(𝑠)`
- `𝐵(𝑠)`
- `𝐻(𝑠)`
- `Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))`
- `𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)`

Media:
- `media/image40.png`
- `media/image240.png`
- `media/image250.png`
- `media/image330.png`
- `media/image270.png`
- `media/image280.png`
- `media/image290.png`

---

### t03-s045 — Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))

Tags: formula, comparison, figure

Content:
- Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))
- 𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)CLTF=(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠))/(1+𝐺(𝑠)𝐻(𝑠))𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)CLTF=(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠))/(1+𝐺(𝑠)𝐻(𝑠))
- 𝐺(𝑠)𝐺(𝑠)
- 𝑅(𝑠)𝑅(𝑠)
- 𝑌(𝑠)𝑌(𝑠)
- 𝐸(𝑠)𝐸(𝑠)
- +
- -
- 𝐵(𝑠)𝐵(𝑠)
- 𝐻(𝑠)𝐻(𝑠)
- Block Diagrams – Closed-Loop TF

Equations / relations:
- `=(𝑌(𝑠))/(𝑅(𝑠))`
- `𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)`
- `CLTF=(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠))/(1+𝐺(𝑠)𝐻(𝑠))`
- `𝐺(𝑠)`
- `𝑅(𝑠)`
- `𝑌(𝑠)`
- `𝐸(𝑠)`
- `𝐵(𝑠)`
- `𝐻(𝑠)`
- `Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))`
- `𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)CLTF=(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠))/(1+𝐺(𝑠)𝐻(𝑠))𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)CLTF=(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠))/(1+𝐺(𝑠)𝐻(𝑠))`

Media:
- `media/image41.png`
- `media/image240.png`
- `media/image250.png`
- `media/image330.png`
- `media/image270.png`
- `media/image280.png`
- `media/image290.png`

---

### t03-s046 — Multiple-Input Multiple-Output(MIMO) Systems

Tags: example, formula, figure

Content:
- Multiple-Input Multiple-Output(MIMO) Systems
- Example
- 𝑌_{1}(𝑠)=𝐺_{11}(𝑠)𝑅_{1}(𝑠)+𝐺_{12}(𝑠)𝑅_{2}(𝑠) 𝑌_{2}(𝑠)=𝐺_{21}(𝑠)𝑅_{1}(𝑠)+𝐺_{22}(𝑠)𝑅_{2}(𝑠)
- (𝑌_{1}(𝑠)𝑌_{2}(𝑠))=(𝐺_{11}(𝑠)𝐺_{12}(𝑠)𝐺_{21}(𝑠)𝐺_{22}(𝑠))(𝑅_{1}(𝑠)𝑅_{2}(𝑠))            𝒀(𝑠)=𝑮(𝑠)𝑹(𝑠)(𝑌_{1}(𝑠)𝑌_{2}(𝑠))=(𝐺_{11}(𝑠)𝐺_{12}(𝑠)𝐺_{21}(𝑠)𝐺_{22}(𝑠))(𝑅_{1}(𝑠)𝑅_{2}(𝑠))            𝒀(𝑠)=𝑮(𝑠)𝑹(𝑠)
- Block Diagrams

Equations / relations:
- `𝑌_{1}(𝑠)=𝐺_{11}(𝑠)𝑅_{1}(𝑠)+𝐺_{12}(𝑠)𝑅_{2}(𝑠)`
- `𝑌_{2}(𝑠)=𝐺_{21}(𝑠)𝑅_{1}(𝑠)+𝐺_{22}(𝑠)𝑅_{2}(𝑠)`
- `(𝑌_{1}(𝑠)𝑌_{2}(𝑠))=(𝐺_{11}(𝑠)𝐺_{12}(𝑠)𝐺_{21}(𝑠)𝐺_{22}(𝑠))(𝑅_{1}(𝑠)𝑅_{2}(𝑠)) 𝒀(𝑠)=𝑮(𝑠)𝑹(𝑠)`
- `𝑌_{1}(𝑠)=𝐺_{11}(𝑠)𝑅_{1}(𝑠)+𝐺_{12}(𝑠)𝑅_{2}(𝑠) 𝑌_{2}(𝑠)=𝐺_{21}(𝑠)𝑅_{1}(𝑠)+𝐺_{22}(𝑠)𝑅_{2}(𝑠)`
- `(𝑌_{1}(𝑠)𝑌_{2}(𝑠))=(𝐺_{11}(𝑠)𝐺_{12}(𝑠)𝐺_{21}(𝑠)𝐺_{22}(𝑠))(𝑅_{1}(𝑠)𝑅_{2}(𝑠))            𝒀(𝑠)=𝑮(𝑠)𝑹(𝑠)(𝑌_{1}(𝑠)𝑌_{2}(𝑠))=(𝐺_{11}(𝑠)𝐺_{12}(𝑠)𝐺_{21}(𝑠)𝐺_{22}(𝑠))(𝑅_{1}(𝑠)𝑅_{2}(𝑠))            𝒀(𝑠)=𝑮(𝑠)𝑹(𝑠)`

Media:
- `media/image42.png`
- `media/image26.jpeg`
- `media/image27.jpeg`

---

### t03-s047 — Block Diagram to Signal-Flow Graph

Tags: diagram

Content:
- Block Diagram to Signal-Flow Graph

Media:
- `media/image28.jpeg`
- `media/image29.jpeg`

---

### t03-s048 — 𝑋_{3}=𝐺_{1}𝐺_{2}𝑋_{1}𝑋_{3}=𝐺_{1}𝐺_{2}𝑋_{1}

Tags: diagram

Content:
- 𝑋_{3}=𝐺_{1}𝐺_{2}𝑋_{1}𝑋_{3}=𝐺_{1}𝐺_{2}𝑋_{1}
- 𝑋_{3}=(𝑋_{1}±𝑋_{2})𝐺 𝑋_{3}=(𝑋_{1}±𝑋_{2})𝐺
- 𝑋_{2}=𝑋_{1}𝐺 𝑋_{2}=𝑋_{1}𝐺
- Block Diagram Transformation

Equations / relations:
- `𝑋_{3}=𝐺_{1}𝐺_{2}𝑋_{1}`
- `𝑋_{3}=(𝑋_{1}±𝑋_{2})𝐺`
- `𝑋_{2}=𝑋_{1}𝐺`
- `𝑋_{3}=𝐺_{1}𝐺_{2}𝑋_{1}𝑋_{3}=𝐺_{1}𝐺_{2}𝑋_{1}`
- `𝑋_{3}=(𝑋_{1}±𝑋_{2})𝐺 𝑋_{3}=(𝑋_{1}±𝑋_{2})𝐺`
- `𝑋_{2}=𝑋_{1}𝐺 𝑋_{2}=𝑋_{1}𝐺`

Media:
- `media/image30.jpeg`
- `media/image48.png`
- `media/image49.png`
- `media/image50.png`

---

### t03-s049 — 𝑋_{2}=𝑋_{1}𝐺 𝑋_{2}=𝑋_{1}𝐺

Tags: diagram

Content:
- 𝑋_{2}=𝑋_{1}𝐺 𝑋_{2}=𝑋_{1}𝐺
- 𝑋_{3}=𝑋_{1}𝐺±𝑋_{2}𝑋_{3}=𝑋_{1}𝐺±𝑋_{2}
- 𝑋_{2}=(𝐺)/(1±𝐺𝐻)𝑋_{1}𝑋_{2}=(𝐺)/(1±𝐺𝐻)𝑋_{1}
- Block Diagram Transformation

Equations / relations:
- `𝑋_{2}=𝑋_{1}𝐺`
- `𝑋_{3}=𝑋_{1}𝐺±𝑋_{2}`
- `𝑋_{2}=(𝐺)/(1±𝐺𝐻)𝑋_{1}`
- `𝑋_{2}=𝑋_{1}𝐺 𝑋_{2}=𝑋_{1}𝐺`
- `𝑋_{3}=𝑋_{1}𝐺±𝑋_{2}𝑋_{3}=𝑋_{1}𝐺±𝑋_{2}`
- `𝑋_{2}=(𝐺)/(1±𝐺𝐻)𝑋_{1}𝑋_{2}=(𝐺)/(1±𝐺𝐻)𝑋_{1}`

Media:
- `media/image31.jpeg`
- `media/image45.png`
- `media/image46.png`
- `media/image47.png`

---

### t03-s050 — 𝐸_{𝑎}(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠)𝐸_{𝑎}(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠)

Tags: formula, diagram

Content:
- 𝐸_{𝑎}(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠)𝐸_{𝑎}(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠)
- 𝑌(𝑠)=𝐺(𝑠)𝑈(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝑍(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐸_{𝑎}(𝑠)𝑌(𝑠)=𝐺(𝑠)𝑈(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝑍(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐸_{𝑎}(𝑠)
- 𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)(𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠))𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)(𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠))
- 𝑌(𝑠)+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝑅(𝑠)𝑌(𝑠)+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝑅(𝑠)
- Block Diagram to Transfer Function

Equations / relations:
- `𝐸_{𝑎}(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠)`
- `𝑌(𝑠)=𝐺(𝑠)𝑈(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝑍(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐸_{𝑎}(𝑠)`
- `𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)(𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠))`
- `𝑌(𝑠)+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝑅(𝑠)`
- `𝐸_{𝑎}(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠)𝐸_{𝑎}(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠)`
- `𝑌(𝑠)=𝐺(𝑠)𝑈(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝑍(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐸_{𝑎}(𝑠)𝑌(𝑠)=𝐺(𝑠)𝑈(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝑍(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐸_{𝑎}(𝑠)`
- `𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)(𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠))𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)(𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠))`
- `𝑌(𝑠)+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝑅(𝑠)𝑌(𝑠)+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝑅(𝑠)`

Media:
- `media/image52.png`
- `media/image32.jpeg`

---

### t03-s051 — (untitled slide 51)

Tags: formula, diagram

Content:
- (𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠))/(1+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠))(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠))/(1+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠))
- Block Diagram to Transfer Function

Equations / relations:
- `(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠))/(1+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠))`
- `(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠))/(1+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠))(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠))/(1+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠))`

Media:
- `media/image43.png`
- `media/image32.jpeg`

---

### t03-s052 — Block Diagram Reduction

Tags: diagram

Content:
- Block Diagram Reduction

Media:
- `media/image33.jpeg`
- `media/image34.jpeg`

---

### t03-s053 — Block Diagram Reduction

Tags: diagram

Content:
- Block Diagram Reduction

Media:
- `media/image34.jpeg`

---

### t03-s054 — (untitled slide 54)

Tags: diagram

Content:
- 𝐸𝑞𝑢𝑖𝑣𝑎𝑙𝑒𝑛𝑡 𝑇𝐹=(𝐺_{2}(𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1})(𝐻_{2})/(𝐺_{4}))=((𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐻_{2})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))𝐸𝑞𝑢𝑖𝑣𝑎𝑙𝑒𝑛𝑡 𝑇𝐹=(𝐺_{2}(𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1})(𝐻_{2})/(𝐺_{4}))=((𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐻_{2})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))
- =(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2})=(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2})
- Block Diagram Reduction

Equations / relations:
- `𝐸𝑞𝑢𝑖𝑣𝑎𝑙𝑒𝑛𝑡 𝑇𝐹=(𝐺_{2}(𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1})(𝐻_{2})/(𝐺_{4}))=((𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐻_{2})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))`
- `=(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2})`
- `𝐸𝑞𝑢𝑖𝑣𝑎𝑙𝑒𝑛𝑡 𝑇𝐹=(𝐺_{2}(𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1})(𝐻_{2})/(𝐺_{4}))=((𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐻_{2})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))𝐸𝑞𝑢𝑖𝑣𝑎𝑙𝑒𝑛𝑡 𝑇𝐹=(𝐺_{2}(𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1})(𝐻_{2})/(𝐺_{4}))=((𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐻_{2})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))`
- `=(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2})=(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2})`

Media:
- `media/image31.png`
- `media/image34.jpeg`

---

### t03-s055 — (untitled slide 55)

Tags: diagram

Content:
- (𝑌(𝑠))/(𝑅(𝑠))=((𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))/(1+(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})(𝑌(𝑠))/(𝑅(𝑠))=((𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))/(1+(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})
- Block Diagram Reduction

Equations / relations:
- `(𝑌(𝑠))/(𝑅(𝑠))=((𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))/(1+(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})`
- `(𝑌(𝑠))/(𝑅(𝑠))=((𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))/(1+(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})(𝑌(𝑠))/(𝑅(𝑠))=((𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))/(1+(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})`

Media:
- `media/image430.png`
- `media/image34.jpeg`

---

### t03-s056 — Overall Transfer Function

Tags: formula, diagram

Content:
- Overall Transfer Function
- (𝑌(𝑠))/(𝑅(𝑠))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})(𝑌(𝑠))/(𝑅(𝑠))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})
- Block Diagram Reduction

Equations / relations:
- `(𝑌(𝑠))/(𝑅(𝑠))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})`
- `(𝑌(𝑠))/(𝑅(𝑠))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})(𝑌(𝑠))/(𝑅(𝑠))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})`

Media:
- `media/image57.png`
- `media/image34.jpeg`

---

### t03-s057 — Given a Block Diagram or a Signal-Flow Graph

Tags: formula, diagram

Content:
- Given a Block Diagram or a Signal-Flow Graph
- The overall Transfer Function can be obtained using Mason’s Rule
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- 𝑃_{𝑖} is the ith forward path gain
- Δ=1−(sum of all individual loop gains) + (sum of gain products of all possible 2 non-touching loops) – (sum of gain products of all possible 3 non- touching loops) + …
- Δ_{𝑖} is obtained from Δ by removing all loops which are touching the ith forward path
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝑃_{𝑖}`
- `Δ=1−`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ=1−(sum of all individual loop gains) + (sum of gain products of all possible 2 non-touching loops) – (sum of gain products of all possible 3 non- touching loops) + …`

Media:
- `media/image58.png`

---

### t03-s058 — 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)

Tags: derivation, formula, procedure, diagram

Content:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Steps:
- Identify forward paths & determine each forward path gain
- Identify individual loops & determine each individual loop gain
- Identify number of 2 non-touching loops & determine the product gains of each pair
- Repeat step 3 for 3 non-touching loops, 4…(if any)
- Calculate each Δ_{𝑖} and Δ
- Apply Mason’s formula to obtain 𝑇(𝑠)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image59.png`

---

### t03-s059 — Example 1:

Tags: example, formula, diagram

Content:
- Example 1:
- Number of forward paths: 𝑁=1
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- 𝐺𝑎𝑖𝑛 𝑃_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺𝑎𝑖𝑛 𝑃_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑁=1`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐺𝑎𝑖𝑛 𝑃_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}`
- `Number of forward paths: 𝑁=1`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐺𝑎𝑖𝑛 𝑃_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺𝑎𝑖𝑛 𝑃_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}`

Media:
- `media/image33.jpeg`
- `media/image60.png`
- `media/image51.png`
- `media/image520.png`

---

### t03-s060 — Example 1:

Tags: example, formula, diagram

Content:
- Example 1:
- Number of individual loops: 𝐿=3
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- 𝐺𝑎𝑖𝑛 𝐿_{1}=−𝐺_{2}𝐺_{3}𝐻_{2}𝐺𝑎𝑖𝑛 𝐿_{1}=−𝐺_{2}𝐺_{3}𝐻_{2}
- 𝐺𝑎𝑖𝑛 𝐿_{2}=𝐺_{3}𝐺_{4}𝐻_{1}𝐺𝑎𝑖𝑛 𝐿_{2}=𝐺_{3}𝐺_{4}𝐻_{1}
- 𝐺𝑎𝑖𝑛 𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3}𝐺𝑎𝑖𝑛 𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3}
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝐿=3`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐺𝑎𝑖𝑛 𝐿_{1}=−𝐺_{2}𝐺_{3}𝐻_{2}`
- `𝐺𝑎𝑖𝑛 𝐿_{2}=𝐺_{3}𝐺_{4}𝐻_{1}`
- `𝐺𝑎𝑖𝑛 𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3}`
- `Number of individual loops: 𝐿=3`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐺𝑎𝑖𝑛 𝐿_{1}=−𝐺_{2}𝐺_{3}𝐻_{2}𝐺𝑎𝑖𝑛 𝐿_{1}=−𝐺_{2}𝐺_{3}𝐻_{2}`
- `𝐺𝑎𝑖𝑛 𝐿_{2}=𝐺_{3}𝐺_{4}𝐻_{1}𝐺𝑎𝑖𝑛 𝐿_{2}=𝐺_{3}𝐺_{4}𝐻_{1}`
- `𝐺𝑎𝑖𝑛 𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3}𝐺𝑎𝑖𝑛 𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3}`

Media:
- `media/image33.jpeg`
- `media/image61.png`
- `media/image51.png`
- `media/image56.png`
- `media/image570.png`
- `media/image580.png`

---

### t03-s061 — Example 1:

Tags: example, formula, diagram

Content:
- Example 1:
- All the loops have common nodes and therefore are all touching
- The forward path 𝑃_{1} touches all the loops so Δ_{1}=1
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑃_{1}`
- `Δ_{1}=1`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `The forward path 𝑃_{1} touches all the loops so Δ_{1}=1`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image33.jpeg`
- `media/image62.png`
- `media/image51.png`

---

### t03-s062 — Example 1:

Tags: example, formula, diagram

Content:
- Example 1:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}(𝑠))/(1−𝐿_{1}(𝑠)−𝐿_{2}(𝑠)−𝐿_{3}(𝑠))𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}(𝑠))/(1−𝐿_{1}(𝑠)−𝐿_{2}(𝑠)−𝐿_{3}(𝑠))
- 𝑇(𝑠)=(𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠))/(1+𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐻_{2}(𝑠)−𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{1}(𝑠)+𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{3}(𝑠))𝑇(𝑠)=(𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠))/(1+𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐻_{2}(𝑠)−𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{1}(𝑠)+𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{3}(𝑠))
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}(𝑠))/(1−𝐿_{1}(𝑠)−𝐿_{2}(𝑠)−𝐿_{3}(𝑠))`
- `𝑇(𝑠)=(𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠))/(1+𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐻_{2}(𝑠)−𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{1}(𝑠)+𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{3}(𝑠))`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}(𝑠))/(1−𝐿_{1}(𝑠)−𝐿_{2}(𝑠)−𝐿_{3}(𝑠))𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}(𝑠))/(1−𝐿_{1}(𝑠)−𝐿_{2}(𝑠)−𝐿_{3}(𝑠))`
- `𝑇(𝑠)=(𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠))/(1+𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐻_{2}(𝑠)−𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{1}(𝑠)+𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{3}(𝑠))𝑇(𝑠)=(𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠))/(1+𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐻_{2}(𝑠)−𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{1}(𝑠)+𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{3}(𝑠))`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image33.jpeg`
- `media/image63.png`
- `media/image51.png`

---

### t03-s063 — Example 1:

Tags: example, formula, diagram

Content:
- Example 1:
- 𝑇(𝑠)=(𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠))/(1+𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐻_{2}(𝑠)−𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{1}(𝑠)+𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{3}(𝑠))𝑇(𝑠)=(𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠))/(1+𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐻_{2}(𝑠)−𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{1}(𝑠)+𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{3}(𝑠))
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠))/(1+𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐻_{2}(𝑠)−𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{1}(𝑠)+𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{3}(𝑠))`
- `𝑇(𝑠)=(𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠))/(1+𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐻_{2}(𝑠)−𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{1}(𝑠)+𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{3}(𝑠))𝑇(𝑠)=(𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠))/(1+𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐻_{2}(𝑠)−𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{1}(𝑠)+𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{3}(𝑠))`

Media:
- `media/image64.png`
- `media/image34.jpeg`

---

### t03-s064 — Example 2: Find the TF of the Signal-Flow Graph below

Tags: example, formula, diagram

Content:
- Example 2: Find the TF of the Signal-Flow Graph below
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- y 1
- y 2
- y 3
- y 4
- y 5
- y 6
- a
- b
- j
- c
- d
- e
- f
- g
- i
- h
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image65.png`

---

### t03-s065 — 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)

Tags: derivation, formula, procedure, diagram

Content:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Steps:
- Identify forward paths & determine each forward path gain
- Identify individual loops & determine each individual loop gain
- Identify number of 2 non-touching loops & determine the product gains of each pair
- Repeat step 3 for 3 non-touching loops, 4…(if any)
- Calculate each Δ_{𝑖} and Δ
- Apply Mason’s formula to obtain 𝑇(𝑠)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image66.png`

---

### t03-s066 — Number of forward paths: 𝑁=2

Tags: formula, diagram

Content:
- Number of forward paths: 𝑁=2
- 𝑁_{1}:𝑦_{1}−𝑦_{2}−𝑦_{3}−𝑦_{4}−𝑦_{5}−𝑦_{6} Gain 𝑃_{1}=𝑎𝑏𝑐𝑑𝑒
- 𝑁_{2}:𝑦_{1}−𝑦_{2}−𝑦_{3}−𝑦_{5}−𝑦_{6} Gain 𝑃_{2}=𝑎𝑏𝑔𝑒
- y 1
- y 2
- y 3
- y 4
- y 5
- y 6
- a
- b
- j
- c
- d
- e
- f
- g
- i
- h
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑁=2`
- `𝑁_{1}:𝑦_{1}−𝑦_{2}−𝑦_{3}−𝑦_{4}−𝑦_{5}−𝑦_{6}`
- `𝑃_{1}=𝑎𝑏𝑐𝑑𝑒`
- `𝑁_{2}:𝑦_{1}−𝑦_{2}−𝑦_{3}−𝑦_{5}−𝑦_{6}`
- `𝑃_{2}=𝑎𝑏𝑔𝑒`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Number of forward paths: 𝑁=2`
- `𝑁_{1}:𝑦_{1}−𝑦_{2}−𝑦_{3}−𝑦_{4}−𝑦_{5}−𝑦_{6} Gain 𝑃_{1}=𝑎𝑏𝑐𝑑𝑒`
- `𝑁_{2}:𝑦_{1}−𝑦_{2}−𝑦_{3}−𝑦_{5}−𝑦_{6} Gain 𝑃_{2}=𝑎𝑏𝑔𝑒`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image67.png`
- `media/image51.png`

---

### t03-s067 — 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)

Tags: derivation, formula, procedure, diagram

Content:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Steps:
- Identify forward paths & determine each forward path gain
- Identify individual loops & determine each individual loop gain
- Identify number of 2 non-touching loops & determine the product gains of each pair
- Repeat step 3 for 3 non-touching loops, 4…(if any)
- Calculate each Δ_{𝑖} and Δ
- Apply Mason’s formula to obtain 𝑇(𝑠)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image68.png`

---

### t03-s068 — Number of individual loops: 𝐿=5

Tags: formula, diagram

Content:
- Number of individual loops: 𝐿=5
- 𝐿_{1}:𝑦_{2}−𝑦_{3}−𝑦_{2} Gain 𝑙_{1}=𝑏𝑗
- 𝐿_{2}:𝑦_{3}−𝑦_{5}−𝑦_{3} Gain 𝑙_{2}=𝑔h
- 𝐿_{3}:𝑦_{3}−𝑦_{4}−𝑦_{5}−𝑦_{3} Gain 𝑙_{3}=𝑐𝑑h
- 𝐿_{4}:𝑦_{4}−𝑦_{5}−𝑦_{4} Gain 𝑙_{4}=𝑑𝑖
- y 1
- y 2
- y 3
- y 4
- y 5
- y 6
- a
- b
- j
- c
- d
- e
- f
- g
- i
- h
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- 𝐿_{5}:𝑦_{5}−𝑦_{5}              Gain 𝑙_{5}=𝑓 𝐿_{5}:𝑦_{5}−𝑦_{5}              Gain 𝑙_{5}=𝑓
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝐿=5`
- `𝐿_{1}:𝑦_{2}−𝑦_{3}−𝑦_{2}`
- `𝑙_{1}=𝑏𝑗`
- `𝐿_{2}:𝑦_{3}−𝑦_{5}−𝑦_{3}`
- `𝑙_{2}=𝑔h`
- `𝐿_{3}:𝑦_{3}−𝑦_{4}−𝑦_{5}−𝑦_{3}`
- `𝑙_{3}=𝑐𝑑h`
- `𝐿_{4}:𝑦_{4}−𝑦_{5}−𝑦_{4}`
- `𝑙_{4}=𝑑𝑖`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐿_{5}:𝑦_{5}−𝑦_{5} Gain 𝑙_{5}=𝑓`
- `Number of individual loops: 𝐿=5`
- `𝐿_{1}:𝑦_{2}−𝑦_{3}−𝑦_{2} Gain 𝑙_{1}=𝑏𝑗`
- `𝐿_{2}:𝑦_{3}−𝑦_{5}−𝑦_{3} Gain 𝑙_{2}=𝑔h`
- `𝐿_{3}:𝑦_{3}−𝑦_{4}−𝑦_{5}−𝑦_{3} Gain 𝑙_{3}=𝑐𝑑h`
- `𝐿_{4}:𝑦_{4}−𝑦_{5}−𝑦_{4} Gain 𝑙_{4}=𝑑𝑖`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐿_{5}:𝑦_{5}−𝑦_{5}              Gain 𝑙_{5}=𝑓 𝐿_{5}:𝑦_{5}−𝑦_{5}              Gain 𝑙_{5}=𝑓`

Media:
- `media/image69.png`
- `media/image510.png`
- `media/image70.png`

---

### t03-s069 — 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)

Tags: derivation, formula, procedure, diagram

Content:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Steps:
- Identify forward paths & determine each forward path gain
- Identify individual loops & determine each individual loop gain
- Identify number of 2 non-touching loops & determine the product gains of each pair
- Repeat step 3 for 3 non-touching loops, 4…(if any)
- Calculate each Δ_{𝑖} and Δ
- Apply Mason’s formula to obtain 𝑇(𝑠)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image71.png`

---

### t03-s070 — Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}=2

Tags: formula, diagram

Content:
- Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}=2
- 𝑃𝑎𝑖𝑟1(𝐿_{1}𝑎𝑛𝑑 𝐿_{4}):𝑦_{2}−𝑦_{3}−𝑦_{2} 𝑎𝑛𝑑 𝑦_{4}−𝑦_{5}−𝑦_{4} Gain 𝑃𝑎𝑖𝑟1=𝑏𝑗∙𝑑𝑖
- 𝑃𝑎𝑖𝑟2 (𝐿_{1}𝑎𝑛𝑑 𝐿_{5}):𝑦_{2}−𝑦_{3}−𝑦_{2} 𝑎𝑛𝑑 𝑦_{5}−𝑦_{5} Gain 𝑃𝑎𝑖𝑟2=𝑏𝑗∙𝑓
- y 1
- y 2
- y 3
- y 4
- y 5
- y 6
- a
- b
- j
- c
- d
- e
- f
- g
- i
- h
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑁_{𝑝𝑎𝑖𝑟𝑠}=2`
- `𝑃𝑎𝑖𝑟1(𝐿_{1}𝑎𝑛𝑑 𝐿_{4}):𝑦_{2}−𝑦_{3}−𝑦_{2} 𝑎𝑛𝑑 𝑦_{4}−𝑦_{5}−𝑦_{4}`
- `𝑃𝑎𝑖𝑟1=𝑏𝑗∙𝑑𝑖`
- `𝑃𝑎𝑖𝑟2 (𝐿_{1}𝑎𝑛𝑑 𝐿_{5}):𝑦_{2}−𝑦_{3}−𝑦_{2} 𝑎𝑛𝑑 𝑦_{5}−𝑦_{5}`
- `𝑃𝑎𝑖𝑟2=𝑏𝑗∙𝑓`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}=2`
- `𝑃𝑎𝑖𝑟1(𝐿_{1}𝑎𝑛𝑑 𝐿_{4}):𝑦_{2}−𝑦_{3}−𝑦_{2} 𝑎𝑛𝑑 𝑦_{4}−𝑦_{5}−𝑦_{4} Gain 𝑃𝑎𝑖𝑟1=𝑏𝑗∙𝑑𝑖`
- `𝑃𝑎𝑖𝑟2 (𝐿_{1}𝑎𝑛𝑑 𝐿_{5}):𝑦_{2}−𝑦_{3}−𝑦_{2} 𝑎𝑛𝑑 𝑦_{5}−𝑦_{5} Gain 𝑃𝑎𝑖𝑟2=𝑏𝑗∙𝑓`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image72.png`
- `media/image51.png`

---

### t03-s071 — 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)

Tags: derivation, formula, procedure, diagram

Content:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Steps:
- Identify forward paths & determine each forward path gain
- Identify individual loops & determine each individual loop gain
- Identify number of 2 non-touching loops & determine the product gains of each pair
- Repeat step 3 for 3 non-touching loops, 4…(if any)
- Calculate each Δ_{𝑖} and Δ
- Apply Mason’s formula to obtain 𝑇(𝑠)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image73.png`

---

### t03-s072 — Number of 3 non-touching loops: 𝑁_{𝑡𝑟𝑖𝑝𝑙𝑒𝑡𝑠}=0

Tags: formula, diagram

Content:
- Number of 3 non-touching loops: 𝑁_{𝑡𝑟𝑖𝑝𝑙𝑒𝑡𝑠}=0
- So we stop here and move to calculating Δ 𝑎𝑛𝑑 Δ_{𝑖}
- y 1
- y 2
- y 3
- y 4
- y 5
- y 6
- a
- b
- j
- c
- d
- e
- f
- g
- i
- h
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑁_{𝑡𝑟𝑖𝑝𝑙𝑒𝑡𝑠}=0`
- `Δ 𝑎𝑛𝑑 Δ_{𝑖}`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Number of 3 non-touching loops: 𝑁_{𝑡𝑟𝑖𝑝𝑙𝑒𝑡𝑠}=0`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image74.png`
- `media/image51.png`

---

### t03-s073 — 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)

Tags: derivation, formula, procedure, diagram

Content:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Steps:
- Identify forward paths & determine each forward path gain
- Identify individual loops & determine each individual loop gain
- Identify number of 2 non-touching loops & determine the product gains of each pair
- Repeat step 3 for 3 non-touching loops, 4…(if any)
- Calculate each Δ_{𝑖} and Δ
- Apply Mason’s formula to obtain 𝑇(𝑠)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image75.png`

---

### t03-s074 — (untitled slide 74)

Tags: formula, diagram

Content:
- Δ=1−(sum of all individual loop gains) + (sum of gain products of all possible 2 non-touching loops) – (sum of gain products of all possible 3 non- touching loops) + …
- Δ=1−(𝑙_{1}+𝑙_{2}+𝑙_{3}+𝑙_{4}+𝑙_{5})+((𝑙_{1}∙𝑙_{4})+(𝑙_{1}∙𝑙_{5}))+0 Δ=1−(𝑙_{1}+𝑙_{2}+𝑙_{3}+𝑙_{4}+𝑙_{5})+((𝑙_{1}∙𝑙_{4})+(𝑙_{1}∙𝑙_{5}))+0
- Δ=1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓)Δ=1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓)
- y 1
- y 2
- y 3
- y 4
- y 5
- y 6
- a
- b
- j
- c
- d
- e
- f
- g
- i
- h
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `Δ=1−`
- `Δ=1−(𝑙_{1}+𝑙_{2}+𝑙_{3}+𝑙_{4}+𝑙_{5})+((𝑙_{1}∙𝑙_{4})+(𝑙_{1}∙𝑙_{5}))+0`
- `Δ=1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ=1−(sum of all individual loop gains) + (sum of gain products of all possible 2 non-touching loops) – (sum of gain products of all possible 3 non- touching loops) + …`
- `Δ=1−(𝑙_{1}+𝑙_{2}+𝑙_{3}+𝑙_{4}+𝑙_{5})+((𝑙_{1}∙𝑙_{4})+(𝑙_{1}∙𝑙_{5}))+0 Δ=1−(𝑙_{1}+𝑙_{2}+𝑙_{3}+𝑙_{4}+𝑙_{5})+((𝑙_{1}∙𝑙_{4})+(𝑙_{1}∙𝑙_{5}))+0`
- `Δ=1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓)Δ=1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image76.png`
- `media/image51.png`

---

### t03-s075 — All loops touch all forward paths

Tags: formula, diagram

Content:
- All loops touch all forward paths
- Δ_{1}=1        Δ_{2}=1 Δ_{1}=1        Δ_{2}=1
- y 1
- y 2
- y 3
- y 4
- y 5
- y 6
- a
- b
- j
- c
- d
- e
- f
- g
- i
- h
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `Δ_{1}=1 Δ_{2}=1`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{1}=1        Δ_{2}=1 Δ_{1}=1        Δ_{2}=1`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image77.png`
- `media/image51.png`

---

### t03-s076 — 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)

Tags: derivation, formula, procedure, diagram

Content:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Steps:
- Identify forward paths & determine each forward path gain
- Identify individual loops & determine each individual loop gain
- Identify number of 2 non-touching loops & determine the product gains of each pair
- Repeat step 3 for 3 non-touching loops, 4…(if any)
- Calculate each Δ_{𝑖} and Δ
- Apply Mason’s formula to obtain 𝑇(𝑠)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image78.png`

---

### t03-s077 — Apply Mason’s Rule:

Tags: formula, diagram

Content:
- Apply Mason’s Rule:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)=(𝑃_{1}Δ_{1})/(Δ)+(𝑃_{2}Δ_{2})/(Δ)=(𝑎𝑏𝑐𝑑𝑒+𝑎𝑏𝑔𝑒)/(1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓))𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)=(𝑃_{1}Δ_{1})/(Δ)+(𝑃_{2}Δ_{2})/(Δ)=(𝑎𝑏𝑐𝑑𝑒+𝑎𝑏𝑔𝑒)/(1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓))
- y 1
- y 2
- y 3
- y 4
- y 5
- y 6
- a
- b
- j
- c
- d
- e
- f
- g
- i
- h
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)=(𝑃_{1}Δ_{1})/(Δ)+(𝑃_{2}Δ_{2})/(Δ)=(𝑎𝑏𝑐𝑑𝑒+𝑎𝑏𝑔𝑒)/(1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓))`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)=(𝑃_{1}Δ_{1})/(Δ)+(𝑃_{2}Δ_{2})/(Δ)=(𝑎𝑏𝑐𝑑𝑒+𝑎𝑏𝑔𝑒)/(1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓))𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)=(𝑃_{1}Δ_{1})/(Δ)+(𝑃_{2}Δ_{2})/(Δ)=(𝑎𝑏𝑐𝑑𝑒+𝑎𝑏𝑔𝑒)/(1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓))`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image79.png`
- `media/image51.png`

---

### t03-s078 — Example 3: Find the TF of the Signal-Flow Graph below

Tags: example, formula, diagram

Content:
- Example 3: Find the TF of the Signal-Flow Graph below
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image80.png`
- `media/image35.jpeg`

---

### t03-s079 — 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)

Tags: derivation, formula, procedure, diagram

Content:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Steps:
- Identify forward paths & determine each forward path gain
- Identify individual loops & determine each individual loop gain
- Identify number of 2 non-touching loops & determine the product gains of each pair
- Repeat step 3 for 3 non-touching loops, 4…(if any)
- Calculate each Δ_{𝑖} and Δ
- Apply Mason’s formula to obtain 𝑇(𝑠)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image82.png`

---

### t03-s080 — Example 3:

Tags: example, formula, diagram

Content:
- Example 3:
- Number of forward paths: 𝑁=3
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- 𝐺𝑎𝑖𝑛 𝑁_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐺𝑎𝑖𝑛 𝑁_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}
- 𝐺𝑎𝑖𝑛 𝑁_{2}=𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐺𝑎𝑖𝑛 𝑁_{2}=𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}
- 𝐺𝑎𝑖𝑛 𝑁_{3}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐺𝑎𝑖𝑛 𝑁_{3}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑁=3`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐺𝑎𝑖𝑛 𝑁_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}`
- `𝐺𝑎𝑖𝑛 𝑁_{2}=𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}`
- `𝐺𝑎𝑖𝑛 𝑁_{3}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}`
- `Number of forward paths: 𝑁=3`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐺𝑎𝑖𝑛 𝑁_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐺𝑎𝑖𝑛 𝑁_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}`
- `𝐺𝑎𝑖𝑛 𝑁_{2}=𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐺𝑎𝑖𝑛 𝑁_{2}=𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}`
- `𝐺𝑎𝑖𝑛 𝑁_{3}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐺𝑎𝑖𝑛 𝑁_{3}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}`

Media:
- `media/image44.png`
- `media/image35.jpeg`
- `media/image770.png`
- `media/image780.png`
- `media/image790.png`
- `media/image800.png`

---

### t03-s081 — 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)

Tags: derivation, formula, procedure, diagram

Content:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Steps:
- Identify forward paths & determine each forward path gain
- Identify individual loops & determine each individual loop gain
- Identify number of 2 non-touching loops & determine the product gains of each pair
- Repeat step 3 for 3 non-touching loops, 4…(if any)
- Calculate each Δ_{𝑖} and Δ
- Apply Mason’s formula to obtain 𝑇(𝑠)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image68.png`

---

### t03-s082 — Example 3:

Tags: example, formula, diagram

Content:
- Example 3:
- Number of individual loops: 𝐿=8
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- 𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}
- 𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}
- 𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}
- 𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}
- 𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}
- 𝐿_{6}=−𝐺_{4}𝐻_{4}𝐿_{6}=−𝐺_{4}𝐻_{4}
- 𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}
- 𝐿_{8}=−𝐺_{8}𝐻_{1}𝐿_{8}=−𝐺_{8}𝐻_{1}
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝐿=8`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}`
- `𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}`
- `𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}`
- `𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}`
- `𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}`
- `𝐿_{6}=−𝐺_{4}𝐻_{4}`
- `𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}`
- `𝐿_{8}=−𝐺_{8}𝐻_{1}`
- `Number of individual loops: 𝐿=8`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}`
- `𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}`
- `𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}`
- `𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}`
- `𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}`
- `𝐿_{6}=−𝐺_{4}𝐻_{4}𝐿_{6}=−𝐺_{4}𝐻_{4}`
- `𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}`
- `𝐿_{8}=−𝐺_{8}𝐻_{1}𝐿_{8}=−𝐺_{8}𝐻_{1}`

Media:
- `media/image35.jpeg`
- `media/image84.png`
- `media/image770.png`
- `media/image820.png`
- `media/image830.png`
- `media/image840.png`
- `media/image85.png`
- `media/image86.png`
- `media/image87.png`
- `media/image88.png`
- `media/image89.png`

---

### t03-s083 — 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)

Tags: derivation, formula, procedure, diagram

Content:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Steps:
- Identify forward paths & determine each forward path gain
- Identify individual loops & determine each individual loop gain
- Identify number of 2 non-touching loops & determine the product gains of each pair
- Repeat step 3 for 3 non-touching loops, 4…(if any)
- Calculate each Δ_{𝑖} and Δ
- Apply Mason’s formula to obtain 𝑇(𝑠)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image71.png`

---

### t03-s084 — Example 3:

Tags: example, formula, diagram

Content:
- Example 3:
- Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}= ?
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- 𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}
- 𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}
- 𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}
- 𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}
- 𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}
- 𝐿_{6}=−𝐺_{4}𝐻_{4}𝐿_{6}=−𝐺_{4}𝐻_{4}
- 𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}
- 𝐿_{8}=−𝐺_{8}𝐻_{1}𝐿_{8}=−𝐺_{8}𝐻_{1}
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑁_{𝑝𝑎𝑖𝑟𝑠}=`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}`
- `𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}`
- `𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}`
- `𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}`
- `𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}`
- `𝐿_{6}=−𝐺_{4}𝐻_{4}`
- `𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}`
- `𝐿_{8}=−𝐺_{8}𝐻_{1}`
- `Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}= ?`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}`
- `𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}`
- `𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}`
- `𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}`
- `𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}`
- `𝐿_{6}=−𝐺_{4}𝐻_{4}𝐿_{6}=−𝐺_{4}𝐻_{4}`
- `𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}`
- `𝐿_{8}=−𝐺_{8}𝐻_{1}𝐿_{8}=−𝐺_{8}𝐻_{1}`

Media:
- `media/image90.png`
- `media/image35.jpeg`
- `media/image770.png`
- `media/image91.png`
- `media/image92.png`
- `media/image93.png`
- `media/image94.png`
- `media/image95.png`
- `media/image96.png`
- `media/image97.png`
- `media/image98.png`

---

### t03-s085 — Example 3:

Tags: example, formula, diagram

Content:
- Example 3:
- Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}= ?
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- 𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}
- 𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}
- 𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}
- 𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}
- 𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}
- 𝐿_{6}=−𝐺_{4}𝐻_{4}𝐿_{6}=−𝐺_{4}𝐻_{4}
- 𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}
- 𝐿_{8}=−𝐺_{8}𝐻_{1}𝐿_{8}=−𝐺_{8}𝐻_{1}
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑁_{𝑝𝑎𝑖𝑟𝑠}=`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}`
- `𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}`
- `𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}`
- `𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}`
- `𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}`
- `𝐿_{6}=−𝐺_{4}𝐻_{4}`
- `𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}`
- `𝐿_{8}=−𝐺_{8}𝐻_{1}`
- `Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}= ?`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}`
- `𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}`
- `𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}`
- `𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}`
- `𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}`
- `𝐿_{6}=−𝐺_{4}𝐻_{4}𝐿_{6}=−𝐺_{4}𝐻_{4}`
- `𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}`
- `𝐿_{8}=−𝐺_{8}𝐻_{1}𝐿_{8}=−𝐺_{8}𝐻_{1}`

Media:
- `media/image99.png`
- `media/image35.jpeg`
- `media/image770.png`
- `media/image91.png`
- `media/image92.png`
- `media/image93.png`
- `media/image94.png`
- `media/image95.png`
- `media/image96.png`
- `media/image97.png`
- `media/image98.png`

---

### t03-s086 — Example 3:

Tags: example, formula, diagram

Content:
- Example 3:
- Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}= ?
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- 𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}
- 𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}
- 𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}
- 𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}
- 𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}
- 𝐿_{6}=−𝐺_{4}𝐻_{4}𝐿_{6}=−𝐺_{4}𝐻_{4}
- 𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}
- 𝐿_{8}=−𝐺_{8}𝐻_{1}𝐿_{8}=−𝐺_{8}𝐻_{1}
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑁_{𝑝𝑎𝑖𝑟𝑠}=`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}`
- `𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}`
- `𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}`
- `𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}`
- `𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}`
- `𝐿_{6}=−𝐺_{4}𝐻_{4}`
- `𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}`
- `𝐿_{8}=−𝐺_{8}𝐻_{1}`
- `Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}= ?`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}`
- `𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}`
- `𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}`
- `𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}`
- `𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}`
- `𝐿_{6}=−𝐺_{4}𝐻_{4}𝐿_{6}=−𝐺_{4}𝐻_{4}`
- `𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}`
- `𝐿_{8}=−𝐺_{8}𝐻_{1}𝐿_{8}=−𝐺_{8}𝐻_{1}`

Media:
- `media/image99.png`
- `media/image35.jpeg`
- `media/image770.png`
- `media/image91.png`
- `media/image92.png`
- `media/image93.png`
- `media/image94.png`
- `media/image53.png`
- `media/image96.png`
- `media/image97.png`
- `media/image98.png`

---

### t03-s087 — Example 3:

Tags: example, formula, diagram

Content:
- Example 3:
- Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}= 3
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- 𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}
- 𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}
- 𝐿_{6}=−𝐺_{4}𝐻_{4}𝐿_{6}=−𝐺_{4}𝐻_{4}
- 𝐿_{8}=−𝐺_{8}𝐻_{1}𝐿_{8}=−𝐺_{8}𝐻_{1}
- &
- 𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}
- &
- 𝐿_{6}=−𝐺_{4}𝐻_{4}𝐿_{6}=−𝐺_{4}𝐻_{4}
- &
- 𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{6}}=𝐺_{2}𝐺_{4}𝐺_{7}𝐻_{2}𝐻_{4}𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{6}}=𝐺_{2}𝐺_{4}𝐺_{7}𝐻_{2}𝐻_{4}
- 𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{8}}=𝐺_{2}𝐺_{7}𝐺_{8}𝐻_{1}𝐻_{2}𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{8}}=𝐺_{2}𝐺_{7}𝐺_{8}𝐻_{1}𝐻_{2}
- 𝐺𝑎𝑖𝑛_{𝐿_{3},𝐿_{6}}=𝐺_{1}𝐺_{2}𝐺_{4}𝐺_{7}𝐺_{6}𝐻_{3}𝐻_{4}𝐺𝑎𝑖𝑛_{𝐿_{3},𝐿_{6}}=𝐺_{1}𝐺_{2}𝐺_{4}𝐺_{7}𝐺_{6}𝐻_{3}𝐻_{4}
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑁_{𝑝𝑎𝑖𝑟𝑠}=`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}`
- `𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}`
- `𝐿_{6}=−𝐺_{4}𝐻_{4}`
- `𝐿_{8}=−𝐺_{8}𝐻_{1}`
- `𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{6}}=𝐺_{2}𝐺_{4}𝐺_{7}𝐻_{2}𝐻_{4}`
- `𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{8}}=𝐺_{2}𝐺_{7}𝐺_{8}𝐻_{1}𝐻_{2}`
- `𝐺𝑎𝑖𝑛_{𝐿_{3},𝐿_{6}}=𝐺_{1}𝐺_{2}𝐺_{4}𝐺_{7}𝐺_{6}𝐻_{3}𝐻_{4}`
- `Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}= 3`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}`
- `𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}`
- `𝐿_{6}=−𝐺_{4}𝐻_{4}𝐿_{6}=−𝐺_{4}𝐻_{4}`
- `𝐿_{8}=−𝐺_{8}𝐻_{1}𝐿_{8}=−𝐺_{8}𝐻_{1}`
- `𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}`
- `𝐿_{6}=−𝐺_{4}𝐻_{4}𝐿_{6}=−𝐺_{4}𝐻_{4}`
- `𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{6}}=𝐺_{2}𝐺_{4}𝐺_{7}𝐻_{2}𝐻_{4}𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{6}}=𝐺_{2}𝐺_{4}𝐺_{7}𝐻_{2}𝐻_{4}`
- `𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{8}}=𝐺_{2}𝐺_{7}𝐺_{8}𝐻_{1}𝐻_{2}𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{8}}=𝐺_{2}𝐺_{7}𝐺_{8}𝐻_{1}𝐻_{2}`
- `𝐺𝑎𝑖𝑛_{𝐿_{3},𝐿_{6}}=𝐺_{1}𝐺_{2}𝐺_{4}𝐺_{7}𝐺_{6}𝐻_{3}𝐻_{4}𝐺𝑎𝑖𝑛_{𝐿_{3},𝐿_{6}}=𝐺_{1}𝐺_{2}𝐺_{4}𝐺_{7}𝐺_{6}𝐻_{3}𝐻_{4}`

Media:
- `media/image100.png`
- `media/image35.jpeg`
- `media/image770.png`
- `media/image101.png`
- `media/image102.png`
- `media/image103.png`
- `media/image104.png`
- `media/image105.png`
- `media/image106.png`
- `media/image107.png`
- `media/image108.png`
- `media/image109.png`

---

### t03-s088 — 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)

Tags: derivation, formula, procedure, diagram

Content:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Steps:
- Identify forward paths & determine each forward path gain
- Identify individual loops & determine each individual loop gain
- Identify number of 2 non-touching loops & determine the product gains of each pair
- Repeat step 3 for 3 non-touching loops, 4…(if any)
- Calculate each Δ_{𝑖} and Δ
- Apply Mason’s formula to obtain 𝑇(𝑠)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image110.png`

---

### t03-s089 — Example 3:

Tags: example, formula, diagram

Content:
- Example 3:
- Number of 3 non-touching loops: 𝑁_{𝑡𝑟𝑖𝑝𝑙𝑒𝑡𝑠}=0
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑁_{𝑡𝑟𝑖𝑝𝑙𝑒𝑡𝑠}=0`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Number of 3 non-touching loops: 𝑁_{𝑡𝑟𝑖𝑝𝑙𝑒𝑡𝑠}=0`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image111.png`
- `media/image35.jpeg`
- `media/image770.png`

---

### t03-s090 — 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)

Tags: derivation, formula, procedure, diagram

Content:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Steps:
- Identify forward paths & determine each forward path gain
- Identify individual loops & determine each individual loop gain
- Identify number of 2 non-touching loops & determine the product gains of each pair
- Repeat step 3 for 3 non-touching loops, 4…(if any)
- Calculate each Δ_{𝑖} and Δ
- Apply Mason’s formula to obtain 𝑇(𝑠)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image112.png`

---

### t03-s091 — Example 3:

Tags: example, formula, diagram

Content:
- Example 3:
- Δ=1−(sum of all individual loop gains) + (sum of gain products of all possible 2 non-touching loops) – (sum of gain products of all possible 3 non- touching loops) + …
- Δ=1−(−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}−𝐺_{2}𝐺_{7}𝐻_{2}−                  𝐺_{4}𝐻_{4}−𝐺_{5}𝐺_{6}𝐻_{1}−𝐺_{8}𝐻_{1})+(𝐺_{2}𝐺_{4}𝐺_{7}𝐻_{2}𝐻_{4}+𝐺_{2}𝐺_{7}𝐺_{8}𝐻_{1}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{4}𝐺_{7}𝐺_{6}𝐻_{3}𝐻_{4})+0
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `Δ=1−`
- `Δ=1−(−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}−𝐺_{2}𝐺_{7}𝐻_{2}− 𝐺_{4}𝐻_{4}−𝐺_{5}𝐺_{6}𝐻_{1}−𝐺_{8}𝐻_{1})+(𝐺_{2}𝐺_{4}𝐺_{7}𝐻_{2}𝐻_{4}+𝐺_{2}𝐺_{7}𝐺_{8}𝐻_{1}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{4}𝐺_{7}𝐺_{6}𝐻_{3}𝐻_{4})+0`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ=1−(sum of all individual loop gains) + (sum of gain products of all possible 2 non-touching loops) – (sum of gain products of all possible 3 non- touching loops) + …`
- `Δ=1−(−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}−𝐺_{2}𝐺_{7}𝐻_{2}−                  𝐺_{4}𝐻_{4}−𝐺_{5}𝐺_{6}𝐻_{1}−𝐺_{8}𝐻_{1})+(𝐺_{2}𝐺_{4}𝐺_{7}𝐻_{2}𝐻_{4}+𝐺_{2}𝐺_{7}𝐺_{8}𝐻_{1}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{4}𝐺_{7}𝐺_{6}𝐻_{3}𝐻_{4})+0`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image35.jpeg`
- `media/image113.png`
- `media/image770.png`

---

### t03-s092 — Example 3:

Tags: example, formula, diagram

Content:
- Example 3:
- Δ_{1} related to forward path 1:
- All loops are touching path 1
- Δ_{1}=1 Δ_{1}=1
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- 𝐺𝑎𝑖𝑛 𝑁_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐺𝑎𝑖𝑛 𝑁_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `Δ_{1}`
- `Δ_{1}=1`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐺𝑎𝑖𝑛 𝑁_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}`
- `Δ_{1}=1 Δ_{1}=1`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐺𝑎𝑖𝑛 𝑁_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐺𝑎𝑖𝑛 𝑁_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}`

Media:
- `media/image35.jpeg`
- `media/image114.png`
- `media/image770.png`
- `media/image115.png`

---

### t03-s093 — Example 3:

Tags: example, formula, diagram

Content:
- Example 3:
- Δ_{2} related to forward path 2:
- Loop 𝐿_{6}=−𝐺_{4}𝐻_{4} does not touch path 2
- Δ_{2}=1−𝐿_{6}=1+𝐺_{4}𝐻_{4}Δ_{2}=1−𝐿_{6}=1+𝐺_{4}𝐻_{4}
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- 𝐺𝑎𝑖𝑛 𝑁_{2}=𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐺𝑎𝑖𝑛 𝑁_{2}=𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `Δ_{2}`
- `𝐿_{6}=−𝐺_{4}𝐻_{4}`
- `Δ_{2}=1−𝐿_{6}=1+𝐺_{4}𝐻_{4}`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐺𝑎𝑖𝑛 𝑁_{2}=𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}`
- `Loop 𝐿_{6}=−𝐺_{4}𝐻_{4} does not touch path 2`
- `Δ_{2}=1−𝐿_{6}=1+𝐺_{4}𝐻_{4}Δ_{2}=1−𝐿_{6}=1+𝐺_{4}𝐻_{4}`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐺𝑎𝑖𝑛 𝑁_{2}=𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐺𝑎𝑖𝑛 𝑁_{2}=𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}`

Media:
- `media/image35.jpeg`
- `media/image116.png`
- `media/image770.png`
- `media/image117.png`

---

### t03-s094 — Example 3:

Tags: example, formula, diagram

Content:
- Example 3:
- Δ_{3} related to forward path 3:
- All loops are touching path 3
- Δ_{3}=1 Δ_{3}=1
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- 𝐺𝑎𝑖𝑛 𝑁_{3}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐺𝑎𝑖𝑛 𝑁_{3}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `Δ_{3}`
- `Δ_{3}=1`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐺𝑎𝑖𝑛 𝑁_{3}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}`
- `Δ_{3}=1 Δ_{3}=1`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝐺𝑎𝑖𝑛 𝑁_{3}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐺𝑎𝑖𝑛 𝑁_{3}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}`

Media:
- `media/image35.jpeg`
- `media/image118.png`
- `media/image770.png`
- `media/image119.png`

---

### t03-s095 — 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)

Tags: derivation, formula, procedure, diagram

Content:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Steps:
- Identify forward paths & determine each forward path gain
- Identify individual loops & determine each individual loop gain
- Identify number of 2 non-touching loops & determine the product gains of each pair
- Repeat step 3 for 3 non-touching loops, 4…(if any)
- Calculate each Δ_{𝑖} and Δ
- Apply Mason’s formula to obtain 𝑇(𝑠)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `Δ_{𝑖}`
- `Δ`
- `𝑇(𝑠)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image78.png`

---

### t03-s096 — Example 3:

Tags: example, formula, diagram

Content:
- Example 3:
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}+𝑃_{2}(𝑠)Δ_{2}+𝑃_{3}(𝑠)Δ_{3})/(Δ(𝑠))𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}+𝑃_{2}(𝑠)Δ_{2}+𝑃_{3}(𝑠)Δ_{3})/(Δ(𝑠))
- 𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)
- Block Diagram Reduction using Mason’s Rule

Equations / relations:
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}+𝑃_{2}(𝑠)Δ_{2}+𝑃_{3}(𝑠)Δ_{3})/(Δ(𝑠))`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}+𝑃_{2}(𝑠)Δ_{2}+𝑃_{3}(𝑠)Δ_{3})/(Δ(𝑠))𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}+𝑃_{2}(𝑠)Δ_{2}+𝑃_{3}(𝑠)Δ_{3})/(Δ(𝑠))`
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)`

Media:
- `media/image35.jpeg`
- `media/image120.png`
- `media/image770.png`

---

## Formula index (this topic)

- `𝑇𝐹=𝐺(𝑠)=(ℒ(𝑜𝑢𝑡𝑝𝑢𝑡))/(ℒ(𝑖𝑛𝑝𝑢𝑡)) 𝐼𝐶=0` ← t03-s002
- `𝑀𝑠^{2}𝑌(𝑠)+𝑏𝑠𝑌(𝑠)+𝑘𝑌(𝑠)=𝑅(𝑠)` ← t03-s002
- `𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(1)/(𝑀𝑠^{2}+𝑏𝑠+𝑘)` ← t03-s002
- `𝑇𝐹=𝐺(𝑠)=(ℒ(𝑜𝑢𝑡𝑝𝑢𝑡))/(ℒ(𝑖𝑛𝑝𝑢𝑡))          𝐼𝐶=0 𝑇𝐹=𝐺(𝑠)=(ℒ(𝑜𝑢𝑡𝑝𝑢𝑡))/(ℒ(𝑖𝑛𝑝𝑢𝑡))          𝐼𝐶=0` ← t03-s002
- `𝑀𝑠^{2}𝑌(𝑠)+𝑏𝑠𝑌(𝑠)+𝑘𝑌(𝑠)=𝑅(𝑠)𝑀𝑠^{2}𝑌(𝑠)+𝑏𝑠𝑌(𝑠)+𝑘𝑌(𝑠)=𝑅(𝑠)` ← t03-s002
- `is 𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(1)/(𝑀𝑠^{2}+𝑏𝑠+𝑘)` ← t03-s002
- `𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))` ← t03-s003
- `𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))` ← t03-s003
- `G(s)` ← t03-s003
- `R(s)` ← t03-s003
- `Y(s)` ← t03-s003
- `(𝑑^{𝑛}𝑦(𝑡))/(𝑑𝑡^{𝑛})+𝑞_{𝑛−1}(𝑑^{𝑛−1}𝑦(𝑡))/(𝑑𝑡^{𝑛−1})+…+𝑞_{0}𝑦(𝑡)` ← t03-s004
- `=𝑝_{𝑛−1}(𝑑^{𝑛−1}𝑟(𝑡))/(𝑑𝑡^{𝑛−1})+𝑝_{𝑛−2}(𝑑^{𝑛−2}𝑟(𝑡))/(𝑑𝑡^{𝑛−2})+…+𝑝_{0}𝑟(𝑡)` ← t03-s004
- `𝐼𝐶=0` ← t03-s004
- `𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑝(𝑠))/(𝑞(𝑠))=(𝑝_{𝑛−1}𝑠^{𝑛−1}+𝑝_{𝑛−2}𝑠^{𝑛−2}+…+𝑝_{0})/(𝑠^{𝑛}+𝑞_{𝑛−1}𝑠^{𝑛−1}+…+𝑞_{0})` ← t03-s004
- `=𝑝_{𝑛−1}(𝑑^{𝑛−1}𝑟(𝑡))/(𝑑𝑡^{𝑛−1})+𝑝_{𝑛−2}(𝑑^{𝑛−2}𝑟(𝑡))/(𝑑𝑡^{𝑛−2})+…+𝑝_{0}𝑟(𝑡)=𝑝_{𝑛−1}(𝑑^{𝑛−1}𝑟(𝑡))/(𝑑𝑡^{𝑛−1})+𝑝_{𝑛−2}(𝑑^{𝑛−2}𝑟(𝑡))/(𝑑𝑡^{𝑛−2})+…+𝑝_{0}𝑟(𝑡)` ← t03-s004
- `If 𝐼𝐶=0  𝐺(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑝(𝑠))/(𝑞(𝑠))=(𝑝_{𝑛−1}𝑠^{𝑛−1}+𝑝_{𝑛−2}𝑠^{𝑛−2}+…+𝑝_{0})/(𝑠^{𝑛}+𝑞_{𝑛−1}𝑠^{𝑛−1}+…+𝑞_{0})` ← t03-s004
- `𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))𝑅(𝑠)` ← t03-s005
- `Output response = natural response (determined by the initial conditions) + forced response (determined by the input)` ← t03-s005
- `𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))𝑅(𝑠)𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))𝑅(𝑠)` ← t03-s005
- `𝑅(𝑠)=(𝑛(𝑠))/(𝑑(𝑠))` ← t03-s006
- `𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))(𝑛(𝑠))/(𝑑(𝑠))=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)` ← t03-s006
- `𝑌_{1}(𝑠)` ← t03-s006
- `𝑌_{2}(𝑠)` ← t03-s006
- `𝑞(𝑠)` ← t03-s006
- `𝑌_{3}(𝑠)` ← t03-s006
- `𝑑(𝑠)` ← t03-s006
- `ℒ^{−1}` ← t03-s006
- `𝑦(𝑡)=𝑦_{1}(𝑡)+𝑦_{2}(𝑡)+𝑦_{3}(𝑡)` ← t03-s006
- `If 𝑅(𝑠)=(𝑛(𝑠))/(𝑑(𝑠)) then 𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))(𝑛(𝑠))/(𝑑(𝑠))=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)` ← t03-s006
- `ℒ^{−1}  𝑦(𝑡)=𝑦_{1}(𝑡)+𝑦_{2}(𝑡)+𝑦_{3}(𝑡)` ← t03-s006
- `(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+4(𝑑𝑦(𝑡))/(𝑑𝑡)+3𝑦(𝑡)=2𝑟(𝑡)` ← t03-s007
- `𝑦(0)=1, (𝑑𝑦)/(𝑑𝑡)(0)=0, 𝑟(𝑡)=1, 𝑡≥0` ← t03-s007
- `(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0))+4(𝑠𝑌(𝑠)−𝑦(0))+3𝑌(𝑠)=2𝑅(𝑠)` ← t03-s007
- `𝑌(𝑠)=(𝑠+4)/(𝑠^{2}+4𝑠+3)+(2)/(𝑠(𝑠^{2}+4𝑠+3))` ← t03-s007
- `Given the ODE: (𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+4(𝑑𝑦(𝑡))/(𝑑𝑡)+3𝑦(𝑡)=2𝑟(𝑡)` ← t03-s007
- `With Initial Conditions: 𝑦(0)=1,   (𝑑𝑦)/(𝑑𝑡)(0)=0,    𝑟(𝑡)=1,    𝑡≥0` ← t03-s007
- `(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0))+4(𝑠𝑌(𝑠)−𝑦(0))+3𝑌(𝑠)=2𝑅(𝑠)(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0))+4(𝑠𝑌(𝑠)−𝑦(0))+3𝑌(𝑠)=2𝑅(𝑠)` ← t03-s007
- `𝑌(𝑠)=(𝑠+4)/(𝑠^{2}+4𝑠+3)+(2)/(𝑠(𝑠^{2}+4𝑠+3))𝑌(𝑠)=(𝑠+4)/(𝑠^{2}+4𝑠+3)+(2)/(𝑠(𝑠^{2}+4𝑠+3))` ← t03-s007
- `𝑞(𝑠)=𝑠^{2}+4𝑠+3=(𝑠+1)(𝑠+3)=0` ← t03-s008
- `Where 𝑞(𝑠)=𝑠^{2}+4𝑠+3=(𝑠+1)(𝑠+3)=0 is the characteristic equation` ← t03-s008
- `𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))(𝑛(𝑠))/(𝑑(𝑠))=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)𝑌(𝑠)=(𝑚(𝑠))/(𝑞(𝑠))+(𝑝(𝑠))/(𝑞(𝑠))(𝑛(𝑠))/(𝑑(𝑠))=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)` ← t03-s008
- `𝑌(𝑠)=((3/2)/(𝑠+1)+(−1/2)/(𝑠+3))+((−1)/(𝑠+1)+(1/3)/(𝑠+3))+(2/3)/(𝑠)=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)` ← t03-s009
- `𝑦(𝑡)=((3)/(2)𝑒^{−𝑡}−(1)/(2)𝑒^{−3𝑡})+(−1𝑒^{−𝑡}+(1)/(3)𝑒^{−3𝑡})+(2)/(3)` ← t03-s009
- `lim𝑡→∞(𝑦(𝑡)=(2)/(3))` ← t03-s009
- `𝑌(𝑠)=((3/2)/(𝑠+1)+(−1/2)/(𝑠+3))+((−1)/(𝑠+1)+(1/3)/(𝑠+3))+(2/3)/(𝑠)=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)𝑌(𝑠)=((3/2)/(𝑠+1)+(−1/2)/(𝑠+3))+((−1)/(𝑠+1)+(1/3)/(𝑠+3))+(2/3)/(𝑠)=𝑌_{1}(𝑠)+𝑌_{2}(𝑠)+𝑌_{3}(𝑠)` ← t03-s009
- `The response: 𝑦(𝑡)=((3)/(2)𝑒^{−𝑡}−(1)/(2)𝑒^{−3𝑡})+(−1𝑒^{−𝑡}+(1)/(3)𝑒^{−3𝑡})+(2)/(3)` ← t03-s009
- `Steady-state response: lim𝑡→∞(𝑦(𝑡)=(2)/(3))` ← t03-s009
- `𝑣_{1}=𝑣_{2}=0, 𝑖_{1}=0` ← t03-s010
- `𝑣_{𝑖𝑛}` ← t03-s010
- `𝑣_{𝑜}` ← t03-s010
- `𝑣_{1}` ← t03-s010
- `(𝑣_{𝑖𝑛}−𝑣_{1})/(𝑅_{1})=(𝑣_{1}−𝑣_{𝑜})/(𝑅_{2})` ← t03-s010
- `𝑣_{1}=𝑣_{2}=0` ← t03-s010
- `(𝑣_{𝑜})/(𝑣_{𝑖𝑛})=−(𝑅_{2})/(𝑅_{1})` ← t03-s010
- `I deal op-amp  𝑣_{1}=𝑣_{2}=0,    𝑖_{1}=0` ← t03-s010
- `(𝑣_{𝑖𝑛}−𝑣_{1})/(𝑅_{1})=(𝑣_{1}−𝑣_{𝑜})/(𝑅_{2})(𝑣_{𝑖𝑛}−𝑣_{1})/(𝑅_{1})=(𝑣_{1}−𝑣_{𝑜})/(𝑅_{2})` ← t03-s010
- `𝑣_{1}=𝑣_{2}=0 (𝑣_{𝑜})/(𝑣_{𝑖𝑛})=−(𝑅_{2})/(𝑅_{1})` ← t03-s010
- `𝐹/2` ← t03-s011
- `𝜏(𝑡)= 𝐹𝑙` ← t03-s011
- `𝐽` ← t03-s011
- `Jet thrust is 𝐹/2 and Torque 𝜏(𝑡)= 𝐹𝑙` ← t03-s011
- `𝜏(𝑡)` ← t03-s012
- `𝜃(𝑡)` ← t03-s012
- `𝐽(𝑑𝜃^{2})/(𝑑𝑡^{2})=𝜏` ← t03-s013
- `𝐽𝑠^{2}Θ(𝑠)=Τ(𝑠)` ← t03-s013
- `Write the differential equation of the system 𝐽(𝑑𝜃^{2})/(𝑑𝑡^{2})=𝜏` ← t03-s013
- `Take the Laplace Transform of the differential equation given all ICs are 0 𝐽𝑠^{2}Θ(𝑠)=Τ(𝑠)` ← t03-s013
- `Θ(𝑠)` ← t03-s014
- `Τ(𝑠)` ← t03-s014
- `(Θ(𝑠))/(Τ(𝑠))=(1)/(𝐽𝑠^{2})` ← t03-s014
- `Transfer Function: (Θ(𝑠))/(Τ(𝑠))=(1)/(𝐽𝑠^{2})` ← t03-s014
- `𝜙(𝑡)` ← t03-s022
- `𝜙(𝑡)=𝐾_{𝑓}𝑖_{𝑓}(𝑡)` ← t03-s022
- `𝑇_{𝑚}(𝑡)=𝐾_{1}𝜙(𝑡)𝑖_{𝑎}(𝑡)=𝐾_{1}𝐾_{𝑓}𝑖_{𝑓}(𝑡)𝑖_{𝑎}(𝑡)` ← t03-s022
- `𝜙(𝑡)=𝐾_{𝑓}𝑖_{𝑓}(𝑡)𝜙(𝑡)=𝐾_{𝑓}𝑖_{𝑓}(𝑡)` ← t03-s022
- `𝑇_{𝑚}(𝑡)=𝐾_{1}𝜙(𝑡)𝑖_{𝑎}(𝑡)=𝐾_{1}𝐾_{𝑓}𝑖_{𝑓}(𝑡)𝑖_{𝑎}(𝑡)𝑇_{𝑚}(𝑡)=𝐾_{1}𝜙(𝑡)𝑖_{𝑎}(𝑡)=𝐾_{1}𝐾_{𝑓}𝑖_{𝑓}(𝑡)𝑖_{𝑎}(𝑡)` ← t03-s022
- `𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑎})𝐼_{𝑓}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)` ← t03-s023
- `𝑉_{𝑓}(𝑠)=(𝑅_{𝑓}+𝐿_{𝑓}𝑠)𝐼_{𝑓}(𝑠)` ← t03-s023
- `𝑇_{𝑚}(𝑠)=𝑇_{𝐿}(𝑠)+𝑇_{𝑑}(𝑠)` ← t03-s023
- `𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑎})𝐼_{𝑓}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑎})𝐼_{𝑓}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)` ← t03-s023
- `𝑉_{𝑓}(𝑠)=(𝑅_{𝑓}+𝐿_{𝑓}𝑠)𝐼_{𝑓}(𝑠)𝑉_{𝑓}(𝑠)=(𝑅_{𝑓}+𝐿_{𝑓}𝑠)𝐼_{𝑓}(𝑠)` ← t03-s023
- `𝑇_{𝑚}(𝑠)=𝑇_{𝐿}(𝑠)+𝑇_{𝑑}(𝑠)𝑇_{𝑚}(𝑠)=𝑇_{𝐿}(𝑠)+𝑇_{𝑑}(𝑠)` ← t03-s023
- `𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)` ← t03-s024
- `𝑇_{𝐿}(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)` ← t03-s024
- `𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)=𝑇_{𝐿}(𝑠)` ← t03-s024
- `𝐼_{𝑓}(𝑠)=(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)` ← t03-s024
- `𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)` ← t03-s024
- `𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)` ← t03-s024
- `𝑇_{𝐿}(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)𝑇_{𝐿}(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)` ← t03-s024
- `𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)=𝑇_{𝐿}(𝑠)𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑓}(𝑠)=𝑇_{𝐿}(𝑠)` ← t03-s024
- `𝐼_{𝑓}(𝑠)=(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)𝐼_{𝑓}(𝑠)=(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)` ← t03-s024
- `𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)𝐾_{𝑚}(𝑉_{𝑓}(𝑠))/(𝑅_{𝑓}+𝐿_{𝑓}𝑠)=(𝐽𝑠^{2}+𝑏𝑠)𝜃(𝑠)` ← t03-s024
- `(𝜃(𝑠))/(𝑉_{𝑓}(𝑠))=(𝐾_{𝑚})/(𝑠(𝐽𝑠+𝑏)(𝐿_{𝑓}𝑠+𝑅_{𝑓}))=(𝐾_{𝑚}/(𝐽𝐿_{𝑓}))/(𝑠(𝑠+𝑏/𝐽)(𝑠+𝑅_{𝑓}/𝐿_{𝑓}))` ← t03-s025
- `(𝜃(𝑠))/(𝑉_{𝑓}(𝑠))=(𝐾_{𝑚})/(𝑠(𝐽𝑠+𝑏)(𝐿_{𝑓}𝑠+𝑅_{𝑓}))=(𝐾_{𝑚}/(𝐽𝐿_{𝑓}))/(𝑠(𝑠+𝑏/𝐽)(𝑠+𝑅_{𝑓}/𝐿_{𝑓}))(𝜃(𝑠))/(𝑉_{𝑓}(𝑠))=(𝐾_{𝑚})/(𝑠(𝐽𝑠+𝑏)(𝐿_{𝑓}𝑠+𝑅_{𝑓}))=(𝐾_{𝑚}/(𝐽𝐿_{𝑓}))/(𝑠(𝑠+𝑏/𝐽)(𝑠+𝑅_{𝑓}/𝐿_{𝑓}))` ← t03-s025
- `𝑖_{𝑎}` ← t03-s027
- `𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑓})𝐼_{𝑎}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)` ← t03-s027
- `𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑓})𝐼_{𝑎}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)𝑇_{𝑚}(𝑠)=(𝐾_{1}𝐾_{𝑓}𝐼_{𝑓})𝐼_{𝑎}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)` ← t03-s027
- `𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)` ← t03-s028
- `𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)` ← t03-s028
- `𝑉_{𝑏}(𝑠)=𝐾_{𝑏}𝜔(𝑠)=𝐾_{𝑏}𝑠𝜃(𝑠)` ← t03-s028
- `𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)𝑇_{𝑚}(𝑠)=𝐾_{𝑚}𝐼_{𝑎}(𝑠)` ← t03-s028
- `𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)𝑉_{𝑎}(𝑠)=(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}+𝑉_{𝑏}(𝑠)` ← t03-s028
- `𝑉_{𝑏}(𝑠)=𝐾_{𝑏}𝜔(𝑠)=𝐾_{𝑏}𝑠𝜃(𝑠)𝑉_{𝑏}(𝑠)=𝐾_{𝑏}𝜔(𝑠)=𝐾_{𝑏}𝑠𝜃(𝑠)` ← t03-s028
- `𝐼_{𝑎}(𝑠)=(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)` ← t03-s029
- `𝑇_{𝐿}(𝑠)` ← t03-s029
- `𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)` ← t03-s029
- `𝐼_{𝑎}(𝑠)=(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)𝐼_{𝑎}(𝑠)=(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)` ← t03-s029
- `𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)𝑇_{𝐿}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)=𝑇_{𝑚}(𝑠)−𝑇_{𝑑}(𝑠)` ← t03-s029
- `𝐾_{𝑚}𝐼_{𝑎}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)` ← t03-s030
- `𝐾_{𝑚}(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)` ← t03-s030
- `𝐺(𝑠)=(𝜃(𝑠))/(𝑉_{𝑎}(𝑠))=(𝐾_{𝑚})/(𝑠((𝑅_{𝑎}+𝐿_{𝑎}𝑠)(𝐽𝑠+𝑏)+𝐾_{𝑏}𝐾_{𝑚}))` ← t03-s030
- `𝐾_{𝑚}𝐼_{𝑎}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)𝐾_{𝑚}𝐼_{𝑎}(𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)` ← t03-s030
- `𝐾_{𝑚}(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)𝐾_{𝑚}(𝑉_{𝑎}(𝑠)−𝐾_{𝑏}𝑠𝜃(𝑠))/(𝑅_{𝑎}+𝐿_{𝑎}𝑠)=𝐽𝑠^{2}𝜃(𝑠)+𝑏𝑠𝜃(𝑠)` ← t03-s030
- `𝐺(𝑠)=(𝜃(𝑠))/(𝑉_{𝑎}(𝑠))=(𝐾_{𝑚})/(𝑠((𝑅_{𝑎}+𝐿_{𝑎}𝑠)(𝐽𝑠+𝑏)+𝐾_{𝑏}𝐾_{𝑚}))𝐺(𝑠)=(𝜃(𝑠))/(𝑉_{𝑎}(𝑠))=(𝐾_{𝑚})/(𝑠((𝑅_{𝑎}+𝐿_{𝑎}𝑠)(𝐽𝑠+𝑏)+𝐾_{𝑏}𝐾_{𝑚}))` ← t03-s030
- `𝑇_{𝐿}` ← t03-s032
- `𝐵` ← t03-s032
- `𝜃` ← t03-s032
- `𝜔` ← t03-s032
- `𝑉_{𝑎}` ← t03-s032
- `𝑉_{𝑏}` ← t03-s032
- `V_{b}` ← t03-s032
- `Transfer Function G(s)` ← t03-s033
- `Signal out = Signal in G(s)` ← t03-s033
- `𝐺(𝑠)` ← t03-s034
- `𝑅(𝑠)` ← t03-s034
- `𝑌(𝑠)` ← t03-s034
- `𝐸(𝑠)` ← t03-s034
- `𝑎` ← t03-s035
- `𝑎−𝑏` ← t03-s035
- `𝑏` ← t03-s035
- `𝐻(𝑠)` ← t03-s037
- `𝐵(𝑠)=𝐻(𝑠)𝑌(𝑠)` ← t03-s037
- `𝐻(𝑠)=1` ← t03-s037
- `𝐵(𝑠)` ← t03-s037
- `This is done by using a feedback element with a transfer function 𝐻(𝑠) to get 𝐵(𝑠)=𝐻(𝑠)𝑌(𝑠).` ← t03-s037
- `In cases where 𝐻(𝑠)=1, the system is called a unity feedback system and 𝐸(𝑠) is called the error signal.` ← t03-s037
- `𝑂𝐿𝑇𝐹=(𝐵(𝑠))/(𝐸(𝑠))=𝐺(𝑠)𝐻(𝑠)` ← t03-s038
- `𝑂𝐿𝑇𝐹=(𝐵(𝑠))/(𝐸(𝑠))=𝐺(𝑠)𝐻(𝑠)𝑂𝐿𝑇𝐹=(𝐵(𝑠))/(𝐸(𝑠))=𝐺(𝑠)𝐻(𝑠)` ← t03-s038
- `=(𝑌(𝑠))/(𝐸(𝑠))=𝐺(𝑠)` ← t03-s039
- `Feed-forward TF=(𝑌(𝑠))/(𝐸(𝑠))=𝐺(𝑠)` ← t03-s039
- `=(𝑌(𝑠))/(𝑅(𝑠))` ← t03-s040
- `Closed-loop TF=(𝑌(𝑠))/(𝑅(𝑠))` ← t03-s040
- `𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)` ← t03-s041
- `𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)` ← t03-s041
- `𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)` ← t03-s042
- `𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)` ← t03-s042
- `𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))` ← t03-s043
- `𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))` ← t03-s043
- `𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)` ← t03-s044
- `𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐸(𝑠)𝐸(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)(𝑅(𝑠)−𝑌(𝑠)𝐻(𝑠))𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)` ← t03-s044
- `CLTF=(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠))/(1+𝐺(𝑠)𝐻(𝑠))` ← t03-s045
- `𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)CLTF=(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠))/(1+𝐺(𝑠)𝐻(𝑠))𝑌(𝑠)(1+𝐺(𝑠)𝐻(𝑠))=𝐺(𝑠)𝑅(𝑠)CLTF=(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠))/(1+𝐺(𝑠)𝐻(𝑠))` ← t03-s045
- `𝑌_{1}(𝑠)=𝐺_{11}(𝑠)𝑅_{1}(𝑠)+𝐺_{12}(𝑠)𝑅_{2}(𝑠)` ← t03-s046
- `𝑌_{2}(𝑠)=𝐺_{21}(𝑠)𝑅_{1}(𝑠)+𝐺_{22}(𝑠)𝑅_{2}(𝑠)` ← t03-s046
- `(𝑌_{1}(𝑠)𝑌_{2}(𝑠))=(𝐺_{11}(𝑠)𝐺_{12}(𝑠)𝐺_{21}(𝑠)𝐺_{22}(𝑠))(𝑅_{1}(𝑠)𝑅_{2}(𝑠)) 𝒀(𝑠)=𝑮(𝑠)𝑹(𝑠)` ← t03-s046
- `𝑌_{1}(𝑠)=𝐺_{11}(𝑠)𝑅_{1}(𝑠)+𝐺_{12}(𝑠)𝑅_{2}(𝑠) 𝑌_{2}(𝑠)=𝐺_{21}(𝑠)𝑅_{1}(𝑠)+𝐺_{22}(𝑠)𝑅_{2}(𝑠)` ← t03-s046
- `(𝑌_{1}(𝑠)𝑌_{2}(𝑠))=(𝐺_{11}(𝑠)𝐺_{12}(𝑠)𝐺_{21}(𝑠)𝐺_{22}(𝑠))(𝑅_{1}(𝑠)𝑅_{2}(𝑠))            𝒀(𝑠)=𝑮(𝑠)𝑹(𝑠)(𝑌_{1}(𝑠)𝑌_{2}(𝑠))=(𝐺_{11}(𝑠)𝐺_{12}(𝑠)𝐺_{21}(𝑠)𝐺_{22}(𝑠))(𝑅_{1}(𝑠)𝑅_{2}(𝑠))            𝒀(𝑠)=𝑮(𝑠)𝑹(𝑠)` ← t03-s046
- `𝑋_{3}=𝐺_{1}𝐺_{2}𝑋_{1}` ← t03-s048
- `𝑋_{3}=(𝑋_{1}±𝑋_{2})𝐺` ← t03-s048
- `𝑋_{2}=𝑋_{1}𝐺` ← t03-s048
- `𝑋_{3}=𝐺_{1}𝐺_{2}𝑋_{1}𝑋_{3}=𝐺_{1}𝐺_{2}𝑋_{1}` ← t03-s048
- `𝑋_{3}=(𝑋_{1}±𝑋_{2})𝐺 𝑋_{3}=(𝑋_{1}±𝑋_{2})𝐺` ← t03-s048
- `𝑋_{2}=𝑋_{1}𝐺 𝑋_{2}=𝑋_{1}𝐺` ← t03-s048
- `𝑋_{3}=𝑋_{1}𝐺±𝑋_{2}` ← t03-s049
- `𝑋_{2}=(𝐺)/(1±𝐺𝐻)𝑋_{1}` ← t03-s049
- `𝑋_{3}=𝑋_{1}𝐺±𝑋_{2}𝑋_{3}=𝑋_{1}𝐺±𝑋_{2}` ← t03-s049
- `𝑋_{2}=(𝐺)/(1±𝐺𝐻)𝑋_{1}𝑋_{2}=(𝐺)/(1±𝐺𝐻)𝑋_{1}` ← t03-s049
- `𝐸_{𝑎}(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠)` ← t03-s050
- `𝑌(𝑠)=𝐺(𝑠)𝑈(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝑍(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐸_{𝑎}(𝑠)` ← t03-s050
- `𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)(𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠))` ← t03-s050
- `𝑌(𝑠)+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝑅(𝑠)` ← t03-s050
- `𝐸_{𝑎}(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠)𝐸_{𝑎}(𝑠)=𝑅(𝑠)−𝐵(𝑠)=𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠)` ← t03-s050
- `𝑌(𝑠)=𝐺(𝑠)𝑈(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝑍(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐸_{𝑎}(𝑠)𝑌(𝑠)=𝐺(𝑠)𝑈(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝑍(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐸_{𝑎}(𝑠)` ← t03-s050
- `𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)(𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠))𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)(𝑅(𝑠)−𝐻(𝑠)𝑌(𝑠))` ← t03-s050
- `𝑌(𝑠)+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝑅(𝑠)𝑌(𝑠)+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠)𝑌(𝑠)=𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝑅(𝑠)` ← t03-s050
- `(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠))/(1+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠))` ← t03-s051
- `(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠))/(1+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠))(𝑌(𝑠))/(𝑅(𝑠))=(𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠))/(1+𝐺(𝑠)𝐺_{𝑎}(𝑠)𝐺_{𝑐}(𝑠)𝐻(𝑠))` ← t03-s051
- `𝐸𝑞𝑢𝑖𝑣𝑎𝑙𝑒𝑛𝑡 𝑇𝐹=(𝐺_{2}(𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1})(𝐻_{2})/(𝐺_{4}))=((𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐻_{2})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))` ← t03-s054
- `=(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2})` ← t03-s054
- `𝐸𝑞𝑢𝑖𝑣𝑎𝑙𝑒𝑛𝑡 𝑇𝐹=(𝐺_{2}(𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1})(𝐻_{2})/(𝐺_{4}))=((𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐻_{2})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))𝐸𝑞𝑢𝑖𝑣𝑎𝑙𝑒𝑛𝑡 𝑇𝐹=(𝐺_{2}(𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1})(𝐻_{2})/(𝐺_{4}))=((𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))/(1+(𝐺_{2}𝐺_{3}𝐻_{2})/(1−𝐺_{3}𝐺_{4}𝐻_{1}))` ← t03-s054
- `=(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2})=(𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2})` ← t03-s054
- `(𝑌(𝑠))/(𝑅(𝑠))=((𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))/(1+(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})` ← t03-s055
- `(𝑌(𝑠))/(𝑅(𝑠))=((𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))/(1+(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})(𝑌(𝑠))/(𝑅(𝑠))=((𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))/(1+(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})` ← t03-s055
- `(𝑌(𝑠))/(𝑅(𝑠))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})` ← t03-s056
- `(𝑌(𝑠))/(𝑅(𝑠))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})(𝑌(𝑠))/(𝑅(𝑠))=(𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4})/(1−𝐺_{3}𝐺_{4}𝐻_{1}+𝐺_{2}𝐺_{3}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3})` ← t03-s056
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)` ← t03-s057
- `𝑃_{𝑖}` ← t03-s057
- `Δ=1−` ← t03-s057
- `Δ_{𝑖}` ← t03-s057
- `Δ` ← t03-s057
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)` ← t03-s057
- `Δ=1−(sum of all individual loop gains) + (sum of gain products of all possible 2 non-touching loops) – (sum of gain products of all possible 3 non- touching loops) + …` ← t03-s057
- `𝑇(𝑠)` ← t03-s058
- `𝑁=1` ← t03-s059
- `𝐺𝑎𝑖𝑛 𝑃_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}` ← t03-s059
- `Number of forward paths: 𝑁=1` ← t03-s059
- `𝐺𝑎𝑖𝑛 𝑃_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺𝑎𝑖𝑛 𝑃_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}` ← t03-s059
- `𝐿=3` ← t03-s060
- `𝐺𝑎𝑖𝑛 𝐿_{1}=−𝐺_{2}𝐺_{3}𝐻_{2}` ← t03-s060
- `𝐺𝑎𝑖𝑛 𝐿_{2}=𝐺_{3}𝐺_{4}𝐻_{1}` ← t03-s060
- `𝐺𝑎𝑖𝑛 𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3}` ← t03-s060
- `Number of individual loops: 𝐿=3` ← t03-s060
- `𝐺𝑎𝑖𝑛 𝐿_{1}=−𝐺_{2}𝐺_{3}𝐻_{2}𝐺𝑎𝑖𝑛 𝐿_{1}=−𝐺_{2}𝐺_{3}𝐻_{2}` ← t03-s060
- `𝐺𝑎𝑖𝑛 𝐿_{2}=𝐺_{3}𝐺_{4}𝐻_{1}𝐺𝑎𝑖𝑛 𝐿_{2}=𝐺_{3}𝐺_{4}𝐻_{1}` ← t03-s060
- `𝐺𝑎𝑖𝑛 𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3}𝐺𝑎𝑖𝑛 𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐻_{3}` ← t03-s060
- `𝑃_{1}` ← t03-s061
- `Δ_{1}=1` ← t03-s061
- `The forward path 𝑃_{1} touches all the loops so Δ_{1}=1` ← t03-s061
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}(𝑠))/(1−𝐿_{1}(𝑠)−𝐿_{2}(𝑠)−𝐿_{3}(𝑠))` ← t03-s062
- `𝑇(𝑠)=(𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠))/(1+𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐻_{2}(𝑠)−𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{1}(𝑠)+𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{3}(𝑠))` ← t03-s062
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}(𝑠))/(1−𝐿_{1}(𝑠)−𝐿_{2}(𝑠)−𝐿_{3}(𝑠))𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}(𝑠))/(1−𝐿_{1}(𝑠)−𝐿_{2}(𝑠)−𝐿_{3}(𝑠))` ← t03-s062
- `𝑇(𝑠)=(𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠))/(1+𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐻_{2}(𝑠)−𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{1}(𝑠)+𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{3}(𝑠))𝑇(𝑠)=(𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠))/(1+𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐻_{2}(𝑠)−𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{1}(𝑠)+𝐺_{1}(𝑠)𝐺_{2}(𝑠)𝐺_{3}(𝑠)𝐺_{4}(𝑠)𝐻_{3}(𝑠))` ← t03-s062
- `𝑁=2` ← t03-s066
- `𝑁_{1}:𝑦_{1}−𝑦_{2}−𝑦_{3}−𝑦_{4}−𝑦_{5}−𝑦_{6}` ← t03-s066
- `𝑃_{1}=𝑎𝑏𝑐𝑑𝑒` ← t03-s066
- `𝑁_{2}:𝑦_{1}−𝑦_{2}−𝑦_{3}−𝑦_{5}−𝑦_{6}` ← t03-s066
- `𝑃_{2}=𝑎𝑏𝑔𝑒` ← t03-s066
- `Number of forward paths: 𝑁=2` ← t03-s066
- `𝑁_{1}:𝑦_{1}−𝑦_{2}−𝑦_{3}−𝑦_{4}−𝑦_{5}−𝑦_{6} Gain 𝑃_{1}=𝑎𝑏𝑐𝑑𝑒` ← t03-s066
- `𝑁_{2}:𝑦_{1}−𝑦_{2}−𝑦_{3}−𝑦_{5}−𝑦_{6} Gain 𝑃_{2}=𝑎𝑏𝑔𝑒` ← t03-s066
- `𝐿=5` ← t03-s068
- `𝐿_{1}:𝑦_{2}−𝑦_{3}−𝑦_{2}` ← t03-s068
- `𝑙_{1}=𝑏𝑗` ← t03-s068
- `𝐿_{2}:𝑦_{3}−𝑦_{5}−𝑦_{3}` ← t03-s068
- `𝑙_{2}=𝑔h` ← t03-s068
- `𝐿_{3}:𝑦_{3}−𝑦_{4}−𝑦_{5}−𝑦_{3}` ← t03-s068
- `𝑙_{3}=𝑐𝑑h` ← t03-s068
- `𝐿_{4}:𝑦_{4}−𝑦_{5}−𝑦_{4}` ← t03-s068
- `𝑙_{4}=𝑑𝑖` ← t03-s068
- `𝐿_{5}:𝑦_{5}−𝑦_{5} Gain 𝑙_{5}=𝑓` ← t03-s068
- `Number of individual loops: 𝐿=5` ← t03-s068
- `𝐿_{1}:𝑦_{2}−𝑦_{3}−𝑦_{2} Gain 𝑙_{1}=𝑏𝑗` ← t03-s068
- `𝐿_{2}:𝑦_{3}−𝑦_{5}−𝑦_{3} Gain 𝑙_{2}=𝑔h` ← t03-s068
- `𝐿_{3}:𝑦_{3}−𝑦_{4}−𝑦_{5}−𝑦_{3} Gain 𝑙_{3}=𝑐𝑑h` ← t03-s068
- `𝐿_{4}:𝑦_{4}−𝑦_{5}−𝑦_{4} Gain 𝑙_{4}=𝑑𝑖` ← t03-s068
- `𝐿_{5}:𝑦_{5}−𝑦_{5}              Gain 𝑙_{5}=𝑓 𝐿_{5}:𝑦_{5}−𝑦_{5}              Gain 𝑙_{5}=𝑓` ← t03-s068
- `𝑁_{𝑝𝑎𝑖𝑟𝑠}=2` ← t03-s070
- `𝑃𝑎𝑖𝑟1(𝐿_{1}𝑎𝑛𝑑 𝐿_{4}):𝑦_{2}−𝑦_{3}−𝑦_{2} 𝑎𝑛𝑑 𝑦_{4}−𝑦_{5}−𝑦_{4}` ← t03-s070
- `𝑃𝑎𝑖𝑟1=𝑏𝑗∙𝑑𝑖` ← t03-s070
- `𝑃𝑎𝑖𝑟2 (𝐿_{1}𝑎𝑛𝑑 𝐿_{5}):𝑦_{2}−𝑦_{3}−𝑦_{2} 𝑎𝑛𝑑 𝑦_{5}−𝑦_{5}` ← t03-s070
- `𝑃𝑎𝑖𝑟2=𝑏𝑗∙𝑓` ← t03-s070
- `Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}=2` ← t03-s070
- `𝑃𝑎𝑖𝑟1(𝐿_{1}𝑎𝑛𝑑 𝐿_{4}):𝑦_{2}−𝑦_{3}−𝑦_{2} 𝑎𝑛𝑑 𝑦_{4}−𝑦_{5}−𝑦_{4} Gain 𝑃𝑎𝑖𝑟1=𝑏𝑗∙𝑑𝑖` ← t03-s070
- `𝑃𝑎𝑖𝑟2 (𝐿_{1}𝑎𝑛𝑑 𝐿_{5}):𝑦_{2}−𝑦_{3}−𝑦_{2} 𝑎𝑛𝑑 𝑦_{5}−𝑦_{5} Gain 𝑃𝑎𝑖𝑟2=𝑏𝑗∙𝑓` ← t03-s070
- `𝑁_{𝑡𝑟𝑖𝑝𝑙𝑒𝑡𝑠}=0` ← t03-s072
- `Δ 𝑎𝑛𝑑 Δ_{𝑖}` ← t03-s072
- `Number of 3 non-touching loops: 𝑁_{𝑡𝑟𝑖𝑝𝑙𝑒𝑡𝑠}=0` ← t03-s072
- `Δ=1−(𝑙_{1}+𝑙_{2}+𝑙_{3}+𝑙_{4}+𝑙_{5})+((𝑙_{1}∙𝑙_{4})+(𝑙_{1}∙𝑙_{5}))+0` ← t03-s074
- `Δ=1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓)` ← t03-s074
- `Δ=1−(𝑙_{1}+𝑙_{2}+𝑙_{3}+𝑙_{4}+𝑙_{5})+((𝑙_{1}∙𝑙_{4})+(𝑙_{1}∙𝑙_{5}))+0 Δ=1−(𝑙_{1}+𝑙_{2}+𝑙_{3}+𝑙_{4}+𝑙_{5})+((𝑙_{1}∙𝑙_{4})+(𝑙_{1}∙𝑙_{5}))+0` ← t03-s074
- `Δ=1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓)Δ=1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓)` ← t03-s074
- `Δ_{1}=1 Δ_{2}=1` ← t03-s075
- `Δ_{1}=1        Δ_{2}=1 Δ_{1}=1        Δ_{2}=1` ← t03-s075
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)=(𝑃_{1}Δ_{1})/(Δ)+(𝑃_{2}Δ_{2})/(Δ)=(𝑎𝑏𝑐𝑑𝑒+𝑎𝑏𝑔𝑒)/(1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓))` ← t03-s077
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)=(𝑃_{1}Δ_{1})/(Δ)+(𝑃_{2}Δ_{2})/(Δ)=(𝑎𝑏𝑐𝑑𝑒+𝑎𝑏𝑔𝑒)/(1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓))𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(∑_{𝑖=1}^{𝑁}(𝑃_{𝑖}Δ_{𝑖}))/(Δ)=(𝑃_{1}Δ_{1})/(Δ)+(𝑃_{2}Δ_{2})/(Δ)=(𝑎𝑏𝑐𝑑𝑒+𝑎𝑏𝑔𝑒)/(1−(𝑏𝑗+𝑔h+𝑐𝑑h+𝑑𝑖+𝑓)+(𝑏𝑗𝑑𝑖+𝑏𝑗𝑓))` ← t03-s077
- `𝑁=3` ← t03-s080
- `𝐺𝑎𝑖𝑛 𝑁_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}` ← t03-s080
- `𝐺𝑎𝑖𝑛 𝑁_{2}=𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}` ← t03-s080
- `𝐺𝑎𝑖𝑛 𝑁_{3}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}` ← t03-s080
- `Number of forward paths: 𝑁=3` ← t03-s080
- `𝐺𝑎𝑖𝑛 𝑁_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐺𝑎𝑖𝑛 𝑁_{1}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}` ← t03-s080
- `𝐺𝑎𝑖𝑛 𝑁_{2}=𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐺𝑎𝑖𝑛 𝑁_{2}=𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}` ← t03-s080
- `𝐺𝑎𝑖𝑛 𝑁_{3}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐺𝑎𝑖𝑛 𝑁_{3}=𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}` ← t03-s080
- `𝐿=8` ← t03-s082
- `𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}` ← t03-s082
- `𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}` ← t03-s082
- `𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}` ← t03-s082
- `𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}` ← t03-s082
- `𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}` ← t03-s082
- `𝐿_{6}=−𝐺_{4}𝐻_{4}` ← t03-s082
- `𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}` ← t03-s082
- `𝐿_{8}=−𝐺_{8}𝐻_{1}` ← t03-s082
- `Number of individual loops: 𝐿=8` ← t03-s082
- `𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}𝐿_{1}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}` ← t03-s082
- `𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}𝐿_{2}=−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}` ← t03-s082
- `𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}𝐿_{3}=−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}` ← t03-s082
- `𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}𝐿_{4}=−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}` ← t03-s082
- `𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}𝐿_{5}=−𝐺_{2}𝐺_{7}𝐻_{2}` ← t03-s082
- `𝐿_{6}=−𝐺_{4}𝐻_{4}𝐿_{6}=−𝐺_{4}𝐻_{4}` ← t03-s082
- `𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}𝐿_{7}=−𝐺_{5}𝐺_{6}𝐻_{1}` ← t03-s082
- `𝐿_{8}=−𝐺_{8}𝐻_{1}𝐿_{8}=−𝐺_{8}𝐻_{1}` ← t03-s082
- `𝑁_{𝑝𝑎𝑖𝑟𝑠}=` ← t03-s084
- `Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}= ?` ← t03-s084
- `𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{6}}=𝐺_{2}𝐺_{4}𝐺_{7}𝐻_{2}𝐻_{4}` ← t03-s087
- `𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{8}}=𝐺_{2}𝐺_{7}𝐺_{8}𝐻_{1}𝐻_{2}` ← t03-s087
- `𝐺𝑎𝑖𝑛_{𝐿_{3},𝐿_{6}}=𝐺_{1}𝐺_{2}𝐺_{4}𝐺_{7}𝐺_{6}𝐻_{3}𝐻_{4}` ← t03-s087
- `Number of 2 non-touching loops: 𝑁_{𝑝𝑎𝑖𝑟𝑠}= 3` ← t03-s087
- `𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{6}}=𝐺_{2}𝐺_{4}𝐺_{7}𝐻_{2}𝐻_{4}𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{6}}=𝐺_{2}𝐺_{4}𝐺_{7}𝐻_{2}𝐻_{4}` ← t03-s087
- `𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{8}}=𝐺_{2}𝐺_{7}𝐺_{8}𝐻_{1}𝐻_{2}𝐺𝑎𝑖𝑛_{𝐿_{5},𝐿_{8}}=𝐺_{2}𝐺_{7}𝐺_{8}𝐻_{1}𝐻_{2}` ← t03-s087
- `𝐺𝑎𝑖𝑛_{𝐿_{3},𝐿_{6}}=𝐺_{1}𝐺_{2}𝐺_{4}𝐺_{7}𝐺_{6}𝐻_{3}𝐻_{4}𝐺𝑎𝑖𝑛_{𝐿_{3},𝐿_{6}}=𝐺_{1}𝐺_{2}𝐺_{4}𝐺_{7}𝐺_{6}𝐻_{3}𝐻_{4}` ← t03-s087
- `Δ=1−(−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}−𝐺_{2}𝐺_{7}𝐻_{2}− 𝐺_{4}𝐻_{4}−𝐺_{5}𝐺_{6}𝐻_{1}−𝐺_{8}𝐻_{1})+(𝐺_{2}𝐺_{4}𝐺_{7}𝐻_{2}𝐻_{4}+𝐺_{2}𝐺_{7}𝐺_{8}𝐻_{1}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{4}𝐺_{7}𝐺_{6}𝐻_{3}𝐻_{4})+0` ← t03-s091
- `Δ=1−(−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐺_{6}𝐻_{3}−𝐺_{1}𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{8}𝐻_{3}−𝐺_{1}𝐺_{2}𝐺_{7}𝐺_{6}𝐻_{3}−𝐺_{2}𝐺_{3}𝐺_{4}𝐺_{5}𝐻_{2}−𝐺_{2}𝐺_{7}𝐻_{2}−                  𝐺_{4}𝐻_{4}−𝐺_{5}𝐺_{6}𝐻_{1}−𝐺_{8}𝐻_{1})+(𝐺_{2}𝐺_{4}𝐺_{7}𝐻_{2}𝐻_{4}+𝐺_{2}𝐺_{7}𝐺_{8}𝐻_{1}𝐻_{2}+𝐺_{1}𝐺_{2}𝐺_{4}𝐺_{7}𝐺_{6}𝐻_{3}𝐻_{4})+0` ← t03-s091
- `Δ_{1}` ← t03-s092
- `Δ_{1}=1 Δ_{1}=1` ← t03-s092
- `Δ_{2}` ← t03-s093
- `Δ_{2}=1−𝐿_{6}=1+𝐺_{4}𝐻_{4}` ← t03-s093
- `Loop 𝐿_{6}=−𝐺_{4}𝐻_{4} does not touch path 2` ← t03-s093
- `Δ_{2}=1−𝐿_{6}=1+𝐺_{4}𝐻_{4}Δ_{2}=1−𝐿_{6}=1+𝐺_{4}𝐻_{4}` ← t03-s093
- `Δ_{3}` ← t03-s094
- `Δ_{3}=1` ← t03-s094
- `Δ_{3}=1 Δ_{3}=1` ← t03-s094
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}+𝑃_{2}(𝑠)Δ_{2}+𝑃_{3}(𝑠)Δ_{3})/(Δ(𝑠))` ← t03-s096
- `𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}+𝑃_{2}(𝑠)Δ_{2}+𝑃_{3}(𝑠)Δ_{3})/(Δ(𝑠))𝑇(𝑠)=(𝑌(𝑠))/(𝑅(𝑠))=(𝑃_{1}(𝑠)Δ_{1}+𝑃_{2}(𝑠)Δ_{2}+𝑃_{3}(𝑠)Δ_{3})/(Δ(𝑠))` ← t03-s096
