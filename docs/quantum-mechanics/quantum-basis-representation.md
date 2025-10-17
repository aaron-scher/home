# Quantum Mechanics: Basis Representation

**Prerequisites:** This builds on [Quantum Foundations](quantum-foundations.md) where we derived Schrödinger's equation and explored the harmonic oscillator. If you haven't read that yet, start there first!

---

## One Wavefunction, Many Faces

In Part 1, we solved the harmonic oscillator and found energy eigenstates $\psi_n(x)$, Gaussians with increasing nodes, each with energy $E_n = \hbar\omega(n + \frac{1}{2})$. We mentioned these have momentum space versions $\tilde{\psi}_n(p)$ via Fourier transform.

Here's something cool: any wavefunction can be written as a sum of energy eigenstates:

$$\psi(x) = c_0 \psi_0(x) + c_1 \psi_1(x) + c_2 \psi_2(x) + ...$$

where $\psi_0(x), \psi_1(x), \psi_2(x), ...$ are the energy eigenstates from Part 1 (each one is a solution to Schrödinger's equation at a specific energy $E_n$), and $c_0, c_1, c_2, ...$ are complex number coefficients telling you "how much" of each eigenstate to include.

But here's the deeper question: **What IS the quantum state?** Is it the function $\psi(x)$? The coefficients $[c_0, c_1, c_2, ...]$? The momentum function $\tilde{\psi}(p)$? Or something more fundamental?

The answer: there's an abstract quantum state $|\psi\rangle$ (called a "ket") that exists independent of how we describe it. The different functions we use are just different ways of writing down the same underlying thing:

- $\psi(x)$ = position representation (a function of position)
- $\tilde{\psi}(p)$ = momentum representation (a function of momentum)
- $[c_0, c_1, c_2, ...]$ = energy representation (a list of coefficients)

Same state, different descriptions! Like how a 3D vector doesn't change whether you use Cartesian or spherical coordinates. The vector itself is the same; only the numbers you write change.

---

## What Is the Abstract State |ψ⟩?

The ket $|\psi\rangle$ is the complete quantum state, the thing itself before you choose how to describe it.

**The loaded die analogy:** A die sitting on the table IS the state. It contains all probabilities for different outcomes. When you roll it (measure), you get one specific number. Before rolling, it's "all possibilities at once."

**The vector analogy:** An arrow in 3D space doesn't change if you describe it using Cartesian coordinates $(x, y, z)$ or cylindrical coordinates $(r, \theta, z)$. It's the same arrow, same length, same direction. Only the numbers change. The arrow itself is basis-independent.

Similarly, $|\psi\rangle$ exists independent of whether you ask about position, momentum, or energy. It contains all the information; you just need to choose which representation to use.

---

## Building States from Basis Vectors

Just like $\vec{v} = v_x\hat{x} + v_y\hat{y} + v_z\hat{z}$ in 3D, we build quantum states from basis vectors. For the harmonic oscillator:

$$|\psi\rangle = c_0 |0\rangle + c_1 |1\rangle + c_2 |2\rangle + ...$$

where $|0\rangle, |1\rangle, |2\rangle, ...$ are energy eigenstates (those Gaussian wavefunctions from Part 1, but now written as abstract vectors).

You're adding up vectors! Each term is a basis vector $|n\rangle$ scaled by a complex number $c_n$. In compact form, we write this as:

$$|\psi\rangle = \sum_{n=0}^{\infty} c_n |n\rangle$$

**Concrete example:** Let's use:
- $c_0 = \frac{1}{2}$
- $c_1 = \frac{\sqrt{2}}{2}$
- $c_2 = \frac{1}{2}$
- All others zero

Then:

$$|\psi\rangle = \frac{1}{2}|0\rangle + \frac{\sqrt{2}}{2}|1\rangle + \frac{1}{2}|2\rangle$$

This is vector addition, just like $\vec{v} = 2\hat{x} + 3\hat{y} - \hat{z}$ in 3D. Take half of basis vector $|0\rangle$, add $\sqrt{2}/2$ of basis vector $|1\rangle$, add half of basis vector $|2\rangle$. Done!

### Column Vector Form

Just like in 3D where we can write $\hat{x} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$, we can write energy eigenstates as column vectors. Each basis vector has a 1 in its position and 0 everywhere else:

$$
|0\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ \vdots \end{pmatrix}, \quad
|1\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ \vdots \end{pmatrix}, \quad
|2\rangle = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix}, \quad \text{etc.}
$$

