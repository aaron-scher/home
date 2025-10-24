# Quantum Operators and Measurement

## The Momentum Operator and Plane Waves

Let's start where we left off in [Foundations](quantum-foundations.md): plane waves. A plane wave solution to Schrödinger's equation with definite momentum $p = \hbar k$ and energy $E = \hbar\omega$ looks like:

$$
\psi(x,t) = A e^{i(kx - \omega t)}
$$

We can use the exponential property to write this as a **product** of spatial and temporal parts:

$$
\psi(x,t) = \underbrace{A e^{ikx}}_{\text{spatial part}} \cdot \underbrace{e^{-i\omega t}}_{\text{time part}}
$$

This separation is crucial! The spatial part encodes momentum information, while the time part encodes energy information. They're independent — a key feature of **stationary states**.

**What's a stationary state?** A stationary state is a quantum state with definite energy (an energy eigenstate). The "stationary" name comes from the fact that all measurable properties (like probability density $|\psi|^2$) are constant in time. The wavefunction oscillates as $e^{-iEt/\hbar}$, but this is just a global phase that doesn't affect any measurements.

Stationary states arise when the system's Hamiltonian doesn't depend on time — meaning all potentials are time-independent: $V(x)$ not $V(x,t)$. This includes free particles (no potential), particles in static external fields, and even interacting particles (like two electrons) as long as all interactions are time-independent (e.g., Coulomb repulsion between electrons doesn't change with time). Plane waves are examples of stationary states for free particles.

**Looking ahead:** Later we'll see that taking the **time derivative** ∂ψ/∂t extracts **energy** from the time part, just like the spatial derivative extracts momentum! But for now, let's focus on momentum.

### Extracting Momentum: The Spatial Derivative

Focus on the spatial part:

$$
\psi(x) = A e^{ikx}
$$

This is what we derived from de Broglie's relation. Now let's ask: **what happens when we take the spatial derivative?**

**Key property of exponentials:** Taking the derivative with respect to $x$ brings down the exponent:

$$
\frac{d}{dx}e^{ikx} = (ik) \cdot e^{ikx}
$$

The factor $ik$ (whatever was multiplying $x$ in the exponent) gets pulled out front. This simple property is what makes the momentum operator work!

Applying this to our plane wave:

$$
\frac{d\psi}{dx} = A(ik)e^{ikx} = ik\psi = \frac{i}{\hbar}p\psi
$$

Multiply both sides by $-i\hbar$:

$$
-i\hbar\frac{d\psi}{dx} = p\psi
$$

**This is huge!** Look at what just happened:

• We applied the mathematical operation $-i\hbar\frac{d}{dx}$ to the wavefunction
• We got back the momentum $p$ times the wavefunction

We call this operation "applying **the momentum operator**" and give it the symbol $\hat{p}$. So we can write:

$$
\hat{p}\psi(x) = -i\hbar\frac{d\psi}{dx} = p\psi
$$

**Important distinction:** This form $-i\hbar\frac{d}{dx}$ is specific to **position representation** (when the wavefunction is written as $\psi(x)$). It tells you *how* the momentum operator acts on functions of $x$.

More generally, without referring to a specific representation, we write this in **abstract notation** (ket notation):

$$
\hat{p}|\psi\rangle = p|\psi\rangle
$$

This says the same physics — "applying the momentum operator gives back the state multiplied by the momentum value $p$" — but now without specifying *how* you calculate it.

**Important:** This equation $\hat{p}|\psi\rangle = p|\psi\rangle$ is NOT true for all states! It only holds for special wavefunctions called **momentum eigenstates** (like plane waves). For general superpositions, applying $\hat{p}$ gives a more complicated result — we'll see examples of this below.

**The key point:** $\hat{p}$ is the operator itself (abstract concept), while $-i\hbar\frac{d}{dx}$ is how that operator acts when you're working with wavefunctions in position space $\psi(x)$.

**Connection to real measurements:** In the lab, one straightforward way to measure momentum is to measure wavelength $\lambda$ (via diffraction or interference patterns). For a free particle, de Broglie tells us $p = h/\lambda = \hbar k$ where $k = 2\pi/\lambda$. So wavelength describes "how rapidly the wave oscillates in space," which is exactly what the spatial derivative $d/dx$ captures. The operator $-i\hbar\frac{d}{dx}$ mathematically packages up this measurement process: different wavelengths → different $k$ values → different rates of spatial oscillation → different values when you take $d/dx$.

When a state satisfies this equation, we say it's a **momentum eigenstate** with **eigenvalue** $p$.

### Example 1: Single Plane Wave (Eigenstate)

Consider a particle in a single plane wave state:

$$
\psi(x) = A e^{ikx} \quad \text{where } k = 5\text{ nm}^{-1}
$$

Apply the momentum operator:

$$
\hat{p}\psi = -i\hbar\frac{d}{dx}\left(Ae^{ikx}\right) = -i\hbar(ik)Ae^{ikx} = \hbar k\psi = p\psi
$$

We get back **the same wavefunction** multiplied by a number ($p = \hbar k$).

**Physical meaning:** If you measure momentum, you get $p = 5\hbar$ nm⁻¹ with **100% certainty**. Every single measurement gives the same result. The particle has **definite momentum**.

### Example 2: Superposition of Two Plane Waves (NOT an Eigenstate)

Now consider a particle in a superposition of two plane waves:

$$
\psi(x) = \frac{1}{\sqrt{2}}\left(e^{ik_1 x} + e^{ik_2 x}\right)
$$

Let's say $k_1 = 3$ nm⁻¹ and $k_2 = 7$ nm⁻¹. Apply the momentum operator:

$$
\hat{p}\psi = -i\hbar\frac{d}{dx}\left[\frac{1}{\sqrt{2}}\left(e^{ik_1 x} + e^{ik_2 x}\right)\right]
$$

$$
= \frac{1}{\sqrt{2}}\left(\hbar k_1 e^{ik_1 x} + \hbar k_2 e^{ik_2 x}\right)
$$

$$
= \frac{1}{\sqrt{2}}\left(p_1 e^{ik_1 x} + p_2 e^{ik_2 x}\right)
$$

**This is NOT equal to $p\psi$ for any single number $p$!** We don't get the same wavefunction back.

**Physical meaning:** This state is **not a momentum eigenstate**. If you measure momentum, you get:

• $p_1 = 3\hbar$ nm⁻¹ with probability $|\frac{1}{\sqrt{2}}|^2 = 50\%$
• $p_2 = 7\hbar$ nm⁻¹ with probability $|\frac{1}{\sqrt{2}}|^2 = 50\%$

The particle does **not** have a definite momentum! This is why quantum measurements are probabilistic.

### Another Superposition: Unequal Amplitudes

Let's make it more interesting with unequal amplitudes:

$$
\psi(x) = \frac{1}{2}e^{ik_1 x} + \frac{\sqrt{3}}{2}e^{ik_2 x}
$$

Now the probabilities are:

• $p_1 = k_1\hbar$ with probability $|\frac{1}{2}|^2 = 25\%$
• $p_2 = k_2\hbar$ with probability $|\frac{\sqrt{3}}{2}|^2 = 75\%$

The **key insight:** When $\psi$ is a superposition, applying $\hat{p}$ gives different eigenvalues multiplied by their respective components. The measurement outcome is probabilistic, with probabilities given by $|c_n|^2$ where $c_n$ is the coefficient of each momentum eigenstate.

---

## Expected Value: The Average Measurement

What if we repeat the momentum measurement many times on identically prepared systems? We get an **average** or **expected value**.

For the unequal superposition above:

$$
\langle p \rangle = 25\% \cdot p_1 + 75\% \cdot p_2 = \frac{1}{4}(k_1\hbar) + \frac{3}{4}(k_2\hbar)
$$

There's a beautiful mathematical formula for this. For a superposition $\psi = c_1\psi_1 + c_2\psi_2$:

$$
\langle p \rangle = \langle\psi|\hat{p}|\psi\rangle = (c_1^*\langle\psi_1| + c_2^*\langle\psi_2|) \hat{p} (c_1|\psi_1\rangle + c_2|\psi_2\rangle)
$$

Expanding this out gives **four terms**:

$$
\langle p \rangle = |c_1|^2 \langle\psi_1|\hat{p}|\psi_1\rangle + |c_2|^2 \langle\psi_2|\hat{p}|\psi_2\rangle + c_1^*c_2 \langle\psi_1|\hat{p}|\psi_2\rangle + c_2^*c_1 \langle\psi_2|\hat{p}|\psi_1\rangle
$$

The last two terms are **cross terms** (mixing different states). Here's the key: when $\psi_1$ and $\psi_2$ are momentum eigenstates, these cross terms vanish:

$$
\langle\psi_1|\hat{p}|\psi_2\rangle = \langle\psi_1|p_2|\psi_2\rangle = p_2\langle\psi_1|\psi_2\rangle = 0
$$

The eigenvalue $p_2$ comes out, leaving just the overlap $\langle\psi_1|\psi_2\rangle = 0$ (eigenstates are orthogonal).

**Let's see this explicitly:** For plane waves $\psi_1 = e^{ik_1 x}$ and $\psi_2 = e^{ik_2 x}$:

$$
\langle\psi_1|\hat{p}|\psi_2\rangle = \int_{-\infty}^{\infty} e^{-ik_1 x} \cdot \left(-i\hbar\frac{d}{dx}e^{ik_2 x}\right) dx = -i\hbar(ik_2) \int_{-\infty}^{\infty} e^{-ik_1 x} e^{ik_2 x} dx
$$

$$
= \hbar k_2 \int_{-\infty}^{\infty} e^{i(k_2-k_1)x} dx = 0 \quad \text{(for } k_1 \neq k_2\text{)}
$$

The integral vanishes because plane waves with different wavenumbers are orthogonal. So we get:

$$
\langle p \rangle = |c_1|^2 p_1 + |c_2|^2 p_2
$$

In position space, this becomes:

$$
\langle p \rangle = \int_{-\infty}^{\infty} \psi^*(x)\left(-i\hbar\frac{d\psi}{dx}\right)dx
$$

**Why this form?** Break it down:

1. $-i\hbar\frac{d\psi}{dx}$ applies the momentum operator to $\psi$
2. Multiply by $\psi^*(x)$ (gives $|\text{amplitude}|^2$ weighting)
3. Integrate over all space (average over the distribution)

In abstract notation (works in any basis):

$$
\langle p \rangle = \langle\psi|\hat{p}|\psi\rangle
$$

This is called the **expectation value** or **quantum average** of the operator $\hat{p}$ in state $|\psi\rangle$.

**Two cases to remember:**

• **Eigenstate** (definite momentum): If $|\psi\rangle$ is a momentum eigenstate with momentum $p$, then $\langle\psi|\hat{p}|\psi\rangle = p$. You get exactly the eigenvalue — 100% certainty.

• **Superposition** (indefinite momentum): If $|\psi\rangle = c_1|\psi_1\rangle + c_2|\psi_2\rangle$ is a superposition of different momentum eigenstates, then $\langle\psi|\hat{p}|\psi\rangle = |c_1|^2 p_1 + |c_2|^2 p_2$ is a weighted average. Individual measurements give either $p_1$ or $p_2$, but the average over many measurements is this probabilistic mix.

**Key point:** Even though individual measurements give discrete eigenvalues ($p_1$ or $p_2$), the *average* over many measurements can be any value between them!

---

## Momentum Space: Flipping the Picture

So far we've worked in **position space** where $\psi(x)$ tells us about position. But we can also work in **momentum space** where $\tilde{\psi}(p)$ tells us about momentum!

### Position Space vs Momentum Space

Remember from [Foundations](quantum-foundations.md) that a wave packet can be written as:

$$
\psi(x) = \int_{-\infty}^{\infty} \tilde{\psi}(p) e^{ipx/\hbar} \frac{dp}{2\pi\hbar}
$$

Here $\tilde{\psi}(p)$ is the **momentum space wavefunction**. It tells you "how much of momentum $p$" is in your state.

**Connection to plane waves:** Each $e^{ipx/\hbar}$ is a momentum eigenstate. We're building $\psi(x)$ by adding up momentum eigenstates weighted by $\tilde{\psi}(p)$.

### Momentum Eigenstates in Momentum Space

For a momentum eigenstate (single plane wave), what does $\tilde{\psi}(p)$ look like?

If $\psi(x) = Ae^{ip_0 x/\hbar}$ (definite momentum $p_0$), then:

$$
\tilde{\psi}(p) = A' \delta(p - p_0)
$$

A **delta function!** All the "weight" is concentrated at exactly $p = p_0$.

**Physical meaning:** Measuring momentum gives $p_0$ with 100% certainty. The momentum space wavefunction is infinitely sharp at that value.

**Compare to position space:** A plane wave $e^{ipx/\hbar}$ is spread uniformly over all space (definite $p$, completely uncertain $x$). Its momentum representation is a delta spike (completely certain $p$).

This is the uncertainty principle in action: sharp in one space means spread in the other!

### The Momentum Operator in Momentum Space

Here's something beautiful. The *same operator* $\hat{p}$ acts differently depending on which representation you use.

**In position representation:**

$$
\hat{p}\psi(x) = -i\hbar\frac{d\psi}{dx}
$$

The operator acts as a derivative.

**In momentum representation:**

$$
\hat{p}\tilde{\psi}(p) = p\tilde{\psi}(p)
$$

The operator just multiplies by $p$. No derivatives needed!

**Why the difference?** We're working in the momentum basis, where momentum eigenstates are the basis states $|p\rangle$ themselves. Acting on an eigenstate just returns its eigenvalue.

Compare to position: in position space, $\hat{x}\psi(x) = x\psi(x)$ (multiply by $x$), but in momentum space, $\hat{x}$ would be $i\hbar\frac{d}{dp}$ (a derivative!).

**The key insight:** The abstract operator $\hat{p}$ is always the same physics. How it acts mathematically depends on which basis you've chosen to work in.

### Superposition in Momentum Space

For the two-plane-wave superposition:

$$
\psi(x) = c_1 e^{ip_1 x/\hbar} + c_2 e^{ip_2 x/\hbar}
$$

The momentum space wavefunction is:

$$
\tilde{\psi}(p) = c_1\delta(p-p_1) + c_2\delta(p-p_2)
$$

Two delta spikes! One at $p_1$ with weight $c_1$, one at $p_2$ with weight $c_2$.

Apply the momentum operator in momentum space:

$$
\hat{p}\tilde{\psi}(p) = p_1 c_1\delta(p-p_1) + p_2 c_2\delta(p-p_2)
$$

Different eigenvalues ($p_1$ and $p_2$) multiply their respective components. This is exactly what we saw in position space, but now it's crystal clear: **the delta spikes are the momentum eigenstates!**

The expected value becomes:

$$
\langle p \rangle = \int_{-\infty}^{\infty} \tilde{\psi}^*(p) \cdot p \cdot \tilde{\psi}(p) dp = |c_1|^2 p_1 + |c_2|^2 p_2
$$

The delta functions do the integration for us, picking out the eigenvalues weighted by their probabilities.

---

## Summary: Operators Extract Observable Information

**What we've learned:**

1. **Operators extract information:** $\hat{p} = -i\hbar\frac{d}{dx}$ extracts momentum from $\psi(x)$

2. **Eigenstates have definite values:** If $\hat{p}|\psi\rangle = p|\psi\rangle$, measuring momentum gives $p$ with 100% certainty

3. **Superpositions give probabilistic results:** If $|\psi\rangle = c_1|p_1\rangle + c_2|p_2\rangle$, you get $p_1$ or $p_2$ with probabilities $|c_1|^2$ and $|c_2|^2$

4. **Expected values average over many measurements:** $\langle p\rangle = \langle\psi|\hat{p}|\psi\rangle$

5. **Different bases, same physics:** In momentum space, eigenstates are delta functions $\delta(p-p_0)$ and $\hat{p}$ simply multiplies by $p$

This framework applies to **all quantum operators**: position, energy, angular momentum, etc. The mathematics is always the same — only the specific operator and basis change!

---

## The Energy Operator and Schrödinger's Equation

### Schrödinger's Equation as an Eigenvalue Problem

Remember from [Foundations](quantum-foundations.md) we derived Schrödinger's equation from the time and spatial derivatives of a plane wave. We found:

$$
i\hbar\frac{\partial\psi}{\partial t} = \hat{H}\psi
$$

where the **Hamiltonian operator** $\hat{H}$ represents the total energy:

$$
\hat{H} = \underbrace{\frac{\hat{p}^2}{2m}}_{\text{kinetic}} + \underbrace{V(x)}_{\text{potential}}
$$

**Why $\hat{H}$ instead of $\hat{E}$?** Pure historical convention from classical mechanics, where the Hamiltonian function represents total energy. We could have used $\hat{E}$ just like we use $\hat{p}$ for momentum, but "Hamiltonian" (named after physicist William Hamilton) became the standard term.

**What's the difference between $\hat{H}$ and $E$?**

• $\hat{H}$ is an **operator** — it acts on wavefunctions. When $\psi$ is an energy eigenstate, applying $\hat{H}$ gives $\hat{H}\psi = E\psi$ (the wavefunction back times a number). Like $\hat{p}$, it's used to calculate expectation values: $\langle E \rangle = \langle\psi|\hat{H}|\psi\rangle$.

• $E$ is a **scalar** (just a number) — the energy eigenvalue. It's the actual total energy value you'd measure.

**Important:** When you see "energy $E$" in quantum mechanics, it means **total energy** (kinetic + potential) unless otherwise specified. This is different from classical mechanics where we often track kinetic and potential energy separately.

**For a free particle** (no forces, so $V = 0$), the energy is purely kinetic:

$$
\hat{H} = \frac{\hat{p}^2}{2m} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}
$$

