# Electrons in Metals: From Bloch Waves to Wave Packets

## What Problem We're Really Solving

You've encountered two conflicting stories about electrons in metals:

**Classical story:** Electrons are little charged particles that move, scatter off ions, and drift through a lattice like pinballs.

**Quantum story:** Electrons occupy Bloch states, fill energy bands, and have well-defined crystal momentum $\mathbf{k}$.

Both stories are *partly true*, but they apply in **different limits**. Confusion comes from mixing them without stating assumptions.

Our goal is to build a **single, unified picture** that:

- Is fully quantum at its core
- Reduces to classical intuition when appropriate
- Makes sense of phonons, scattering, and wave packets
- Sets the stage for conductivity (without doing transport yet)

We're building the *kinematic and quantum foundation* here.

---

## Part 1: The Ideal Starting Point

### A Frozen, Infinite Crystal

We begin with a deliberately unrealistic but extremely clarifying limit.

**Assumptions (state them explicitly):**

1. **Infinite crystal** — the ionic lattice extends forever in all directions, no surfaces
2. **Perfect periodicity** — the ionic potential satisfies $V(\mathbf{r} + \mathbf{R}) = V(\mathbf{r})$ for all lattice vectors $\mathbf{R}$
3. **Ions are frozen** — no thermal motion, no phonons, time-independent Hamiltonian
4. **Single-electron picture** — electron-electron interactions absorbed into an effective periodic potential

Under these assumptions, the single-electron Hamiltonian is:

$$
H = \frac{p^2}{2m} + V(\mathbf{r})
$$

This Hamiltonian has **exact discrete translational symmetry**.

---

### Why Bloch Waves Exist

Because of that symmetry, the Schrödinger equation admits solutions of the form:

$$
\psi_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} \, u_{n\mathbf{k}}(\mathbf{r})
$$

where $u_{n\mathbf{k}}(\mathbf{r})$ has the same periodicity as the lattice.

**What matters conceptually:**

- Each $(n, \mathbf{k})$ labels an **exact energy eigenstate**
- Energy depends on $\mathbf{k}$, forming **bands**: $E = E_n(\mathbf{k})$
- These eigenstates are **stationary**: their probability density doesn't change in time
- For a fixed $\mathbf{k}$, the state evolves only by a global phase:

$$
\psi_{n\mathbf{k}}(\mathbf{r},t) = \psi_{n\mathbf{k}}(\mathbf{r}) \, e^{-iE_n(\mathbf{k})t/\hbar}
$$

**Key insight:** A Bloch state has a *perfectly defined* crystal momentum $\mathbf{k}$. Here $\mathbf{k}$ is a symmetry label, not the electron's mechanical momentum. By Fourier duality:

- Perfectly sharp $\mathbf{k}$ $\rightarrow$ completely delocalized in space

> In this ideal limit, each electron literally extends across the entire crystal — a direct mathematical consequence of symmetry.

---

### Where Bands Come From Physically

While Bloch's theorem tells us bands must exist given perfect symmetry, it doesn't explain their **origin or width**.

Physically, bands arise from **atomic orbitals splitting** when isolated atoms come together to form a crystal:

• **Isolated atom:** Each electron occupies a discrete atomic orbital (e.g., 1s, 2s, 2p)
• **Bring atoms close:** Orbitals on neighboring atoms overlap
• **Crystal forms:** Each atomic level splits into $N$ slightly different energies (where $N$ is the number of atoms), forming a band

**Key physical insight:**

• **Strong orbital overlap** → wide bands → highly delocalized states (e.g., conduction electrons)
• **Weak orbital overlap** → narrow bands → more atom-like behavior (e.g., core electrons, d-electrons in transition metals)

This explains why:

• Deep core electrons barely feel the crystal — their wavefunctions overlap weakly
• Valence electrons form wide bands — their wavefunctions extend between atoms
• Phonons disrupt some states more than others — delocalized states couple more strongly to lattice motion

---

### Filling the Bands: Electrons in Equilibrium

At zero temperature:

- Electrons fill the lowest available Bloch states
- Pauli exclusion enforces one electron per $(n, \mathbf{k}, \text{spin})$
- The many-electron ground state is built from **pure Bloch waves**

**Important conceptual point:** In this limit:

- Electrons are **not particles moving through space**
- They are **stationary quantum states**
- Talking about trajectories or collisions is meaningless

This is the cleanest possible starting point.

!!! warning "Clarification used throughout this tutorial"
    When we say "an electron occupies a Bloch state," we are using shorthand. The *many-electron ground state* has Bloch symmetry; individual electrons are not independently observable objects with fixed identities. "An electron in state $\mathbf{k}$" really means: the single-particle excitations are labeled by Bloch quantum numbers.

