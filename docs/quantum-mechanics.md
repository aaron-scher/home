# Quantum Mechanics

## Hand-Wavey Quick Derivation to Schrödinger's Equation

Let's start with a free particle (no potential, just moving in space) and work backwards to get Schrödinger's equation.

### de Broglie Relations (1924)

By the 1920s, light was known to have both wave and particle properties:
- Planck & Einstein showed photons have energy $E = h\nu$
- Compton scattering (1923) confirmed photons have momentum $p = h/\lambda$

**de Broglie's leap:** If light waves have particle properties, maybe particles have wave properties with the same relations?

For matter waves, we use:

$$
E = \hbar\omega, \quad p = \hbar k
$$

where $\hbar = h/2\pi$, $k$ is wave number, and $\omega$ is angular frequency. Electron diffraction experiments soon confirmed it.

### Free Particle Wave Function

A free particle moving in space can be described as a plane wave. We have two options:

1. **Real wave:** $A\cos(kx - \omega t)$
2. **Complex wave (phasor):** $A e^{i(kx - \omega t)}$

**Why use the complex form?**

- We know waves interfere (double slit experiment) - they add in and out of phase
- The cosine form can be written as a phasor using Euler's equation: $e^{i\theta} = \cos\theta + i\sin\theta$
- We need to calculate probability (which should always be positive, not oscillating between + and -)
- Complex form makes this easy: probability = $|\psi|^2 = \psi^* \psi$ (multiply by complex conjugate)

So we use:

$$
\psi(x,t) = A e^{i(kx - \omega t)}
$$

### Deriving Schrödinger's Equation

Now let's take derivatives and use the de Broglie relations to connect them.

**Time derivative:**

$$
\frac{\partial \psi}{\partial t} = -i\omega \psi
$$

Using $E = \hbar\omega$:

$$
\frac{\partial \psi}{\partial t} = -i\frac{E}{\hbar}\psi
$$

Multiply both sides by $i\hbar$:

$$
i\hbar \frac{\partial \psi}{\partial t} = E\psi
$$

**Spatial derivative (twice):**

$$
\frac{\partial^2 \psi}{\partial x^2} = (ik)^2 \psi = -k^2 \psi
$$

Using $p = \hbar k$:

$$
\frac{\partial^2 \psi}{\partial x^2} = -\frac{p^2}{\hbar^2}\psi
$$

Multiply both sides by $-\hbar^2/2m$:

$$
-\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2} = \frac{p^2}{2m}\psi
$$

**Setting them equal:**

For a free particle, classical mechanics says $E = p^2/2m$. So:

$$
E\psi = \frac{p^2}{2m}\psi
$$

Therefore our two derivative expressions must be equal:

$$
i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2}
$$

**That's Schrödinger's equation for a free particle!**

**What does this mean?** The time derivative extracts energy from the wave, the spatial derivative extracts kinetic energy (from momentum). For a free particle these are the same thing, so we get one equation. It's the quantum version of $E = p^2/2m$.

### Adding a Potential

If the particle is in a potential $V(x)$, total energy = KE + PE:

$$
i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2} + V(x)\psi
$$

Or more compactly:

$$
i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi
$$

where $\hat{H} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)$ is the Hamiltonian operator.

---

## Building Intuition: From Wave Packets to Stationary States

### Position and Momentum Space (Fourier Transform)

A single plane wave $e^{ikx}$ extends forever - not realistic for a localized particle.

**Real particles are wave packets.** Consider a state at fixed energy $E$. We've factored out the time part $e^{-iEt/\hbar}$, so we're looking at just the spatial part $\psi(x)$. Start simple - add a few plane waves with different momenta:

$$
\psi(x) = A_1 e^{ik_1 x} + A_2 e^{ik_2 x} + A_3 e^{ik_3 x} + \cdots
$$

Each $A_n$ tells you the amplitude and phase of momentum $k_n$. As a sum:

$$
\psi(x) = \sum_n A_n e^{ik_n x}
$$