This is why plane wave energy $E = \frac{\hbar^2k^2}{2m}$ is just the kinetic energy formula $E = \frac{p^2}{2m}$ — there's nothing else!

### The Key Insight: Eigenvalue Equation for Time-Independent Potentials

Here's what we didn't emphasize in Foundations: **for time-independent potentials** (systems where $V(x)$ doesn't change with time), we can separate variables:

$$
\psi(x,t) = \psi(x)e^{-iEt/\hbar}
$$

Plugging this into Schrödinger's equation, the time part cancels out and we get:

$$
\hat{H}\psi(x) = E\psi(x)
$$

**This is literally an eigenvalue equation!**

Think about what you're solving for:

• You **know** the operator: $\hat{H}$ (you specify the potential $V(x)$ and mass $m$)
• You **don't know** the function: $\psi(x)$ (this is what you're solving for!)
• You **don't know** the constant: $E$ (what energies are allowed?)

You're looking for functions $\psi(x)$ that, when you apply $\hat{H}$ to them, give back the same function multiplied by a constant. Those special functions are the **eigenfunctions** (energy eigenstates) and those special constants are the **eigenvalues** (energy levels).

**What "solving Schrödinger's equation" really means:** You're finding eigenfunctions and eigenvalues of the Hamiltonian operator! Every solution $\psi(x)$ you find is automatically an energy eigenstate with a definite energy eigenvalue $E$.

