# Mental Model of Metals and Semiconductors

## Energy Bands: From Isolated Atoms to Solids

When atoms are brought together to form a solid, their discrete electron energy levels transform into continuous energy bands.

**Two ways to understand band formation:**

• **Bottom-up (orbital splitting):** Start with isolated atomic orbitals. As atoms approach for covalent bonding, orbitals overlap and split into N states for N atoms. These merge into continuous bands.

• **Top-down (Bloch theory):** Solve the Schrödinger equation for electrons in a periodic crystal potential. The solutions are Bloch waves, and allowed energies naturally form bands separated by gaps.

### Energy Level Spreading

As atoms approach each other, their electron orbitals begin to overlap. This causes each discrete atomic energy level to split into multiple closely-spaced states.

![Energy states spreading as atoms approach](../images/energyband1_spread.png)

*Figure 1 [1]: As atoms are brought closer together, individual allowed energy states start to spread in energy. The 1s and 2s electron states each split into 12 states (for 12 atoms), forming the beginning of energy bands.*

### Band Formation at Equilibrium Spacing

At the equilibrium interatomic spacing in a solid, these closely-spaced states merge into continuous energy bands, separated by band gaps where no electron states exist.

![Energy bands and band gaps](../images/energyband2_spread.png)

*Figure 2 [1]: At equilibrium interatomic spacing in a solid, the spread states form continuous energy bands. Band gaps appear between bands - energy ranges where no electron states are allowed.*

### Bands in Real Space

In the bulk of a crystal, electrons occupy states within bands. The energy varies with position, creating potential wells at atomic sites.

![Conduction and valence bands in a crystal](../images/energyband3_bands.png)

*Figure 3 [2]: Conduction and valence bands in a crystal showing spatial variation. The periodic potential creates wells at atomic sites. Note how the energy levels vary between rows of atoms and along rows.*

## Bloch Theorem: Electrons in Periodic Crystals

To understand electron behavior quantitatively, we solve the **Schrödinger equation for a periodic potential** extending throughout an infinite crystal.

**Bloch's theorem** states that electron wavefunctions in a periodic crystal have the form:

$$\psi(x) = U_K(x) e^{iKx}$$

where:

- $U_K(x)$ has the same periodicity as the crystal lattice
- $e^{iKx}$ is a plane wave with wavevector K
- The wavefunction is a **plane wave modulated by the crystal periodicity**

This is the **stationary state** (time-independent part). A stationary state has a **single definite energy** E. The complete time-dependent wavefunction is:

$$\Psi(x,t) = U_K(x) e^{iKx} e^{-iEt/\hbar}$$

The probability density $|\Psi|^2$ doesn't change with time - hence "stationary."

**Key properties:**

1. **Symmetry:** $E(K) = E(-K)$ - energy is the same for ±K (forward and backward traveling waves)

2. **Periodicity:** $E(K) = E(K + \frac{2\pi n}{a})$ - adding $2\pi/a$ to K gives the same energy (physically equivalent states)

**For 3D crystals:**

$$\psi(\vec{r}) = U_{\vec{K}}(\vec{r}) e^{i\vec{K}\cdot\vec{r}}$$

where $|\vec{K}| = 2\pi/\lambda$ connects the wavevector magnitude to the de Broglie wavelength.

### Brillouin Zones and the Reduced Zone Scheme

The **first Brillouin zone** spans $K \in [-\pi/a, \pi/a]$ and contains all distinct k-values - a complete set of unique solutions. K-values outside this range simply duplicate solutions inside.

### Solving for the Dispersion Relation: E-k Diagrams

When you solve the Schrödinger equation for a periodic potential using the Bloch wavefunction form, you obtain the **dispersion relation E(K)** - how energy depends on wavevector K.

The result is the **E-k diagram**, which reveals the full band structure:

![E-k band diagram](../images/band theory with k.png)

*Figure 4 [3]: Reduced-zone representation of allowed E-k states in a one-dimensional crystal. Solving Schrödinger's equation with Bloch wavefunctions gives these dispersion curves - four energy bands separated by band gaps. Each band contains a continuum of allowed k-states between -π/(a+b) and π/(a+b).*

**Connecting k, momentum, and energy:**

| Property | Free Electron | Electron in Crystal (Bloch) |
|----------|---------------|----------------------------|
| **Wavefunction** | $\psi = Ae^{i(kx-\omega t)}$ | $\psi = U_K(x)e^{i(Kx-\omega t)}$ |
| **Spatial part** | Plane wave $e^{ikx}$ | Bloch wave $U_K(x)e^{iKx}$ |
| **Wavenumber** | $k = \frac{2\pi}{\lambda}$ | $K = \frac{2\pi}{\lambda}$ (crystal momentum) |
| **Frequency** | $\omega = \frac{E}{\hbar}$ | $\omega = \frac{E}{\hbar}$ |
| **Momentum** | $p = \hbar k$ | $\hbar K$ (crystal momentum, not actual) |
| **Energy** | $E = \frac{\hbar^2 k^2}{2m}$ | $E = E_0 + \frac{\hbar^2 K^2}{2m_0}$ (near band minimum, where $E_0$ is band edge at K=0) |
| **Velocity** | $v = \frac{\hbar k}{m}$ | $v = \frac{1}{\hbar}\frac{dE}{dK}$ (group velocity) |

**Why does energy increase with momentum for free electrons?**

For a free particle: $E = \frac{p^2}{2m} = \frac{\hbar^2 k^2}{2m}$

- Since $p = \hbar k$, momentum is directly proportional to k
- As energy increases: E ↑ → ω ↑ → p ↑ → k ↑ → λ ↓ (shorter wavelength, since λ = 2π/k)
- E ∝ k² is a parabola: higher k **always** means higher energy (monotonic)
- Higher energy → higher k → shorter wavelength → more localized

**Mass dependence:** For the same energy E, solving $k = \sqrt{2mE/\hbar^2}$ shows lighter particles (electrons) have smaller k → larger wavelength λ = 2π/k. A light particle doesn't need much momentum to achieve a given kinetic energy, so it has a longer wavelength. Longer wavelengths are harder to confine spatially (try fitting a long wave into a small box!), making light particles naturally more delocalized than heavy ones at the same energy.

**Does this happen in crystals?**

**Not always!** Near band edges, the E-k curve **bends backward** - higher |K| can mean **lower** E. At zone boundaries (K = ±π/a), electrons form standing waves (Bragg reflection) rather than propagating, with dE/dK = 0. This non-monotonic behavior is unique to crystals and creates band gaps.

### Group Velocity: How Fast Do Electrons Move?

The electron velocity is given by the **group velocity**:

$$v = v_g = \frac{1}{\hbar}\frac{dE}{dK}$$

This is the slope of the E-K curve!

- **Flat bands** (small dE/dK) → slow electrons
- **Steep bands** (large dE/dK) → fast electrons
- At band edges, dE/dK = 0 → electrons have zero velocity (standing waves at Brillouin zone boundaries)

---

## References

[1] "Energy bands and band gaps," Pennsylvania State University, Materials Science and Engineering. [Online]. Available: https://courses.ems.psu.edu/matse81/node/2227

[2] B. L. Anderson and R. Anderson, *Fundamentals of Semiconductor Devices*, 2nd ed. McGraw-Hill Education.

[3] R. F. Pierret, *Advanced Semiconductor Fundamentals*, 2nd ed., vol. VI, Modular Series on Solid State Devices. Upper Saddle River, NJ: Prentice Hall, 2003.
