# Multi-Particle Quantum Mechanics and Entanglement

**Prerequisites:** This builds on [Quantum Foundations](quantum-foundations.md), [Basis Representation](quantum-basis-representation.md), and [Operators](quantum-operators.md). Make sure you're comfortable with single-particle wavefunctions, superposition, and measurement before diving in!

---

## From One to Two: Extending the Wavefunction

Everything we've learned so far described **one particle**. The wavefunction $\psi(x,t)$ told us the amplitude for finding that particle at position $x$ at time $t$.

**What happens with two particles?**

The wavefunction becomes a function of **both positions**:

$$
\psi(x_1, x_2, t)
$$

This is a fundamentally different beast! Here's what it means:

- $x_1$ = position of particle 1
- $x_2$ = position of particle 2
- $\psi(x_1, x_2, t)$ = amplitude for finding particle 1 at $x_1$ **AND** particle 2 at $x_2$ simultaneously

### Probability Interpretation: Joint Probability

$$
P(x_1, x_2) = |\psi(x_1, x_2)|^2 dx_1 dx_2
$$

This is the probability of finding particle 1 **at** $x_1$ **AND** particle 2 **at** $x_2$ at the same time.

**Important:** The probability at any single point is vanishingly small (technically zero for continuous distributions). In practice, you **integrate over a region** to find the probability that particle 1 is in some interval and particle 2 is in some interval.

**Analogy - Rolling Two Dice:**

Think of rolling a red die and a blue die. The outcome is a **pair of numbers**: (red=3, blue=5).

**One die:** Probability $P(\text{red}=3)$ tells you about just the red die
**Two dice (joint):** Probability $P(\text{red}=3 \text{ AND blue}=5)$ tells you about **both** outcomes together

For quantum mechanics:

- **One particle:** $|\psi(x)|^2dx$ = probability particle is at position $x$
- **Two particles (joint):** $|\psi(x_1,x_2)|^2dx_1dx_2$ = probability particle 1 at $x_1$ **AND** particle 2 at $x_2$

**Key insight:** This is a **joint probability distribution**. The wavefunction doesn't just tell you about each particle separately; it encodes correlations between them!

Just like knowing the red die rolled 3 might affect what the blue die shows (if the dice are rigged together), knowing where particle 1 is can affect where particle 2 is likely to be!

### The Dimension Explosion

With one particle in 1D, $\psi(x)$ is a function of 1 variable. With two particles:

• Two particles in 1D: $\psi(x_1, x_2)$ (function of **2 variables**)

• Two particles in 3D: $\psi(\vec{r}_1, \vec{r}_2)$ (function of **6 variables**)

• Three particles in 3D: $\psi(\vec{r}_1, \vec{r}_2, \vec{r}_3)$ (function of **9 variables**)

The complexity grows explosively! This is why quantum chemistry is so computationally hard.

### Normalization: Why Does It Equal 1?

**One particle:** The particle must be **somewhere**, so:

$$
\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1
$$

Add up probabilities over all possible positions → get 100%.

**Two particles:** The **system** must exist in **some configuration**, so:

$$
\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} |\psi(x_1, x_2)|^2 dx_1 dx_2 = 1
$$

**What does this mean? The double integral sums over ALL possible configurations.**

A **configuration** is a pair of positions: (particle 1 here, particle 2 there).

**Concrete example:** Imagine two particles constrained to a discrete grid with just 3 positions: x = 0, 1, 2.

Possible configurations (9 total):

1. Both at 0: $(x_1=0, x_2=0)$
2. Particle 1 at 0, particle 2 at 1: $(x_1=0, x_2=1)$
3. Particle 1 at 0, particle 2 at 2: $(x_1=0, x_2=2)$
4. Particle 1 at 1, particle 2 at 0: $(x_1=1, x_2=0)$
5. Both at 1: $(x_1=1, x_2=1)$
6. Particle 1 at 1, particle 2 at 2: $(x_1=1, x_2=2)$
7. Particle 1 at 2, particle 2 at 0: $(x_1=2, x_2=0)$
8. Particle 1 at 2, particle 2 at 1: $(x_1=2, x_2=1)$
9. Both at 2: $(x_1=2, x_2=2)$

**Normalization says:** Add probabilities for all 9 configurations → must equal 1 (100%).

$$
\sum_{x_1=0}^{2} \sum_{x_2=0}^{2} |\psi(x_1, x_2)|^2 = 1
$$

The system is **definitely** in one of these 9 configurations!

**Continuous case:** Same idea, but infinitely many positions. The double integral adds up probabilities for **every pair** $(x_1, x_2)$:

- Particle 1 anywhere from $-\infty$ to $+\infty$
- Particle 2 anywhere from $-\infty$ to $+\infty$
- Total configurations: infinitely many

The system must be in **some** configuration, so total probability = 1.

**Key point:** It's not "particle 1 must be somewhere" AND separately "particle 2 must be somewhere." It's "the **two-particle system** must be in **some configuration**" (and a configuration is a pair $(x_1, x_2)$ specifying where **both** particles are simultaneously).

---

## Independent Particles: Product States

Let's start with the simplest case: **two particles that don't interact**.

### The Setup

Suppose we have:

- Particle 1 in state $\psi_a(x_1)$
- Particle 2 in state $\psi_b(x_2)$
- No interaction between them

The two-particle wavefunction is just the **product**:

$$
\psi(x_1, x_2) = \psi_a(x_1) \psi_b(x_2)
$$

This is called a **separable** or **product state**.

**Physical meaning:** The particles are completely independent. The probability of finding particle 1 at $x_1$ doesn't depend on where particle 2 is:

$$
|\psi(x_1, x_2)|^2 = |\psi_a(x_1)|^2 \cdot |\psi_b(x_2)|^2
$$

The joint probability **factorizes** (exactly like independent random variables in probability theory)!

### Schrödinger's Equation for Two Particles

The Hamiltonian for two non-interacting particles is:

$$
\hat{H} = \underbrace{\hat{H}_1}_{\text{particle 1}} + \underbrace{\hat{H}_2}_{\text{particle 2}}
$$

where each $\hat{H}_i = -\frac{\hbar^2}{2m_i}\frac{\partial^2}{\partial x_i^2} + V_i(x_i)$.

For a product state $\psi(x_1, x_2) = \psi_a(x_1)\psi_b(x_2)$, let's apply the Hamiltonian:

$$
\hat{H}\psi = \hat{H}_1[\psi_a(x_1)\psi_b(x_2)] + \hat{H}_2[\psi_a(x_1)\psi_b(x_2)]
$$

The key: $\hat{H}_1$ only acts on $x_1$ (treats $\psi_b(x_2)$ as a constant), and $\hat{H}_2$ only acts on $x_2$:

$$
= \psi_b(x_2) \hat{H}_1\psi_a(x_1) + \psi_a(x_1) \hat{H}_2\psi_b(x_2)
$$

If each particle is in an energy eigenstate ($\hat{H}_1\psi_a = E_a\psi_a$ and $\hat{H}_2\psi_b = E_b\psi_b$):

$$
= E_a\psi_a(x_1)\psi_b(x_2) + E_b\psi_a(x_1)\psi_b(x_2) = (E_a + E_b)\psi(x_1, x_2)
$$

**Result:** The product state is an energy eigenstate with **total energy = sum of individual energies**!

$$
\boxed{\hat{H}\psi = (E_a + E_b)\psi}
$$

### Concrete Example: Two Electrons in Separate Boxes

Consider two electrons, each in its own infinite potential well:

- Electron 1 in box of length $L_1 = 1$ nm
- Electron 2 in box of length $L_2 = 2$ nm

Both in ground state ($n=1$):

$$
E_1 = \frac{\pi^2\hbar^2}{2m_e L_1^2} \approx 0.38 \text{ eV}
$$

$$
E_2 = \frac{\pi^2\hbar^2}{2m_e L_2^2} \approx 0.095 \text{ eV}
$$

**Total energy:** $E_{total} = 0.38 + 0.095 = 0.475$ eV

**Wavefunction:**

$$
\psi(x_1, x_2) = \sqrt{\frac{2}{L_1}}\sin\left(\frac{\pi x_1}{L_1}\right) \cdot \sqrt{\frac{2}{L_2}}\sin\left(\frac{\pi x_2}{L_2}\right)
$$

**Measurement independence:** If you measure the position of electron 1, it doesn't affect the probability distribution for electron 2. They're completely separate systems.

---

## Coupling Particles: Interaction Potentials

Now let's make it interesting: **what if the particles interact?**

### Adding Interaction

The Hamiltonian becomes:

$$
\hat{H} = \hat{H}_1 + \hat{H}_2 + \underbrace{V(x_1, x_2)}_{\text{interaction}}
$$

The interaction potential $V(x_1, x_2)$ depends on **both positions** (this is what couples the particles!).

**Common examples:**

• **Coulomb repulsion** (two electrons): $V(x_1, x_2) = \frac{ke^2}{|x_1 - x_2|}$

• **Coulomb attraction** (electron-proton): $V(x_1, x_2) = -\frac{ke^2}{|x_1 - x_2|}$

• **Spring coupling**: $V(x_1, x_2) = \frac{1}{2}k(x_1 - x_2)^2$

### Product States No Longer Work!

Let's see what happens when we apply $\hat{H}$ to a product state:

$$
\hat{H}\psi = (\hat{H}_1 + \hat{H}_2 + V(x_1,x_2))[\psi_a(x_1)\psi_b(x_2)]
$$

The first two terms still give us $E_a + E_b$ times $\psi$, but the interaction term:

$$
V(x_1, x_2)\psi_a(x_1)\psi_b(x_2)
$$

**This doesn't factor!** You can't write it as $(E_a + E_b + \text{something})\psi$.

**Result:** Product states are **not energy eigenstates** when particles interact!

---

## Operators for Two-Particle Systems

Before we calculate energies, let's understand how operators work with two particles. This is crucial for understanding expectation values!

### Single-Particle Operators: Acting on One Particle at a Time

For two particles, you have **separate operators** for each particle:

**Momentum operators:**

