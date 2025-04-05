ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/installation/conda.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/installation/conda.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Conda [¶](https://docs.manim.community/en/stable/installation/conda.html\#conda "Link to this heading")

## Required Dependencies [¶](https://docs.manim.community/en/stable/installation/conda.html\#required-dependencies "Link to this heading")

There are several package managers that work with conda packages,
namely [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html),
[mamba](https://mamba.readthedocs.io/) and [pixi](https://pixi.sh/).

After installing your package manager, you can create a new environment and install `manim` inside by running

conda / mamba

```
# if you want to use mamba, just replace conda below with mamba
conda create -n my-manim-environment
conda activate my-manim-environment
conda install -c conda-forge manim

```

Copy to clipboard

pixi

```
pixi init
pixi add manim

```

Copy to clipboard

Since all dependencies (except LaTeX) are handled by conda, you don’t need to worry
about needing to install additional dependencies.

## Optional Dependencies [¶](https://docs.manim.community/en/stable/installation/conda.html\#optional-dependencies "Link to this heading")

In order to make use of Manim’s interface to LaTeX to, for example, render
equations, LaTeX has to be installed as well. Note that this is an optional
dependency: if you don’t intend to use LaTeX, you don’t have to install it.

Recommendations on how to install LaTeX on different operating systems
can be found [in our local installation guide](https://docs.manim.community/en/stable/installation/uv.html).

## Working with Manim [¶](https://docs.manim.community/en/stable/installation/conda.html\#working-with-manim "Link to this heading")

At this point, you should have a working installation of Manim, head
over to our [Quickstart Tutorial](https://docs.manim.community/en/stable/tutorials/quickstart.html) to learn
how to make your own _Manimations_!