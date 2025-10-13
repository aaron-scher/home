# Math Examples

This page demonstrates LaTeX equation support with automatic equation numbering.

## Inline Equations

You can write inline math like this: \(E = mc^2\) or \(a^2 + b^2 = c^2\).

## Display Equations

### Simple Display Equation

Here's a basic equation:

\[
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
\]

### Numbered Equations

Equations are automatically numbered when using `\begin{equation}`:

\begin{equation}
\frac{d}{dx} \left( \int_{0}^{x} f(u)\,du\right) = f(x)
\end{equation}

This is the fundamental theorem of calculus.

\begin{equation}
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
\end{equation}

That's Faraday's law of induction.

### Matrix Equations

\begin{equation}
\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
\end{equation}

### Multi-line Equations

Use `align` for aligned equations:

\begin{align}
f(x) &= (x+a)(x+b) \\
     &= x^2 + (a+b)x + ab
\end{align}

### Equation without Numbering

If you don't want numbering, use `equation*` or just `\[...\]`:

\begin{equation*}
\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
\end{equation*}

## Common Formulas

### Quadratic Formula

\begin{equation}
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{equation}

### Taylor Series

\begin{equation}
f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots
\end{equation}

### Fourier Transform

\begin{equation}
\hat{f}(\xi) = \int_{-\infty}^{\infty} f(x) e^{-2\pi i x \xi} dx
\end{equation}

## Greek Letters and Symbols

- Alpha: \(\alpha\), Beta: \(\beta\), Gamma: \(\gamma\), Delta: \(\delta\)
- Summation: \(\sum\), Product: \(\prod\), Integral: \(\int\)
- Partial: \(\partial\), Nabla: \(\nabla\), Infinity: \(\infty\)

## Testing Notes

This page serves as a reference for:
- Inline math rendering
- Display equation rendering
- Automatic equation numbering with `\begin{equation}`
- Multi-line equations with `align`
- Matrix support
- Greek letters and mathematical symbols
