# Quantum Mechanics: Basis Representation

**Prerequisites:** This builds on [Quantum Foundations](quantum-foundations.md) where we derived Schrödinger's equation and explored the harmonic oscillator. If you haven't read that yet, start there first!

---

## One Wavefunction, Many Faces

In Part 1, we solved the harmonic oscillator and found energy eigenstates $\psi_n(x)$ — Gaussians with increasing nodes, each with energy $E_n = \hbar\omega(n + \frac{1}{2})$. We mentioned these have momentum space versions $\tilde{\psi}_n(p)$ via Fourier transform.

But here's the deeper question: **What IS the quantum state?** Is it $\psi(x)$? Is it $\tilde{\psi}(p)$? Or something more fundamental?

---

## The Abstract State |ψ⟩

The quantum state has an identity **independent of how we describe it**. We write this abstract state as $|\psi\rangle$ (called a "ket"). It represents THE quantum state itself — before you choose any particular "coordinate system."

**Vector analogy:** An arrow in 3D space doesn't change if you describe it using Cartesian coordinates $(x, y, z)$ or spherical coordinates $(r, \theta, \phi)$. It's the same arrow — same length, same direction — just different numbers. Crucially, you always need exactly 3 numbers because the space is 3-dimensional.

**Similarly in quantum mechanics:**
- $|\psi\rangle$ is THE quantum state (the arrow itself) — **basis-independent**
- $\psi(x)$ is how it looks in position coordinates — **a function of x**
- $\tilde{\psi}(p)$ is how it looks in momentum coordinates — **a function of p**
- $[c_0, c_1, c_2, ...]$ is how it looks in energy coordinates — **a list of numbers**

---

## CRITICAL: Naked ψ vs Ket |ψ⟩ — What's the Difference?

This is THE most confusing notation issue in quantum mechanics. Let's nail it down.

### The Short Answer

**$|\psi\rangle$** = The abstract quantum state itself (lives in Hilbert space, no coordinates)

**$\psi(x)$** = The position-space wavefunction (a function, gives amplitude at each position x)

**Relationship:** $\psi(x) = \langle x | \psi \rangle$ ("extract the x-component of the abstract state")

### The Long Answer: What Does This Actually Mean?

Think back to 3D vectors. If $\vec{v}$ is a vector:
- $\vec{v}$ = the abstract vector itself
- $v_x, v_y, v_z$ = its components in Cartesian coordinates
- We extract components via dot product: $v_y = \hat{y} \cdot \vec{v}$

**Quantum mechanics works identically:**

| Concept | 3D Vector | Quantum State (Energy Basis) | Quantum State (Position Basis) |
|---------|-----------|------------------------------|--------------------------------|
| **Abstract object** | $\vec{v}$ | $\|\psi\rangle$ | $\|\psi\rangle$ (same state!) |
| **Basis vectors** | $\hat{x}, \hat{y}, \hat{z}$ | $\|0\rangle, \|1\rangle, \|2\rangle, ...$ | $\|x\rangle$ for each position $x$ |
| **Components** | $v_x, v_y, v_z$ | $c_0, c_1, c_2, ...$ | $\psi(x)$ for each $x$ |
| **Extract component** | $v_y = \hat{y} \cdot \vec{v}$ | $c_n = \langle n \| \psi \rangle$ | $\psi(x) = \langle x \| \psi \rangle$ |
| **Reconstruct state** | $\vec{v} = v_x\hat{x} + v_y\hat{y} + v_z\hat{z}$ | $\|\psi\rangle = \sum_n c_n \|n\rangle$ | $\|\psi\rangle = \int \psi(x)\|x\rangle dx$ |

### Key Insight: Discrete vs Continuous

**Energy basis (discrete):**
* Basis vectors: $|0\rangle, |1\rangle, |2\rangle, ...$ (countable list)
* Components: $c_0, c_1, c_2, ...$ (list of numbers)
* Extract: $c_n = \langle n | \psi \rangle$ (a number for each n)
* Reconstruct: $|\psi\rangle = \sum_{n=0}^{\infty} c_n |n\rangle$ (sum over discrete index)

**Position basis (continuous):**
* Basis vectors: $|x\rangle$ for every real number $x$ (uncountable!)
* Components: $\psi(x)$ for every $x$ (a function, not a list!)
* Extract: $\psi(x) = \langle x | \psi \rangle$ (a number for each x)
* Reconstruct: $|\psi\rangle = \int_{-\infty}^{\infty} \psi(x) |x\rangle \, dx$ (integral over continuous index)

**The parallel structure:**

$$
\text{Discrete: } |\psi\rangle = \sum_n c_n |n\rangle \quad \leftrightarrow \quad \text{Continuous: } |\psi\rangle = \int \psi(x) |x\rangle \, dx
$$

The sum $\sum$ becomes integral $\int$, and the discrete index $n$ becomes continuous variable $x$. That's it!

### What Does Σc_n|n⟩ Actually Mean? A Step-by-Step Example

Let's demystify this notation by **writing it out completely** with concrete numbers.

**The compact notation:**
$$
|\psi\rangle = \sum_{n=0}^{\infty} c_n |n\rangle
$$

**What this actually means — written out in full:**

