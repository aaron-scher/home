# Quantum Mechanics

## Fundamentals

### Wave Function

The wave function \(\psi(x,t)\) contains all information about a quantum system:

\begin{equation}
\psi(x,t) = A e^{i(kx - \omega t)}
\end{equation}

### Schrödinger Equation

Time-dependent:

\begin{equation}
i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi
\end{equation}

Time-independent:

\begin{equation}
\hat{H}\psi = E\psi
\end{equation}

where \(\hat{H}\) is the Hamiltonian operator:

\begin{equation}
\hat{H} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)
\end{equation}

## Key Concepts

### Operators

- Position: \(\hat{x} = x\)
- Momentum: \(\hat{p} = -i\hbar\frac{\partial}{\partial x}\)
- Energy (Hamiltonian): \(\hat{H} = \frac{\hat{p}^2}{2m} + V(\hat{x})\)

### Commutators

\begin{equation}
[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}
\end{equation}

Heisenberg uncertainty principle:

\begin{equation}
[\hat{x}, \hat{p}] = i\hbar
\end{equation}

\begin{equation}
\Delta x \Delta p \geq \frac{\hbar}{2}
\end{equation}

## Standard Problems

### Particle in a Box

Energy levels:

\begin{equation}
E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}, \quad n = 1, 2, 3, ...
\end{equation}

Wave functions:

\begin{equation}
\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)
\end{equation}

### Harmonic Oscillator

Energy levels:

\begin{equation}
E_n = \hbar\omega\left(n + \frac{1}{2}\right), \quad n = 0, 1, 2, ...
\end{equation}

### Hydrogen Atom

Energy levels:

\begin{equation}
E_n = -\frac{13.6 \text{ eV}}{n^2}, \quad n = 1, 2, 3, ...
\end{equation}

## Quick Reference

**Constants:**
- \(\hbar = 1.055 \times 10^{-34}\) J·s
- Electron mass: \(m_e = 9.109 \times 10^{-31}\) kg
- Proton mass: \(m_p = 1.673 \times 10^{-27}\) kg

**Common conversions:**
- 1 eV = \(1.602 \times 10^{-19}\) J
- \(k_B T\) at room temp ≈ 0.026 eV
