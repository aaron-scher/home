# Quantum Mechanics: Basis Representation

**Prerequisites:** This builds on [Quantum Foundations](quantum-foundations.md) where we derived Schrödinger's equation and explored the harmonic oscillator. If you haven't read that yet, start there first!

---

## The Harmonic Oscillator: One State, Three Representations

In Part 1, we found that the harmonic oscillator has discrete energy levels $E_n = \hbar\omega(n + \frac{1}{2})$ with corresponding energy eigenstates $\psi_n(x)$ (Gaussians with increasing nodes). Here's the key insight: **we can describe the same quantum state in three different "languages"** depending on what we want to measure.

### The Solutions

| **Representation** | **Variable** | **Expression** | **Domain** |
|-------------------|--------------|----------------|------------|
| **Position** | $x$ | $\psi(x,t) = \sum_n c_n e^{-iE_n t/\hbar} \psi_n(x)$ | continuous |
| **Momentum** | $p$ | $\psi(p,t) = \sum_n c_n e^{-iE_n t/\hbar} \phi_n(p)$ | continuous |
| **Energy (index)** | $n$ | $\psi_E[n,t] = c_n e^{-iE_n t/\hbar} = \sum_m c_m e^{-iE_m t/\hbar} \delta_{n,m}$ | discrete |

**Think of these as:**

- $\psi(x,t)$ — amplitudes in **space**
- $\psi(p,t)$ — amplitudes in **momentum**
- $\psi_E[n,t]$ — amplitudes in **energy index (n)**

The position and momentum representations are continuous functions (infinitely many values), while the energy representation is a discrete list of coefficients $c_0, c_1, c_2, ...$ (one for each energy level).

### The Energy Rotation Phasor

The factor $e^{-iE_n t/\hbar}$ is the **energy rotation phasor**. Each energy level rotates in the complex plane at its own rate:

- Higher energy → faster rotation (higher $E_n$ means faster $\omega_n = E_n/\hbar$)
- Lower energy → slower rotation
- The phase $\phi_n(t) = -E_n t/\hbar$ advances linearly in time

This phase rotation is fundamental to quantum dynamics, but for now, we'll work at $t=0$ for simplicity. The spatial structure doesn't change with time—only these phases rotate. Understanding basis representation at $t=0$ captures all the key concepts.

### Normalization

The energy eigenstates $\psi_0(x), \psi_1(x), \psi_2(x), ...$ in the position representation are all **normalized**, meaning:

$$\int_{-\infty}^{\infty} |\psi_n(x)|^2 dx = 1$$

This ensures the total probability of finding the particle somewhere is 100%. When we write a general state as a sum $\psi(x) = \sum_n c_n \psi_n(x)$, each $\psi_n(x)$ already satisfies this normalization condition.

**The coefficients $c_n$ are ALSO normalized**. Since $|c_n|^2$ represents the probability of measuring energy $E_n$, all probabilities must sum to 1:

$$\sum_{n=0}^{\infty} |c_n|^2 = 1$$

For our running example with $c_0 = \frac{1}{2}$, $c_1 = \frac{\sqrt{2}}{2}$, $c_2 = \frac{1}{2}$ (all others zero), let's verify:

$$|c_0|^2 + |c_1|^2 + |c_2|^2 = \left|\frac{1}{2}\right|^2 + \left|\frac{\sqrt{2}}{2}\right|^2 + \left|\frac{1}{2}\right|^2 = \frac{1}{4} + \frac{1}{2} + \frac{1}{4} = 1 \,\checkmark$$

This holds for any valid quantum state—the probability of measuring *something* must always be 100%.

### Why Choose Different Representations?

Each representation makes certain questions trivial:

**"What's the probability of energy $E_1$?"** → Energy basis: just $|c_1|^2$. One number!

**"Where is the particle most likely to be found?"** → Position basis: find max of $|\psi(x)|^2$

**"What's the momentum distribution?"** → Momentum basis: $|\psi(p)|^2$ directly tells you the probability density in momentum space. Useful for scattering problems, particle physics, and understanding wave packets.

