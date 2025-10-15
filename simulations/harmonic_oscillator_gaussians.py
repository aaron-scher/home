import numpy as np
import matplotlib.pyplot as plt

# Domain in x
x = np.linspace(-4, 4, 1000)

# Potential: harmonic oscillator V(x) = ½ x^2
V = 0.5 * x**2

# Three Gaussians: widths (sigma)
sigmas = [0.5, 1.0, 2.0]  # "too narrow", "just right", "too wide"
colors = ['#E74C3C', '#2ECC71', '#3498DB']  # red, green, blue - more distinct
labels = ['Narrow (σ=0.5)', 'Just Right (σ=1.0)', 'Wide (σ=2.0)']

# Wavefunctions (not normalized exactly, just for shape)
psis = [np.exp(-x**2 / (2 * sigma**2)) for sigma in sigmas]

# Normalize for visual consistency
psis = [psi / np.sqrt(np.trapezoid(psi**2, x)) for psi in psis]

# ============================================================================
# PLOT 1: Wavefunctions showing curvature differences
# ============================================================================
fig1, ax1 = plt.subplots(figsize=(11, 7))

# Plot potential
ax1.plot(x, V, 'k--', linewidth=3, label='V(x) = ½x²', alpha=0.5, zorder=1)

# Plot wavefunctions (larger scale, no fill)
scale = 1.8  # increased scale so they're not squished
for i, (psi, c, lab) in enumerate(zip(psis, colors, labels)):
    y = scale * psi
    ax1.plot(x, y, color=c, label=lab, linewidth=3.5, zorder=3)

# Add curvature annotations at the peaks (x=0) where curvature is highest
# Narrow Gaussian - highest curvature at peak
narrow_peak_y = scale * psis[0][500]  # psis are already normalized
ax1.annotate('Sharp peak\nHigh curvature\n→ High KE',
             xy=(0, narrow_peak_y),
             xytext=(-1.8, 1.45),
             fontsize=11,
             color=colors[0],
             weight='bold',
             arrowprops=dict(arrowstyle='->', color=colors[0], lw=2.5),
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=colors[0], alpha=0.95, linewidth=2))

# Medium Gaussian - medium curvature at peak
medium_peak_y = scale * psis[1][500]
ax1.annotate('Medium curvature\n→ Medium KE\n(Just right!)',
             xy=(0, medium_peak_y),
             xytext=(1.4, 1.05),
             fontsize=11,
             color=colors[1],
             weight='bold',
             arrowprops=dict(arrowstyle='->', color=colors[1], lw=2.5),
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=colors[1], alpha=0.95, linewidth=2))

# Wide Gaussian - lowest curvature at peak
wide_peak_y = scale * psis[2][500]
ax1.annotate('Flat peak\nLow curvature\n→ Low KE',
             xy=(0, wide_peak_y),
             xytext=(1.5, 0.32),
             fontsize=11,
             color=colors[2],
             weight='bold',
             arrowprops=dict(arrowstyle='->', color=colors[2], lw=2.5),
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=colors[2], alpha=0.95, linewidth=2))

# Add label at bottom of potential well
ax1.text(0, 0.002, 'Bottom of well', fontsize=14, ha='center', va='top',
         color='gray', style='italic', weight='bold')

# Add ψ labels on left side of each curve
# Red narrow curve - at x=-1.8, evaluate psi at that x position
x_label = -1.8
x_idx = np.argmin(np.abs(x - x_label))
ax1.text(x_label - 0.15, scale * psis[0][x_idx] + 0.05, r'$\psi_1$',
         fontsize=16, color=colors[0], weight='bold', ha='right', va='center')

# Green medium curve
ax1.text(x_label - 0.15, scale * psis[1][x_idx], r'$\psi_2$',
         fontsize=16, color=colors[1], weight='bold', ha='right', va='center')

# Blue wide curve
ax1.text(x_label - 0.15, scale * psis[2][x_idx] + 0.03, r'$\psi_3$',
         fontsize=16, color=colors[2], weight='bold', ha='right', va='center')