Then our state becomes:

$$
|\psi\rangle = \frac{1}{2}\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ \vdots \end{pmatrix} + \frac{\sqrt{2}}{2}\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ \vdots \end{pmatrix} + \frac{1}{2}\begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix} = \begin{pmatrix} 1/2 \\ \sqrt{2}/2 \\ 1/2 \\ 0 \\ \vdots \end{pmatrix}
$$

The coefficients $c_0, c_1, c_2, ...$ are just the entries in the column vector! The sum $\sum c_n |n\rangle$ is assembling this column vector by adding scaled basis vectors.

---

## Components as Functions

Here's a useful way to think about the parallel between discrete and continuous: both use functions to specify amplitudes.

**Energy basis:** The coefficients $c_0, c_1, c_2, ...$ can be thought of as a discrete function c[n] where you input an integer n and get back the amplitude for that energy level.

**Position basis:** The wavefunction $\psi(x)$ is a continuous function where you input a real number x and get back the amplitude at that position.

Same idea, different domains! The discrete case uses integers (n = 0, 1, 2, ...) while the continuous case uses real numbers (any x).

This parallel becomes important when we see that:
- Discrete sums: $|\psi\rangle = \sum_n c_n|n\rangle$
- Continuous integrals: $|\psi\rangle = \int \psi(x)|x\rangle dx$

Same pattern, just sum vs integral!

---

## Extracting Components: Inner Products

We have $|\psi\rangle = \frac{1}{2}|0\rangle + \frac{\sqrt{2}}{2}|1\rangle + \frac{1}{2}|2\rangle$. But how do we GET these coefficients from the abstract state?

### The Quantum Dot Product

In 3D, how do we extract a specific component like $v_y$ from a vector $\vec{v}$? We use the **dot product**, which projects the vector onto an axis.

**Concrete example:** Suppose $\vec{v} = 2\hat{x} + 3\hat{y} + 1\hat{z}$. To extract the y-component:

$$v_y = \vec{v} \cdot \hat{y} = (2\hat{x} + 3\hat{y} + 1\hat{z}) \cdot \hat{y}$$

The dot product picks out just the y-component because:
- $\hat{x} \cdot \hat{y} = 0$ (perpendicular)
- $\hat{y} \cdot \hat{y} = 1$ (parallel)
- $\hat{z} \cdot \hat{y} = 0$ (perpendicular)

So: $v_y = 2(0) + 3(1) + 1(0) = 3$

The dot product "projects" $\vec{v}$ onto the y-axis and tells you how much of $\vec{v}$ points in that direction. Quantum mechanics works the same way!

We introduce **bras** $\langle\psi|$ (think "row vectors") to pair with **kets** $|\psi\rangle$ (think "column vectors"):

$$\langle\phi|\psi\rangle = \text{"bra-ket"} = \text{"bracket"} = \text{inner product}$$

**What's a bra exactly?** It's the conjugate transpose of the ket. If:

$$|\psi\rangle = \begin{pmatrix} 1/2 \\ \sqrt{2}/2 \\ 1/2 \end{pmatrix}$$

Then the bra is:

$$\langle\psi| = \begin{pmatrix} 1/2 & \sqrt{2}/2 & 1/2 \end{pmatrix}$$