**For a free particle:** Plane waves $\psi(x) = Ae^{ikx}$ are the energy eigenfunctions with eigenvalues $E = \frac{\hbar^2k^2}{2m}$. The energy spectrum is **continuous** — any $E \geq 0$ is allowed.

### Example 1: Single Plane Wave (Energy Eigenstate)

Consider an electron (mass $m_e = 9.11 \times 10^{-31}$ kg) in a single plane wave state:

$$
\psi(x) = A e^{ikx} \quad \text{where } k = 5 \times 10^{10}\text{ m}^{-1}
$$

The energy is:

$$
E = \frac{\hbar^2 k^2}{2m_e} = \frac{(1.055 \times 10^{-34})^2 (5 \times 10^{10})^2}{2(9.11 \times 10^{-31})} \approx 1.53 \times 10^{-18}\text{ J} \approx 9.6\text{ eV}
$$

Apply the Hamiltonian operator:

$$
\hat{H}\psi = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}\left(Ae^{ikx}\right) = -\frac{\hbar^2}{2m}(ik)^2 Ae^{ikx} = \frac{\hbar^2k^2}{2m}\psi = E\psi
$$

We get back **the same wavefunction** multiplied by the energy eigenvalue $E$.

**Physical meaning:** If you measure energy, you get $E = 9.6$ eV with **100% certainty**. Every single measurement gives the same result. The particle has **definite energy**.