$$
|\psi\rangle = c_0 |0\rangle + c_1 |1\rangle + c_2 |2\rangle + c_3 |3\rangle + c_4 |4\rangle + ...
$$

It's just **adding up** a bunch of vectors! Each term is:
* **$|n\rangle$** = a basis vector (the n-th energy eigenstate)
* **$c_n$** = a number (complex, in general) that scales that basis vector
* **$c_n |n\rangle$** = that basis vector scaled by the coefficient

You're adding up infinitely many scaled basis vectors to build $|\psi\rangle$.

**Concrete example with actual numbers:**

Suppose we have:
* $c_0 = \frac{1}{2}$
* $c_1 = \frac{\sqrt{2}}{2}$
* $c_2 = \frac{1}{2}$
* $c_n = 0$ for all $n \geq 3$

Then:

$$
|\psi\rangle = \frac{1}{2}|0\rangle + \frac{\sqrt{2}}{2}|1\rangle + \frac{1}{2}|2\rangle + 0|3\rangle + 0|4\rangle + ...
$$

The terms with $c_n = 0$ vanish, so:

$$
|\psi\rangle = \frac{1}{2}|0\rangle + \frac{\sqrt{2}}{2}|1\rangle + \frac{1}{2}|2\rangle
$$

**This is just vector addition!** Like in 3D where $\vec{v} = 2\hat{x} + 3\hat{y} - 1\hat{z}$ means "2 units in the x-direction, plus 3 units in the y-direction, minus 1 unit in the z-direction."

**In column vector form:**

If we write basis states as column vectors (with 1 in the n-th position):

$$
|0\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ \vdots \end{pmatrix}, \quad
|1\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ \vdots \end{pmatrix}, \quad
|2\rangle = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix}, \quad \text{etc.}
$$

Then our state becomes:

$$
|\psi\rangle = \frac{1}{2}\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ \vdots \end{pmatrix} + \frac{\sqrt{2}}{2}\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ \vdots \end{pmatrix} + \frac{1}{2}\begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix} = \begin{pmatrix} 1/2 \\ \sqrt{2}/2 \\ 1/2 \\ 0 \\ \vdots \end{pmatrix}
$$

**That's it!** The coefficients $c_0, c_1, c_2, ...$ are just the entries in the column vector. The sum $\sum c_n |n\rangle$ is assembling this column vector by adding scaled basis vectors.

**The sum notation $\sum_{n=0}^{\infty}$ just means:**
* Start with $n = 0$: add $c_0|0\rangle$
* Then $n = 1$: add $c_1|1\rangle$
* Then $n = 2$: add $c_2|2\rangle$
* Keep going forever: $n = 3, 4, 5, ...$

It's shorthand for "add up all these terms."

### Now The Continuous Case: ∫ψ(x)|x⟩dx

Now let's do the **continuous analog**. The key difference: we can't write a list like $[c_0, c_1, c_2, ...]$ because there are uncountably many positions!

**What is the continuous "basis vector" |x⟩?**

The position eigenstate $|x\rangle$ is an abstract basis vector indexed by $x$. In position representation, it looks like a delta function:

$$
\langle x' | x \rangle = \delta(x' - x) \quad \text{(amplitude at position } x' \text{)}
$$

This is the continuous analog of the discrete basis vector $|n\rangle$. It's zero everywhere except at position $x$, where it has an infinite spike.

**The compact notation:**
$$
|\psi\rangle = \int_{-\infty}^{\infty} \psi(x) |x\rangle \, dx
$$

This is the continuous version of $\sum_n c_n |n\rangle$! Let's break it down.

**Discrete approximation to make it concrete:**

Imagine we divide space into tiny bins of width $dx$. At each position $x_i$, we have:
* A coefficient: $\psi(x_i)$ (the amplitude at that position)
* A basis vector: $|x_i\rangle$ (the position eigenstate at $x_i$)

The discrete approximation is:

$$
|\psi\rangle \approx \psi(x_0)|x_0\rangle \cdot dx + \psi(x_1)|x_1\rangle \cdot dx + \psi(x_2)|x_2\rangle \cdot dx + ...
$$

Or more compactly:

$$
|\psi\rangle \approx \sum_{\text{all bins}} \psi(x_i) |x_i\rangle \cdot dx
$$

Each term $\psi(x_i)|x_i\rangle \cdot dx$ contributes a weighted basis vector at position $x_i$.

**With concrete numbers (dx = 0.1):**

$$
|\psi\rangle \approx \psi(-0.2)|x=-0.2\rangle \cdot 0.1 + \psi(-0.1)|x=-0.1\rangle \cdot 0.1 + \psi(0.0)|x=0.0\rangle \cdot 0.1 + ...
$$

As $dx \to 0$, this sum becomes the integral:

$$
|\psi\rangle = \int_{-\infty}^{\infty} \psi(x) |x\rangle \, dx
$$

**Key insight:** You can't write "sum over all x" as a literal list because there are too many x values (uncountable). But you CAN write it as an integral, which is the continuous version of a sum. The thing you're adding up at each point is $\psi(x)|x\rangle$, where $|x\rangle$ is the basis vector at that position.

**Concrete example with a Gaussian wavefunction:**

Suppose $\psi(x) = e^{-x^2/2}$ (unnormalized Gaussian). Then:

$$
|\psi\rangle = \int_{-\infty}^{\infty} e^{-x^2/2} |x\rangle \, dx
$$

Written out with specific positions (discrete approximation):
* At $x = 0$: add $1.00 \cdot |x=0\rangle \cdot dx$ (largest contribution)
* At $x = 1$: add $0.61 \cdot |x=1\rangle \cdot dx$
* At $x = 2$: add $0.14 \cdot |x=2\rangle \cdot dx$
* At $x = 3$: add $0.01 \cdot |x=3\rangle \cdot dx$ (small contribution)
* etc. for all $x$ from $-\infty$ to $+\infty$

Each term is a **weighted basis vector** at that position. The Gaussian $e^{-x^2/2}$ weights how much each position contributes. Positions near $x = 0$ get large weights, positions far away get small weights.

**The integral adds up all these weighted basis vectors** to build the final state $|\psi\rangle$.

### Side-by-Side Comparison

| | **Discrete (Energy)** | **Continuous (Position)** |
|---|---|---|
| **Compact notation** | $\|\psi\rangle = \sum_n c_n \|n\rangle$ | $\|\psi\rangle = \int \psi(x) \|x\rangle dx$ |
| **What it means** | Add up scaled basis vectors | Add up scaled basis vectors (delta functions) |
| **Basis vectors** | $\|0\rangle, \|1\rangle, \|2\rangle, ...$ (discrete) | $\|x\rangle = \delta(x'-x)$ (delta spike at $x$) |
| **Coefficients** | $c_0, c_1, c_2, ...$ (list) | $\psi(x)$ (function) |
| **How to add** | Regular sum: $\sum$ | Integral: $\int dx$ (continuous sum) |
| **Fully expanded** | $c_0\|0\rangle + c_1\|1\rangle + c_2\|2\rangle + ...$ | $\int \psi(x) \delta(x'-x) dx$ |
| **Example term** | $\frac{1}{2}\|0\rangle$ = "half of basis vector 0" | $\psi(1.5) \delta(x'-1.5) \cdot dx$ = "weighted delta at x=1.5" |
| **Can write as list?** | Yes: $[c_0, c_1, c_2, ...]$ | No: uncountably many points! |

Both are doing the **same thing**: building a state by adding up basis vectors, each scaled by its coefficient.

**Key difference:** Discrete case has countable basis vectors, so we can write a list. Continuous case has uncountable basis vectors (one delta function for each real number $x$), so we need an integral!

### The Delta Function: How Continuous Bases Work

**What is the continuous basis vector |x⟩?**

The position eigenstate $|x\rangle$ is an abstract basis vector indexed by position $x$. In position representation, it looks like a delta function:

$$
\langle x' | x \rangle = \delta(x' - x)
$$

This says: "The amplitude to find |x⟩ at position x' is a delta spike at x." This is the continuous analog of the Kronecker delta $\delta_{mn}$ for discrete bases.

---

#### Part 1: Building States (Construction)

When you write $\int \psi(x) |x\rangle \, dx$, you're **building** the abstract state $|\psi\rangle$:

$$
|\psi\rangle = \int_{-\infty}^{\infty} \psi(x) |x\rangle \, dx
$$

**Discrete approximation:** Divide space into bins of width $dx$:

$$
|\psi\rangle \approx \psi(x_0)|x_0\rangle \cdot dx + \psi(x_1)|x_1\rangle \cdot dx + \psi(x_2)|x_2\rangle \cdot dx + ...
$$

* Each term is a basis vector $|x_i\rangle$ at position $x_i$
* Weighted by amplitude $\psi(x_i)$
* Scaled by bin width $dx$

As $dx \to 0$, we get the integral. We're adding up infinitely many weighted basis vectors to build $|\psi\rangle$!

**This is like Riemann sums**, but instead of adding numbers, we add functions (delta spikes).

---

#### Part 2: Extracting Components (Projection)

The delta function has a **sifting property** — when you integrate it against any function, it "picks out" one value:

$$
\int_{-\infty}^{\infty} f(x') \delta(x' - x) \, dx' = f(x)
$$

**How ⟨x|ψ⟩ extracts ψ(x):** Start with $|\psi\rangle = \int \psi(x') |x'\rangle dx'$ and project onto $\langle x|$:

$$
\psi(x) = \langle x | \psi \rangle = \int_{-\infty}^{\infty} \psi(x') \langle x | x' \rangle \, dx' = \int_{-\infty}^{\infty} \psi(x') \delta(x - x') \, dx' = \psi(x) \quad \checkmark
$$

The delta function sifts out the value at $x$! **This is how the dot product "picks out" the wavefunction value at position x.**

---

#### Discrete vs Continuous: The Perfect Parallel

| | **Discrete (Energy)** | **Continuous (Position)** |
|---|---|---|
| **Orthonormality** | $\langle m \| n \rangle = \delta_{mn}$ | $\langle x' \| x \rangle = \delta(x' - x)$ |
| **What it means** | Different basis states are orthogonal | Different positions are orthogonal |
| **"Sifting"** | $\sum_n c_n \delta_{mn} = c_m$ | $\int \psi(x) \delta(x'-x) dx = \psi(x')$ |
| **Build state** | $\|\psi\rangle = \sum_n c_n \|n\rangle$ | $\|\psi\rangle = \int \psi(x) \|x\rangle dx$ |
| **Extract component** | $c_m = \sum_n \langle m\|n\rangle c_n$ | $\psi(x') = \int \langle x'\|x\rangle \psi(x) dx$ |

In discrete case: $\delta_{mn}$ kills all terms except $m=n$. In continuous case: $\delta(x'-x)$ kills all positions except $x=x'$. Same mechanism!

**Physical intuition:** $|x\rangle$ represents a particle **perfectly localized** at position $x$ — zero probability everywhere else, infinite spike at $x$. When you dot this with $|\psi\rangle$, you're asking "how much of $|\psi\rangle$ overlaps with being exactly at position $x$?" The answer is $\psi(x)$.

Position eigenstates aren't physically realizable (can't have infinite position certainty), but they're perfect mathematical basis vectors — just like plane waves $e^{ipx/\hbar}$ (perfect momentum basis, but unphysical).

### What About Schrödinger's Equation?

When we write the **time-independent** Schrödinger equation as:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi
$$

We're actually writing it in **position representation**. The fully abstract version is:

$$
\hat{H}|\psi\rangle = E|\psi\rangle
$$

To get the position-space equation, we "project" both sides onto position basis by acting with $\langle x|$:

$$
\langle x|\hat{H}|\psi\rangle = E\langle x|\psi\rangle
$$

The right side becomes $E\psi(x)$. The left side becomes the differential equation:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} + V(x)\psi(x) = E\psi(x)
$$

So when we write "$\psi$" in Schrödinger's equation, we really mean **$\psi(x) = \langle x|\psi\rangle$**, the position-space wavefunction!

### Summary Table: What Does Each Symbol Mean?

| Symbol | Meaning | Type | Example |
|--------|---------|------|---------|
| $\|\psi\rangle$ | Abstract quantum state | Vector in Hilbert space | (basis-independent) |
| $\psi(x)$ | Position wavefunction | Function of $x$ | $\psi(x) = e^{-x^2/2}$ |
| $\tilde{\psi}(p)$ | Momentum wavefunction | Function of $p$ | Fourier transform of $\psi(x)$ |
| $c_n$ | Energy coefficients | List of numbers | $c_0 = 0.5, c_1 = 0.7, ...$ |
| $\langle x \| \psi\rangle$ | Extract position component | Equals $\psi(x)$ | Dot product in continuous basis |
| $\langle n \| \psi\rangle$ | Extract energy component | Equals $c_n$ | Dot product in discrete basis |
| $\|x\rangle$ | Position eigenstate | Delta function at $x$ | Basis vector (continuous) |
| $\|n\rangle$ | Energy eigenstate | The $n$-th eigenfunction | Basis vector (discrete) |

**The golden rule:**
* **Ket $|\psi\rangle$** is abstract, basis-independent
* **Naked $\psi$** (like in $\psi(x)$) is a representation — components in some basis
* They're related by: **$\psi(x) = \langle x|\psi\rangle$** or **$c_n = \langle n|\psi\rangle$**

**The key difference:** Quantum states live in an **infinite-dimensional space** (called Hilbert space). You always need infinitely many numbers, but they come in two flavors:
* **Discrete infinite:** A countable list like $[c_0, c_1, c_2, ...]$ (energy basis for harmonic oscillator)
* **Continuous infinite:** A function like $\psi(x)$ — one value for every point $x$ (position/momentum basis)

Both are infinite-dimensional! Position feels "more infinite" because it's continuous (uncountably infinite), while energy is discrete (countably infinite). But mathematically, both describe the same infinite-dimensional state.

**Why is energy discrete but position continuous?** For the harmonic oscillator, boundary conditions (wavefunction vanishes at infinity) force energy to take discrete values $E_n$. But position can be anywhere on the real line — no restriction, so the position basis is continuous.

**Normalization:** Since quantum mechanics is about probabilities (which sum to 1), the state $|\psi\rangle$ always has length 1:
* Energy basis: $|c_0|^2 + |c_1|^2 + |c_2|^2 + ... = 1$
* Position basis: $\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1$
* Momentum basis: $\int_{-\infty}^{\infty} |\tilde{\psi}(p)|^2 dp = 1$

The length stays 1 in all bases, just like a unit vector in 3D keeps length 1 in any coordinate system!

---

## Three Faces of One State

Let's make this concrete. Suppose our quantum state is a superposition of the first three harmonic oscillator energy levels:

$$
|\psi\rangle = c_0 |0\rangle + c_1 |1\rangle + c_2 |2\rangle
$$

where $|0\rangle, |1\rangle, |2\rangle$ are energy eigenstates with $E_n = \hbar\omega(n + \frac{1}{2})$. The coefficients $c_0, c_1, c_2$ are complex probability amplitudes.

This is ONE quantum state. Let's see its three faces.

### Face 1: Energy Basis (3 Numbers)

The state is just a column vector of coefficients:

$$
|\psi\rangle = \begin{pmatrix} c_0 \\ c_1 \\ c_2 \end{pmatrix}
$$

**Probabilities:** Measuring energy $E_n$ gives probability $|c_n|^2$:
* $P(E_0) = |c_0|^2$
* $P(E_1) = |c_1|^2$
* $P(E_2) = |c_2|^2$

**Normalization:** $|c_0|^2 + |c_1|^2 + |c_2|^2 = 1$

**Example:** Take $c_0 = \frac{1}{2}, c_1 = \frac{\sqrt{2}}{2}, c_2 = \frac{1}{2}$. Then:
* Probabilities: 25%, 50%, 25%
* Average energy: $\langle E \rangle = E_0 \cdot \frac{1}{4} + E_1 \cdot \frac{1}{2} + E_2 \cdot \frac{1}{4} = \frac{3}{2}\hbar\omega$

In the energy basis, everything is simple!

### Face 2: Position Basis (A Function)

The SAME state expressed as a function of position:

$$
\psi(x) = c_0 \psi_0(x) + c_1 \psi_1(x) + c_2 \psi_2(x)
$$

where $\psi_0(x), \psi_1(x), \psi_2(x)$ are the Gaussian energy eigenstates from Part 1.

**Key insight:** We're still using the same three energy components $(c_0, c_1, c_2)$, but now each energy eigenstate is expressed as a function of $x$. This gives us infinitely many numbers — one $\psi(x)$ value for every position $x$ — because each Gaussian $\psi_n(x)$ is non-zero everywhere.

**Probabilities:** $|\psi(x)|^2$ is the probability **density**. The probability of finding the particle between $x = a$ and $x = b$ is:

$$
P(a \leq x \leq b) = \int_a^b |\psi(x)|^2 dx
$$

**Normalization:** $\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1$ (same length-1 constraint, different form)

### Face 3: Momentum Basis (Also a Function)

The SAME state in momentum space:

$$
\tilde{\psi}(p) = \text{Fourier transform of } \psi(x)
$$

Same state, now giving amplitude for each momentum value $p$.

### The Profound Insight

**How can the SAME state need 3 numbers in one basis but infinite in another?**

In the energy representation, we're only tracking 3 basis vectors (the first 3 energy levels). The full Hilbert space has infinitely many energy levels! But our particular state has $c_n = 0$ for all $n \geq 3$, so we only need those 3 numbers.

It's like a vector in 3D that lies in the xy-plane: you could use 3 coordinates $(x, y, 0)$, or just 2 since $z = 0$. The space is still 3D, but this vector simplifies.

Similarly, our quantum state lives in infinite-dimensional Hilbert space but only has components in the first 3 energy levels. In energy basis: just 3 numbers. Switch to position basis: every position $x$ gets non-zero amplitude $\psi(x)$ because the Gaussians spread out, so you need infinitely many numbers.

**This is quantum mechanics' power:** Different bases can dramatically simplify or complicate the description!

### Why Choose Different Bases?

You have ONE state $|\psi\rangle$, but different questions lead to different representations:

**Question:** "What's the probability the particle is between $x = 1$ and $x = 2$?"
**Use:** Position basis → Answer: $\int_1^2 |\psi(x)|^2 dx$

**Question:** "What's the probability of energy $E_1$?"
**Use:** Energy basis → Answer: $|c_1|^2$ (trivial!)

**Question:** "What's the probability of momentum between $p_1$ and $p_2$?"
**Use:** Momentum basis → Answer: $\int_{p_1}^{p_2} |\tilde{\psi}(p)|^2 dp$

Each basis makes certain questions trivial and others hard!

---

## Time Evolution

Now add time. Each energy component picks up a phase factor $e^{-iE_n t/\hbar}$:

$$
|\psi(t)\rangle = c_0 |0\rangle e^{-iE_0 t/\hbar} + c_1 |1\rangle e^{-iE_1 t/\hbar} + c_2 |2\rangle e^{-iE_2 t/\hbar}
$$

**Important:** The coefficients $c_0, c_1, c_2$ are **constants**. What changes is the **phase** of each component. Different energies have different frequencies $\omega_n = E_n/\hbar$, so phases evolve at different rates:
* Ground state: $e^{-i\omega t/2}$ (slowest)
* First excited: $e^{-i3\omega t/2}$
* Second excited: $e^{-i5\omega t/2}$ (fastest)

In position space:

$$
\psi(x,t) = c_0 \psi_0(x) e^{-iE_0 t/\hbar} + c_1 \psi_1(x) e^{-iE_1 t/\hbar} + c_2 \psi_2(x) e^{-iE_2 t/\hbar}
$$

The probability density $|\psi(x,t)|^2$ **oscillates** — different energy components beat against each other, creating a sloshing pattern. But the energy probabilities $|c_n|^2$ never change — energy is conserved! Only relative phases evolve.

**Geometric picture:** The quantum state $|\psi(t)\rangle$ is a vector in Hilbert space that **rotates** as time passes. Each component $c_n$ rotates at frequency $\omega_n = E_n/\hbar$. For superpositions, different components beat against each other, creating the oscillating probability densities we observe. The vector traces a complicated path through infinite-dimensional space, but its length stays 1.

---

## Mathematical Machinery: Inner Products and Bra-Ket Notation

### Extracting Components via Dot Product

We have $|\psi\rangle = c_0 |0\rangle + c_1 |1\rangle + c_2 |2\rangle$. How do we extract $c_1$?

**Answer:** Take the dot product with $|1\rangle$.

In 3D, if $\vec{v} = v_x \hat{x} + v_y \hat{y} + v_z \hat{z}$, then $\vec{v} \cdot \hat{y} = v_y$ because $\hat{x} \cdot \hat{y} = 0$, $\hat{y} \cdot \hat{y} = 1$, $\hat{z} \cdot \hat{y} = 0$. The dot product **projects** onto one axis.

In quantum mechanics, energy eigenstates are orthonormal (just like $\hat{x}, \hat{y}, \hat{z}$):

$$
\text{(dot product of } |m\rangle \text{ with } |n\rangle \text{)} = \begin{cases} 1 & \text{if } m = n \\ 0 & \text{if } m \neq n \end{cases}
$$

To extract $c_1$, write $|1\rangle$ as a row vector and multiply:

$$
\begin{pmatrix} 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} c_0 \\ c_1 \\ c_2 \end{pmatrix} = c_1
$$

For complex vectors, we take the complex conjugate when making the row vector (transpose + conjugate).

**Continuous case:** For position or momentum (continuous indices), the dot product becomes an integral:

$$
\text{Dot product} = \int_{-\infty}^{\infty} \phi^*(x) \psi(x) \, dx
$$

The sum $\sum$ becomes integral $\int dx$, but the structure is identical!

**Position eigenstates are also orthonormal**, but in the continuous sense:

$$
\langle x' | x \rangle = \delta(x' - x)
$$

where $\delta(x' - x)$ is the Dirac delta function (infinite spike at $x' = x$, zero elsewhere). This is the continuous analog of the discrete Kronecker delta. It means:
* Different position eigenstates are orthogonal: $\langle x'|x\rangle = 0$ if $x' \neq x$
* Same position eigenstate has "infinite norm" concentrated at one point (we normalize by integrating over a region)

### Bra-Ket Notation

We need clean notation for dot products. We write quantum states as $|\psi\rangle$ (a "ket" = column vector). For dot products, we need notation for the row vector (complex conjugate transpose).

**The bra:** $\langle \psi |$ (row vector, ready to do a dot product)

Together:
$$
\langle \phi | \psi \rangle = \text{bra-ket} = \text{bracket} = \text{inner product}
$$

This is the quantum analog of the dot product. It measures the "overlap" between two quantum states.

**Energy basis (discrete):** To extract the n-th component:

$$
c_n = \langle n | \psi \rangle
$$

This is literally the dot product of basis vector $|n\rangle$ with state $|\psi\rangle$. In matrix form:

$$
c_n = \begin{pmatrix} 0 & \cdots & 0 & 1 & 0 & \cdots \end{pmatrix} \begin{pmatrix} c_0 \\ \vdots \\ c_n \\ \vdots \end{pmatrix} = c_n
$$

General inner product of two states: $\langle \phi | \psi \rangle = \sum_n d_n^* c_n$ (complex conjugate first state, multiply components, sum)

**Position basis (continuous):** To extract the position-space wavefunction:

$$
\psi(x) = \langle x | \psi \rangle
$$

This says: "The wavefunction at position x is the inner product of the position eigenstate $|x\rangle$ with the abstract state $|\psi\rangle$." It's projecting $|\psi\rangle$ onto the position basis!

General inner product of two states: $\langle \phi | \psi \rangle = \int_{-\infty}^{\infty} \phi^*(x) \psi(x) \, dx$ (complex conjugate first state, multiply, integrate)

### The Beauty of Bra-Ket Notation

**Why this notation?** The expression $\langle n | \psi \rangle$ works in **any basis** — it just changes between sum (discrete) and integral (continuous). You don't rewrite formulas when switching representations!

**Unified formulas that work everywhere:**

| Formula | Discrete (Energy) | Continuous (Position) |
|---------|-------------------|----------------------|
| **Extract component** | $c_n = \langle n \| \psi \rangle$ | $\psi(x) = \langle x \| \psi \rangle$ |
| **Reconstruct state** | $\|\psi\rangle = \sum_n \langle n\|\psi\rangle \|n\rangle$ | $\|\psi\rangle = \int \langle x\|\psi\rangle \|x\rangle dx$ |
| **Inner product** | $\langle\phi\|\psi\rangle = \sum_n \langle\phi\|n\rangle^* \langle n\|\psi\rangle$ | $\langle\phi\|\psi\rangle = \int \langle\phi\|x\rangle^* \langle x\|\psi\rangle dx$ |
| **Orthonormality** | $\langle m \| n \rangle = \delta_{mn}$ | $\langle x' \| x \rangle = \delta(x' - x)$ |

Same structure, different notation for "sum over basis"!

**Notation note:**
* $|n\rangle$ means "the n-th energy eigenstate" (discrete index: n = 0, 1, 2, ...)
* $|x\rangle$ means "position eigenstate at position x" (continuous index: x is any real number)
* $|x\rangle$ is **not** the same as $\psi(x)$! One is a basis vector, the other is a component/coefficient
  * $|x\rangle$ = basis vector (like $\hat{x}, \hat{y}, \hat{z}$ in 3D)
  * $\psi(x) = \langle x|\psi\rangle$ = coefficient (like $v_x, v_y, v_z$ in 3D)

---

## Operators: From Waves to Observables

### How Operators Emerge

In Part 1, we saw a particle with definite momentum $p$ and energy $E$ is described by:

$$
\psi(x,t) = A e^{i(px/\hbar - Et/\hbar)}
$$

**Watch what happens when we take derivatives:**

$$
\frac{\partial\psi}{\partial x} = \frac{ip}{\hbar}\psi \quad \Rightarrow \quad -i\hbar\frac{\partial}{\partial x}\psi = p\psi
$$

$$
\frac{\partial\psi}{\partial t} = -\frac{iE}{\hbar}\psi \quad \Rightarrow \quad i\hbar\frac{\partial}{\partial t}\psi = E\psi
$$

**The derivative operators extract the observable values!** This is how operators are born — they're mathematical tools that extract physical quantities from waves.

### What Are Operators?

Operators are mathematical objects that extract physical observables from quantum states. Each measurable quantity has an operator:

* $\hat{H}$ = Hamiltonian (energy operator) = $-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)$
* $\hat{x}$ = position operator (multiply by $x$ in position basis)
* $\hat{p}$ = momentum operator = $-i\hbar \frac{\partial}{\partial x}$ (in position basis)
* $\hat{L}$ = angular momentum operator

