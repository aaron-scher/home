# Quantum Mechanics

## Hand-Wavey Quick Derivation to Schrödinger's Equation

Let's start with a free particle (no potential, just moving in space) and work backwards to get Schrödinger's equation.

### Using Properties of Light to Derive Wave Properties of Matter

**For photons (light):**

- **Energy:** Planck (blackbody radiation) and Einstein (photoelectric effect, 1905) showed \(E = h\nu\)
- **Momentum:** Classical EM says light carries momentum (radiation pressure). Compton scattering (1923) proved it experimentally: photons bounce off electrons like billiard balls with \(p = h/\lambda\)

**de Broglie's leap (1924):** "If light waves have particle properties, maybe particles have wave properties with the same relations?"

Bold assumption, but it worked. Electron diffraction experiments confirmed it.

### Basic Assumptions (de Broglie)

So we assume matter waves behave like photons:

**Energy:**

\begin{equation}
E = h\nu = \hbar\omega
\end{equation}

**Momentum:**

\begin{equation}
p = \hbar k
\end{equation}

where \(\hbar = h/2\pi\), \(k\) is wave number, and \(\omega\) is angular frequency.

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

Now let's take some derivatives and see what happens.

**Time derivative:**

\begin{equation}
\frac{\partial \psi}{\partial t} = -i\omega \psi = -i\frac{E}{\hbar}\psi
\end{equation}

Multiply both sides by \(i\hbar\):

\begin{equation}
i\hbar \frac{\partial \psi}{\partial t} = E\psi
\end{equation}

**Spatial derivative (twice):**

\begin{equation}
\frac{\partial^2 \psi}{\partial x^2} = -k^2 \psi = -\frac{p^2}{\hbar^2}\psi
\end{equation}

Rearrange:

\begin{equation}
-\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2} = \frac{p^2}{2m}\psi
\end{equation}

**Connecting energy and momentum:**

From classical mechanics, kinetic energy is:

\begin{equation}
E = \frac{p^2}{2m}
\end{equation}

For a **free particle** (no potential), total energy = kinetic energy. So we can set our two results equal:

\begin{equation}
i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2}
\end{equation}

**That's Schrödinger's equation for a free particle!**

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
