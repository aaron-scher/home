# Quantum Mechanics: Basis Representation

**Prerequisites:** This builds on [Quantum Foundations](quantum-foundations.md) where we derived Schrödinger's equation and explored the harmonic oscillator. If you haven't read that yet, start there first!

---

## One Wavefunction, Many Faces: Basis Decomposition

### Recall: Where We Left Off

In Part 1, we solved the time-independent Schrödinger equation for the harmonic oscillator potential $V(x) = \frac{1}{2}m\omega^2 x^2$. We found:

**Energy levels** (evenly spaced):

$$
E_n = \hbar\omega\left(n + \frac{1}{2}\right), \quad n = 0, 1, 2, ...
$$

**Wavefunctions in position space** (Gaussians with increasing nodes):

$$
\psi_0(x) = \left(\frac{1}{\pi x_0^2}\right)^{1/4} e^{-x^2/(2x_0^2)}, \quad \psi_1(x) = \left(\frac{1}{4\pi x_0^2}\right)^{1/4} \frac{2x}{x_0} e^{-x^2/(2x_0^2)}, \quad ...
$$

We also mentioned these have momentum space versions $\tilde{\psi}_n(p)$ (Fourier transforms of $\psi_n(x)$) with the same beautiful Gaussian structure.

But here's a deeper question: **What IS the quantum state?** Is it $\psi(x)$? Is it $\tilde{\psi}(p)$? Or something more fundamental?

The answer transforms how we think about quantum mechanics.

---

### The Abstract State |ψ⟩

The quantum state has an identity **independent of how we describe it**. We write this abstract state as:

$$
|\psi\rangle
$$

This symbol (called a "ket") represents THE quantum state itself — before you choose any particular "coordinate system" to describe it.

**Vector analogy:** Think of an arrow in 3D space. The arrow itself doesn't change if you describe it using:
- Cartesian coordinates $(x, y, z)$ — 3 numbers
- Spherical coordinates $(r, \theta, \phi)$ — 3 numbers
- Any other coordinate system — always 3 numbers!

It's the same arrow — same length, same direction — just different numbers describing it. **Crucially: you always need exactly 3 numbers because the space is 3-dimensional.**

**Similarly in quantum mechanics:**

- $|\psi\rangle$ is THE quantum state (like the arrow itself)
- $\psi(x)$ is how it looks in position coordinates
- $\tilde{\psi}(p)$ is how it looks in momentum coordinates
- $[c_0, c_1, c_2, ...]$ is how it looks in energy coordinates

**But here's where it gets different from 3D:** In quantum mechanics, the "space" (Hilbert space) is **infinite-dimensional**. So you always need infinitely many numbers, but they come in two flavors:
- **Discrete infinite:** A countable list like $[c_0, c_1, c_2, ...]$ (energy basis for harmonic oscillator)
- **Continuous infinite:** A function like $\psi(x)$ — one value for every point on the real line (position/momentum basis)

Both are infinite-dimensional! Position just feels "more infinite" because it's continuous (uncountably infinite), while energy is discrete (countably infinite). But mathematically, both are infinite-dimensional bases for the same infinite-dimensional Hilbert space.

**Why is energy discrete but position continuous?** This depends on the system! For the harmonic oscillator, the boundary conditions (wavefunction must vanish at infinity) force energy to take only certain discrete values $E_n$. But position can be anywhere on the real line — there's no restriction, so the position basis is continuous. If we put the particle in a box, energy would still be discrete, but position would still be continuous (the particle can be at any point inside the box). The mathematical structure of Hilbert space accommodates both types!

**The basis-independent picture:**

$|\psi\rangle$ lives in an abstract mathematical space called **Hilbert space**. Don't let the name scare you — it's just "vector space that might have infinitely many dimensions"! Named after mathematician David Hilbert (1862-1943).

Regular vectors like arrows live in 3D space. Quantum states live in Hilbert space. Same idea, just more dimensions. That's it!

$|\psi\rangle$ contains all the physics: where the particle might be found, what momentum it might have, what energy it has. Everything. The wavefunction $\psi(x)$ is just one way of writing down this information.

**A crucial constraint: |ψ⟩ always has length 1**

Since quantum mechanics is about probabilities, and probabilities must sum to 1, the quantum state $|\psi\rangle$ is always **normalized** — it has length 1.

Think of a unit vector in 3D: $\vec{v} = (v_x, v_y, v_z)$ with $v_x^2 + v_y^2 + v_z^2 = 1$. No matter how you rotate your coordinate system (Cartesian, spherical, etc.), the length stays 1!

**Same in quantum mechanics:** No matter which basis you use to describe $|\psi\rangle$, the "length" is always 1:

- Energy basis: $|c_0|^2 + |c_1|^2 + |c_2|^2 + ... = 1$
- Position basis: $\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1$
- Momentum basis: $\int_{-\infty}^{\infty} |\tilde{\psi}(p)|^2 dp = 1$

This is the **normalization condition** — it ensures the total probability is 100%. The length of the state vector is the same in all bases, just like the length of an arrow doesn't change when you use different coordinates!

---

### Different Representations of the Same State

Let's see how the SAME quantum state $|\psi\rangle$ looks when described in different "coordinate systems."

