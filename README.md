# simple-venn

Simple two-way, three-way, and four-way Venn diagrams in matplotlib.

The function calls are mostly interchangeable with those from
[matplotlib_venn](https://github.com/konstantint/matplotlib-venn). The `venn2`
and `venn3` functions lack the `normalize_to` parameter, and all functions
return an `AxesSubplot` object instead of a `VennDiagram`.

`simple-venn` adds four-way Venn diagrams and makes label customization
slightly easier by permitting string subset labels and including parameters for
set and subset label font sizes.  The default font sizes are appropriate for an
8 inch by 8 inch axes.

## Installation
Available on [PyPi](https://pypi.python.org/pypi/simple-venn/0.1.0)

    pip install simple-venn

## Example
![demo](https://github.com/msto/simple-venn/blob/master/demo/demo.png)

The code used to generate this figure can be found in the included [iPython
notebook demo](demo/simple-venn-demo.ipynb).

