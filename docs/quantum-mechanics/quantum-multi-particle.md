# Multi-Particle Quantum Mechanics

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

**Let's be crystal clear about what this means:**

- **If you DON'T measure particle 1** (no knowledge about its position): Particle 2's probability is $P(x_2) = \frac{1}{2}[|\psi_b(x_2)|^2 + |\psi_a(x_2)|^2] + \text{cross terms}$. This is the **marginal probability** (averaging over all possible particle 1 positions).

- **If you DO measure particle 1** and find it at $x_1^0$: Particle 2's probability **changes** to $P(x_2|x_1=x_1^0)$, which depends on where you found particle 1! This is the **conditional probability**.

The measurement of particle 1 gives you new information that changes your prediction for particle 2. That's entanglement!

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

**Note:** We'll introduce spin (an important quantum property) later when we need it for understanding Bell's theorem and EPR paradox. For now, let's continue with spatial wavefunctions only!

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

This means the wavefunctions can only differ by a phase: ψ(x₂, x₁) = e^(iφ)ψ(x₁, x₂) for some phase φ.

**Let's figure out what φ must be.** Exchange twice gets you back to the original state. Let's do this step by step:

**Step 1:** Start with the original state ψ(x₁, x₂)

**Step 2:** Exchange once (swap 1 ↔ 2). This gives us ψ(x₂, x₁), which by the equation above equals:

$$
\psi(x_2, x_1) = e^{i\phi}\psi(x_1, x_2)
$$

**Step 3:** Exchange again (swap 1 ↔ 2 again). Starting from ψ(x₂, x₁), swapping gives us ψ(x₁, x₂). But we can also apply our exchange rule to ψ(x₂, x₁):

$$
\text{Exchanging } \psi(x_2, x_1) \text{ gives: } e^{i\phi}\psi(x_2, x_1)
$$

**Step 4:** But we know from Step 2 that ψ(x₂, x₁) = e^(iφ)ψ(x₁, x₂), so substitute:

$$
e^{i\phi}\psi(x_2, x_1) = e^{i\phi} \cdot e^{i\phi}\psi(x_1, x_2) = e^{2i\phi}\psi(x_1, x_2)
$$

**Step 5:** But exchanging twice must give back the original state ψ(x₁, x₂)! So:

$$
\psi(x_1, x_2) = e^{2i\phi}\psi(x_1, x_2)
$$

This is only true if $e^{2i\phi} = 1$, which means $\phi = 0$ or $\phi = \pi$.

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

**Next:** Continue to [The Pauli Exclusion Principle](quantum-pauli-exclusion.md) to see the profound consequences of antisymmetry for atomic structure and the periodic table!