$\hat{p}_1 = -i\hbar\frac{\partial}{\partial x_1}$ (acts only on particle 1's position)
$\hat{p}_2 = -i\hbar\frac{\partial}{\partial x_2}$ (acts only on particle 2's position)

**Position operators:**

$\hat{x}_1$ (multiplies by $x_1$)
$\hat{x}_2$ (multiplies by $x_2$)

**Key point:** Each operator acts on **its own variable only**. When $\hat{p}_1$ takes a derivative, it treats $x_2$ as a constant!

### Example: Momentum of Particle 1

Apply $\hat{p}_1$ to a two-particle wavefunction:

$$
\hat{p}_1 \psi(x_1, x_2) = -i\hbar\frac{\partial}{\partial x_1}\psi(x_1, x_2)
$$

**For a product state** $\psi(x_1, x_2) = \psi_a(x_1)\psi_b(x_2)$:

$$
\hat{p}_1[\psi_a(x_1)\psi_b(x_2)] = \psi_b(x_2) \cdot \left(-i\hbar\frac{\partial\psi_a}{\partial x_1}\right) = \psi_b(x_2) \cdot \hat{p}_1\psi_a(x_1)
$$

The operator "sees" $\psi_b(x_2)$ as just a constant (doesn't depend on $x_1$), so it factors out!

**Expected value of particle 1's momentum:**

$$
\langle p_1 \rangle = \int\int \psi^* \hat{p}_1 \psi \, dx_1 dx_2
$$

This gives you the average momentum of **just particle 1**, regardless of what particle 2 is doing.

### Why Does Potential Energy Depend on Both Particles?

Here's the key difference between kinetic and potential energy:

**Kinetic energy (independent):**

Particle 1's kinetic energy: $\frac{\hat{p}_1^2}{2m_1}$ (depends only on $x_1$)
Particle 2's kinetic energy: $\frac{\hat{p}_2^2}{2m_2}$ (depends only on $x_2$)
Total: $\hat{T} = \frac{\hat{p}_1^2}{2m_1} + \frac{\hat{p}_2^2}{2m_2}$

**Potential energy (can couple!):**

Coulomb repulsion: $V(x_1, x_2) = \frac{ke^2}{|x_1 - x_2|}$ (depends on **both** positions!)
The interaction energy depends on the **distance between particles**

**Physical meaning:**

- Kinetic energy is "local" (each particle has its own motion)
- Interaction energy is "nonlocal" (depends on **relative positions**)

This is why $V(x_1, x_2)$ has **both variables** (the repulsion depends on how far apart the electrons are!).

---

### Concrete Example: Two Electrons in One Box

Consider two electrons in the **same** box of length $L = 1$ nm, with Coulomb repulsion between them.

**Without interaction** (pretending they don't repel):
• Both in ground state: $E = 2E_1 = 2(0.38) = 0.76$ eV

**With Coulomb repulsion:**

The interaction raises the energy. How much? We need to calculate the **expected value** (average value) of the repulsion energy.

**Connection to Operators section:** Remember from [Operators and Measurement](quantum-operators.md) that the expected value of an operator $\hat{A}$ is:

$$
\langle A \rangle = \langle\psi|\hat{A}|\psi\rangle
$$

This is the average value you'd get if you measured $A$ many times on identically prepared systems.

**For potential energy:** The potential $V(x_1, x_2)$ is just a function (not a derivative), so the operator $\hat{V}$ acts by multiplication:

$$
\hat{V}\psi(x_1, x_2) = V(x_1, x_2) \psi(x_1, x_2)
$$

**In position representation:** The expectation value $\langle\psi|\hat{V}|\psi\rangle$ becomes an integral:

$$
\langle V \rangle = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \psi^*(x_1, x_2) \cdot V(x_1, x_2) \cdot \psi(x_1, x_2) \, dx_1 dx_2
$$

For **real wavefunctions** (like particle in a box), $\psi^* = \psi$, so $\psi^* \psi = |\psi|^2$:

$$
\langle V \rangle = \int \int |\psi(x_1, x_2)|^2 V(x_1, x_2) dx_1 dx_2
$$

**Physical meaning:** Weight the potential energy $V(x_1, x_2)$ by the probability $|\psi(x_1, x_2)|^2$ of finding the electrons at those positions, then average over all configurations.

**It's the same expectation value formula**, just extended to two particles!

**For our example:** Both electrons in ground state $\psi_1(x)$, so $\psi(x_1, x_2) = \psi_1(x_1)\psi_1(x_2)$:

$$
\langle V \rangle = \int_0^L \int_0^L |\psi_1(x_1)|^2 |\psi_1(x_2)|^2 \frac{ke^2}{|x_1 - x_2|} dx_1 dx_2
$$

For our 1 nm box with both electrons in ground state:

$$
\langle V \rangle \approx 1.4 \text{ eV}
$$

**New ground state energy:** $E \approx 0.76 + 1.4 = 2.2$ eV

The interaction adds significant energy! And the true ground state wavefunction is **not** simply $\psi_1(x_1)\psi_1(x_2)$ (it gets distorted by the repulsion).

---

## Entanglement Emerges: Non-Separable States

When particles interact, something profound happens: the wavefunction becomes **non-separable**.

### What Is a Non-Separable State?

A state $\psi(x_1, x_2)$ is **separable** if you can write it as:

$$
\psi(x_1, x_2) = \psi_a(x_1) \psi_b(x_2)
$$

for some single-particle states $\psi_a$ and $\psi_b$.

If you **can't** write it this way, the state is **entangled** (or non-separable).

### A Simple Entangled State

Consider this superposition:

$$
\psi(x_1, x_2) = \frac{1}{\sqrt{2}}\left[\psi_a(x_1)\psi_b(x_2) + \psi_b(x_1)\psi_a(x_2)\right]
$$

**Try to factor it:** Can we write this as $f(x_1) \cdot g(x_2)$ for any functions $f$ and $g$?

No! The two terms are "mixed" (you can't separate $x_1$ from $x_2$).

**Physical interpretation:**

- Either "particle 1 in state $a$ AND particle 2 in state $b$"
- Or "particle 1 in state $b$ AND particle 2 in state $a$"

The particles are **correlated**. You can't describe them independently!

### Conditional Probabilities: The Key to Entanglement

Here's what makes entanglement weird. For the entangled state:

$$
\psi(x_1, x_2) = \frac{1}{\sqrt{2}}[\psi_a(x_1)\psi_b(x_2) + \psi_b(x_1)\psi_a(x_2)]
$$

Let's ask: **"What's the probability distribution for particle 2's position?"**

It depends on what you measure for particle 1!

**Before measuring particle 1:** Integrate over $x_1$ to get the marginal probability for particle 2:

$$
P(x_2) = \int |\psi(x_1, x_2)|^2 dx_1
$$

Expanding $|\psi|^2$:

$$
|\psi(x_1, x_2)|^2 = \frac{1}{2}\left[|\psi_a(x_1)|^2|\psi_b(x_2)|^2 + |\psi_b(x_1)|^2|\psi_a(x_2)|^2 + 2\text{Re}(\psi_a^*(x_1)\psi_b^*(x_2)\psi_b(x_1)\psi_a(x_2))\right]
$$

Integrating over $x_1$ (using normalization $\int |\psi_a|^2 dx_1 = \int |\psi_b|^2 dx_1 = 1$):

$$
P(x_2) = \frac{1}{2}\left[|\psi_b(x_2)|^2 + |\psi_a(x_2)|^2\right] + \text{cross terms}
$$

**What are the cross terms?** They come from the interference term in $|\psi|^2$:

$$
\text{cross terms} = \text{Re}\int \psi_a^*(x_1)\psi_b^*(x_2)\psi_b(x_1)\psi_a(x_2) dx_1
$$

For real wavefunctions, this becomes:

$$
= \int \psi_a(x_1)\psi_b(x_1) dx_1 \cdot \psi_a(x_2)\psi_b(x_2)
$$

This is the **overlap integral** $\langle\psi_a|\psi_b\rangle$ times the product $\psi_a(x_2)\psi_b(x_2)$. If states $a$ and $b$ are orthogonal (no overlap), the cross terms vanish! Otherwise, you get quantum interference that affects particle 2's probability distribution.

Particle 2 has contributions from **both** states $a$ and $b$, plus interference from the cross terms!

**After measuring particle 1 at position $x_1^0$:** The wavefunction "collapses" and particle 2's distribution becomes:

$$
P(x_2 | x_1 = x_1^0) \propto |\psi(x_1^0, x_2)|^2 = \frac{1}{2}\left|\psi_a(x_1^0)\psi_b(x_2) + \psi_b(x_1^0)\psi_a(x_2)\right|^2
$$

This depends on the specific value $x_1^0$ where you found particle 1!

**Example:** Suppose $\psi_a$ is localized on the left and $\psi_b$ is localized on the right.

- If you find particle 1 on the **left** (where $|\psi_a(x_1^0)|^2 \gg |\psi_b(x_1^0)|^2$), then $\psi_a(x_1^0)\psi_b(x_2)$ dominates → particle 2 is likely on the **right**!

- If you find particle 1 on the **right** (where $|\psi_b(x_1^0)|^2 \gg |\psi_a(x_1^0)|^2$), then $\psi_b(x_1^0)\psi_a(x_2)$ dominates → particle 2 is likely on the **left**!

**Key insight:** Measuring particle 1 **instantly changes** the probability distribution for particle 2, even if they're far apart!

### Concrete Example: Which Box?

Imagine two boxes separated by a large distance. You have one particle and you prepare the state:

$$
\psi(x_1, x_2) = \frac{1}{\sqrt{2}}[\psi_{\text{left}}(x_1)\psi_{\text{right}}(x_2) + \psi_{\text{right}}(x_1)\psi_{\text{left}}(x_2)]
$$

**Before measurement:** Each particle has 50% chance of being in the left box, 50% in the right box.

**Measure particle 1 → find it in the left box:**

Instantly, particle 2 is **definitely** in the right box! The measurement of particle 1 "collapsed" particle 2's state.

This is entanglement. Einstein called it "spooky action at a distance."

---

## Spin: A Brief Introduction

Before we go further, we need to introduce **spin** (an intrinsic property of particles like electrons).

### What Is Spin?

Spin is **angular momentum** that particles have even when sitting still. It's not actually spinning (electrons aren't little balls), but it acts like angular momentum in many ways.

**For electrons:** Spin-1/2, meaning it comes in two states:

- Spin up: $|\uparrow\rangle$ or $|+\rangle$
- Spin down: $|\downarrow\rangle$ or $|-\rangle$

These are the only two options. Measure electron spin along any axis (say, the z-axis) and you get one of these two results.

### Spin States as Vectors

We can represent spin states as column vectors in a 2D Hilbert space:

$$
|\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

A general spin state is a superposition:

$$
|\psi\rangle = \alpha|\uparrow\rangle + \beta|\downarrow\rangle = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}
$$

where $|\alpha|^2 + |\beta|^2 = 1$.

**Measurement:** If you measure spin along the z-axis, you get:

- $|\uparrow\rangle$ with probability $|\alpha|^2$
- $|\downarrow\rangle$ with probability $|\beta|^2$

### Complete State: Spatial + Spin

An electron's complete quantum state includes **both** spatial and spin parts:

$$
\Psi(\vec{r}) = \psi_{\uparrow}(\vec{r})|\uparrow\rangle + \psi_{\downarrow}(\vec{r})|\downarrow\rangle
$$

For two electrons:

$$
\Psi(x_1, x_2) = \psi(x_1, x_2)|s_1, s_2\rangle
$$

where $s_1, s_2 \in \{\uparrow, \downarrow\}$.

**Four possible spin combinations:**

• $|\uparrow\uparrow\rangle$ (both spin up)

• $|\uparrow\downarrow\rangle$ (electron 1 up, electron 2 down)

• $|\downarrow\uparrow\rangle$ (electron 1 down, electron 2 up)

• $|\downarrow\downarrow\rangle$ (both spin down)

We'll return to spin in much more detail when we discuss Bell's theorem!

---

## Identical Particles: Symmetric and Antisymmetric Wavefunctions

Now for something truly fundamental about quantum mechanics: **identical particles are indistinguishable**.

### The Problem with Distinguishable Particles

Classically, even if two electrons are identical, you can "paint one red" (track it over time). You always know which is which.

**Quantum mechanically, this is impossible!** If you have two electrons, there's no way to tell "electron 1" from "electron 2." They're **fundamentally indistinguishable**.

### What "Indistinguishable" Means

If you **exchange** the two particles (swap labels $1 \leftrightarrow 2$), physics shouldn't change. Observable quantities like $|\psi|^2$ must stay the same:

$$
|\psi(x_2, x_1)|^2 = |\psi(x_1, x_2)|^2
$$

This means:

$$
\psi(x_2, x_1) = e^{i\phi}\psi(x_1, x_2)
$$

for some phase $\phi$.

**Exchange twice** gets you back to the original state:

$$
\psi(x_1, x_2) = e^{i\phi}\psi(x_2, x_1) = e^{2i\phi}\psi(x_1, x_2)
$$

Therefore $e^{2i\phi} = 1$, so $\phi = 0$ or $\phi = \pi$.

**Result:** Only two possibilities!

$$
\psi(x_2, x_1) = +\psi(x_1, x_2) \quad \text{(symmetric)}
$$

$$
\psi(x_2, x_1) = -\psi(x_1, x_2) \quad \text{(antisymmetric)}
$$

### Fermions vs Bosons

Nature uses both:

**Fermions** (antisymmetric):
• Electrons, protons, neutrons
• All spin-1/2 particles
• More generally: spin = 1/2, 3/2, 5/2, ... (half-integer)

**Bosons** (symmetric):
• Photons, gluons
• Helium-4 atoms
• More generally: spin = 0, 1, 2, ... (integer)

**Spin-statistics theorem:** The connection between spin and symmetry is deep (it comes from combining quantum mechanics with special relativity).

### Constructing an Antisymmetric Wavefunction

Suppose we want to put two electrons in states $\psi_a(x)$ and $\psi_b(x)$.

**Wrong:** $\psi(x_1, x_2) = \psi_a(x_1)\psi_b(x_2)$ (not antisymmetric!)

**Right:** We need to antisymmetrize:

$$
\psi(x_1, x_2) = \frac{1}{\sqrt{2}}\left[\psi_a(x_1)\psi_b(x_2) - \psi_a(x_2)\psi_b(x_1)\right]
$$

**Check exchange symmetry:**

$$
\psi(x_2, x_1) = \frac{1}{\sqrt{2}}\left[\psi_a(x_2)\psi_b(x_1) - \psi_a(x_1)\psi_b(x_2)\right] = -\psi(x_1, x_2) \quad \checkmark
$$

Perfect! The $1/\sqrt{2}$ ensures normalization.

**Physical meaning:** The wavefunction is a superposition:

- "Electron 1 in state $a$, electron 2 in state $b$"
- **minus** "Electron 1 in state $b$, electron 2 in state $a$"

But remember: these labels are arbitrary! The particles are truly indistinguishable.

### Slater Determinant Notation

For two particles, we can write the antisymmetric state as a determinant:

$$
\psi(x_1, x_2) = \frac{1}{\sqrt{2}}\begin{vmatrix}
\psi_a(x_1) & \psi_b(x_1) \\
\psi_a(x_2) & \psi_b(x_2)
\end{vmatrix} = \frac{1}{\sqrt{2}}[\psi_a(x_1)\psi_b(x_2) - \psi_a(x_2)\psi_b(x_1)]
$$

This generalizes beautifully to N particles (just use an N×N determinant, called a Slater determinant).

---

## Pauli Exclusion Principle

The antisymmetry requirement leads directly to one of the most important principles in quantum mechanics.

### What Happens If $a = b$?

Suppose we try to put both electrons in the **same** state: $\psi_a = \psi_b$.

The antisymmetric wavefunction becomes:

$$
\psi(x_1, x_2) = \frac{1}{\sqrt{2}}[\psi_a(x_1)\psi_a(x_2) - \psi_a(x_2)\psi_a(x_1)] = 0
$$

**The wavefunction vanishes!** This state doesn't exist.

**Pauli Exclusion Principle:** Two identical fermions cannot occupy the same quantum state.

**Alternative statement:** If two fermions are in the same position ($x_1 = x_2 = x$):

$$
\psi(x, x) = -\psi(x, x) = 0
$$

The antisymmetry forces $\psi(x,x) = 0$. Fermions avoid each other!

### Including Spin: The Complete Picture

The **complete** wavefunction must be antisymmetric under exchange of **all quantum numbers** (spatial + spin):

$$
\Psi(x_1, x_2) = \psi_{\text{spatial}}(x_1, x_2) \times \psi_{\text{spin}}
$$

**Key insight:** If the spatial part is symmetric, the spin part must be antisymmetric (and vice versa).

**Example 1: Spatial symmetric → spin antisymmetric**

$$
\Psi = \underbrace{\frac{1}{\sqrt{2}}[\psi_a(x_1)\psi_b(x_2) + \psi_a(x_2)\psi_b(x_1)]}_{\text{symmetric}} \times \underbrace{\frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)}_{\text{antisymmetric (singlet)}}
$$

**Example 2: Spatial antisymmetric → spin symmetric**

$$
\Psi = \underbrace{\frac{1}{\sqrt{2}}[\psi_a(x_1)\psi_b(x_2) - \psi_a(x_2)\psi_b(x_1)]}_{\text{antisymmetric}} \times \underbrace{|\uparrow\uparrow\rangle}_{\text{symmetric}}
$$

**Result:** Two electrons can be in the same **spatial** state if they have opposite spins!

The complete state (spatial × spin) is still antisymmetric overall:

$$
\psi_a(x_1)\psi_a(x_2) \times \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)
$$

This is what allows two electrons to occupy the "same orbital" in atoms (they must have opposite spins).

---

## Electrons in a Box: Energy Levels Fill Up

Let's see Pauli exclusion in action by adding electrons to a 1D infinite potential well one at a time.

### Energy Levels (Reminder)

The single-particle energy levels are:

$$
E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}, \quad n = 1, 2, 3, ...
$$