The Hamiltonian has two key roles:
1. **Eigenvalue equation:** $\hat{H}|n\rangle = E_n|n\rangle$ finds energy eigenstates
2. **Time evolution:** $i\hbar \frac{\partial}{\partial t}|\psi\rangle = \hat{H}|\psi\rangle$ determines how states evolve

The Schrödinger equation says: "The rate of change of the state is determined by its energy." States with higher energy oscillate faster!

### Eigenvalue Equations and Why Eigenstates Are Special

The eigenvalue equation for the Hamiltonian:

$$
\hat{H}|n\rangle = E_n|n\rangle
$$

says: "When the energy operator acts on energy eigenstate $|n\rangle$, it returns the energy value $E_n$ times that state."

This is what we've been solving! The time-independent Schrödinger equation $\hat{H}\psi = E\psi$ finds:
* **Eigenstates:** special states $|n\rangle$ (or $\psi_n(x)$ in position representation)
* **Eigenvalues:** energy values $E_n$

**Why are eigenstates special?**

1. **Natural "coordinate axes"** for that observable
2. **Orthogonal:** $\langle m|n\rangle = 0$ if $m \neq n$, $= 1$ if $m = n$
3. **Complete:** any state decomposes as $|\psi\rangle = \sum_n c_n |n\rangle$
4. **Simple probabilities:** $|c_n|^2$ are independent probabilities that add classically (no interference)