(For real numbers, it's just transpose. For complex numbers, you also take complex conjugates.)

**Concrete inner product example:** Let's compute $\langle 1|\psi\rangle$ to extract the coefficient $c_1$:

$$\langle 1| = \begin{pmatrix} 0 & 1 & 0 \end{pmatrix}, \quad |\psi\rangle = \begin{pmatrix} 1/2 \\ \sqrt{2}/2 \\ 1/2 \end{pmatrix}$$

$$\langle 1|\psi\rangle = \begin{pmatrix} 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 1/2 \\ \sqrt{2}/2 \\ 1/2 \end{pmatrix} = 0 \cdot \frac{1}{2} + 1 \cdot \frac{\sqrt{2}}{2} + 0 \cdot \frac{1}{2} = \frac{\sqrt{2}}{2}$$

This is just row-times-column matrix multiplication! The inner product picks out the second entry.

### Orthonormal Basis Vectors

Energy eigenstates are orthonormal:

$$\langle m|n\rangle = \begin{cases} 1 & \text{if } m = n \\ 0 & \text{if } m \neq n \end{cases}$$

Just like $\hat{x} \cdot \hat{y} = 0$ and $\hat{x} \cdot \hat{x} = 1$ in 3D! Let's verify with our basis vectors:

**Case 1: Different states (m ≠ n).** Compute $\langle 0|1\rangle$:

$$\langle 0|1\rangle = \begin{pmatrix} 1 & 0 & 0 & \cdots \end{pmatrix} \begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix} = 1(0) + 0(1) + 0(0) + \cdots = 0$$

They're orthogonal (perpendicular)!

**Case 2: Same state (m = n).** Compute $\langle 1|1\rangle$:

$$\langle 1|1\rangle = \begin{pmatrix} 0 & 1 & 0 & \cdots \end{pmatrix} \begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix} = 0(0) + 1(1) + 0(0) + \cdots = 1$$

The state is normalized (length 1)!

Now we can use this to extract components. To extract $c_1$ from our state:

$$\langle 1|\psi\rangle = \langle 1|\left(\frac{1}{2}|0\rangle + \frac{\sqrt{2}}{2}|1\rangle + \frac{1}{2}|2\rangle\right)$$

$$= \frac{1}{2}\langle 1|0\rangle + \frac{\sqrt{2}}{2}\langle 1|1\rangle + \frac{1}{2}\langle 1|2\rangle$$

$$= \frac{1}{2}(0) + \frac{\sqrt{2}}{2}(1) + \frac{1}{2}(0) = \frac{\sqrt{2}}{2}$$

Perfect! The formula is simply:

$$\boxed{c_n = \langle n|\psi\rangle}$$

The inner product extracts the coefficient c_n, which is a complex number. Don't confuse c_n (the coefficient) with |n⟩ (the basis vector)!

---

## Position Basis: Where Things Get Weird

Now for the continuous case. Position is continuous (the particle can be anywhere), so we need basis vectors for every position.

### Position Eigenstates |x⟩

For each real number x, there's a basis vector $|x\rangle$ representing "particle definitely at position x".

**What does |x⟩ look like in position representation?** It's a delta function centered at x:

$$|x\rangle = \delta(x' - x)$$

where x' is the position variable. Think of |x=2.5⟩ as a spike sitting at position 2.5, zero everywhere else.

These are orthonormal in the continuous sense:

$$\langle x'|x\rangle = \delta(x' - x)$$

The inner product gives a delta function, just like $\langle m|n\rangle = \delta_{mn}$ in the discrete case.

### The Position Wavefunction

Just as $c_n = \langle n|\psi\rangle$ extracts energy coefficients, we extract position coefficients:

$$\boxed{\psi(x) = \langle x|\psi\rangle}$$

This is THE key equation! The wavefunction $\psi(x)$ is the amplitude for the basis vector at position x. You give it a position, it tells you the amplitude there.