---

### Why Energy Eigenstates Are Stationary

You might wonder: why do electrons settle into pure energy eigenstates rather than arbitrary superpositions?

The key is **stationarity**, not energetics.

Consider a superposition of two energy eigenstates:

$$
\Psi(x,t) = c_1 \phi_1(x) e^{-iE_1 t/\hbar} + c_2 \phi_2(x) e^{-iE_2 t/\hbar}
$$

The probability density $|\Psi|^2$ **oscillates in time** at frequency $(E_2 - E_1)/\hbar$. The state has internal time structure.

But in the frozen crystal:

- There is nothing external oscillating at that frequency
- There is nothing for this time structure to couple to
- The superposition has no way to exchange energy with its environment

> The reason Bloch states dominate in the frozen crystal is not that superpositions are energetically forbidden, but that they introduce internal time dependence in a system with nothing to couple to that time structure.

Superpositions are allowed and persist forever in a perfectly isolated system; they are simply not stationary because observables oscillate in time. Energy eigenstates are the natural "resting states" — not because other states are unstable, but because they are the only ones that are truly stationary.

---

## Part 2: The Crucial Pivot

This is the most important conceptual turn in the entire tutorial:

> **Bloch waves exist because of symmetry, not because of energetics.**

Here is the canonical statement to remember:

> **Once translational symmetry is even weakly broken, exact Bloch eigenstates no longer exist; what survives are long-lived, Bloch-like quasiparticles.**

And in the real world, symmetry is always broken — by lattice motion, defects, surfaces, and finite size.

---

## Part 3: Reality Enters — Lattice Motion and Phonons

### What Phonons Are

At any finite temperature, ions vibrate. But even at absolute zero, quantum mechanics forces **zero-point motion** — a consequence of the uncertainty principle.

These vibrations are not random noise. They organize into **normal modes**: collective oscillations where each mode has a wavevector $\mathbf{q}$ and frequency $\omega_{\mathbf{q}}$. Quantizing these modes gives phonons.

Each mode is a harmonic oscillator with energy levels:

$$
E_n = \hbar\omega\left(n + \frac{1}{2}\right)
$$

The $\frac{1}{2}\hbar\omega$ zero-point energy is unavoidable — even at $T=0$, the lattice jiggles.

---

### Two Flavors of Phonons

Not all phonons are alike. The two main types behave very differently:

```
ACOUSTIC: neighbors move together         OPTICAL: neighbors move opposite

  ●  ○  ●  ○  ●  ○   equilibrium           ●  ○  ●  ○  ●  ○   equilibrium

  → → → → → →                              → ← → ← → ←
  ●  ○  ●  ○  ●  ○   displaced             ●  ○  ●  ○  ●  ○   displaced
     \____/                                   \/    \/
   move together                           push apart

(● and ○ = two atom types; optical modes require 2+ atoms per unit cell)
```

**Acoustic phonons:**

- Neighboring atoms move *in phase* — the whole lattice compresses and stretches
- Called "acoustic" because long wavelengths behave like sound waves
- Linear dispersion at small $q$: $E \approx \hbar v_s q$
- Dominate ordinary scattering at moderate temperatures

**Optical phonons:**

- Neighboring atoms move *out of phase* — one sublattice against another
- Called "optical" because in ionic crystals, opposite motion of +/− ions creates an oscillating dipole that couples to infrared light
- Have a minimum energy even at $q = 0$ (typically tens of meV)
- Important for high-field transport: emitting an optical phonon is an efficient "energy dump"

Both types scatter electrons, but through different mechanisms and at different energy scales.

---

## Part 4: The Key Toy Model — Particle in a Box with Moving Walls

This model captures the *essential physics* of how lattice motion affects electrons. It's the cleanest bridge between basic Schrödinger physics and electron-phonon intuition.

---

### Static Box (Baseline)

**Assumptions:**

- 1D, one electron
- Infinite walls at $x = 0$ and $x = L$
- Walls do not move
- Time-independent Hamiltonian

The Schrödinger equation inside the box:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi
$$

**Solutions:**

$$
\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)
$$

$$
E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}
$$

**What matters physically:**

- Each $\psi_n$ has a **single, sharp energy**
- The probability density $|\psi_n|^2$ does not change in time
- This is the analog of a Bloch wave in a frozen crystal

---

### Now Make the Walls Move

Let:

$$
L(t) = L_0 + \delta L \cos(\Omega t), \quad \delta L \ll L_0
$$