When you measure energy, you're asking "which eigenstate am I in?" Orthogonality ensures probabilities don't interfere — they just add.

### Expectation Values

If you measure energy many times on identical copies of $|\psi\rangle$, what's the **average**?

**Classical analogy:** Rolling a weighted die with probabilities $P_1, ..., P_6$:

$$
\langle \text{value} \rangle = \sum_{n=1}^{6} n \cdot P_n
$$

(weighted average: each outcome times its probability)

**Quantum case:** For $|\psi\rangle = \sum_n c_n |n\rangle$, probability of measuring $E_n$ is $|c_n|^2$:

$$
\langle E \rangle = \sum_n E_n |c_n|^2
$$

Quantum mechanics gives us a compact formula for **any** observable $A$:

$$
\langle A \rangle = \langle \psi | \hat{A} | \psi \rangle
$$

**Why does this work?** Start with $|\psi\rangle = \sum_n c_n |n\rangle$ and apply the operator using $\hat{H}|n\rangle = E_n|n\rangle$:

$$
\hat{H}|\psi\rangle = \sum_n c_n E_n |n\rangle
$$

Take inner product with $\langle\psi| = \sum_m c_m^* \langle m|$:

$$
\langle \psi | \hat{H} | \psi \rangle = \sum_{m,n} c_m^* c_n E_n \langle m|n\rangle = \sum_n |c_n|^2 E_n
$$

