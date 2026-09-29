# Topic 2: Mathematical Models & Laplace Transform

Source: `ELE442_Topic2_Mathematical_Models_Laplace_Transform (2).pptx`
Slides: 56 · Notes: 11 · Media refs: 115

## Learning map

- **formula**: 27 slides
- **example**: 14 slides
- **derivation**: 5 slides
- **definition**: 4 slides
- **property**: 3 slides
- **figure**: 2 slides
- **content**: 1 slides

## Slide knowledge cards

### t02-s001 — ELE 442 – Control Systems

Tags: formula

Content:
- ELE 442 – Control Systems
- Topic 2: Mathematical Models of Systems Laplace Transform

---

### t02-s002 — Mathematical Models

Tags: formula

Content:
- Mathematical Models
- Key elements in design and analysis of control systems
- Quantitative representation of the system
- Relationship between system variables
- Dynamic behaviour is described by Ordinary Differential Equations
- ODEs are hard to solve
- We will use Laplace Transform to simplify the equations and operations

---

### t02-s003 — Mathematical Models

Tags: formula

Content:
- Mathematical Models
- Laplace Transform requires the system to be linear
- Most systems are usually nonlinear in nature
- We have to apply linearization techniques on the system model
- This forces us to make assumptions

---

### t02-s004 — Dynamic System Modeling - Outline

Tags: derivation, objectives

Content:
- Dynamic System Modeling - Outline
- Define the system and its components.
- Formulate the mathematical model and fundamental necessary assumptions based on basic principles.
- Obtain the differential equations representing the mathematical model.
- Solve the equations for the desired output variables.
- Examine the solutions and the assumptions.
- If necessary, reanalyze or redesign the system.

---

### t02-s005 — Differential Equations of Physical Systems

Tags: formula, figure

Content:
- Differential Equations of Physical Systems
- Spring-mass damper system
- Newton’s Second Law of Motion
- 𝐹=𝑀𝑎
- ∑_{}^{}(𝐹)=𝑀𝑦
- −𝑘𝑦(𝑡)−𝑏𝑦(𝑡)+𝐹_{𝑒𝑥𝑡𝑒𝑟𝑛𝑎𝑙}=𝑀𝑦(𝑡)
- 𝑀(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦(𝑡))/(𝑑𝑡)+𝑘𝑦(𝑡)=𝑟(𝑡)
- 2 nd order NONHOMOGENEOUS differential equation
- 𝑅𝐻𝑆≠0 𝑅𝐻𝑆≠0

Equations / relations:
- `𝐹=𝑀𝑎`
- `∑_{}^{}(𝐹)=𝑀𝑦`
- `−𝑘𝑦(𝑡)−𝑏𝑦(𝑡)+𝐹_{𝑒𝑥𝑡𝑒𝑟𝑛𝑎𝑙}=𝑀𝑦(𝑡)`
- `𝑀(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦(𝑡))/(𝑑𝑡)+𝑘𝑦(𝑡)=𝑟(𝑡)`
- `𝑅𝐻𝑆≠0`

Media:
- `media/image2.png`
- `media/image2.jpeg`
- `media/image4.png`

---

### t02-s006 — Differential Equations of Physical Systems

Tags: figure

Content:
- Differential Equations of Physical Systems
- Spring-mass damper system
- Equivalent to Parallel RLC circuit
- 𝑀(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦(𝑡))/(𝑑𝑡)+𝑘𝑦(𝑡)=𝑟(𝑡) (𝑣(𝑡))/(𝑅)+𝐶(𝑑𝑣(𝑡))/(𝑑𝑡)+(1)/(𝐿)∫_{0}^{𝑡}(𝑣(𝑡)𝑑(𝑡))=𝑟(𝑡)

Equations / relations:
- `𝑀(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦(𝑡))/(𝑑𝑡)+𝑘𝑦(𝑡)=𝑟(𝑡)`
- `(𝑣(𝑡))/(𝑅)+𝐶(𝑑𝑣(𝑡))/(𝑑𝑡)+(1)/(𝐿)∫_{0}^{𝑡}(𝑣(𝑡)𝑑(𝑡))=𝑟(𝑡)`
- `𝑀(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦(𝑡))/(𝑑𝑡)+𝑘𝑦(𝑡)=𝑟(𝑡) (𝑣(𝑡))/(𝑅)+𝐶(𝑑𝑣(𝑡))/(𝑑𝑡)+(1)/(𝐿)∫_{0}^{𝑡}(𝑣(𝑡)𝑑(𝑡))=𝑟(𝑡)`

Media:
- `media/image5.png`
- `media/image3.jpeg`
- `media/image6.png`

---

### t02-s007 — Differential Equations of Physical Systems

Tags: formula, procedure, figure

Content:
- Differential Equations of Physical Systems
- 𝑀(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦(𝑡))/(𝑑𝑡)+𝑘𝑦(𝑡)=𝑟(𝑡)
- How to solve?
- Write the general solution for 𝑦(𝑡)
- in the form 𝑦(𝑡)=𝑦_{𝑐}(𝑡)+𝑦_{𝑝}(𝑡)
- 𝑦_{𝑐}(𝑡) is the complementary solution to 𝑀(𝑑^{2}𝑦_{𝑐}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑐}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑐}(𝑡)=0
- 𝑦_{𝑝}(𝑡) is the particular solution to 𝑀(𝑑^{2}𝑦_{𝑝}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑝}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑝}(𝑡)=𝑟(𝑡)

Equations / relations:
- `𝑀(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦(𝑡))/(𝑑𝑡)+𝑘𝑦(𝑡)=𝑟(𝑡)`
- `𝑦(𝑡)`
- `𝑦(𝑡)=𝑦_{𝑐}(𝑡)+𝑦_{𝑝}(𝑡)`
- `𝑦_{𝑐}(𝑡)`
- `𝑀(𝑑^{2}𝑦_{𝑐}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑐}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑐}(𝑡)=0`
- `𝑦_{𝑝}(𝑡)`
- `𝑀(𝑑^{2}𝑦_{𝑝}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑝}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑝}(𝑡)=𝑟(𝑡)`
- `in the form 𝑦(𝑡)=𝑦_{𝑐}(𝑡)+𝑦_{𝑝}(𝑡)`
- `𝑦_{𝑐}(𝑡) is the complementary solution to 𝑀(𝑑^{2}𝑦_{𝑐}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑐}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑐}(𝑡)=0`
- `𝑦_{𝑝}(𝑡) is the particular solution to 𝑀(𝑑^{2}𝑦_{𝑝}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑝}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑝}(𝑡)=𝑟(𝑡)`

Media:
- `media/image10.png`
- `media/image7.jpeg`

---

### t02-s008 — 𝑒^{𝜆𝑡}≠0 𝑒^{𝜆𝑡}≠0

Tags: formula, figure

Content:
- 𝑒^{𝜆𝑡}≠0 𝑒^{𝜆𝑡}≠0
- 1. 𝑀(𝑑^{2}𝑦_{𝑐}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑐}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑐}(𝑡)=0
- Make an educated guess 𝑦_{𝑐}(𝑡)=𝑒^{𝜆𝑡}
- (𝑑𝑦_{𝑐})/(𝑑𝑡)=𝜆𝑒^{𝜆𝑡}            (𝑑^{2}𝑦_{𝑐})/(𝑑𝑡^{2})=𝜆^{2}𝑒^{𝜆𝑡}(𝑑𝑦_{𝑐})/(𝑑𝑡)=𝜆𝑒^{𝜆𝑡}            (𝑑^{2}𝑦_{𝑐})/(𝑑𝑡^{2})=𝜆^{2}𝑒^{𝜆𝑡}
- 𝑀𝜆^{2}𝑒^{𝜆𝑡}+𝑏𝜆𝑒^{𝜆𝑡}+𝑘𝑒^{𝜆𝑡}=0 𝑀𝜆^{2}𝑒^{𝜆𝑡}+𝑏𝜆𝑒^{𝜆𝑡}+𝑘𝑒^{𝜆𝑡}=0
- 𝑀𝜆^{2}+𝑏𝜆+𝑘=0 𝑀𝜆^{2}+𝑏𝜆+𝑘=0
- Solving the quadratic equation  roots 𝜆_{1} & 𝜆_{2}
- Differential Equations of Physical Systems
- Now we only have to solve a quadratic equation

Equations / relations:
- `𝑒^{𝜆𝑡}≠0`
- `𝑀(𝑑^{2}𝑦_{𝑐}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑐}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑐}(𝑡)=0`
- `𝑦_{𝑐}(𝑡)=𝑒^{𝜆𝑡}`
- `(𝑑𝑦_{𝑐})/(𝑑𝑡)=𝜆𝑒^{𝜆𝑡} (𝑑^{2}𝑦_{𝑐})/(𝑑𝑡^{2})=𝜆^{2}𝑒^{𝜆𝑡}`
- `𝑀𝜆^{2}𝑒^{𝜆𝑡}+𝑏𝜆𝑒^{𝜆𝑡}+𝑘𝑒^{𝜆𝑡}=0`
- `𝑀𝜆^{2}+𝑏𝜆+𝑘=0`
- `𝜆_{1} & 𝜆_{2}`
- `1. 𝑀(𝑑^{2}𝑦_{𝑐}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑐}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑐}(𝑡)=0`
- `Make an educated guess 𝑦_{𝑐}(𝑡)=𝑒^{𝜆𝑡}`
- `(𝑑𝑦_{𝑐})/(𝑑𝑡)=𝜆𝑒^{𝜆𝑡}            (𝑑^{2}𝑦_{𝑐})/(𝑑𝑡^{2})=𝜆^{2}𝑒^{𝜆𝑡}(𝑑𝑦_{𝑐})/(𝑑𝑡)=𝜆𝑒^{𝜆𝑡}            (𝑑^{2}𝑦_{𝑐})/(𝑑𝑡^{2})=𝜆^{2}𝑒^{𝜆𝑡}`
- `𝑀𝜆^{2}𝑒^{𝜆𝑡}+𝑏𝜆𝑒^{𝜆𝑡}+𝑘𝑒^{𝜆𝑡}=0 𝑀𝜆^{2}𝑒^{𝜆𝑡}+𝑏𝜆𝑒^{𝜆𝑡}+𝑘𝑒^{𝜆𝑡}=0`
- `𝑀𝜆^{2}+𝑏𝜆+𝑘=0 𝑀𝜆^{2}+𝑏𝜆+𝑘=0`

Media:
- `media/image13.png`
- `media/image15.png`
- `media/image7.jpeg`

---

### t02-s009 — If 𝜆_{1} & 𝜆_{2} are real and 𝜆_{1}≠𝜆_{2}

Tags: formula, figure

Content:
- If 𝜆_{1} & 𝜆_{2} are real and 𝜆_{1}≠𝜆_{2}
- 𝑦_{𝑐}(𝑡)=𝐴𝑒^{𝜆_{1}𝑡}+𝐵𝑒^{𝜆_{2}𝑡} (𝐴 and 𝐵 are constants)
- If 𝜆_{1}=𝜆_{2}
- 𝑦_{𝑐}(𝑡)=(𝐴+𝐵)𝑒^{𝜆_{1}𝑡}
- If 𝜆_{1} & 𝜆_{2} are complex conjugates
- 𝜆_{1}=𝑟+𝑖𝑠           𝜆_{2}=𝑟−𝑖𝑠
- 𝑦_{𝑐}(𝑡)=𝑒^{𝑟𝑡}(𝐴cos((𝑠𝑡))+𝐵sin((𝑠𝑡)))
- To find the values of constants A and B the initial conditions are needed
- Differential Equations of Physical Systems

Equations / relations:
- `𝜆_{1} & 𝜆_{2}`
- `𝜆_{1}≠𝜆_{2}`
- `𝑦_{𝑐}(𝑡)=𝐴𝑒^{𝜆_{1}𝑡}+𝐵𝑒^{𝜆_{2}𝑡}`
- `𝐴`
- `𝐵`
- `𝜆_{1}=𝜆_{2}`
- `𝑦_{𝑐}(𝑡)=(𝐴+𝐵)𝑒^{𝜆_{1}𝑡}`
- `𝜆_{1}=𝑟+𝑖𝑠 𝜆_{2}=𝑟−𝑖𝑠`
- `𝑦_{𝑐}(𝑡)=𝑒^{𝑟𝑡}(𝐴cos((𝑠𝑡))+𝐵sin((𝑠𝑡)))`
- `𝑦_{𝑐}(𝑡)=𝐴𝑒^{𝜆_{1}𝑡}+𝐵𝑒^{𝜆_{2}𝑡} (𝐴 and 𝐵 are constants)`
- `If 𝜆_{1}=𝜆_{2}`
- `𝜆_{1}=𝑟+𝑖𝑠           𝜆_{2}=𝑟−𝑖𝑠`

Media:
- `media/image8.png`
- `media/image7.jpeg`

---

### t02-s010 — 1. 𝑀(𝑑^{2}𝑦_{𝑐}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑐}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑐}(𝑡)=0

Tags: example, formula, figure

Content:
- 1. 𝑀(𝑑^{2}𝑦_{𝑐}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑐}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑐}(𝑡)=0
- Let’s take a numeric example
- 𝑀=1,    𝑏=2,    𝑘=5 𝑀=1,    𝑏=2,    𝑘=5
- (𝑑𝑦_{𝑐})/(𝑑𝑡)=𝜆𝑒^{𝜆𝑡}            (𝑑^{2}𝑦_{𝑐})/(𝑑𝑡^{2})=𝜆^{2}𝑒^{𝜆𝑡}
- 𝜆^{2}𝑒^{𝜆𝑡}+2𝜆𝑒^{𝜆𝑡}+5𝑒^{𝜆𝑡}=0
- 𝜆^{2}+2𝜆+5=0
- 𝑒^{𝜆𝑡}≠0 𝑒^{𝜆𝑡}≠0
- Differential Equations of Physical Systems
- 𝜆_{1,2}=(−2±sqrt(4−20))/(2)=−1±2𝑖
- 𝑦_{𝑐}(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))𝑦_{𝑐}(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))
- Next, we solve for 𝑦_{𝑝}(𝑡)

Equations / relations:
- `𝑀(𝑑^{2}𝑦_{𝑐}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑐}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑐}(𝑡)=0`
- `𝑀=1, 𝑏=2, 𝑘=5`
- `(𝑑𝑦_{𝑐})/(𝑑𝑡)=𝜆𝑒^{𝜆𝑡} (𝑑^{2}𝑦_{𝑐})/(𝑑𝑡^{2})=𝜆^{2}𝑒^{𝜆𝑡}`
- `𝜆^{2}𝑒^{𝜆𝑡}+2𝜆𝑒^{𝜆𝑡}+5𝑒^{𝜆𝑡}=0`
- `𝜆^{2}+2𝜆+5=0`
- `𝑒^{𝜆𝑡}≠0`
- `𝜆_{1,2}=(−2±sqrt(4−20))/(2)=−1±2𝑖`
- `𝑦_{𝑐}(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))`
- `𝑦_{𝑝}(𝑡)`
- `1. 𝑀(𝑑^{2}𝑦_{𝑐}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑐}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑐}(𝑡)=0`
- `𝑀=1,    𝑏=2,    𝑘=5 𝑀=1,    𝑏=2,    𝑘=5`
- `(𝑑𝑦_{𝑐})/(𝑑𝑡)=𝜆𝑒^{𝜆𝑡}            (𝑑^{2}𝑦_{𝑐})/(𝑑𝑡^{2})=𝜆^{2}𝑒^{𝜆𝑡}`
- `𝑦_{𝑐}(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))𝑦_{𝑐}(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))`

Media:
- `media/image9.png`
- `media/image7.jpeg`
- `media/image18.png`
- `media/image11.png`
- `media/image12.png`
- `media/image14.png`

---

### t02-s011 — 2. 𝑀(𝑑^{2}𝑦_{𝑝}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑝}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑝}(𝑡)=𝑟(𝑡)

Tags: example, formula, figure