### Example 2: Superposition of Two Plane Waves (NOT an Eigenstate)

Now consider a superposition of two plane waves with different wavenumbers:

$$
\psi(x) = \frac{1}{\sqrt{2}}\left(e^{ik_1 x} + e^{ik_2 x}\right)
$$

Let's use $k_1 = 3 \times 10^{10}$ m⁻¹ and $k_2 = 7 \times 10^{10}$ m⁻¹. These give different energies:

$$
E_1 = \frac{\hbar^2k_1^2}{2m_e} \approx 3.5\text{ eV}
$$

$$
E_2 = \frac{\hbar^2k_2^2}{2m_e} \approx 18.8\text{ eV}
$$

Apply the Hamiltonian:

$$
\hat{H}\psi = \frac{1}{\sqrt{2}}\left(\hat{H}e^{ik_1 x} + \hat{H}e^{ik_2 x}\right) = \frac{1}{\sqrt{2}}\left(E_1 e^{ik_1 x} + E_2 e^{ik_2 x}\right)
$$

**This is NOT equal to $E\psi$ for any single energy $E$!** Different eigenvalues ($E_1$ and $E_2$) multiply their respective components.

**Physical meaning:** This state is **not an energy eigenstate**. If you measure energy, you get:

• $E_1 = 3.5$ eV with probability $|\frac{1}{\sqrt{2}}|^2 = 50\%$
• $E_2 = 18.8$ eV with probability $|\frac{1}{\sqrt{2}}|^2 = 50\%$