For a box of length $L = 1$ nm:

• $E_1 \approx 0.38$ eV (ground state)
• $E_2 = 4E_1 \approx 1.5$ eV
• $E_3 = 9E_1 \approx 3.4$ eV
• $E_4 = 16E_1 \approx 6.0$ eV

### Adding Electrons One by One

**One electron:**

Goes into the ground state: $n=1$, either spin up or down.

$$
\Psi = \psi_1(x_1)|\uparrow\rangle
$$

**Total energy:** $E = E_1 \approx 0.38$ eV

---

**Two electrons:**

Both can go into $n=1$ level if they have **opposite spins**!

$$
\Psi = \psi_1(x_1)\psi_1(x_2) \times \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)
$$

Spatial part is symmetric, spin part is antisymmetric → total antisymmetric ✓

**Total energy:** $E = 2E_1 \approx 0.76$ eV

(We're ignoring Coulomb repulsion for now to keep it simple.)

---

**Three electrons:**

Now we have a problem! The $n=1$ level is "full" (two electrons with opposite spins).

**Pauli exclusion:** The third electron **must** go into the next level up!

$$
\Psi = \psi_1(x_1)\psi_1(x_2)\psi_2(x_3) \times (\text{properly antisymmetrized spin state})
$$

**Total energy:** $E = 2E_1 + E_2 = 2(0.38) + 1.5 = 2.3$ eV

Big jump! The third electron forced into a higher energy state.

---

**Four electrons:**

Two in $n=1$ (opposite spins), two in $n=2$ (opposite spins):

**Total energy:** $E = 2E_1 + 2E_2 = 2(0.38) + 2(1.5) = 3.8$ eV

---

**Five electrons:**

$$
E = 2E_1 + 2E_2 + E_3 = 0.76 + 3.0 + 3.4 = 7.2 \text{ eV}
$$

**The pattern:** Energy levels fill up like stairs. Each spatial state holds **at most 2 electrons** (spin up and spin down).

### Connection to the Periodic Table

This is **exactly** how electrons fill atomic orbitals!

• Each orbital (characterized by quantum numbers $n, \ell, m$) can hold **2 electrons**

• Electrons fill from lowest to highest energy

• This explains the structure of the periodic table

**Examples:**

• Helium (2 electrons): 1s² (both in ground state, opposite spins)

• Lithium (3 electrons): 1s² 2s¹ (third electron forced to next shell)

• Neon (10 electrons): 1s² 2s² 2p⁶ (first two shells completely filled)

The Pauli exclusion principle is why matter is stable and has structure!

---

## Coulomb Repulsion: Spatial Correlation Example

Now let's add back the interaction between electrons and see how it creates **spatial correlations**.

### Two Electrons in a Box with Repulsion

Consider two electrons in a 1D box of length $L$, both with the same spin (say, both spin up). By Pauli exclusion, they must be in different **spatial** states.

Simplest antisymmetric state (ignoring spin notation since both are $\uparrow$):

$$
\psi(x_1, x_2) = \frac{1}{\sqrt{2}}[\psi_1(x_1)\psi_2(x_2) - \psi_2(x_1)\psi_1(x_2)]
$$

where $\psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$.

**Without interaction:** This is exact! Energy = $E_1 + E_2 = 5E_1$.

**With Coulomb repulsion:** $V(x_1, x_2) = \frac{ke^2}{|x_1 - x_2|}$

The wavefunction gets distorted (electrons avoid each other even more!).

### Probability Distributions

**Question:** If we find electron 1 at position $x_1$, where is electron 2 likely to be?

**Conditional probability:**

$$
P(x_2 | x_1) = \frac{|\psi(x_1, x_2)|^2}{\int |\psi(x_1, x_2)|^2 dx_2}
$$

**Let's plug in a specific location:** Say $x_1 = L/4$ (left side of box).

For the antisymmetric state above:

$$
|\psi(L/4, x_2)|^2 = \frac{1}{2}\left|\psi_1(L/4)\psi_2(x_2) - \psi_2(L/4)\psi_1(x_2)\right|^2
$$

**Result:** Electron 2 is more likely to be found on the **right side** of the box!

The antisymmetry + Coulomb repulsion creates a "hole" in the probability distribution near $x_2 = x_1$.

### Expected Separation

We can calculate the average distance between electrons:

$$
\langle |x_1 - x_2| \rangle = \int_0^L \int_0^L |x_1 - x_2| |\psi(x_1, x_2)|^2 dx_1 dx_2
$$

**Without Pauli exclusion** (if they were distinguishable bosons in the same state):

$$
\langle |x_1 - x_2| \rangle \approx 0.4L
$$

**With Pauli exclusion** (antisymmetric fermion state):

$$
\langle |x_1 - x_2| \rangle \approx 0.5L
$$

Fermions stay further apart on average! Antisymmetry creates an effective "repulsion" even before considering Coulomb forces.

**With Coulomb repulsion included:**

$$
\langle |x_1 - x_2| \rangle \approx 0.6L
$$

The interaction pushes them even further apart.

**Key insight:** Finding one electron at a particular location **changes** the probability distribution for the other (they're entangled!).

---

## Spin Entanglement and the EPR Paradox

Now we're ready for the truly weird stuff: **entangled spin states** and the EPR paradox that troubled Einstein.

### The Singlet State

The most famous entangled state is the **spin singlet**:

$$
|\psi\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)
$$

**What this means:**

- Particle 1 spin up AND particle 2 spin down
- **minus** particle 1 spin down AND particle 2 spin up

This is a superposition of the two possibilities! You don't know which is which until you measure.

**Key property:** The two spins are **anticorrelated**. If you measure particle 1 and find spin up, particle 2 is **definitely** spin down (and vice versa).

### The EPR Setup (1935)

Einstein, Podolsky, and Rosen proposed this thought experiment:

**Step 1:** Create two particles in the singlet state.

**Step 2:** Separate them by a huge distance (say, light-years apart).

**Step 3:** Alice measures particle 1's spin. Bob measures particle 2's spin.

**What happens:**

• Alice measures particle 1 → finds spin up
• **Instantly**, particle 2's state becomes spin down
• Bob measures particle 2 → finds spin down (guaranteed!)

They're perfectly anticorrelated, no matter how far apart!

### Einstein's Objection: "Spooky Action at a Distance"

Einstein was deeply troubled by this:

**Einstein's argument:**

1. The particles are far apart (space-like separated)
2. Special relativity says no signal can travel faster than light
3. Yet Alice's measurement **instantly** determines Bob's result
4. How can particle 2 "know" what Alice measured?

**Einstein's conclusion:** Quantum mechanics must be **incomplete**. The particles must have carried predetermined values with them (**hidden variables** that quantum mechanics doesn't describe).

