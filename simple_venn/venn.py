# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 msto <mstone5@mgh.harvard.edu>
#
# Distributed under terms of the MIT license.

"""Simple Venn diagrams."""

from collections.abc import Sequence
from typing import Union

import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

SubsetValue = Union[int, float, str]


def venn4(
    subsets: Sequence[SubsetValue],
    set_labels: tuple[str, ...] = ("A", "B", "C", "D"),
    set_colors: tuple[str, ...] = ("#8eab12", "#feb308", "#8f1402", "#0485d1"),
    alpha: float = 0.4,
    ax: Axes | None = None,
    set_label_fontsize: int = 18,
    subset_label_fontsize: int = 14,
) -> Axes:
    """
    Plot a four-way venn diagram.

    Parameters
    ----------
    subsets : list
        Values for each subset of Venn.
        May be int, float, or string. Use strings for any custom formatting
        [A, B, C, D, AB, AC, AD, BC, BD, CD, ABC, ABD, ACD, BCD, ABCD]
    set_labels : list of str, optional
        Labels around ellipses' exterior
    set_colors : list, optional
        Colors of Venn ellipses.
        Defaults to xkcd's [pea green, amber, brick red, cerulean]
    alpha : float, optional
        Alpha of Venn ellipses
    ax : AxesSubplot
        Axis to draw Venn on
    set_label_fontsize : int, optional
        Fontsize of exterior set labels.
        Default=18pt, optimized for 8in by 8in figure
    subset_label_fontsize : int, optional
        Fontsize of interior count labels
        Default=14pt, optimized for 8in by 8in figure

    Returns:
    -------
    ax : AxesSubplot
    """
    if len(subsets) != 15:
        raise Exception("Must provide exactly 15 subset values")

    if ax is None:
        ax = plt.gca()

    width = 0.75
    height = 0.5
    alpha = 0.4

    # Draw ellipses
    ellipse_coords = [
        ((0.50, 0.60), -45),  # A (top left)
        ((0.50, 0.60), 45),  # B (top right)
        ((0.65, 0.40), 45),  # C (bottom right)
        ((0.35, 0.40), -45),  # D (bottom left)
    ]
    for (coord, angle), color in zip(ellipse_coords, set_colors, strict=True):
        e = patches.Ellipse(coord, width, height, angle=angle, alpha=alpha, facecolor=color)
        ax.add_patch(e)

    # Add exterior set labels
    set_label_positions = [
        (0.22, 0.91, 45),  # A (top left)
        (0.78, 0.91, -45),  # B (top right)
        (0.12, 0.22, -45),  # C (bottom right)
        (0.88, 0.22, 45),  # D (bottom left)
    ]
    for label, (x, y, rotation) in zip(set_labels, set_label_positions, strict=True):
        ax.text(
            x, y, label, rotation=rotation, ha="center", va="center", fontsize=set_label_fontsize
        )

    # Add subset count labels
    subset_labels = [str(s) for s in subsets]
    subset_positions = [
        (0.30, 0.83, 45),  # A
        (0.70, 0.83, -45),  # B
        (0.18, 0.30, -45),  # C
        (0.83, 0.30, 45),  # D
        (0.50, 0.77, 0),  # AB
        (0.22, 0.68, 55),  # AC
        (0.75, 0.40, 45),  # AD
        (0.25, 0.40, -45),  # BC
        (0.78, 0.68, -55),  # BD
        (0.50, 0.18, 0),  # CD
        (0.33, 0.58, 0),  # ABC
        (0.66, 0.58, 0),  # ABD
        (0.60, 0.32, 10),  # ACD
        (0.40, 0.32, -10),  # BCD
        (0.50, 0.45, 0),  # ABCD
    ]
    for label, (x, y, rotation) in zip(subset_labels, subset_positions, strict=True):
        ax.text(
            x, y, label, rotation=rotation, ha="center", va="center", fontsize=subset_label_fontsize
        )

    # Remove borders
    ax.set_xticklabels("")
    ax.set_yticklabels("")
    ax.axis("off")

    ax.set_aspect("equal")

    return ax


