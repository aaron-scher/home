# Quantum Operators and Measurement

## The Momentum Operator and Plane Waves

Let's start where we left off in [Foundations](quantum-foundations.md): plane waves. A plane wave with definite momentum $p = \hbar k$ looks like:

$$
\psi(x) = A e^{ikx}
$$

We derived this from de Broglie's relation. Now let's ask: **what happens when we take the derivative?**

$$
\frac{d\psi}{dx} = ik\psi = \frac{i}{\hbar}p\psi
$$

Multiply both sides by $-i\hbar$:

$$
-i\hbar\frac{d\psi}{dx} = p\psi
$$

**This is huge!** Taking the derivative "extracts" the momentum from the wavefunction. We call this operation the **momentum operator**:

$$
\hat{p} = -i\hbar\frac{d}{dx}
$$

In abstract notation (operator acting on a state):

$$
\hat{p}|\psi\rangle = p|\psi\rangle
$$

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
- $p_1 = 3\hbar$ nm⁻¹ with probability $|\frac{1}{\sqrt{2}}|^2 = 50\%$
- $p_2 = 7\hbar$ nm⁻¹ with probability $|\frac{1}{\sqrt{2}}|^2 = 50\%$

The particle does **not** have a definite momentum! This is why quantum measurements are probabilistic.

### Another Superposition: Unequal Amplitudes

Let's make it more interesting with unequal amplitudes:

$$
\psi(x) = \frac{1}{2}e^{ik_1 x} + \frac{\sqrt{3}}{2}e^{ik_2 x}
$$

Now the probabilities are:
- $p_1 = k_1\hbar$ with probability $|\frac{1}{2}|^2 = 25\%$
- $p_2 = k_2\hbar$ with probability $|\frac{\sqrt{3}}{2}|^2 = 75\%$

The **key insight:** When $\psi$ is a superposition, applying $\hat{p}$ gives different eigenvalues multiplied by their respective components. The measurement outcome is probabilistic, with probabilities given by $|c_n|^2$ where $c_n$ is the coefficient of each momentum eigenstate.

---

## Expected Value: The Average Measurement

What if we repeat the momentum measurement many times on identically prepared systems? We get an **average** or **expected value**.

For the unequal superposition above:

$$
\langle p \rangle = 25\% \cdot p_1 + 75\% \cdot p_2 = \frac{1}{4}(k_1\hbar) + \frac{3}{4}(k_2\hbar)
$$

There's a beautiful mathematical formula for this. In position space:

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

Here's something beautiful. In position space:

$$
\hat{p} = -i\hbar\frac{d}{dx}
$$

In momentum space, it's much simpler:

$$
\hat{p}\tilde{\psi}(p) = p\tilde{\psi}(p)
$$

Just **multiply by $p$!** No derivatives needed.

**Why?** Because we're already in the momentum basis. Momentum eigenstates are just the basis states $|p\rangle$ themselves, so applying $\hat{p}$ just gives you the eigenvalue $p$.

It's exactly like position space where $\hat{x}\psi(x) = x\psi(x)$ (the position operator just multiplies by $x$).

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

This framework applies to **all quantum operators**: position, energy, angular momentum, etc. The mathematics is always the same - only the specific operator and basis change!