This does **two critical things**:

1. The boundary conditions now depend on time
2. The Hamiltonian now depends on time

This immediately means:

> **Energy is no longer conserved for the electron alone.**

---

### How to Think About the Solution (No Heavy Math)

At each instant, the electron *tries* to look like one of the original box states. So we write:

$$
\Psi(x,t) \approx c_1(t)\psi_1(x) + c_2(t)\psi_2(x) + c_3(t)\psi_3(x)
$$

You can imagine more terms, but three is enough for intuition.

**What do these coefficients mean?**

- $|c_n(t)|^2$ = probability of being in energy level $n$
- If walls are static: one $c_n = 1$, the rest are zero
- If walls move: **the $c_n$'s change in time**

---

### Why Moving Walls Cause Energy Level Mixing

The key physical idea:

- Moving the walls changes the *shape* of the allowed wavefunctions
- The old eigenstates are no longer exact solutions
- The electron must "borrow" pieces of other states to stay consistent

Mathematically (but gently):

$$
\frac{dc_m}{dt} \propto \cos(\Omega t) \times (\text{overlap integrals})
$$

**What matters:**

- The cosine term is the **energy pump**
- The overlaps determine **which states can mix**
- Mixing is strongest when frequencies match

---

### Resonance: When Things Actually Happen

Each energy difference defines a natural frequency:

$$
\omega_{mn} = \frac{E_m - E_n}{\hbar}
$$

If the wall oscillation frequency satisfies:

$$
\Omega \approx \omega_{mn}
$$

then:

- Energy is transferred efficiently between levels
- $c_m(t)$ grows significantly
- The electron enters a **superposition of energies**

This is generic behavior of driven quantum systems.

---

### What the Wavefunction Now Looks Like

Once multiple $c_n$'s are nonzero:

$$
\Psi(x,t) = c_1(t)\psi_1(x) + c_2(t)\psi_2(x)
$$

Then:

$$
|\Psi(x,t)|^2 \text{ changes in time}
$$

This means:

- The electron no longer has a stationary probability cloud
- The electron is now a **dynamic wave packet**
- Energy is genuinely uncertain

This is the moment classical intuition starts to sneak back in.

---

### Why This Maps Directly to Phonons

Here is the **exact conceptual mapping**:

| Moving Box | Real Crystal |
|------------|--------------|
| Wall motion | Ion motion |
| Oscillation frequency $\Omega$ | Phonon frequency $\omega_{\mathbf{q}}$ |
| Energy pumped externally | Energy exchanged internally |
| No momentum exchange | Phonon carries momentum $\mathbf{q}$ |

In a crystal:

- The potential minimum itself moves
- It moves *periodically* in both space and time
- That drives electrons into **energy and momentum superpositions**

---

## Part 5: Electron-Phonon Coupling

### What the Electron Actually Sees

When ions move, the electron experiences:

$$
V(\mathbf{r}, t) = V_0(\mathbf{r}) + \delta V(\mathbf{r}, t)
$$

where $V_0$ is the periodic lattice potential and $\delta V$ is the time-dependent perturbation from lattice motion.

---

### The One Equation You Can Carry Around

A phonon creates a traveling deformation in the lattice. You can model this as:

$$
\delta V(x,t) \approx A\cos(qx - \omega t)
$$

This says:

- The lattice creates a **traveling wave** of potential
- That wave has:
  - Wavelength $\lambda = 2\pi/q$ (momentum content)
  - Frequency $\omega$ (energy content)

**The key physical picture:**

> A phonon is a **moving grating** for electrons — like a traveling Bragg reflector or a moving diffraction grating. It transfers energy and crystal momentum to the electron wave.

This connects directly to the "moving walls" toy model, but adds the missing ingredient: the drive is not global — it's a **traveling deformation field**.

**The electron responds by picking up:**

- Momentum $\pm \hbar q$
- Energy $\pm \hbar\omega$

That's the essential physics. No more formalism needed for intuition.

---

### Conservation Laws in Crystals

!!! note "Three Different Momenta — Don't Confuse Them"
    In solid state physics, three different momenta appear:

    • **Mechanical momentum** $\mathbf{p} = m\mathbf{v}$ — the "mv" from classical mechanics
    • **Crystal momentum** $\hbar\mathbf{k}$ — a quantum number labeling Bloch states (not always equal to mechanical momentum!)
    • **Phonon momentum** $\hbar\mathbf{q}$ — labels the lattice wave that carries momentum

    Only **crystal momentum** is conserved (mod $\mathbf{G}$) in electron-phonon processes. This allows phenomena like **Umklapp scattering** where mechanical momentum appears to violate conservation — but crystal momentum accounting (with reciprocal lattice vectors) remains exact.