Now take the limit: spacing between $k$ values → 0, sum → integral. The discrete amplitudes $A_n$ become a continuous function $\tilde{\psi}(k)$:

$$
\psi(x) = \int_{-\infty}^{\infty} \tilde{\psi}(k) e^{ikx} dk
$$

That's the **Fourier transform**. $\tilde{\psi}(k)$ tells you "how much of momentum $k$" is in your wave packet.

**Key insight:** You can't have both narrow at once.
- Narrow in position (localized) → wide spread in momentum
- Narrow in momentum (definite p) → spread out in space
- This is the **uncertainty principle**!

**Quick derivation:** From Fourier theory (like time-bandwidth product in signal processing), a wave packet localized to width $\Delta x$ needs a spread in $k$ of roughly $\Delta k \sim 1/\Delta x$. Since $p = \hbar k$, we have $\Delta p = \hbar \Delta k$, giving:

$$
\Delta x \cdot \Delta p \sim \hbar
$$

The rigorous proof (using the commutator $[\hat{x},\hat{p}] = i\hbar$) gives $\Delta x \cdot \Delta p \geq \hbar/2$.

### Time-Independent Schrödinger Equation

Now let's think about the **time derivative** in Schrödinger's equation.

From $i\hbar \frac{\partial \psi}{\partial t} = E\psi$, we see: higher energy → faster time oscillation.

For states with **definite energy** (energy eigenstates), we can separate variables:

$$
\psi(x,t) = \psi(x) e^{-iEt/\hbar}
$$

The time part is just a rotating phase $e^{-i\omega t}$ where $\omega = E/\hbar$. All the physics (probability, where the particle is) lives in $\psi(x)$.

Plug this back into Schrödinger's equation:

$$
i\hbar \frac{\partial}{\partial t}\left[\psi(x) e^{-iEt/\hbar}\right] = \hat{H}\left[\psi(x) e^{-iEt/\hbar}\right]
$$

The time derivative just brings down $-iE/\hbar$, which cancels the $i\hbar$, leaving:

$$
E\psi(x) = \hat{H}\psi(x)
$$

Or written out fully:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi
$$

**That's the time-independent Schrödinger equation.** It's an eigenvalue equation: find the functions $\psi(x)$ and energies $E$ that satisfy it.

### Intuition: Wiggliness vs Potential

Here's the key physical insight from the time-independent equation.

Start with the Schrödinger equation and **divide both sides by ψ**:

$$
-\frac{\hbar^2}{2m}\frac{\psi''}{\psi} = E - V(x)
$$

Now the physics is crystal clear:

**Left side:** The second derivative ψ'' measures how much the wavefunction curves. Dividing by ψ itself gives the **local kinetic energy**.

**Right side:** Since total energy E = KE + PE, we have KE = E - V(x).

**Why divide by ψ?** When you localize (squeeze) a wavefunction, two things happen: it gets taller (higher amplitude at the peak) and sharper (higher curvature). Dividing by ψ separates these effects — ψ''/ψ captures just the sharpness of the curve, independent of the overall height. This is what determines the kinetic energy.

**What this means:**

- **Low potential** (V small) → right side is large → ψ''/ψ is large → ψ is very wiggly
- **High potential** (V large) → right side is small → ψ''/ψ is small → ψ is less wiggly

The equation literally says: **the curvature of ψ (relative to its value) equals the local kinetic energy**!

When you solve for ψ(x), it automatically adjusts its wiggliness to match the kinetic energy at each point. In regions where potential is low, the wavefunction oscillates rapidly. Where potential is high, it oscillates slowly (or even decays exponentially if V > E).

---

## Why Can't a Particle Just Sit at the Bottom of a Well?

### Classical vs Quantum Ground State

**Classical intuition:** If you put a ball in a bowl (harmonic oscillator potential), the lowest energy state is the ball sitting still at the bottom. Total energy = 0.

**Quantum reality:** This doesn't work! Here's why.