def venn3(
    subsets: Sequence[SubsetValue],
    set_labels: tuple[str, ...] = ("A", "B", "C"),
    set_colors: tuple[str, ...] = ("#feb308", "#8f1402", "#0485d1"),
    alpha: float = 0.4,
    ax: Axes | None = None,
    set_label_fontsize: int = 18,
    subset_label_fontsize: int = 14,
) -> Axes:
    """
    Plot a three-way venn diagram.

    Parameters
    ----------
    subsets : list
        Values for each subset of Venn.
        May be int, float, or string. Use strings for any custom formatting
        [A, B, C, AB, AC, BC, ABC]
    set_labels : list of str, optional
        Labels around ellipses' exterior
    set_colors : list, optional
        Colors of Venn ellipses.
        Defaults to xkcd's [amber, brick red, cerulean]
    alpha : float, optional
        Alpha of Venn ellipses
    ax : AxesSubplot
        Axis to draw Venn on
    set_label_fontsize : int, optional
        Fontsize of exterior set labels.
        Default=18pt, optimized for 8in by 8in figure
    subset_label_fontsize : int, optional
        Fontsize of interior count labels
        Default=14pt, optimized for 8in by 8in figure

    Returns:
    -------
    ax : AxesSubplot
    """
    if len(subsets) != 7:
        raise Exception("Must provide exactly 7 subset values")

    if ax is None:
        ax = plt.gca()

    width = 0.6
    height = 0.6
    alpha = 0.4

    # Draw ellipses
    ellipse_coords = [
        (0.50, 0.63),  # A (top)
        (0.63, 0.37),  # B (bottom right)
        (0.37, 0.37),  # C (bottom left)
    ]
    for color, coord in zip(set_colors, ellipse_coords, strict=True):
        e = patches.Ellipse(coord, width, height, alpha=alpha, facecolor=color)
        ax.add_patch(e)

    # Add exterior set labels
    set_label_positions = [
        (0.50, 0.97, 0),  # A (top)
        (0.88, 0.14, 45),  # B (bottom right)
        (0.12, 0.14, -45),  # C (bottom left)
    ]
    for label, (x, y, rotation) in zip(set_labels, set_label_positions, strict=True):
        ax.text(
            x, y, label, rotation=rotation, ha="center", va="center", fontsize=set_label_fontsize
        )

    # Add subset count labels
    subset_labels = [str(s) for s in subsets]
    subset_positions = [
        (0.5, 0.77),  # A
        (0.77, 0.3),  # B
        (0.23, 0.3),  # C
        (0.7, 0.55),  # AB
        (0.3, 0.55),  # AC
        (0.5, 0.24),  # BC
        (0.5, 0.47),  # ABC
    ]
    for label, (x, y) in zip(subset_labels, subset_positions, strict=True):
        ax.text(x, y, label, rotation=0, ha="center", va="center", fontsize=subset_label_fontsize)

    # Remove borders
    ax.set_xticklabels("")
    ax.set_yticklabels("")
    ax.axis("off")
    ax.set_aspect("equal")

    return ax


def venn2(
    subsets: Sequence[SubsetValue],
    set_labels: tuple[str, ...] = ("A", "B"),
    set_colors: tuple[str, ...] = ("#0485d1", "#8f1402"),
    alpha: float = 0.4,
    ax: Axes | None = None,
    set_label_fontsize: int = 18,
    subset_label_fontsize: int = 14,
) -> Axes:
    """
    Plot a two-way venn diagram.

    Parameters
    ----------
    subsets : list
        Values for each subset of Venn.
        May be int, float, or string. Use strings for any custom formatting
        [A, B, AB]
    set_labels : list of str, optional
        Labels around ellipses' exterior
    set_colors : list, optional
        Colors of Venn ellipses.
        Defaults to xkcd's [cerulean, brick red]
    alpha : float, optional
        Alpha of Venn ellipses
    ax : AxesSubplot
        Axis to draw Venn on
    set_label_fontsize : int, optional
        Fontsize of exterior set labels.
        Default=18pt, optimized for 8in by 8in figure
    subset_label_fontsize : int, optional
        Fontsize of interior count labels
        Default=14pt, optimized for 8in by 8in figure

    Returns:
    -------
    ax : AxesSubplot
    """
    if len(subsets) != 3:
        raise Exception("Must provide exactly 3 subset values")

    if ax is None:
        ax = plt.gca()

    # Circle shape and coloring
    width = 0.65
    height = 0.65
    alpha = 0.4

    # Draw ellipses
    ellipse_coords = [
        (0.37, 0.5),  # A (left)
        (0.63, 0.5),  # B (right)
    ]
    for color, coord in zip(set_colors, ellipse_coords, strict=True):
        e = patches.Ellipse(coord, width, height, alpha=alpha, facecolor=color)
        ax.add_patch(e)

    # Add exterior set labels
    set_label_positions = [
        (0.18, 0.82, 30),  # A (left)
        (0.82, 0.82, -30),  # B (right)
    ]
    for label, (x, y, rotation) in zip(set_labels, set_label_positions, strict=True):
        ax.text(
            x, y, label, rotation=rotation, ha="center", va="center", fontsize=set_label_fontsize
        )

    # Add subset count labels
    subset_labels = [str(s) for s in subsets]
    subset_positions = [
        (0.2, 0.5),  # A
        (0.8, 0.5),  # B
        (0.5, 0.5),  # AB
    ]
    for label, (x, y) in zip(subset_labels, subset_positions, strict=True):
        ax.text(x, y, label, rotation=0, ha="center", va="center", fontsize=subset_label_fontsize)

    # Remove borders
    ax.set_xticklabels("")
    ax.set_yticklabels("")
    ax.axis("off")
    ax.set_aspect("equal")

    return ax
