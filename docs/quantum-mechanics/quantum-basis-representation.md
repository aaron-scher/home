# Quantum Mechanics: Basis Representation

**Prerequisites:** This builds on [Quantum Foundations](quantum-foundations.md) where we derived Schrödinger's equation and explored the harmonic oscillator. If you haven't read that yet, start there first!

---

## One Wavefunction, Many Faces: Basis Decomposition

Quantum states can be expressed in different "coordinate systems" — just like a vector [3, 4] can be written in Cartesian (x,y) or polar (r,θ) coordinates. The key difference: some bases are **discrete** (like energy levels) and some are **continuous** (like position).

### Understanding Quantum "Coordinates": The Big Picture

Before diving into examples, let's understand what makes quantum mechanics different from classical physics.

**Classical vectors:** Components point in spatial directions

With a vector like $\vec{v} = (v_x, v_y, v_z)$, each component tells you "how much of the vector points in that direction" (x, y, or z).

**Quantum states:** Components point in "observable directions"

Here's the key idea: **you have a single quantum state (one "vector"), and you're just using different coordinate systems to describe it** — exactly like describing the same arrow in 3D space using Cartesian (x,y,z) vs spherical (r,θ,φ) coordinates. The arrow doesn't change, just the numbers you use to describe it!

In quantum mechanics, **the "directions" are physical observables**:
- Energy basis: each component $c_n$ tells you "how much is in energy state n"
- Position basis: each value $\psi(x)$ tells you "how much is at position x"
- Momentum basis: each value $\tilde{\psi}(p)$ tells you "how much has momentum p"

**The "coordinates" in quantum mechanics are observables!** The quantum state is the same, but you're measuring it along different physical quantities (energy, position, momentum) instead of spatial directions.

**Functions are vectors with continuous indices**

Here's a profound insight: Think about a time signal f(t). At each time t, you have a number f(t). This **is a vector** — just with a continuous index instead of discrete entries! Since time is continuous, you can't write it as a finite list [f₁, f₂, f₃, ...], so you write it as a **function** f(t).

**What is "Hilbert space"? (Don't let the name scare you!)**

Mathematically, we say these functions live in an infinite-dimensional **Hilbert space**. This sounds intimidating, but it's really just the name for "vector spaces that might have infinitely many dimensions." Named after David Hilbert (1862-1943), a German mathematician who studied the geometry of such spaces.

Here's the key idea: A regular vector space has finitely many basis vectors (like x̂, ŷ, ẑ in 3D). But functions need infinitely many "directions" because x is continuous. A Hilbert space is just a vector space equipped with:
1. An **inner product** (dot product generalized to functions: $\int \psi^*(x)\phi(x) dx$)
2. Possibly **infinite dimensions** (continuous indices)

That's it! It's the natural mathematical home for wavefunctions. Every rule you know about vectors (add them, take dot products, decompose into bases) works exactly the same way — you just use integrals instead of sums when dealing with continuous indices.

The name might sound fancy, but it's almost obvious once you think about it: if 3D vectors need a 3D vector space, then functions (with infinitely many "entries") need an infinite-dimensional vector space. Hilbert space is that space!

Apply this to quantum mechanics:

| Representation | "Index" | "Component" | Written as |
|----------------|---------|-------------|------------|
| **Energy basis** | n (discrete: 0, 1, 2, ...) | $c_n$ = "how much of energy n" | Discrete vector: $[c_0, c_1, c_2, ...]^T$ |
| **Position basis** | x (continuous: all real numbers) | $\psi(x)$ = "how much at position x" | Function: $\psi(x)$ |
| **Momentum basis** | p (continuous) | $\tilde{\psi}(p)$ = "how much with momentum p" | Function: $\tilde{\psi}(p)$ |

**Same quantum state |ψ⟩, different coordinate systems!**

This is profound: The quantum state itself doesn't change. It's an abstract "vector" living in Hilbert space. When you write it as [c₀, c₁, c₂, ...]ᵀ (energy basis) or ψ(x) (position basis), you're just picking different coordinates to describe the **same physical state** — like the same arrow described as (x,y,z) = (3,4,0) or (r,θ,φ) = (5, 53°, 0°).

**How do you transform between bases?**

The inner product does the work! To express the abstract state $|\psi\rangle$ in any basis, take the inner product with each basis vector:

- Energy basis: $c_n = \langle n | \psi \rangle$ extracts the amplitude for energy state n
- Position basis: $\psi(x) = \langle x | \psi \rangle$ extracts the amplitude at position x

Same operation, just discrete vs continuous. Both $c_n$ and $\psi(x)$ are **probability amplitudes** — square them to get probabilities: $|c_n|^2$ is the probability of energy $E_n$, and $|\psi(x)|^2$ is the probability density at position x. This is why:
- Sums become integrals: $\sum_n \rightarrow \int dx$
- Inner products look the same: $\sum_n c_n^* d_n \rightarrow \int \psi^*(x)\phi(x) dx$

**What exactly is |n⟩ — vector or wavefunction?**

Both! But first, **important notation clarification**: $|n\rangle$ means "the n-th ENERGY eigenstate" where n = 0, 1, 2, ... So |1⟩ is the **first excited energy state**, NOT the state at position x=1!

If we wanted to talk about a position eigenstate (a spike at a specific location), we'd write $|x\rangle$ where x is a position value. So $|x=1.5\rangle$ would be "the state localized at position x=1.5" (a delta function). Different notation!

Now, the symbol $|n\rangle$ (energy eigenstate) is **basis-independent** — it's the abstract quantum state. When expressed in different bases:

- In energy basis: $|1\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix}$ (simple vector - "first excited energy state")
- In position basis: $|1\rangle \rightarrow \psi_1(x)$ (function showing how that energy state is distributed in space)