Content:
- 2. 𝑀(𝑑^{2}𝑦_{𝑝}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑝}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑝}(𝑡)=𝑟(𝑡)
- Let’s go back to the numeric example
- 𝑀=1,    𝑏=2,    𝑘=5,    𝑟(𝑡)=5𝑡^{2}+12 𝑀=1,    𝑏=2,    𝑘=5,    𝑟(𝑡)=5𝑡^{2}+12
- We choose 𝑦_{𝑝}(𝑡)=𝑃𝑡^{2}+𝑄𝑡+𝐿 (𝑃, 𝑄 and L are constants)
- (𝑑𝑦_{𝑝})/(𝑑𝑡)=2𝑃𝑡+𝑄            (𝑑^{2}𝑦_{𝑝})/(𝑑𝑡^{2})=2𝑃
- 2𝑃+4𝑃𝑡+2𝑄+5𝑃𝑡^{2}+5𝑄𝑡+5𝐿=5𝑡^{2}+12
- Equating coefficients  𝑃=1        𝑄=−(4)/(5)        𝐿=(58)/(25)
- 𝑦_{𝑝}(𝑡)=𝑡^{2}−(4)/(5)𝑡+(58)/(25)𝑦_{𝑝}(𝑡)=𝑡^{2}−(4)/(5)𝑡+(58)/(25)
- Differential Equations of Physical Systems
- (2𝑃+2𝑄+5𝐿=12 ; 4𝑃+5𝑄=0 ; 5𝑃=5)(2𝑃+2𝑄+5𝐿=12 ; 4𝑃+5𝑄=0 ; 5𝑃=5)

Equations / relations:
- `𝑀(𝑑^{2}𝑦_{𝑝}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑝}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑝}(𝑡)=𝑟(𝑡)`
- `𝑀=1, 𝑏=2, 𝑘=5, 𝑟(𝑡)=5𝑡^{2}+12`
- `𝑦_{𝑝}(𝑡)=𝑃𝑡^{2}+𝑄𝑡+𝐿`
- `𝑃`
- `𝑄`
- `(𝑑𝑦_{𝑝})/(𝑑𝑡)=2𝑃𝑡+𝑄 (𝑑^{2}𝑦_{𝑝})/(𝑑𝑡^{2})=2𝑃`
- `2𝑃+4𝑃𝑡+2𝑄+5𝑃𝑡^{2}+5𝑄𝑡+5𝐿=5𝑡^{2}+12`
- `𝑃=1 𝑄=−(4)/(5) 𝐿=(58)/(25)`
- `𝑦_{𝑝}(𝑡)=𝑡^{2}−(4)/(5)𝑡+(58)/(25)`
- `(2𝑃+2𝑄+5𝐿=12 ; 4𝑃+5𝑄=0 ; 5𝑃=5)`
- `2. 𝑀(𝑑^{2}𝑦_{𝑝}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑝}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑝}(𝑡)=𝑟(𝑡)`
- `𝑀=1,    𝑏=2,    𝑘=5,    𝑟(𝑡)=5𝑡^{2}+12 𝑀=1,    𝑏=2,    𝑘=5,    𝑟(𝑡)=5𝑡^{2}+12`
- `We choose 𝑦_{𝑝}(𝑡)=𝑃𝑡^{2}+𝑄𝑡+𝐿 (𝑃, 𝑄 and L are constants)`
- `(𝑑𝑦_{𝑝})/(𝑑𝑡)=2𝑃𝑡+𝑄            (𝑑^{2}𝑦_{𝑝})/(𝑑𝑡^{2})=2𝑃`
- `Equating coefficients  𝑃=1        𝑄=−(4)/(5)        𝐿=(58)/(25)`
- `𝑦_{𝑝}(𝑡)=𝑡^{2}−(4)/(5)𝑡+(58)/(25)𝑦_{𝑝}(𝑡)=𝑡^{2}−(4)/(5)𝑡+(58)/(25)`
- `(2𝑃+2𝑄+5𝐿=12 ; 4𝑃+5𝑄=0 ; 5𝑃=5)(2𝑃+2𝑄+5𝐿=12 ; 4𝑃+5𝑄=0 ; 5𝑃=5)`

Media:
- `media/image22.png`
- `media/image7.jpeg`
- `media/image23.png`

---

### t02-s012 — 𝑀(𝑑^{2}𝑦_{𝑝}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑝}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑝}(𝑡)=𝑟(𝑡)

Tags: formula, figure

Content:
- 𝑀(𝑑^{2}𝑦_{𝑝}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑝}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑝}(𝑡)=𝑟(𝑡)
- General solution
- 𝑦(𝑡)=𝑦_{𝑐}(𝑡)+𝑦_{𝑝}(𝑡)𝑦(𝑡)=𝑦_{𝑐}(𝑡)+𝑦_{𝑝}(𝑡)
- 𝑦(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))+𝑡^{2}−(4)/(5)𝑡+(58)/(25)𝑦(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))+𝑡^{2}−(4)/(5)𝑡+(58)/(25)
- To find the values of constants A and B the initial conditions are needed
- Differential Equations of Physical Systems

Equations / relations:
- `𝑀(𝑑^{2}𝑦_{𝑝}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑝}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑝}(𝑡)=𝑟(𝑡)`
- `𝑦(𝑡)=𝑦_{𝑐}(𝑡)+𝑦_{𝑝}(𝑡)`
- `𝑦(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))+𝑡^{2}−(4)/(5)𝑡+(58)/(25)`
- `𝑦(𝑡)=𝑦_{𝑐}(𝑡)+𝑦_{𝑝}(𝑡)𝑦(𝑡)=𝑦_{𝑐}(𝑡)+𝑦_{𝑝}(𝑡)`
- `𝑦(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))+𝑡^{2}−(4)/(5)𝑡+(58)/(25)𝑦(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))+𝑡^{2}−(4)/(5)𝑡+(58)/(25)`

Media:
- `media/image230.png`
- `media/image7.jpeg`

---

### t02-s013 — Differential Equations of Physical Systems

Tags: content

Content:
- Differential Equations of Physical Systems
- What about higher order ODEs?
- Solving those equations in the traditional way can be very complicated and time consuming
- There must be an easier alternative to solve these equations

---

### t02-s014 — Linearity and Time-Invariance

Tags: definition, property, figure

Content:
- Linearity and Time-Invariance
- Excitation 𝑥(𝑡)  Response 𝑦(𝑡)
- What is a linear system?
- A linear system satisfies two properties:
- Superposition
- Homogeneity

Equations / relations:
- `𝑥(𝑡)`
- `𝑦(𝑡)`

Media:
- `media/image810.png`

---

### t02-s015 — Linearity and Time-Invariance

Tags: property, figure

Content:
- Linearity and Time-Invariance
- Excitation 𝑥(𝑡)  Response 𝑦(𝑡)
- Superposition
- If 𝑥_{1}(𝑡)  𝑦_{1}(𝑡) & 𝑥_{2}(𝑡)  𝑦_{2}(𝑡)
- then 𝑥_{1}(𝑡)+𝑥_{2}(𝑡)  𝑦_{1}(𝑡)+𝑦_{2}(𝑡)
- 𝑦(𝑥_{1}+𝑥_{2})=𝑦(𝑥_{1})+𝑦(𝑥_{2})

Equations / relations:
- `𝑥(𝑡)`
- `𝑦(𝑡)`
- `𝑥_{1}(𝑡)`
- `𝑦_{1}(𝑡)`
- `𝑥_{2}(𝑡)`
- `𝑦_{2}(𝑡)`
- `𝑥_{1}(𝑡)+𝑥_{2}(𝑡)`
- `𝑦_{1}(𝑡)+𝑦_{2}(𝑡)`
- `𝑦(𝑥_{1}+𝑥_{2})=𝑦(𝑥_{1})+𝑦(𝑥_{2})`

Media:
- `media/image17.png`

---

### t02-s016 — Excitation 𝑥(𝑡)  Response 𝑦(𝑥(𝑡))

Tags: property, figure

Content:
- Excitation 𝑥(𝑡)  Response 𝑦(𝑥(𝑡))
- Homogeneity
- If 𝑥(𝑡)  𝑦(𝑡)
- then 𝛽𝑥(𝑡) 𝛽𝑦(𝑡)
- 𝑦(𝛽𝑥(𝑡))=𝛽𝑦(𝑥(𝑡))
- Linearity and Time-Invariance

Equations / relations:
- `𝑥(𝑡)`
- `𝑦(𝑥(𝑡))`
- `𝑦(𝑡)`
- `𝛽𝑥(𝑡)`
- `𝛽𝑦(𝑡)`
- `𝑦(𝛽𝑥(𝑡))=𝛽𝑦(𝑥(𝑡))`

Media:
- `media/image19.png`

---

### t02-s017 — Linearity and Time-Invariance

Tags: formula, property, figure

Content:
- Linearity and Time-Invariance
- Are the following systems linear?
- System 1: 𝑦(𝑡)=2 𝑥(𝑡)+10
- Superposition
- 𝑦_{1}(𝑡)=2 𝑥_{1}(𝑡)+10              𝑦_{2}(𝑡)=2 𝑥_{2}(𝑡)+10 𝑦_{1}(𝑡)=2 𝑥_{1}(𝑡)+10              𝑦_{2}(𝑡)=2 𝑥_{2}(𝑡)+10
- 𝑦(𝑥_{1}+𝑥_{2})=2(𝑥_{1}+𝑥_{2})+10
- 𝑦_{1}(𝑡)+𝑦_{2}(𝑡)=2(𝑥_{1}+𝑥_{2})+20
- 𝑦(𝑥_{1}+𝑥_{2})≠𝑦_{1}(𝑡)+𝑦_{2}(𝑡) The system is not linear

Equations / relations:
- `𝑦(𝑡)=2 𝑥(𝑡)+10`
- `𝑦_{1}(𝑡)=2 𝑥_{1}(𝑡)+10 𝑦_{2}(𝑡)=2 𝑥_{2}(𝑡)+10`
- `𝑦(𝑥_{1}+𝑥_{2})=2(𝑥_{1}+𝑥_{2})+10`
- `𝑦_{1}(𝑡)+𝑦_{2}(𝑡)=2(𝑥_{1}+𝑥_{2})+20`
- `𝑦(𝑥_{1}+𝑥_{2})≠𝑦_{1}(𝑡)+𝑦_{2}(𝑡)`
- `System 1: 𝑦(𝑡)=2 𝑥(𝑡)+10`
- `𝑦_{1}(𝑡)=2 𝑥_{1}(𝑡)+10              𝑦_{2}(𝑡)=2 𝑥_{2}(𝑡)+10 𝑦_{1}(𝑡)=2 𝑥_{1}(𝑡)+10              𝑦_{2}(𝑡)=2 𝑥_{2}(𝑡)+10`

Media:
- `media/image20.png`

---

### t02-s018 — Are the following systems linear?

Tags: formula, property, figure

Content:
- Are the following systems linear?
- System 2: 𝑦(𝑡)=𝑥^{2}(𝑡)
- Homogeneity
- 𝑦(𝛽𝑥)=(𝛽𝑥)^{2}                             𝛽𝑦(𝑥)=𝛽𝑥^{2}𝑦(𝛽𝑥)=(𝛽𝑥)^{2}                             𝛽𝑦(𝑥)=𝛽𝑥^{2}
- 𝑦(𝛽𝑥)≠𝛽𝑦(𝑥)
- The system is not linear
- Linearity and Time-Invariance

Equations / relations:
- `𝑦(𝑡)=𝑥^{2}(𝑡)`
- `𝑦(𝛽𝑥)=(𝛽𝑥)^{2} 𝛽𝑦(𝑥)=𝛽𝑥^{2}`
- `𝑦(𝛽𝑥)≠𝛽𝑦(𝑥)`
- `System 2: 𝑦(𝑡)=𝑥^{2}(𝑡)`
- `𝑦(𝛽𝑥)=(𝛽𝑥)^{2}                             𝛽𝑦(𝑥)=𝛽𝑥^{2}𝑦(𝛽𝑥)=(𝛽𝑥)^{2}                             𝛽𝑦(𝑥)=𝛽𝑥^{2}`

Media:
- `media/image21.png`

---

### t02-s019 — Linearity and Time-Invariance

Tags: definition, formula, property, figure

Content:
- Linearity and Time-Invariance
- Excitation 𝑥(𝑡)  Response 𝑦(𝑡)
- What is a time-invariant system?
- The relationship between the excitation function 𝑥(𝑡) and the output function 𝑦(𝑡) is constant with respect to time.
- 𝑥(𝑡)  𝑦(𝑡) & 𝑥_{𝑑}(𝑡)=𝑥(𝑡+𝛿)  𝑦_{1}(𝑡) & 𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)
- If 𝑦_{1}(𝑡)=𝑦_{2}(𝑡)
- then The system is time-invariant

Equations / relations:
- `𝑥(𝑡)`
- `𝑦(𝑡)`
- `𝑥_{𝑑}(𝑡)=𝑥(𝑡+𝛿)`
- `𝑦_{1}(𝑡)`
- `𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)`
- `𝑦_{1}(𝑡)=𝑦_{2}(𝑡)`
- `𝑥(𝑡)  𝑦(𝑡) & 𝑥_{𝑑}(𝑡)=𝑥(𝑡+𝛿)  𝑦_{1}(𝑡) & 𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)`
- `If 𝑦_{1}(𝑡)=𝑦_{2}(𝑡)`

Media:
- `media/image24.png`

---

### t02-s020 — Are the following systems time-invariant?

Tags: formula, property, figure

Content:
- Are the following systems time-invariant?
- System 1: 𝑦(𝑡)=10𝑥(𝑡)
- 𝑦_{1}(𝑡)=10𝑥_{𝑑}(𝑡)=10𝑥(𝑡+𝛿)                    𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=10𝑥(𝑡+𝛿)𝑦_{1}(𝑡)=10𝑥_{𝑑}(𝑡)=10𝑥(𝑡+𝛿)                    𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=10𝑥(𝑡+𝛿)
- 𝑦_{1}(𝑡)=𝑦_{2}(𝑡)
- The system is time-invariant
- Linearity and Time-Invariance

Equations / relations:
- `𝑦(𝑡)=10𝑥(𝑡)`
- `𝑦_{1}(𝑡)=10𝑥_{𝑑}(𝑡)=10𝑥(𝑡+𝛿) 𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=10𝑥(𝑡+𝛿)`
- `𝑦_{1}(𝑡)=𝑦_{2}(𝑡)`
- `System 1: 𝑦(𝑡)=10𝑥(𝑡)`
- `𝑦_{1}(𝑡)=10𝑥_{𝑑}(𝑡)=10𝑥(𝑡+𝛿)                    𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=10𝑥(𝑡+𝛿)𝑦_{1}(𝑡)=10𝑥_{𝑑}(𝑡)=10𝑥(𝑡+𝛿)                    𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=10𝑥(𝑡+𝛿)`

Media:
- `media/image25.png`

---

### t02-s021 — Are the following systems time-invariant?

Tags: formula, property, figure

Content:
- Are the following systems time-invariant?
- System 2: 𝑦(𝑡)=𝑡∙𝑥(𝑡)
- 𝑦_{1}(𝑡)=𝑡∙𝑥_{𝑑}(𝑡)=𝑡∙𝑥(𝑡+𝛿)           𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=(𝑡+𝛿)∙𝑥(𝑡+𝛿)𝑦_{1}(𝑡)=𝑡∙𝑥_{𝑑}(𝑡)=𝑡∙𝑥(𝑡+𝛿)           𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=(𝑡+𝛿)∙𝑥(𝑡+𝛿)
- 𝑦_{1}(𝑡)≠𝑦_{2}(𝑡)
- The system is not time-invariant
- Linearity and Time-Invariance

Equations / relations:
- `𝑦(𝑡)=𝑡∙𝑥(𝑡)`
- `𝑦_{1}(𝑡)=𝑡∙𝑥_{𝑑}(𝑡)=𝑡∙𝑥(𝑡+𝛿) 𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=(𝑡+𝛿)∙𝑥(𝑡+𝛿)`
- `𝑦_{1}(𝑡)≠𝑦_{2}(𝑡)`
- `System 2: 𝑦(𝑡)=𝑡∙𝑥(𝑡)`
- `𝑦_{1}(𝑡)=𝑡∙𝑥_{𝑑}(𝑡)=𝑡∙𝑥(𝑡+𝛿)           𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=(𝑡+𝛿)∙𝑥(𝑡+𝛿)𝑦_{1}(𝑡)=𝑡∙𝑥_{𝑑}(𝑡)=𝑡∙𝑥(𝑡+𝛿)           𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=(𝑡+𝛿)∙𝑥(𝑡+𝛿)`

Media:
- `media/image26.png`

---

### t02-s022 — In reality most systems are non-linear or linear in a given range.

Tags: property

Content:
- In reality most systems are non-linear or linear in a given range.
- Nevertheless, linearity is an approximation, which greatly simplifies the analysis of systems.
- In many control applications, the normal operation of the system may be around an equilibrium point.
- Furthermore, the signals may be considered to vary very little around this equilibrium point.
- In such conditions, it is possible to linearize the system.
- Linear Approximation of Physical Systems