using orthonormality $\langle m|n\rangle = \delta_{mn}$.

The sandwich $\langle \psi | \hat{A} | \psi \rangle$ automatically:
1. Decomposes the state into eigenstates
2. Weights each eigenvalue by its probability
3. Sums them up

This formula works in **any basis**!

### Operators in Different Bases

**Key insight:** Operators are easy in their own eigenbasis, hard in others.

**Energy basis:**
* $\hat{H}$ is trivial (diagonal matrix): $\hat{H} = \text{diag}(E_0, E_1, E_2, ...)$
* $\hat{x}$ is complicated (off-diagonal, mixes energy states)

**Position basis:**
* $\hat{x}$ is trivial: $\hat{x}\psi(x) = x\psi(x)$ (just multiply by $x$)
* $\hat{H}$ is complicated: $\hat{H}\psi(x) = -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi(x)$ (differential operator)
* $\hat{p}$ is also a differential operator: $\hat{p} = -i\hbar \frac{\partial}{\partial x}$

### The Parallel Structure

| Concept | Energy Basis (Discrete) | Position Basis (Continuous) |
|---------|-------------------------|----------------------------|
| **State components** | $c_n = \langle n\|\psi\rangle$ | $\psi(x) = \langle x\|\psi\rangle$ |
| **Combine components** | $\sum_n$ | $\int dx$ |
| **Probability** | $\|c_n\|^2$ | $\|\psi(x)\|^2$ (density) |
| **Normalization** | $\sum_n \|c_n\|^2 = 1$ | $\int \|\psi(x)\|^2 dx = 1$ |
| **Easy operator** | $\hat{H}$ (diagonal) | $\hat{x}$ (multiply) |
| **Hard operator** | $\hat{x}$ (matrix) | $\hat{H}$ (differential) |
| **Inner product** | $\langle\psi\|\phi\rangle = \sum_n c_n^* d_n$ | $\langle\psi\|\phi\rangle = \int \psi^*(x)\phi(x) dx$ |