#### Energy Representation (Discrete Components)

For the harmonic oscillator, any state can be written as a sum over energy eigenstates:

$$
|\psi\rangle = c_0 |0\rangle + c_1 |1\rangle + c_2 |2\rangle + ...
$$

This looks just like a 3D vector decomposition: $\vec{v} = v_x \hat{x} + v_y \hat{y} + v_z \hat{z}$!

**What are $|0\rangle, |1\rangle, |2\rangle$?** These are the **basis vectors** — the energy eigenstates with definite energies $E_0, E_1, E_2, ...$  They're like the unit vectors $\hat{x}, \hat{y}, \hat{z}$ in 3D space, except instead of pointing in spatial directions, they represent states with definite energy.

**What are $c_0, c_1, c_2$?** These are the **components** — complex numbers telling you "how much of each energy" is in your state. Like the components $v_x, v_y, v_z$ of a vector.

We can write this as a column vector:

$$
|\psi\rangle = \begin{pmatrix} c_0 \\ c_1 \\ c_2 \\ \vdots \end{pmatrix}
$$

It's just a discrete list of numbers: $c_0, c_1, c_2, ...$

#### Position Representation (Continuous Components)

The SAME quantum state $|\psi\rangle$ can be described using position "coordinates." But now we need a component for **every position** $x$:

**Component at each position:** $\psi(x)$ — one number for each value of $x$

This is like an "infinite-dimensional vector":

$$
\psi = \begin{pmatrix} \vdots \\ \psi(x_1) \\ \psi(x_2) \\ \psi(x_3) \\ \psi(x_4) \\ \vdots \end{pmatrix} \leftarrow \text{infinitely many entries, one for each } x
$$

Since there are infinitely many positions, we can't write this as a finite list. Instead, we write it as a **function**: $\psi(x)$.

**Functions are vectors with continuous indices!** This is profound: A time signal $f(t)$ IS a vector — it just has a continuous index $t$ instead of discrete entries like [f₁, f₂, f₃, ...].

**How do position and energy representations relate?**

For a state in the energy basis $|\psi\rangle = c_0|0\rangle + c_1|1\rangle + c_2|2\rangle$, the position representation is:

$$
\psi(x) = c_0 \psi_0(x) + c_1 \psi_1(x) + c_2 \psi_2(x)
$$

where $\psi_0(x), \psi_1(x), \psi_2(x)$ are what the energy basis vectors $|0\rangle, |1\rangle, |2\rangle$ look like when expressed as functions of position. (These are the Gaussian solutions from Part 1!)

#### Momentum Representation (Continuous Components)

The SAME $|\psi\rangle$ can also be described using momentum coordinates:

**Component at each momentum:** $\tilde{\psi}(p)$ — one number for each value of $p$

Also an infinite-dimensional vector, written as a function $\tilde{\psi}(p)$.

**How do position and momentum relate?** They're connected by Fourier transform! Different "coordinate systems" for describing the same state.

---

### Quantum "Coordinates" Are Observables

Here's the key insight that makes quantum mechanics different from classical physics.

**Classical vectors:** Components point in **spatial directions**
- A vector $\vec{v} = (v_x, v_y, v_z)$ has components along the x, y, and z axes
- These are fixed directions in physical space

**Quantum states:** Components point in **observable directions**
- Energy basis: each component $c_n$ tells you "how much of energy level $n$"
- Position basis: each value $\psi(x)$ tells you "how much at position $x$"
- Momentum basis: each value $\tilde{\psi}(p)$ tells you "how much with momentum $p$"

**The "coordinate axes" in quantum mechanics are physical observables!** Energy, position, and momentum aren't just numbers — they're the fundamental ways of measuring the quantum state.

#### What is "Hilbert Space"? (Don't Let the Name Scare You!)

Mathematically, quantum states live in an infinite-dimensional **Hilbert space**. This sounds intimidating, but it's really just:

> **"Vector space that might have infinitely many dimensions"**

Named after David Hilbert (1862-1943), a German mathematician who studied the geometry of infinite-dimensional spaces.

Here's the key idea: A regular vector space has finitely many basis vectors (like $\hat{x}, \hat{y}, \hat{z}$ in 3D). But functions need infinitely many "directions" because position $x$ is continuous. A Hilbert space is just a vector space equipped with:
1. An **inner product** (dot product generalized to functions: $\int \psi^*(x)\phi(x) dx$)
2. Possibly **infinite dimensions** (continuous indices)

That's it! Every rule you know about vectors works exactly the same way:
- Add states: $|\psi\rangle + |\phi\rangle$
- Take dot products: we'll introduce this notation next!
- Decompose into bases: $|\psi\rangle = \sum_n c_n |n\rangle$ or $|\psi\rangle = \int \psi(x) |x\rangle dx$

You just use integrals instead of sums when dealing with continuous indices.

The name might sound fancy, but it's almost obvious once you think about it: if 3D vectors need a 3D vector space, then functions (with infinitely many "entries") need an infinite-dimensional vector space. Hilbert space is that space!

#### Summary Table