---

### t02-s023 — Linear Approximation of Physical Systems

Tags: figure

Content:
- Linear Approximation of Physical Systems
- This linear approximation is only valid for a limited range.
- To linearize a function we perform a Taylor series expansion about the equilibrium point and only use the linear components of this expansion.

Media:
- `media/image16.png`

---

### t02-s024 — Linear Approximation of Physical Systems

Tags: formula, figure

Content:
- Linear Approximation of Physical Systems
- Consider a system whose input is 𝑥 and output is 𝑦.
- 𝑦(𝑡)=𝑔(𝑥(𝑡))𝑦(𝑡)=𝑔(𝑥(𝑡))
- Assume the normal operating conditions are 𝑥_{0} and 𝑦_{0} expand (Taylor) the above equation about these points:
- 𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)+((𝑑^{2}𝑔)/(𝑑𝑥^{2}))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0})^{2})/(2!)+…𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)+((𝑑^{2}𝑔)/(𝑑𝑥^{2}))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0})^{2})/(2!)+…

Equations / relations:
- `𝑥`
- `𝑦`
- `𝑦(𝑡)=𝑔(𝑥(𝑡))`
- `𝑥_{0}`
- `𝑦_{0}`
- `𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)+((𝑑^{2}𝑔)/(𝑑𝑥^{2}))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0})^{2})/(2!)+…`
- `𝑦(𝑡)=𝑔(𝑥(𝑡))𝑦(𝑡)=𝑔(𝑥(𝑡))`
- `𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)+((𝑑^{2}𝑔)/(𝑑𝑥^{2}))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0})^{2})/(2!)+…𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)+((𝑑^{2}𝑔)/(𝑑𝑥^{2}))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0})^{2})/(2!)+…`

Media:
- `media/image30.png`

---

### t02-s025 — Operating around the equilibrium point 𝑥_{0}, we can get rid of the higher order part of the Taylor Series Expansion.

Tags: formula, figure

Content:
- Operating around the equilibrium point 𝑥_{0}, we can get rid of the higher order part of the Taylor Series Expansion.
- 𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)
- Slope at the operating point
- Linear Approximation of Physical Systems

Equations / relations:
- `𝑥_{0}`
- `𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)`
- `𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)`

Media:
- `media/image31.png`

---

### t02-s026 — Example – Pendulum oscillator model

Tags: example, formula, figure

Content:
- Example – Pendulum oscillator model
- 𝑇(𝑡)=𝑀𝑔𝐿sin(𝜃(𝑡))𝑇(𝑡)=𝑀𝑔𝐿sin(𝜃(𝑡))
- Equilibrium point: 𝜃_{0}=0
- First derivative at equilibrium provides linear approximation
- Linear Approximation of Physical Systems

Equations / relations:
- `𝑇(𝑡)=𝑀𝑔𝐿sin(𝜃(𝑡))`
- `𝜃_{0}=0`
- `𝑇(𝑡)=𝑀𝑔𝐿sin(𝜃(𝑡))𝑇(𝑡)=𝑀𝑔𝐿sin(𝜃(𝑡))`
- `Equilibrium point: 𝜃_{0}=0`

Media:
- `media/image33.png`
- `media/image17.jpeg`

---

### t02-s027 — Example – Pendulum oscillator model

Tags: example, formula, figure

Content:
- Example – Pendulum oscillator model
- 𝑇(𝑡)=𝑀𝑔𝐿sin(𝜃(𝑡))𝑇(𝑡)=𝑀𝑔𝐿sin(𝜃(𝑡))
- First derivative at equilibrium provides linear approximation
- 𝑇(𝑡)≈𝑇_{0}+(𝑀𝑔𝐿(𝜕sin(𝜃))/(𝜕𝜃))_{𝜃(𝑡)=𝜃_{0}}(𝜃(𝑡)−𝜃_{0})
- Linear Approximation of Physical Systems

Equations / relations:
- `𝑇(𝑡)=𝑀𝑔𝐿sin(𝜃(𝑡))`
- `𝑇(𝑡)≈𝑇_{0}+(𝑀𝑔𝐿(𝜕sin(𝜃))/(𝜕𝜃))_{𝜃(𝑡)=𝜃_{0}}(𝜃(𝑡)−𝜃_{0})`
- `𝑇(𝑡)=𝑀𝑔𝐿sin(𝜃(𝑡))𝑇(𝑡)=𝑀𝑔𝐿sin(𝜃(𝑡))`

Media:
- `media/image34.png`
- `media/image17.jpeg`

---

### t02-s028 — Example – Pendulum oscillator model

Tags: example, formula, figure

Content:
- Example – Pendulum oscillator model
- 𝑇(𝑡)≈𝑇_{0}+(𝑀𝑔𝐿(𝜕sin(𝜃))/(𝜕𝜃))_{𝜃(𝑡)=𝜃_{0}}(𝜃(𝑡)−𝜃_{0})𝑇(𝑡)≈𝑇_{0}+(𝑀𝑔𝐿(𝜕sin(𝜃))/(𝜕𝜃))_{𝜃(𝑡)=𝜃_{0}}(𝜃(𝑡)−𝜃_{0})
- But 𝑇_{0}=0
- 𝑇(𝑡)≈𝑀𝑔𝐿 𝜃(𝑡)𝑇(𝑡)≈𝑀𝑔𝐿 𝜃(𝑡)
- Linear Approximation of Physical Systems

Equations / relations:
- `𝑇(𝑡)≈𝑇_{0}+(𝑀𝑔𝐿(𝜕sin(𝜃))/(𝜕𝜃))_{𝜃(𝑡)=𝜃_{0}}(𝜃(𝑡)−𝜃_{0})`
- `𝑇_{0}=0`
- `𝑇(𝑡)≈𝑀𝑔𝐿 𝜃(𝑡)`
- `𝑇(𝑡)≈𝑇_{0}+(𝑀𝑔𝐿(𝜕sin(𝜃))/(𝜕𝜃))_{𝜃(𝑡)=𝜃_{0}}(𝜃(𝑡)−𝜃_{0})𝑇(𝑡)≈𝑇_{0}+(𝑀𝑔𝐿(𝜕sin(𝜃))/(𝜕𝜃))_{𝜃(𝑡)=𝜃_{0}}(𝜃(𝑡)−𝜃_{0})`
- `But 𝑇_{0}=0`
- `𝑇(𝑡)≈𝑀𝑔𝐿 𝜃(𝑡)𝑇(𝑡)≈𝑀𝑔𝐿 𝜃(𝑡)`

Media:
- `media/image35.png`

---

### t02-s029 — Example – Pendulum oscillator model

Tags: example, formula, figure

Content:
- Example – Pendulum oscillator model
- 𝑇(𝑡)≈𝑀𝑔𝐿 𝜃(𝑡)
- Approx. is reasonably accurate for
- −(𝜋)/(4)≤𝜃≤(𝜋)/(4)
- Linear Approximation of Physical Systems

Equations / relations:
- `𝑇(𝑡)≈𝑀𝑔𝐿 𝜃(𝑡)`
- `−(𝜋)/(4)≤𝜃≤(𝜋)/(4)`
- `𝑇(𝑡)≈𝑀𝑔𝐿 𝜃(𝑡)`

Media:
- `media/image36.png`
- `media/image18.jpeg`

---

### t02-s030 — (untitled slide 30)

Tags: formula, figure

Content:
- If the dependent variable 𝑦(𝑡) depends upon several excitation variables, 𝑥_{1}(𝑡), 𝑥_{2}(𝑡), … , 𝑥_{𝑛}(𝑡), then the functional relationship is written as
- 𝑦(𝑡)=𝑔(𝑥_{1}(𝑡), 𝑥_{2}(𝑡), … , 𝑥_{𝑛}(𝑡))
- The Taylor series expansion about the operating point 𝑥_{1_{0}}, 𝑥_{2_{0}}, … , 𝑥_{𝑛_{0}} is
- 𝑦(𝑡)=𝑔(𝑥_{1_{0}}, 𝑥_{2_{0}}, … , 𝑥_{𝑛_{0}})+((𝜕𝑔)/(𝜕𝑥_{1}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{1}(𝑡)−𝑥_{1_{0}})+((𝜕𝑔)/(𝜕𝑥_{2}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{2}(𝑡)−𝑥_{2_{0}})+…+((𝜕𝑔)/(𝜕𝑥_{𝑛}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{𝑛}(𝑡)−𝑥_{𝑛_{0}})𝑦(𝑡)=𝑔(𝑥_{1_{0}}, 𝑥_{2_{0}}, … , 𝑥_{𝑛_{0}})+((𝜕𝑔)/(𝜕𝑥_{1}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{1}(𝑡)−𝑥_{1_{0}})+((𝜕𝑔)/(𝜕𝑥_{2}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{2}(𝑡)−𝑥_{2_{0}})+…+((𝜕𝑔)/(𝜕𝑥_{𝑛}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{𝑛}(𝑡)−𝑥_{𝑛_{0}})
- Linear Approximation of Physical Systems

Equations / relations:
- `𝑦(𝑡)`
- `𝑥_{1}(𝑡), 𝑥_{2}(𝑡), … , 𝑥_{𝑛}(𝑡)`
- `𝑦(𝑡)=𝑔(𝑥_{1}(𝑡), 𝑥_{2}(𝑡), … , 𝑥_{𝑛}(𝑡))`
- `𝑥_{1_{0}}, 𝑥_{2_{0}}, … , 𝑥_{𝑛_{0}}`
- `𝑦(𝑡)=𝑔(𝑥_{1_{0}}, 𝑥_{2_{0}}, … , 𝑥_{𝑛_{0}})+((𝜕𝑔)/(𝜕𝑥_{1}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{1}(𝑡)−𝑥_{1_{0}})+((𝜕𝑔)/(𝜕𝑥_{2}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{2}(𝑡)−𝑥_{2_{0}})+…`
- `+((𝜕𝑔)/(𝜕𝑥_{𝑛}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{𝑛}(𝑡)−𝑥_{𝑛_{0}})`
- `𝑦(𝑡)=𝑔(𝑥_{1}(𝑡), 𝑥_{2}(𝑡), … , 𝑥_{𝑛}(𝑡))`
- `𝑦(𝑡)=𝑔(𝑥_{1_{0}}, 𝑥_{2_{0}}, … , 𝑥_{𝑛_{0}})+((𝜕𝑔)/(𝜕𝑥_{1}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{1}(𝑡)−𝑥_{1_{0}})+((𝜕𝑔)/(𝜕𝑥_{2}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{2}(𝑡)−𝑥_{2_{0}})+…+((𝜕𝑔)/(𝜕𝑥_{𝑛}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{𝑛}(𝑡)−𝑥_{𝑛_{0}})𝑦(𝑡)=𝑔(𝑥_{1_{0}}, 𝑥_{2_{0}}, … , 𝑥_{𝑛_{0}})+((𝜕𝑔)/(𝜕𝑥_{1}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{1}(𝑡)−𝑥_{1_{0}})+((𝜕𝑔)/(𝜕𝑥_{2}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{2}(𝑡)−𝑥_{2_{0}})+…+((𝜕𝑔)/(𝜕𝑥_{𝑛}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{𝑛}(𝑡)−𝑥_{𝑛_{0}})`

Media:
- `media/image37.png`

---

### t02-s031 — Laplace Transform

Tags: formula

Content:
- Laplace Transform

---

### t02-s032 — Laplace Transform

Tags: definition, formula, figure, table

Content:
- Laplace Transform
- Converting a real variable (usually time t) to a complex variable (usually complex frequency s)
- Definition: For a function 𝑓(𝑡)   (𝑓(𝑡)=0 𝑓𝑜𝑟 𝑡<0)
- Time Domain (t)
- Frequency Domain (s)
- Differential equation
- Algebraic equation
- Convolution
- Multiplication
- ℒ ℒ
- ℒ^{−1}
- 𝐹(𝑠)=ℒ(𝑓(𝑡))≔∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)𝐹(𝑠)=ℒ(𝑓(𝑡))≔∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)
- 𝐹(𝑠) is the Laplace Transform of 𝑓(𝑡)

Tables:
- Table 1:
  - Time Domain (t) | Frequency Domain (s)
  - Differential equation | Algebraic equation
  - Convolution | Multiplication

Equations / relations:
- `𝑓(𝑡) (𝑓(𝑡)=0 𝑓𝑜𝑟 𝑡<0)`
- `ℒ`
- `ℒ^{−1}`
- `𝐹(𝑠)=ℒ(𝑓(𝑡))≔∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)`
- `𝐹(𝑠)`
- `𝑓(𝑡)`
- `Definition: For a function 𝑓(𝑡)   (𝑓(𝑡)=0 𝑓𝑜𝑟 𝑡<0)`
- `ℒ ℒ`
- `𝐹(𝑠)=ℒ(𝑓(𝑡))≔∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)𝐹(𝑠)=ℒ(𝑓(𝑡))≔∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)`

Media:
- `media/image200.png`
- `media/image210.png`
- `media/image29.png`
- `media/image32.png`
- `media/image38.png`

---

### t02-s033 — Converting a real variable (usually time t) to a complex variable (usually complex frequency s)

Tags: definition, formula, figure, table

Content:
- Converting a real variable (usually time t) to a complex variable (usually complex frequency s)
- Definition: For a function 𝑓(𝑡)   (𝑓(𝑡)=0 𝑓𝑜𝑟 𝑡<0)
- ℒ^{−1}(𝐹(𝑠))=(1)/(2𝜋𝑗)∫_{𝜎−𝑗∞}^{𝜎+𝑗∞}(𝐹(𝑠)𝑒^{+𝑠𝑡}𝑑𝑠)ℒ^{−1}(𝐹(𝑠))=(1)/(2𝜋𝑗)∫_{𝜎−𝑗∞}^{𝜎+𝑗∞}(𝐹(𝑠)𝑒^{+𝑠𝑡}𝑑𝑠)
- Time Domain (t)
- Frequency Domain (s)
- Differential equation
- Algebraic equation
- Convolution
- Multiplication
- ℒ ℒ
- ℒ^{−1}
- Laplace Transform
- Inverse Laplace Transform

Tables:
- Table 1:
  - Time Domain (t) | Frequency Domain (s)
  - Differential equation | Algebraic equation
  - Convolution | Multiplication

Equations / relations:
- `𝑓(𝑡) (𝑓(𝑡)=0 𝑓𝑜𝑟 𝑡<0)`
- `ℒ^{−1}(𝐹(𝑠))=(1)/(2𝜋𝑗)∫_{𝜎−𝑗∞}^{𝜎+𝑗∞}(𝐹(𝑠)𝑒^{+𝑠𝑡}𝑑𝑠)`
- `ℒ`
- `ℒ^{−1}`
- `Definition: For a function 𝑓(𝑡)   (𝑓(𝑡)=0 𝑓𝑜𝑟 𝑡<0)`
- `ℒ^{−1}(𝐹(𝑠))=(1)/(2𝜋𝑗)∫_{𝜎−𝑗∞}^{𝜎+𝑗∞}(𝐹(𝑠)𝑒^{+𝑠𝑡}𝑑𝑠)ℒ^{−1}(𝐹(𝑠))=(1)/(2𝜋𝑗)∫_{𝜎−𝑗∞}^{𝜎+𝑗∞}(𝐹(𝑠)𝑒^{+𝑠𝑡}𝑑𝑠)`
- `ℒ ℒ`

Media:
- `media/image42.png`
- `media/image380.png`
- `media/image39.png`

---

### t02-s034 — Step function:

Tags: formula, procedure, figure

Content:
- Step function:
- 𝑓(𝑡)=10𝑢(𝑡)=(10,  𝑡≥0 ; &0,  𝑡<0)
- 𝐹(𝑠)=∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)=∫_{0}^{∞}(10𝑒^{−𝑠𝑡}𝑑𝑡)=10∫_{0}^{∞}(𝑒^{−𝑠𝑡}𝑑𝑡)=10(−(1)/(𝑠)(𝑒^{−𝑠𝑡})_{0}^{∞})=10(0−(−(1)/(𝑠)))=(10)/(𝑠)𝐹(𝑠)=∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)=∫_{0}^{∞}(10𝑒^{−𝑠𝑡}𝑑𝑡)=10∫_{0}^{∞}(𝑒^{−𝑠𝑡}𝑑𝑡)=10(−(1)/(𝑠)(𝑒^{−𝑠𝑡})_{0}^{∞})=10(0−(−(1)/(𝑠)))=(10)/(𝑠)
- ℒ(𝑢(𝑡))=(1)/(𝑠)ℒ(𝑢(𝑡))=(1)/(𝑠)
- f(t)
- t
- Laplace Transform

Equations / relations:
- `𝑓(𝑡)=10𝑢(𝑡)=(10, 𝑡≥0 ; &0, 𝑡<0)`
- `𝐹(𝑠)=∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)=∫_{0}^{∞}(10𝑒^{−𝑠𝑡}𝑑𝑡)=10∫_{0}^{∞}(𝑒^{−𝑠𝑡}𝑑𝑡)`
- `=10(−(1)/(𝑠)(𝑒^{−𝑠𝑡})_{0}^{∞})=10(0−(−(1)/(𝑠)))=(10)/(𝑠)`
- `ℒ(𝑢(𝑡))=(1)/(𝑠)`
- `𝑓(𝑡)=10𝑢(𝑡)=(10,  𝑡≥0 ; &0,  𝑡<0)`
- `𝐹(𝑠)=∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)=∫_{0}^{∞}(10𝑒^{−𝑠𝑡}𝑑𝑡)=10∫_{0}^{∞}(𝑒^{−𝑠𝑡}𝑑𝑡)=10(−(1)/(𝑠)(𝑒^{−𝑠𝑡})_{0}^{∞})=10(0−(−(1)/(𝑠)))=(10)/(𝑠)𝐹(𝑠)=∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)=∫_{0}^{∞}(10𝑒^{−𝑠𝑡}𝑑𝑡)=10∫_{0}^{∞}(𝑒^{−𝑠𝑡}𝑑𝑡)=10(−(1)/(𝑠)(𝑒^{−𝑠𝑡})_{0}^{∞})=10(0−(−(1)/(𝑠)))=(10)/(𝑠)`
- `ℒ(𝑢(𝑡))=(1)/(𝑠)ℒ(𝑢(𝑡))=(1)/(𝑠)`

Media:
- `media/image43.png`

---

### t02-s035 — Laplace Transform

Tags: formula, figure

Content:
- Laplace Transform

Media:
- `media/image19.jpeg`

---

### t02-s036 — Laplace Transform

Tags: formula, figure

Content:
- Laplace Transform

Media:
- `media/image20.jpeg`

---

### t02-s037 — Laplace Transform

Tags: formula, figure

Content:
- Laplace Transform

Media:
- `media/image21.jpeg`

---

### t02-s038 — Linearity

Tags: derivation, formula, property, figure

Content:
- Linearity
- ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=𝛼_{1}ℒ(𝑓_{1}(𝑡))+𝛼_{2}ℒ(𝑓_{2}(𝑡))=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=𝛼_{1}ℒ(𝑓_{1}(𝑡))+𝛼_{2}ℒ(𝑓_{2}(𝑡))=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)
- Proof:
- ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=∫_{0}^{∞}((𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡)))𝑒^{−𝑠𝑡}𝑑𝑡 ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=∫_{0}^{∞}((𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡)))𝑒^{−𝑠𝑡}𝑑𝑡
- =𝛼_{1}∫_{0}^{∞}(𝑓_{1}(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)+𝛼_{2}∫_{0}^{∞}(𝑓_{2}(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)
- =𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)
- Properties of Laplace Transform

Equations / relations:
- `ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=𝛼_{1}ℒ(𝑓_{1}(𝑡))+𝛼_{2}ℒ(𝑓_{2}(𝑡))=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)`
- `ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=∫_{0}^{∞}((𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡)))𝑒^{−𝑠𝑡}𝑑𝑡`
- `=𝛼_{1}∫_{0}^{∞}(𝑓_{1}(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)+𝛼_{2}∫_{0}^{∞}(𝑓_{2}(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)`
- `=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)`
- `ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=𝛼_{1}ℒ(𝑓_{1}(𝑡))+𝛼_{2}ℒ(𝑓_{2}(𝑡))=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=𝛼_{1}ℒ(𝑓_{1}(𝑡))+𝛼_{2}ℒ(𝑓_{2}(𝑡))=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)`
- `ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=∫_{0}^{∞}((𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡)))𝑒^{−𝑠𝑡}𝑑𝑡 ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=∫_{0}^{∞}((𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡)))𝑒^{−𝑠𝑡}𝑑𝑡`

Media:
- `media/image44.png`

---

### t02-s039 — Linearity

Tags: example, formula, property, figure

Content:
- Linearity
- ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=𝛼_{1}ℒ(𝑓_{1}(𝑡))+𝛼_{2}ℒ(𝑓_{2}(𝑡))=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=𝛼_{1}ℒ(𝑓_{1}(𝑡))+𝛼_{2}ℒ(𝑓_{2}(𝑡))=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)
- Example: ℒ(4𝑢(𝑡)+5𝑒^{−2𝑡})
- Properties of Laplace Transform
- =4ℒ(𝑢(𝑡))+5ℒ(𝑒^{−2𝑡})=4ℒ(𝑢(𝑡))+5ℒ(𝑒^{−2𝑡})
- Using the Table
- =(4)/(𝑠)+(5)/(𝑠+2)=(4)/(𝑠)+(5)/(𝑠+2)