ax1.set_xlabel('Position x', fontsize=15, weight='bold')
ax1.set_ylabel('Wavefunction ψ(x)', fontsize=15, weight='bold')
ax1.set_title('Testing Different Gaussian Widths in a Harmonic Oscillator', fontsize=17, weight='bold', pad=15)
ax1.set_xlim(-3, 3)
ax1.set_ylim(-0.1, 2.0)
ax1.legend(fontsize=13, loc='upper right', framealpha=0.95, edgecolor='black', fancybox=True)
ax1.grid(True, alpha=0.25, linestyle='--')
ax1.tick_params(labelsize=12)
plt.tight_layout()

# Save figure 1
plt.savefig('../docs/images/harmonic_oscillator_gaussians_1.png', dpi=300, bbox_inches='tight')

# ============================================================================
# PLOT 2: Local energy E(x) = KE(x) + V(x)
# ============================================================================
def local_energy(psi, x):
    """Compute local energy E(x) = KE(x) + V(x)"""
    # second derivative
    d2 = np.gradient(np.gradient(psi, x), x)
    KE_local = -0.5 * d2 / psi
    return KE_local + V

fig2, ax2 = plt.subplots(figsize=(11, 7))

# Plot local energies
E_locs = []
for i, (psi, c, lab) in enumerate(zip(psis, colors, labels)):
    E_loc = local_energy(psi, x)
    E_locs.append(E_loc)
    ax2.plot(x, E_loc, color=c, label=lab, linewidth=3.5, zorder=3)

# Add ideal energy reference line (ground state E0 = 0.5 for HO)
E_ideal = 0.5
ax2.axhline(E_ideal, color='black', linestyle='--', linewidth=2.5,
            alpha=0.7, zorder=2)

# Add annotations for each Gaussian
# Narrow - too high in center
ax2.annotate('Too much KE\n→ E(x) bulges\nat center',
             xy=(0, E_locs[0][500]),
             xytext=(-1.5, 1.8),
             fontsize=11,
             color=colors[0],
             weight='bold',
             arrowprops=dict(arrowstyle='->', color=colors[0], lw=2.5),
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=colors[0], alpha=0.9))

# Medium - flattest (best)
ax2.annotate('Flat E(x)\n→ Stationary state',
             xy=(0, E_locs[1][500]),
             xytext=(1.2, 0.7),
             fontsize=11,
             color=colors[1],
             weight='bold',
             arrowprops=dict(arrowstyle='->', color=colors[1], lw=2.5),
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=colors[1], alpha=0.9))

# Wide - too low in center
ax2.annotate('Not enough KE\nto balance V(x)',
             xy=(0, E_locs[2][500]),
             xytext=(-1.5, 0.15),
             fontsize=11,
             color=colors[2],
             weight='bold',
             arrowprops=dict(arrowstyle='->', color=colors[2], lw=2.5),
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=colors[2], alpha=0.9))

# Add E labels next to each curve where they're clearly separated
# Red narrow E(x) - label to the left of red curve
ax2.text(-0.32, 1.8, r'$E_1$',
         fontsize=16, color=colors[0], weight='bold', ha='center', va='center')

# Green medium E(x) - label on the flat section
ax2.text(-2.0, 0.58, r'$E_2$',
         fontsize=16, color=colors[1], weight='bold', ha='center', va='center')

# Blue wide E(x) - label to the left of blue curve, higher up
ax2.text(-1.3, 0.7, r'$E_3$',
         fontsize=16, color=colors[2], weight='bold', ha='center', va='center')

ax2.set_xlabel('Position x', fontsize=15, weight='bold')
ax2.set_ylabel('Local Total Energy E(x)', fontsize=15, weight='bold')
ax2.set_title('Only the "Just Right" Width Keeps Total Energy Flat', fontsize=17, weight='bold', pad=15)
ax2.set_xlim(-3, 3)
ax2.set_ylim(0, 2.5)
ax2.legend(fontsize=12, loc='upper right', framealpha=0.95, edgecolor='black', fancybox=True)
ax2.grid(True, alpha=0.25, linestyle='--')
ax2.tick_params(labelsize=12)
plt.tight_layout()

# Save figure 2
plt.savefig('../docs/images/harmonic_oscillator_gaussians_2.png', dpi=300, bbox_inches='tight')

print("Saved plots to home/docs/images/")
print("  - harmonic_oscillator_gaussians_1.png")
print("  - harmonic_oscillator_gaussians_2.png")

# Uncomment to show plots interactively:
# plt.show()
