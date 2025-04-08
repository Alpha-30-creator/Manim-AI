# v0.14.0 [¶](https://docs.manim.community/en/stable/changelog/0.14.0-changelog.html\#v0-14-0 "Link to this heading")

Date:

January 07, 2022

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.14.0-changelog.html\#contributors "Link to this heading")

A total of 29 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Benjamin Hackl

- BorisTheBrave +

- Darylgolden

- GameDungeon

- Gergely Bencsik +

- Jan-Hendrik Müller

- Jihoon +

- Kian Kasad +

- Kiran-Raj-Dev +

- Laith Bahodi

- Leo Xu +

- Marcin Serwin

- Matt Gleich +

- Naveen M K

- Steven nguyen +

- Vectozavr +

- Viicos

- citrusmunch

- netwizard22 +


The patches included in this release have been reviewed by
the following contributors.

- Benjamin Hackl

- BorisTheBrave

- Christopher Besch

- Darylgolden

- GameDungeon

- Gergely Bencsik

- Hugues Devimeux

- Jan-Hendrik Müller

- Kiran-Raj-Dev

- Laith Bahodi

- Leo Xu

- Lucas Ricci

- Marcin Serwin

- Naveen M K

- Raghav Goel

- Ryan McCauley

- Viicos

- icedcoffeeee


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.14.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 29 pull requests were merged for this release.

### Deprecated classes and functions [¶](https://docs.manim.community/en/stable/changelog/0.14.0-changelog.html\#deprecated-classes-and-functions "Link to this heading")

- [#2390](https://github.com/ManimCommunity/manim/pull/2390): Removed deprecations up to v0.13.0

- Removed `get_graph`, `get_implicit_curve`, `get_derivative_graph`, `get_line_graph` and `get_parametric_curve` in favour of their `plot` variants

- Removed `FullScreenFadeRectangle` and `PictureInPictureFrame`

- Removed `path_arc` parameter from [`SpinInFromNothing`](https://docs.manim.community/en/stable/reference/manim.animation.growing.SpinInFromNothing.html#manim.animation.growing.SpinInFromNothing "manim.animation.growing.SpinInFromNothing")

- Removed `set_submobjects` method from `opengl_mobject.py`


### New features [¶](https://docs.manim.community/en/stable/changelog/0.14.0-changelog.html\#new-features "Link to this heading")

- [#2341](https://github.com/ManimCommunity/manim/pull/2341): Update [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") to use new `ManimPango` color setting

- [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") class now uses color setting introduced in `ManimPango 0.4.0` for color and gradient.


- [#2397](https://github.com/ManimCommunity/manim/pull/2397): Added `label_constructor` parameter for [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")

Allows changing the class that will be used to construct [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes") and [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine") labels by default. Makes it possible to easily use [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") for labels if needed.


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.14.0-changelog.html\#enhancements "Link to this heading")

- [#2383](https://github.com/ManimCommunity/manim/pull/2383): Made [`Surface.set_fill_by_value()`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface.set_fill_by_value "manim.mobject.three_d.three_dimensions.Surface.set_fill_by_value") support gradients along different axes

- [#2388](https://github.com/ManimCommunity/manim/pull/2388): Added `about_point` keyword argument to [`ApplyMatrix`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html#manim.animation.transform.ApplyMatrix "manim.animation.transform.ApplyMatrix")

- [#2395](https://github.com/ManimCommunity/manim/pull/2395): Add documentation for paths functions

- [#2372](https://github.com/ManimCommunity/manim/pull/2372): Improved [`DashedVMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.DashedVMobject.html#manim.mobject.types.vectorized_mobject.DashedVMobject "manim.mobject.types.vectorized_mobject.DashedVMobject")

[`DashedVMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.DashedVMobject.html#manim.mobject.types.vectorized_mobject.DashedVMobject "manim.mobject.types.vectorized_mobject.DashedVMobject") used to create stretched and uneven dashes on most plotted curves. Now the dash lengths are equalized. An option is reserved to use the old method.
New keyword argument: `dash_offset`. This parameter shifts the starting point.


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.14.0-changelog.html\#fixed-bugs "Link to this heading")

- [#2409](https://github.com/ManimCommunity/manim/pull/2409): Fixed performance degradation by trimming empty curves from paths when calling [`VMobject.align_points()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.align_points "manim.mobject.types.vectorized_mobject.VMobject.align_points")

- [#2392](https://github.com/ManimCommunity/manim/pull/2392): Fixed `ZeroDivisionError` in `three_dimensions`

- [#2362](https://github.com/ManimCommunity/manim/pull/2362): Fixed phi updater in [`ThreeDScene.begin_3dillusion_camera_rotation()`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.begin_3dillusion_camera_rotation "manim.scene.three_d_scene.ThreeDScene.begin_3dillusion_camera_rotation")


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.14.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#2415](https://github.com/ManimCommunity/manim/pull/2415): Removed instructions on using and installing Docker in README

- [#2414](https://github.com/ManimCommunity/manim/pull/2414): Made improvements to the [Configuration](https://docs.manim.community/en/stable/guides/configuration.html) tutorial

- [#2423](https://github.com/ManimCommunity/manim/pull/2423): Changed recommendation to `mactex-no-gui` from `mactex` for macOS install

- [#2407](https://github.com/ManimCommunity/manim/pull/2407): Clarified docstrings of [`Mobject.animate()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.animate "manim.mobject.mobject.Mobject.animate"), [`Mobject.set()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set "manim.mobject.mobject.Mobject.set") and [`Variable`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Variable.html#manim.mobject.text.numbers.Variable "manim.mobject.text.numbers.Variable")

- [#2352](https://github.com/ManimCommunity/manim/pull/2352): Added Crowdin badge

- [#2371](https://github.com/ManimCommunity/manim/pull/2371): Added `dvips` to list of required LaTeX packages on Linux

- [#2403](https://github.com/ManimCommunity/manim/pull/2403): Improved docstring of [`ApplyMethod`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod") and removed propagated `__init__` docstring

- [#2391](https://github.com/ManimCommunity/manim/pull/2391): Fixed typo in parameter name in documentation of [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")

- [#2368](https://github.com/ManimCommunity/manim/pull/2368): Added note in Internationalization


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.14.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#2408](https://github.com/ManimCommunity/manim/pull/2408): Removed various return annotations that were stifling type inference

- [#2424](https://github.com/ManimCommunity/manim/pull/2424): Removed `strings.py`

- [#1972](https://github.com/ManimCommunity/manim/pull/1972): Added support for MyPy

- [#2410](https://github.com/ManimCommunity/manim/pull/2410): Fixed Flake8

- [#2401](https://github.com/ManimCommunity/manim/pull/2401): Fixed type annotations in `mobject.three_dimensions`

- [#2405](https://github.com/ManimCommunity/manim/pull/2405): Removed some unused OpenGL files

- [#2399](https://github.com/ManimCommunity/manim/pull/2399): Fixed type annotations in [`table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.html#module-manim.mobject.table "manim.mobject.table")

- [#2385](https://github.com/ManimCommunity/manim/pull/2385): Made comments in quickstart tutorial more precise

- [#2377](https://github.com/ManimCommunity/manim/pull/2377): Fixed type hint for an argument of [`MoveAlongPath`](https://docs.manim.community/en/stable/reference/manim.animation.movement.MoveAlongPath.html#manim.animation.movement.MoveAlongPath "manim.animation.movement.MoveAlongPath")


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.14.0-changelog.html\#new-releases "Link to this heading")

- [#2411](https://github.com/ManimCommunity/manim/pull/2411): Prepare new release, `v0.14.0`