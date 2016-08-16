# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 msto <mstone5@mgh.harvard.edu>
#
# Distributed under terms of the MIT license.

"""

"""

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def venn4(subsets,
          set_labels=('A', 'B', 'C', 'D'),
          set_colors=['#8f1402', '#0485d1', '#feb308', '#8eab12'],
          alpha=0.4,
          ax=None,
          set_label_fontsize=18,
          subset_label_fontsize=14):
    
    if ax is None:
        ax = plt.gca()

    width = 0.75
    height = 0.5
    ellipse_angle = 45
    alpha = 0.4
    text_angle = 45

    e = patches.Ellipse((0.65, 0.4), width, height, ellipse_angle, alpha=alpha, facecolor=set_colors[0])
    ax.add_patch(e)
    ax.text(0.17, 0.92, set_labels[0], rotation=45, fontsize=set_label_fontsize)

    e = patches.Ellipse((0.35, 0.4), width, height, -ellipse_angle, alpha=alpha, facecolor=set_colors[1])
    ax.add_patch(e)
    ax.text(0.73, 0.92, set_labels[1], rotation=-45, fontsize=set_label_fontsize)

    e = patches.Ellipse((0.5, 0.6), width, height, ellipse_angle, alpha=alpha, facecolor=set_colors[2])
    ax.add_patch(e)
    ax.text(0.05, 0.26, set_labels[2], rotation=-45, fontsize=set_label_fontsize)

    e = patches.Ellipse((0.5, 0.6), width, height, -ellipse_angle, alpha=alpha, facecolor=set_colors[3])
    ax.add_patch(e)
    ax.text(0.85, 0.28, set_labels[3], rotation=50, fontsize=set_label_fontsize)

    # D, L, M, W, DL, DM, DW, LM, LW, MW, DLM, DLW, DMW, LMW, DLMW
    
    subsets = [str(s) for s in subsets]
    # ax.text(0.25, 0.8, subsets[0], va='center', rotation=45, fontsize=14)
    ax.text(0.3, 0.83, subsets[0], va='center', ha='center', rotation=45, fontsize=subset_label_fontsize)
    ax.text(0.7, 0.83, subsets[1], va='center', ha='center', rotation=-45, fontsize=subset_label_fontsize)
    ax.text(0.18, 0.3, subsets[2], va='center', ha='center', rotation=-45, fontsize=subset_label_fontsize)
    ax.text(0.83, 0.3, subsets[3], va='center', ha='center', rotation=45, fontsize=subset_label_fontsize)
    ax.text(0.5, 0.77, subsets[4], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize) # DL
    ax.text(0.22, 0.68, subsets[5], va='center', ha='center', rotation=55, fontsize=subset_label_fontsize) # DM
    ax.text(0.75, 0.4, subsets[6], va='center', ha='center', rotation=45, fontsize=subset_label_fontsize) # DW
    ax.text(0.25, 0.4, subsets[7], va='center', ha='center', rotation=-45, fontsize=subset_label_fontsize) # LM
    ax.text(0.77, 0.68, subsets[8], va='center', ha='center', rotation=-55, fontsize=subset_label_fontsize) # LW
    ax.text(0.5, 0.18, subsets[9], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize) # MW
    ax.text(0.33, 0.58, subsets[10], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize) # DLM
    ax.text(0.66, 0.58, subsets[11], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize) # DLW
    ax.text(0.6, 0.32, subsets[12], va='center', ha='center', rotation=10, fontsize=subset_label_fontsize) # DMW
    ax.text(0.4, 0.32, subsets[13], va='center', ha='center', rotation=-10, fontsize=subset_label_fontsize) # LMW
    ax.text(0.5, 0.45, subsets[14], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize) # DLMW

    # Remove borders
    ax.set_xticklabels('')
    ax.set_yticklabels('')
    ax.axis('off')
    
    # Trim whitespace
#     ax.set_ylim(0.07, 0.96)
    ax.set_aspect('equal')

    return ax