Like the number 3 written as "3" (decimal), "11" (binary), or "III" (Roman) — same abstract thing, different notations!

---

### Part 1: Energy Basis (Discrete) — Mixing Different Energies

Now let's see a concrete example of how the same quantum state looks in different bases.

**Concrete example: ONE quantum state, TWO ways to write it**

Suppose we have a superposition state — a particle that's in a mix of three different energy levels. This is **ONE quantum state** that we can describe in two different coordinate systems:

**In the energy basis** (simple!):

$$
|\psi(t)\rangle = c_0 |0\rangle e^{-iE_0 t/\hbar} + c_1 |1\rangle e^{-iE_1 t/\hbar} + c_2 |2\rangle e^{-iE_2 t/\hbar}
$$

This says: "The state has amplitude c₀ for ground state |0⟩, amplitude c₁ for first excited |1⟩, and amplitude c₂ for second excited |2⟩." Each picks up its own time evolution phase.

**What do |0⟩, |1⟩, |2⟩ mean?** They're the **basis vectors** — the energy eigenstates of the harmonic oscillator with energies:
- Ground state |0⟩: $E_0 = \frac{1}{2}\hbar\omega$
- First excited |1⟩: $E_1 = \frac{3}{2}\hbar\omega$
- Second excited |2⟩: $E_2 = \frac{5}{2}\hbar\omega$

Think of them as the "x-axis", "y-axis", "z-axis" of this space, except instead of spatial directions, they represent pure energy states.

**Expressed in position space** (more complicated!):

**Important distinction:** We're still decomposing in the ENERGY basis (3 components: c₀, c₁, c₂), but now we're **expressing** each energy eigenstate as a function of position x. This is NOT the same as "using the position basis" (which would have infinitely many components - one for each x value)!

To express this state as a function of x, we need to know what each energy basis vector |n⟩ looks like in position space:

$$
\psi_0(x) = \left(\frac{1}{\pi x_0^2}\right)^{1/4} e^{-x^2/(2x_0^2)} \quad \text{(what } |0\rangle \text{ looks like in position space)}
$$

$$
\psi_1(x) = \left(\frac{1}{4\pi x_0^2}\right)^{1/4} \frac{2x}{x_0} e^{-x^2/(2x_0^2)} \quad \text{(what } |1\rangle \text{ looks like)}
$$

$$
\psi_2(x) = \left(\frac{1}{16\pi x_0^2}\right)^{1/4} \left(\frac{4x^2}{x_0^2} - 2\right) e^{-x^2/(2x_0^2)} \quad \text{(what } |2\rangle \text{ looks like)}
$$

**Wait - is |1⟩ a function of position?**

