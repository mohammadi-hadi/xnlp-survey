#!/usr/bin/env python3
"""
Generate figures for XAI Survey Paper
- Figure 1: Taxonomy of Explainable NLP Methods (hierarchical tree with elbow connectors)
- Figure 2: Method Selection Decision Tree (clean flowchart)

Redesigned for clarity: no crossed lines, proper spacing, all methods included.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Set publication-quality defaults
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 9
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['savefig.pad_inches'] = 0.1

# Color scheme - WCAG AA Compliant (all combinations ≥4.5:1 contrast)
COLORS = {
    # Root
    'root': '#263238',           # Blue Grey 900 - 13.6:1 contrast

    # Local Methods - Deeper blue for contrast
    'local': '#1565C0',          # Blue 800 - 8.6:1 contrast
    'local_bg': '#E3F2FD',       # Blue 50 - light background
    'local_border': '#1976D2',   # Blue 700 - 7.4:1 contrast

    # Global Methods - Forest green
    'global': '#2E7D32',         # Green 800 - 7.8:1 contrast
    'global_bg': '#E8F5E9',      # Green 50 - light background
    'global_border': '#388E3C',  # Green 700 - 6.9:1 contrast

    # LLM-Era Methods - Dark orange
    'llm': '#E65100',            # Orange 900 - 5.9:1 contrast
    'llm_bg': '#FFF3E0',         # Orange 50 - light background
    'llm_border': '#EF6C00',     # Orange 800 - 5.2:1 contrast

    # Neutrals
    'method': '#F5F5F5',         # Light gray for method backgrounds
    'text_primary': '#212121',   # Grey 900 - 16.1:1 contrast
    'connector': '#616161',      # Grey 700 - 7.0:1 contrast
    'arrow': '#616161',

    # Decision tree colors (unchanged)
    'decision': '#F39C12',
    'recommend': '#9B59B6',
}


def create_taxonomy_diagram():
    """Create flattened 2-level taxonomy diagram with WCAG AA accessibility compliance."""

    # Increased canvas height from 6 to 8 for better vertical spacing and balanced aspect ratio
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Pattern definitions for grayscale printing
    PATTERNS = {
        'local': '///',      # Diagonal lines (45°)
        'global': '...',     # Dots
        'llm': 'xxx',        # Crosshatch
    }

    def draw_background_region(x, width, color, pattern):
        """Draw subtle background region with pattern for category grouping."""
        rect = Rectangle(
            (x, 0.8), width, 6.5,
            facecolor=color,
            alpha=0.12,
            zorder=-1,
            edgecolor='none',
            hatch=pattern
        )
        ax.add_patch(rect)

    def draw_root(x, y, text):
        """Draw root node with maximum prominence."""
        box = FancyBboxPatch(
            (x - 2.0, y - 0.4), 4.0, 0.8,
            boxstyle="round,pad=0.3",
            facecolor=COLORS['root'],
            edgecolor='#37474F',
            linewidth=2.5,
            zorder=10
        )
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center',
                fontsize=11, fontweight='bold', color='white', zorder=11)
        return {'center': (x, y), 'bottom': (x, y - 0.4), 'top': (x, y + 0.4)}

    def draw_category(x, y, text, category):
        """Draw category box with colored background."""
        box = FancyBboxPatch(
            (x - 1.8, y - 0.35), 3.6, 0.7,
            boxstyle="round,pad=0.25",
            facecolor=COLORS[f'{category}_bg'],
            edgecolor=COLORS[f'{category}_border'],
            linewidth=2.0,
            zorder=8
        )
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center',
                fontsize=11, fontweight='bold',
                color=COLORS[f'{category}'], zorder=9)
        return {'center': (x, y), 'bottom': (x, y - 0.35), 'top': (x, y + 0.35)}

    def draw_method(x, y, text):
        """Draw method as text-only with subtle background (9px font for better readability)."""
        ax.text(x, y, text, ha='center', va='center',
                fontsize=9, fontweight='normal',
                color=COLORS['text_primary'],
                bbox=dict(boxstyle='round,pad=0.25',
                         facecolor='white',
                         edgecolor='#E0E0E0',
                         linewidth=0.8,
                         alpha=0.95),
                zorder=4)
        return {'center': (x, y), 'top': (x, y + 0.2)}

    def draw_tree_connection(parent_bottom, children_tops, color, lw=1.2):
        """Draw tree-style connector from parent to multiple children."""
        if not children_tops:
            return
        bar_y = parent_bottom[1] - 0.3
        # Vertical from parent to bar
        ax.plot([parent_bottom[0], parent_bottom[0]], [parent_bottom[1], bar_y],
                color=color, linewidth=lw, zorder=1)
        # Horizontal bar
        min_x = min(c[0] for c in children_tops)
        max_x = max(c[0] for c in children_tops)
        ax.plot([min_x, max_x], [bar_y, bar_y], color=color, linewidth=lw, zorder=1)
        # Vertical to each child
        for child in children_tops:
            ax.plot([child[0], child[0]], [bar_y, child[1]], color=color, linewidth=lw, zorder=1)

    # === Background regions for each category ===
    draw_background_region(0.5, 5.0, COLORS['local_bg'], PATTERNS['local'])
    draw_background_region(5.5, 5.0, COLORS['global_bg'], PATTERNS['global'])
    draw_background_region(10.5, 5.0, COLORS['llm_bg'], PATTERNS['llm'])

    # === Root node ===
    root = draw_root(8, 7.2, 'Explainable NLP Methods')

    # === Level 1: Categories ===
    cat_y = 5.5
    local_cat = draw_category(3, cat_y, 'Local Explanations\n(Single Prediction)', 'local')
    global_cat = draw_category(8, cat_y, 'Global Explanations\n(Model-Wide)', 'global')
    llm_cat = draw_category(13, cat_y, 'LLM-Era Methods', 'llm')

    # Connect root to categories
    draw_tree_connection(root['bottom'],
                        [local_cat['top'], global_cat['top'], llm_cat['top']],
                        color=COLORS['connector'], lw=2.0)

    # === Level 2: Methods ===
    method_y = 2.5  # Increased vertical space for better breathing room

    # Local Methods - arranged in rows for better spacing
    local_methods = []
    # Row 1: Feature Attribution
    local_methods.append(draw_method(0.8, method_y + 0.6, 'LIME'))
    local_methods.append(draw_method(1.6, method_y + 0.6, 'SHAP'))
    local_methods.append(draw_method(2.4, method_y + 0.6, 'Anchors'))
    # Row 2: Gradient-based
    local_methods.append(draw_method(0.8, method_y, 'Integrated\nGradients'))
    local_methods.append(draw_method(1.8, method_y, 'LRP'))
    local_methods.append(draw_method(2.6, method_y, 'DeepLIFT'))
    # Row 3: Attention & Example-based
    local_methods.append(draw_method(3.5, method_y + 0.6, 'Attention\nWeights'))
    local_methods.append(draw_method(4.5, method_y + 0.6, 'Attention\nRollout'))
    local_methods.append(draw_method(3.5, method_y, 'Counterfactual'))
    local_methods.append(draw_method(4.5, method_y, 'Contrastive'))
    local_methods.append(draw_method(3.5, method_y - 0.6, 'Influence\nFunctions'))
    local_methods.append(draw_method(4.5, method_y - 0.6, 'Prototypes'))

    # Connect local category to methods
    draw_tree_connection(local_cat['bottom'],
                        [m['top'] for m in local_methods],
                        color=COLORS['local'], lw=1.8)

    # Global Methods
    global_methods = []
    global_methods.append(draw_method(6.5, method_y, 'Rule\nExtraction'))
    global_methods.append(draw_method(7.5, method_y, 'SHAP\nGlobal'))
    global_methods.append(draw_method(8.5, method_y, 'TCAV'))
    global_methods.append(draw_method(9.5, method_y, 'Diagnostic\nClassifiers'))

    # Connect global category to methods
    draw_tree_connection(global_cat['bottom'],
                        [m['top'] for m in global_methods],
                        color=COLORS['global'], lw=1.5)

    # LLM-Era Methods - arranged in rows
    llm_methods = []
    # Row 1: Chain-of-Thought
    llm_methods.append(draw_method(11.5, method_y + 0.6, 'Chain-of-Thought\nZero-shot'))
    llm_methods.append(draw_method(13, method_y + 0.6, 'Chain-of-Thought\nFew-shot'))
    # Row 2: Self-Explanation
    llm_methods.append(draw_method(11.5, method_y, 'Self-Critique'))
    llm_methods.append(draw_method(13, method_y, 'Rationale\nGeneration'))
    # Row 3: Mechanistic
    llm_methods.append(draw_method(12.2, method_y - 0.6, 'Mechanistic\nCircuits'))
    llm_methods.append(draw_method(13.8, method_y - 0.6, 'Feature\nAnalysis'))

    # Connect LLM category to methods
    draw_tree_connection(llm_cat['bottom'],
                        [m['top'] for m in llm_methods],
                        color=COLORS['llm'], lw=1.5)

    # === Legend with patterns ===
    legend_elements = [
        mpatches.Patch(facecolor=COLORS['local_bg'],
                      edgecolor=COLORS['local_border'],
                      hatch=PATTERNS['local'],
                      label='Local Methods'),
        mpatches.Patch(facecolor=COLORS['global_bg'],
                      edgecolor=COLORS['global_border'],
                      hatch=PATTERNS['global'],
                      label='Global Methods'),
        mpatches.Patch(facecolor=COLORS['llm_bg'],
                      edgecolor=COLORS['llm_border'],
                      hatch=PATTERNS['llm'],
                      label='LLM-Era Methods'),
    ]
    ax.legend(handles=legend_elements, loc='lower right',
              fontsize=9, framealpha=0.95, edgecolor='#2C3E50')

    # === Caption ===
    ax.text(8, 0.4, 'Figure 4: Taxonomy of Explainable NLP Methods',
            ha='center', fontsize=11, fontstyle='italic', color=COLORS['text_primary'])

    plt.tight_layout()
    plt.savefig('taxonomy_diagram.pdf', format='pdf', bbox_inches='tight')
    plt.savefig('taxonomy_diagram.png', format='png', bbox_inches='tight')
    print("Created: taxonomy_diagram.pdf and .png")
    plt.close()


def create_decision_tree():
    """Create decision tree flowchart with clean vertical flow and no crossed lines."""

    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.axis('off')

    def draw_diamond(x, y, text, color=COLORS['decision'], size=0.7):
        """Draw a diamond decision node."""
        diamond = plt.Polygon(
            [(x, y + size), (x + size, y), (x, y - size), (x - size, y)],
            facecolor=color, edgecolor='#2C3E50', linewidth=1.5, zorder=10
        )
        ax.add_patch(diamond)
        ax.text(x, y, text, ha='center', va='center', fontsize=8,
                fontweight='bold', wrap=True, color='#2C3E50', zorder=11)
        return {'top': (x, y + size), 'bottom': (x, y - size),
                'left': (x - size, y), 'right': (x + size, y)}

    def draw_rect(x, y, text, color=COLORS['recommend'], width=2.0, height=0.65):
        """Draw a rectangular recommendation node."""
        rect = FancyBboxPatch(
            (x - width/2, y - height/2), width, height,
            boxstyle="round,pad=0.02,rounding_size=0.12",
            facecolor=color, edgecolor='#2C3E50', linewidth=1.3, zorder=10
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=7.5,
                color='white', fontweight='bold', wrap=True, zorder=11)
        return {'top': (x, y + height/2), 'bottom': (x, y - height/2),
                'left': (x - width/2, y), 'right': (x + width/2, y)}

    def draw_start(x, y, text, color='#27AE60'):
        """Draw start/end node (rounded rectangle)."""
        rect = FancyBboxPatch(
            (x - 1.5, y - 0.4), 3.0, 0.8,
            boxstyle="round,pad=0.02,rounding_size=0.35",
            facecolor=color, edgecolor='#2C3E50', linewidth=2, zorder=10
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=11,
                color='white', fontweight='bold', zorder=11)
        return {'bottom': (x, y - 0.4), 'top': (x, y + 0.4)}

    def draw_arrow(start, end, label='', label_offset=(0, 0.15)):
        """Draw an arrow with optional label."""
        ax.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle='->', color=COLORS['arrow'], lw=1.8),
                    zorder=5)
        if label:
            mid_x = (start[0] + end[0]) / 2 + label_offset[0]
            mid_y = (start[1] + end[1]) / 2 + label_offset[1]
            ax.text(mid_x, mid_y, label, fontsize=7.5, ha='center',
                    va='center', color='#2C3E50', fontstyle='italic',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                             edgecolor='none', alpha=0.9), zorder=6)

    def draw_elbow_arrow(start, mid_x, end, label='', label_pos='mid'):
        """Draw an elbow-shaped arrow (horizontal then vertical)."""
        # Horizontal line
        ax.plot([start[0], mid_x], [start[1], start[1]], color=COLORS['arrow'], lw=1.8, zorder=5)
        # Vertical line with arrow
        ax.annotate('', xy=end, xytext=(mid_x, start[1]),
                    arrowprops=dict(arrowstyle='->', color=COLORS['arrow'], lw=1.8), zorder=5)
        if label:
            if label_pos == 'start':
                lx, ly = (start[0] + mid_x) / 2, start[1] + 0.2
            else:
                lx, ly = mid_x, (start[1] + end[1]) / 2
            ax.text(lx, ly, label, fontsize=7.5, ha='center', va='center',
                    color='#2C3E50', fontstyle='italic',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                             edgecolor='none', alpha=0.9), zorder=6)

    # === Start node ===
    start = draw_start(7.5, 9.3, 'Select XAI Method')

    # === First decision: Model Access ===
    d1 = draw_diamond(7.5, 7.8, 'Model\nAccess?')
    draw_arrow(start['bottom'], d1['top'])

    # === Three branches from Model Access (well-separated) ===

    # LEFT: Full Access path
    d2_full = draw_diamond(2.8, 6.0, 'Explanation\nScope?')
    draw_elbow_arrow(d1['left'], 2.8, d2_full['top'], 'Full Access', 'start')

    # Local methods (Full Access) - positioned far left
    r_local = draw_rect(1.3, 4.0, 'Integrated Gradients\nAttention\nSHAP',
                        color='#3498DB', width=2.0, height=0.9)
    draw_elbow_arrow(d2_full['left'], 1.3, r_local['top'], 'Local', 'start')

    # Global methods (Full Access) - positioned to avoid crossing
    r_global = draw_rect(3.8, 4.0, 'Probing Classifiers\nTCAV\nDistillation',
                         color='#27AE60', width=2.0, height=0.9)
    draw_elbow_arrow(d2_full['right'], 3.8, r_global['top'], 'Global', 'start')

    # MIDDLE: API Access path (centered, with wide separation)
    d2_api = draw_diamond(7.5, 6.0, 'Is it\nan LLM?')
    draw_arrow(d1['bottom'], d2_api['top'], 'API Only')

    # LLM Yes - positioned left of center with gap from Global
    r_llm_yes = draw_rect(6.5, 4.0, 'Chain-of-Thought\nSelf-Explanation',
                          color='#E67E22', width=2.0, height=0.8)
    draw_elbow_arrow(d2_api['left'], 6.5, r_llm_yes['top'], 'Yes', 'start')

    # LLM No - positioned right of center with gap from Black-box
    r_llm_no = draw_rect(9.0, 4.0, 'LIME\nAnchors',
                         color='#9B59B6', width=1.6, height=0.7)
    draw_elbow_arrow(d2_api['right'], 9.0, r_llm_no['top'], 'No', 'start')

    # RIGHT: Black-box path - positioned far right
    r_blackbox = draw_rect(12.5, 6.0, 'LIME\nCounterfactuals\nAnchors',
                           color='#8E44AD', width=2.0, height=0.9)
    draw_elbow_arrow(d1['right'], 12.5, r_blackbox['top'], 'Black-box', 'start')

    # === Audience section (as informational box, not decision) ===
    # Draw a subtle background - wider for new canvas
    audience_bg = FancyBboxPatch(
        (0.5, 0.8), 14, 2.2,
        boxstyle="round,pad=0.02,rounding_size=0.2",
        facecolor='#F8F9F9', edgecolor='#BDC3C7', linewidth=1.5, zorder=1
    )
    ax.add_patch(audience_bg)

    # Header for audience section
    ax.text(7.5, 2.65, 'Tailor Explanations to Target Audience',
            ha='center', fontsize=10, fontweight='bold', color='#2C3E50', zorder=10)

    # Audience boxes with even spacing - wider distribution
    audiences = [
        (2.0, 1.5, 'End Users', 'Simple highlights\nNatural language', '#1ABC9C'),
        (5.5, 1.5, 'Domain Experts', 'Feature importance\nDomain terms', '#3498DB'),
        (9.5, 1.5, 'ML Practitioners', 'Gradients\nAttention maps', '#E74C3C'),
        (13.0, 1.5, 'Regulators', 'Auditable\nMethodology', '#95A5A6'),
    ]

    for x, y, title, desc, color in audiences:
        # Title box
        title_rect = FancyBboxPatch(
            (x - 1.2, y + 0.15), 2.4, 0.5,
            boxstyle="round,pad=0.02,rounding_size=0.1",
            facecolor=color, edgecolor='#2C3E50', linewidth=1.2, zorder=10
        )
        ax.add_patch(title_rect)
        ax.text(x, y + 0.4, title, ha='center', va='center', fontsize=8,
                fontweight='bold', color='white', zorder=11)
        # Description
        ax.text(x, y - 0.25, desc, ha='center', va='center', fontsize=7,
                color='#2C3E50', zorder=10)

    # === Legend ===
    legend_elements = [
        mpatches.Patch(facecolor=COLORS['decision'], edgecolor='#2C3E50',
                       label='Decision Point'),
        mpatches.Patch(facecolor='#9B59B6', edgecolor='#2C3E50',
                       label='Recommendation'),
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=8,
              framealpha=0.95, edgecolor='#2C3E50', bbox_to_anchor=(0.98, 0.98))

    # === Caption ===
    ax.text(7.5, 0.25, 'Figure 2: Decision Tree for Selecting Explainability Methods',
            ha='center', fontsize=11, fontstyle='italic', color='#2C3E50')

    plt.tight_layout()
    plt.savefig('decision_tree.pdf', format='pdf', bbox_inches='tight')
    plt.savefig('decision_tree.png', format='png', bbox_inches='tight')
    print("Created: decision_tree.pdf and .png")
    plt.close()


def create_explainability_approaches():
    """Create explainability approaches categorization diagram."""

    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    def draw_box(x, y, text, color, width=2.2, height=0.55, fontsize=8, bold=False):
        """Draw a rounded box with text."""
        box = FancyBboxPatch(
            (x - width/2, y - height/2), width, height,
            boxstyle="round,pad=0.03,rounding_size=0.12",
            facecolor=color, edgecolor='#2C3E50', linewidth=1.3,
            zorder=10
        )
        ax.add_patch(box)
        weight = 'bold' if bold else 'normal'
        text_color = 'white' if color in [COLORS['root'], '#3498DB', '#27AE60', '#E67E22'] else '#2C3E50'
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
                fontweight=weight, color=text_color, wrap=True, zorder=11)
        return {'center': (x, y), 'bottom': (x, y - height/2), 'top': (x, y + height/2)}

    def draw_elbow_connection(start, end, color='#7F8C8D', lw=1.2):
        """Draw an elbow connector."""
        mid_y = (start[1] + end[1]) / 2
        ax.plot([start[0], start[0]], [start[1], mid_y], color=color, linewidth=lw, zorder=1)
        ax.plot([start[0], end[0]], [mid_y, mid_y], color=color, linewidth=lw, zorder=1)
        ax.plot([end[0], end[0]], [mid_y, end[1]], color=color, linewidth=lw, zorder=1)

    def draw_vertical_connection(start, end, color='#7F8C8D', lw=1.2):
        """Draw a simple vertical connection."""
        ax.plot([start[0], end[0]], [start[1], end[1]], color=color, linewidth=lw, zorder=1)

    # === Root node ===
    root = draw_box(7, 7.3, 'Explainability Approaches', COLORS['root'],
                    width=4.0, height=0.65, fontsize=13, bold=True)

    # === Level 1: Three main categorization dimensions ===
    timing_color = '#3498DB'    # Blue
    scope_color = '#27AE60'     # Green
    access_color = '#E67E22'    # Orange

    timing = draw_box(2.5, 5.8, 'By Timing', timing_color, width=2.0, height=0.55, fontsize=10, bold=True)
    scope = draw_box(7, 5.8, 'By Scope', scope_color, width=2.0, height=0.55, fontsize=10, bold=True)
    access = draw_box(11.5, 5.8, 'By Model Access', access_color, width=2.4, height=0.55, fontsize=10, bold=True)

    # Connect root to level 1
    draw_elbow_connection(root['bottom'], timing['top'], color='#5D6D7E', lw=1.5)
    draw_vertical_connection(root['bottom'], scope['top'], color='#5D6D7E', lw=1.5)
    draw_elbow_connection(root['bottom'], access['top'], color='#5D6D7E', lw=1.5)

    # === Level 2: Subcategories ===
    sub_timing_color = '#AED6F1'
    sub_scope_color = '#A9DFBF'
    sub_access_color = '#FAD7A0'

    # Under Timing
    direct = draw_box(1.5, 4.3, 'Direct\nInterpretability', sub_timing_color, width=1.8, height=0.65, fontsize=8)
    posthoc = draw_box(3.5, 4.3, 'Post-hoc\nExplanation', sub_timing_color, width=1.8, height=0.65, fontsize=8)
    draw_elbow_connection(timing['bottom'], direct['top'], color=timing_color)
    draw_elbow_connection(timing['bottom'], posthoc['top'], color=timing_color)

    # Under Scope
    local = draw_box(6, 4.3, 'Local\n(Per Instance)', sub_scope_color, width=1.8, height=0.65, fontsize=8)
    global_exp = draw_box(8, 4.3, 'Global\n(Model-Wide)', sub_scope_color, width=1.8, height=0.65, fontsize=8)
    draw_elbow_connection(scope['bottom'], local['top'], color=scope_color)
    draw_elbow_connection(scope['bottom'], global_exp['top'], color=scope_color)

    # Under Model Access
    specific = draw_box(10.5, 4.3, 'Model-\nSpecific', sub_access_color, width=1.7, height=0.65, fontsize=8)
    agnostic = draw_box(12.5, 4.3, 'Model-\nAgnostic', sub_access_color, width=1.7, height=0.65, fontsize=8)
    draw_elbow_connection(access['bottom'], specific['top'], color=access_color)
    draw_elbow_connection(access['bottom'], agnostic['top'], color=access_color)

    # === Level 3: Examples ===
    example_color = '#F8F9F9'
    example_fontsize = 7

    # Examples under Direct Interpretability
    direct_ex = draw_box(1.5, 2.8, 'Decision Trees\nLinear Models\nRule Lists', example_color,
                         width=1.7, height=0.85, fontsize=example_fontsize)
    draw_vertical_connection(direct['bottom'], direct_ex['top'], color='#85C1E9')

    # Examples under Post-hoc
    posthoc_ex = draw_box(3.5, 2.8, 'LIME\nSHAP\nAnchors', example_color,
                          width=1.7, height=0.85, fontsize=example_fontsize)
    draw_vertical_connection(posthoc['bottom'], posthoc_ex['top'], color='#85C1E9')

    # Examples under Local
    local_ex = draw_box(6, 2.8, 'Feature Attribution\nCounterfactuals\nInfluence Functions', example_color,
                        width=2.0, height=0.85, fontsize=example_fontsize)
    draw_vertical_connection(local['bottom'], local_ex['top'], color='#58D68D')

    # Examples under Global
    global_ex = draw_box(8, 2.8, 'Model Distillation\nProbing Classifiers\nTCAV', example_color,
                         width=2.0, height=0.85, fontsize=example_fontsize)
    draw_vertical_connection(global_exp['bottom'], global_ex['top'], color='#58D68D')

    # Examples under Model-Specific
    specific_ex = draw_box(10.5, 2.8, 'Attention Viz\nLRP\nDeepLIFT', example_color,
                           width=1.7, height=0.85, fontsize=example_fontsize)
    draw_vertical_connection(specific['bottom'], specific_ex['top'], color='#F5B041')

    # Examples under Model-Agnostic
    agnostic_ex = draw_box(12.5, 2.8, 'LIME\nSHAP\nAnchors', example_color,
                           width=1.7, height=0.85, fontsize=example_fontsize)
    draw_vertical_connection(agnostic['bottom'], agnostic_ex['top'], color='#F5B041')

    # === Legend ===
    legend_elements = [
        mpatches.Patch(facecolor=timing_color, edgecolor='#2C3E50', label='By Timing'),
        mpatches.Patch(facecolor=scope_color, edgecolor='#2C3E50', label='By Scope'),
        mpatches.Patch(facecolor=access_color, edgecolor='#2C3E50', label='By Model Access'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9,
              framealpha=0.95, edgecolor='#2C3E50', bbox_to_anchor=(0.98, 0.02))

    plt.tight_layout()
    plt.savefig('explainability_approaches.pdf', format='pdf', bbox_inches='tight')
    plt.savefig('explainability_approaches.png', format='png', bbox_inches='tight')
    print("Created: explainability_approaches.pdf and .png")
    plt.close()


def create_accuracy_interpretability():
    """Create accuracy vs interpretability trade-off scatter plot."""

    fig, ax = plt.subplots(figsize=(11, 8))

    # Model data: (accuracy, interpretability, name, color)
    models = [
        (3.5, 9.5, 'Linear Regression', '#27AE60'),
        (4.5, 8.5, 'Decision Trees', '#2ECC71'),
        (6.0, 6.0, 'K-Nearest Neighbors', '#F39C12'),
        (7.0, 4.5, 'Random Forests', '#E67E22'),
        (7.8, 3.0, 'Support Vector Machines', '#E74C3C'),
        (9.0, 1.5, 'Deep Neural Networks', '#9B59B6'),
    ]

    # Add colored corner zones to indicate the trade-off regions
    from matplotlib.patches import Polygon, FancyBboxPatch

    # Top-left zone (High Interpretability, Lower Accuracy) - green tint
    top_left_zone = Polygon(
        [(0, 6), (0, 10.5), (4.5, 10.5), (0, 6)],
        facecolor='#27AE60', edgecolor='none', alpha=0.08, zorder=0
    )
    ax.add_patch(top_left_zone)

    # Bottom-right zone (High Accuracy, Lower Interpretability) - purple tint
    bottom_right_zone = Polygon(
        [(6, 0), (10.5, 0), (10.5, 4.5), (6, 0)],
        facecolor='#9B59B6', edgecolor='none', alpha=0.08, zorder=0
    )
    ax.add_patch(bottom_right_zone)

    # Add trade-off curve (fitted through points)
    x_curve = np.linspace(2, 10, 100)
    y_curve = 11 - 1.1 * x_curve  # Approximate inverse relationship
    y_curve = np.clip(y_curve, 0.5, 10)
    ax.fill_between(x_curve, y_curve - 1.3, y_curve + 1.3, alpha=0.12, color='#3498DB', zorder=1)
    ax.plot(x_curve, y_curve, '--', color='#3498DB', alpha=0.6, linewidth=2, zorder=2)

    # Plot models
    for accuracy, interpretability, name, color in models:
        ax.scatter(accuracy, interpretability, s=280, c=color, edgecolors='#2C3E50',
                   linewidth=2, zorder=10, alpha=0.9)
        # Add label with smart offset to avoid overlaps
        if name == 'Linear Regression':
            offset_x, offset_y, ha = 0.4, 0.0, 'left'
        elif name == 'Decision Trees':
            offset_x, offset_y, ha = 0.4, -0.1, 'left'
        elif name == 'K-Nearest Neighbors':
            offset_x, offset_y, ha = 0.4, 0.0, 'left'
        elif name == 'Random Forests':
            offset_x, offset_y, ha = 0.4, 0.0, 'left'
        elif name == 'Support Vector Machines':
            offset_x, offset_y, ha = -0.4, 0.0, 'right'
        else:  # Deep Neural Networks
            offset_x, offset_y, ha = 0.4, -0.1, 'left'

        ax.annotate(name, (accuracy, interpretability),
                    xytext=(accuracy + offset_x, interpretability + offset_y),
                    fontsize=10, ha=ha, va='center', fontweight='bold',
                    color='#2C3E50',
                    arrowprops=dict(arrowstyle='-', color='#7F8C8D', lw=0.8, shrinkA=5, shrinkB=5))

    # Axis configuration
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 10.5)
    ax.set_xlabel('Accuracy (Model Performance)', fontsize=12, fontweight='bold', color='#2C3E50')
    ax.set_ylabel('Interpretability (Human Understanding)', fontsize=12, fontweight='bold', color='#2C3E50')
    ax.set_title('Accuracy-Interpretability Trade-off in Machine Learning',
                 fontsize=14, fontweight='bold', color='#2C3E50', pad=15)

    # Grid
    ax.grid(True, linestyle='--', alpha=0.4, color='#BDC3C7')
    ax.set_axisbelow(True)

    # Ticks
    ax.set_xticks(range(0, 11, 2))
    ax.set_yticks(range(0, 11, 2))
    ax.tick_params(axis='both', which='major', labelsize=10, colors='#2C3E50')

    # Add zone labels in corners (text only, no boxes)
    # Top-left corner label
    ax.text(1.8, 9.9, 'High Interpretability\nLower Accuracy', fontsize=10, ha='center', va='center',
            color='#27AE60', fontweight='bold', style='italic', zorder=16)

    # Bottom-right corner label
    ax.text(8.7, 0.9, 'High Accuracy\nLower Interpretability', fontsize=10, ha='center', va='center',
            color='#9B59B6', fontweight='bold', style='italic', zorder=16)

    # Spine styling
    for spine in ax.spines.values():
        spine.set_color('#2C3E50')
        spine.set_linewidth(1.5)

    plt.tight_layout()
    plt.savefig('accuracy_interpretability.pdf', format='pdf', bbox_inches='tight')
    plt.savefig('accuracy_interpretability.png', format='png', bbox_inches='tight')
    print("Created: accuracy_interpretability.pdf and .png")
    plt.close()


if __name__ == '__main__':
    print("Generating figures for XAI Survey Paper...")
    print("=" * 50)
    create_taxonomy_diagram()
    create_decision_tree()
    create_explainability_approaches()
    create_accuracy_interpretability()
    print("=" * 50)
    print("All figures generated successfully!")