The particle does **not** have definite energy! This is the same probabilistic measurement story we saw with the momentum operator.

Let's calculate the **expected value** explicitly using the expectation value formula. For our superposition $\psi = \frac{1}{\sqrt{2}}|E_1\rangle + \frac{1}{\sqrt{2}}|E_2\rangle$:

$$
\langle E \rangle = \langle\psi|\hat{H}|\psi\rangle = \left(\frac{1}{\sqrt{2}}\langle E_1| + \frac{1}{\sqrt{2}}\langle E_2|\right) \hat{H} \left(\frac{1}{\sqrt{2}}|E_1\rangle + \frac{1}{\sqrt{2}}|E_2\rangle\right)
$$

Expanding this gives four terms:

$$
\langle E \rangle = \frac{1}{2}\langle E_1|\hat{H}|E_1\rangle + \frac{1}{2}\langle E_2|\hat{H}|E_2\rangle + \frac{1}{2}\langle E_1|\hat{H}|E_2\rangle + \frac{1}{2}\langle E_2|\hat{H}|E_1\rangle
$$

The cross terms vanish (just like the momentum case):

$$
\langle E_1|\hat{H}|E_2\rangle = \langle E_1|E_2|E_2\rangle = E_2 \langle E_1|E_2\rangle = 0
$$

