ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# v0.10.0 [¶](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html\#v0-10-0 "Link to this heading")

Date:

September 01, 2021

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html\#contributors "Link to this heading")

A total of 40 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Animfysyk +

- Benjamin Hackl

- Christian Clauss

- Daniel Adelodun +

- Darigov Research

- Darylgolden

- Eric Biedert +

- Harivinay

- Jan-Hendrik Müller

- Jephian Lin +

- Joy Bhalla +

- Laith Bahodi

- Lalourche +

- Max Stoumen

- Naveen M K

- Oliver

- Partha Das +

- Raj Dandekar +

- Rohan Sharma +

- Ryan McCauley

- Václav Hlaváč +

- asjadaugust +

- ccn

- icedcoffeeee

- sparshg

- vinnniii15 +

- vladislav doster +

- xia0long +


The patches included in this release have been reviewed by
the following contributors.

- Aathish Sivasubrahmanian

- Benjamin Hackl

- Darylgolden

- Devin Neal

- Eric Biedert

- GameDungeon

- Harivinay

- Hugues Devimeux

- Jan-Hendrik Müller

- Jason Villanueva

- Jephian Lin

- Joy Bhalla

- KingWampy

- Laith Bahodi

- Naveen M K

- Oliver

- Raghav Goel

- Raj Dandekar

- Ryan McCauley

- ccn

- icedcoffeeee

- ralphieraccoon

- sparshg


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 59 pull requests were merged for this release.

### Breaking changes [¶](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html\#breaking-changes "Link to this heading")