No! Let me be crystal clear:

- **|1⟩** is NOT a function of position. It's an **abstract state** — the first excited energy eigenstate. It has definite energy $E_1 = \frac{3}{2}\hbar\omega$, period.
- **ψ₁(x)** = ⟨x|1⟩ IS a function of position — it's the representation of |1⟩ in position space.

**Analogy:**
- "The number 5" is an abstract concept
- "5 in binary" = 101 (a specific representation)
- "5 in Roman numerals" = V (a different representation)

The number itself isn't "a function of notation" — it's just 5. Similarly:
- **|1⟩** is just "the first excited state" (abstract, basis-independent)
- **ψ₁(x)** is "how that state looks when expressed as a function of position"

**Why does it become a function?**

Because we're asking: "For every position x, what's the amplitude of |1⟩ at that position?" That's infinitely many questions (one for each x), so the answer is a continuous function ψ₁(x).

The state |1⟩ doesn't "know" about x — it's just a state with definite energy $E_1$. But because quantum mechanics allows states to be spread out in space, when you ask "where is this energy state located?", the answer is "everywhere, but with amplitude ψ₁(x) at each point x."

**Mathematical detail: How does ⟨x|1⟩ actually work?**

Here's the intuitive picture — it's just a projection (dot product)!

**Position space has infinitely many basis vectors** — one impulse |x⟩ for each position x. These are all linearly independent (think delta functions at different positions).

When you compute ⟨x|1⟩, you're **projecting** the state |1⟩ onto the basis vector |x⟩. This tells you "how much of |1⟩ has at position x" — it pulls out a number!

Since you can do this projection for **every** x, you get infinitely many numbers — one for each position. Instead of writing them as an infinite list, we write them as a **function**: ψ₁(x).

**The analogy to 3D:**
- In 3D: **v** · x̂ projects onto x-axis → gives one number (the x-component)
- In quantum: ⟨x|ψ⟩ projects onto position x → gives one number for each x → written as ψ(x)

**The big picture:**
- **⟨n|ψ⟩** projects onto energy basis vector n → gives c_n (discrete: 3 numbers)
- **⟨x|ψ⟩** projects onto position basis vector x → gives ψ(x) (continuous: infinitely many numbers)
- Same operation (projection), just discrete vs continuous indices!

Now we can write our **same quantum state** as a function of x:

$$
\psi(x,t) = c_0 \psi_0(x) e^{-iE_0 t/\hbar} + c_1 \psi_1(x) e^{-iE_1 t/\hbar} + c_2 \psi_2(x) e^{-iE_2 t/\hbar}
$$

**It's the same state!** Still using the energy basis (3 components c₀, c₁, c₂), but now each energy eigenstate is written as a function of x. The true "position basis" decomposition would be: $|\psi\rangle = \int \psi(x) |x\rangle dx$ — infinitely many components ψ(x), one for each position x!

**Key point:** ψ₀(x), ψ₁(x), ψ₂(x) are NOT the state we're describing — they're the **energy basis vectors expressed as functions of x**. We're building our state by taking c₀ times the first energy state, c₁ times the second, c₂ times the third, just like (3,4,5) = 3·x̂ + 4·ŷ + 5·ẑ in regular vectors. The result ψ(x,t) gives us the amplitude at each position x.

**Why use different bases? It depends on what question you're asking!**

Here's the profound insight: You have ONE quantum state |ψ⟩, but different questions naturally lead you to express it in different coordinates:

- **Question:** "What's the probability the particle is between x = 1 and x = 2?"
  - **Natural basis:** Position! Use ψ(x) = c₀ψ₀(x) + c₁ψ₁(x) + c₂ψ₂(x)
  - **Answer:** $\int_1^2 |\psi(x)|^2 dx$

- **Question:** "What's the probability the particle has energy E₁?"
  - **Natural basis:** Energy! Use |ψ⟩ = c₀|0⟩ + c₁|1⟩ + c₂|2⟩
  - **Answer:** $|c_1|^2$

- **Question:** "What's the probability the particle has momentum between p = p₁ and p = p₂?"
  - **Natural basis:** Momentum! Use ψ̃(p) (Fourier transform of ψ(x))
  - **Answer:** $\int_{p_1}^{p_2} |\tilde{\psi}(p)|^2 dp$

