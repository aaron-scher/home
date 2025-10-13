# Quantum Mechanics

## Hand-Wavey Quick Derivation to Schrödinger's Equation

Let's start with a free particle (no potential, just moving in space) and work backwards to get Schrödinger's equation.

### de Broglie Relations (1924)

By the 1920s, light was known to have both wave and particle properties:
- Planck & Einstein showed photons have energy \(E = h\nu\)
- Compton scattering (1923) confirmed photons have momentum \(p = h/\lambda\)

**de Broglie's leap:** If light waves have particle properties, maybe particles have wave properties with the same relations?

For matter waves, we use:

\begin{equation}
E = \hbar\omega, \quad p = \hbar k
\end{equation}

where \(\hbar = h/2\pi\), \(k\) is wave number, and \(\omega\) is angular frequency. Electron diffraction experiments soon confirmed it.

### Free Particle Wave Function

A free particle moving in space can be described as a plane wave. We have two options:

1. **Real wave:** \(A\cos(kx - \omega t)\)
2. **Complex wave (phasor):** \(A e^{i(kx - \omega t)}\)

**Why use the complex form?**

- We know waves interfere (double slit experiment) - they add in and out of phase
- The cosine form can be written as a phasor using Euler's equation: \(e^{i\theta} = \cos\theta + i\sin\theta\)
- We need to calculate probability (which should always be positive, not oscillating between + and -)
- Complex form makes this easy: probability = \(|\psi|^2 = \psi^* \psi\) (multiply by complex conjugate)

So we use:

\begin{equation}
\psi(x,t) = A e^{i(kx - \omega t)}
\end{equation}

### Deriving Schrödinger's Equation

Now let's take derivatives and use the de Broglie relations to connect them.

**Time derivative:**

\begin{equation}
\frac{\partial \psi}{\partial t} = -i\omega \psi
\end{equation}

Using \(E = \hbar\omega\):

\begin{equation}
\frac{\partial \psi}{\partial t} = -i\frac{E}{\hbar}\psi
\end{equation}

Multiply both sides by \(i\hbar\):

\begin{equation}
i\hbar \frac{\partial \psi}{\partial t} = E\psi
\end{equation}

**Spatial derivative (twice):**

\begin{equation}
\frac{\partial^2 \psi}{\partial x^2} = (ik)^2 \psi = -k^2 \psi
\end{equation}

Using \(p = \hbar k\):

\begin{equation}
\frac{\partial^2 \psi}{\partial x^2} = -\frac{p^2}{\hbar^2}\psi
\end{equation}

Multiply both sides by \(-\hbar^2/2m\):

\begin{equation}
-\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2} = \frac{p^2}{2m}\psi
\end{equation}

**Setting them equal:**

For a free particle, classical mechanics says \(E = p^2/2m\). So:

\begin{equation}
E\psi = \frac{p^2}{2m}\psi
\end{equation}

Therefore our two derivative expressions must be equal:

\begin{equation}
i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2}
\end{equation}

**That's Schrödinger's equation for a free particle!**

**What does this mean?** The time derivative extracts energy from the wave, the spatial derivative extracts kinetic energy (from momentum). For a free particle these are the same thing, so we get one equation. It's the quantum version of \(E = p^2/2m\).

### Adding a Potential

If the particle is in a potential \(V(x)\), total energy = KE + PE:

\begin{equation}
i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2} + V(x)\psi
\end{equation}

Or more compactly:

\begin{equation}
i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi
\end{equation}

where \(\hat{H} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)\) is the Hamiltonian operator.

---

## Building Intuition: From Wave Packets to Stationary States

### Position and Momentum Space (Fourier Transform)

A single plane wave \(e^{ikx}\) extends forever - not realistic for a localized particle.

**Real particles are wave packets.** Consider a state at fixed energy \(E\). We've factored out the time part \(e^{-iEt/\hbar}\), so we're looking at just the spatial part \(\psi(x)\). Start simple - add a few plane waves with different momenta:

\begin{equation}
\psi(x) = A_1 e^{ik_1 x} + A_2 e^{ik_2 x} + A_3 e^{ik_3 x} + \cdots
\end{equation}

Each \(A_n\) tells you the amplitude and phase of momentum \(k_n\). As a sum:

\begin{equation}
\psi(x) = \sum_n A_n e^{ik_n x}
\end{equation}

Now take the limit: spacing between \(k\) values → 0, sum → integral. The discrete amplitudes \(A_n\) become a continuous function \(\tilde{\psi}(k)\):

\begin{equation}
\psi(x) = \int_{-\infty}^{\infty} \tilde{\psi}(k) e^{ikx} dk
\end{equation}

That's the **Fourier transform**. \(\tilde{\psi}(k)\) tells you "how much of momentum \(k\)" is in your wave packet.