Discrete sums become integrals, but the structure is **identical**!

---

## Schrödinger's Equation in All Its Forms

The usual Schrödinger equation is in position coordinates:

$$
i\hbar\frac{\partial\psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi(x,t)}{\partial x^2} + V(x)\psi(x,t)
$$

But you can write it in **any basis**!

**Energy basis** (super simple!):

$$
i\hbar\frac{dc_n(t)}{dt} = E_n c_n(t) \quad \Rightarrow \quad c_n(t) = c_n(0) e^{-iE_n t/\hbar}
$$

Just a rotating phase!

**Momentum basis:**

$$
i\hbar\frac{\partial\tilde{\psi}(p,t)}{\partial t} = \frac{p^2}{2m}\tilde{\psi}(p,t) + \tilde{V}(p)\tilde{\psi}(p,t)
$$

Kinetic energy is simple (multiply by $p^2/2m$), potential energy is hard (convolution).

**Basis-independent form** (the most fundamental!):

$$
i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle = \hat{H}|\psi(t)\rangle
$$

This is the "true" Schrödinger equation. It doesn't care what basis you use! The abstract state $|\psi(t)\rangle$ is more fundamental than any particular representation.

---

## Computing with Quantum States

### Example 1: Energy Basis

State: $|\psi\rangle = \frac{1}{2}|0\rangle + \frac{\sqrt{2}}{2}|1\rangle + \frac{1}{2}|2\rangle$