Equations / relations:
- `ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=𝛼_{1}ℒ(𝑓_{1}(𝑡))+𝛼_{2}ℒ(𝑓_{2}(𝑡))=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)`
- `ℒ(4𝑢(𝑡)+5𝑒^{−2𝑡})`
- `=4ℒ(𝑢(𝑡))+5ℒ(𝑒^{−2𝑡})`
- `=(4)/(𝑠)+(5)/(𝑠+2)`
- `ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=𝛼_{1}ℒ(𝑓_{1}(𝑡))+𝛼_{2}ℒ(𝑓_{2}(𝑡))=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=𝛼_{1}ℒ(𝑓_{1}(𝑡))+𝛼_{2}ℒ(𝑓_{2}(𝑡))=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)`
- `Example: ℒ(4𝑢(𝑡)+5𝑒^{−2𝑡})`
- `=4ℒ(𝑢(𝑡))+5ℒ(𝑒^{−2𝑡})=4ℒ(𝑢(𝑡))+5ℒ(𝑒^{−2𝑡})`
- `=(4)/(𝑠)+(5)/(𝑠+2)=(4)/(𝑠)+(5)/(𝑠+2)`

Media:
- `media/image50.png`
- `media/image45.png`
- `media/image46.png`

---

### t02-s040 — Differentiation

Tags: derivation, formula, figure

Content:
- Differentiation
- ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0)
- Proof:
- ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡 ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡
- Hint: Integration by parts  ∫_{0}^{∞}(𝑢(𝑑𝑣)/(𝑑𝑡))𝑑𝑡=𝑢𝑣−∫_{0}^{∞}(𝑣(𝑑𝑢)/(𝑑𝑡)𝑑𝑡)
- Properties of Laplace Transform
- ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)
- (𝑑𝑣)/(𝑑𝑡)(𝑑𝑣)/(𝑑𝑡)
- 𝑢 𝑢

Equations / relations:
- `ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0)`
- `ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡`
- `∫_{0}^{∞}(𝑢(𝑑𝑣)/(𝑑𝑡))𝑑𝑡=𝑢𝑣−∫_{0}^{∞}(𝑣(𝑑𝑢)/(𝑑𝑡)𝑑𝑡)`
- `ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)`
- `(𝑑𝑣)/(𝑑𝑡)`
- `𝑢`
- `ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡 ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡`
- `Hint: Integration by parts  ∫_{0}^{∞}(𝑢(𝑑𝑣)/(𝑑𝑡))𝑑𝑡=𝑢𝑣−∫_{0}^{∞}(𝑣(𝑑𝑢)/(𝑑𝑡)𝑑𝑡)`
- `ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)`

Media:
- `media/image47.png`
- `media/image48.png`
- `media/image49.png`
- `media/image51.png`

---

### t02-s041 — Differentiation

Tags: derivation, formula, figure

Content:
- Differentiation
- ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0) ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)
- Proof:
- ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡=(𝑓(𝑡)𝑒^{−𝑠𝑡})_{0}^{∞}+𝑠∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡=(𝑓(𝑡)𝑒^{−𝑠𝑡})_{0}^{∞}+𝑠∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)
- (𝑑𝑣)/(𝑑𝑡)(𝑑𝑣)/(𝑑𝑡)
- 𝑢 𝑢
- Properties of Laplace Transform
- ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0)ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0)

Equations / relations:
- `ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0)`
- `ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)`
- `ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡=(𝑓(𝑡)𝑒^{−𝑠𝑡})_{0}^{∞}+𝑠∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)`
- `(𝑑𝑣)/(𝑑𝑡)`
- `𝑢`
- `ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0) ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)`
- `ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡=(𝑓(𝑡)𝑒^{−𝑠𝑡})_{0}^{∞}+𝑠∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡=(𝑓(𝑡)𝑒^{−𝑠𝑡})_{0}^{∞}+𝑠∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)`
- `ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0)ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0)`

Media:
- `media/image59.png`
- `media/image60.png`
- `media/image61.png`
- `media/image52.png`

---

### t02-s042 — Differentiation

Tags: example, formula, figure

Content:
- Differentiation
- ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0) ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)
- Example: ℒ((𝑑(sin((2𝑡))))/(𝑑𝑡))
- Properties of Laplace Transform
- =𝑠(2)/(𝑠^{2}+4)=𝑠(2)/(𝑠^{2}+4)
- −sin(0=(2𝑠)/(𝑠^{2}+4))−sin(0=(2𝑠)/(𝑠^{2}+4))

Equations / relations:
- `ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0)`
- `ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)`
- `ℒ((𝑑(sin((2𝑡))))/(𝑑𝑡))`
- `=𝑠(2)/(𝑠^{2}+4)`
- `−sin(0=(2𝑠)/(𝑠^{2}+4))`
- `ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0) ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)`
- `Example: ℒ((𝑑(sin((2𝑡))))/(𝑑𝑡))`
- `=𝑠(2)/(𝑠^{2}+4)=𝑠(2)/(𝑠^{2}+4)`
- `−sin(0=(2𝑠)/(𝑠^{2}+4))−sin(0=(2𝑠)/(𝑠^{2}+4))`

Media:
- `media/image53.png`
- `media/image54.png`
- `media/image55.png`
- `media/image22.jpeg`

---

### t02-s043 — Integration

Tags: derivation, formula, figure

Content:
- Integration
- ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=(𝐹(𝑠))/(𝑠)ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=(𝐹(𝑠))/(𝑠)
- Proof:
- ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=∫_{0}^{∞}((∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏)))𝑒^{−𝑠𝑡}𝑑𝑡 ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=∫_{0}^{∞}((∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏)))𝑒^{−𝑠𝑡}𝑑𝑡
- =(−(1)/(𝑠)(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))𝑒^{−𝑠𝑡})_{0}^{∞}+(1)/(𝑠)∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)=(−(1)/(𝑠)(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))𝑒^{−𝑠𝑡})_{0}^{∞}+(1)/(𝑠)∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)
- Properties of Laplace Transform
- (𝑑𝑣)/(𝑑𝑡)(𝑑𝑣)/(𝑑𝑡)
- 𝑢 𝑢
- =(𝐹(𝑠))/(𝑠)=(𝐹(𝑠))/(𝑠)

Equations / relations:
- `ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=(𝐹(𝑠))/(𝑠)`
- `ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=∫_{0}^{∞}((∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏)))𝑒^{−𝑠𝑡}𝑑𝑡`
- `=(−(1)/(𝑠)(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))𝑒^{−𝑠𝑡})_{0}^{∞}+(1)/(𝑠)∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)`
- `(𝑑𝑣)/(𝑑𝑡)`
- `𝑢`
- `=(𝐹(𝑠))/(𝑠)`
- `ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=(𝐹(𝑠))/(𝑠)ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=(𝐹(𝑠))/(𝑠)`
- `ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=∫_{0}^{∞}((∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏)))𝑒^{−𝑠𝑡}𝑑𝑡 ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=∫_{0}^{∞}((∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏)))𝑒^{−𝑠𝑡}𝑑𝑡`
- `=(−(1)/(𝑠)(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))𝑒^{−𝑠𝑡})_{0}^{∞}+(1)/(𝑠)∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)=(−(1)/(𝑠)(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))𝑒^{−𝑠𝑡})_{0}^{∞}+(1)/(𝑠)∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)`
- `=(𝐹(𝑠))/(𝑠)=(𝐹(𝑠))/(𝑠)`

Media:
- `media/image40.png`
- `media/image57.png`
- `media/image58.png`
- `media/image62.png`

---

### t02-s044 — Time Domain (t)

Tags: formula, figure, table

Content:
- Time Domain (t)
- Frequency Domain (s)
- (𝑑)/(𝑑𝑡)(𝑑)/(𝑑𝑡)
- 𝑠 𝑠
- ∫_{0}^{𝑡}(𝑑𝑡)∫_{0}^{𝑡}(𝑑𝑡)
- (1)/(𝑠)(1)/(𝑠)
- ODE
- Multiplication and division by 𝑠
- Time Domain (t)
- Frequency Domain (s)
- ODE
- Importance of Laplace Transform

Tables:
- Table 1:
  - Time Domain (t) | Frequency Domain (s)
  - ODE | Multiplication and division by
- Table 2:
  - Time Domain (t) | Frequency Domain (s)
  - ODE | 

Equations / relations:
- `(𝑑)/(𝑑𝑡)`
- `𝑠`
- `∫_{0}^{𝑡}(𝑑𝑡)`
- `(1)/(𝑠)`
- `∫_{0}^{𝑡}(𝑑𝑡)∫_{0}^{𝑡}(𝑑𝑡)`

Media:
- `media/image73.png`

---

### t02-s045 — Solving ODEs using Laplace Transform

Tags: formula, figure

Content:
- Solving ODEs using Laplace Transform
- Spring-mass damper system
- 2(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+6(𝑑𝑦(𝑡))/(𝑑𝑡)+4𝑦(𝑡)=𝑟(𝑡)2(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+6(𝑑𝑦(𝑡))/(𝑑𝑡)+4𝑦(𝑡)=𝑟(𝑡)
- 2(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0)−((𝑑𝑦)/(𝑑𝑡))_{𝑡=0})+6(𝑠𝑌(𝑠)−𝑦(0))+4𝑌(𝑠)=𝑅(𝑠)2(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0)−((𝑑𝑦)/(𝑑𝑡))_{𝑡=0})+6(𝑠𝑌(𝑠)−𝑦(0))+4𝑌(𝑠)=𝑅(𝑠)
- When 𝑟(𝑡)=0  𝑎𝑛𝑑  𝑦(0)=𝑦_{0}  𝑎𝑛𝑑  ((𝑑𝑦)/(𝑑𝑡))_{𝑡=0}=0
- We have 2𝑠^{2}𝑌(𝑠)−2𝑠𝑦_{0}+6𝑠𝑌(𝑠)−6𝑦_{0}+4𝑌(𝑠)=0
- Solving for 𝑌(𝑠): 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))

Equations / relations:
- `2(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+6(𝑑𝑦(𝑡))/(𝑑𝑡)+4𝑦(𝑡)=𝑟(𝑡)`
- `2(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0)−((𝑑𝑦)/(𝑑𝑡))_{𝑡=0})+6(𝑠𝑌(𝑠)−𝑦(0))+4𝑌(𝑠)=𝑅(𝑠)`
- `𝑟(𝑡)=0 𝑎𝑛𝑑 𝑦(0)=𝑦_{0} 𝑎𝑛𝑑 ((𝑑𝑦)/(𝑑𝑡))_{𝑡=0}=0`
- `2𝑠^{2}𝑌(𝑠)−2𝑠𝑦_{0}+6𝑠𝑌(𝑠)−6𝑦_{0}+4𝑌(𝑠)=0`
- `𝑌(𝑠)`
- `𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))`
- `2(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+6(𝑑𝑦(𝑡))/(𝑑𝑡)+4𝑦(𝑡)=𝑟(𝑡)2(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+6(𝑑𝑦(𝑡))/(𝑑𝑡)+4𝑦(𝑡)=𝑟(𝑡)`
- `2(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0)−((𝑑𝑦)/(𝑑𝑡))_{𝑡=0})+6(𝑠𝑌(𝑠)−𝑦(0))+4𝑌(𝑠)=𝑅(𝑠)2(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0)−((𝑑𝑦)/(𝑑𝑡))_{𝑡=0})+6(𝑠𝑌(𝑠)−𝑦(0))+4𝑌(𝑠)=𝑅(𝑠)`
- `When 𝑟(𝑡)=0  𝑎𝑛𝑑  𝑦(0)=𝑦_{0}  𝑎𝑛𝑑  ((𝑑𝑦)/(𝑑𝑡))_{𝑡=0}=0`
- `We have 2𝑠^{2}𝑌(𝑠)−2𝑠𝑦_{0}+6𝑠𝑌(𝑠)−6𝑦_{0}+4𝑌(𝑠)=0`
- `Solving for 𝑌(𝑠): 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))`