The art of quantum mechanics is choosing the right tool for the job. Let's see how this works!

---

## What IS the Quantum State?

Here's the deeper question: **What IS the quantum state?** Is it the function $\psi(x)$? The coefficients $[c_0, c_1, c_2, ...]$? The momentum function $\psi(p)$? Or something more fundamental?

The answer: there's an **abstract quantum state** $|\psi\rangle$ (called a "ket") that exists independent of how we describe it. The different functions we use are just different ways of writing down the same underlying thing:

- $\psi(x)$ = position representation (a function of position)
- $\psi(p)$ = momentum representation (a function of momentum)
- $[c_0, c_1, c_2, ...]$ = energy representation (a list of coefficients)

Same state, different descriptions! Like how a 3D vector doesn't change whether you use Cartesian or spherical coordinates. The vector itself is the same; only the numbers you write change.

### The Abstract State |ψ⟩

The ket $|\psi\rangle$ is the complete quantum state—the thing itself before you choose how to describe it.

**The vector analogy:** An arrow in 3D space doesn't change if you describe it using Cartesian coordinates $(x, y, z)$ or cylindrical coordinates $(r, \theta, z)$. It's the same arrow, same length, same direction. Only the numbers you write down change. The arrow itself is **basis-independent**.

Similarly, $|\psi\rangle$ exists independent of whether you ask about position, momentum, or energy. It contains all the information; you just need to choose which representation to use.

### Projecting the State into Different "Realms"

Here's how we extract different representations from the abstract state $|\psi\rangle$. We **project** it into the realm of whatever physical property we want to observe:

$$\langle x|\psi\rangle = \psi(x) \quad \text{(position wavefunction)}$$

$$\langle p|\psi\rangle = \tilde{\psi}(p) \quad \text{(momentum wavefunction)}$$

$$\langle n|\psi\rangle = c_n \quad \text{(energy coefficient)}$$

Don't worry about the $\langle$ $|$ notation yet—we'll explain it thoroughly in the next section. For now, the key idea is:

- The abstract state $|\psi\rangle$ contains everything
- **Projections** extract specific aspects we care about
- Want to know about position? Project onto position basis with $\langle x|$
- Want to know about energy? Project onto energy basis with $\langle n|$
- Want to know about momentum? Project onto momentum basis with $\langle p|$

The state itself doesn't change—only our view of it changes. Just like the arrow in 3D space stays the same whether you describe it in Cartesian, cylindrical, or spherical coordinates.

---

## THE DISCRETE CASE: Energy Basis (Complete Treatment)

Let's master the discrete case completely before moving to continuous variables. We'll build everything from column vectors (which you already know from linear algebra) to the full quantum formalism.

---

## Building States: Start With Column Vectors

### Our Running Example

Throughout this section, we'll work with one concrete quantum state:

**A superposition of three energy levels (n=0, n=1, n=2) with coefficients:**

- $c_0 = \frac{1}{2}$
- $c_1 = \frac{\sqrt{2}}{2}$
- $c_2 = \frac{1}{2}$
- All others zero

This isn't random—these coefficients are normalized (we'll verify this soon), and this state will help us see all the key ideas concretely.

### Column Vectors

We can represent our three energy levels as **basis vectors**—these are "one-hot" column vectors with a 1 in one position and 0 everywhere else:

**Energy level 0:**

$$\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ \vdots \end{pmatrix}$$

**Energy level 1:**

$$\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ \vdots \end{pmatrix}$$

**Energy level 2:**

$$\begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix}$$

Each basis vector represents "definitely in energy level n". The first entry corresponds to n=0, second to n=1, third to n=2, and so on.

### Vector Addition With Concrete Numbers

Now here's the key: our quantum state is built by **adding scaled basis vectors**, just like in 3D where $\vec{v} = 2\hat{x} + 3\hat{y} + 1\hat{z}$:

$$
\text{state} = \frac{1}{2}\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ \vdots \end{pmatrix} + \frac{\sqrt{2}}{2}\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \\ \vdots \end{pmatrix} + \frac{1}{2}\begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix}
$$

