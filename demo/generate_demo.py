"""Generate the demo PNG for the README."""

from itertools import combinations

import matplotlib
import matplotlib.pyplot as plt

from simple_venn import venn2
from simple_venn import venn3
from simple_venn import venn4

matplotlib.use("Agg")

DEMO_PNG = "demo/demo.png"


def main() -> None:
    """Generate a demo figure showing venn2, venn3, and venn4 side by side."""
    fig, axes = plt.subplots(1, 3, figsize=(24, 8))

    # two-way venn
    sets = "A B".split()
    subsets = ["".join(combo) for i in range(1, 3) for combo in combinations(sets, i)]
    ax = axes[0]
    venn2(subsets, ax=ax)
    ax.set_title("venn2", fontsize=24)

    # three-way venn
    sets = "A B C".split()
    subsets = ["".join(combo) for i in range(1, 4) for combo in combinations(sets, i)]
    ax = axes[1]
    venn3(subsets, ax=ax)
    ax.set_title("venn3", fontsize=24)

    # four-way venn
    sets = "A B C D".split()
    subsets = ["".join(combo) for i in range(1, 5) for combo in combinations(sets, i)]
    ax = axes[2]
    venn4(subsets, ax=ax)
    ax.set_title("venn4", fontsize=24)

    fig.suptitle("simple_venn Demo", fontsize=30)
    plt.savefig(DEMO_PNG, bbox_inches="tight")
    print(f"Saved {DEMO_PNG}")


if __name__ == "__main__":
    main()