Media:
- `media/image74.png`
- `media/image75.png`
- `media/image63.png`
- `media/image64.png`
- `media/image65.png`
- `media/image66.png`

---

### t02-s046 — 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=((𝑠+3)𝑦_{0})/(𝑠^{2}+3𝑠+2)𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=((𝑠+3)𝑦_{0})/(𝑠^{2}+3𝑠+2)

Tags: formula, figure

Content:
- 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=((𝑠+3)𝑦_{0})/(𝑠^{2}+3𝑠+2)𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=((𝑠+3)𝑦_{0})/(𝑠^{2}+3𝑠+2)
- Zero: 𝑠=−3
- Poles: 𝑠=−1  𝑎𝑛𝑑  𝑠=−2
- Characteristic Equation: the roots determine the character of the time response
- Solving ODEs using Laplace Transform

Equations / relations:
- `𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=((𝑠+3)𝑦_{0})/(𝑠^{2}+3𝑠+2)`
- `𝑠=−3`
- `𝑠=−1 𝑎𝑛𝑑 𝑠=−2`
- `𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=((𝑠+3)𝑦_{0})/(𝑠^{2}+3𝑠+2)𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=((𝑠+3)𝑦_{0})/(𝑠^{2}+3𝑠+2)`
- `Zero: 𝑠=−3`
- `Poles: 𝑠=−1  𝑎𝑛𝑑  𝑠=−2`

Media:
- `media/image80.png`
- `media/image23.jpeg`

---

### t02-s047 — Back to solving: 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2)

Tags: formula, figure

Content:
- Back to solving: 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2)
- Partial Fraction Expansion
- Solving ODEs using Laplace Transform
- Let 𝑦_{0}=1
- 𝑌(𝑠)=(𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2})/((𝑠+1)(𝑠+2))=((𝑠+3))/((𝑠+1)(𝑠+2))𝑌(𝑠)=(𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2})/((𝑠+1)(𝑠+2))=((𝑠+3))/((𝑠+1)(𝑠+2))
- 𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3 𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3

Equations / relations:
- `𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2)`
- `𝑦_{0}=1`
- `𝑌(𝑠)=(𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2})/((𝑠+1)(𝑠+2))=((𝑠+3))/((𝑠+1)(𝑠+2))`
- `𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3`
- `Back to solving: 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2)`
- `Let 𝑦_{0}=1`
- `𝑌(𝑠)=(𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2})/((𝑠+1)(𝑠+2))=((𝑠+3))/((𝑠+1)(𝑠+2))𝑌(𝑠)=(𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2})/((𝑠+1)(𝑠+2))=((𝑠+3))/((𝑠+1)(𝑠+2))`
- `𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3 𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3`

Media:
- `media/image82.png`
- `media/image68.png`
- `media/image69.png`
- `media/image70.png`

---

### t02-s048 — Back to solving: 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2) Let 𝑦_{0}=1

Tags: formula, figure

Content:
- Back to solving: 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2) Let 𝑦_{0}=1
- 𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3  (𝑘_{1}+𝑘_{2}=1 ; 2𝑘_{1}+𝑘_{2}=3)  (𝑘_{1}=2 ; 𝑘_{2}=−1)
- 𝑌(𝑠)=(2)/(𝑠+1)+(−1)/(𝑠+2)𝑌(𝑠)=(2)/(𝑠+1)+(−1)/(𝑠+2)
- Solving ODEs using Laplace Transform

Equations / relations:
- `𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2)`
- `𝑦_{0}=1`
- `𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3`
- `(𝑘_{1}+𝑘_{2}=1 ; 2𝑘_{1}+𝑘_{2}=3)`
- `(𝑘_{1}=2 ; 𝑘_{2}=−1)`
- `𝑌(𝑠)=(2)/(𝑠+1)+(−1)/(𝑠+2)`
- `Back to solving: 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2) Let 𝑦_{0}=1`
- `𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3  (𝑘_{1}+𝑘_{2}=1 ; 2𝑘_{1}+𝑘_{2}=3)  (𝑘_{1}=2 ; 𝑘_{2}=−1)`
- `𝑌(𝑠)=(2)/(𝑠+1)+(−1)/(𝑠+2)𝑌(𝑠)=(2)/(𝑠+1)+(−1)/(𝑠+2)`

Media:
- `media/image71.png`

---

### t02-s049 — Back to solving: 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2) Let 𝑦_{0}=1

Tags: formula, figure

Content:
- Back to solving: 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2) Let 𝑦_{0}=1
- 𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3  (𝑘_{1}+𝑘_{2}=1 ; 2𝑘_{1}+𝑘_{2}=3)  (𝑘_{1}=2 ; 𝑘_{2}=−1)
- 𝑦(𝑡)=ℒ^{−1}((2)/(𝑠+1))+ℒ^{−1}((−1)/(𝑠+2))𝑦(𝑡)=ℒ^{−1}((2)/(𝑠+1))+ℒ^{−1}((−1)/(𝑠+2))
- Solving ODEs using Laplace Transform
- 𝑌(𝑠)=(2)/(𝑠+1)+(−1)/(𝑠+2)𝑌(𝑠)=(2)/(𝑠+1)+(−1)/(𝑠+2)
- 𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}
- We solved the ODE with simple algebraic equations using Laplace Transform

Equations / relations:
- `𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2)`
- `𝑦_{0}=1`
- `𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3`
- `(𝑘_{1}+𝑘_{2}=1 ; 2𝑘_{1}+𝑘_{2}=3)`
- `(𝑘_{1}=2 ; 𝑘_{2}=−1)`
- `𝑦(𝑡)=ℒ^{−1}((2)/(𝑠+1))+ℒ^{−1}((−1)/(𝑠+2))`
- `𝑌(𝑠)=(2)/(𝑠+1)+(−1)/(𝑠+2)`
- `𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}`
- `Back to solving: 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2) Let 𝑦_{0}=1`
- `𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3  (𝑘_{1}+𝑘_{2}=1 ; 2𝑘_{1}+𝑘_{2}=3)  (𝑘_{1}=2 ; 𝑘_{2}=−1)`
- `𝑦(𝑡)=ℒ^{−1}((2)/(𝑠+1))+ℒ^{−1}((−1)/(𝑠+2))𝑦(𝑡)=ℒ^{−1}((2)/(𝑠+1))+ℒ^{−1}((−1)/(𝑠+2))`
- `𝑌(𝑠)=(2)/(𝑠+1)+(−1)/(𝑠+2)𝑌(𝑠)=(2)/(𝑠+1)+(−1)/(𝑠+2)`
- `𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}`

Media:
- `media/image72.png`
- `media/image76.png`
- `media/image77.png`

---

### t02-s050 — Solving ODEs using Laplace Transform

Tags: example, formula, property, figure

Content:
- Solving ODEs using Laplace Transform
- Final Value Theorem
- lim𝑡→∞(𝑓(𝑡))=lim𝑠→0(𝑠𝐹(𝑠)) applicable if all the poles of 𝑠𝐹(𝑠) are in the left half plane (LHP)
- Back to our example
- 𝑌(𝑠)=((𝑠+3))/((𝑠+1)(𝑠+2))   →   𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}𝑌(𝑠)=((𝑠+3))/((𝑠+1)(𝑠+2))   →   𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}
- Poles: 𝑠=−1 & 𝑠=−2 (LHP)
- lim𝑡→∞(𝑦(𝑡))=lim𝑠→0(𝑠𝑌(𝑠))=0 lim𝑡→∞(𝑦(𝑡))=lim𝑠→0(𝑠𝑌(𝑠))=0

Equations / relations:
- `lim𝑡→∞(𝑓(𝑡))=lim𝑠→0(𝑠𝐹(𝑠))`
- `𝑠𝐹(𝑠)`
- `𝑌(𝑠)=((𝑠+3))/((𝑠+1)(𝑠+2)) → 𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}`
- `𝑠=−1 & 𝑠=−2`
- `lim𝑡→∞(𝑦(𝑡))=lim𝑠→0(𝑠𝑌(𝑠))=0`
- `lim𝑡→∞(𝑓(𝑡))=lim𝑠→0(𝑠𝐹(𝑠)) applicable if all the poles of 𝑠𝐹(𝑠) are in the left half plane (LHP)`
- `𝑌(𝑠)=((𝑠+3))/((𝑠+1)(𝑠+2))   →   𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}𝑌(𝑠)=((𝑠+3))/((𝑠+1)(𝑠+2))   →   𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}`
- `Poles: 𝑠=−1 & 𝑠=−2 (LHP)`
- `lim𝑡→∞(𝑦(𝑡))=lim𝑠→0(𝑠𝑌(𝑠))=0 lim𝑡→∞(𝑦(𝑡))=lim𝑠→0(𝑠𝑌(𝑠))=0`

Media:
- `media/image400.png`

---

### t02-s051 — ODE

Tags: formula, figure

Content:
- ODE
- Algebraic Equation
- Partial Fraction Expansion
- Solution to ODE
- ℒ ℒ
- ℒ^{−1}ℒ^{−1}
- t-domain
- s-domain
- Roadmap

Equations / relations:
- `ℒ`
- `ℒ^{−1}`
- `ℒ ℒ`
- `ℒ^{−1}ℒ^{−1}`

Media:
- `media/image89.png`
- `media/image90.png`

---

### t02-s052 — ODE with Initial Conditions:

Tags: example, formula, figure

Content:
- ODE with Initial Conditions:
- 𝑦^{′′}(𝑡)−𝑦(𝑡)=𝑡,    𝑦(0)=1,   𝑦^{′}(0)=1 𝑦^{′′}(𝑡)−𝑦(𝑡)=𝑡,    𝑦(0)=1,   𝑦^{′}(0)=1
- Laplace Transform
- ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)
- Another Example
- 𝑠^{2}𝑌(𝑠)−𝑠−1−𝑌(𝑠)=(1!)/(𝑠^{1+1})=(1)/(𝑠^{2})𝑠^{2}𝑌(𝑠)−𝑠−1−𝑌(𝑠)=(1!)/(𝑠^{1+1})=(1)/(𝑠^{2})
- (𝑠^{2}−1)𝑌(𝑠)−(𝑠+1)=(1)/(𝑠^{2})(𝑠^{2}−1)𝑌(𝑠)−(𝑠+1)=(1)/(𝑠^{2})
- 𝑌(𝑠)=(1)/(𝑠^{2}(𝑠^{2}−1))+(𝑠+1)/(𝑠^{2}−1)=(1+𝑠^{3}+𝑠^{2})/(𝑠^{2}(𝑠^{2}−1))=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))𝑌(𝑠)=(1)/(𝑠^{2}(𝑠^{2}−1))+(𝑠+1)/(𝑠^{2}−1)=(1+𝑠^{3}+𝑠^{2})/(𝑠^{2}(𝑠^{2}−1))=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))

Equations / relations:
- `𝑦^{′′}(𝑡)−𝑦(𝑡)=𝑡, 𝑦(0)=1, 𝑦^{′}(0)=1`
- `ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)`
- `𝑠^{2}𝑌(𝑠)−𝑠−1−𝑌(𝑠)=(1!)/(𝑠^{1+1})=(1)/(𝑠^{2})`
- `(𝑠^{2}−1)𝑌(𝑠)−(𝑠+1)=(1)/(𝑠^{2})`
- `𝑌(𝑠)=(1)/(𝑠^{2}(𝑠^{2}−1))+(𝑠+1)/(𝑠^{2}−1)=(1+𝑠^{3}+𝑠^{2})/(𝑠^{2}(𝑠^{2}−1))=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))`
- `𝑦^{′′}(𝑡)−𝑦(𝑡)=𝑡,    𝑦(0)=1,   𝑦^{′}(0)=1 𝑦^{′′}(𝑡)−𝑦(𝑡)=𝑡,    𝑦(0)=1,   𝑦^{′}(0)=1`
- `ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)`
- `𝑠^{2}𝑌(𝑠)−𝑠−1−𝑌(𝑠)=(1!)/(𝑠^{1+1})=(1)/(𝑠^{2})𝑠^{2}𝑌(𝑠)−𝑠−1−𝑌(𝑠)=(1!)/(𝑠^{1+1})=(1)/(𝑠^{2})`
- `(𝑠^{2}−1)𝑌(𝑠)−(𝑠+1)=(1)/(𝑠^{2})(𝑠^{2}−1)𝑌(𝑠)−(𝑠+1)=(1)/(𝑠^{2})`
- `𝑌(𝑠)=(1)/(𝑠^{2}(𝑠^{2}−1))+(𝑠+1)/(𝑠^{2}−1)=(1+𝑠^{3}+𝑠^{2})/(𝑠^{2}(𝑠^{2}−1))=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))𝑌(𝑠)=(1)/(𝑠^{2}(𝑠^{2}−1))+(𝑠+1)/(𝑠^{2}−1)=(1+𝑠^{3}+𝑠^{2})/(𝑠^{2}(𝑠^{2}−1))=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))`

Media:
- `media/image91.png`
- `media/image440.png`
- `media/image78.png`
- `media/image79.png`
- `media/image81.png`

---

### t02-s053 — 𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))

Tags: example, figure

Content:
- 𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))
- 2. Partial Fraction Expansion
- Another Example – cont’d
- (𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)
- 𝑠^{3}+𝑠^{2}+1=(𝐴𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠)+(𝐵𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠^{2})+(𝐶𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠−1)+(𝐷𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠+1)𝑠^{3}+𝑠^{2}+1=(𝐴𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠)+(𝐵𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠^{2})+(𝐶𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠−1)+(𝐷𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠+1)
- 𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)

Equations / relations:
- `𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))`
- `(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)`
- `𝑠^{3}+𝑠^{2}+1=(𝐴𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠)+(𝐵𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠^{2})+(𝐶𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠−1)+(𝐷𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠+1)`
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)`
- `𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))`
- `(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)`
- `𝑠^{3}+𝑠^{2}+1=(𝐴𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠)+(𝐵𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠^{2})+(𝐶𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠−1)+(𝐷𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠+1)𝑠^{3}+𝑠^{2}+1=(𝐴𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠)+(𝐵𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠^{2})+(𝐶𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠−1)+(𝐷𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠+1)`
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)`

Media:
- `media/image83.png`
- `media/image84.png`
- `media/image85.png`
- `media/image86.png`

---

### t02-s054 — 𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))

Tags: example, formula, figure

Content:
- 𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))
- 2. Partial Fraction Expansion
- Another Example – cont’d
- (𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)
- 𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)
- Replacing the denominator root values
- (𝑟𝑜𝑜𝑡 0:−𝐵=1 ; 𝑟𝑜𝑜𝑡 1:    𝐶=(3)/(2) ; 𝑟𝑜𝑜𝑡 −1:   𝐷=−(1)/(2))  𝐵=−1,  𝐶=(3)/(2),   𝐷=−(1)/(2)

Equations / relations:
- `𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))`
- `(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)`
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)`
- `(𝑟𝑜𝑜𝑡 0:−𝐵=1 ; 𝑟𝑜𝑜𝑡 1: 𝐶=(3)/(2) ; 𝑟𝑜𝑜𝑡 −1: 𝐷=−(1)/(2))`
- `𝐵=−1, 𝐶=(3)/(2), 𝐷=−(1)/(2)`
- `𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))`
- `(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)`
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)`
- `(𝑟𝑜𝑜𝑡 0:−𝐵=1 ; 𝑟𝑜𝑜𝑡 1:    𝐶=(3)/(2) ; 𝑟𝑜𝑜𝑡 −1:   𝐷=−(1)/(2))  𝐵=−1,  𝐶=(3)/(2),   𝐷=−(1)/(2)`

Media:
- `media/image83.png`
- `media/image84.png`
- `media/image87.png`
- `media/image41.png`

---

### t02-s055 — 𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))

Tags: example, figure

