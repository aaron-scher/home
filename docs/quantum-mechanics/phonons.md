# Phonons: What They Are and How They Hit Electrons

## The Two-Layer Picture

Solid-state physics is built on a sneaky trick: we solve for electrons assuming the ions are frozen in place, *then* we let the ions move and treat it as a perturbation.

**Layer 1 — Frozen lattice (idealization):**
You solve Schrödinger's equation for an electron in a perfectly periodic potential $V(\mathbf{r})$. The solutions are Bloch states $|n,\mathbf{k}\rangle$ — the "alphabet" for describing electrons. These are exact eigenstates, and in this frozen world, electrons never scatter.

> **Notation:** $|n,\mathbf{k}\rangle$ is Dirac notation for a Bloch wavefunction. Here $n$ is the band index (which energy band) and $\mathbf{k}$ is the crystal momentum (wavevector in the Brillouin zone). In position space, this state has the form $\psi_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r})$, where $u$ has the periodicity of the lattice.

**Layer 2 — Moving lattice (reality):**
Ions vibrate. The potential becomes time-dependent: $V(\mathbf{r},t) = V_0(\mathbf{r}) + \delta V(\mathbf{r},t)$. That $\delta V$ is made of normal modes. Quantize those modes → phonons. Electrons scatter: $|\mathbf{k}\rangle \rightarrow |\mathbf{k} \pm \mathbf{q}\rangle$.