Let's do the addition explicitly:

$$
\text{state} = \begin{pmatrix}
\frac{1}{2} \cdot 1 + \frac{\sqrt{2}}{2} \cdot 0 + \frac{1}{2} \cdot 0 \\
\frac{1}{2} \cdot 0 + \frac{\sqrt{2}}{2} \cdot 1 + \frac{1}{2} \cdot 0 \\
\frac{1}{2} \cdot 0 + \frac{\sqrt{2}}{2} \cdot 0 + \frac{1}{2} \cdot 1 \\
0 \\
\vdots
\end{pmatrix} = \begin{pmatrix}
\frac{1}{2} \\
\frac{\sqrt{2}}{2} \\
\frac{1}{2} \\
0 \\
\vdots
\end{pmatrix}
$$

This is just vector addition! We're scaling each basis vector by its coefficient and adding them together. The result is a column vector whose entries are exactly our coefficients $c_0, c_1, c_2, ...$

### Introducing Ket Notation as Shorthand

Writing out full column vectors gets tedious, so physicists invented a compact notation called **ket notation**. The symbol $|n\rangle$ is shorthand for the column vector we just wrote:

- $|0\rangle$ means $\begin{pmatrix} 1 \\ 0 \\ 0 \\ \vdots \end{pmatrix}$
- $|1\rangle$ means $\begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix}$
- $|2\rangle$ means $\begin{pmatrix} 0 \\ 0 \\ 1 \\ \vdots \end{pmatrix}$

The ket $|\psi\rangle$ **IS** the column vector—it's just cleaner notation. Our state becomes:

$$|\psi\rangle = \frac{1}{2}|0\rangle + \frac{\sqrt{2}}{2}|1\rangle + \frac{1}{2}|2\rangle$$

In general, we write this compactly as:

$$|\psi\rangle = \sum_{n=0}^{\infty} c_n |n\rangle$$

where the sum $\sum c_n |n\rangle$ just means "add up all the scaled basis vectors"—exactly what we did above!

**Key insight:** The ket notation $|n\rangle$ and $|\psi\rangle$ is just shorthand for column vectors. Everything you know about vectors from linear algebra applies directly.

### A Note on "Hilbert Space"

You might hear quantum mechanics described as taking place in a "Hilbert space" and think it sounds intimidating. It's not! **Hilbert space is just the fancy mathematical name for the vector space we're working in.**

Think of it this way:
- In 3D, vectors live in $\mathbb{R}^3$ (three-dimensional real space)
- In quantum mechanics, state vectors live in Hilbert space

Hilbert space is just:
1. A vector space (you can add vectors and multiply by scalars)
2. With an inner product (you can compute $\langle\phi|\psi\rangle$)
3. That's complete (technical detail: every Cauchy sequence converges - don't worry about this)

For our energy basis with states like $|\psi\rangle = \sum_n c_n |n\rangle$, the Hilbert space is just the space of all possible sequences $(c_0, c_1, c_2, ...)$ where $\sum_n |c_n|^2 < \infty$. That's it!

**Bottom line:** "Hilbert space" = "vector space with inner product". Same linear algebra you know, just with a fancier name. Nothing to be scared of!

---

## Extracting Components: Bras and Inner Products

We have our state $|\psi\rangle = \frac{1}{2}|0\rangle + \frac{\sqrt{2}}{2}|1\rangle + \frac{1}{2}|2\rangle$ as a column vector. But suppose someone just hands you the abstract state $|\psi\rangle$—how do you GET the coefficients $c_0, c_1, c_2$ from it?

The answer: **inner products** (quantum dot products).

### Review: The 3D Dot Product

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

## Probabilities and Normalization

Now that we can extract coefficients, let's use them to calculate physical quantities. We'll use our running example throughout.

### From Coefficients to Probabilities

The Born rule tells us: **the probability of measuring energy $E_n$ is the squared magnitude of coefficient $c_n$**:

$$P(E_n) = |c_n|^2$$

For our state with $c_0 = \frac{1}{2}$, $c_1 = \frac{\sqrt{2}}{2}$, $c_2 = \frac{1}{2}$:

$$P(E_0) = \left|\frac{1}{2}\right|^2 = \frac{1}{4} = 25\%$$

$$P(E_1) = \left|\frac{\sqrt{2}}{2}\right|^2 = \frac{1}{2} = 50\%$$

$$P(E_2) = \left|\frac{1}{2}\right|^2 = \frac{1}{4} = 25\%$$

So if we measure the energy, we have a 25% chance of finding $E_0 = \frac{1}{2}\hbar\omega$, a 50% chance of finding $E_1 = \frac{3}{2}\hbar\omega$, and a 25% chance of finding $E_2 = \frac{5}{2}\hbar\omega$.

### The Average Energy

What's the **average (expected) energy** if we measure many identical systems? It's the weighted average:

$$\langle E \rangle = \sum_n P(E_n) \cdot E_n$$

For our example:

$$\langle E \rangle = \frac{1}{4}\left(\frac{1}{2}\hbar\omega\right) + \frac{1}{2}\left(\frac{3}{2}\hbar\omega\right) + \frac{1}{4}\left(\frac{5}{2}\hbar\omega\right)$$

$$= \frac{1}{8}\hbar\omega + \frac{3}{4}\hbar\omega + \frac{5}{8}\hbar\omega = \frac{1 + 6 + 5}{8}\hbar\omega = \frac{12}{8}\hbar\omega = \frac{3}{2}\hbar\omega$$

This makes sense—the average energy is between $E_1$ and $E_2$, weighted toward $E_1$ since that's the most probable outcome.

### Normalization: Probabilities Must Sum to 100%

Here's a fundamental requirement: **all probabilities must add up to 1** (100%). The particle must be found in *some* energy state when we measure!

In bra-ket notation, this is written as:

$$\langle\psi|\psi\rangle = 1$$

This is the **inner product** of the state with itself. In the energy basis, this expands to:

$$\langle\psi|\psi\rangle = \sum_n |c_n|^2 = 1$$

Let's verify this for our example:

$$|c_0|^2 + |c_1|^2 + |c_2|^2 = \frac{1}{4} + \frac{1}{2} + \frac{1}{4} = 1 \quad \checkmark$$

Perfect! This is what we mean when we say a state is **normalized**. If someone gives you arbitrary coefficients, you need to rescale them so this condition holds.

**Physical meaning:** Normalization ensures conservation of probability. When you measure, you're guaranteed to get *some* result—the probabilities of all possible outcomes must sum to certainty.

---

## Time Evolution and Phase Rotation

Quantum time evolution is beautifully simple in the energy basis.

### The Evolution Rule from Schrödinger's Equation

How do states change with time? The fundamental equation is the time-dependent Schrödinger equation:

$$i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle = \hat{H}|\psi(t)\rangle$$

"The rate of change of the state equals its energy (the Hamiltonian $\hat{H}$ operating on it), divided by $i\hbar$."

In the energy basis, this becomes remarkably simple. Since energy eigenstates satisfy $\hat{H}|n\rangle = E_n|n\rangle$, each coefficient evolves **independently**:

$$i\hbar\frac{dc_n(t)}{dt} = E_n c_n(t)$$

This is a simple differential equation with solution:

$$\boxed{c_n(t) = c_n(0) \cdot e^{-iE_n t/\hbar}}$$

Each coefficient just picks up a rotating phase! The factor $e^{-iE_n t/\hbar}$ is the energy rotation phasor we saw earlier.

### Applying to Our Running Example

For our state, time evolution looks like:

$$|\psi(t)\rangle = \frac{1}{2}|0\rangle e^{-iE_0 t/\hbar} + \frac{\sqrt{2}}{2}|1\rangle e^{-iE_1 t/\hbar} + \frac{1}{2}|2\rangle e^{-iE_2 t/\hbar}$$

Higher energy means faster rotation in the complex plane ($E_2$ rotates fastest, $E_0$ slowest).

### What This Means Physically

The **magnitudes** $|c_n(t)| = |c_n(0)|$ never change! Only the **phases** rotate. This means:

- Energy probabilities $P(E_n) = |c_n|^2$ are **constant in time**
- The average energy $\langle E \rangle$ never changes
- Only **relative phases** between different energy levels evolve

This is why energy is conserved in quantum mechanics—the energy basis is special!

### The Deep Physics: Rotation and Interference

Different numbers of energy levels create fundamentally different dynamics:

**One energy level:** $|\psi\rangle = |n\rangle$
- Just picks up overall phase: $|n\rangle \to |n\rangle e^{-iE_n t/\hbar}$
- Overall phase has **no observable effect** (it factors out of all measurements)
- These are **stationary states**—nothing changes!
- No dynamics at all

**Two energy levels:** Like a qubit
- $|\psi\rangle = c_0|0\rangle e^{-i\omega_0 t} + c_1|1\rangle e^{-i\omega_1 t}$ (with $\omega_n = E_n/\hbar$)
- **Relative phase** $\Delta\phi = (\omega_1 - \omega_0)t$ creates oscillations
- This is fundamentally what makes qubits interesting!
- Like Bloch sphere dynamics—interference between two levels
- Observable quantities oscillate at the beat frequency $\omega_1 - \omega_0$

**Multiple energy levels:** Our example
- Many frequencies beating against each other
- Multi-dimensional phase space
- Complex interference patterns

### In Position Space: The State "Sloshes"

What does this look like in position space? For our state:

$$\psi(x,t) = \frac{1}{2}\psi_0(x)e^{-iE_0 t/\hbar} + \frac{\sqrt{2}}{2}\psi_1(x)e^{-iE_1 t/\hbar} + \frac{1}{2}\psi_2(x)e^{-iE_2 t/\hbar}$$

Different energy levels oscillate at different frequencies. When you compute the probability density $|\psi(x,t)|^2$, these different frequencies **interfere**, creating oscillating patterns in space.

The quantum state "sloshes" back and forth in position space, while maintaining constant energy probabilities. Energy eigenstates don't change shape—only their relative phases rotate, creating interference when viewed in other bases.

**This is the origin of quantum dynamics!** Superpositions create time evolution. Pure energy eigenstates are static ("stationary"). Only mixing different energies creates observable change.

---

## THE CONTINUOUS CASE: Position Basis

Now we've mastered the discrete case. Let's extend these ideas to **continuous** variables like position. The key insight: position is just like energy, except the labels are continuous real numbers instead of discrete integers.

---

## From Discrete to Continuous: The Natural Path

### Start With Discrete Position

Imagine a particle that can only be at N specific locations: $x_1, x_2, ..., x_N$ (like beads on a wire with fixed positions).

This is just like the energy basis! We have basis vectors:

$$
|x_1\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ \vdots \end{pmatrix} \quad
|x_2\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix} \quad
|x_3\rangle = \begin{pmatrix} 0 \\ 0 \\ 1 \\ \vdots \end{pmatrix}
$$

Each is a one-hot vector: "particle definitely at position $x_i$".

A general state: $|\psi\rangle = \sum_i c_i |x_i\rangle$ where $c_i = \psi(x_i)$ is the amplitude at position $x_i$.

Same idea as energy basis—just different labels!

### Make the Lattice Finer

Now make the spacing $\Delta x$ smaller and add more positions:
- N = 5 positions → coarse lattice
- N = 20 positions → finer lattice
- N = 100 positions → very fine lattice

As N increases:
- The column vector gets longer
- The coefficients $c_i$ become a function: $c_i \to \psi(x_i)$
- Normalization $\sum_i |\psi(x_i)|^2 = 1$ starts looking like area under a curve
- If we multiply by $\Delta x$: $\sum_i |\psi(x_i)|^2 \Delta x \approx \int |\psi(x)|^2 dx$

### The Continuous Limit

Let $\Delta x \to 0$ and $N \to \infty$. The discrete list becomes a smooth function:

$$\psi(x_i) \longrightarrow \psi(x)$$

**Thinking of states as column vectors:**