**Schrödinger's equation looks different in different bases!**

The usual form you see is "position-biased" because it's written in position coordinates:

$$
i\hbar\frac{\partial\psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi(x,t)}{\partial x^2} + V(x)\psi(x,t)
$$

But you can write Schrödinger's equation in **any basis**:

**Energy basis** (super simple!):

$$
i\hbar\frac{dc_n(t)}{dt} = E_n c_n(t)
$$

Solution: $c_n(t) = c_n(0) e^{-iE_n t/\hbar}$ — just a rotating phase!

**Momentum basis**:

$$
i\hbar\frac{\partial\tilde{\psi}(p,t)}{\partial t} = \frac{p^2}{2m}\tilde{\psi}(p,t) + \tilde{V}(p)\tilde{\psi}(p,t)
$$

(Kinetic energy is simple, potential is complicated - opposite of position space!)

**Basis-independent form** (the most fundamental!):

$$
i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle = \hat{H}|\psi(t)\rangle
$$

This is the "true" Schrödinger equation — it doesn't care about what basis you use! The abstract quantum state |ψ(t)⟩ is more fundamental than any particular representation ψ(x,t) or c_n(t).

**The state "rotates" in Hilbert space with time**

Here's a beautiful way to think about time evolution: The quantum state |ψ(t)⟩ is a vector in an infinite-dimensional Hilbert space. As time passes, this vector **rotates**!

In the energy basis, each component c_n picks up a phase $e^{-iE_n t/\hbar}$. Since different energy components rotate at different rates, the overall state vector traces out a complicated path through Hilbert space — kind of like a vector in 3D space rotating, but in infinitely many dimensions!

For a single energy eigenstate, the "rotation" is simple — just one component spinning at frequency ω = E/ℏ. For superpositions, different components beat against each other, creating the oscillating probability densities we see.

---

### The SAME State, THREE Ways to Write It

Let's focus on t=0 to see the connection clearly. We have **ONE quantum state |ψ⟩**. Here it is in three different coordinate systems:

**1. Energy basis** (discrete vector - 3 components):

$$
|\psi\rangle = \begin{pmatrix} c_0 \\ c_1 \\ c_2 \end{pmatrix}
$$

Each entry tells you "how much of energy state n." This is a discrete, finite list of numbers.

**2. Position basis** (continuous vector - infinite components):

$$
\psi(x) = c_0 \psi_0(x) + c_1 \psi_1(x) + c_2 \psi_2(x)
$$

At each position x, you get a number ψ(x). This is a **continuous vector** — the function ψ(x) IS a vector with x as the continuous index! You can think of it as:

$$
\psi = \begin{pmatrix} \vdots \\ \psi(x_1) \\ \psi(x_2) \\ \psi(x_3) \\ \vdots \end{pmatrix} \leftarrow \text{infinite entries, one for each } x
$$

Too many entries to write as a list, so we write it as a function ψ(x).

**3. Momentum basis** (continuous vector - infinite components):

$$
\tilde{\psi}(p) = \text{Fourier transform of } \psi(x)
$$

Same state, now telling you "how much momentum p" at each value of p. Also a continuous vector, written as a function.

**They're all the same quantum state!** Just like how the vector **v** with magnitude 5 pointing northeast can be written as:
- Cartesian: (3, 4)
- Polar: (5, 53°)
- Different numbers, same arrow!

The table at the end of this section shows exactly how these representations relate to each other.

---

**What about at t=0?**

At time $t=0$, the phase factors all equal 1 (since $e^{-i \cdot 0} = 1$), so the state simplifies to:

$$
|\psi(0)\rangle = c_0|0\rangle + c_1|1\rangle + c_2|2\rangle
$$

**Notation convention:** When we write $|\psi\rangle$ without a time argument, we typically mean **the state at t=0**. This is useful because the coefficients $c_n$ are constants — they don't change with time! Only the phases $e^{-iE_n t/\hbar}$ evolve. So when discussing properties that don't depend on time (like "what is the probability of measuring energy $E_1$?"), we just write $|\psi\rangle$ to mean the initial state.

---

### Working in the Energy Basis

**Example: Extracting a component with the inner product**