> **Notation:** When we write $|\mathbf{k}\rangle$ (dropping the band index $n$), we're assuming the electron stays in the same band during scattering. The arrow $|\mathbf{k}\rangle \rightarrow |\mathbf{k} \pm \mathbf{q}\rangle$ means the electron's crystal momentum changes by $\pm\mathbf{q}$ (the phonon's wavevector) — plus for absorption, minus for emission.

```
┌──────────────────────────────────────────────────────────────┐
│ Layer 1: Frozen lattice (idealization)                       │
│   ions fixed → V(r) periodic → Bloch states |n,k⟩            │
│   (alphabet for electrons)                                   │
└──────────────────────────────────────────────────────────────┘
                 ↓ now un-freeze the ions
┌──────────────────────────────────────────────────────────────┐
│ Layer 2: Moving lattice (reality)                            │
│   ions wiggle → V(r,t) = V₀(r) + δV(r,t)                     │
│   δV is made of normal modes → quantize → phonons            │
│   electrons scatter: |k⟩ → |k±q⟩                             │
└──────────────────────────────────────────────────────────────┘
```

> **Scope note:** This tutorial is metal-first. Many simple metals (Cu, Al, Na) are monatomic Bravais lattices with only acoustic phonon branches. Optical phonons are most important in polar semiconductors (GaAs), ionic crystals (NaCl), and high-field transport.

### Mental Model Map

```
Frozen lattice (idealization)
  └─→ Schrödinger equation → Bloch states (alphabet for electrons)

Allow ions to move (reality)
  └─→ Newton's equations → normal modes (CLASSICAL waves)
      └─→ Quantization → phonons (energy quanta ℏω)

Phonons present
  └─→ Time-dependent potential perturbation
      └─→ Electrons scatter (Δk, ΔE conserved with phonon)

Macroscopic result
  └─→ Resistivity, velocity limits, thermal conductivity
```

---

## Part 1: The 1D Monatomic Chain — Where Phonons Come From

### The Toy Model

Picture a line of identical atoms, each with mass $M$, connected by springs of stiffness $K$, spaced by lattice constant $a$:

```
    K       K       K       K
○───⊏⊐⊏⊐───○───⊏⊐⊏⊐───○───⊏⊐⊏⊐───○───⊏⊐⊏⊐───○
   M        M        M        M        M
   |<--a-->|
```

Let $u_n(t)$ be the displacement of atom $n$ from its equilibrium position.

### Newton's Law for Atom $n$

Each atom feels spring forces from its two neighbors:

$$
M\frac{d^2 u_n}{dt^2} = K(u_{n+1} - u_n) - K(u_n - u_{n-1}) = K(u_{n+1} - 2u_n + u_{n-1})
$$

This is just $F = ma$ with Hooke's law springs on both sides.

### The Traveling Wave Solution

Try a plane wave:

$$
u_n(t) = A \, e^{i(kna - \omega t)}
$$

Plug into Newton's law, do some algebra (the $e^{i(kna-\omega t)}$ cancels), and you get the **dispersion relation**:

$$
\omega(k) = 2\sqrt{\frac{K}{M}} \left|\sin\left(\frac{ka}{2}\right)\right|
$$

This tells you how frequency depends on wavevector — the phonon's "E vs k" curve.

```
ω
│            ⌢⌢⌢
│         ⌢'     '⌢         v_g = dω/dk
│      ⌢'           '⌢      (slope of curve)
│   ⌢'                 '⌢
├──┼─────────┼──────────┼──── k
  -π/a       0         +π/a
       First Brillouin Zone

Near k≈0: slope ≈ sound speed (linear dispersion)
Near zone edge: slope → 0  (standing-wave-like)
```

### Numerical Example: Copper

Let's plug in real numbers:

- $M = 63.5$ amu $= 1.05 \times 10^{-25}$ kg
- $a = 0.36$ nm (lattice constant)
- $K \approx 14$ N/m (effective spring constant from elastic modulus)

Maximum frequency (at zone edge $k = \pi/a$):

$$
\omega_{\max} = 2\sqrt{\frac{K}{M}} = 2\sqrt{\frac{14}{1.05 \times 10^{-25}}} \approx 2.3 \times 10^{13} \text{ rad/s}
$$

Converting:
- $f_{\max} = \omega_{\max}/2\pi \approx 3.7$ THz
- $\hbar\omega_{\max} \approx 15$ meV

So the highest-energy acoustic phonons in copper carry about 15 meV — compare this to room temperature thermal energy $k_B T \approx 26$ meV.

### What the Phase Does

A normal mode means *every atom oscillates at the same frequency*, but with a phase that shifts along the chain:

```
Equilibrium positions:
|----a----|----a----|----a----|----a----|
○         ○         ○         ○         ○

Traveling wave u_n(t) = A cos(kna - ωt):

t = 0:      ↑     ↑     ↑     ↑     ↑
t = T/4:    →     ↑     ←     ↓     →
t = T/2:    ↓     ↓     ↓     ↓     ↓
```

The pattern travels — that's what makes it a wave.

---

## Part 2: Quantization — From Waves to Phonons

### The Critical Clarification

> **The normal modes and dispersion relation are CLASSICAL.** They come from Newton's equations, not Schrödinger. Quantization does NOT change the mode shapes or dispersion; it only discretizes the **energy** in each mode.

### The Quantum Step

Here's how we bridge from Newton to quantum — no Schrödinger equation for atom positions!

**Step 1: Rewrite in normal mode coordinates.** The displacements $u_n(t)$ can be decomposed into independent normal modes. Define a collective coordinate $Q_k$ for each mode:

$$
u_n(t) = \frac{1}{\sqrt{N}} \sum_k Q_k(t) \, e^{ikna}
$$

> **Why a discrete sum, not an integral?** With $N$ atoms in your chain, there are exactly $N$ independent ways to wiggle them — hence $N$ normal modes with $N$ allowed $k$ values. This comes from boundary conditions (periodic: $u_{n+N} = u_n$, which forces $e^{ikNa} = 1$, so $k = 2\pi m / Na$ for $m = 0, 1, ..., N-1$). In the thermodynamic limit $N \to \infty$, the spacing between $k$ values shrinks to zero and the sum becomes an integral: $\frac{1}{N}\sum_k \to \frac{a}{2\pi}\int dk$.

> **Why complex exponentials?** This is shorthand. The physical displacement $u_n$ must be real. To get a real $u_n$ from this sum, we need $Q_{-k} = Q_k^*$ (complex conjugate). Then $Q_k e^{ikna} + Q_{-k} e^{-ikna} = 2\text{Re}[Q_k e^{ikna}]$, which is real. The complex form is mathematically cleaner than writing cosines with phases.

> **What's $na$?** It's the position of atom $n$ along the chain. In a continuous medium you'd write $e^{ikx}$; here we only have atoms at discrete positions $x_n = na$ (where $a$ is the lattice spacing), so we write $e^{ikna}$.

Each $Q_k$ evolves independently: $\ddot{Q}_k = -\omega_k^2 Q_k$. This is just a harmonic oscillator equation for $Q_k$.

**Step 2: Quantize each oscillator.** The energy (Hamiltonian) for mode $k$ is:

$$
H_k = \frac{P_k^2}{2M_{\text{eff}}} + \frac{1}{2}M_{\text{eff}}\omega_k^2 Q_k^2
$$

> **What's the Hamiltonian?** It's just total energy = kinetic + potential. This formula exists in classical mechanics too (Hamilton wrote it down in the 1830s, before quantum mechanics). The first term is kinetic energy, the second is potential energy of a spring.

Now we *do* use Schrödinger — but for the collective coordinate $Q_k$, not for individual atom positions. Since $H_k$ has the form of a harmonic oscillator, we know the answer: promote $Q_k$ and $P_k$ to operators, and the energy eigenvalues are $(n + \frac{1}{2})\hbar\omega$.

> **Key insight:** There *is* a wavefunction — it's $\Psi(Q_k)$, a function of the collective coordinate (like the Gaussian ground state of a harmonic oscillator). But we almost never write it. Instead, we just track the occupation number $n_k$ (how many phonons in mode $k$).

Each normal mode (each $k$) is mathematically a harmonic oscillator. When you quantize it (standard QM harmonic oscillator), you get discrete energy levels:

$$
E_n = \left(n + \frac{1}{2}\right)\hbar\omega
$$

where $n = 0, 1, 2, 3, \ldots$

**A phonon is one quantum of energy $\hbar\omega$ in that mode** — not the wave itself.

```
Harmonic oscillator levels for one mode (q):
E
│        (5)  (n+½)ℏω
│        (4)
│        (3)
│        (2)
│        (1)
│        (0)  zero-point = ½ℏω
├──────────────────────────────→ n
      each step = ℏω = one phonon
```

> **Important — Amplitude is NOT quantized!** You might think: classically $E = \frac{1}{2}m\omega^2 A^2$, so if energy is discrete, shouldn't amplitude be discrete too? No! In quantum mechanics, the system doesn't have a definite amplitude — the wavefunction $\Psi(Q)$ is *spread out* over different $Q$ values. The ground state is a Gaussian centered at $Q=0$; excited states spread wider. You can *measure* any displacement value; what's quantized is the **energy eigenvalue**, not the position. (Same story for a particle in a box: position is continuous, energy levels are discrete.)

### The Photon Analogy

| Electromagnetic Field | Lattice Vibrations |
|----------------------|-------------------|
| EM mode (k, polarization) | Vibration mode (q, branch) |
| Photon = 1 quantum of EM energy | Phonon = 1 quantum of vibrational energy |
| n photons → E-field amplitude $\propto \sqrt{n}$ | n phonons → displacement amplitude $\propto \sqrt{n}$ |
| Large n → classical EM wave | Large n → classical sound wave |

When many phonons occupy a mode, it looks like a classical wave. When $n$ is small (or zero), quantum effects dominate.

### Numerical Example: How Many Phonons?

Consider a mode at $\omega = 2\pi \times 1$ THz:

- One phonon energy: $\hbar\omega = 4.1$ meV
- Thermal energy at 300K: $k_B T = 26$ meV

The average occupation (Bose-Einstein statistics):

$$
\langle n \rangle = \frac{1}{e^{\hbar\omega/k_B T} - 1} = \frac{1}{e^{4.1/26} - 1} \approx 5.3 \text{ phonons}
$$

So at room temperature, this mode has about 5 phonons on average — firmly in the "classical-looking" regime.

---

## Part 3: Longitudinal vs Transverse — This is About Polarization

This classification is about the **direction of displacement** relative to propagation:

```
Propagation direction:  ─────>  k

LA (longitudinal acoustic): compression / dilation
○───> ○───> ○───> ○───> ○───>
(atoms move parallel to wave propagation)

TA (transverse acoustic): shear-like wiggle
○  ^  ○  v  ○  ^  ○  v  ○  ^
(atoms move perpendicular to wave propagation)
```

**In 3D crystals:**
- 1 longitudinal branch (compression wave)
- 2 transverse branches (two perpendicular shear directions)
- Total: 3 acoustic branches for a monatomic crystal

**Key point:** Longitudinal/transverse is a **separate concept** from acoustic/optical. You can have:
- Longitudinal acoustic (LA)
- Transverse acoustic (TA)
- Longitudinal optical (LO)
- Transverse optical (TO)

---

## Part 4: Acoustic vs Optical — The REAL Distinction

This is where most tutorials fail you. Here's the clean version:

> **Optical phonons exist ONLY if the unit cell has more than one atom.**

### The Rule

| Crystal Type | Example | Phonon Branches |
|--------------|---------|-----------------|
| Monatomic | Cu, Al, Na | Acoustic only (LA + 2×TA) |
| Diatomic | Si, GaAs, NaCl | Acoustic + Optical |

### The 1D Diatomic Chain

Now put *two different* atoms in each unit cell:

```
    K       K       K       K       K
●───⊏⊐⊏⊐───○───⊏⊐⊏⊐───●───⊏⊐⊏⊐───○───⊏⊐⊏⊐───●
  M₁       M₂       M₁       M₂       M₁
  |<──────── a ────────>|
       primitive unit cell
```

Now you get **two solutions** — two branches in the dispersion:

### ACOUSTIC Branch (Lower Energy)

```
Equilibrium:
A   B   A   B   A   B
●   ○   ●   ○   ●   ○

ACOUSTIC (long wavelength): all atoms move IN PHASE
→   →   →   →   →   →
●   ○   ●   ○   ●   ○

The whole lattice sloshes together like a sound wave.
At k→0: ω→0 (this is the defining property!)
```

> **"Acoustic" means $\omega \to 0$ as $q \to 0$** — NOT "always low frequency."
> Near the zone edge, acoustic phonons can have very high frequencies!

```
Acoustic branch: ω→0 at k→0  (that's the definition)

ω
│         acoustic can be HIGH here
│                 ^
│                 │
│              ⌢' '⌢
│           ⌢'       '⌢
│        ⌢'             '⌢
├───────┼───────────────────┼──── k
        0                 π/a
```

### OPTICAL Branch (Higher Energy)

```
Equilibrium:
A   B   A   B   A   B
●   ○   ●   ○   ●   ○

OPTICAL (any wavelength): basis atoms move OUT OF PHASE
→   ←   →   ←   →   ←
●   ○   ●   ○   ●   ○

The two atoms in each unit cell push against each other.
At k=0: ω ≠ 0! (finite minimum energy)
```

**Why "optical"?** In ionic crystals like NaCl, the + and − ions moving against each other creates an oscillating electric dipole. This couples directly to electromagnetic radiation (infrared light) — hence "optical."

### Numerical Example: GaAs

- LO phonon at k=0: $\hbar\omega_{LO} = 36$ meV
- TO phonon at k=0: $\hbar\omega_{TO} = 33$ meV
- Thermal energy at 300K: $k_B T = 26$ meV

Optical phonons require significant energy to excite — they're not easily populated at room temperature.

### The Full Picture

```
Diatomic chain (two atoms per unit cell):  ... A B A B A B ...

Equilibrium:
A   B   A   B   A   B
●   ○   ●   ○   ●   ○

ACOUSTIC (k→0): in-phase (whole lattice sloshes together)
→   →   →   →   →   →
●   ○   ●   ○   ●   ○
ω → 0 as k → 0

OPTICAL (k→0): out-of-phase within the unit cell
→   ←   →   ←   →   ←
●   ○   ●   ○   ●   ○
ω ≠ 0 at k = 0
```

---

## Part 5: Phonon Dispersion — The Phonon "Band Structure"

Just like electrons have $E(\mathbf{k})$ curves, phonons have $\omega(\mathbf{q})$ curves. For a diatomic crystal:

```
ℏω
│    ____________________   Optical branches (LO, TO)
│   /                    \    ← gap (if M₁ ≠ M₂)
│  │                      │
│──┼──────────────────────┼──
│   \                    /   Acoustic branches (LA, TA)
│    \__________________/
│
├─────────┼───────────┼───────→ k
       -π/a          π/a
```

Key features:
- **Acoustic branches** touch zero at $k=0$
- **Optical branches** have finite frequency at $k=0$
- **Gap between branches** (in diatomic crystals with $M_1 \neq M_2$)
- **Group velocity** $v_g = d\omega/dk$ → zero at zone boundaries

---

## Part 6: The Moving Walls Model — How Phonons Affect Electrons

Here's the key intuition for electron-phonon coupling, borrowed from basic quantum mechanics.

### Static Box = Frozen Lattice

A particle in a box with fixed walls:

```
Static box: sharp energy levels
0 │====================│ L₀
    ψ_n fits cleanly

Electron sits in eigenstate ψ_n forever.
Energy sharp. Position delocalized.
```

### Oscillating Walls = Phonons

Now let the walls move:

$$
L(t) = L_0 + \delta L \cos(\Omega t)
$$

```
Moving wall: L(t) = L₀ + δL cos(Ωt)
0 │==================│ L(t)
    boundary shakes → ψ_n mixes with ψ_m
```

The oscillating boundary forces the electron into a **superposition of energy levels**. It can no longer sit quietly in a single eigenstate.

### The Mapping to Phonons

| Moving Box | Crystal with Phonons |
|------------|---------------------|
| Wall oscillation frequency $\Omega$ | Phonon frequency $\omega_q$ |
| Energy pumped by walls | Energy exchanged with phonon ($\hbar\omega$) |
| No momentum exchange (1D box) | Phonon carries crystal momentum $\hbar q$ |
| Resonance at $\Omega = (E_2-E_1)/\hbar$ | Resonance when energy/momentum conserved |

---

## Part 7: Electron-Phonon Scattering — The Actual Physics

### What the Electron Sees

A phonon creates a traveling deformation in the lattice potential:

$$
\delta V(x,t) \approx A \cos(qx - \omega t)
$$

Think of it as a **moving diffraction grating** — a traveling Bragg reflector that diffracts the electron wave.

```
Phonon makes the potential look like a moving ripple:

δV(x,t) ~ cos(qx - ωt)

x →
~~~~~~~^^^^^^~~~~~~~^^^^^^~~~~~~~    (peaks move right)

Electron sees a moving diffraction grating:
k  →  k ± q   (plus possibly +G)
```

### Conservation Laws

When an electron absorbs or emits a phonon:

```
Phonon absorption:           Phonon emission:
k' = k + q                   k' = k - q
E' = E + ℏω                  E' = E - ℏω
(phonon destroyed)           (phonon created)
```

Phonons are quantized — you absorb or emit the *whole* phonon, not a piece of it.

### Umklapp (Zone Folding)

Sometimes $k + q$ lands outside the first Brillouin zone. No problem — fold it back:

$$
k' = k \pm q + G
$$

where $G$ is a reciprocal lattice vector.

```
k-space (1D):
... │───│───│───│───│───│───│ ...
    -2π/a  -π/a  0  +π/a +2π/a

1st Brillouin zone: [-π/a, +π/a]

Normal:    k' = k + q      stays in same zone
Umklapp:   k' = k + q - G  folds back into 1st zone

k+q  (lands outside zone)  ───>  subtract G  ───>  folded k'
```

### Numerical Example: Scattering in Copper

Electron near the Fermi surface:
- $k_F \approx 13.6$ nm$^{-1}$
- $E_F \approx 7$ eV

Acoustic phonon:
- $q \approx 1$ nm$^{-1}$
- $\hbar\omega \approx 5$ meV

After absorbing the phonon:
- New wavevector: $k' \approx 14.6$ nm$^{-1}$
- Momentum change: **significant** ($\Delta k/k \sim 7\%$)
- Energy change: **tiny** (5 meV vs 7000 meV, or 0.07%)

```
E
│     E_F  _______________________
│         /                       \
│        /                         \
│_______/___________________________\_____ k
          k_F

phonon scattering mostly changes direction on the Fermi surface
(energy shift is small: meV vs eV)

ΔE:  │·│      Δk: │──────────│
     meV           big
```

**This is why acoustic phonon scattering randomizes direction but barely changes speed.**

---

## Part 8: Physical Consequences

### Acoustic Phonon Scattering (Low Fields, Moderate T)

Acoustic phonons modulate the lattice spacing → compression/dilation → band edges shift locally. Electrons scatter off these potential variations.

- Small energy transfer per scattering event
- Large angle scattering (momentum randomized)
- Dominates resistivity at moderate temperatures: $\rho \propto T$ at high $T$

### Optical Phonon Scattering (High Fields)

Optical phonons have a **minimum energy** ($\sim$30-60 meV). An electron needs at least this much kinetic energy to emit one.

```
E_electron
│
│     /  ← electron gains energy from field
│    /
│───/────ℏω_opt──── threshold
│  /     ↓ emit optical phonon, lose energy
│ /
│/__________________ k
```

Once an electron reaches the threshold, it can efficiently dump energy by emitting optical phonons. This causes **velocity saturation** in semiconductors — no matter how hard you push, the electron can't go faster because it keeps emitting optical phonons.

### Temperature Dependence

Higher $T$ → more phonons → more scattering → lower mobility

At high temperature, phonon occupation goes as:
$$
\langle n \rangle \approx \frac{k_B T}{\hbar\omega}
$$

So scattering rate (and resistivity) grows roughly linearly with $T$.

---

## Quick Reference Summary

### What's Classical vs Quantum

| Aspect | Classical or Quantum? |
|--------|----------------------|
| Normal modes, shapes, dispersion $\omega(q)$ | **Classical** (Newton) |
| Energy quantization $E = (n+\frac{1}{2})\hbar\omega$ | **Quantum** |
| Displacement amplitude | Continuous (any value) |
| Energy in a mode | Discrete ($\hbar\omega$ chunks) |

### Phonon Basics

- **Mode** = collective oscillation with wavevector $q$, frequency $\omega(q)$
- **Phonon** = one quantum of energy $\hbar\omega$ in that mode (NOT the wave itself)
- **Large amplitude** ≈ many phonons (classical limit)

### Acoustic vs Optical (Memorize This)

| Property | Acoustic | Optical |
|----------|----------|---------|
| Atoms move... | In phase (together) | Out of phase (against each other) |
| At $k \to 0$... | $\omega \to 0$ | $\omega \neq 0$ (finite minimum) |
| Exists in... | ALL crystals | Only if >1 atom per unit cell |
| Common misconception | "Low frequency" — **wrong!** Can be high near zone edge | — |

### Longitudinal vs Transverse

- **Longitudinal:** displacement parallel to propagation (compression wave)
- **Transverse:** displacement perpendicular to propagation (shear wave)
- **SEPARATE concept from acoustic/optical!**

### Electron-Phonon Interaction

- **Bloch states** = exact solutions for frozen lattice (the alphabet)
- **Phonon** = traveling potential perturbation on that frozen-lattice solution
- **Transfers:** energy $\hbar\omega$ and crystal momentum $\hbar q$ (mod $G$)
- **Acoustic scattering:** randomizes direction, small $\Delta E$
- **Optical scattering:** large $\Delta E$, velocity saturation mechanism