- [#1843](https://github.com/ManimCommunity/manim/pull/1843): Dropped redundant OpenGL files and add metaclass support for [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface")

- `OpenGL<x>` classes from `opengl_geometry.py`, `opengl_text_mobject.py`, `opengl_tex_mobject.py`, `opengl_svg_path.py`, `opengl_svg_mobject.py` and most of `opengl_three_dimensions.py` have been removed.

- `ParametricSurface` has been renamed to [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface")


### Deprecated classes and functions [¶](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html\#deprecated-classes-and-functions "Link to this heading")

- [#1941](https://github.com/ManimCommunity/manim/pull/1941): Added examples, tests and improved documentation for [`coordinate_systems`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.html#module-manim.mobject.graphing.coordinate_systems "manim.mobject.graphing.coordinate_systems")

- [#1694](https://github.com/ManimCommunity/manim/pull/1694): Added `font_size` parameter for [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") and [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"), replaced `scale` parameters with `font_size`

- [#1860](https://github.com/ManimCommunity/manim/pull/1860): Removed `GraphScene`, `NumberLineOld` and parameters for [`ChangingDecimal`](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html#manim.animation.numbers.ChangingDecimal "manim.animation.numbers.ChangingDecimal")


### New features [¶](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html\#new-features "Link to this heading")

- [#1929](https://github.com/ManimCommunity/manim/pull/1929): Implementing a `zoom` parameter for [`ThreeDScene.move_camera()`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.move_camera "manim.scene.three_d_scene.ThreeDScene.move_camera")

Zooming into a [`ThreeDScene`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene "manim.scene.three_d_scene.ThreeDScene") can now be done by calling, for example, `self.move_camera(zoom=2)` in the `construct` method.

- [#1980](https://github.com/ManimCommunity/manim/pull/1980): Added a `dissipating_time` keyword argument to [`TracedPath`](https://docs.manim.community/en/stable/reference/manim.animation.changing.TracedPath.html#manim.animation.changing.TracedPath "manim.animation.changing.TracedPath") to allow animating a dissipating path

- [#1899](https://github.com/ManimCommunity/manim/pull/1899): Allow switching the renderer to OpenGL at runtime

Previously, the metaclass approach only changed the inheritance chain to switch between OpenGL and cairo mobjects when the class objects are initialized, i.e., at import time. This PR also triggers the changes to the inheritance chain when the value of `config.renderer` is changed.

- [#1828](https://github.com/ManimCommunity/manim/pull/1828): Added configuration option `zero_pad` for zero padding PNG file names


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html\#enhancements "Link to this heading")

- [#1882](https://github.com/ManimCommunity/manim/pull/1882): Added OpenGL support for [`PMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject "manim.mobject.types.point_cloud_mobject.PMobject") and its subclasses

- [#1881](https://github.com/ManimCommunity/manim/pull/1881): Added methods [`Angle.get_lines()`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle.get_lines "manim.mobject.geometry.line.Angle.get_lines") and [`Angle.get_value()`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle.get_value "manim.mobject.geometry.line.Angle.get_value") to [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle")

- [#1952](https://github.com/ManimCommunity/manim/pull/1952): Added the option to save last frame for OpenGL

- [#1922](https://github.com/ManimCommunity/manim/pull/1922): Fixed IPython interface to exit cleanly when OpenGL renderer raises an error

- [#1923](https://github.com/ManimCommunity/manim/pull/1923): Fixed CLI help text for `manim init` subcommand so that it is not truncated

- [#1868](https://github.com/ManimCommunity/manim/pull/1868): Added OpenGL support to IPython magic

The OpenGL renderer can now be used in jupyter notebooks when using the `%%manim` magic command.

- [#1841](https://github.com/ManimCommunity/manim/pull/1841): Reduced default resolution of [`Dot3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Dot3D.html#manim.mobject.three_d.three_dimensions.Dot3D "manim.mobject.three_d.three_dimensions.Dot3D")

- [#1866](https://github.com/ManimCommunity/manim/pull/1866): Allow passing keyword argument `corner_radius` to [`SurroundingRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html#manim.mobject.geometry.shape_matchers.SurroundingRectangle "manim.mobject.geometry.shape_matchers.SurroundingRectangle")

- [#1847](https://github.com/ManimCommunity/manim/pull/1847): Allow [`Cross`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.Cross.html#manim.mobject.geometry.shape_matchers.Cross "manim.mobject.geometry.shape_matchers.Cross") to be created without requiring a mobject


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html\#fixed-bugs "Link to this heading")

- [#1985](https://github.com/ManimCommunity/manim/pull/1985): Use `height` to determine `font_size` instead of the `_font_size` attribute

- [#1758](https://github.com/ManimCommunity/manim/pull/1758): Fixed scene selection being ignored when using the OpenGL renderer

- [#1871](https://github.com/ManimCommunity/manim/pull/1871): Fixed broken [`VectorScene.vector_to_coords()`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.VectorScene.html#manim.scene.vector_space_scene.VectorScene.vector_to_coords "manim.scene.vector_space_scene.VectorScene.vector_to_coords")

- [#1973](https://github.com/ManimCommunity/manim/pull/1973): Fixed indexing of [`Table.get_entries()`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_entries "manim.mobject.table.Table.get_entries") to respect row length

- [#1950](https://github.com/ManimCommunity/manim/pull/1950): Fixed passing custom arrow shapes to [`CurvedArrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CurvedArrow.html#manim.mobject.geometry.arc.CurvedArrow "manim.mobject.geometry.arc.CurvedArrow")

- [#1967](https://github.com/ManimCommunity/manim/pull/1967): Fixed `Axes.coordinate_labels` referring to the entire axis, not just its labels

- [#1951](https://github.com/ManimCommunity/manim/pull/1951): Fixed `Axes.get_line_graph()` returning a graph rendered below the axes

- [#1943](https://github.com/ManimCommunity/manim/pull/1943): Added `buff` keyword argument to [`BraceLabel`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceLabel.html#manim.mobject.svg.brace.BraceLabel "manim.mobject.svg.brace.BraceLabel")

- [#1938](https://github.com/ManimCommunity/manim/pull/1938): Fixed [`Rotate`](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html#manim.animation.rotation.Rotate "manim.animation.rotation.Rotate") for angles that are multiples of 2π

- [#1924](https://github.com/ManimCommunity/manim/pull/1924): Made arrow tips rotate `IN` and `OUT` properly

- [#1931](https://github.com/ManimCommunity/manim/pull/1931): Fixed `row_heights` in [`Mobject.arrange_in_grid()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange_in_grid "manim.mobject.mobject.Mobject.arrange_in_grid")

- [#1893](https://github.com/ManimCommunity/manim/pull/1893): Fixed CLI error when rendering a file containing a single scene without specifying the scene name

- [#1744](https://github.com/ManimCommunity/manim/pull/1744): Fixed bug in [`NumberPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane") with strictly positive or strictly negative values for `x_range` and `y_range`

- [#1887](https://github.com/ManimCommunity/manim/pull/1887): Fixed `custom_config` not working in `frames_comparison`

- [#1879](https://github.com/ManimCommunity/manim/pull/1879): Fixed how the installed version is determined by Poetry


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#1979](https://github.com/ManimCommunity/manim/pull/1979): Corrected Japanese phrases in documentation

- [#1976](https://github.com/ManimCommunity/manim/pull/1976): Fixed labelling of languages in documentation example

- [#1949](https://github.com/ManimCommunity/manim/pull/1949): Rewrite installation instructions from scratch

- [#1963](https://github.com/ManimCommunity/manim/pull/1963): Added sitemap to `robots.txt`

- [#1939](https://github.com/ManimCommunity/manim/pull/1939): Fixed formatting of parameter description of [`NumberPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane")

- [#1918](https://github.com/ManimCommunity/manim/pull/1918): Fixed a typo in the text tutorial

- [#1915](https://github.com/ManimCommunity/manim/pull/1915): Improved the wording of the installation instructions for Google Colab

- [#1906](https://github.com/ManimCommunity/manim/pull/1906): Improved language and overall consistency in `README`

- [#1880](https://github.com/ManimCommunity/manim/pull/1880): Updated tutorials to use `.animate` instead of [`ApplyMethod`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

- [#1877](https://github.com/ManimCommunity/manim/pull/1877): Remove duplicated imports in some documentation examples

- [#1869](https://github.com/ManimCommunity/manim/pull/1869): Fixed duplicated Parameters section in [`Mobject.arrange_in_grid()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange_in_grid "manim.mobject.mobject.Mobject.arrange_in_grid")


### Changes concerning the testing system [¶](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html\#changes-concerning-the-testing-system "Link to this heading")

- [#1894](https://github.com/ManimCommunity/manim/pull/1894): Fixed an OpenGL test


### Changes to our development infrastructure [¶](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html\#changes-to-our-development-infrastructure "Link to this heading")

- [#1987](https://github.com/ManimCommunity/manim/pull/1987): Added support for using OpenGL in subprocess in Windows pipeline

- [#1964](https://github.com/ManimCommunity/manim/pull/1964): Added `CITATION.cff` and a method to automatically update this citation with new releases

- [#1856](https://github.com/ManimCommunity/manim/pull/1856): Modified Dockerfile to support multi-platform builds via `docker buildx`

- [#1955](https://github.com/ManimCommunity/manim/pull/1955): Partially support OpenGL rendering with Docker

- [#1896](https://github.com/ManimCommunity/manim/pull/1896): Made RTD apt install FFMPEG instead of installing a Python binding

- [#1864](https://github.com/ManimCommunity/manim/pull/1864): Shortened and simplified PR template

- [#1853](https://github.com/ManimCommunity/manim/pull/1853): Updated Sphinx to 4.1.2


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#1960](https://github.com/ManimCommunity/manim/pull/1960): Ignore fewer flake8 errors

- [#1947](https://github.com/ManimCommunity/manim/pull/1947): Set flake8 not to ignore undefined names in Python code

- [#1948](https://github.com/ManimCommunity/manim/pull/1948): flake8: Set max-line-length instead of ignoring long lines

- [#1956](https://github.com/ManimCommunity/manim/pull/1956): Upgrade to modern Python syntax

- This pull request was created [with the command](https://github.com/asottile/pyupgrade#readme) `pyupgrade --py36-plus **/*.py`

- Python f-strings simplify the code and [should speed up execution](https://www.scivision.dev/python-f-string-speed).


- [#1898](https://github.com/ManimCommunity/manim/pull/1898): Replaced `self.data["attr"]` and `self.uniforms["attr"]` with `self.attr`

In particular, `OpenGLVMobject.points` can now be accessed directly.

- [#1934](https://github.com/ManimCommunity/manim/pull/1934): Improved code quality by implementing suggestions from LGTM

- [#1861](https://github.com/ManimCommunity/manim/pull/1861): Updated `dearpygui` version to 0.8.x


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.10.0-changelog.html\#new-releases "Link to this heading")

- [#1989](https://github.com/ManimCommunity/manim/pull/1989): Prepare new release v0.10.0


[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/8270/019600e9-7399-72f3-9593-9b0da36f1fa4/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/devops/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8270/019600e9-7399-72f3-9593-9b0da36f1fa4/)