How do we extract, say, $c_1$ (the coefficient of the first excited state)? Use the inner product $c_1 = \langle 1|\psi\rangle$.

In vector language, $\langle 1|$ is a **row vector** — the complex conjugate transpose of $|1\rangle$:

$$
|1\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix} \quad \Rightarrow \quad \langle 1| = \begin{pmatrix} 0 & 1 & 0 & \cdots \end{pmatrix}
$$

Now "sandwich" $|\psi\rangle$ with $\langle 1|$ (just standard matrix multiplication: row times column):

$$
c_1 = \langle 1|\psi\rangle = \begin{pmatrix} 0 & 1 & 0 & \cdots \end{pmatrix} \begin{pmatrix} c_0 \\ c_1 \\ c_2 \\ \vdots \end{pmatrix} = 0 \cdot c_0 + 1 \cdot c_1 + 0 \cdot c_2 + \cdots = c_1
$$

It picks out the second entry! This works because the eigenstates are **orthonormal**: $\langle m|n\rangle = \delta_{mn}$ (Kronecker delta: 1 if m=n, 0 otherwise). The inner product with $\langle 1|$ zeros out all components except the one you want.

**Calculating probabilities (discrete sums):**

The probability of measuring energy $E_n$ is $|c_n|^2$. For our three-state example:
- Probability of measuring $E_0$: $|c_0|^2$
- Probability of measuring $E_1$: $|c_1|^2$
- Probability of measuring $E_2$: $|c_2|^2$

Want the probability of finding the particle in one of the lowest two energy states?

$$
P(E_0 \text{ or } E_1) = |c_0|^2 + |c_1|^2
$$

Just add up the individual probabilities — a discrete sum over the states you care about!

**Normalization:** Since the particle must be in *some* energy state, the probabilities must sum to 1:

$$
|c_0|^2 + |c_1|^2 + |c_2|^2 + \cdots = \sum_n |c_n|^2 = 1
$$

This is the **normalization condition** — the total probability is always 1.

**Extracting expectation values with operators:**

**Why this formula?** You might wonder: where does $\langle E \rangle = \langle \psi | \hat{H} | \psi \rangle$ come from? Why the "sandwich" notation?

Think about **classical expectation values**. If you roll a weighted die with probabilities $P_1, P_2, ..., P_6$ of getting each face, the average value is:

$$
\langle \text{value} \rangle = 1 \cdot P_1 + 2 \cdot P_2 + \cdots + 6 \cdot P_6 = \sum_n n \cdot P_n
$$

It's a **weighted average**: each outcome times its probability.

In quantum mechanics, we have the state $|\psi\rangle = \sum_n c_n |n\rangle$, and we know the probability of measuring energy $E_n$ is $|c_n|^2$. So by analogy:

$$
\langle E \rangle = E_0 |c_0|^2 + E_1 |c_1|^2 + E_2 |c_2|^2 + \cdots = \sum_n E_n |c_n|^2
$$

**But here's the quantum twist:** Instead of writing this out manually, we use **operators** to automatically extract the right observable. The formula $\langle \psi | \hat{H} | \psi \rangle$ is the quantum mechanics way of computing this weighted average. It's actually a **postulate** of quantum mechanics:

> **To measure the average value of an observable $A$, apply its operator $\hat{A}$ to the state and take the inner product: $\langle A \rangle = \langle \psi | \hat{A} | \psi \rangle$**

The magic is that this formula works for *any* observable — energy, position, momentum, etc. Let's verify it gives the right answer:

**Where does this formula come from?** Let's derive it from the Schrödinger equation and see why it works.

**Quick reminder: What is $\hat{H}$?**

The Hamiltonian $\hat{H}$ is the **energy operator**. It's the quantum version of the total energy (kinetic + potential):

$$
\hat{H} = \underbrace{-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}}_{\text{kinetic energy}} + \underbrace{V(x)}_{\text{potential energy}}
$$

Remember from earlier: the time-independent Schrödinger equation is $\hat{H}\psi = E\psi$ (an eigenvalue equation). When $\hat{H}$ acts on an energy eigenstate $|n\rangle$, it simply returns the energy of that state:

$$
\hat{H}|n\rangle = E_n|n\rangle
$$