| Representation | "Index" | "Component" | Written as |
|----------------|---------|-------------|------------|
| **Energy basis** | n (discrete: 0, 1, 2, ...) | $c_n$ = "how much of energy n" | Column vector: $[c_0, c_1, c_2, ...]^T$ |
| **Position basis** | x (continuous: all real numbers) | $\psi(x)$ = "how much at position x" | Function: $\psi(x)$ |
| **Momentum basis** | p (continuous) | $\tilde{\psi}(p)$ = "how much with momentum p" | Function: $\tilde{\psi}(p)$ |

**Same quantum state $|\psi\rangle$, different coordinate systems!**

---

### Extracting Components: The Dot Product

We have $|\psi\rangle$ decomposed in the energy basis:

$$
|\psi\rangle = c_0 |0\rangle + c_1 |1\rangle + c_2 |2\rangle
$$

**Question:** How do we extract the component $c_1$?

**Answer:** Dot product!

#### The 3D Analogy

In 3D space, if you have a vector $\vec{v} = v_x \hat{x} + v_y \hat{y} + v_z \hat{z}$, how do you get the y-component?

Take the dot product with $\hat{y}$:

$$
\vec{v} \cdot \hat{y} = v_x (\hat{x} \cdot \hat{y}) + v_y (\hat{y} \cdot \hat{y}) + v_z (\hat{z} \cdot \hat{y}) = 0 + v_y (1) + 0 = v_y
$$

The dot product **projects** the vector onto the y-axis. Since the basis vectors are orthonormal ($\hat{x} \cdot \hat{y} = 0$, $\hat{y} \cdot \hat{y} = 1$), all the other components drop out.

#### The Quantum Version (Discrete Case)

Same idea! To extract $c_1$ from $|\psi\rangle$, take the dot product with $|1\rangle$:

**"Dot product of $|1\rangle$ with $|\psi\rangle$" = $c_1$**

How does this work mathematically? In the energy basis, $|1\rangle$ is a column vector:

$$
|1\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix}
$$

To compute the dot product, we need a **row vector** (the transpose). For complex vectors, we also take the complex conjugate:

$$
\text{Row vector} = \begin{pmatrix} 0^* & 1^* & 0^* & \cdots \end{pmatrix} = \begin{pmatrix} 0 & 1 & 0 & \cdots \end{pmatrix}
$$

Now multiply: row times column:

$$
\begin{pmatrix} 0 & 1 & 0 & \cdots \end{pmatrix} \begin{pmatrix} c_0 \\ c_1 \\ c_2 \\ \vdots \end{pmatrix} = 0 \cdot c_0 + 1 \cdot c_1 + 0 \cdot c_2 + \cdots = c_1
$$

It picks out exactly what we want! This works because the energy eigenstates are **orthonormal**:

$$
\text{(dot product of } |m\rangle \text{ with } |n\rangle \text{)} = \begin{cases} 1 & \text{if } m = n \\ 0 & \text{if } m \neq n \end{cases}
$$

#### The Continuous Case (Position Basis)

For continuous indices, the dot product becomes an integral:

**Discrete (energy):** $\sum_n (\text{component}_n)^* \times (\text{component}_n)$

**Continuous (position):** $\int (\text{component}_x)^* \times (\text{component}_x) \, dx$

For two wavefunctions $\phi(x)$ and $\psi(x)$, their dot product is:

$$
\text{Dot product} = \int_{-\infty}^{\infty} \phi^*(x) \psi(x) \, dx
$$

The complex conjugate $^*$ plays the same role as taking the transpose in the discrete case.

**Example:** To extract $\psi(x)$ (the amplitude at position $x$) from the abstract state $|\psi\rangle$, you take the "dot product with the position basis vector at $x$."

#### The Projection Picture

The dot product is a **projection** — it tells you "how much of one vector points along another."

- In 3D: $\vec{v} \cdot \hat{x}$ projects $\vec{v}$ onto the x-axis → gives $v_x$
- In quantum (energy basis): "dot product with $|n\rangle$" projects $|\psi\rangle$ onto energy state $n$ → gives $c_n$
- In quantum (position basis): "dot product with position $x$" projects $|\psi\rangle$ onto position $x$ → gives $\psi(x)$

Since you can do this projection for **every** position $x$, you get infinitely many numbers — one for each $x$. That's why $\psi(x)$ is a function: it's the list of all these projection values!

---

### Bra-Ket Notation

Now that we understand dot products, we need clean notation for them. This is where "bra-ket" notation comes in.

#### Introducing the Bra

We've been writing quantum states as $|\psi\rangle$ (a "ket"). To do dot products, we need notation for "the thing that does dot products" — a row vector (complex conjugate transpose).

**The bra:** $\langle \psi |$

It's the complex conjugate transpose of the ket $|\psi\rangle$. Together they make:

$$
\langle \phi | \psi \rangle = \text{bra-ket} = \text{bracket} = \text{inner product} = \text{dot product!}
$$

**Mathematically:**
- $|\psi\rangle$ = ket = column vector = the state itself
- $\langle \psi|$ = bra = row vector (complex conjugate transpose) = "ready to do a dot product"
- $\langle \phi | \psi \rangle$ = inner product = single complex number measuring overlap

#### In Different Bases

**Energy basis (discrete):**

