# The Pauli Exclusion Principle

!!! warning "OUTDATED CONTENT"
    This page contains draft/outdated material and is not currently maintained.

**Prerequisites:** This builds on [Multi-Particle Quantum Mechanics](quantum-multi-particle.md). Make sure you understand identical particles, fermions vs bosons, and antisymmetric wavefunctions before continuing!

---

## Quick Recap: Identical Fermions Must Be Antisymmetric

In the [previous section](quantum-multi-particle.md), we learned that identical fermions (like electrons) must have **antisymmetric wavefunctions**:

$$
\psi(x_2, x_1) = -\psi(x_1, x_2)
$$

When we put two fermions in states $\psi_a$ and $\psi_b$, we construct the antisymmetric wavefunction:

$$
\psi(x_1, x_2) = \frac{1}{\sqrt{2}}\left[\psi_a(x_1)\psi_b(x_2) - \psi_a(x_2)\psi_b(x_1)\right]
$$

Now let's see what happens when we try to put both fermions in the **same** state...

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

## Summary: Why Pauli Exclusion Matters

The Pauli exclusion principle isn't just a rule - it's a fundamental consequence of fermion antisymmetry that has profound effects:

**1. Atoms have structure:** Without it, all electrons would collapse into the ground state. No chemistry, no life!

**2. Matter is stable:** Pauli pressure prevents white dwarfs and neutron stars from collapsing further.

**3. Electrons stay apart:** Even without Coulomb repulsion, antisymmetry creates "exchange repulsion."

**4. The periodic table:** Explains why elements have their chemical properties (valence electrons, noble gases, etc.).

**5. Conductors vs insulators:** Band structure and electrical conductivity depend on how energy levels fill up.

---

**Next:** Continue to [Spin, Entanglement, and Bell's Theorem](quantum-spin-entanglement.md) to explore the deeper quantum correlations and experimental tests of quantum mechanics!