This is what makes $|n\rangle$ an *energy* eigenstate — applying the energy operator gives you back the energy value $E_n$ times the state.

**The Hamiltonian also governs time evolution** through the full Schrödinger equation: $i\hbar \frac{\partial}{\partial t}|\psi\rangle = \hat{H}|\psi\rangle$. This says: "the rate of change of the state is determined by its energy." That's why states with higher energy oscillate faster in time!

**Deriving the expectation value:**

Start with the superposition:

$$
|\psi\rangle = \sum_n c_n |n\rangle
$$

Now apply $\hat{H}$ to this state. Use the eigenvalue equation $\hat{H}|n\rangle = E_n|n\rangle$:

$$
\hat{H}|\psi\rangle = \hat{H}\left(\sum_n c_n |n\rangle\right) = \sum_n c_n \hat{H}|n\rangle = \sum_n c_n E_n |n\rangle
$$

Now take the inner product with $\langle\psi| = \sum_m c_m^* \langle m|$:

$$
\langle E \rangle = \langle \psi | \hat{H} | \psi \rangle = \sum_{m,n} c_m^* c_n E_n \langle m|n\rangle
$$

Use orthonormality $\langle m|n\rangle = \delta_{mn}$ (equals 1 if m=n, 0 otherwise). This kills all terms except when m=n:

$$
\langle E \rangle = \sum_n c_n^* c_n E_n = \sum_n |c_n|^2 E_n
$$

**Physical interpretation:** Each term $|c_n|^2 E_n$ is "probability of being in state n" times "energy of state n". The average energy is the weighted sum of all possible energies!

In this basis, $\hat{H}$ is **trivial** — it's a diagonal matrix that just multiplies each component by its energy:

$$
\hat{H} = \begin{pmatrix} E_0 & 0 & 0 & \cdots \\ 0 & E_1 & 0 & \cdots \\ 0 & 0 & E_2 & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}
$$

**Where does this come from?** Remember the time-independent Schrödinger equation: $\hat{H}|\psi\rangle = E|\psi\rangle$. For an energy eigenstate $|n\rangle$, by definition:

$$
\hat{H}|n\rangle = E_n|n\rangle
$$

The Hamiltonian acting on $|n\rangle$ just gives you back $E_n$ times $|n\rangle$ — that's what makes it an eigenstate! When you write this in the energy eigenbasis, $\hat{H}$ becomes diagonal because each basis vector gets multiplied by its own eigenvalue. Off-diagonal elements are zero because eigenstates are orthogonal.

What about the average position? Same idea — we use the **position operator** $\hat{x}$:

$$
\langle x \rangle = \langle \psi | \hat{x} | \psi \rangle = \sum_{m,n} c_m^* c_n \langle m|\hat{x}|n\rangle
$$

**Why is this harder?** In the energy basis, we have $c_0, c_1, c_2, ...$ but these don't directly tell us about position. To find the average position, we need to know how each energy state is distributed in space — that's what the **matrix elements** $\langle m|\hat{x}|n\rangle$ encode. They tell you "how much overlap in position space do states $|m\rangle$ and $|n\rangle$ have?"

The position operator is **non-diagonal** in the energy basis — it mixes different energy states together. This is hard to compute! (Later we'll see it's trivial in the position basis.)

**Time evolution:**

Remember we started with the full time-dependent state:

$$
|\psi(t)\rangle = c_0 |0\rangle e^{-iE_0 t/\hbar} + c_1 |1\rangle e^{-iE_1 t/\hbar} + c_2 |2\rangle e^{-iE_2 t/\hbar}
$$

**Important clarification:** The coefficients $c_0, c_1, c_2$ themselves are **constants** — they don't change with time! What changes is the **phase** of each energy component.

Each energy eigenstate $|n\rangle$ picks up a rotating phase factor $e^{-iE_n t/\hbar}$. Since different energies rotate at different frequencies, the phases evolve at different rates:
- Ground state phase: $e^{-iE_0 t/\hbar} = e^{-i\omega t/2}$ (slowest)
- First excited phase: $e^{-iE_1 t/\hbar} = e^{-i3\omega t/2}$ (faster)
- Second excited phase: $e^{-iE_2 t/\hbar} = e^{-i5\omega t/2}$ (fastest)