So we're left with:

$$
\langle E \rangle = \frac{1}{2}(3.5\text{ eV}) + \frac{1}{2}(18.8\text{ eV}) = 11.15\text{ eV}
$$

Even though individual measurements give either 3.5 eV or 18.8 eV, the *average* is 11.15 eV!

---

## Confined Particles and Discrete Energy Levels

### From Continuous to Discrete

So far, we've looked at **free particles** where the energy spectrum is continuous — any energy $E \geq 0$ is allowed. But what happens when we **confine** the particle?

**Boundary conditions change everything:**

• Add walls (particle in a box)
• Add a potential well
• Confine in an atom or molecule

When you confine a particle, the wavefunction must satisfy boundary conditions (like being zero at walls). This restricts which wavelengths — and therefore which wavenumbers $k$ — are allowed.

**Result:** Only certain discrete values of $k$ are permitted, which means only certain energies are allowed!

$$
E_1, E_2, E_3, \ldots \quad \text{(a discrete ladder of energy levels)}
$$

### Example: Particle in a Box

The simplest confined system is a particle trapped in a 1D box of length $L$ with infinitely high walls. The boundary conditions force the wavefunction to be zero at the walls.

**Energy eigenvalues:**

$$
E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}, \quad n = 1, 2, 3, \ldots
$$

**Energy eigenfunctions:**

$$
\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right), \quad 0 \leq x \leq L
$$

The quantum number $n$ labels the energy levels. The first few levels:

• $n=1$ (ground state): $E_1 = \frac{\pi^2\hbar^2}{2mL^2}$
• $n=2$ (first excited state): $E_2 = 4E_1$
• $n=3$ (second excited state): $E_3 = 9E_1$

Notice the energies grow as $n^2$ — the spacing between levels gets larger as you go up!

**For a concrete example:** An electron in a box of length $L = 1$ nm:

$$
E_1 = \frac{\pi^2(1.055 \times 10^{-34})^2}{2(9.11 \times 10^{-31})(10^{-9})^2} \approx 6.0 \times 10^{-20}\text{ J} \approx 0.38\text{ eV}
$$

Then $E_2 \approx 1.5$ eV, $E_3 \approx 3.4$ eV, etc.

**Key insight:** Confinement creates discrete energy levels. The smaller the box, the larger the energy spacing!

---

## Matrix Representation of Operators

### Discrete Basis → Operators Become Matrices

We've now seen two very different situations:

**Continuous basis (position $x$, momentum $p$):**
• Basis labels are continuous variables
• States are functions of continuous variables: $\psi(x)$ or $\tilde{\psi}(p)$
• Operators are differential operators (involve derivatives)

**Discrete basis (energy levels, quantum numbers):**
• Basis labels are discrete: $n = 1, 2, 3, \ldots$
• States written as sums over discrete basis states: $|E_1\rangle, |E_2\rangle, |E_3\rangle, \ldots$
• **Common examples:** energy levels, spin states (↑/↓), photon polarization (H/V)
• **Operators become matrices!**

**Why matrices?** Any quantum state can be written as a superposition of basis states:

$$
|\psi\rangle = c_1|E_1\rangle + c_2|E_2\rangle + c_3|E_3\rangle + \cdots
$$

We can represent this state as a **column vector** of coefficients:

$$
|\psi\rangle \leftrightarrow \begin{pmatrix} c_1 \\ c_2 \\ c_3 \\ \vdots \end{pmatrix}
$$

When an operator acts on a state, it becomes **matrix multiplication**!

### The Hamiltonian in the Energy Basis

Here's something beautiful: in its **own eigenbasis**, an operator is always **diagonal**.

The Hamiltonian in the energy basis is:

$$
\hat{H} = \begin{pmatrix}
E_1 & 0 & 0 & \cdots \\
0 & E_2 & 0 & \cdots \\
0 & 0 & E_3 & \cdots \\
\vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

The energy eigenvalues sit on the diagonal. All off-diagonal elements are zero.

**Why?** When you apply $\hat{H}$ to an eigenstate $|E_n\rangle$, you get $E_n|E_n\rangle$ — it just multiplies by the eigenvalue. No mixing with other states!

### Example: Two-Level System

Let's work with the simplest discrete system: **two energy levels**. This could represent:

• The first two levels of a particle in a box
• Two electronic states in an atom
• A spin-1/2 particle (coming later!)

**Setup:** Two energy eigenstates with energies $E_1 = 1$ eV and $E_2 = 3$ eV.

Basis states: $|E_1\rangle$ and $|E_2\rangle$

The Hamiltonian as a 2×2 matrix:

$$
\hat{H} = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix} \text{ eV}
$$

**Example A: Energy Eigenstate**

Consider the particle in the second excited state:

$$
|\psi\rangle = |E_2\rangle
$$

As a column vector:

$$
|\psi\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

Apply the Hamiltonian (matrix multiplication):

$$
\hat{H}|\psi\rangle = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 3 \end{pmatrix} = 3 \begin{pmatrix} 0 \\ 1 \end{pmatrix} = E_2|\psi\rangle
$$

We get back **the same state** multiplied by the eigenvalue $E_2 = 3$ eV.

**Physical meaning:** Measure energy → get 3 eV with **100% certainty**.

**Example B: Superposition State**

Now consider an equal superposition:

$$
|\psi\rangle = \frac{1}{\sqrt{2}}|E_1\rangle + \frac{1}{\sqrt{2}}|E_2\rangle
$$

As a column vector:

$$
|\psi\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

Apply the Hamiltonian:

$$
\hat{H}|\psi\rangle = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 3 \end{pmatrix}
$$

**This is NOT equal to $E|\psi\rangle$ for any single energy!** The components get multiplied by different eigenvalues (1 and 3).

**Physical meaning:** This is **not an energy eigenstate**. If you measure energy, you get:

• $E_1 = 1$ eV with probability $|\frac{1}{\sqrt{2}}|^2 = 50\%$
• $E_2 = 3$ eV with probability $|\frac{1}{\sqrt{2}}|^2 = 50\%$

The **expected value** (average over many measurements):

$$
\langle E \rangle = 50\% \cdot 1 + 50\% \cdot 3 = 2\text{ eV}
$$

Individual measurements give 1 eV or 3 eV, but the average is 2 eV!

**Using the matrix formula:**

$$
\langle E \rangle = \langle\psi|\hat{H}|\psi\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \end{pmatrix} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 3 \end{pmatrix} = \frac{1}{2}(1 + 3) = 2\text{ eV}
$$

The row vector $\langle\psi|$ is the conjugate transpose of $|\psi\rangle$.

### Example: Position Operator in Energy Basis

We saw that the Hamiltonian is diagonal in the energy basis. But what about other operators?

**Key principle:** An operator is diagonal **only in its own eigenbasis**. In other bases, it has off-diagonal elements.

Let's see this by calculating the expected position for a particle in a box in a superposition of energy states:

$$
|\psi\rangle = \frac{1}{\sqrt{2}}|E_1\rangle + \frac{1}{\sqrt{2}}|E_2\rangle
$$

Using the expectation value formula (same structure as before):

$$
\langle x \rangle = \langle\psi|\hat{x}|\psi\rangle = \frac{1}{2}\langle E_1|\hat{x}|E_1\rangle + \frac{1}{2}\langle E_2|\hat{x}|E_2\rangle + \frac{1}{2}\langle E_1|\hat{x}|E_2\rangle + \frac{1}{2}\langle E_2|\hat{x}|E_1\rangle
$$

**But this time the cross terms don't vanish!** Why? Because $|E_1\rangle$ and $|E_2\rangle$ are not position eigenstates. We can't pull out an eigenvalue, so orthogonality doesn't help us.

**What is $\langle E_m|\hat{x}|E_n\rangle$ mathematically?**

Here's the key: We're working in the **energy basis** (discrete, column vectors), but to **calculate** the matrix elements, we need to convert to position representation where we know the explicit forms of the energy eigenstates.

The energy eigenstate $|E_n\rangle$ (an abstract ket in energy basis) corresponds to a specific wavefunction $\psi_n(x)$ in position representation. For particle in a box:

$$
\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)
$$

These are the same states — just written in different representations! To calculate the matrix element $\langle E_m|\hat{x}|E_n\rangle$, we convert to position space:

$$
\langle E_m|\hat{x}|E_n\rangle = \int_0^L \psi_m^*(x) \cdot x \cdot \psi_n(x) \, dx = \frac{2}{L}\int_0^L x \sin\left(\frac{m\pi x}{L}\right) \sin\left(\frac{n\pi x}{L}\right) dx
$$

**Result of the integrals:**

• **Diagonal elements** ($m=n$): By symmetry, $\langle E_n|\hat{x}|E_n\rangle = \frac{L}{2}$ (expected position at center of box)

• **Off-diagonal elements** ($m \neq n$): These integrals are generally **non-zero**! Each integral gives you a single number.

These numbers become the entries in our matrix when we return to the energy basis representation (column vectors).

**Contrast with the Hamiltonian:**

$$
\langle E_m|\hat{H}|E_n\rangle = \int_0^L \psi_m^*(x) \hat{H}\psi_n(x) \, dx = E_n \int_0^L \psi_m^*(x) \psi_n(x) \, dx = E_n \cdot 0 = 0
$$

The eigenvalue $E_n$ comes out, leaving orthogonality → zero. But for $\hat{x}$, there's no eigenvalue to extract!