To extract $c_n$:

$$
c_n = \langle n | \psi \rangle
$$

This is matrix multiplication: row [0, 0, ..., 1, ..., 0] times column [$c_0, c_1, ..., c_n, ...$]$^T$ = $c_n$.

General inner product:

$$
\langle \phi | \psi \rangle = \sum_n d_n^* c_n
$$

where $|\phi\rangle = \sum_n d_n |n\rangle$ and $|\psi\rangle = \sum_n c_n |n\rangle$.

**Position basis (continuous):**

To extract $\psi(x)$:

$$
\psi(x) = \langle x | \psi \rangle
$$

This is "dot product with the position basis vector $|x\rangle$" — it extracts the amplitude at position $x$.

General inner product:

$$
\langle \phi | \psi \rangle = \int_{-\infty}^{\infty} \phi^*(x) \psi(x) \, dx
$$

#### Why This Notation?

**Basis-independent formulas!** The expression $\langle n | \psi \rangle$ works in any basis — it just changes between a sum (discrete) and an integral (continuous). You don't have to rewrite formulas when switching representations.

**Clean, compact expressions:** Instead of writing "the dot product of $|1\rangle$ with $|\psi\rangle$" we just write $\langle 1 | \psi \rangle$.

**The notation tells you what to do:** See $\langle \cdot | \cdot \rangle$? Take the dot product!

#### Important Notation Clarification

- **$|n\rangle$** means "the n-th energy eigenstate" (n = 0, 1, 2, ...)
- **$|x\rangle$** would mean "the position eigenstate at position x" (a delta function spike at that location)

Don't confuse energy index $n$ with position value $x$. The context usually makes it clear:
- Energy eigenstates: $|0\rangle, |1\rangle, |2\rangle, ...$
- Position basis vectors: $|x\rangle$ for all $x$

---

### Concrete Example: One State, Three Faces

Let's put it all together with a concrete example.

#### The State

Suppose our quantum state is a superposition of three energy levels of the harmonic oscillator:

$$
|\psi\rangle = c_0 |0\rangle + c_1 |1\rangle + c_2 |2\rangle
$$

where:
- $|0\rangle$ is the ground state with energy $E_0 = \frac{1}{2}\hbar\omega$
- $|1\rangle$ is the first excited state with energy $E_1 = \frac{3}{2}\hbar\omega$
- $|2\rangle$ is the second excited state with energy $E_2 = \frac{5}{2}\hbar\omega$

The coefficients $c_0, c_1, c_2$ are complex numbers (probability amplitudes).

This is **ONE quantum state** $|\psi\rangle$. Now let's see how it looks in different representations.

#### Representation 1: Energy Basis (Discrete - 3 Numbers)

In the energy basis, the state is simple — just a list of coefficients:

$$
|\psi\rangle = \begin{pmatrix} c_0 \\ c_1 \\ c_2 \end{pmatrix}
$$

**Extracting components:** $c_n = \langle n | \psi \rangle$ (dot product with basis vector)

**Probabilities:** The probability of measuring energy $E_n$ is $|c_n|^2$:
- Probability of $E_0$: $|c_0|^2$
- Probability of $E_1$: $|c_1|^2$
- Probability of $E_2$: $|c_2|^2$

**Normalization:** Total probability must equal 1:

$$
|c_0|^2 + |c_1|^2 + |c_2|^2 = 1
$$

This is the "length" of the state vector in the energy basis — it equals 1.

#### Representation 2: Position Basis (Function of x)

The SAME state $|\psi\rangle$ expressed as a function of position:

$$
\psi(x) = c_0 \psi_0(x) + c_1 \psi_1(x) + c_2 \psi_2(x)
$$

where $\psi_0(x), \psi_1(x), \psi_2(x)$ are what the energy eigenstates look like in position space — these are the Gaussian solutions from Part 1!

**Important distinction:** We're still decomposing into **three energy states** ($c_0, c_1, c_2$), but now expressing each energy eigenstate as a function of $x$. This is different from "using the position basis" which would mean $|\psi\rangle = \int \psi(x) |x\rangle dx$ (infinitely many components, one for each $x$).

**Extracting values:** $\psi(x) = \langle x | \psi \rangle$ (projects onto position $x$)

**Probabilities:** $|\psi(x)|^2$ is the probability **density**. The probability of finding the particle between $x = a$ and $x = b$ is:

$$
P(a \leq x \leq b) = \int_a^b |\psi(x)|^2 dx
$$

**Normalization:**

$$
\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1
$$

This is the SAME length-1 constraint, just computed differently — an integral instead of a sum because position is continuous!

#### Representation 3: Momentum Basis (Function of p)

The SAME state $|\psi\rangle$ expressed in momentum space:

$$
\tilde{\psi}(p) = \text{Fourier transform of } \psi(x)
$$

Same state, now telling you the amplitude for each momentum value $p$.

**Important:** All three representations describe the SAME quantum state $|\psi\rangle$ with the SAME length 1:
- Energy: $\sum_n |c_n|^2 = 1$ (discrete sum)
- Position: $\int |\psi(x)|^2 dx = 1$ (continuous integral)
- Momentum: $\int |\tilde{\psi}(p)|^2 dp = 1$ (continuous integral)