This causes the probability density $|\psi(x,t)|^2$ to **oscillate in time** — the wavefunction sloshes back and forth because different energies beat against each other.

**Key point:** The "amount" of each energy (the $|c_n|^2$ probabilities) never changes — energy is conserved! Only the relative phases between the different energy components change.

### Part 2: Position Basis (Continuous) — One Energy, Different View

Now take a **single energy eigenstate** — say the first excited state $|n=1\rangle$ with definite energy $E_1 = \frac{3}{2}\hbar\omega$.

In the energy basis, this is simple: $|\psi\rangle = |1\rangle$, or $c_0 = 0, c_1 = 1, c_2 = 0, ...$

But we can decompose **this same state** in the **position basis**. Think of it as a continuous sum over all positions:

$$
|\psi\rangle = \int \psi(x) |x\rangle dx
$$

where $\psi(x) = \langle x|\psi\rangle$ is the "amplitude at position x". For the first excited state:

$$
\psi_1(x) = \left(\frac{1}{4\pi x_0^2}\right)^{1/4} \frac{2x}{x_0} e^{-x^2/(2x_0^2)}
$$

**Physical picture:** Think of $|x\rangle$ as an "impulse" (delta function) localized at position x. The wavefunction $\psi(x)$ tells you "how much of each impulse" to mix together. It's like a continuous weighted sum of impulses — analogous to convolution!

**Calculating probabilities (continuous sums/integrals):**

The probability density at position x is $|\psi(x)|^2$. Want the probability of finding the particle between x = 0 and x = $x_0$?

$$
P(0 \leq x \leq x_0) = \int_0^{x_0} |\psi(x)|^2 dx
$$

Integrate the probability density — a continuous sum over the region you care about! This is the continuous analog of $|c_0|^2 + |c_1|^2$.

**Normalization:** Since the particle must be *somewhere*, the total probability must equal 1:

$$
\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1
$$

This is the continuous version of $\sum_n |c_n|^2 = 1$ — same idea, integral instead of sum!

**Extracting expectation values with operators:**

To get the average position, use the position operator $\hat{x}$:

$$
\langle x \rangle = \langle \psi | \hat{x} | \psi \rangle = \int x |\psi(x)|^2 dx
$$

In this basis, $\hat{x}$ is **trivial** — it just multiplies by x. Super easy!

What about the average energy? Apply the Hamiltonian:

$$
\langle E \rangle = \langle \psi | \hat{H} | \psi \rangle = \int \psi^*(x) \left[-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)\right] \psi(x) dx
$$

Since $\psi_1(x)$ is an energy eigenstate, this just gives $E_1$ back. But notice: $\hat{H}$ is **complicated** here — it's a differential operator!

What about momentum? Use $\hat{p} = -i\hbar \frac{\partial}{\partial x}$:

$$
\langle p \rangle = \int \psi^*(x) \left(-i\hbar \frac{\partial}{\partial x}\right) \psi(x) dx
$$

For this symmetric state, $\langle p \rangle = 0$ (particle moves left and right equally).

**Time evolution:**

Since this is an energy eigenstate, $\psi(x,t) = \psi(x) e^{-iE_1 t/\hbar}$. The probability density $|\psi(x,t)|^2 = |\psi(x)|^2$ is **constant in time** — stationary state!

### The Parallel Structure

Notice the pattern:

| Concept | Energy Basis (Discrete) | Position Basis (Continuous) |
|---------|-------------------------|----------------------------|
| **State components** | $c_n = \langle n\|\psi\rangle$ (numbers) | $\psi(x) = \langle x\|\psi\rangle$ (function) |
| **Combine components** | $\sum_n$ (discrete sum) | $\int dx$ (continuous sum) |
| **Probability** | $\|c_n\|^2$ | $\|\psi(x)\|^2$ (density) |
| **Sum probabilities** | $\sum_n \|c_n\|^2 = 1$ | $\int \|\psi(x)\|^2 dx = 1$ |
| **Easy operator** | $\hat{H}$ (diagonal matrix) | $\hat{x}$ (multiply by x) |
| **Hard operator** | $\hat{x}$ (off-diagonal matrix) | $\hat{H}$ (differential) |