Content:
- 𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))
- 2. Partial Fraction Expansion
- Another Example – cont’d
- (𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)
- 𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)
- 𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)−1(𝑠−1)(𝑠+1)+(3)/(2)𝑠^{2}(𝑠+1)−(1)/(2)𝑠^{2}(𝑠−1)𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)−1(𝑠−1)(𝑠+1)+(3)/(2)𝑠^{2}(𝑠+1)−(1)/(2)𝑠^{2}(𝑠−1)
- 𝑠^{3}+𝑠^{2}+1=𝐴𝑠^{3}−𝐴𝑠−𝑠^{2}+1+(3)/(2)𝑠^{3}+(3)/(2)𝑠^{2}−(1)/(2)𝑠^{3}+(1)/(2)𝑠^{2}𝑠^{3}+𝑠^{2}+1=𝐴𝑠^{3}−𝐴𝑠−𝑠^{2}+1+(3)/(2)𝑠^{3}+(3)/(2)𝑠^{2}−(1)/(2)𝑠^{3}+(1)/(2)𝑠^{2}
- 𝐴=0 𝐴=0

Equations / relations:
- `𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))`
- `(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)`
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)`
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)−1(𝑠−1)(𝑠+1)+(3)/(2)𝑠^{2}(𝑠+1)−(1)/(2)𝑠^{2}(𝑠−1)`
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠^{3}−𝐴𝑠−𝑠^{2}+1+(3)/(2)𝑠^{3}+(3)/(2)𝑠^{2}−(1)/(2)𝑠^{3}+(1)/(2)𝑠^{2}`
- `𝐴=0`
- `𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))`
- `(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)`
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)`
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)−1(𝑠−1)(𝑠+1)+(3)/(2)𝑠^{2}(𝑠+1)−(1)/(2)𝑠^{2}(𝑠−1)𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)−1(𝑠−1)(𝑠+1)+(3)/(2)𝑠^{2}(𝑠+1)−(1)/(2)𝑠^{2}(𝑠−1)`
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠^{3}−𝐴𝑠−𝑠^{2}+1+(3)/(2)𝑠^{3}+(3)/(2)𝑠^{2}−(1)/(2)𝑠^{3}+(1)/(2)𝑠^{2}𝑠^{3}+𝑠^{2}+1=𝐴𝑠^{3}−𝐴𝑠−𝑠^{2}+1+(3)/(2)𝑠^{3}+(3)/(2)𝑠^{2}−(1)/(2)𝑠^{3}+(1)/(2)𝑠^{2}`
- `𝐴=0 𝐴=0`

Media:
- `media/image83.png`
- `media/image84.png`
- `media/image87.png`
- `media/image67.png`
- `media/image88.png`
- `media/image92.png`

---

### t02-s056 — 𝑌(𝑠)=(0)/(𝑠)+(−1)/(𝑠^{2})+((3)/(2))/(𝑠−1)+(−(1)/(2))/(𝑠+1)𝑌(𝑠)=(0)/(𝑠)+(−1)/(𝑠^{2})+((3)/(2))/(𝑠−1)+(−(1)/(2))/(𝑠+1)

Tags: example, formula, figure

Content:
- 𝑌(𝑠)=(0)/(𝑠)+(−1)/(𝑠^{2})+((3)/(2))/(𝑠−1)+(−(1)/(2))/(𝑠+1)𝑌(𝑠)=(0)/(𝑠)+(−1)/(𝑠^{2})+((3)/(2))/(𝑠−1)+(−(1)/(2))/(𝑠+1)
- 3. Inverse Laplace (using the Table)
- 𝑦(𝑡)=−𝑡+(3)/(2)𝑒^{𝑡}−(1)/(2)𝑒^{−𝑡}𝑦(𝑡)=−𝑡+(3)/(2)𝑒^{𝑡}−(1)/(2)𝑒^{−𝑡}
- Another Example – cont’d

Equations / relations:
- `𝑌(𝑠)=(0)/(𝑠)+(−1)/(𝑠^{2})+((3)/(2))/(𝑠−1)+(−(1)/(2))/(𝑠+1)`
- `𝑦(𝑡)=−𝑡+(3)/(2)𝑒^{𝑡}−(1)/(2)𝑒^{−𝑡}`
- `𝑌(𝑠)=(0)/(𝑠)+(−1)/(𝑠^{2})+((3)/(2))/(𝑠−1)+(−(1)/(2))/(𝑠+1)𝑌(𝑠)=(0)/(𝑠)+(−1)/(𝑠^{2})+((3)/(2))/(𝑠−1)+(−(1)/(2))/(𝑠+1)`
- `𝑦(𝑡)=−𝑡+(3)/(2)𝑒^{𝑡}−(1)/(2)𝑒^{−𝑡}𝑦(𝑡)=−𝑡+(3)/(2)𝑒^{𝑡}−(1)/(2)𝑒^{−𝑡}`

Media:
- `media/image93.png`

---

## Formula index (this topic)

