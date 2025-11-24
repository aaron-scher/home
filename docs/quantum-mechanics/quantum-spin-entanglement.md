# Spin, Entanglement, and Bell's Theorem

!!! warning "OUTDATED CONTENT"
    This page contains draft/outdated material and is not currently maintained.

**Prerequisites:** This builds on [Multi-Particle Quantum Mechanics](quantum-multi-particle.md) and [The Pauli Exclusion Principle](quantum-pauli-exclusion.md). Make sure you understand entangled states and identical particles before continuing!

---

## From Position to Spin: A New Quantum Property

So far, we've focused on **spatial entanglement** (correlations in position). Now we'll introduce **spin** - an intrinsic quantum property that provides the cleanest examples of entanglement and led to experimental tests that shook our understanding of reality.

**Quick recap of what we know about entanglement:**

In [Multi-Particle Quantum Mechanics](quantum-multi-particle.md), we learned that entangled states **cannot be factored**:

$$
\psi(x_1, x_2) \neq \psi_a(x_1) \psi_b(x_2)
$$

And we saw that measuring one particle **instantly affects** the probability distribution of the other. Now we'll see this gets even stranger with spin...

---

## Spin: A Brief Introduction

Before we go further, we need to introduce **spin** (an intrinsic property of particles like electrons).

### What Is Spin?

Spin is **angular momentum** that particles have even when sitting still. It's not actually spinning (electrons aren't little balls), but it acts like angular momentum in many ways.

**For electrons:** Spin-1/2, meaning it comes in two states:

- Spin up: $|\uparrow\rangle$ or $|+\rangle$
- Spin down: $|\downarrow\rangle$ or $|-\rangle$

These are the only two options. Measure electron spin along any axis (say, the z-axis) and you get one of these two results.

**Important:** "Up" and "down" are **relative to your measurement direction**, not absolute directions in space! There's no universal "up" in the universe (is the center of the Milky Way "down"?). When we say "spin up along the z-axis," we mean the spin is **aligned with** the direction you chose to call +z (your detector's orientation). "Spin down" means **opposite to** that direction. You're free to choose any axis you want—the labels just tell you whether the spin points parallel or antiparallel to your chosen measurement direction.

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

An electron has **two properties**: where it is (position) and which way it's spinning (spin). The complete quantum state must specify both!

**You still have ONE quantum state**, but now it has **two components** (because spin can be ↑ or ↓).

**Analogy:** A 2D velocity vector $\vec{v} = (v_x, v_y)$ is ONE vector, but it has two components (x-component and y-component). Similarly, the electron's quantum state is ONE state, but it has two spin components.

**The complete state** is written:

$$
\Psi(x) = \psi_{\uparrow}(x)|\uparrow\rangle + \psi_{\downarrow}(x)|\downarrow\rangle
$$

**Wait, what's going on here? Are the kets column vectors? Are they being multiplied?**

Yes! Let me unpack this confusing notation. The kets ARE still column vectors:

$$
|\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

And $\psi_\uparrow(x)$ and $\psi_\downarrow(x)$ are just **scalar functions** (regular numbers that depend on $x$).

**So at each position $x$, you multiply scalars times vectors:**

$$
\Psi(x) = \psi_{\uparrow}(x) \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \psi_{\downarrow}(x) \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} \psi_{\uparrow}(x) \\ \psi_{\downarrow}(x) \end{pmatrix}
$$

**Key insight:** At each position $x$, the wavefunction Ψ(x) is a **2-component column vector**! The top component is ψ↑(x) and the bottom component is ψ↓(x).

**What are these components?**

- $\psi_\uparrow(x)$ = amplitude for electron to be at position $x$ **with spin up**
- $\psi_\downarrow(x)$ = amplitude for electron to be at position $x$ **with spin down**

This is the **ONE** complete wavefunction—it just has two components (a 2D spinor) at each position $x$!

**What this means:**

- If you measure spin and get ↑, the electron's position is described by $\psi_\uparrow(x)$
- If you measure spin and get ↓, the electron's position is described by $\psi_\downarrow(x)$
- Before measurement, the electron is in a superposition of both spin states

**Important: Renormalization after measurement!**

Before measurement, the full state is normalized:

$$
\int \left[|\psi_\uparrow(x)|^2 + |\psi_\downarrow(x)|^2\right] dx = 1
$$

But $\int |\psi_\uparrow(x)|^2 dx$ alone equals the **probability** of measuring spin up (call it $P_\uparrow$), which might be less than 1!

**After you measure spin up**, the state collapses to just the spin-up component, but you need to **renormalize** it:

$$
\psi_\uparrow(x) \to \frac{\psi_\uparrow(x)}{\sqrt{P_\uparrow}}
$$

Now $\int \left|\frac{\psi_\uparrow(x)}{\sqrt{P_\uparrow}}\right|^2 dx = \frac{P_\uparrow}{P_\uparrow} = 1$ ✓