The numbers change (different "coordinates"), but the underlying state and its length don't!

#### Wait, This Is Actually Insane

Let's pause and appreciate how bizarre this is!

**In 3D space:** An arrow always needs exactly 3 numbers, no matter what coordinate system you use:
- Cartesian: $(x, y, z)$ — **3 numbers**
- Spherical: $(r, \theta, \phi)$ — **3 numbers**
- Cylindrical: $(r, \theta, z)$ — **3 numbers**

The coordinate system changes how you describe it, but you always need the SAME NUMBER of coordinates because the space is 3-dimensional.

**In quantum mechanics:** The SAME state $|\psi\rangle$ can be described by:
- Energy basis: **3 numbers** $(c_0, c_1, c_2)$ (for this particular example with 3 energy levels)
- Position basis: **infinitely many numbers** $\psi(x)$ — one for every point $x$ on the real line!
- Momentum basis: **infinitely many numbers** $\tilde{\psi}(p)$ — one for every momentum value $p$!

**How can the SAME state be described by 3 numbers in one basis but infinite numbers in another?!**

The resolution: In the energy representation, we're **truncating** to just 3 basis vectors (the first 3 energy levels). The full, complete Hilbert space is actually infinite-dimensional — there are infinitely many energy levels! But if we know our state only has components in the first 3 energy levels (i.e., $c_n = 0$ for all $n \geq 3$), then we only need those 3 numbers.

It's like describing a vector in 3D space that happens to lie in the xy-plane: you could use all 3 coordinates $(x, y, 0)$, or you could just use 2 coordinates $(x, y)$ since you know $z = 0$. The space is still 3D, but this particular vector only needs 2 numbers.

Similarly, our quantum state lives in an infinite-dimensional Hilbert space, but if it only has components in the first 3 energy levels, we can describe it with just 3 numbers in the energy basis. When we switch to position basis, we're forced to use the full infinite-dimensional description because the state doesn't "simplify" in that basis — every position $x$ gets a non-zero amplitude $\psi(x)$.

**This is what makes quantum mechanics so powerful:** Different bases can dramatically simplify (or complicate) the description! The same state that requires infinitely many numbers in position space might only need a handful in energy space, or vice versa.

#### Why Choose Different Bases?

**Here's the profound insight:** You have ONE quantum state $|\psi\rangle$, but different questions naturally lead you to different representations!

- **Question:** "What's the probability the particle is between $x = 1$ and $x = 2$?"
  - **Natural basis:** Position! Use $\psi(x) = c_0\psi_0(x) + c_1\psi_1(x) + c_2\psi_2(x)$
  - **Answer:** $\int_1^2 |\psi(x)|^2 dx$

- **Question:** "What's the probability the particle has energy $E_1$?"
  - **Natural basis:** Energy! Use $|\psi\rangle = c_0|0\rangle + c_1|1\rangle + c_2|2\rangle$
  - **Answer:** $|c_1|^2$

- **Question:** "What's the probability the particle has momentum between $p = p_1$ and $p = p_2$?"
  - **Natural basis:** Momentum! Use $\tilde{\psi}(p)$ (Fourier transform)
  - **Answer:** $\int_{p_1}^{p_2} |\tilde{\psi}(p)|^2 dp$

**Each basis makes certain questions trivial and others complicated!**

#### Time Evolution

Now add time to our superposition. Each energy component picks up a phase factor $e^{-iE_n t/\hbar}$:

$$
|\psi(t)\rangle = c_0 |0\rangle e^{-iE_0 t/\hbar} + c_1 |1\rangle e^{-iE_1 t/\hbar} + c_2 |2\rangle e^{-iE_2 t/\hbar}
$$

**Important:** The coefficients $c_0, c_1, c_2$ themselves are **constants** — they don't change! What changes is the **phase** of each energy component.

Since different energies $E_n$ have different frequencies $\omega_n = E_n/\hbar$, the phases evolve at different rates:
- Ground state: $e^{-i\omega t/2}$ (slowest)
- First excited: $e^{-i3\omega t/2}$ (faster)
- Second excited: $e^{-i5\omega t/2}$ (fastest)

In position space:

$$
\psi(x,t) = c_0 \psi_0(x) e^{-iE_0 t/\hbar} + c_1 \psi_1(x) e^{-iE_1 t/\hbar} + c_2 \psi_2(x) e^{-iE_2 t/\hbar}
$$

The probability density $|\psi(x,t)|^2$ **oscillates in time** — different energy components beat against each other, creating a sloshing pattern.

**Key insight:** The "amount" of each energy (the $|c_n|^2$ probabilities) never changes — energy is conserved! Only the relative phases between energy components evolve.

#### The State "Rotates" in Hilbert Space

Here's a beautiful way to visualize time evolution: The quantum state $|\psi(t)\rangle$ is a vector in infinite-dimensional Hilbert space. As time passes, this vector **rotates**!

In the energy basis, each component $c_n$ picks up a phase $e^{-iE_n t/\hbar}$. Since different energy components rotate at different frequencies, the overall state vector traces out a complicated path through Hilbert space — like a vector in 3D rotating, but in infinitely many dimensions!