- `𝐹=𝑀𝑎` ← t02-s005
- `∑_{}^{}(𝐹)=𝑀𝑦` ← t02-s005
- `−𝑘𝑦(𝑡)−𝑏𝑦(𝑡)+𝐹_{𝑒𝑥𝑡𝑒𝑟𝑛𝑎𝑙}=𝑀𝑦(𝑡)` ← t02-s005
- `𝑀(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦(𝑡))/(𝑑𝑡)+𝑘𝑦(𝑡)=𝑟(𝑡)` ← t02-s005
- `𝑅𝐻𝑆≠0` ← t02-s005
- `(𝑣(𝑡))/(𝑅)+𝐶(𝑑𝑣(𝑡))/(𝑑𝑡)+(1)/(𝐿)∫_{0}^{𝑡}(𝑣(𝑡)𝑑(𝑡))=𝑟(𝑡)` ← t02-s006
- `𝑀(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦(𝑡))/(𝑑𝑡)+𝑘𝑦(𝑡)=𝑟(𝑡) (𝑣(𝑡))/(𝑅)+𝐶(𝑑𝑣(𝑡))/(𝑑𝑡)+(1)/(𝐿)∫_{0}^{𝑡}(𝑣(𝑡)𝑑(𝑡))=𝑟(𝑡)` ← t02-s006
- `𝑦(𝑡)` ← t02-s007
- `𝑦(𝑡)=𝑦_{𝑐}(𝑡)+𝑦_{𝑝}(𝑡)` ← t02-s007
- `𝑦_{𝑐}(𝑡)` ← t02-s007
- `𝑀(𝑑^{2}𝑦_{𝑐}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑐}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑐}(𝑡)=0` ← t02-s007
- `𝑦_{𝑝}(𝑡)` ← t02-s007
- `𝑀(𝑑^{2}𝑦_{𝑝}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑝}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑝}(𝑡)=𝑟(𝑡)` ← t02-s007
- `in the form 𝑦(𝑡)=𝑦_{𝑐}(𝑡)+𝑦_{𝑝}(𝑡)` ← t02-s007
- `𝑦_{𝑐}(𝑡) is the complementary solution to 𝑀(𝑑^{2}𝑦_{𝑐}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑐}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑐}(𝑡)=0` ← t02-s007
- `𝑦_{𝑝}(𝑡) is the particular solution to 𝑀(𝑑^{2}𝑦_{𝑝}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑝}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑝}(𝑡)=𝑟(𝑡)` ← t02-s007
- `𝑒^{𝜆𝑡}≠0` ← t02-s008
- `𝑦_{𝑐}(𝑡)=𝑒^{𝜆𝑡}` ← t02-s008
- `(𝑑𝑦_{𝑐})/(𝑑𝑡)=𝜆𝑒^{𝜆𝑡} (𝑑^{2}𝑦_{𝑐})/(𝑑𝑡^{2})=𝜆^{2}𝑒^{𝜆𝑡}` ← t02-s008
- `𝑀𝜆^{2}𝑒^{𝜆𝑡}+𝑏𝜆𝑒^{𝜆𝑡}+𝑘𝑒^{𝜆𝑡}=0` ← t02-s008
- `𝑀𝜆^{2}+𝑏𝜆+𝑘=0` ← t02-s008
- `𝜆_{1} & 𝜆_{2}` ← t02-s008
- `1. 𝑀(𝑑^{2}𝑦_{𝑐}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑐}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑐}(𝑡)=0` ← t02-s008
- `Make an educated guess 𝑦_{𝑐}(𝑡)=𝑒^{𝜆𝑡}` ← t02-s008
- `(𝑑𝑦_{𝑐})/(𝑑𝑡)=𝜆𝑒^{𝜆𝑡}            (𝑑^{2}𝑦_{𝑐})/(𝑑𝑡^{2})=𝜆^{2}𝑒^{𝜆𝑡}(𝑑𝑦_{𝑐})/(𝑑𝑡)=𝜆𝑒^{𝜆𝑡}            (𝑑^{2}𝑦_{𝑐})/(𝑑𝑡^{2})=𝜆^{2}𝑒^{𝜆𝑡}` ← t02-s008
- `𝑀𝜆^{2}𝑒^{𝜆𝑡}+𝑏𝜆𝑒^{𝜆𝑡}+𝑘𝑒^{𝜆𝑡}=0 𝑀𝜆^{2}𝑒^{𝜆𝑡}+𝑏𝜆𝑒^{𝜆𝑡}+𝑘𝑒^{𝜆𝑡}=0` ← t02-s008
- `𝑀𝜆^{2}+𝑏𝜆+𝑘=0 𝑀𝜆^{2}+𝑏𝜆+𝑘=0` ← t02-s008
- `𝜆_{1}≠𝜆_{2}` ← t02-s009
- `𝑦_{𝑐}(𝑡)=𝐴𝑒^{𝜆_{1}𝑡}+𝐵𝑒^{𝜆_{2}𝑡}` ← t02-s009
- `𝐴` ← t02-s009
- `𝐵` ← t02-s009
- `𝜆_{1}=𝜆_{2}` ← t02-s009
- `𝑦_{𝑐}(𝑡)=(𝐴+𝐵)𝑒^{𝜆_{1}𝑡}` ← t02-s009
- `𝜆_{1}=𝑟+𝑖𝑠 𝜆_{2}=𝑟−𝑖𝑠` ← t02-s009
- `𝑦_{𝑐}(𝑡)=𝑒^{𝑟𝑡}(𝐴cos((𝑠𝑡))+𝐵sin((𝑠𝑡)))` ← t02-s009
- `𝑦_{𝑐}(𝑡)=𝐴𝑒^{𝜆_{1}𝑡}+𝐵𝑒^{𝜆_{2}𝑡} (𝐴 and 𝐵 are constants)` ← t02-s009
- `If 𝜆_{1}=𝜆_{2}` ← t02-s009
- `𝜆_{1}=𝑟+𝑖𝑠           𝜆_{2}=𝑟−𝑖𝑠` ← t02-s009
- `𝑀=1, 𝑏=2, 𝑘=5` ← t02-s010
- `𝜆^{2}𝑒^{𝜆𝑡}+2𝜆𝑒^{𝜆𝑡}+5𝑒^{𝜆𝑡}=0` ← t02-s010
- `𝜆^{2}+2𝜆+5=0` ← t02-s010
- `𝜆_{1,2}=(−2±sqrt(4−20))/(2)=−1±2𝑖` ← t02-s010
- `𝑦_{𝑐}(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))` ← t02-s010
- `𝑀=1,    𝑏=2,    𝑘=5 𝑀=1,    𝑏=2,    𝑘=5` ← t02-s010
- `(𝑑𝑦_{𝑐})/(𝑑𝑡)=𝜆𝑒^{𝜆𝑡}            (𝑑^{2}𝑦_{𝑐})/(𝑑𝑡^{2})=𝜆^{2}𝑒^{𝜆𝑡}` ← t02-s010
- `𝑦_{𝑐}(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))𝑦_{𝑐}(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))` ← t02-s010
- `𝑀=1, 𝑏=2, 𝑘=5, 𝑟(𝑡)=5𝑡^{2}+12` ← t02-s011
- `𝑦_{𝑝}(𝑡)=𝑃𝑡^{2}+𝑄𝑡+𝐿` ← t02-s011
- `𝑃` ← t02-s011
- `𝑄` ← t02-s011
- `(𝑑𝑦_{𝑝})/(𝑑𝑡)=2𝑃𝑡+𝑄 (𝑑^{2}𝑦_{𝑝})/(𝑑𝑡^{2})=2𝑃` ← t02-s011
- `2𝑃+4𝑃𝑡+2𝑄+5𝑃𝑡^{2}+5𝑄𝑡+5𝐿=5𝑡^{2}+12` ← t02-s011
- `𝑃=1 𝑄=−(4)/(5) 𝐿=(58)/(25)` ← t02-s011
- `𝑦_{𝑝}(𝑡)=𝑡^{2}−(4)/(5)𝑡+(58)/(25)` ← t02-s011
- `(2𝑃+2𝑄+5𝐿=12 ; 4𝑃+5𝑄=0 ; 5𝑃=5)` ← t02-s011
- `2. 𝑀(𝑑^{2}𝑦_{𝑝}(𝑡))/(𝑑𝑡^{2})+𝑏(𝑑𝑦_{𝑝}(𝑡))/(𝑑𝑡)+𝑘𝑦_{𝑝}(𝑡)=𝑟(𝑡)` ← t02-s011
- `𝑀=1,    𝑏=2,    𝑘=5,    𝑟(𝑡)=5𝑡^{2}+12 𝑀=1,    𝑏=2,    𝑘=5,    𝑟(𝑡)=5𝑡^{2}+12` ← t02-s011
- `We choose 𝑦_{𝑝}(𝑡)=𝑃𝑡^{2}+𝑄𝑡+𝐿 (𝑃, 𝑄 and L are constants)` ← t02-s011
- `(𝑑𝑦_{𝑝})/(𝑑𝑡)=2𝑃𝑡+𝑄            (𝑑^{2}𝑦_{𝑝})/(𝑑𝑡^{2})=2𝑃` ← t02-s011
- `Equating coefficients  𝑃=1        𝑄=−(4)/(5)        𝐿=(58)/(25)` ← t02-s011
- `𝑦_{𝑝}(𝑡)=𝑡^{2}−(4)/(5)𝑡+(58)/(25)𝑦_{𝑝}(𝑡)=𝑡^{2}−(4)/(5)𝑡+(58)/(25)` ← t02-s011
- `(2𝑃+2𝑄+5𝐿=12 ; 4𝑃+5𝑄=0 ; 5𝑃=5)(2𝑃+2𝑄+5𝐿=12 ; 4𝑃+5𝑄=0 ; 5𝑃=5)` ← t02-s011
- `𝑦(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))+𝑡^{2}−(4)/(5)𝑡+(58)/(25)` ← t02-s012
- `𝑦(𝑡)=𝑦_{𝑐}(𝑡)+𝑦_{𝑝}(𝑡)𝑦(𝑡)=𝑦_{𝑐}(𝑡)+𝑦_{𝑝}(𝑡)` ← t02-s012
- `𝑦(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))+𝑡^{2}−(4)/(5)𝑡+(58)/(25)𝑦(𝑡)=𝑒^{−𝑡}(𝐴cos(2𝑡)+𝐵sin(2𝑡))+𝑡^{2}−(4)/(5)𝑡+(58)/(25)` ← t02-s012
- `𝑥(𝑡)` ← t02-s014
- `𝑥_{1}(𝑡)` ← t02-s015
- `𝑦_{1}(𝑡)` ← t02-s015
- `𝑥_{2}(𝑡)` ← t02-s015
- `𝑦_{2}(𝑡)` ← t02-s015
- `𝑥_{1}(𝑡)+𝑥_{2}(𝑡)` ← t02-s015
- `𝑦_{1}(𝑡)+𝑦_{2}(𝑡)` ← t02-s015
- `𝑦(𝑥_{1}+𝑥_{2})=𝑦(𝑥_{1})+𝑦(𝑥_{2})` ← t02-s015
- `𝑦(𝑥(𝑡))` ← t02-s016
- `𝛽𝑥(𝑡)` ← t02-s016
- `𝛽𝑦(𝑡)` ← t02-s016
- `𝑦(𝛽𝑥(𝑡))=𝛽𝑦(𝑥(𝑡))` ← t02-s016
- `𝑦(𝑡)=2 𝑥(𝑡)+10` ← t02-s017
- `𝑦_{1}(𝑡)=2 𝑥_{1}(𝑡)+10 𝑦_{2}(𝑡)=2 𝑥_{2}(𝑡)+10` ← t02-s017
- `𝑦(𝑥_{1}+𝑥_{2})=2(𝑥_{1}+𝑥_{2})+10` ← t02-s017
- `𝑦_{1}(𝑡)+𝑦_{2}(𝑡)=2(𝑥_{1}+𝑥_{2})+20` ← t02-s017
- `𝑦(𝑥_{1}+𝑥_{2})≠𝑦_{1}(𝑡)+𝑦_{2}(𝑡)` ← t02-s017
- `System 1: 𝑦(𝑡)=2 𝑥(𝑡)+10` ← t02-s017
- `𝑦_{1}(𝑡)=2 𝑥_{1}(𝑡)+10              𝑦_{2}(𝑡)=2 𝑥_{2}(𝑡)+10 𝑦_{1}(𝑡)=2 𝑥_{1}(𝑡)+10              𝑦_{2}(𝑡)=2 𝑥_{2}(𝑡)+10` ← t02-s017
- `𝑦(𝑡)=𝑥^{2}(𝑡)` ← t02-s018
- `𝑦(𝛽𝑥)=(𝛽𝑥)^{2} 𝛽𝑦(𝑥)=𝛽𝑥^{2}` ← t02-s018
- `𝑦(𝛽𝑥)≠𝛽𝑦(𝑥)` ← t02-s018
- `System 2: 𝑦(𝑡)=𝑥^{2}(𝑡)` ← t02-s018
- `𝑦(𝛽𝑥)=(𝛽𝑥)^{2}                             𝛽𝑦(𝑥)=𝛽𝑥^{2}𝑦(𝛽𝑥)=(𝛽𝑥)^{2}                             𝛽𝑦(𝑥)=𝛽𝑥^{2}` ← t02-s018
- `𝑥_{𝑑}(𝑡)=𝑥(𝑡+𝛿)` ← t02-s019
- `𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)` ← t02-s019
- `𝑦_{1}(𝑡)=𝑦_{2}(𝑡)` ← t02-s019
- `𝑥(𝑡)  𝑦(𝑡) & 𝑥_{𝑑}(𝑡)=𝑥(𝑡+𝛿)  𝑦_{1}(𝑡) & 𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)` ← t02-s019
- `If 𝑦_{1}(𝑡)=𝑦_{2}(𝑡)` ← t02-s019
- `𝑦(𝑡)=10𝑥(𝑡)` ← t02-s020
- `𝑦_{1}(𝑡)=10𝑥_{𝑑}(𝑡)=10𝑥(𝑡+𝛿) 𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=10𝑥(𝑡+𝛿)` ← t02-s020
- `System 1: 𝑦(𝑡)=10𝑥(𝑡)` ← t02-s020
- `𝑦_{1}(𝑡)=10𝑥_{𝑑}(𝑡)=10𝑥(𝑡+𝛿)                    𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=10𝑥(𝑡+𝛿)𝑦_{1}(𝑡)=10𝑥_{𝑑}(𝑡)=10𝑥(𝑡+𝛿)                    𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=10𝑥(𝑡+𝛿)` ← t02-s020
- `𝑦(𝑡)=𝑡∙𝑥(𝑡)` ← t02-s021
- `𝑦_{1}(𝑡)=𝑡∙𝑥_{𝑑}(𝑡)=𝑡∙𝑥(𝑡+𝛿) 𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=(𝑡+𝛿)∙𝑥(𝑡+𝛿)` ← t02-s021
- `𝑦_{1}(𝑡)≠𝑦_{2}(𝑡)` ← t02-s021
- `System 2: 𝑦(𝑡)=𝑡∙𝑥(𝑡)` ← t02-s021
- `𝑦_{1}(𝑡)=𝑡∙𝑥_{𝑑}(𝑡)=𝑡∙𝑥(𝑡+𝛿)           𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=(𝑡+𝛿)∙𝑥(𝑡+𝛿)𝑦_{1}(𝑡)=𝑡∙𝑥_{𝑑}(𝑡)=𝑡∙𝑥(𝑡+𝛿)           𝑦_{2}(𝑡)=𝑦(𝑡+𝛿)=(𝑡+𝛿)∙𝑥(𝑡+𝛿)` ← t02-s021
- `𝑥` ← t02-s024
- `𝑦` ← t02-s024
- `𝑦(𝑡)=𝑔(𝑥(𝑡))` ← t02-s024
- `𝑥_{0}` ← t02-s024
- `𝑦_{0}` ← t02-s024
- `𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)+((𝑑^{2}𝑔)/(𝑑𝑥^{2}))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0})^{2})/(2!)+…` ← t02-s024
- `𝑦(𝑡)=𝑔(𝑥(𝑡))𝑦(𝑡)=𝑔(𝑥(𝑡))` ← t02-s024
- `𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)+((𝑑^{2}𝑔)/(𝑑𝑥^{2}))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0})^{2})/(2!)+…𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)+((𝑑^{2}𝑔)/(𝑑𝑥^{2}))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0})^{2})/(2!)+…` ← t02-s024
- `𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)` ← t02-s025
- `𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)𝑦(𝑡)=𝑔(𝑥(𝑡))=𝑔(𝑥_{0})+((𝑑𝑔)/(𝑑𝑥))_{𝑥(𝑡)=𝑥_{0}}((𝑥(𝑡)−𝑥_{0}))/(1!)` ← t02-s025
- `𝑇(𝑡)=𝑀𝑔𝐿sin(𝜃(𝑡))` ← t02-s026
- `𝜃_{0}=0` ← t02-s026
- `𝑇(𝑡)=𝑀𝑔𝐿sin(𝜃(𝑡))𝑇(𝑡)=𝑀𝑔𝐿sin(𝜃(𝑡))` ← t02-s026
- `Equilibrium point: 𝜃_{0}=0` ← t02-s026
- `𝑇(𝑡)≈𝑇_{0}+(𝑀𝑔𝐿(𝜕sin(𝜃))/(𝜕𝜃))_{𝜃(𝑡)=𝜃_{0}}(𝜃(𝑡)−𝜃_{0})` ← t02-s027
- `𝑇_{0}=0` ← t02-s028
- `𝑇(𝑡)≈𝑀𝑔𝐿 𝜃(𝑡)` ← t02-s028
- `𝑇(𝑡)≈𝑇_{0}+(𝑀𝑔𝐿(𝜕sin(𝜃))/(𝜕𝜃))_{𝜃(𝑡)=𝜃_{0}}(𝜃(𝑡)−𝜃_{0})𝑇(𝑡)≈𝑇_{0}+(𝑀𝑔𝐿(𝜕sin(𝜃))/(𝜕𝜃))_{𝜃(𝑡)=𝜃_{0}}(𝜃(𝑡)−𝜃_{0})` ← t02-s028
- `But 𝑇_{0}=0` ← t02-s028
- `𝑇(𝑡)≈𝑀𝑔𝐿 𝜃(𝑡)𝑇(𝑡)≈𝑀𝑔𝐿 𝜃(𝑡)` ← t02-s028
- `−(𝜋)/(4)≤𝜃≤(𝜋)/(4)` ← t02-s029
- `𝑇(𝑡)≈𝑀𝑔𝐿 𝜃(𝑡)` ← t02-s029
- `𝑥_{1}(𝑡), 𝑥_{2}(𝑡), … , 𝑥_{𝑛}(𝑡)` ← t02-s030
- `𝑦(𝑡)=𝑔(𝑥_{1}(𝑡), 𝑥_{2}(𝑡), … , 𝑥_{𝑛}(𝑡))` ← t02-s030
- `𝑥_{1_{0}}, 𝑥_{2_{0}}, … , 𝑥_{𝑛_{0}}` ← t02-s030
- `𝑦(𝑡)=𝑔(𝑥_{1_{0}}, 𝑥_{2_{0}}, … , 𝑥_{𝑛_{0}})+((𝜕𝑔)/(𝜕𝑥_{1}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{1}(𝑡)−𝑥_{1_{0}})+((𝜕𝑔)/(𝜕𝑥_{2}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{2}(𝑡)−𝑥_{2_{0}})+…` ← t02-s030
- `+((𝜕𝑔)/(𝜕𝑥_{𝑛}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{𝑛}(𝑡)−𝑥_{𝑛_{0}})` ← t02-s030
- `𝑦(𝑡)=𝑔(𝑥_{1}(𝑡), 𝑥_{2}(𝑡), … , 𝑥_{𝑛}(𝑡))` ← t02-s030
- `𝑦(𝑡)=𝑔(𝑥_{1_{0}}, 𝑥_{2_{0}}, … , 𝑥_{𝑛_{0}})+((𝜕𝑔)/(𝜕𝑥_{1}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{1}(𝑡)−𝑥_{1_{0}})+((𝜕𝑔)/(𝜕𝑥_{2}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{2}(𝑡)−𝑥_{2_{0}})+…+((𝜕𝑔)/(𝜕𝑥_{𝑛}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{𝑛}(𝑡)−𝑥_{𝑛_{0}})𝑦(𝑡)=𝑔(𝑥_{1_{0}}, 𝑥_{2_{0}}, … , 𝑥_{𝑛_{0}})+((𝜕𝑔)/(𝜕𝑥_{1}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{1}(𝑡)−𝑥_{1_{0}})+((𝜕𝑔)/(𝜕𝑥_{2}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{2}(𝑡)−𝑥_{2_{0}})+…+((𝜕𝑔)/(𝜕𝑥_{𝑛}))_{𝑥(𝑡)=𝑥_{0}}(𝑥_{𝑛}(𝑡)−𝑥_{𝑛_{0}})` ← t02-s030
- `𝑓(𝑡) (𝑓(𝑡)=0 𝑓𝑜𝑟 𝑡<0)` ← t02-s032
- `ℒ` ← t02-s032
- `ℒ^{−1}` ← t02-s032
- `𝐹(𝑠)=ℒ(𝑓(𝑡))≔∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)` ← t02-s032
- `𝐹(𝑠)` ← t02-s032
- `𝑓(𝑡)` ← t02-s032
- `Definition: For a function 𝑓(𝑡)   (𝑓(𝑡)=0 𝑓𝑜𝑟 𝑡<0)` ← t02-s032
- `ℒ ℒ` ← t02-s032
- `𝐹(𝑠)=ℒ(𝑓(𝑡))≔∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)𝐹(𝑠)=ℒ(𝑓(𝑡))≔∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)` ← t02-s032
- `ℒ^{−1}(𝐹(𝑠))=(1)/(2𝜋𝑗)∫_{𝜎−𝑗∞}^{𝜎+𝑗∞}(𝐹(𝑠)𝑒^{+𝑠𝑡}𝑑𝑠)` ← t02-s033
- `ℒ^{−1}(𝐹(𝑠))=(1)/(2𝜋𝑗)∫_{𝜎−𝑗∞}^{𝜎+𝑗∞}(𝐹(𝑠)𝑒^{+𝑠𝑡}𝑑𝑠)ℒ^{−1}(𝐹(𝑠))=(1)/(2𝜋𝑗)∫_{𝜎−𝑗∞}^{𝜎+𝑗∞}(𝐹(𝑠)𝑒^{+𝑠𝑡}𝑑𝑠)` ← t02-s033
- `𝑓(𝑡)=10𝑢(𝑡)=(10, 𝑡≥0 ; &0, 𝑡<0)` ← t02-s034
- `𝐹(𝑠)=∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)=∫_{0}^{∞}(10𝑒^{−𝑠𝑡}𝑑𝑡)=10∫_{0}^{∞}(𝑒^{−𝑠𝑡}𝑑𝑡)` ← t02-s034
- `=10(−(1)/(𝑠)(𝑒^{−𝑠𝑡})_{0}^{∞})=10(0−(−(1)/(𝑠)))=(10)/(𝑠)` ← t02-s034
- `ℒ(𝑢(𝑡))=(1)/(𝑠)` ← t02-s034
- `𝑓(𝑡)=10𝑢(𝑡)=(10,  𝑡≥0 ; &0,  𝑡<0)` ← t02-s034
- `𝐹(𝑠)=∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)=∫_{0}^{∞}(10𝑒^{−𝑠𝑡}𝑑𝑡)=10∫_{0}^{∞}(𝑒^{−𝑠𝑡}𝑑𝑡)=10(−(1)/(𝑠)(𝑒^{−𝑠𝑡})_{0}^{∞})=10(0−(−(1)/(𝑠)))=(10)/(𝑠)𝐹(𝑠)=∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)=∫_{0}^{∞}(10𝑒^{−𝑠𝑡}𝑑𝑡)=10∫_{0}^{∞}(𝑒^{−𝑠𝑡}𝑑𝑡)=10(−(1)/(𝑠)(𝑒^{−𝑠𝑡})_{0}^{∞})=10(0−(−(1)/(𝑠)))=(10)/(𝑠)` ← t02-s034
- `ℒ(𝑢(𝑡))=(1)/(𝑠)ℒ(𝑢(𝑡))=(1)/(𝑠)` ← t02-s034
- `ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=𝛼_{1}ℒ(𝑓_{1}(𝑡))+𝛼_{2}ℒ(𝑓_{2}(𝑡))=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)` ← t02-s038
- `ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=∫_{0}^{∞}((𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡)))𝑒^{−𝑠𝑡}𝑑𝑡` ← t02-s038
- `=𝛼_{1}∫_{0}^{∞}(𝑓_{1}(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)+𝛼_{2}∫_{0}^{∞}(𝑓_{2}(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)` ← t02-s038
- `=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)` ← t02-s038
- `ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=𝛼_{1}ℒ(𝑓_{1}(𝑡))+𝛼_{2}ℒ(𝑓_{2}(𝑡))=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=𝛼_{1}ℒ(𝑓_{1}(𝑡))+𝛼_{2}ℒ(𝑓_{2}(𝑡))=𝛼_{1}𝐹_{1}(𝑠)+𝛼_{2}𝐹_{2}(𝑠)` ← t02-s038
- `ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=∫_{0}^{∞}((𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡)))𝑒^{−𝑠𝑡}𝑑𝑡 ℒ(𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡))=∫_{0}^{∞}((𝛼_{1}𝑓_{1}(𝑡)+𝛼_{2}𝑓_{2}(𝑡)))𝑒^{−𝑠𝑡}𝑑𝑡` ← t02-s038
- `ℒ(4𝑢(𝑡)+5𝑒^{−2𝑡})` ← t02-s039
- `=4ℒ(𝑢(𝑡))+5ℒ(𝑒^{−2𝑡})` ← t02-s039
- `=(4)/(𝑠)+(5)/(𝑠+2)` ← t02-s039
- `Example: ℒ(4𝑢(𝑡)+5𝑒^{−2𝑡})` ← t02-s039
- `=4ℒ(𝑢(𝑡))+5ℒ(𝑒^{−2𝑡})=4ℒ(𝑢(𝑡))+5ℒ(𝑒^{−2𝑡})` ← t02-s039
- `=(4)/(𝑠)+(5)/(𝑠+2)=(4)/(𝑠)+(5)/(𝑠+2)` ← t02-s039
- `ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0)` ← t02-s040
- `ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡` ← t02-s040
- `∫_{0}^{∞}(𝑢(𝑑𝑣)/(𝑑𝑡))𝑑𝑡=𝑢𝑣−∫_{0}^{∞}(𝑣(𝑑𝑢)/(𝑑𝑡)𝑑𝑡)` ← t02-s040
- `ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)` ← t02-s040
- `(𝑑𝑣)/(𝑑𝑡)` ← t02-s040
- `𝑢` ← t02-s040
- `ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡 ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡` ← t02-s040
- `Hint: Integration by parts  ∫_{0}^{∞}(𝑢(𝑑𝑣)/(𝑑𝑡))𝑑𝑡=𝑢𝑣−∫_{0}^{∞}(𝑣(𝑑𝑢)/(𝑑𝑡)𝑑𝑡)` ← t02-s040
- `ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)` ← t02-s040
- `ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡=(𝑓(𝑡)𝑒^{−𝑠𝑡})_{0}^{∞}+𝑠∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)` ← t02-s041
- `ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0) ℒ(𝑓^{𝑘}(𝑡))=𝑠^{𝑘}𝐹(𝑠)−𝑠^{𝑘−1}𝑓(0)−𝑠^{𝑘−2}𝑓^{′}(0)−…−𝑓^{𝑘−1}(0)` ← t02-s041
- `ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡=(𝑓(𝑡)𝑒^{−𝑠𝑡})_{0}^{∞}+𝑠∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)ℒ(𝑓′(𝑡))=∫_{0}^{∞}(𝑓′(𝑡))𝑒^{−𝑠𝑡}𝑑𝑡=(𝑓(𝑡)𝑒^{−𝑠𝑡})_{0}^{∞}+𝑠∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)` ← t02-s041
- `ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0)ℒ(𝑓′(𝑡))=𝑠𝐹(𝑠)−𝑓(0)` ← t02-s041
- `ℒ((𝑑(sin((2𝑡))))/(𝑑𝑡))` ← t02-s042
- `=𝑠(2)/(𝑠^{2}+4)` ← t02-s042
- `−sin(0=(2𝑠)/(𝑠^{2}+4))` ← t02-s042
- `Example: ℒ((𝑑(sin((2𝑡))))/(𝑑𝑡))` ← t02-s042
- `=𝑠(2)/(𝑠^{2}+4)=𝑠(2)/(𝑠^{2}+4)` ← t02-s042
- `−sin(0=(2𝑠)/(𝑠^{2}+4))−sin(0=(2𝑠)/(𝑠^{2}+4))` ← t02-s042
- `ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=(𝐹(𝑠))/(𝑠)` ← t02-s043
- `ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=∫_{0}^{∞}((∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏)))𝑒^{−𝑠𝑡}𝑑𝑡` ← t02-s043
- `=(−(1)/(𝑠)(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))𝑒^{−𝑠𝑡})_{0}^{∞}+(1)/(𝑠)∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)` ← t02-s043
- `=(𝐹(𝑠))/(𝑠)` ← t02-s043
- `ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=(𝐹(𝑠))/(𝑠)ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=(𝐹(𝑠))/(𝑠)` ← t02-s043
- `ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=∫_{0}^{∞}((∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏)))𝑒^{−𝑠𝑡}𝑑𝑡 ℒ(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))=∫_{0}^{∞}((∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏)))𝑒^{−𝑠𝑡}𝑑𝑡` ← t02-s043
- `=(−(1)/(𝑠)(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))𝑒^{−𝑠𝑡})_{0}^{∞}+(1)/(𝑠)∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)=(−(1)/(𝑠)(∫_{0}^{𝑡}(𝑓(𝜏)𝑑𝜏))𝑒^{−𝑠𝑡})_{0}^{∞}+(1)/(𝑠)∫_{0}^{∞}(𝑓(𝑡)𝑒^{−𝑠𝑡}𝑑𝑡)` ← t02-s043
- `=(𝐹(𝑠))/(𝑠)=(𝐹(𝑠))/(𝑠)` ← t02-s043
- `(𝑑)/(𝑑𝑡)` ← t02-s044
- `𝑠` ← t02-s044
- `∫_{0}^{𝑡}(𝑑𝑡)` ← t02-s044
- `(1)/(𝑠)` ← t02-s044
- `∫_{0}^{𝑡}(𝑑𝑡)∫_{0}^{𝑡}(𝑑𝑡)` ← t02-s044
- `2(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+6(𝑑𝑦(𝑡))/(𝑑𝑡)+4𝑦(𝑡)=𝑟(𝑡)` ← t02-s045
- `2(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0)−((𝑑𝑦)/(𝑑𝑡))_{𝑡=0})+6(𝑠𝑌(𝑠)−𝑦(0))+4𝑌(𝑠)=𝑅(𝑠)` ← t02-s045
- `𝑟(𝑡)=0 𝑎𝑛𝑑 𝑦(0)=𝑦_{0} 𝑎𝑛𝑑 ((𝑑𝑦)/(𝑑𝑡))_{𝑡=0}=0` ← t02-s045
- `2𝑠^{2}𝑌(𝑠)−2𝑠𝑦_{0}+6𝑠𝑌(𝑠)−6𝑦_{0}+4𝑌(𝑠)=0` ← t02-s045
- `𝑌(𝑠)` ← t02-s045
- `𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))` ← t02-s045
- `2(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+6(𝑑𝑦(𝑡))/(𝑑𝑡)+4𝑦(𝑡)=𝑟(𝑡)2(𝑑^{2}𝑦(𝑡))/(𝑑𝑡^{2})+6(𝑑𝑦(𝑡))/(𝑑𝑡)+4𝑦(𝑡)=𝑟(𝑡)` ← t02-s045
- `2(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0)−((𝑑𝑦)/(𝑑𝑡))_{𝑡=0})+6(𝑠𝑌(𝑠)−𝑦(0))+4𝑌(𝑠)=𝑅(𝑠)2(𝑠^{2}𝑌(𝑠)−𝑠𝑦(0)−((𝑑𝑦)/(𝑑𝑡))_{𝑡=0})+6(𝑠𝑌(𝑠)−𝑦(0))+4𝑌(𝑠)=𝑅(𝑠)` ← t02-s045
- `When 𝑟(𝑡)=0  𝑎𝑛𝑑  𝑦(0)=𝑦_{0}  𝑎𝑛𝑑  ((𝑑𝑦)/(𝑑𝑡))_{𝑡=0}=0` ← t02-s045
- `We have 2𝑠^{2}𝑌(𝑠)−2𝑠𝑦_{0}+6𝑠𝑌(𝑠)−6𝑦_{0}+4𝑌(𝑠)=0` ← t02-s045
- `Solving for 𝑌(𝑠): 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))` ← t02-s045
- `𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=((𝑠+3)𝑦_{0})/(𝑠^{2}+3𝑠+2)` ← t02-s046
- `𝑠=−3` ← t02-s046
- `𝑠=−1 𝑎𝑛𝑑 𝑠=−2` ← t02-s046
- `𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=((𝑠+3)𝑦_{0})/(𝑠^{2}+3𝑠+2)𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=((𝑠+3)𝑦_{0})/(𝑠^{2}+3𝑠+2)` ← t02-s046
- `Zero: 𝑠=−3` ← t02-s046
- `Poles: 𝑠=−1  𝑎𝑛𝑑  𝑠=−2` ← t02-s046
- `𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2)` ← t02-s047
- `𝑦_{0}=1` ← t02-s047
- `𝑌(𝑠)=(𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2})/((𝑠+1)(𝑠+2))=((𝑠+3))/((𝑠+1)(𝑠+2))` ← t02-s047
- `𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3` ← t02-s047
- `Back to solving: 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2)` ← t02-s047
- `Let 𝑦_{0}=1` ← t02-s047
- `𝑌(𝑠)=(𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2})/((𝑠+1)(𝑠+2))=((𝑠+3))/((𝑠+1)(𝑠+2))𝑌(𝑠)=(𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2})/((𝑠+1)(𝑠+2))=((𝑠+3))/((𝑠+1)(𝑠+2))` ← t02-s047
- `𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3 𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3` ← t02-s047
- `(𝑘_{1}+𝑘_{2}=1 ; 2𝑘_{1}+𝑘_{2}=3)` ← t02-s048
- `(𝑘_{1}=2 ; 𝑘_{2}=−1)` ← t02-s048
- `𝑌(𝑠)=(2)/(𝑠+1)+(−1)/(𝑠+2)` ← t02-s048
- `Back to solving: 𝑌(𝑠)=((𝑠+3)𝑦_{0})/((𝑠+1)(𝑠+2))=(𝑘_{1})/(𝑠+1)+(𝑘_{2})/(𝑠+2) Let 𝑦_{0}=1` ← t02-s048
- `𝑘_{1}𝑠+2𝑘_{1}+𝑘_{2}𝑠+𝑘_{2}=𝑠+3  (𝑘_{1}+𝑘_{2}=1 ; 2𝑘_{1}+𝑘_{2}=3)  (𝑘_{1}=2 ; 𝑘_{2}=−1)` ← t02-s048
- `𝑌(𝑠)=(2)/(𝑠+1)+(−1)/(𝑠+2)𝑌(𝑠)=(2)/(𝑠+1)+(−1)/(𝑠+2)` ← t02-s048
- `𝑦(𝑡)=ℒ^{−1}((2)/(𝑠+1))+ℒ^{−1}((−1)/(𝑠+2))` ← t02-s049
- `𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}` ← t02-s049
- `𝑦(𝑡)=ℒ^{−1}((2)/(𝑠+1))+ℒ^{−1}((−1)/(𝑠+2))𝑦(𝑡)=ℒ^{−1}((2)/(𝑠+1))+ℒ^{−1}((−1)/(𝑠+2))` ← t02-s049
- `𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}` ← t02-s049
- `lim𝑡→∞(𝑓(𝑡))=lim𝑠→0(𝑠𝐹(𝑠))` ← t02-s050
- `𝑠𝐹(𝑠)` ← t02-s050
- `𝑌(𝑠)=((𝑠+3))/((𝑠+1)(𝑠+2)) → 𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}` ← t02-s050
- `𝑠=−1 & 𝑠=−2` ← t02-s050
- `lim𝑡→∞(𝑦(𝑡))=lim𝑠→0(𝑠𝑌(𝑠))=0` ← t02-s050
- `lim𝑡→∞(𝑓(𝑡))=lim𝑠→0(𝑠𝐹(𝑠)) applicable if all the poles of 𝑠𝐹(𝑠) are in the left half plane (LHP)` ← t02-s050
- `𝑌(𝑠)=((𝑠+3))/((𝑠+1)(𝑠+2))   →   𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}𝑌(𝑠)=((𝑠+3))/((𝑠+1)(𝑠+2))   →   𝑦(𝑡)=2𝑒^{−𝑡}−1𝑒^{−2𝑡}` ← t02-s050
- `Poles: 𝑠=−1 & 𝑠=−2 (LHP)` ← t02-s050
- `lim𝑡→∞(𝑦(𝑡))=lim𝑠→0(𝑠𝑌(𝑠))=0 lim𝑡→∞(𝑦(𝑡))=lim𝑠→0(𝑠𝑌(𝑠))=0` ← t02-s050
- `ℒ^{−1}ℒ^{−1}` ← t02-s051
- `𝑦^{′′}(𝑡)−𝑦(𝑡)=𝑡, 𝑦(0)=1, 𝑦^{′}(0)=1` ← t02-s052
- `𝑠^{2}𝑌(𝑠)−𝑠−1−𝑌(𝑠)=(1!)/(𝑠^{1+1})=(1)/(𝑠^{2})` ← t02-s052
- `(𝑠^{2}−1)𝑌(𝑠)−(𝑠+1)=(1)/(𝑠^{2})` ← t02-s052
- `𝑌(𝑠)=(1)/(𝑠^{2}(𝑠^{2}−1))+(𝑠+1)/(𝑠^{2}−1)=(1+𝑠^{3}+𝑠^{2})/(𝑠^{2}(𝑠^{2}−1))=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))` ← t02-s052
- `𝑦^{′′}(𝑡)−𝑦(𝑡)=𝑡,    𝑦(0)=1,   𝑦^{′}(0)=1 𝑦^{′′}(𝑡)−𝑦(𝑡)=𝑡,    𝑦(0)=1,   𝑦^{′}(0)=1` ← t02-s052
- `𝑠^{2}𝑌(𝑠)−𝑠−1−𝑌(𝑠)=(1!)/(𝑠^{1+1})=(1)/(𝑠^{2})𝑠^{2}𝑌(𝑠)−𝑠−1−𝑌(𝑠)=(1!)/(𝑠^{1+1})=(1)/(𝑠^{2})` ← t02-s052
- `(𝑠^{2}−1)𝑌(𝑠)−(𝑠+1)=(1)/(𝑠^{2})(𝑠^{2}−1)𝑌(𝑠)−(𝑠+1)=(1)/(𝑠^{2})` ← t02-s052
- `𝑌(𝑠)=(1)/(𝑠^{2}(𝑠^{2}−1))+(𝑠+1)/(𝑠^{2}−1)=(1+𝑠^{3}+𝑠^{2})/(𝑠^{2}(𝑠^{2}−1))=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))𝑌(𝑠)=(1)/(𝑠^{2}(𝑠^{2}−1))+(𝑠+1)/(𝑠^{2}−1)=(1+𝑠^{3}+𝑠^{2})/(𝑠^{2}(𝑠^{2}−1))=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))` ← t02-s052
- `𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))` ← t02-s053
- `(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)` ← t02-s053
- `𝑠^{3}+𝑠^{2}+1=(𝐴𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠)+(𝐵𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠^{2})+(𝐶𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠−1)+(𝐷𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠+1)` ← t02-s053
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)` ← t02-s053
- `𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))𝑌(𝑠)=(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))` ← t02-s053
- `(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)(𝑠^{3}+𝑠^{2}+1)/(𝑠^{2}(𝑠−1)(𝑠+1))=(𝐴)/(𝑠)+(𝐵)/(𝑠^{2})+(𝐶)/(𝑠−1)+(𝐷)/(𝑠+1)` ← t02-s053
- `𝑠^{3}+𝑠^{2}+1=(𝐴𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠)+(𝐵𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠^{2})+(𝐶𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠−1)+(𝐷𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠+1)𝑠^{3}+𝑠^{2}+1=(𝐴𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠)+(𝐵𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠^{2})+(𝐶𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠−1)+(𝐷𝑠^{2}(𝑠−1)(𝑠+1))/(𝑠+1)` ← t02-s053
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)+𝐵(𝑠−1)(𝑠+1)+𝐶𝑠^{2}(𝑠+1)+𝐷𝑠^{2}(𝑠−1)` ← t02-s053
- `(𝑟𝑜𝑜𝑡 0:−𝐵=1 ; 𝑟𝑜𝑜𝑡 1: 𝐶=(3)/(2) ; 𝑟𝑜𝑜𝑡 −1: 𝐷=−(1)/(2))` ← t02-s054
- `𝐵=−1, 𝐶=(3)/(2), 𝐷=−(1)/(2)` ← t02-s054
- `(𝑟𝑜𝑜𝑡 0:−𝐵=1 ; 𝑟𝑜𝑜𝑡 1:    𝐶=(3)/(2) ; 𝑟𝑜𝑜𝑡 −1:   𝐷=−(1)/(2))  𝐵=−1,  𝐶=(3)/(2),   𝐷=−(1)/(2)` ← t02-s054
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)−1(𝑠−1)(𝑠+1)+(3)/(2)𝑠^{2}(𝑠+1)−(1)/(2)𝑠^{2}(𝑠−1)` ← t02-s055
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠^{3}−𝐴𝑠−𝑠^{2}+1+(3)/(2)𝑠^{3}+(3)/(2)𝑠^{2}−(1)/(2)𝑠^{3}+(1)/(2)𝑠^{2}` ← t02-s055
- `𝐴=0` ← t02-s055
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)−1(𝑠−1)(𝑠+1)+(3)/(2)𝑠^{2}(𝑠+1)−(1)/(2)𝑠^{2}(𝑠−1)𝑠^{3}+𝑠^{2}+1=𝐴𝑠(𝑠−1)(𝑠+1)−1(𝑠−1)(𝑠+1)+(3)/(2)𝑠^{2}(𝑠+1)−(1)/(2)𝑠^{2}(𝑠−1)` ← t02-s055
- `𝑠^{3}+𝑠^{2}+1=𝐴𝑠^{3}−𝐴𝑠−𝑠^{2}+1+(3)/(2)𝑠^{3}+(3)/(2)𝑠^{2}−(1)/(2)𝑠^{3}+(1)/(2)𝑠^{2}𝑠^{3}+𝑠^{2}+1=𝐴𝑠^{3}−𝐴𝑠−𝑠^{2}+1+(3)/(2)𝑠^{3}+(3)/(2)𝑠^{2}−(1)/(2)𝑠^{3}+(1)/(2)𝑠^{2}` ← t02-s055
- `𝐴=0 𝐴=0` ← t02-s055
- `𝑌(𝑠)=(0)/(𝑠)+(−1)/(𝑠^{2})+((3)/(2))/(𝑠−1)+(−(1)/(2))/(𝑠+1)` ← t02-s056
- `𝑦(𝑡)=−𝑡+(3)/(2)𝑒^{𝑡}−(1)/(2)𝑒^{−𝑡}` ← t02-s056
- `𝑌(𝑠)=(0)/(𝑠)+(−1)/(𝑠^{2})+((3)/(2))/(𝑠−1)+(−(1)/(2))/(𝑠+1)𝑌(𝑠)=(0)/(𝑠)+(−1)/(𝑠^{2})+((3)/(2))/(𝑠−1)+(−(1)/(2))/(𝑠+1)` ← t02-s056
- `𝑦(𝑡)=−𝑡+(3)/(2)𝑒^{𝑡}−(1)/(2)𝑒^{−𝑡}𝑦(𝑡)=−𝑡+(3)/(2)𝑒^{𝑡}−(1)/(2)𝑒^{−𝑡}` ← t02-s056