**Probabilities:**
* $P(E_0) = |c_0|^2 = 1/4 = 25\%$
* $P(E_1) = |c_1|^2 = 1/2 = 50\%$
* $P(E_2) = |c_2|^2 = 1/4 = 25\%$

**Average energy:**

$$
\langle E \rangle = \frac{1}{2}\hbar\omega \cdot \frac{1}{4} + \frac{3}{2}\hbar\omega \cdot \frac{1}{2} + \frac{5}{2}\hbar\omega \cdot \frac{1}{4} = \frac{7}{4}\hbar\omega
$$

### Example 2: Position Basis

For the first excited state $|n=1\rangle$ with wavefunction:

$$
\psi_1(x) = \left(\frac{1}{4\pi x_0^2}\right)^{1/4} \frac{2x}{x_0} e^{-x^2/(2x_0^2)}
$$

**Average position:** $\langle x \rangle = \int x |\psi_1(x)|^2 dx = 0$ (by symmetry)

**Average momentum:** $\langle p \rangle = \int \psi_1^*(x) \left(-i\hbar \frac{\partial}{\partial x}\right) \psi_1(x) dx = 0$ (by symmetry)

**Average energy:** $\langle E \rangle = \int \psi_1^*(x) \hat{H} \psi_1(x) dx = E_1 = \frac{3}{2}\hbar\omega$ (eigenstate!)

Notice: calculating $\hat{H}\psi_1(x)$ requires second derivatives — much harder than the energy basis!

---

## The Bridge to Matrix Mechanics

In finite-dimensional space (spin-½, or truncating to first N energy levels), everything becomes linear algebra.

**States → column vectors:**

$$
|\psi\rangle = \begin{pmatrix} c_0 \\ c_1 \\ c_2 \\ \vdots \end{pmatrix}
$$

**Operators → matrices.** Hamiltonian in energy basis:

$$
\hat{H} = \begin{pmatrix} E_0 & 0 & 0 & \cdots \\ 0 & E_1 & 0 & \cdots \\ 0 & 0 & E_2 & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}
$$

**Eigenvalue equation:** $\hat{H}|\psi\rangle = E|\psi\rangle$ becomes $H\mathbf{c} = E\mathbf{c}$ (standard matrix problem)

**Time evolution:** Matrix exponential:

$$
|\psi(t)\rangle = e^{-i\hat{H}t/\hbar}|\psi(0)\rangle
$$

For diagonal $\hat{H}$, this rotates each component: $c_n(t) = e^{-iE_n t/\hbar} c_n(0)$

**The punchline:** The continuous wavefunctions $\psi(x)$ are the **infinite-dimensional limit** of this finite picture. Same structure — eigenstates, operators, inner products, time evolution — just with integrals instead of sums!

This is why quantum mechanics is called "wave mechanics" (Schrödinger's wavefunctions) or "matrix mechanics" (Heisenberg's matrices). Same theory, different lenses.

---

*Next up: Spin-½ — where everything is 2×2 matrices, and all of quantum mechanics fits in a tiny box. This is the foundation of qubits and quantum computing.*