For a single energy eigenstate (no superposition), the "rotation" is simple — just one component spinning at frequency $\omega = E/\hbar$. For superpositions, different components beat against each other, creating the oscillating probability densities we observe.

#### Schrödinger's Equation in Different Bases

The usual form of Schrödinger's equation is written in position coordinates:

$$
i\hbar\frac{\partial\psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi(x,t)}{\partial x^2} + V(x)\psi(x,t)
$$

But you can write Schrödinger's equation in **any basis**!

**Energy basis** (super simple!):

$$
i\hbar\frac{dc_n(t)}{dt} = E_n c_n(t)
$$

Solution: $c_n(t) = c_n(0) e^{-iE_n t/\hbar}$ — just a rotating phase!

**Momentum basis**:

$$
i\hbar\frac{\partial\tilde{\psi}(p,t)}{\partial t} = \frac{p^2}{2m}\tilde{\psi}(p,t) + \tilde{V}(p)\tilde{\psi}(p,t)
$$

Kinetic energy is simple (multiply by $p^2/2m$), potential energy is complicated (convolution in momentum space) — opposite of position space!

**Basis-independent form** (the most fundamental!):

$$
i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle = \hat{H}|\psi(t)\rangle
$$

This is the "true" Schrödinger equation. It doesn't care what basis you use! The abstract quantum state $|\psi(t)\rangle$ is more fundamental than any particular representation $\psi(x,t)$ or $c_n(t)$.

---

### Understanding Operators

So far we've talked about states and how to represent them. Now let's talk about how we extract observable quantities from states. Enter: **operators**.

#### Where Do Operators Come From?

Before diving into the formalism, let's connect back to Part 1 and see how operators arise naturally from wave mechanics.

Remember the de Broglie plane wave from Part 1? A particle with definite momentum $p$ and energy $E$ is described by:

$$
\psi(x,t) = A e^{i(kx - \omega t)} = A e^{i(px/\hbar - Et/\hbar)}
$$

using de Broglie's relations $p = \hbar k$ and $E = \hbar\omega$.

**Now watch what happens when we take derivatives:**

Take $\frac{\partial}{\partial x}$ of this wave:

$$
\frac{\partial\psi}{\partial x} = A \cdot i\frac{p}{\hbar} \cdot e^{i(px/\hbar - Et/\hbar)} = \frac{ip}{\hbar}\psi
$$

Rearrange: $-i\hbar\frac{\partial\psi}{\partial x} = p\psi$

**The derivative operator $-i\hbar\frac{\partial}{\partial x}$ extracts the momentum!** It's the natural mathematical object that "reaches into" the wave and pulls out the momentum value.

Similarly for energy:

$$
\frac{\partial\psi}{\partial t} = A \cdot \left(-i\frac{E}{\hbar}\right) \cdot e^{i(px/\hbar - Et/\hbar)} = -\frac{iE}{\hbar}\psi
$$

Rearrange: $i\hbar\frac{\partial\psi}{\partial t} = E\psi$

**The time derivative operator $i\hbar\frac{\partial}{\partial t}$ extracts the energy!** This is exactly the time-dependent Schrödinger equation — it's saying "energy operator acting on the state equals the energy value times the state."

**This is how operators are born:** They're the mathematical tools that extract observable values from waves. For plane waves with definite $p$ and $E$, the derivatives give you back the values. For superpositions (like wavepackets), the operators give you something more interesting — they help you compute average values, which is what we'll explore next.

#### What Are Operators?

More generally, operators are mathematical objects that extract physical observables from quantum states. Each measurable quantity has an associated operator:

- $\hat{H}$ = Hamiltonian (energy operator)
- $\hat{x}$ = position operator
- $\hat{p}$ = momentum operator
- $\hat{L}$ = angular momentum operator
- etc.

Operators are written with hats: $\hat{A}$. They **act on states** to produce new states or numbers.

#### Eigenvalue Equations

The most important property of operators is their **eigenvalue equation**. For the energy operator (Hamiltonian):

$$
\hat{H}|n\rangle = E_n|n\rangle
$$

This says: "When the energy operator acts on energy eigenstate $|n\rangle$, it returns the energy value $E_n$ times that state."

This is what we've been solving all along! The time-independent Schrödinger equation $\hat{H}\psi = E\psi$ is an eigenvalue equation. We're finding:
- **Eigenstates:** special states $|n\rangle$ (or $\psi_n(x)$ in position representation)
- **Eigenvalues:** energy values $E_n$

**Why are eigenstates special?**

1. **They're the natural "coordinate axes"** for that observable
2. **They're orthogonal:** $\langle m|n\rangle = \delta_{mn}$ (0 if $m \neq n$, 1 if $m = n$)
3. **They're complete:** any state can be decomposed into them: $|\psi\rangle = \sum_n c_n |n\rangle$
4. **They make probabilities simple:** $|c_n|^2$ are independent probabilities that add like classical probabilities

When you measure an observable, you're asking "which eigenstate am I in?" The coefficients $c_n$ in the decomposition $|\psi\rangle = \sum_n c_n |n\rangle$ give you the probability amplitudes. Because of orthogonality, these probabilities don't interfere — they just add.