**Local realism:** Each particle has a definite (but hidden) spin value from the moment they separate. Measurements just reveal pre-existing properties.

This seems reasonable! Like drawing colored balls from a hat (they had their colors all along).

### The Quantum Response

**Quantum mechanics says:** No! The particles **don't** have definite spins until measured. The singlet state is the complete description.

Before measurement:

- Particle 1 is in superposition: $\frac{1}{\sqrt{2}}(|\uparrow\rangle - |\downarrow\rangle)$ (if you ignore particle 2)
- Particle 2 is in superposition: $\frac{1}{\sqrt{2}}(|\downarrow\rangle - |\uparrow\rangle)$ (if you ignore particle 1)
- But they're **entangled** (the correlations are built into the joint state)

After Alice measures:

- The entangled state "collapses"
- Bob's particle is now in a definite state (opposite to Alice's result)

**Is this spooky action at a distance?**

Sort of! The correlations are nonlocal. But you can't use this to send signals faster than light (no information is transmitted by the collapse).

**Who's right: Einstein or quantum mechanics?**

For 30 years this was just philosophy. Then John Bell figured out how to test it experimentally...

---

## Bell's Theorem: Deriving the Inequality

John Bell (1964) showed that **local hidden variable theories make different predictions than quantum mechanics**. We can test who's right!