This ensures the collapsed state is still properly normalized (total probability = 1).

**Probability interpretation:**

- $|\psi_\uparrow(x)|^2 dx$ = probability of finding electron at position $x$ **with spin up**
- $|\psi_\downarrow(x)|^2 dx$ = probability of finding electron at position $x$ **with spin down**

The ket notation $|\uparrow\rangle$ and $|\downarrow\rangle$ is just a compact way to label which spin component you're talking about.

**Key point:** Spin adds an extra "dimension" to the wavefunction. Before spin: ψ(x) was one number at each position. With spin: Ψ(x) has two numbers at each position (one for spin-up, one for spin-down). It's still ONE quantum state—just with more structure!

### Two Electrons: Position AND Spin

For two electrons in 1D, you have **four** possible spin combinations. The complete state is actually:

$$
\Psi(x_1, x_2) = \psi_{\uparrow\uparrow}(x_1, x_2)|\uparrow\uparrow\rangle + \psi_{\uparrow\downarrow}(x_1, x_2)|\uparrow\downarrow\rangle + \psi_{\downarrow\uparrow}(x_1, x_2)|\downarrow\uparrow\rangle + \psi_{\downarrow\downarrow}(x_1, x_2)|\downarrow\downarrow\rangle
$$

**So yes, it's a column vector with FOUR elements, each multiplied by a spatial wavefunction!**

At each pair of positions $(x_1, x_2)$, the state is:

$$
\Psi(x_1, x_2) = \begin{pmatrix}
\psi_{\uparrow\uparrow}(x_1, x_2) \\
\psi_{\uparrow\downarrow}(x_1, x_2) \\
\psi_{\downarrow\uparrow}(x_1, x_2) \\
\psi_{\downarrow\downarrow}(x_1, x_2)
\end{pmatrix}
$$

**What these mean:**

- $\psi_{\uparrow\uparrow}(x_1, x_2)$ = amplitude for electron 1 at $x_1$ with spin up AND electron 2 at $x_2$ with spin up
- $\psi_{\uparrow\downarrow}(x_1, x_2)$ = amplitude for electron 1 at $x_1$ with spin up AND electron 2 at $x_2$ with spin down
- And so on...

**Compact notation:** We often write this as $\psi(x_1, x_2)|s_1, s_2\rangle$ where $s_1, s_2 \in \{\uparrow, \downarrow\}$, but that's hiding the fact that there are really **four different spatial wavefunctions**, one for each spin combination!

**Important simplification:** Often the spin and spatial parts are **separable**, meaning we can write:

$$
\Psi(x_1, x_2) = \psi_{\text{spatial}}(x_1, x_2) \times |\text{spin state}\rangle
$$

For example: $\psi(x_1, x_2)|\uparrow\downarrow\rangle$ means the **same** spatial wavefunction ψ(x₁, x₂) applies, with electron 1 having spin up and electron 2 having spin down. This is much simpler and is what we'll use for most of the document!

We'll return to spin in much more detail when we discuss Bell's theorem!

---


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

We've journeyed through spin, entanglement, and the experimental tests that revealed the quantum nature of reality:

### Spin as a Quantum Property

**Intrinsic angular momentum:** Electrons have spin-1/2 (two states: ↑ and ↓)

**Complete state:** Must specify both position AND spin: $\Psi(x) = \psi_\uparrow(x)|\uparrow\rangle + \psi_\downarrow(x)|\downarrow\rangle$

**Two particles:** 4D spin space (↑↑, ↑↓, ↓↑, ↓↓)

### The EPR Paradox

**Singlet state:** $\frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$ - perfectly anticorrelated

**Einstein's objection:** Measuring one particle instantly affects the other → must be hidden variables!

**Quantum response:** No hidden variables - entanglement is real!

### Bell's Theorem

**Key insight:** Local hidden variables predict $|S| \leq 2$

**Quantum mechanics:** Predicts $|S| = 2\sqrt{2} \approx 2.83$ (violates Bell's inequality!)

**This is testable:** Different theories make different experimental predictions!

### Experimental Verification

**Early tests (1972-1982):** Clauser, Aspect - quantum mechanics wins!

**Loophole-free (2015):** All major loopholes closed - entanglement is real!

**2022 Nobel Prize:** Awarded for establishing quantum nonlocality

### What It All Means

**Nature is nonlocal:**
- Correlations are instantaneous
- Not due to hidden variables
- Genuine quantum entanglement

**But no faster-than-light communication:**
- Individual results are random
- Only comparison reveals correlations
- Information limited by speed of light

**Implications:**
- Quantum mechanics is complete
- Reality is fundamentally different from classical intuition
- Entanglement enables quantum technologies

---

## Applications and Future

Entanglement isn't just weird—it's **useful**:

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