In a crystal, electron-phonon coupling enforces:

$$
\mathbf{k}' = \mathbf{k} \pm \mathbf{q} \quad (\text{mod } \mathbf{G})
$$

$$
E_{n'}(\mathbf{k}') = E_n(\mathbf{k}) \pm \hbar\omega_{\mathbf{q}}
$$

where $\mathbf{G}$ is a reciprocal lattice vector (the "mod $\mathbf{G}$" allows Umklapp processes).

**Why phonons matter for momentum:** In many crystal processes, phonons are the main way to satisfy crystal-momentum constraints. Photons supply plenty of energy but almost no momentum; phonons are the lattice's "momentum channel."

This looks like scattering, but fundamentally:

> **The electron wavefunction gains and loses Fourier components.**

---

### Static vs Dynamic Symmetry Breaking

Not all symmetry breaking is the same. Understanding the difference explains why temperature matters:

**Impurities break symmetry once:**

- A substitutional atom or vacancy creates a *static* perturbation
- The potential is different at that site, but it doesn't change in time
- Electrons scatter off impurities, but the scattering rate doesn't depend on temperature (in this simple picture)
- The perturbation is "always there" — a permanent bump in the road

**Phonons break symmetry continuously:**

- Lattice vibrations create a *dynamic* perturbation that evolves in time
- The potential landscape is constantly shifting
- More phonons (higher $T$) means more frequent and larger perturbations
- The electron's environment never settles down

This distinction matters for transport:

- **Impurity scattering** dominates at low temperatures (residual resistivity)
- **Phonon scattering** dominates at high temperatures (resistivity $\propto T$)

---

### Why Electron-Phonon Scattering Increases with Temperature

As temperature rises, more phonon modes are populated and their amplitudes increase. This makes the lattice potential increasingly time-dependent and spatially distorted. Electrons are therefore driven into superpositions of nearby Bloch states more frequently, shortening quasiparticle lifetimes and increasing momentum relaxation.

In wavefunction language, scattering increases because the electron's state is being reshaped more often, not because particles collide more violently.

---

## Part 6: From Bloch Waves to Wave Packets

### The Central Conclusion

Once translational symmetry is broken (by phonons, defects, or surfaces), electrons are no longer pure Bloch waves — they become **finite wave packets**, superpositions of nearby Bloch components.

**Important nuance:** Phonons don't *force* every electron into a localized packet. What they do is give Bloch-like excitations a **finite lifetime** — a finite linewidth in both energy and $\mathbf{k}$. Wave packets are the useful representation when you want something localized and moving.

**Critical distinction:**

• **Bloch waves do not move** — they are stationary eigenstates with probability density frozen in time
• **Wave packets DO move** — motion comes from **group velocity** $\mathbf{v}_g = \nabla_{\mathbf{k}} E(\mathbf{k}) / \hbar$, not from any single $\mathbf{k}$ value

This is the bridge to transport, effective mass, and classical motion.

---

### What "Scattering" Really Is

From the wavefunction point of view, the electron does **not** bounce like a billiard ball. Its wavefunction gains and loses momentum components — a perfectly sharp $k$ becomes a distribution of nearby $k$'s. This momentum spread implies spatial localization.

> **Wave packets are born from broken symmetry.**

A real electron state becomes:

$$
\Psi(\mathbf{r}) = \int a(\mathbf{k}) \, \psi_{n\mathbf{k}}(\mathbf{r}) \, d\mathbf{k}
$$

where $a(\mathbf{k})$ has finite width $\Delta k$, giving localization length $\sim 1/\Delta k$.

**The key hierarchy:**

- **Bloch waves:** Exact eigenstates of an idealized, symmetric Hamiltonian
- **Real electrons:** Finite wave packets built from Bloch components

Bloch waves are not "wrong" — they are the **basis states**. Real electrons are superpositions of them.

---

### The "Alphabet vs Words" Analogy

Think of Bloch states as letters in an alphabet:

- Individual letters (Bloch states) are building blocks
- Real electrons are words — specific combinations
- Phonons constantly "edit" the words by swapping letters in and out

The alphabet remains fixed; only the combinations change.

---

## Part 7: Pauli Exclusion and Deep Electrons

Even electrons deep below the Fermi level are not frozen point particles. When symmetry is imperfect, they too are described by wave packets (superpositions of Bloch components). But Pauli blocking strongly suppresses real transitions in equilibrium — there are no nearby empty states to scatter into.

