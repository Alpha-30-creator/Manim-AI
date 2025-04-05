ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/contributing.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/contributing.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Contributing [¶](https://docs.manim.community/en/stable/contributing.html\#contributing "Link to this heading")

Important

Manim is currently undergoing a major refactor. In general,
contributions implementing new features will not be accepted in this period.
Other contributions unrelated to cleaning up the codebase may also take a longer
period of time to be reviewed. This guide may quickly become outdated quickly; we
highly recommend joining our [Discord server](https://www.manim.community/discord/)
to discuss any potential contributions and keep up to date with the latest developments.

Thank you for your interest in contributing to Manim! However you have decided to contribute
or interact with the community, please always be civil and respect other
members of the community. If you haven’t read our [code of conduct](https://docs.manim.community/en/stable/conduct.html),
do so here. Manim is Free and Open Source Software (FOSS) for mathematical
animations. As such, **we welcome everyone** who is interested in
mathematics, pedagogy, computer animations, open-source,
software development, and beyond. Manim accepts many kinds of contributions,
some are detailed below:

- Code maintenance and development

- DevOps

- Documentation

- Developing educational content & narrative documentation

- Plugins to extend Manim functionality

- Testing (graphical, unit & video)

- Website design and development

- Translating documentation and docstrings


To get an overview of what our community is currently working on, check out
[our development project board](https://github.com/orgs/ManimCommunity/projects/7/views/1).

Note

Please ensure that you are reading the latest version of this guide by ensuring that “latest” is selected in the version switcher.

Contributing can be confusing, so here are a few guides:

- [Manim Development Process](https://docs.manim.community/en/stable/contributing/development.html)
  - [For first-time contributors](https://docs.manim.community/en/stable/contributing/development.html#for-first-time-contributors)
  - [Develop your contribution](https://docs.manim.community/en/stable/contributing/development.html#develop-your-contribution)
  - [Polishing Changes and Submitting a Pull Request](https://docs.manim.community/en/stable/contributing/development.html#polishing-changes-and-submitting-a-pull-request)
    - [Further useful guidelines](https://docs.manim.community/en/stable/contributing/development.html#further-useful-guidelines)
- [Adding Documentation](https://docs.manim.community/en/stable/contributing/docs.html)
  - [Building the documentation](https://docs.manim.community/en/stable/contributing/docs.html#building-the-documentation)
  - [Sphinx library and extensions](https://docs.manim.community/en/stable/contributing/docs.html#sphinx-library-and-extensions)
  - [Sphinx theme](https://docs.manim.community/en/stable/contributing/docs.html#sphinx-theme)
  - [Custom Sphinx directives](https://docs.manim.community/en/stable/contributing/docs.html#custom-sphinx-directives)
  - [Index](https://docs.manim.community/en/stable/contributing/docs.html#index)
    - [Adding Admonitions](https://docs.manim.community/en/stable/contributing/docs/admonitions.html)
    - [Adding Docstrings](https://docs.manim.community/en/stable/contributing/docs/docstrings.html)
    - [Adding Examples](https://docs.manim.community/en/stable/contributing/docs/examples.html)
    - [Adding References](https://docs.manim.community/en/stable/contributing/docs/references.html)
    - [Typing Conventions](https://docs.manim.community/en/stable/contributing/docs/typings.html)
    - [Choosing Type Hints](https://docs.manim.community/en/stable/contributing/docs/types.html)
- [Adding Tests](https://docs.manim.community/en/stable/contributing/testing.html)
  - [How Manim tests](https://docs.manim.community/en/stable/contributing/testing.html#how-manim-tests)
    - [How it Works](https://docs.manim.community/en/stable/contributing/testing.html#how-it-works)
  - [Architecture](https://docs.manim.community/en/stable/contributing/testing.html#architecture)
  - [The Main Directories](https://docs.manim.community/en/stable/contributing/testing.html#the-main-directories)
  - [Adding a New Test](https://docs.manim.community/en/stable/contributing/testing.html#adding-a-new-test)
    - [Unit Tests](https://docs.manim.community/en/stable/contributing/testing.html#unit-tests)
    - [Graphical Unit Test](https://docs.manim.community/en/stable/contributing/testing.html#graphical-unit-test)
    - [Videos tests](https://docs.manim.community/en/stable/contributing/testing.html#videos-tests)
- [Improving performance](https://docs.manim.community/en/stable/contributing/performance.html)
  - [Profiling](https://docs.manim.community/en/stable/contributing/performance.html#profiling)
    - [Running an animation as a script](https://docs.manim.community/en/stable/contributing/performance.html#running-an-animation-as-a-script)
    - [An example: profiling with cProfile and SnakeViz](https://docs.manim.community/en/stable/contributing/performance.html#an-example-profiling-with-cprofile-and-snakeviz)
- [Internationalization](https://docs.manim.community/en/stable/contributing/internationalization.html)
  - [Signing up](https://docs.manim.community/en/stable/contributing/internationalization.html#signing-up)
  - [Contributing](https://docs.manim.community/en/stable/contributing/internationalization.html#contributing)
    - [Voting](https://docs.manim.community/en/stable/contributing/internationalization.html#voting)
    - [Translations](https://docs.manim.community/en/stable/contributing/internationalization.html#translations)
  - [Translation guidelines](https://docs.manim.community/en/stable/contributing/internationalization.html#translation-guidelines)
  - [Proofreading](https://docs.manim.community/en/stable/contributing/internationalization.html#proofreading)
  - [Errors](https://docs.manim.community/en/stable/contributing/internationalization.html#errors)
    - [Source errors](https://docs.manim.community/en/stable/contributing/internationalization.html#source-errors)