(Note: For complex states, $\psi(x) = \langle x|\psi\rangle = \langle\psi|x\rangle^*$, but when ψ is real-valued they're equal.)

### Building States in Position Basis

In energy basis: $|\psi\rangle = \sum_n c_n|n\rangle$
In position basis: $|\psi\rangle = \int \psi(x)|x\rangle dx$

Same pattern! We're adding up basis vectors, weighted by amplitudes. Since position is continuous, we integrate instead of sum.

**Physical picture:** Each $|x\rangle$ is a spike (delta function) at position x. Since $|x\rangle = \delta(x' - x)$, the integral:

$$|\psi\rangle = \int \psi(x)|x\rangle dx = \int \psi(x)\delta(x' - x) dx$$

says "place amplitude $\psi(x)$ worth of spike at each position x, then add them all up." You're building the state from infinitely many delta functions, each weighted by $\psi(x)$.

**Why this works:** The delta function has a sifting property. When you compute $\langle x|\psi\rangle$, you get:

$$\psi(x) = \langle x|\psi\rangle = \int \psi(x') \langle x|x'\rangle dx' = \int \psi(x') \delta(x - x') dx' = \psi(x)$$

The delta function $\delta(x - x')$ "picks out" the value at $x' = x$, extracting exactly $\psi(x)$. This is how the inner product extracts position amplitudes!

---

## Naked ψ vs Ket |ψ⟩: Now It's Clear

The distinction is simple:

**|ψ⟩** = The complete quantum state (basis-independent)
- Contains all measurement possibilities
- Like a vector in 3D space

**ψ(x)** = The position representation
- Gives amplitude at each position: $\psi(x) = \langle x|\psi\rangle$
- Like the x-components of a 3D vector

**$c_0, c_1, c_2, ...$** = The energy representation
- Coefficients for each energy level: $c_n = \langle n|\psi\rangle$
- Like components in a different coordinate system

The pattern is always:
- Energy coefficients: $c_n = \langle n|\psi\rangle$
- Position wavefunction: $\psi(x) = \langle x|\psi\rangle$
- Momentum wavefunction: $\tilde{\psi}(p) = \langle p|\psi\rangle$

The ket |ψ⟩ is the state itself. The functions ψ(x), $\tilde{\psi}(p)$ and coefficients $c_n$ are different ways of describing it.

---

## One State, Three Faces

Let's see how ONE quantum state looks in different representations. We'll use:

$$|\psi\rangle = \frac{1}{2}|0\rangle + \frac{\sqrt{2}}{2}|1\rangle + \frac{1}{2}|2\rangle$$

### Energy Representation

The coefficients:
- $c_0 = 1/2$
- $c_1 = \sqrt{2}/2$
- $c_2 = 1/2$
- $c_n = 0$ for $n \geq 3$

**Probabilities:**
- $P(E_0) = |c_0|^2 = 1/4 = 25\%$
- $P(E_1) = |c_1|^2 = 1/2 = 50\%$
- $P(E_2) = |c_2|^2 = 1/4 = 25\%$

**Average energy:** The weighted average of energy values:
$$\langle E \rangle = P(E_0) \cdot E_0 + P(E_1) \cdot E_1 + P(E_2) \cdot E_2$$
$$= \frac{1}{4}\left(\frac{1}{2}\hbar\omega\right) + \frac{1}{2}\left(\frac{3}{2}\hbar\omega\right) + \frac{1}{4}\left(\frac{5}{2}\hbar\omega\right) = \frac{7}{4}\hbar\omega$$

### Position Representation

The SAME state as a position function:

$$\psi(x) = \frac{1}{2}\psi_0(x) + \frac{\sqrt{2}}{2}\psi_1(x) + \frac{1}{2}\psi_2(x)$$

where $\psi_n(x)$ are the Gaussian energy eigenfunctions.

**Key insight:** Even though we only use 3 energy levels, $\psi(x)$ is non-zero almost everywhere! Each Gaussian spreads over all space, so we need infinitely many position values.

### Momentum Representation

The SAME state in momentum space (via Fourier transform):

$$\tilde{\psi}(p) = \mathcal{F}[\psi(x)] = \frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty} \psi(x) e^{-ipx/\hbar} dx$$

This is another continuous function giving the amplitude for each momentum value p. Since each energy eigenstate has a well-defined momentum distribution, the superposition creates a momentum wavefunction $\tilde{\psi}(p)$ spread over many momentum values.

Same state, now expressed as a function of momentum instead of position!

### The Deep Answer

"How can the same state need 3 numbers in one basis but infinitely many in another?"

Our state only "uses" three energy basis vectors (the rest have $c_n = 0$). But those three energy eigenstates each spread over all positions when expressed as Gaussians. So in position basis, we need $\psi(x)$ defined everywhere.

It's like describing a diagonal line in 2D:
- Rotated basis aligned with line: just one coordinate needed
- Standard xy basis: need both x and y coordinates

Different bases make different aspects simple or complicated!

---

## Time Evolution: Just Rotating Phases

Quantum time evolution is beautifully simple in the energy basis.

### The Rule

Each energy component gets a rotating phase:

$$c_n(t) = c_n(0) \cdot e^{-iE_n t/\hbar}$$

**Where does this come from?** Solving the time-dependent Schrödinger equation $i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle = \hat{H}|\psi(t)\rangle$ in the energy basis. Since energy eigenstates satisfy $\hat{H}|n\rangle = E_n|n\rangle$, each coefficient evolves independently with its own energy-dependent phase.

Higher energy means faster rotation. For our example:

$$|\psi(t)\rangle = \frac{1}{2}|0\rangle e^{-iE_0 t/\hbar} + \frac{\sqrt{2}}{2}|1\rangle e^{-iE_1 t/\hbar} + \frac{1}{2}|2\rangle e^{-iE_2 t/\hbar}$$

### What This Means

The magnitudes $|c_n|$ never change, so energy probabilities are constant. Only relative phases evolve.

In position space, this creates interference:

$$\psi(x,t) = \frac{1}{2}\psi_0(x)e^{-iE_0 t/\hbar} + \frac{\sqrt{2}}{2}\psi_1(x)e^{-iE_1 t/\hbar} + \frac{1}{2}\psi_2(x)e^{-iE_2 t/\hbar}$$

Different frequencies beat against each other, making $|\psi(x,t)|^2$ oscillate. The quantum state "sloshes" in position space while maintaining constant energy probabilities.

**Why energy eigenstates are special:** A pure energy eigenstate $|n\rangle$ just picks up an overall phase. No observable changes at all. These are "stationary states". Only superpositions create dynamics!

---

## Operators: Extracting Observables

Operators are tools that extract physical quantities from quantum states.

### From Waves to Operators

Remember the plane wave $\psi = Ae^{i(px - Et)/\hbar}$ for definite momentum p?

Taking the derivative:
$$\frac{\partial \psi}{\partial x} = \frac{ip}{\hbar}\psi$$

Rearranging:
$$p \psi = -i\hbar\frac{\partial \psi}{\partial x}$$

The differential operator $-i\hbar\frac{\partial}{\partial x}$ extracts momentum! So we define:

$$\hat{p} = -i\hbar\frac{\partial}{\partial x}$$

### Operators in Different Bases

Each operator is simple in its own basis:

**Position operator $\hat{x}$:**
- Position basis: just multiply by x
- Energy basis: complicated matrix mixing levels

**Energy operator $\hat{H}$:**
- Energy basis: diagonal matrix with energies
- Position basis: $-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)$

Choose your basis to make your calculation easy!

### Expectation Values

The average value of any observable A:

$$\langle A \rangle = \langle \psi | \hat{A} | \psi \rangle$$

This formula automatically computes the weighted average over all possible outcomes. Works in ANY basis!

---

## The Complete Parallel Structure

Everything in quantum mechanics follows this parallel pattern:

| **Concept** | **Discrete (Energy)** | **Continuous (Position)** |
|------------|----------------------|--------------------------|
| **State** | $\|\psi\rangle$ | $\|\psi\rangle$ (same!) |
| **Basis vectors** | $\|n\rangle$ for n = 0,1,2,... | $\|x\rangle$ for all real x |
| **Coefficients** | $c_n$ for each level | $\psi(x)$ for each position |
| **Extract component** | $c_n = \langle n\|\psi\rangle$ | $\psi(x) = \langle x\|\psi\rangle$ |
| **Build state** | $\|\psi\rangle = \sum_n c_n\|n\rangle$ | $\|\psi\rangle = \int \psi(x)\|x\rangle dx$ |
| **Orthonormality** | $\langle m\|n\rangle = \delta_{mn}$ | $\langle x'\|x\rangle = \delta(x'-x)$ |
| **Probability** | $P(n) = \|c_n\|^2$ | $P(x)dx = \|\psi(x)\|^2 dx$ |
| **Normalization** | $\sum_n \|c_n\|^2 = 1$ | $\int \|\psi(x)\|^2 dx = 1$ |

Discrete sums become continuous integrals. Everything else is identical!

---

## Schrödinger's Equation: One Rule, Many Forms

The Schrödinger equation tells us how states evolve. The fundamental form is:

$$i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle = \hat{H}|\psi(t)\rangle$$

"The rate of change of the state equals its energy (divided by $i\hbar$)."

### In Different Bases

**Energy basis (simplest):**

$$i\hbar\frac{dc_n(t)}{dt} = E_n c_n(t)$$

Solution: $c_n(t) = c_n(0)e^{-iE_n t/\hbar}$

**Position basis (most familiar):**

$$i\hbar\frac{\partial \psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2} + V(x)\psi$$

Same equation, different coordinates. Choose wisely!

---

## Why Choose Different Bases?

Each basis makes certain questions trivial:

**"What's the probability of energy $E_1$?"**
Energy basis: Just $|c(1)|^2$. One number!

**"What's the probability of finding the particle between x=1 and x=2?"**
Position basis: Just $\int_1^2 |\psi(x)|^2 dx$. One integral!

**"How does the state evolve in time?"**
Energy basis: Each component rotates independently. Simple phases!

Using the wrong basis turns simple questions into horrible calculations. The art is choosing the right tool for the job.

---

## The Bridge to Quantum Computing

When we truncate to finite dimensions (like a 2-level system), everything becomes matrices:

$$|\psi\rangle = \begin{pmatrix} c_0 \\ c_1 \end{pmatrix}, \quad \hat{H} = \begin{pmatrix} E_0 & 0 \\ 0 & E_1 \end{pmatrix}$$

Time evolution: $|\psi(t)\rangle = e^{-i\hat{H}t/\hbar}|\psi(0)\rangle$

This is a qubit! The continuous wavefunctions we've been studying are just the infinite-dimensional version of these simple matrices.

---

## The Punchline

Quantum mechanics seems complicated because we're juggling multiple representations of the same thing. But it all follows one pattern:

1. **States are containers of amplitudes** for all possible measurements
2. **Choose your basis** based on what you want to know
3. **Coefficients are functions** mapping indices to amplitudes
4. **Time evolution** is just rotating phases in energy basis
5. **Measurements extract** one piece of information, collapsing possibilities

The notation is half the battle. Once you see that $\psi(x) = \langle x|\psi\rangle$ is just "the position coefficient function", and that $\sum$ vs $\int$ is just discrete vs continuous, the mystery evaporates.

Next up: Spin-½, where everything is 2×2 matrices and the full power of quantum mechanics fits in four numbers!