**Matrix representation:** These $\langle E_m|\hat{x}|E_n\rangle$ values are the matrix elements. For a 2-level system:

$$
\hat{x} \approx \begin{pmatrix} L/2 & x_{12} \\ x_{21} & L/2 \end{pmatrix}
$$

where $x_{12}$ and $x_{21}$ are the off-diagonal matrix elements.

**The key insight:** Every operator is diagonal in its own eigenbasis, but appears as a more complex matrix in other bases.

---

## Summary: Energy, Schrödinger's Equation, and Matrices

**What we've learned:**

1. **Time derivative extracts energy:** Just like spatial derivative $\frac{\partial}{\partial x}$ extracts momentum, time derivative $\frac{\partial}{\partial t}$ extracts energy: $i\hbar\frac{\partial\psi}{\partial t} = E\psi$

2. **Hamiltonian = total energy operator:** $\hat{H} = \frac{\hat{p}^2}{2m} + V(x)$ represents kinetic + potential energy. Energy eigenvalue $E$ always means total energy (unlike classical mechanics where we often separate KE and PE).

3. **Schrödinger's equation is an eigenvalue equation:** For time-independent potentials, "solving Schrödinger's equation" means finding energy eigenfunctions and eigenvalues: $\hat{H}\psi(x) = E\psi(x)$

4. **Free particles: continuous spectrum:** Plane wave solutions $\psi(x) = Ae^{ikx}$ with $E = \frac{\hbar^2k^2}{2m}$ (purely kinetic). Any energy $E \geq 0$ is allowed.

5. **Confined particles: discrete spectrum:** Boundary conditions restrict allowed wavelengths, creating discrete energy levels $E_1, E_2, E_3, \ldots$ (Example: particle in box with $E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}$)

6. **Discrete basis → matrix representation:** When working with discrete energy levels:
   • States become column vectors: $|\psi\rangle = c_1|E_1\rangle + c_2|E_2\rangle \rightarrow \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$
   • Operators become matrices
   • Operator action = matrix multiplication

7. **Operators are diagonal in their own eigenbasis:** $\hat{H}$ in energy basis has eigenvalues on diagonal. In other bases (like position operator in energy basis), matrices have off-diagonal elements.

8. **Same probabilistic measurement framework:** Whether continuous (plane waves) or discrete (energy levels), superposition states give probabilistic measurement outcomes with probabilities $|c_n|^2$.

**The big picture:** Quantum operators extract observable quantities through eigenvalue equations. The mathematical form changes (derivatives vs matrices) depending on whether you're working with continuous or discrete bases, but the physics — eigenstates, eigenvalues, and probabilistic measurements — remains the same!

---

## What Changes With Problem vs Basis?

This can be confusing, so let's be crystal clear about what changes when:

### What Changes With the Physical Problem

The **Hamiltonian** $\hat{H}$ changes depending on the physical system:

• Free particle: $\hat{H} = \frac{\hat{p}^2}{2m}$ (just kinetic energy)
• Particle in box: $\hat{H} = \frac{\hat{p}^2}{2m}$ + infinite walls at boundaries
• Harmonic oscillator: $\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2\hat{x}^2$
• Hydrogen atom: $\hat{H} = \frac{\hat{p}^2}{2m} - \frac{e^2}{4\pi\epsilon_0 r}$

Different Hamiltonians → different energy eigenvalues and eigenfunctions!

**Other operators don't change:** The position operator $\hat{x}$, momentum operator $\hat{p}$, etc. are the same for all problems. They're fundamental quantum observables.

### What Changes With the Basis You Choose

The **mathematical form** of operators changes depending on which basis you write $\psi$ in:

| Operator | Position Basis $\psi(x)$ | Momentum Basis $\tilde{\psi}(p)$ | Energy Basis $c_n$ (discrete) |
|----------|----------|----------|----------|
| $\hat{x}$ | multiply by $x$ | $i\hbar\frac{d}{dp}$ | off-diagonal matrix |
| $\hat{p}$ | $-i\hbar\frac{d}{dx}$ | multiply by $p$ | off-diagonal matrix |
| $\hat{H}$ | $-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)$ | $\frac{p^2}{2m} + V(i\hbar\frac{d}{dp})$ | diagonal matrix (eigenvalues $E_n$) |

**Key insight:** Same operator, different mathematical representation. The physics (eigenvalues, expected values) doesn't change—only how you calculate them!

**Example:** The momentum operator $\hat{p}$ is always the same abstract operator. But:
• In position basis: it's the derivative $-i\hbar\frac{d}{dx}$
• In momentum basis: it just multiplies by $p$
• In energy basis: it's a matrix with off-diagonal elements

Which basis you use is your choice. Pick whichever makes the calculation easiest!