def venn3(subsets,
          set_labels=('A', 'B', 'C'),
          set_colors=['#8f1402', '#0485d1', '#feb308'],
          alpha=0.4,
          ax=None,
          set_label_fontsize=18,
          subset_label_fontsize=14):

    if ax is None:
        ax = plt.gca()

    width = 0.6
    height = 0.6
    ellipse_angle = 45
    alpha = 0.4
    text_angle = 45
    set_label_fontsize = 18
    subset_label_fontsize = 14

    e = patches.Ellipse((0.63, 0.37), width, height, alpha=alpha, facecolor=set_colors[0])
    ax.add_patch(e)
    ax.text(0.5, 0.97, set_labels[0], rotation=0, ha='center', va='center', fontsize=set_label_fontsize)

    e = patches.Ellipse((0.37, 0.37), width, height, alpha=alpha, facecolor=set_colors[1])
    ax.add_patch(e)
    ax.text(0.88, 0.14, set_labels[1], rotation=45, ha='center', va='center', fontsize=set_label_fontsize)

    e = patches.Ellipse((0.5, 0.63), width, height, alpha=alpha, facecolor=set_colors[2])
    ax.add_patch(e)
    ax.text(0.12, 0.14, set_labels[2], rotation=-45, ha='center', va='center', fontsize=set_label_fontsize)

    # D, L, M, W, DL, DM, DW, LM, LW, MW, DLM, DLW, DMW, LMW, DLMW

    subsets = [str(s) for s in subsets]
    # ax.text(0.25, 0.8, subsets[0], va='center', rotation=45, fontsize=14)
    ax.text(0.5, 0.77, subsets[0], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize)
    ax.text(0.77, 0.3, subsets[1], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize)
    ax.text(0.23, 0.3, subsets[2], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize)
    ax.text(0.7, 0.55, subsets[3], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize)
    ax.text(0.3, 0.55, subsets[4], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize) # DL
    ax.text(0.5, 0.24, subsets[5], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize) # DM
    ax.text(0.5, 0.47, subsets[6], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize) # DW

    # Remove borders
    ax.set_xticklabels('')
    ax.set_yticklabels('')
    ax.axis('off')
    ax.set_aspect('equal')

    return ax

def venn2(subsets,
          set_labels=('A', 'B'),
          set_colors=['#8f1402', '#0485d1'],
          alpha=0.4,
          ax=None,
          set_label_fontsize=18,
          subset_label_fontsize=14):
    
    if ax is None:
        ax = plt.gca()
        
    width = 0.65
    height = 0.65
    ellipse_angle = 45
    alpha = 0.4
    text_angle = 45
    set_label_fontsize = 18
    subset_label_fontsize = 14

    e = patches.Ellipse((0.63, 0.5), width, height, alpha=alpha, facecolor=set_colors[0])
    ax.add_patch(e)
    ax.text(0.18, 0.82, set_labels[0], rotation=30, ha='center', va='center', fontsize=set_label_fontsize)

    e = patches.Ellipse((0.37, 0.5), width, height, alpha=alpha, facecolor=set_colors[1])
    ax.add_patch(e)
    ax.text(0.82, 0.82, set_labels[1], rotation=-30, ha='center', va='center', fontsize=set_label_fontsize)

    # D, L, M, W, DL, DM, DW, LM, LW, MW, DLM, DLW, DMW, LMW, DLMW

    subsets = [str(s) for s in subsets]
    # ax.text(0.25, 0.8, subsets[0], va='center', rotation=45, fontsize=14)
    ax.text(0.2, 0.5, subsets[0], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize)
    ax.text(0.8, 0.5, subsets[1], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize)
    ax.text(0.5, 0.5, subsets[2], va='center', ha='center', rotation=0, fontsize=subset_label_fontsize)


    # Remove borders
    ax.set_xticklabels('')
    ax.set_yticklabels('')
    ax.axis('off')
    ax.set_aspect('equal')

    return ax