**Why don't they matter for transport?**

Deep electrons form wave packets, but those wave packets don't change occupancy under weak perturbations. Only electrons near the Fermi surface have available states to scatter into — that's why they dominate conduction.

---

## Part 8: What Does T = 0 Really Mean?

At $T = 0$, there are no thermally excited phonons — but zero-point motion still exists. The ions fluctuate quantum mechanically even in the ground state.

**The key refinement:** The *expectation value* of the lattice potential remains periodic, even though instantaneous ion positions fluctuate. This is why band structure remains so accurate at $T = 0$ — the average potential is periodic, even if snapshots are not.

**The quasiparticle picture:** In a real crystal, exact Bloch eigenstates do not exist. What survives are long-lived quasiparticle states that are approximately Bloch-like. At the Fermi surface, lifetimes grow as $T \to 0$ but are never truly infinite.

**What this means practically:**

- Occupation of Bloch-like states remains well-defined
- Fermi sea structure persists
- $E(\mathbf{k})$ relations remain meaningful
- Band theory works despite being an idealization

---

## Part 9: What Is Exact, Approximate, and Misunderstood

### Exact (Under Stated Assumptions)

- **Bloch's theorem:** Given perfect periodicity, eigenstates have the Bloch form
- **Phonons as quantized normal modes:** Direct consequence of linearized lattice dynamics
- **Time-dependent perturbation physics:** The framework for how oscillating potentials mix energy levels

### Approximate

- **Single-electron picture:** Real metals have electron-electron interactions
- **Weak electron-phonon coupling:** Perturbation theory assumes small $\delta V$
- **Long-lived quasiparticles:** Fermi liquid theory, not exact for all systems

### Common Misconceptions

| Misconception | Reality |
|---------------|---------|
| "Electrons bounce off ions like billiard balls" | Wavefunctions reshape; there's no impact point |
| "Only electrons near Fermi level are quantum" | All electrons are quantum waves; deep ones just don't change occupancy |
| "Phonons are fake mathematical particles" | Phonons are as real as photons — quantized collective excitations |
| "Bloch waves are just approximations" | They're exact under symmetry; the approximation is assuming that symmetry holds |
| "At T=0, electrons are perfect Bloch waves forever" | Zero-point motion still breaks exact periodicity |

---

## Part 10: The Mental Model to Keep

Carry this hierarchy with you:

1. **In a perfect crystal,** electrons are stationary Bloch waves extending across the entire lattice

2. **Real crystals break symmetry** through:
   - Lattice motion (phonons) — always present
   - Defects and impurities
   - Surfaces and finite size

3. **Phonons are organized, quantized lattice motion** — collective oscillations, not random jiggling

4. **Phonons force electrons into superpositions** of energies and momenta through time-dependent potentials

5. **Momentum and energy are conserved** — when an electron gains $+\mathbf{q}$, a phonon loses $-\mathbf{q}$ (absorption), or vice versa (emission). Electrons can create and destroy phonons; the interaction is bidirectional, not electrons being pushed around by a fixed background

6. **These superpositions form wave packets** — spatially localized, with uncertain momentum

7. **"Scattering" is wavefunction reshaping,** not collisions — momentum components are added and removed

8. **Classical behavior emerges** only after phase coherence is lost over many scattering events

---

## The Bottom Line

**Q: Are electrons in metals Bloch waves or localized particles?**

**A: Bloch waves are the alphabet. Real electrons are words.**

Bloch states $\psi_{n\mathbf{k}}$ are exact solutions *only* for a perfect, frozen, infinite crystal — a mathematical idealization. They form a complete basis set. Real electrons are *superpositions* of Bloch states:

$$\Psi(\mathbf{r}) = \int a(\mathbf{k}) \, \psi_{n\mathbf{k}}(\mathbf{r}) \, d\mathbf{k}$$

**What breaks the symmetry:** Phonons, defects, surfaces — anything that makes $V(\mathbf{r})$ non-periodic. Phonons are always present (even zero-point motion at $T=0$).

**What "scattering" actually is:** Not collisions. The electron wavefunction gains and loses $\mathbf{k}$ components. A sharp momentum state spreads into a distribution — that spread *is* localization.

**Why classical intuition eventually works:** After many scattering events, phase coherence is lost. The wave packet's center moves like a classical particle with effective mass $m^* = \hbar^2/(d^2E/dk^2)$.

**The one sentence version:**

> Bloch waves are the basis; real electrons are finite wave packets built from that basis; phonons continuously reshuffle which basis states are superposed.