**Key insight:** You can't have both narrow at once.
- Narrow in position (localized) → wide spread in momentum
- Narrow in momentum (definite p) → spread out in space
- This is the **uncertainty principle**!

**Quick derivation:** From Fourier theory (like time-bandwidth product in signal processing), a wave packet localized to width \(\Delta x\) needs a spread in \(k\) of roughly \(\Delta k \sim 1/\Delta x\). Since \(p = \hbar k\), we have \(\Delta p = \hbar \Delta k\), giving:

\begin{equation}
\Delta x \cdot \Delta p \sim \hbar
\end{equation}

The rigorous proof (using the commutator \([\hat{x},\hat{p}] = i\hbar\)) gives \(\Delta x \cdot \Delta p \geq \hbar/2\).

### Time-Independent Schrödinger Equation

Now let's think about the **time derivative** in Schrödinger's equation.

From \(i\hbar \frac{\partial \psi}{\partial t} = E\psi\), we see: higher energy → faster time oscillation.

For states with **definite energy** (energy eigenstates), we can separate variables:

\begin{equation}
\psi(x,t) = \psi(x) e^{-iEt/\hbar}
\end{equation}

The time part is just a rotating phase \(e^{-i\omega t}\) where \(\omega = E/\hbar\). All the physics (probability, where the particle is) lives in \(\psi(x)\).

Plug this back into Schrödinger's equation:

\begin{equation}
i\hbar \frac{\partial}{\partial t}\left[\psi(x) e^{-iEt/\hbar}\right] = \hat{H}\left[\psi(x) e^{-iEt/\hbar}\right]
\end{equation}

The time derivative just brings down \(-iE/\hbar\), which cancels the \(i\hbar\), leaving:

\begin{equation}
E\psi(x) = \hat{H}\psi(x)
\end{equation}

Or written out fully:

\begin{equation}
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi
\end{equation}

**That's the time-independent Schrödinger equation.** It's an eigenvalue equation: find the functions \(\psi(x)\) and energies \(E\) that satisfy it.

### Intuition: Wiggliness vs Potential

Here's the key physical insight from the time-independent equation.

Rearrange it:

\begin{equation}
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = [E - V(x)]\psi
\end{equation}

The left side is the **kinetic energy** (related to momentum, which is about wiggliness). The right side is \(E - V(x)\).

Since total energy \(E = KE + PE\), we have \(KE = E - V(x)\).

**What this means:**

- **Low potential** (\(V\) small) → high kinetic energy → high momentum → \(\psi\) is very wiggly (large \(d^2/dx^2\))
- **High potential** (\(V\) large) → low kinetic energy → low momentum → \(\psi\) is less wiggly (small \(d^2/dx^2\))

The equation literally says: **the spatial wiggliness equals the kinetic energy**!

When you solve for \(\psi(x)\), it automatically adjusts its wiggliness to match the local kinetic energy. In regions where potential is low, the wave function oscillates rapidly. Where potential is high, it oscillates slowly (or even decays exponentially if \(V > E\)).

---

## Standard Problems (Quick Reference)

### Particle in a Box

Infinite walls at \(x=0\) and \(x=L\).

**Energy levels:**

\begin{equation}
E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}, \quad n = 1, 2, 3, ...
\end{equation}

**Wave functions:**

\begin{equation}
\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)
\end{equation}

### Harmonic Oscillator

Spring potential: \(V(x) = \frac{1}{2}m\omega^2 x^2\)

**Energy levels:**

\begin{equation}
E_n = \hbar\omega\left(n + \frac{1}{2}\right), \quad n = 0, 1, 2, ...
\end{equation}

Note: Ground state has \(E_0 = \frac{1}{2}\hbar\omega\) (zero-point energy).

### Hydrogen Atom

**Energy levels:**

\begin{equation}
E_n = -\frac{13.6 \text{ eV}}{n^2}, \quad n = 1, 2, 3, ...
\end{equation}

Ground state: \(n=1\), \(E_1 = -13.6\) eV

---

## Useful Operators

- **Position:** \(\hat{x} = x\)
- **Momentum:** \(\hat{p} = -i\hbar\frac{\partial}{\partial x}\)
- **Hamiltonian (Energy):** \(\hat{H} = \frac{\hat{p}^2}{2m} + V(\hat{x})\)

### Heisenberg Uncertainty Principle

\begin{equation}
\Delta x \Delta p \geq \frac{\hbar}{2}
\end{equation}

You can't know both position and momentum exactly at the same time.

---

## Constants

- \(\hbar = 1.055 \times 10^{-34}\) J·s
- Electron mass: \(m_e = 9.109 \times 10^{-31}\) kg
- 1 eV = \(1.602 \times 10^{-19}\) J
- Room temperature: \(k_B T \approx 0.026\) eV