Discrete (N positions):
$$|\psi\rangle \longleftrightarrow \begin{pmatrix} \psi(x_1) \\ \psi(x_2) \\ \psi(x_3) \\ \vdots \\ \psi(x_N) \end{pmatrix}$$

Continuous limit (infinitely many positions):
$$|\psi\rangle \longleftrightarrow (..., \psi(x-\Delta x), \psi(x), \psi(x+\Delta x), ...)^T$$

**What about basis vectors?**

Discrete:
$$|x_i\rangle \longleftrightarrow (..., 0, 1 \text{ (at } x_i), 0, ...)^T$$

Continuous limit:
$$|x\rangle \longleftrightarrow (..., 0, 1 \text{ (at } x), 0, ...)^T$$

In the continuous limit, that "1 at position x" becomes a **delta function spike**: $|x\rangle \leftrightarrow \delta(x' - x)$

**One-line summary:** $|x\rangle$ is the continuous version of the one-hot basis vectors—it represents "particle definitely at position x".

---

## Position Basis: The Complete Machinery

Now let's see how everything from the discrete case carries over.

### Orthonormality

**Discrete:** $\langle x_i|x_j\rangle = \delta_{ij}$ (Kronecker delta)

**Continuous:** $\langle x'|x\rangle = \delta(x' - x)$ (Dirac delta)

The Kronecker delta becomes the Dirac delta—same idea, continuous version!

### Extracting the Wavefunction

**Discrete:** $c_i = \langle x_i|\psi\rangle$ extracts coefficient at position $x_i$

**Continuous:** $\boxed{\psi(x) = \langle x|\psi\rangle}$ extracts amplitude at position $x$

This is THE key equation! The wavefunction $\psi(x)$ is just the position coefficient function. You input a position, it tells you the amplitude there.

