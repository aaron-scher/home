# Velocity in Quantum Mechanics: A Complete Tutorial

## Introduction: Why Is Velocity Confusing in Quantum Mechanics?

In classical mechanics, velocity is simple: $v = dx/dt$, a single number telling you how fast something moves. In quantum mechanics, things get messier because particles don't have definite positions or momenta—they have wavefunctions. This leads to *multiple* velocity concepts, each answering a different question.

This tutorial will give you the intuition to immediately recognize which velocity concept applies to any situation. We'll derive everything from first principles so you understand *where* each definition comes from, not just memorize formulas.

---

## Part 1: The Foundation—Ehrenfest's Theorem

Everything starts here. Ehrenfest's theorem tells us how expectation values evolve in time, bridging quantum mechanics to classical intuition.

### Starting Point: The Schrödinger Equation

The time-dependent Schrödinger equation governs quantum evolution:

$$i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi$$

Taking the complex conjugate (and using that $\hat{H}$ is Hermitian, so $\hat{H}^\dagger = \hat{H}$):

$$-i\hbar \frac{\partial \psi^*}{\partial t} = \hat{H}\psi^*$$

### Deriving the General Form

For any operator $\hat{A}$, the expectation value is:

$$\langle A \rangle = \int \psi^* \hat{A} \psi \, dx$$

Taking the time derivative (using the product rule on three terms):

$$\frac{d\langle A \rangle}{dt} = \int \left(\frac{\partial \psi^*}{\partial t} \hat{A} \psi + \psi^* \hat{A} \frac{\partial \psi}{\partial t} + \psi^* \frac{\partial \hat{A}}{\partial t} \psi \right) dx$$

Substituting from the Schrödinger equation:

$$\frac{d\langle A \rangle}{dt} = \int \left(\frac{-\hat{H}\psi^*}{i\hbar} \hat{A} \psi + \psi^* \hat{A} \frac{\hat{H}\psi}{i\hbar} + \psi^* \frac{\partial \hat{A}}{\partial t} \psi \right) dx$$

Rearranging:

$$\frac{d\langle A \rangle}{dt} = \frac{1}{i\hbar} \int \psi^* (\hat{A}\hat{H} - \hat{H}\hat{A}) \psi \, dx + \left\langle \frac{\partial \hat{A}}{\partial t} \right\rangle$$

This gives us **Ehrenfest's Theorem**:

$$\boxed{\frac{d\langle A \rangle}{dt} = \frac{1}{i\hbar}\langle[\hat{A}, \hat{H}]\rangle + \left\langle \frac{\partial \hat{A}}{\partial t} \right\rangle}$$

**Physical meaning**: The rate of change of any expectation value depends on (1) how the operator fails to commute with the Hamiltonian, and (2) any explicit time dependence of the operator itself.

---

## Part 2: Deriving the Velocity Operator

Now let's apply Ehrenfest's theorem to the position operator $\hat{x}$ to find what "velocity" means quantum mechanically.

### Applying to Position

Set $\hat{A} = \hat{x}$. Since $\hat{x}$ has no explicit time dependence ($\frac{\partial \hat{x}}{\partial t} = 0$):

$$\frac{d\langle x \rangle}{dt} = \frac{1}{i\hbar}\langle[\hat{x}, \hat{H}]\rangle$$

Now we need to compute the commutator $[\hat{x}, \hat{H}]$ for different Hamiltonians.

### Case 1: Free Particle ($V = 0$)

For a free particle: $\hat{H} = \frac{\hat{p}^2}{2m}$

Calculate the commutator:

$$[\hat{x}, \hat{H}] = \left[\hat{x}, \frac{\hat{p}^2}{2m}\right] = \frac{1}{2m}[\hat{x}, \hat{p}^2]$$

To evaluate $[\hat{x}, \hat{p}^2]$, use the identity $[\hat{A}, \hat{B}\hat{C}] = \hat{B}[\hat{A}, \hat{C}] + [\hat{A}, \hat{B}]\hat{C}$:

$$[\hat{x}, \hat{p}^2] = [\hat{x}, \hat{p}\cdot\hat{p}] = \hat{p}[\hat{x}, \hat{p}] + [\hat{x}, \hat{p}]\hat{p}$$

Using the canonical commutation relation $[\hat{x}, \hat{p}] = i\hbar$:

$$[\hat{x}, \hat{p}^2] = \hat{p}(i\hbar) + (i\hbar)\hat{p} = 2i\hbar\hat{p}$$

Therefore:

$$[\hat{x}, \hat{H}] = \frac{1}{2m}(2i\hbar\hat{p}) = \frac{i\hbar\hat{p}}{m}$$

Substituting back into Ehrenfest's theorem:

$$\frac{d\langle x \rangle}{dt} = \frac{1}{i\hbar} \cdot \frac{i\hbar\langle\hat{p}\rangle}{m} = \frac{\langle\hat{p}\rangle}{m}$$

### Case 2: Particle in a Potential ($V \neq 0$)

For a particle in a potential: $\hat{H} = \frac{\hat{p}^2}{2m} + V(\hat{x})$

$$[\hat{x}, \hat{H}] = \left[\hat{x}, \frac{\hat{p}^2}{2m}\right] + [\hat{x}, V(\hat{x})]$$

The first term we already calculated. For the second term:

$$[\hat{x}, V(\hat{x})] = \hat{x}V(\hat{x}) - V(\hat{x})\hat{x} = 0$$

**This is zero because $\hat{x}$ commutes with any function of itself!** Position doesn't care what potential it's in—it's still just position.

Therefore:

$$[\hat{x}, \hat{H}] = \frac{i\hbar\hat{p}}{m}$$

And again:

$$\frac{d\langle x \rangle}{dt} = \frac{\langle\hat{p}\rangle}{m}$$

### The Velocity Operator

Since $\frac{d\langle x \rangle}{dt}$ represents the average velocity, and we found it equals $\frac{\langle\hat{p}\rangle}{m}$, we identify the **velocity operator**:

$$\boxed{\hat{v} = \frac{\hat{p}}{m}}$$

**This is remarkable**: The velocity operator is $\hat{p}/m$ whether the particle is free or in a potential—the potential doesn't appear!

### Physical Interpretation

This matches classical intuition perfectly:

- The velocity *at any instant* depends only on the momentum *at that instant*
- The potential $V(x)$ affects the **acceleration** (how velocity changes over time), not the instantaneous velocity
- In classical mechanics: $v = p/m$ regardless of forces. Same in quantum mechanics!

---

## Part 3: Wave Velocities—Phase and Group

When we have propagating waves, two more velocity concepts emerge from the wave nature of the solutions.

### Phase Velocity: Speed of the Crests

For a plane wave $\psi = Ae^{i(kx - \omega t)}$, surfaces of constant phase satisfy:

$$kx - \omega t = \text{constant}$$

Differentiating: $k\,dx - \omega\,dt = 0$, so:

$$v_{\text{ph}} = \frac{dx}{dt} = \frac{\omega}{k}$$

**What it means**: This is the speed at which a particular wave crest (or trough) moves through space.

For a free quantum particle with $E = \hbar\omega$ and $p = \hbar k$:

$$\omega = \frac{E}{\hbar} = \frac{p^2}{2m\hbar} = \frac{\hbar k^2}{2m}$$

So:

$$v_{\text{ph}} = \frac{\omega}{k} = \frac{\hbar k}{2m} = \frac{p}{2m}$$

**Note**: This is *half* the classical velocity! Phase velocity alone doesn't tell you how fast the particle moves.

### Group Velocity: Speed of the Envelope

A wave packet is a superposition of many plane waves:

$$\psi(x,t) = \int A(k) e^{i(kx - \omega(k) t)} dk$$

If the packet is peaked around $k_0$, the envelope moves at:

$$v_g = \frac{d\omega}{dk}\bigg|_{k=k_0}$$

**Derivation sketch**: Expand $\omega(k)$ around $k_0$: $\omega(k) \approx \omega_0 + \omega'_0(k-k_0)$. The phase becomes:

$$kx - \omega t \approx k_0 x - \omega_0 t + (k-k_0)(x - \omega'_0 t)$$

The envelope (the $A(k)$ contribution) depends on $(x - \omega'_0 t)$, so it moves at speed $\omega'_0 = d\omega/dk$.

For a free particle:

$$v_g = \frac{d\omega}{dk} = \frac{d}{dk}\left(\frac{\hbar k^2}{2m}\right) = \frac{\hbar k}{m} = \frac{p}{m}$$

**This matches the classical velocity!** The group velocity tells you how fast the probability "bump" actually moves.

### The Key Relationship

For a free particle:

$$v_g = 2 \, v_{\text{ph}} = \frac{p}{m} = \langle \hat{v} \rangle$$

The group velocity equals the expectation value of the velocity operator—this is the "real" speed of the particle.

---

## Part 4: When Does Each Velocity Apply?

This is the crucial practical knowledge. Here's when each concept is meaningful:

### Velocity Operator $\hat{v} = \hat{p}/m$

**Always exists.** It's an operator—a mathematical object that acts on wavefunctions.

- **What it does**: When acting on $\psi$, it transforms the wavefunction according to momentum/mass
- **Eigenvalue equation**: $\hat{v}\psi = v\psi$ only when $\psi$ is a momentum eigenstate (plane wave)
- **General case**: $\hat{v}\psi$ gives some other function, not a multiple of $\psi$

### Group Velocity $v_g = d\omega/dk$

**Requires**: Propagating waves with a dispersion relation $\omega(k)$

Works for:
- Free particles (wave packets)
- Bloch waves in crystals: $v_g = \frac{1}{\hbar}\frac{dE_n}{dk}$
- Waveguides, phonons, any dispersive medium

Does **NOT** work for:
- Standing waves (particle in a box)
- Bound states with discrete spectra
- Single plane waves (need a packet!)

### Phase Velocity $v_{\text{ph}} = \omega/k$

**Requires**: A single plane wave with definite $k$

- More of a mathematical curiosity in quantum mechanics
- Doesn't represent particle motion
- Can exceed the speed of light without violating relativity (no information transfer)

### Expectation Velocity $\langle \hat{v} \rangle = d\langle x \rangle/dt$

**Requires**: Normalizable wavefunction

- This is the "average velocity" from Ehrenfest's theorem
- Equals $\langle \hat{p} \rangle / m$ for any potential
- The closest quantum analog to classical velocity

---

## Part 5: Quick Reference Tables

### Table 1: The Four Velocity Concepts

| Concept | Type | Definition | Formula | Requirements |
|---------|------|------------|---------|--------------|
| **Velocity Operator** | OPERATOR | Heisenberg equation of motion | $\hat{v} = \frac{\hat{p}}{m}$ | None—always valid |
| **Group Velocity** | NUMBER | Envelope speed of wave packet | $v_g = \frac{d\omega}{dk}\big\|_{k_0}$ | Dispersion relation, wave packet |
| **Phase Velocity** | NUMBER | Crest speed of single wave | $v_{\text{ph}} = \frac{\omega}{k}$ | Single plane wave |
| **Expectation Velocity** | NUMBER | Average position motion | $v_{\text{exp}} = \frac{d\langle x \rangle}{dt} = \frac{\langle \hat{p} \rangle}{m}$ | Normalizable $\psi$ |

### Table 2: Which Velocities Work in Each System?

| System | Wavefunction | Operator $\hat{v}$ | Group $v_g$ | Phase $v_{\text{ph}}$ | Expectation $\langle \hat{v} \rangle$ |
|--------|--------------|-------------------|-------------|---------------------|--------------------------------------|
| **Plane wave** | $e^{i(kx-\omega t)}$ | ✓ (eigenstate) | ✗ (need packet) | ✓ | ✗ (not normalizable) |
| **Free wave packet** | $\int A(k)e^{ikx}dk$ | ✓ | ✓ | ✓ (per mode) | ✓ (equals $v_g$) |
| **Particle in box** | $\sin(n\pi x/L)$ | ✓ | ✗ (discrete $k$) | — | ✓ (equals 0) |
| **Harmonic oscillator** | $\psi_n(x)$ | ✓ | ✗ (no $k$) | — | ✓ (equals 0 for $\psi_n$) |
| **Bloch wave in crystal** | $u_k(x)e^{ikx}$ | ✓ | ✓ | ✓ | ✓ |

### Table 3: Concrete Numbers (Electron Example)

Parameters: $m = 9.1 \times 10^{-31}$ kg, $k = 5 \times 10^6$ m$^{-1}$

| Quantity | Value | Calculation |
|----------|-------|-------------|
| Momentum | $p = \hbar k = 5.3 \times 10^{-25}$ kg·m/s | $p = (1.055 \times 10^{-34})(5 \times 10^6)$ |
| Classical/Group velocity | $v_g = 5.8 \times 10^5$ m/s | $v_g = p/m = \hbar k/m$ |
| Phase velocity | $v_{\text{ph}} = 2.9 \times 10^5$ m/s | $v_{\text{ph}} = \hbar k/(2m) = v_g/2$ |
| Eigenvalue of $\hat{v}$ | $5.8 \times 10^5$ m/s | Same as $v_g$ (for plane wave) |

---

## Part 6: Deep Dive—What Does the Velocity Operator Actually Do?

This is often confusing. Let's be precise:

### Acting on an Eigenstate

If $\psi$ is a momentum eigenstate (plane wave $e^{ikx}$):

$$\hat{v}\psi = \frac{\hat{p}}{m}\psi = \frac{\hbar k}{m}\psi = v_{\text{eigen}}\psi$$

The wavefunction just gets multiplied by a number—the velocity eigenvalue. This is the *only* case where the velocity "is" a definite number.

### Acting on a General State

For anything else (Gaussian packet, bound state, etc.):

$$\hat{v}\psi = \frac{\hat{p}}{m}\psi = \frac{-i\hbar}{m}\frac{\partial \psi}{\partial x}$$

This gives a *different function*, not a multiple of $\psi$. The particle doesn't have a definite velocity!

### Measurement

When you measure velocity:
- You get one eigenvalue randomly
- Probability of getting $v$ is $|\langle v | \psi \rangle|^2$
- After measurement, the state collapses to that eigenstate
- Repeated measurements give the average $\langle \hat{v} \rangle$

### Summary

Think of the velocity operator as a "velocity measuring machine recipe":
- It transforms wavefunctions according to momentum
- Only eigenstates give definite velocity values
- For general states, you get probabilities and averages

---

## Part 7: Intuition Summary

**When you see "velocity" in a QM problem, ask:**

1. **Is it an operator?** → Then it's $\hat{v} = \hat{p}/m$, valid always

2. **Is it a number describing wave propagation?**
   - Envelope speed → Group velocity $v_g = d\omega/dk$
   - Crest speed → Phase velocity $v_{\text{ph}} = \omega/k$

3. **Is it "how fast is the particle moving on average"?** → Expectation value $\langle \hat{v} \rangle = \langle \hat{p} \rangle / m$

4. **Is the particle in a potential?** → Doesn't matter! All these definitions still apply the same way.

**The elegant unity**: For a free particle wave packet, all the "number" velocities agree:

$$v_g = \langle \hat{v} \rangle = \frac{p_0}{m}$$

And this is exactly what classical mechanics says: $v = p/m$.

---

## Appendix: Extensions to Crystals

In a periodic potential (crystal), electrons are described by Bloch waves with band structure $E_n(k)$. The group velocity becomes:

$$v_g = \frac{1}{\hbar}\frac{dE_n}{dk}$$

This is crucial in solid-state physics:
- Near band edges, $dE/dk \approx 0$, so electrons slow down
- Effective mass: $m^* = \hbar^2 / (d^2E/dk^2)$ can be negative!
- The velocity operator still applies, but now includes crystal momentum

The key insight: **group velocity works whenever you have propagating waves with a dispersion relation**—not just free particles.

---

*This page was written with the assistance of Claude (Anthropic).*
