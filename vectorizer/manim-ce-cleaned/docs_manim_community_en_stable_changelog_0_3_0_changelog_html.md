# v0.3.0 [¶](https://docs.manim.community/en/stable/changelog/0.3.0-changelog.html\#v0-3-0 "Link to this heading")

Date:

February 1, 2021

The changes since Manim Community release v0.2.0 are listed below.

## New Features [¶](https://docs.manim.community/en/stable/changelog/0.3.0-changelog.html\#new-features "Link to this heading")

- [#945](https://github.com/ManimCommunity/manim/pull/945): `change_layout()` method for [`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph") mobject

- [#943](https://github.com/ManimCommunity/manim/pull/943): IPython %%manim magic

- [#970](https://github.com/ManimCommunity/manim/pull/970): Added `--version` command line flag

- [#948](https://github.com/ManimCommunity/manim/pull/948): Allow passing a code string to [`Code`](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code "manim.mobject.text.code_mobject.Code")

- [#917](https://github.com/ManimCommunity/manim/pull/917): Allow overriding new-style method animations

- [#756](https://github.com/ManimCommunity/manim/pull/756): Allow setting frame\_height and frame\_width via config file

- [#939](https://github.com/ManimCommunity/manim/pull/939): Added custom font files support

- [#892](https://github.com/ManimCommunity/manim/pull/892): Added ManimCommunity colors

- [#922](https://github.com/ManimCommunity/manim/pull/922): Tree layout for Graph mobject

- [#935](https://github.com/ManimCommunity/manim/pull/935): Added code of conduct

- [#916](https://github.com/ManimCommunity/manim/pull/916): Multi-column layout for partite graphs

- [#742](https://github.com/ManimCommunity/manim/pull/742): Units: Pixels, Munits, Percent in `unit`

- [#893](https://github.com/ManimCommunity/manim/pull/893): Convenience method `from_networkx()` for creating a graph from a networkx graph


## Bugfixes and Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.3.0-changelog.html\#bugfixes-and-enhancements "Link to this heading")

- [#988](https://github.com/ManimCommunity/manim/pull/988): Fix Windows CI pipeline by adding missing LaTeX package

- [#961](https://github.com/ManimCommunity/manim/pull/961): Added typings and docs for vectorized mobjects and bezier related functions

- [#977](https://github.com/ManimCommunity/manim/pull/977): JupyterLab docker image and documentation for manim and IPython

- [#985](https://github.com/ManimCommunity/manim/pull/985): Fix variable name for webgl renderer

- [#954](https://github.com/ManimCommunity/manim/pull/954): Fix edges lagging behind vertices in animations of graphs

- [#980](https://github.com/ManimCommunity/manim/pull/980): Allow usage of custom Pygments styles in Code

- [#952](https://github.com/ManimCommunity/manim/pull/952): Allow passing tween information to the WebGL frontend

- [#978](https://github.com/ManimCommunity/manim/pull/978): Fix `possible_paths` not printing in `code_mobject`

- [#976](https://github.com/ManimCommunity/manim/pull/976): Update `ManimPango`

- [#967](https://github.com/ManimCommunity/manim/pull/967): Automatically import plugins

- [#971](https://github.com/ManimCommunity/manim/pull/971): Make ManimCommunity look consistent

- [#957](https://github.com/ManimCommunity/manim/pull/957): Raise `NotImplementedError` when trying to chain overridden method animations

- [#947](https://github.com/ManimCommunity/manim/pull/947): Several fixes and improvements for `PointCloundDot`

- [#923](https://github.com/ManimCommunity/manim/pull/923): Documentation: move installation instructions for developers to page for developers

- [#964](https://github.com/ManimCommunity/manim/pull/964): Added unit test for [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")’s unit vector

- [#960](https://github.com/ManimCommunity/manim/pull/960): Magnitude of [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")’s unit vector should be `unit_size`, not 1

- [#958](https://github.com/ManimCommunity/manim/pull/958): Fix code formatting in `utils/debug.py`

- [#953](https://github.com/ManimCommunity/manim/pull/953): Update license year

- [#944](https://github.com/ManimCommunity/manim/pull/944): Interpolate stroke opacity in [`FadeIn`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeIn.html#manim.animation.fading.FadeIn "manim.animation.fading.FadeIn") and update `stroke_opacity` and `fill_opacity` in `set_stroke()` and [`set_fill()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.set_fill "manim.mobject.types.vectorized_mobject.VMobject.set_fill")

- [#865](https://github.com/ManimCommunity/manim/pull/865): Rename `get_submobject_index_labels` to `index_labels`

- [#941](https://github.com/ManimCommunity/manim/pull/941): Added keyword arguments `x_min`, `x_max`, `y_min`, `y_max` to [`ThreeDAxes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ThreeDAxes.html#manim.mobject.graphing.coordinate_systems.ThreeDAxes "manim.mobject.graphing.coordinate_systems.ThreeDAxes")

- [#886](https://github.com/ManimCommunity/manim/pull/886): Let the render progress bar show details about the rendered animation again

- [#936](https://github.com/ManimCommunity/manim/pull/936): Fix [`BulletedList`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.BulletedList.html#manim.mobject.text.tex_mobject.BulletedList "manim.mobject.text.tex_mobject.BulletedList") TeX environment problem and add a typing to `get_module`

- [#938](https://github.com/ManimCommunity/manim/pull/938): Remove dependency on progressbar

- [#937](https://github.com/ManimCommunity/manim/pull/937): Change ‘brew cask install’ to ‘brew install –cask’ for CI pipeline

- [#933](https://github.com/ManimCommunity/manim/pull/933): Make matrix work with lists again

- [#932](https://github.com/ManimCommunity/manim/pull/932): Correctly parse `log_dir` option

- [#920](https://github.com/ManimCommunity/manim/pull/920): Raise error if markup in [`MarkupText`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText") is invalid

- [#929](https://github.com/ManimCommunity/manim/pull/929): Raise an error if a [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix") object is created with < 2-dimensional input

- [#907](https://github.com/ManimCommunity/manim/pull/907): Make Scene.add\_sound work again (when running with `--disable_caching`)

- [#906](https://github.com/ManimCommunity/manim/pull/906): Allow new-style method animation to be used in animation groups

- [#908](https://github.com/ManimCommunity/manim/pull/908): Removed deprecated command line arguments from documentation

- [#903](https://github.com/ManimCommunity/manim/pull/903): Tiny grammar improvements

- [#904](https://github.com/ManimCommunity/manim/pull/904): Added blank line between imports and class example

- [#898](https://github.com/ManimCommunity/manim/pull/898): CI: fix publish workflow


[**Document Extraction for Developers** Transform docs into structured data with Sensible. **Try for free →**](https://server.ethicalads.io/proxy/click/8518/019600e2-1cda-79d2-af8c-7a9ad51709e6/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8518/019600e2-1cda-79d2-af8c-7a9ad51709e6/)