If we try to localize the particle tightly at the bottom of the well (making ψ very narrow), the wavefunction has **high curvature**. From the Schrödinger equation divided by ψ:

$$
-\frac{\hbar^2}{2m}\frac{\psi''}{\psi} = E - V(x)
$$

Squeezing ψ narrow increases its curvature ($\psi''$), making the left side large. This means the kinetic energy $E - V(x)$ shoots up at the center, so $E(x) = \text{KE}(x) + V(x)$ is not constant — meaning it's **not a stationary state**.

### Finding the "Just Right" Width

Let's test three different Gaussian trial wavefunctions with different widths:

![Gaussian widths comparison](images/harmonic_oscillator_gaussians_1.png)

- **ψ₁ (narrow, red):** Sharp peak → high curvature at center → high KE
- **ψ₂ (medium, green):** "Just right" width — balances spread vs curvature
- **ψ₃ (wide, blue):** Flat peak → low curvature → low KE

Now let's check which one gives constant total energy $E(x) = \text{KE}(x) + V(x)$:

![Local energy comparison](images/harmonic_oscillator_gaussians_2.png)

- **E₁ (red):** Too much KE → $E(x)$ bulges at center (not constant!)
- **E₂ (green):** Nearly flat $E(x)$ → this is a **stationary state**!
- **E₃ (blue):** Not enough KE to balance the rising potential $V(x)$ → $E(x)$ varies

### The Zero-Point Energy

Only ψ₂ (the "just right" width) gives approximately constant $E(x)$ — this is the **ground state** of the harmonic oscillator. Notice:

1. The wavefunction **spreads out** (can't be localized to a point)
2. The particle has **kinetic energy even in the ground state**
3. For this specific potential ($V = \frac{1}{2}m\omega^2 x^2$), the minimum energy is $E_0 = \frac{1}{2}\hbar\omega$, **not zero**

This minimum energy is the **zero-point energy** — a purely quantum effect arising from the uncertainty principle. If you try to confine the particle too tightly (small Δx), its momentum uncertainty Δp increases, giving it kinetic energy. The ground state is the perfect balance between being localized enough to stay near the potential minimum, but spread out enough to avoid excessive kinetic energy.

**Key insight:** The time-independent Schrödinger equation is essentially saying "find the wavefunction shape where curvature (KE) and potential energy add up to the same constant everywhere." Only specific shapes (eigenstates) and energies (eigenvalues) work!

---

## The Harmonic Oscillator: Explicit Solutions

Now that we understand why the ground state can't be at the bottom, let's see the actual solutions for the harmonic oscillator potential $V(x) = \frac{1}{2}m\omega^2 x^2$.

### Energy Levels

The allowed energies are:

$$
E_n = \hbar\omega\left(n + \frac{1}{2}\right), \quad n = 0, 1, 2, ...
$$

Notice:
- **Evenly spaced** by ℏω (like a ladder!)
- **Ground state** (n=0): $E_0 = \frac{1}{2}\hbar\omega$ (the zero-point energy we saw)
- **First excited** (n=1): $E_1 = \frac{3}{2}\hbar\omega$
- **Second excited** (n=2): $E_2 = \frac{5}{2}\hbar\omega$

### The Wavefunctions in Position and Momentum Space

For convenience, define the natural length and momentum scales: $x_0 = \sqrt{\hbar/(m\omega)}$ and $p_0 = \sqrt{m\hbar\omega}$

**n=0 (Ground state): E₀ = ½ℏω**

Position space:

$$
\psi_0(x) = \left(\frac{1}{\pi x_0^2}\right)^{1/4} e^{-x^2/(2x_0^2)}
$$

Momentum space:

$$
\tilde{\psi}_0(p) = \left(\frac{1}{\pi p_0^2}\right)^{1/4} e^{-p^2/(2p_0^2)}
$$

Both Gaussians! Fourier transform of a Gaussian is a Gaussian. This is the "just right" width we found.

Notice something special: the ground state has width ~ x₀ in position space and width ~ p₀ in momentum space. If you calculate Δx·Δp, you get exactly ℏ/2 — the **minimum allowed** by the uncertainty principle! This is why it's the lowest energy state: it's spread out just enough to minimize both position and momentum uncertainty.

**n=1 (First excited): E₁ = 3/2ℏω**

Position space:

$$
\psi_1(x) = \left(\frac{1}{4\pi x_0^2}\right)^{1/4} \frac{2x}{x_0} e^{-x^2/(2x_0^2)}
$$

Momentum space:

$$
\tilde{\psi}_1(p) = \left(\frac{1}{4\pi p_0^2}\right)^{1/4} \frac{2p}{p_0} e^{-p^2/(2p_0^2)}
$$

One node at origin (antisymmetric). Same functional form in both spaces!

**n=2 (Second excited): E₂ = 5/2ℏω**

Position space:

$$
\psi_2(x) = \left(\frac{1}{16\pi x_0^2}\right)^{1/4} \left(\frac{4x^2}{x_0^2} - 2\right) e^{-x^2/(2x_0^2)}
$$

Momentum space:

$$
\tilde{\psi}_2(p) = \left(\frac{1}{16\pi p_0^2}\right)^{1/4} \left(\frac{4p^2}{p_0^2} - 2\right) e^{-p^2/(2p_0^2)}
$$

Two nodes (symmetric). Again, same functional form!

**Pattern:** Higher n → more nodes → more wiggly → higher energy. The harmonic oscillator has beautiful symmetry between position and momentum.

---

## One Wavefunction, Many Faces: Basis Decomposition

Quantum states can be expressed in different "coordinate systems" — just like a vector [3, 4] can be written in Cartesian (x,y) or polar (r,θ) coordinates. The key difference: some bases are **discrete** (like energy levels) and some are **continuous** (like position).

Let's see how the same math structure appears in both cases.

### Part 1: Energy Basis (Discrete) — Mixing Different Energies

Let's start with a concrete example and then show how Dirac notation is just compact shorthand for the same thing.

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

**In the position basis** (more complicated!):

To write this **same state** in position space, we need to know what each basis vector |n⟩ looks like as a function of x. These are:

$$
\psi_0(x) = \left(\frac{1}{\pi x_0^2}\right)^{1/4} e^{-x^2/(2x_0^2)} \quad \text{(what } |0\rangle \text{ looks like in position space)}
$$

$$
\psi_1(x) = \left(\frac{1}{4\pi x_0^2}\right)^{1/4} \frac{2x}{x_0} e^{-x^2/(2x_0^2)} \quad \text{(what } |1\rangle \text{ looks like)}
$$

$$
\psi_2(x) = \left(\frac{1}{16\pi x_0^2}\right)^{1/4} \left(\frac{4x^2}{x_0^2} - 2\right) e^{-x^2/(2x_0^2)} \quad \text{(what } |2\rangle \text{ looks like)}
$$

Now we can write our **same quantum state** in position coordinates:

$$
\psi(x,t) = c_0 \psi_0(x) e^{-iE_0 t/\hbar} + c_1 \psi_1(x) e^{-iE_1 t/\hbar} + c_2 \psi_2(x) e^{-iE_2 t/\hbar}
$$

**It's the same state!** We're just writing it in position coordinates instead of energy coordinates. The coefficients c₀, c₁, c₂ are the same, but now we're expressing each basis vector as a function ψₙ(x) instead of an abstract symbol |n⟩.

**Key point:** ψ₀(x), ψ₁(x), ψ₂(x) are NOT the state we're describing — they're the **coordinate axes** (basis functions) in position space. We're building our state by taking c₀ times the first axis, c₁ times the second axis, c₂ times the third axis, just like (3,4,5) = 3·x̂ + 4·ŷ + 5·ẑ in regular vectors.

**Why use different bases? It depends on what question you're asking!**

Here's the profound insight: You have ONE quantum state |ψ⟩, but different questions naturally lead you to express it in different coordinates:

- **Question:** "What's the probability the particle is between x = 1 and x = 2?"
  - **Natural basis:** Position! Use ψ(x) = c₀ψ₀(x) + c₁ψ₁(x) + c₂ψ₂(x)
  - **Answer:** $\int_1^2 |\psi(x)|^2 dx$

- **Question:** "What's the probability the particle has energy E₁?"
  - **Natural basis:** Energy! Use |ψ⟩ = c₀|0⟩ + c₁|1⟩ + c₂|2⟩
  - **Answer:** $|c_1|^2$

- **Question:** "What's the probability the particle has momentum p?"
  - **Natural basis:** Momentum! Use ψ̃(p) (Fourier transform of ψ(x))
  - **Answer:** $|\tilde{\psi}(p)|^2$

**Schrödinger's equation is "position-biased"** because it was originally written in position coordinates: $i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2} + V(x)\psi$. But the underlying physics (the quantum state |ψ⟩) is more fundamental — you can express it in whatever coordinates are most useful for the question you're asking!

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

### Understanding Quantum "Coordinates": The Big Picture

**What do "position space" and "energy basis" really mean?**

Here's the key idea: **you have a single quantum state (one "vector"), and you're just using different coordinate systems to describe it** — exactly like describing the same arrow in 3D space using Cartesian (x,y,z) vs spherical (r,θ,φ) coordinates. The arrow doesn't change, just the numbers you use to describe it!

**Classical vectors:** Components point in spatial directions

With a vector like $\vec{v} = (v_x, v_y, v_z)$, each component tells you "how much of the vector points in that direction" (x, y, or z).

**Quantum states:** Components point in "observable directions"

In quantum mechanics, **the "directions" are physical observables**:
- Energy basis: each component $c_n$ tells you "how much is in energy state n"
- Position basis: each value $\psi(x)$ tells you "how much is at position x"
- Momentum basis: each value $\tilde{\psi}(p)$ tells you "how much has momentum p"

**The "coordinates" in quantum mechanics are observables!** The quantum state is the same, but you're measuring it along different physical quantities (energy, position, momentum) instead of spatial directions.

**Functions are vectors with continuous indices**

Here's a profound insight: Think about a time signal f(t). At each time t, you have a number f(t). This **is a vector** — just with a continuous index instead of discrete entries! Since time is continuous, you can't write it as a finite list [f₁, f₂, f₃, ...], so you write it as a **function** f(t). Mathematically, it's the same as a vector in an infinite-dimensional **Hilbert space**.

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

- Energy basis: $c_n = \langle n | \psi \rangle$ extracts the n-th coefficient
- Position basis: $\psi(x) = \langle x | \psi \rangle$ extracts the amplitude at x

Same operation, just discrete vs continuous. This is why:
- Sums become integrals: $\sum_n \rightarrow \int dx$
- Inner products look the same: $\sum_n c_n^* d_n \rightarrow \int \psi^*(x)\phi(x) dx$

**What exactly is |n⟩ — vector or wavefunction?**

Both! The symbol $|n\rangle$ is **basis-independent** — it's the abstract quantum state. When expressed in different bases:

- In energy basis: $|1\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \end{pmatrix}$ (simple vector)
- In position basis: $|1\rangle \rightarrow \psi_1(x) = \left(\frac{1}{4\pi x_0^2}\right)^{1/4} \frac{2x}{x_0} e^{-x^2/(2x_0^2)}$ (function)

Like the number 3 written as "3" (decimal), "11" (binary), or "III" (Roman) — same thing, different notation!

**Our three-state superposition:**

In energy basis, $|\psi\rangle = c_0|0\rangle + c_1|1\rangle + c_2|2\rangle$ is just:

$$
|\psi\rangle = \begin{pmatrix} c_0 \\ c_1 \\ c_2 \\ \vdots \end{pmatrix}
$$

Each entry is the amplitude for that energy state.

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