### The Setup

Instead of just measuring spin along one axis (say, z-axis), Alice and Bob can choose different measurement directions.

**Measurement directions:**

- Alice chooses angle $\theta_A$ (direction to measure spin)
- Bob chooses angle $\theta_B$
- Each gets result: $\pm 1$ (spin up/down along that axis)

**Correlation function:** Average product of their results:

$$
E(\theta_A, \theta_B) = \langle A \cdot B \rangle
$$

where $A, B \in \{+1, -1\}$.

### Local Hidden Variables Prediction

**Assumption:** Each particle carries hidden variable $\lambda$ that predetermines all measurement outcomes.

For any $\lambda$:

- Alice's result is $A(\theta_A, \lambda) = \pm 1$
- Bob's result is $B(\theta_B, \lambda) = \pm 1$

These are **predetermined functions** (the results exist before measurement!).

**Averaging over all possible $\lambda$ (with probability distribution $\rho(\lambda)$):**

$$
E(\theta_A, \theta_B) = \int A(\theta_A, \lambda) B(\theta_B, \lambda) \rho(\lambda) d\lambda
$$

### The CHSH Inequality

Consider four measurement combinations with angles $a, a', b, b'$:

$$
S = E(a,b) - E(a,b') + E(a',b) + E(a',b')
$$

**Bell's mathematical result:** For **any** local hidden variable theory:

$$
|S| \leq 2
$$

