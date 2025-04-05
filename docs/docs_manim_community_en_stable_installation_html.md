ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/installation.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/installation.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Installation [¶](https://docs.manim.community/en/stable/installation.html\#installation "Link to this heading")

Depending on your use case, different installation options are recommended:
if you just want to play around with Manim for a bit, interactive in-browser
notebooks are a really simple way of exploring the library as they
require no local installation. Head over to
[https://try.manim.community](https://try.manim.community/) to give our interactive tutorial a try.

Otherwise, if you intend to use Manim to work on an animation project,
we recommend installing the library locally (preferably to some isolated
virtual Python environment, or a conda-like environment, or via Docker).

Warning

Note that there are several different versions of Manim. The
instructions on this website are **only** for the _community edition_.
Find out more about the [differences between Manim\\
versions](https://docs.manim.community/en/stable/faq/installation.html#different-versions) if you are unsure which
version you should install.

1. [(Recommended) Installing Manim via Python’s package manager pip](https://docs.manim.community/en/stable/installation.html#local-installation)

2. [Installing Manim to a conda environment](https://docs.manim.community/en/stable/installation.html#conda-installation)

3. [Using Manim via Docker](https://docs.manim.community/en/stable/installation.html#docker-installation)

4. [Interactive Jupyter notebooks via Binder / Google Colab](https://docs.manim.community/en/stable/installation.html#interactive-online)


## Installing Manim locally via pip [¶](https://docs.manim.community/en/stable/installation.html\#installing-manim-locally-via-pip "Link to this heading")

The recommended way of installing Manim is by using Python’s package manager
pip. If you already have a Python environment set up, you can simply run
`pip install manim` to install the library.

Our [local installation guide](https://docs.manim.community/en/stable/installation/uv.html) provides more detailed
instructions, including best practices for setting up a suitable local environment.

## Installing Manim via Conda and related environment managers [¶](https://docs.manim.community/en/stable/installation.html\#installing-manim-via-conda-and-related-environment-managers "Link to this heading")

Conda is a package manager for Python that allows creating environments
where all your dependencies are stored. Like this, you don’t clutter up your PC with
unwanted libraries and you can just delete the environment when you don’t need it anymore.
It is a good way to install manim since all dependencies like `pycairo`, etc. come with it.
Also, the installation steps are the same, no matter if you are
on Windows, Linux, Intel Macs or on Apple Silicon.

Note

There are various popular alternatives to Conda like
[mamba](https://mamba.readthedocs.io/en/latest/) /
[micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html),
or [pixi](https://pixi.sh/).
They all can be used to setup a suitable, isolated environment
for your Manim projects.

The following pages show how to install Manim in a conda environment:

- [Conda](https://docs.manim.community/en/stable/installation/conda.html)
  - [Required Dependencies](https://docs.manim.community/en/stable/installation/conda.html#required-dependencies)
  - [Optional Dependencies](https://docs.manim.community/en/stable/installation/conda.html#optional-dependencies)
  - [Working with Manim](https://docs.manim.community/en/stable/installation/conda.html#working-with-manim)

## Using Manim via Docker [¶](https://docs.manim.community/en/stable/installation.html\#using-manim-via-docker "Link to this heading")

[Docker](https://www.docker.com/) is a virtualization tool that
allows the distribution of encapsulated software environments (containers).

The following pages contain more information about the docker image
maintained by the community, `manimcommunity/manim`:

- [Docker](https://docs.manim.community/en/stable/installation/docker.html)
  - [Basic usage of the Docker container](https://docs.manim.community/en/stable/installation/docker.html#basic-usage-of-the-docker-container)
  - [Running JupyterLab via Docker](https://docs.manim.community/en/stable/installation/docker.html#running-jupyterlab-via-docker)

## Interactive Jupyter notebooks for your browser [¶](https://docs.manim.community/en/stable/installation.html\#interactive-jupyter-notebooks-for-your-browser "Link to this heading")

Manim ships with a built-in `%%manim` IPython magic command
designed for the use within [Jupyter notebooks](https://jupyter.org/).
Our interactive tutorial over at [https://try.manim.community](https://try.manim.community/) illustrates
how Manim can be used from within a Jupyter notebook.

The following pages explain how you can setup interactive environments
like that yourself:

- [Jupyter Notebooks](https://docs.manim.community/en/stable/installation/jupyter.html)
  - [Binder](https://docs.manim.community/en/stable/installation/jupyter.html#binder)
  - [Google Colaboratory](https://docs.manim.community/en/stable/installation/jupyter.html#google-colaboratory)

## Editors [¶](https://docs.manim.community/en/stable/installation.html\#editors "Link to this heading")

If you’re using Visual Studio Code you can install an extension called
_Manim Sideview_ which provides automated rendering and an integrated preview
of the animation inside the editor. The extension can be installed through the
[marketplace of VS Code](https://marketplace.visualstudio.com/items?itemName=Rickaym.manim-sideview).

Caution

This extension is not officially maintained by the Manim Community.
If you run into issues, please report them to the extension’s author.

## Installation for developers [¶](https://docs.manim.community/en/stable/installation.html\#installation-for-developers "Link to this heading")

In order to change code in the library, it is recommended to
install Manim in a different way. Please follow the instructions
in our [contribution guide](https://docs.manim.community/en/stable/contributing.html) if you are
interested in that.