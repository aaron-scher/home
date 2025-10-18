#!/usr/bin/env python3
"""
Generate visualization showing discrete to continuous transition for quantum basis vectors.
Shows how one-hot vectors become delta functions in the continuous limit.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches

# Set up the figure with 4 panels
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('From Discrete to Continuous: Basis Vectors and States',
             fontsize=16, fontweight='bold', y=0.995)

# Color scheme
basis_color = '#2E86AB'  # Blue for basis vectors
state_color = '#A23B72'  # Purple/magenta for states
grid_color = '#CCCCCC'

def plot_discrete_basis(ax, N, highlight_idx, title):
    """Plot a discrete basis vector |x_i⟩ as a bar chart"""
    positions = np.arange(N)
    values = np.zeros(N)
    values[highlight_idx] = 1.0

    bars = ax.bar(positions, values, width=0.7, color=basis_color,
                   edgecolor='black', linewidth=1.5, alpha=0.8)

    ax.set_xlim(-0.5, N-0.5)
    ax.set_ylim(0, 1.3)
    ax.set_xlabel('Position index', fontsize=11)
    ax.set_ylabel('Amplitude', fontsize=11)
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    ax.grid(True, alpha=0.3, color=grid_color)
    ax.set_xticks(positions)

    # Add label for the highlighted basis vector
    if N <= 10:
        ax.text(highlight_idx, 1.15, f'|x_{highlight_idx}⟩',
                ha='center', fontsize=11, fontweight='bold', color=basis_color)

    return ax

def plot_continuous_basis(ax, title):
    """Plot continuous limit showing delta function spike"""
    x = np.linspace(-2, 2, 1000)
    spike_pos = 0.5

    # Create a very narrow Gaussian to represent delta function
    width = 0.03
    delta_approx = (1.0/(width * np.sqrt(2*np.pi))) * np.exp(-0.5*((x - spike_pos)/width)**2)
    # Normalize for visualization
    delta_approx = delta_approx / np.max(delta_approx) * 5

    ax.fill_between(x, 0, delta_approx, color=basis_color, alpha=0.7, linewidth=0)
    ax.plot(x, delta_approx, color=basis_color, linewidth=2)

    # Add arrow pointing to spike
    ax.annotate(f'|x={spike_pos}⟩', xy=(spike_pos, 2.5), xytext=(spike_pos + 0.6, 3.5),
                fontsize=11, fontweight='bold', color=basis_color,
                arrowprops=dict(arrowstyle='->', lw=2, color=basis_color))

    ax.set_xlim(-2, 2)
    ax.set_ylim(0, 6)
    ax.set_xlabel('Position x', fontsize=11)
    ax.set_ylabel('δ(x\' - x)', fontsize=11)
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    ax.grid(True, alpha=0.3, color=grid_color)
    ax.text(0.5, 0.95, '"1 at x" → δ-spike', transform=ax.transAxes,
            fontsize=10, ha='center', va='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    return ax

def plot_discrete_state(ax, N, title):
    """Plot a discrete state |ψ⟩ as coefficients"""
    positions = np.arange(N)

    # Create a simple wavepacket-like state
    center = N // 2
    values = np.exp(-0.5 * ((positions - center) / (N/8))**2)
    values = values / np.sqrt(np.sum(values**2))  # Normalize

    bars = ax.bar(positions, values, width=0.7, color=state_color,
                   edgecolor='black', linewidth=1.5, alpha=0.8)

    ax.set_xlim(-0.5, N-0.5)
    ax.set_ylim(0, np.max(values)*1.2)
    ax.set_xlabel('Position index', fontsize=11)
    ax.set_ylabel('Amplitude ψ(xᵢ)', fontsize=11)
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    ax.grid(True, alpha=0.3, color=grid_color)
    ax.set_xticks(positions[::max(1, N//10)])

    # Add note about normalization
    ax.text(0.5, 0.95, f'Σ|ψ(xᵢ)|² = 1', transform=ax.transAxes,
            fontsize=10, ha='center', va='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    return ax

def plot_continuous_state(ax, title):
    """Plot continuous state ψ(x) as smooth function"""
    x = np.linspace(-2, 2, 1000)

    # Gaussian wavepacket
    center = 0.3
    width = 0.4
    psi = np.exp(-0.5 * ((x - center) / width)**2)
    # Normalize
    dx = x[1] - x[0]
    norm = np.sqrt(np.sum(psi**2 * dx))
    psi = psi / norm

    ax.fill_between(x, 0, psi, color=state_color, alpha=0.5, linewidth=0)
    ax.plot(x, psi, color=state_color, linewidth=2.5)

    ax.set_xlim(-2, 2)
    ax.set_ylim(0, np.max(psi)*1.2)
    ax.set_xlabel('Position x', fontsize=11)
    ax.set_ylabel('Amplitude ψ(x)', fontsize=11)
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    ax.grid(True, alpha=0.3, color=grid_color)

    # Add note about normalization
    ax.text(0.5, 0.95, '∫|ψ(x)|² dx = 1', transform=ax.transAxes,
            fontsize=10, ha='center', va='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    return ax

# Panel 1: Coarse discrete basis (N=5)
plot_discrete_basis(axes[0, 0], N=5, highlight_idx=2,
                    title='Coarse Lattice: Basis Vector |x₂⟩')

# Panel 2: Fine discrete basis (N=20)
plot_discrete_basis(axes[0, 1], N=20, highlight_idx=12,
                    title='Fine Lattice: Δx smaller')

# Panel 3: Continuous basis (delta function)
plot_continuous_basis(axes[1, 0],
                      title='Continuous Limit: Delta Function')

# Panel 4: Show state evolution (coarse to smooth)
# Let's show N=20 discrete state
plot_discrete_state(axes[1, 1], N=20,
                   title='Discrete State → Smooth Function')

# Add some overall styling
plt.tight_layout(rect=[0, 0, 1, 0.99])

# Add text boxes with key insights
fig.text(0.5, 0.01,
         'Key Insight: As spacing Δx → 0, discrete "one-hot" vectors → continuous delta functions δ(x\'-x)',
         ha='center', fontsize=11, style='italic',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))

# Save the figure
output_path = '/Users/aaronscher/Desktop/1_Projects/aaron-scher github website/home/docs/quantum-mechanics/discrete_to_continuous.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f'Visualization saved to: {output_path}')

# Also save as SVG for better quality in docs
output_path_svg = '/Users/aaronscher/Desktop/1_Projects/aaron-scher github website/home/docs/quantum-mechanics/discrete_to_continuous.svg'
plt.savefig(output_path_svg, format='svg', bbox_inches='tight', facecolor='white')
print(f'SVG version saved to: {output_path_svg}')

print('Done!')