(Note: For complex states, $\psi(x) = \langle x|\psi\rangle = \langle\psi|x\rangle^*$, but when ψ is real-valued they're equal.)

### Building States

**Discrete:** $|\psi\rangle = \sum_i c_i |x_i\rangle$

**Continuous:** $|\psi\rangle = \int \psi(x)|x\rangle dx$

Same pattern! Sum becomes integral. We're adding up basis vectors weighted by amplitudes.

**Physical picture:** Each $|x\rangle$ is a delta spike at position x. The integral says "place amplitude $\psi(x)$ worth of spike at each position, then add them all up." You're building the state from infinitely many delta functions.

### The Delta Function Sifting Property

Why does $\langle x|\psi\rangle = \psi(x)$ work? The delta function "picks out" values:

$$\psi(x) = \langle x|\psi\rangle = \int \psi(x') \langle x|x'\rangle dx' = \int \psi(x') \delta(x - x') dx' = \psi(x)$$

The delta function $\delta(x - x')$ is zero everywhere except at $x' = x$, where it "sifts out" exactly $\psi(x)$.

### Normalization

**Discrete:** $\sum_i |c_i|^2 = 1$

**Continuous:** $\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1$

All probabilities must sum to 100%. In the continuous case, $|\psi(x)|^2 dx$ is the probability of finding the particle in interval $[x, x+dx]$.

---

## The Complete Parallel Structure

| **Concept** | **Discrete (Energy)** | **Continuous (Position)** |
|-------------|----------------------|---------------------------|
| **Basis labels** | $n = 0,1,2,...$ | $x \in \mathbb{R}$ |
| **Basis vectors** | One-hot columns $\vert n\rangle$ | Delta spikes $\vert x\rangle$ |
| **Coefficients** | $c_n = \langle n\vert\psi\rangle$ | $\psi(x) = \langle x\vert\psi\rangle$ |
| **Orthonormality** | $\langle m\vert n\rangle = \delta_{mn}$ | $\langle x'\vert x\rangle = \delta(x'-x)$ |
| **Build state** | $\vert\psi\rangle = \sum_n c_n\vert n\rangle$ | $\vert\psi\rangle = \int \psi(x)\vert x\rangle dx$ |
| **Normalization** | $\sum_n \vert c_n\vert^2 = 1$ | $\int \vert\psi(x)\vert^2 dx = 1$ |
| **Probability** | $P(E_n) = \vert c_n\vert^2$ | $P(x)dx = \vert\psi(x)\vert^2 dx$ |

Discrete sums $\sum$ become continuous integrals $\int$. Kronecker deltas $\delta_{mn}$ become Dirac deltas $\delta(x-x')$. Everything else is identical!

---

## Connecting to Our Running Example

Remember our state: $|\psi\rangle = \frac{1}{2}|0\rangle + \frac{\sqrt{2}}{2}|1\rangle + \frac{1}{2}|2\rangle$

In position space, this becomes:

$$\psi(x) = \frac{1}{2}\psi_0(x) + \frac{\sqrt{2}}{2}\psi_1(x) + \frac{1}{2}\psi_2(x)$$

where $\psi_0(x), \psi_1(x), \psi_2(x)$ are the Gaussian energy eigenfunctions from Part 1.

**Key insight:** We only use **three** energy basis vectors (the rest have $c_n = 0$). But in position basis, we need $\psi(x)$ defined for **every** x! Why?

Because each Gaussian energy eigenstate spreads over all space. When we add three Gaussians together, the result is non-zero almost everywhere. So in position basis, we need infinitely many values to describe what's happening.

It's like describing a diagonal line in 2D:
- **Rotated basis aligned with the line:** Just one coordinate
- **Standard xy basis:** Need both x and y everywhere

Different bases make different aspects simple or complicated. Our state is "simple" in energy basis (just 3 numbers) but "complicated" in position basis (function over all x).

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

## The Punchline

Quantum mechanics seems complicated because we're juggling multiple representations of the same thing. But once you see the pattern, it all becomes linear algebra:

### The Core Ideas

**1. The abstract state |ψ⟩ exists independent of how we describe it**
- Like a vector in 3D space that doesn't change whether you use Cartesian, cylindrical, or spherical coordinates
- The state itself is basis-independent—only our description changes

**2. Representations are projections**
- Energy coefficients: $c_n = \langle n|\psi\rangle$
- Position wavefunction: $\psi(x) = \langle x|\psi\rangle$
- Momentum wavefunction: $\tilde{\psi}(p) = \langle p|\psi\rangle$
- Same formula, different basis!

**3. Discrete and continuous follow identical patterns**
- Discrete: sums $\sum$, Kronecker delta $\delta_{mn}$, column vectors
- Continuous: integrals $\int$, Dirac delta $\delta(x-x')$, functions
- Everything else is the same—just different limiting cases

**4. Choose your basis to match what you want to measure**
- Want energy probabilities? Use energy basis: $P(E_n) = |c_n|^2$
- Want position probabilities? Use position basis: $P(x)dx = |\psi(x)|^2 dx$
- Each basis makes certain questions trivial and others complicated

**5. Time evolution is rotating phases in the energy basis**
- $c_n(t) = c_n(0)e^{-iE_n t/\hbar}$ (from Schrödinger's equation)
- Magnitudes stay constant → energy probabilities conserved
- Only relative phases change → interference creates dynamics
- Pure energy eigenstates are stationary; only superpositions evolve

### The Big Picture

The notation is half the battle. Once you see that:
- Ket notation $|n\rangle$ is just shorthand for column vectors
- The wavefunction $\psi(x)$ is the position coefficient function
- $\sum$ vs $\int$ is just discrete vs continuous
- Bra-ket $\langle\phi|\psi\rangle$ is just the dot product

...the mystery evaporates. Quantum mechanics is fundamentally **linear algebra in infinite dimensions**, with probabilities coming from squared magnitudes.

Start with what you know (column vectors, dot products, basis expansion), recognize the same pattern in continuous form (functions, integrals, delta functions), and you've understood the mathematical heart of quantum mechanics.

---

**Next up:** [Quantum Operators and Observables](quantum-operators.md) - How operators extract physical quantities, expectation values, and the uncertainty principle.

**Beyond that:** Spin-½ - Where everything fits in 2×2 matrices and the full power of quantum mechanics lives in four numbers!