#### Expectation Values: Building Up from Classical

Suppose you measure energy many times on identical copies of the state $|\psi\rangle$. What's the **average** energy you'll measure?

**Classical analogy:** If you roll a weighted die with probabilities $P_1, P_2, ..., P_6$ for each face, the average value is:

$$
\langle \text{value} \rangle = 1 \cdot P_1 + 2 \cdot P_2 + \cdots + 6 \cdot P_6 = \sum_{n=1}^{6} n \cdot P_n
$$

It's a **weighted average**: each outcome times its probability.

**Quantum case:** For the state $|\psi\rangle = \sum_n c_n |n\rangle$, the probability of measuring energy $E_n$ is $|c_n|^2$. By analogy:

$$
\langle E \rangle = E_0 |c_0|^2 + E_1 |c_1|^2 + E_2 |c_2|^2 + \cdots = \sum_n E_n |c_n|^2
$$

Each energy value $E_n$ weighted by its probability $|c_n|^2$.

#### The Quantum Formula: ⟨ψ|Â|ψ⟩

Instead of writing out the weighted sum manually, quantum mechanics gives us a compact formula:

> **Expectation value of observable $A$:**
> $$\langle A \rangle = \langle \psi | \hat{A} | \psi \rangle$$

This is actually a **postulate** of quantum mechanics. It works for *any* observable — energy, position, momentum, anything. Let's verify it gives the right answer for energy.

#### Derivation: Why It Works

Start with the state in the energy basis:

$$
|\psi\rangle = \sum_n c_n |n\rangle
$$

**Step 1:** Apply the Hamiltonian. Use the eigenvalue equation $\hat{H}|n\rangle = E_n|n\rangle$:

$$
\hat{H}|\psi\rangle = \hat{H}\left(\sum_n c_n |n\rangle\right) = \sum_n c_n \hat{H}|n\rangle = \sum_n c_n E_n |n\rangle
$$

**Step 2:** Take the inner product with $\langle\psi| = \sum_m c_m^* \langle m|$:

$$
\langle \psi | \hat{H} | \psi \rangle = \left(\sum_m c_m^* \langle m|\right) \left(\sum_n c_n E_n |n\rangle\right) = \sum_{m,n} c_m^* c_n E_n \langle m|n\rangle
$$

**Step 3:** Use orthonormality: $\langle m|n\rangle = \delta_{mn}$ (equals 1 if $m=n$, 0 otherwise). This kills all terms except when $m=n$:

$$
\langle E \rangle = \sum_n c_n^* c_n E_n = \sum_n |c_n|^2 E_n
$$

**Exactly what we wanted!** Each term $|c_n|^2 E_n$ is "probability of state n" times "energy of state n."

**Physical interpretation:** The sandwich $\langle \psi | \hat{H} | \psi \rangle$ automatically:
1. Decomposes the state into eigenstates
2. Weights each eigenvalue by its probability
3. Sums them up

The magic is that this formula works in **any basis**, not just energy!

#### What Is the Hamiltonian?

The Hamiltonian $\hat{H}$ is the **energy operator**. It's the quantum version of total energy (kinetic + potential):

$$
\hat{H} = \underbrace{-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}}_{\text{kinetic energy}} + \underbrace{V(x)}_{\text{potential energy}}
$$

This is a differential operator — it takes derivatives of the wavefunction.

**Two roles of the Hamiltonian:**

1. **Eigenvalue equation** (time-independent): $\hat{H}|n\rangle = E_n|n\rangle$ finds energy eigenstates
2. **Time evolution** (time-dependent): $i\hbar \frac{\partial}{\partial t}|\psi\rangle = \hat{H}|\psi\rangle$ determines how states evolve

The Schrödinger equation says: "The rate of change of the state is determined by its energy." That's why states with higher energy oscillate faster in time!

#### Operators in Different Bases

Here's the key insight: **operators are easy in their own eigenbasis, hard in others**.

**Energy basis:**
- $\hat{H}$ is **trivial** — just a diagonal matrix:

$$
\hat{H} = \begin{pmatrix} E_0 & 0 & 0 & \cdots \\ 0 & E_1 & 0 & \cdots \\ 0 & 0 & E_2 & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}
$$

- $\hat{x}$ (position) is **complicated** — off-diagonal matrix that mixes energy states
- To find $\langle x \rangle$, you need matrix elements $\langle m|\hat{x}|n\rangle$ (measures overlap in position space)

**Position basis:**
- $\hat{x}$ is **trivial** — just multiply by $x$: $\hat{x}\psi(x) = x\psi(x)$
- $\hat{H}$ is **complicated** — differential operator: $\hat{H}\psi(x) = -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi(x)$
- $\hat{p}$ (momentum) is also a differential operator: $\hat{p} = -i\hbar \frac{\partial}{\partial x}$

#### The Parallel Structure

Notice the beautiful symmetry:

| Concept | Energy Basis (Discrete) | Position Basis (Continuous) |
|---------|-------------------------|----------------------------|
| **State components** | $c_n = \langle n\|\psi\rangle$ (numbers) | $\psi(x) = \langle x\|\psi\rangle$ (function) |
| **Combine components** | $\sum_n$ (discrete sum) | $\int dx$ (continuous sum) |
| **Probability** | $\|c_n\|^2$ | $\|\psi(x)\|^2$ (density) |
| **Normalization** | $\sum_n \|c_n\|^2 = 1$ | $\int \|\psi(x)\|^2 dx = 1$ |
| **Easy operator** | $\hat{H}$ (diagonal matrix) | $\hat{x}$ (multiply by x) |
| **Hard operator** | $\hat{x}$ (off-diagonal matrix) | $\hat{H}$ (differential) |
| **Inner product** | $\langle\psi\|\phi\rangle = \sum_n c_n^* d_n$ | $\langle\psi\|\phi\rangle = \int \psi^*(x)\phi(x) dx$ |

**Key insight:** Discrete sums become integrals, but the structure is **identical**. Energy basis is finite-dimensional linear algebra; position basis is infinite-dimensional, but the same rules apply!

---

### Working with States: Examples

Let's see how to actually compute things in different bases.

#### Example 1: Energy Basis Calculations

Take the state $|\psi\rangle = c_0|0\rangle + c_1|1\rangle + c_2|2\rangle$ with $c_0 = \frac{1}{2}, c_1 = \frac{\sqrt{2}}{2}, c_2 = \frac{1}{2}$.

**Check normalization:**

$$
|c_0|^2 + |c_1|^2 + |c_2|^2 = \frac{1}{4} + \frac{1}{2} + \frac{1}{4} = 1 \quad \checkmark
$$

**Probabilities of each energy:**
- $P(E_0) = |c_0|^2 = 1/4 = 25\%$
- $P(E_1) = |c_1|^2 = 1/2 = 50\%$
- $P(E_2) = |c_2|^2 = 1/4 = 25\%$

**Average energy:**

$$
\langle E \rangle = E_0|c_0|^2 + E_1|c_1|^2 + E_2|c_2|^2 = \frac{1}{2}\hbar\omega \cdot \frac{1}{4} + \frac{3}{2}\hbar\omega \cdot \frac{1}{2} + \frac{5}{2}\hbar\omega \cdot \frac{1}{4} = \frac{7}{4}\hbar\omega
$$

In the energy basis, everything is easy!

#### Example 2: Position Basis Calculations

For a single energy eigenstate $|n=1\rangle$ (first excited state):

$$
\psi_1(x) = \left(\frac{1}{4\pi x_0^2}\right)^{1/4} \frac{2x}{x_0} e^{-x^2/(2x_0^2)}
$$

**Average position:**

$$
\langle x \rangle = \int_{-\infty}^{\infty} x |\psi_1(x)|^2 dx = 0
$$

(by symmetry — antisymmetric state)

**Average momentum:**

$$
\langle p \rangle = \int_{-\infty}^{\infty} \psi_1^*(x) \left(-i\hbar \frac{\partial}{\partial x}\right) \psi_1(x) dx = 0
$$

(again by symmetry)

**Average energy:**

$$
\langle E \rangle = \int_{-\infty}^{\infty} \psi_1^*(x) \hat{H} \psi_1(x) dx = E_1 = \frac{3}{2}\hbar\omega
$$

Since $\psi_1(x)$ is an energy eigenstate, the average energy is just $E_1$. But notice: calculating $\hat{H}\psi_1(x)$ requires taking second derivatives — much harder than the energy basis!

---

### The Bridge to Matrix Mechanics

In a finite-dimensional space (like spin-½, or truncating to the first N energy levels), everything becomes concrete linear algebra.

**States → column vectors:**

$$
|\psi\rangle = \begin{pmatrix} c_0 \\ c_1 \\ c_2 \\ \vdots \end{pmatrix}
$$

**Operators → matrices.** The Hamiltonian in the energy basis:

$$
\hat{H} = \begin{pmatrix} E_0 & 0 & 0 & \cdots \\ 0 & E_1 & 0 & \cdots \\ 0 & 0 & E_2 & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}
$$

**Eigenvalue equation:** $\hat{H}|\psi\rangle = E|\psi\rangle$ becomes $H\mathbf{c} = E\mathbf{c}$ (standard matrix eigenvalue problem you've seen in linear algebra)

**Time evolution:** The Schrödinger equation becomes a matrix exponential:

$$
|\psi(t)\rangle = e^{-i\hat{H}t/\hbar}|\psi(0)\rangle
$$

For a diagonal $\hat{H}$ in the energy basis, this just rotates each component:

$$
c_n(t) = e^{-iE_n t/\hbar} c_n(0)
$$

**The punchline:** The continuous wavefunctions $\psi(x)$ we've been working with are the **infinite-dimensional limit** of this finite-dimensional picture. Same mathematical structure — eigenstates, operators, inner products, time evolution — just with integrals instead of sums!

This is why quantum mechanics is sometimes called "wave mechanics" (Schrödinger's approach with wavefunctions) or "matrix mechanics" (Heisenberg's approach with matrices). They're the same theory, just viewed through different lenses.

---

*Next up: We'll explore the simplest quantum system — spin-½ — where everything is 2×2 matrices, and all of quantum mechanics fits in a tiny box. This is the foundation of qubits and quantum computing.*