**Key insight:** Discrete sums become integrals, but the structure is identical. Energy basis is finite-dimensional linear algebra; position basis is infinite-dimensional, but same rules!

### Why Eigenstates Are Special

Here's the bottom line: **eigenstates form a complete orthogonal basis**. This means:

1. **Any state can be decomposed** into eigenstates (they're linearly independent and span the space)
2. **Eigenstates are orthogonal:** $\langle m|n\rangle = \delta_{mn}$ (0 if m≠n, 1 if m=n)
3. **This makes probabilities simple:** Because of orthogonality, $\sum_n |c_n|^2 = 1$ automatically
4. **Operators act simply on their eigenstates:** $\hat{H}|n\rangle = E_n|n\rangle$ — just multiply by eigenvalue!

When you measure an observable, you're asking "which eigenstate am I in?" The decomposition $|\psi\rangle = \sum_n c_n |n\rangle$ tells you the probability amplitudes. The orthogonality means these probabilities don't interfere — they just add like classical probabilities.

**This is why Dirac notation is so powerful!**

### Introducing Dirac Notation

We've been using this |ψ⟩ notation (called a "ket"). Here's the formal picture:

**Ket |ψ⟩:** An abstract quantum state (independent of basis)

**Bra ⟨φ|:** The dual vector (complex conjugate transpose for inner products)

**Inner product ⟨φ|ψ⟩:** Overlap between states (gives a complex number)

The key insight: $c_n = \langle n|\psi\rangle$ extracts the component of $|\psi\rangle$ along $|n\rangle$.

**In the energy basis:**
- $|\psi\rangle$ is a column vector $[c_0, c_1, c_2, ...]^T$
- $\langle n|\psi\rangle = c_n$ (the n-th component)
- $\langle \psi|\phi\rangle = \sum_n c_n^* d_n$ (inner product)

**In the position basis:**
- $|\psi\rangle$ becomes the function $\psi(x)$
- $\langle x|\psi\rangle = \psi(x)$ (amplitude at position x)
- $\langle \psi|\phi\rangle = \int \psi^*(x)\phi(x) dx$ (inner product)

**Operators in Dirac notation:**

Expectation value: $\langle \hat{A} \rangle = \langle \psi | \hat{A} | \psi \rangle$

Matrix element: $\langle m|\hat{A}|n\rangle$ is the (m,n) entry of the operator's matrix representation

**Why use this notation?**
- **Basis-independent:** $|\psi\rangle$ is the same abstract state whether you write it as $c_n$ or $\psi(x)$
- **Clean formulas:** The same expression works in any basis — just change what $\langle \cdot | \cdot \rangle$ means!
- **Matrices emerge naturally:** In a discrete basis, everything is linear algebra

### The Bridge to Matrix Mechanics

In a finite-dimensional space (like spin-½, or truncating to the first N energy levels), everything becomes concrete linear algebra:

**States** → column vectors:

$$
|\psi\rangle = \begin{pmatrix} c_0 \\ c_1 \\ c_2 \\ \vdots \end{pmatrix}
$$

**Operators** → matrices. The Hamiltonian in the energy basis is diagonal:

$$
\hat{H} = \begin{pmatrix} E_0 & 0 & 0 & \cdots \\ 0 & E_1 & 0 & \cdots \\ 0 & 0 & E_2 & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}
$$

**Eigenvalue equation:** $\hat{H}|\psi\rangle = E|\psi\rangle$ becomes $H\mathbf{c} = E\mathbf{c}$ (standard matrix eigenvalue problem)

**Time evolution:** The Schrödinger equation becomes a matrix exponential:

$$
|\psi(t)\rangle = e^{-i\hat{H}t/\hbar}|\psi(0)\rangle
$$

For a diagonal $\hat{H}$, this just rotates each component: $c_n(t) = e^{-iE_n t/\hbar} c_n(0)$.

**The punchline:** The continuous wavefunctions $\psi(x)$ we've been working with are the **infinite-dimensional limit** of this finite-dimensional picture. Same mathematical structure — eigenstates, operators, inner products — just with integrals instead of sums!

---

*Next up: We'll explore the simplest quantum system — spin-1/2 — where everything is 2×2 matrices, and all of quantum mechanics fits in a tiny box. This is the foundation of qubits and quantum computing.*