This is called the **CHSH inequality** (Clauser-Horne-Shimony-Holt, a version of Bell's original).

**Proof sketch:** Since $A, B \in \{-1, +1\}$, for any fixed $\lambda$:

$$
A(a,\lambda)[B(b,\lambda) - B(b',\lambda)] + A(a',\lambda)[B(b,\lambda) + B(b',\lambda)]
$$

Notice: $B(b) - B(b') \in \{-2, 0, +2\}$ and $B(b) + B(b') \in \{-2, 0, +2\}$.

When $B(b) - B(b') = 0$, we have $B(b) = B(b')$, so $|B(b) + B(b')| = 2$.
When $B(b) + B(b') = 0$, we have $B(b) = -B(b')$, so $|B(b) - B(b')| = 2$.

In either case: $|A(a)[B(b)-B(b')]| + |A(a')[B(b)+B(b')]| \leq 2$ (since $|A| = 1$).

Taking absolute value before averaging over $\lambda$ gives $|S| \leq 2$.

**Interpretation:** Local realism **constrains** the correlations. You can't get too correlated across different measurement angles.

### Quantum Mechanics Violates It!

For the singlet state $\frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$, quantum mechanics predicts:

$$
E(\theta_A, \theta_B) = -\cos(\theta_A - \theta_B)
$$

The correlation depends on the **relative angle** between measurement directions!

**Optimal angle choices:** $a = 0°$, $a' = 90°$, $b = 45°$, $b' = 135°$

Calculate each term:

- $E(a,b) = E(0°, 45°) = -\cos(45°) = -\frac{1}{\sqrt{2}}$
- $E(a,b') = E(0°, 135°) = -\cos(135°) = +\frac{1}{\sqrt{2}}$
- $E(a',b) = E(90°, 45°) = -\cos(45°) = -\frac{1}{\sqrt{2}}$
- $E(a',b') = E(90°, 135°) = -\cos(45°) = -\frac{1}{\sqrt{2}}$

$$
S = -\frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}} = -\frac{4}{\sqrt{2}} = -2\sqrt{2} \approx -2.83
$$

**Result:** $|S| = 2.83 > 2$ (**Bell's inequality is violated!**)

Quantum mechanics predicts correlations that are **impossible** for any local hidden variable theory.

### What This Means

**The verdict:**

- ✗ **Local realism is wrong** (Nature doesn't have predetermined values)
- ✓ **Quantum mechanics is right** (The correlations are genuinely nonlocal)

**But wait:** How do we know quantum mechanics is right? We need to do the experiment!

---

## Experimental Tests: Bell's Inequality in the Lab

Bell's theorem moved entanglement from philosophy to experimental science.

### Aspect's Experiments (1981-1982)

Alain Aspect and collaborators performed the definitive early tests:

**Setup:**

- Source produces entangled photon pairs (polarization-entangled, analogous to spin-entangled electrons)
- Photons sent to Alice and Bob (13 meters apart)
- Each measures polarization along chosen angle
- Record correlations for different angle combinations

**Key innovation:** Rapidly switching measurement angles while photons are in flight → ensures measurements are space-like separated (no communication possible between detectors).

**Result:**

$$
S_{\text{measured}} = 2.70 \pm 0.05
$$

**Violates Bell's inequality!** Quantum mechanics wins, local realism loses.

### Loopholes and How They Were Closed

Early experiments had potential loopholes Einstein fans could exploit:

**1. Detection loophole:**

- Not all photons are detected (typical efficiency ~20-30%)
- Maybe hidden variables cleverly avoid being measured?
- **Closed:** Use more efficient detectors (>80% efficiency)

**2. Locality loophole:**

- Detectors not far enough apart (maybe communication possible?)
- **Closed:** Space-like separated measurements (detection events outside each other's light cones)

**3. Freedom-of-choice loophole:**

- Measurement angles chosen by pseudo-random number generators
- Maybe hidden variables determine both outcomes and measurement choices?
- **Closed:** Use cosmic photons or human choice to set angles

### Loophole-Free Experiments (2015)

Three independent groups simultaneously closed **all major loopholes**:

• **Delft** (Hanson et al.): Entangled electron spins in diamond, 1.3 km separation

• **Vienna** (Zeilinger et al.): Entangled photons, 60 meters, >75% efficiency detectors

• **NIST** (Shalm et al.): Entangled photons, efficient detectors, space-like separation

**All found:** Clear violation of Bell's inequality with all loopholes closed!

$$
|S| > 2 \quad \text{(with high statistical significance)}
$$

### The 2022 Nobel Prize

The Nobel Prize in Physics was awarded to:

• **Alain Aspect** (France): pioneering photon entanglement experiments

• **John Clauser** (USA): first experimental test of Bell's inequality (1972)

• **Anton Zeilinger** (Austria): quantum information and loophole-free tests

**The citation:** "for experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science"

### What We've Learned

**Nature is fundamentally nonlocal:**

- Measurement outcomes at one location are **instantaneously** correlated with distant measurements
- This isn't due to hidden variables or communication
- It's **genuine quantum entanglement**

**But information still can't travel faster than light:**

- Alice's individual results look random (50% up, 50% down)
- Only when Alice and Bob **compare** results do they see the correlations
- Comparing requires classical communication (limited by speed of light)

**Einstein was wrong, but in the most interesting way:**

- Quantum mechanics really is complete (no hidden variables needed)
- "Spooky action at a distance" is real!
- But it doesn't violate relativity

The universe is even weirder than Einstein thought!

---

## Matrix Representation for Discrete Systems

For systems with discrete spin states, we can represent everything using matrices (making entanglement very concrete).

### Single Spin: 2D Hilbert Space

A single spin-1/2 particle lives in a 2D Hilbert space:

**Basis states:**

$$
|\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

**General state:**

$$
|\psi\rangle = \alpha|\uparrow\rangle + \beta|\downarrow\rangle = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}
$$

### Two Spins: 4D Hilbert Space (Tensor Product)

With two particles, the Hilbert space is the **tensor product**: $\mathcal{H}_1 \otimes \mathcal{H}_2$.

**Dimension:** $2 \times 2 = 4$ (dimension multiplies!)

**Basis states:**

$$
|\uparrow\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \quad
|\uparrow\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \quad
|\downarrow\uparrow\rangle = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \quad
|\downarrow\downarrow\rangle = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}
$$

**Ordering convention:** First entry is particle 1, second is particle 2.

### Product States vs Entangled States

**Product state example:** $|\uparrow\downarrow\rangle$

$$
|\uparrow\downarrow\rangle = |\uparrow\rangle \otimes |\downarrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \otimes \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}
$$

This is **separable** (particle 1 is definitely up, particle 2 is definitely down).

**Singlet state (entangled):**

$$
|\psi_{\text{singlet}}\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle) = \frac{1}{\sqrt{2}}\begin{pmatrix} 0 \\ 1 \\ -1 \\ 0 \end{pmatrix}
$$

**Check if separable:** Can we write this as $(\alpha_1|\uparrow\rangle + \beta_1|\downarrow\rangle) \otimes (\alpha_2|\uparrow\rangle + \beta_2|\downarrow\rangle)$?

Expanding the tensor product:

$$
= \alpha_1\alpha_2|\uparrow\uparrow\rangle + \alpha_1\beta_2|\uparrow\downarrow\rangle + \beta_1\alpha_2|\downarrow\uparrow\rangle + \beta_1\beta_2|\downarrow\downarrow\rangle
$$

For the singlet: coefficient of $|\uparrow\uparrow\rangle$ is 0, so $\alpha_1\alpha_2 = 0$.

- If $\alpha_1 = 0$: then coefficient of $|\uparrow\downarrow\rangle$ is 0, so $\alpha_1\beta_2 = 0$ ✓
- But then coefficient of $|\downarrow\uparrow\rangle$ is $\beta_1\alpha_2$, which must equal $-1/\sqrt{2}$
- And coefficient of $|\downarrow\downarrow\rangle$ is $\beta_1\beta_2$, which must equal $0$

So $\beta_2 = 0$ (to make last term zero), but then $\beta_1\alpha_2 = -1/\sqrt{2}$ requires $\alpha_2 \neq 0$... but we needed $\alpha_1\alpha_2 = 0$ with $\alpha_1 = 0$ ✓, giving no constraint on $\alpha_2$.

Actually, let's be more careful: if $\alpha_1 = 0$, then $\beta_1 \neq 0$ (normalized). Then $\beta_1\beta_2 = 0$ means $\beta_2 = 0$. But $\alpha_2$ must be normalized: $|\alpha_2|^2 + |\beta_2|^2 = 1$, so $\alpha_2 = e^{i\phi}$ for some phase.

Then coefficient of $|\downarrow\uparrow\rangle$ is $\beta_1 e^{i\phi} = -1/\sqrt{2}$.
And coefficient of $|\uparrow\downarrow\rangle$ should be $1/\sqrt{2}$, but $\alpha_1\beta_2 = 0 \cdot 0 = 0 \neq 1/\sqrt{2}$. Contradiction!

**Result:** The singlet **cannot** be factored into a product state (it's genuinely entangled!).

### Measuring Entanglement: Example Calculation

Let's calculate what happens when Alice measures her spin in the singlet state.

**Before measurement:**

$$
|\psi\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)
$$

**Alice measures particle 1 along z-axis:**

**Case 1: Alice gets $\uparrow$**

The state collapses to the part with particle 1 = $|\uparrow\rangle$:

$$
|\psi_{\text{after}}\rangle = |\uparrow\downarrow\rangle
$$

Bob's particle is **definitely** $|\downarrow\rangle$!

**Case 2: Alice gets $\downarrow$**

The state collapses to:

$$
|\psi_{\text{after}}\rangle = -|\downarrow\uparrow\rangle
$$

Bob's particle is **definitely** $|\uparrow\rangle$!

(The minus sign is an overall phase, physically irrelevant for Bob's local measurements.)

**Probability:** Each outcome occurs with 50% probability:

$$
P(\uparrow) = \left|\frac{1}{\sqrt{2}}\right|^2 = \frac{1}{2}, \quad P(\downarrow) = \left|\frac{1}{\sqrt{2}}\right|^2 = \frac{1}{2}
$$

**Key insight:** Alice's measurement **instantaneously** determines Bob's state, even though her result was random (50/50)!

### Operators as Matrices

For a single spin, the z-component spin operator is:

$$
\hat{S}_z = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

Eigenvalues: $+\hbar/2$ (spin up) and $-\hbar/2$ (spin down).

For two spins, we can measure correlations. The operator $\hat{S}_{1z} \otimes \hat{S}_{2z}$ (product of individual spin measurements) becomes a 4×4 matrix:

$$
\hat{S}_{1z} \otimes \hat{S}_{2z} = \frac{\hbar^2}{4}\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}
$$

**Calculate expected value for singlet state:**

$$
\langle \hat{S}_{1z} \otimes \hat{S}_{2z} \rangle = \langle\psi|\hat{S}_{1z} \otimes \hat{S}_{2z}|\psi\rangle
$$

$$
= \frac{1}{2}\begin{pmatrix} 0 & 1 & -1 & 0 \end{pmatrix} \frac{\hbar^2}{4}\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \\ -1 \\ 0 \end{pmatrix}
$$

$$
= \frac{\hbar^2}{8}\begin{pmatrix} 0 & 1 & -1 & 0 \end{pmatrix} \begin{pmatrix} 0 \\ -1 \\ 1 \\ 0 \end{pmatrix} = \frac{\hbar^2}{8}(-1 - 1) = -\frac{\hbar^2}{4}
$$

**Result:** Negative correlation! When particle 1 is up, particle 2 tends to be down (and vice versa).

For a product state like $|\uparrow\uparrow\rangle$, you'd get $+\hbar^2/4$ (positive correlation).

**The singlet has maximum anticorrelation** (the defining feature of this entangled state!).

---

## Summary: The Big Picture

We've journeyed from one particle to two, discovering profound changes along the way:

### 1. Two-Particle Wavefunctions

**One particle:** $\psi(x,t)$ (amplitude at position $x$)

**Two particles:** $\psi(x_1, x_2, t)$ (joint amplitude at positions $x_1$ **and** $x_2$)

**Dimension explosion:** Function of 2 variables (or 6 in 3D), so quantum chemistry is hard!

### 2. Product States vs Entangled States

**Product (separable):** $\psi(x_1,x_2) = \psi_a(x_1)\psi_b(x_2)$

- Particles are independent
- No correlations beyond classical probability

**Entangled (non-separable):** Cannot be factored

- Measuring one particle affects the other
- Genuine quantum correlations

### 3. Identical Particles: Fermions and Bosons

**Indistinguishability** forces exchange symmetry:

**Fermions** (electrons, protons, neutrons): $\psi(x_2,x_1) = -\psi(x_1,x_2)$
- Antisymmetric wavefunctions
- Pauli exclusion: no two in same state
- Explains atomic structure and periodic table

**Bosons** (photons, helium-4): $\psi(x_2,x_1) = +\psi(x_1,x_2)$
- Symmetric wavefunctions
- Can pile into same state (Bose-Einstein condensation)

### 4. Energy Levels Fill Up

**Pauli exclusion** means electrons fill orbitals like apartments:

• Each spatial state holds **max 2 electrons** (opposite spins)

• Build up from lowest to highest energy

• Explains chemistry, solid-state physics, stellar structure

### 5. Interactions Create Correlations

**Coupling potential** $V(x_1, x_2)$ means product states no longer eigenstates

**Coulomb repulsion** means spatial anticorrelations:

• Find electron 1 on left, then electron 2 more likely on right

• Measured via conditional probabilities $P(x_2|x_1)$

### 6. Spin Entanglement and EPR

**Singlet state:** $\frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$

• Perfect anticorrelations

• Measure one, then instantly know the other

**EPR paradox (1935):** Einstein's objection to "spooky action at a distance"

• Proposed local hidden variables instead

### 7. Bell's Theorem: Nature Is Nonlocal

**Bell's inequality (1964):** Local hidden variables predict $|S| \leq 2$

**Quantum mechanics:** Predicts $|S| = 2\sqrt{2} \approx 2.83$ (**violation!**)

**Experiments (1972-2015):**

• Aspect, Clauser, Zeilinger, many others

• All loopholes closed by 2015

• Nature violates Bell's inequality, so quantum mechanics wins!

**2022 Nobel Prize:** Awarded for establishing quantum nonlocality experimentally

### 8. What This Means

**No local realism:**

• Particles don't have predetermined properties

• Correlations are fundamentally nonlocal

• Measurement on one particle instantly affects the other

**No faster-than-light communication:**

• Individual results still random

• Only by comparing do you see correlations

• Information still limited by speed of light

**Entanglement is real:**

• Not due to hidden variables

• Not an illusion or incomplete theory

• Fundamental feature of quantum mechanics

### 9. Applications and Future

Entanglement isn't just weird (it's **useful**):

• **Quantum computing:** Entangled qubits for parallel computation

• **Quantum cryptography:** Unhackable communication using entangled photons

• **Quantum teleportation:** Transfer quantum states using entanglement

• **Quantum sensing:** Entanglement-enhanced measurements

The strangeness that troubled Einstein is now the foundation of quantum information science!

---

## Further Reading

**Bell's original papers:**

- "On the Einstein Podolsky Rosen Paradox" (1964): the groundbreaking theorem
- "Bertlmann's socks and the nature of reality" (1981): wonderfully accessible explanation

**Classic experiments:**

- Aspect, Dalibard, Roger, "Experimental test of Bell's inequalities..." (1982)
- Hensen et al., "Loophole-free Bell inequality violation..." (2015)

**Books:**

- "Quantum Computation and Quantum Information" (Nielsen & Chuang)
- "Entanglement" (Amir Aczel, popular science)

**Next steps:**

- Density matrices (describing mixed states and partial information)
- Quantum information theory (quantifying entanglement)
- Many-body quantum mechanics (atoms, molecules, solids)
