# v0.9.0 [¶](https://docs.manim.community/en/stable/changelog/0.9.0-changelog.html\#v0-9-0 "Link to this heading")

Date:

August 02, 2021

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.9.0-changelog.html\#contributors "Link to this heading")

A total of 35 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Alex Lembcke

- Benjamin Hackl

- Darylgolden

- Devin Neal

- Harivinay +

- Hugues Devimeux

- Jared Hughes +

- Jason Villanueva

- Kadatatlu Kishore +

- KingWampy

- LED Me Explain +

- Laith Bahodi

- Mohammad Al-Fetyani

- Noam Zaks

- Oliver

- PaulCMurdoch

- Raghav Prabhakar +

- Ryan McCauley

- Suhail Sherif +

- Taektiek +

- Udeshya Dhungana +

- UraniumCronorum +

- Vinh H. Pham (Vincent) +

- ccn +

- icedcoffeeee +

- sahilmakhijani +

- sparshg


The patches included in this release have been reviewed by
the following contributors.

- Abhijith Muthyala

- Alex Lembcke

- Benjamin Hackl

- Darylgolden

- Devin Neal

- Harivinay

- Hugues Devimeux

- Jan-Hendrik Müller

- Jason Villanueva

- KingWampy

- Laith Bahodi

- Lino

- Mohammad Al-Fetyani

- Oliver

- Raghav Goel

- Suhail Sherif

- icedcoffeeee

- sahilmakhijani

- sparshg


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.9.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 55 pull requests were merged for this release.

### Highlights [¶](https://docs.manim.community/en/stable/changelog/0.9.0-changelog.html\#highlights "Link to this heading")

- [#1677](https://github.com/ManimCommunity/manim/pull/1677): Added a new [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") mobject

This brings easy-to-use and customizable tables to Manim. Several examples for this new mobject can be found at [`the module documentation page`](https://docs.manim.community/en/stable/reference/manim.mobject.table.html#module-manim.mobject.table "manim.mobject.table") and its subpages.


### Deprecated classes and functions [¶](https://docs.manim.community/en/stable/changelog/0.9.0-changelog.html\#deprecated-classes-and-functions "Link to this heading")

- [#1848](https://github.com/ManimCommunity/manim/pull/1848): Deprecated parameters for [`DashedLine`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DashedLine.html#manim.mobject.geometry.line.DashedLine "manim.mobject.geometry.line.DashedLine") and [`DashedVMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.DashedVMobject.html#manim.mobject.types.vectorized_mobject.DashedVMobject "manim.mobject.types.vectorized_mobject.DashedVMobject")

- `dash_spacing` is an unused parameter

- `positive_space_ratio` has been replaced with the shorter name `dashed_ratio`


- [#1773](https://github.com/ManimCommunity/manim/pull/1773): Remove all classes and functions that were deprecated until `v0.7.0` and `v0.8.0`

The classes `FadeInFrom`, `FadeOutAndShift`, `FadeOutToPoint`, `FadeInFromPoint`, `FadeInFromLarge`, `VFadeIn`, `VFadeOut`, `VFadeInThenOut` have been removed, use [`FadeIn`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeIn.html#manim.animation.fading.FadeIn "manim.animation.fading.FadeIn") or [`FadeOut`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html#manim.animation.fading.FadeOut "manim.animation.fading.FadeOut") with appropriate
keyword arguments instead.



The classes `CircleIndicate`, `ShowCreationThenDestruction`, `AnimationOnSurroundingRectangle`, `ShowPassingFlashAround`, `ShowCreationThenDestructionAround`, `ShowCreationThenFadeAround`, `WiggleOutThenIn`, `TurnInsideOut` have been removed. Use [`Circumscribe`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html#manim.animation.indication.Circumscribe "manim.animation.indication.Circumscribe"), [`ShowPassingFlash`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash "manim.animation.indication.ShowPassingFlash"), or [`Wiggle`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Wiggle.html#manim.animation.indication.Wiggle "manim.animation.indication.Wiggle") instead.



The classes `OpenGLTexMobject` and `OpenGLTextMobject` have been removed, use [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") and [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") instead. Also, `VMobjectFromSVGPathstring` has been removed, use `SVGPathMobject` instead.



Finally, the utility functions `get_norm` and `cross` have been removed (use the corresponding Numpy methods instead), and the function `angle_between` has been replaced with `angle_between_vectors`.

- [#1731](https://github.com/ManimCommunity/manim/pull/1731): Deprecated `ParametricSurface` parameters

- `u_min` and `u_max` have been replaced by `u_range`.

- `v_min` and `v_max` have been replaced by `v_range`.


### New features [¶](https://docs.manim.community/en/stable/changelog/0.9.0-changelog.html\#new-features "Link to this heading")

- [#1780](https://github.com/ManimCommunity/manim/pull/1780): Allow non-numerical values to be added to [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine") and [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes")

- Added [`NumberLine.add_labels()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine.add_labels "manim.mobject.graphing.number_line.NumberLine.add_labels") method to [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine") which accepts a dictionary of positions/values.

- [`CoordinateSystem.add_coordinates()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.add_coordinates "manim.mobject.graphing.coordinate_systems.CoordinateSystem.add_coordinates") now accepts a dictionary too.


- [#1719](https://github.com/ManimCommunity/manim/pull/1719): Added a [`Broadcast`](https://docs.manim.community/en/stable/reference/manim.animation.specialized.Broadcast.html#manim.animation.specialized.Broadcast "manim.animation.specialized.Broadcast") animation

- [#1765](https://github.com/ManimCommunity/manim/pull/1765): Added a static method [`Circle.from_three_points()`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle.from_three_points "manim.mobject.geometry.arc.Circle.from_three_points") for defining a circle from three points

- Added a new [`perpendicular_bisector()`](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.perpendicular_bisector "manim.utils.space_ops.perpendicular_bisector") function in `space_ops.py`


- [#1686](https://github.com/ManimCommunity/manim/pull/1686): Added `ParametricSurface.set_fill_by_value()`

This method enables a color gradient to be applied to a `ParametricSurface`, including the ability to define at which points the colors should be centered.


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.9.0-changelog.html\#enhancements "Link to this heading")

- [#1833](https://github.com/ManimCommunity/manim/pull/1833): Added OpenGL compatibility for [`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict"), `get_line_graph()` and [`FocusOn`](https://docs.manim.community/en/stable/reference/manim.animation.indication.FocusOn.html#manim.animation.indication.FocusOn "manim.animation.indication.FocusOn")

- [#1760](https://github.com/ManimCommunity/manim/pull/1760): Added `window_size` flag to manually adjust the size of the OpenGL window

Accepts a tuple in the form: `x,y`.

- [#1823](https://github.com/ManimCommunity/manim/pull/1823): Reworked [`DashedVMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.DashedVMobject.html#manim.mobject.types.vectorized_mobject.DashedVMobject "manim.mobject.types.vectorized_mobject.DashedVMobject")

Rewritten the logic to generate dashes

- [#1808](https://github.com/ManimCommunity/manim/pull/1808): OpenGL renderer updates

- Adds model matrices to all OpenGLVMobjects

- Improved performance on vectorized mobject shaders

- Added updaters that are part of the scene rather than a mobject


- [#1787](https://github.com/ManimCommunity/manim/pull/1787): Made [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") apply color to the ellipsis

Made color apply to the dots when show\_ellipsis is set to true in DecimalNumber

- [#1775](https://github.com/ManimCommunity/manim/pull/1775): Let [`Create`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create") work on `OpenGLSurface`

- [#1757](https://github.com/ManimCommunity/manim/pull/1757): Added warning when there is a large number of items to hash.

- [#1774](https://github.com/ManimCommunity/manim/pull/1774): Add the `reverse` parameter to [`Write`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Write.html#manim.animation.creation.Write "manim.animation.creation.Write")


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.9.0-changelog.html\#fixed-bugs "Link to this heading")

- [#1722](https://github.com/ManimCommunity/manim/pull/1722): Fixed `remover=True` for [`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

- [#1727](https://github.com/ManimCommunity/manim/pull/1727): Fixed some hot reload issues and compatibility with IDEs

- Fixed interactive embed issue where it would fail when running on non-tty terminals

- Fixed issue where file observer would error after the second run as the first observer was not closed


- [#1844](https://github.com/ManimCommunity/manim/pull/1844): Fixed the oversized [`Code`](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code "manim.mobject.text.code_mobject.Code") window with the OpenGL renderer

- [#1821](https://github.com/ManimCommunity/manim/pull/1821): Fixed issues concerning `frame_center` in [`ThreeDScene`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene "manim.scene.three_d_scene.ThreeDScene")

- Changing `frame_center` in a [`ThreeDScene`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene "manim.scene.three_d_scene.ThreeDScene") now actually changes the camera position.

- An animation with only `frame_center` animated will now be rendered properly.

- A black dot is not created at the origin once `frame_center` is animated.


- [#1826](https://github.com/ManimCommunity/manim/pull/1826): Fixed scaling issue with [`BarChart.change_bar_values()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.probability.BarChart.html#manim.mobject.graphing.probability.BarChart.change_bar_values "manim.mobject.graphing.probability.BarChart.change_bar_values")

- [#1839](https://github.com/ManimCommunity/manim/pull/1839): Allow passing arguments to `.animate` with the OpenGL renderer

- [#1791](https://github.com/ManimCommunity/manim/pull/1791): [`set_z_index()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_z_index "manim.mobject.mobject.Mobject.set_z_index") now sets all submobjects’ `z_index` value

- [#1792](https://github.com/ManimCommunity/manim/pull/1792): Fixed bug that caused dry runs to fail when using the PNG format

- [#1790](https://github.com/ManimCommunity/manim/pull/1790): Fixed an import from `manimlib`

- [#1782](https://github.com/ManimCommunity/manim/pull/1782): Fixed [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") not working properly with the OpenGL renderer

- [#1783](https://github.com/ManimCommunity/manim/pull/1783): Fixed `shuffle()` function and added [`invert()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.invert "manim.mobject.mobject.Mobject.invert") to OpenGL

- [#1786](https://github.com/ManimCommunity/manim/pull/1786): Fixed [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") not working properly when the number of digits changes

- [#1763](https://github.com/ManimCommunity/manim/pull/1763): Fixed not being able to set some CLI flags in the configuration file

- [#1776](https://github.com/ManimCommunity/manim/pull/1776): [`CoordinateSystem.get_riemann_rectangles()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_riemann_rectangles "manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_riemann_rectangles") now uses the graph’s range instead of the axes range

If no range specified, get\_riemann\_rectangles generates the rectangles only where the area is correctly bounded

- [#1770](https://github.com/ManimCommunity/manim/pull/1770): Rewrote `OpenGLMobject.put_start_and_end_on()` to work correctly in 3D

- [#1736](https://github.com/ManimCommunity/manim/pull/1736): Fixed [`LinearTransformationScene`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene "manim.scene.vector_space_scene.LinearTransformationScene") crashing on multiple animations


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.9.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#1852](https://github.com/ManimCommunity/manim/pull/1852): Fixed docs for `Coordinate_system.add_coordinates()` and moved :class: ~.Code example

- [#1807](https://github.com/ManimCommunity/manim/pull/1807): Updated installation instructions

- Added a warning about the incompatibility of different versions of Manim in the README

- Modified the admonition warning in the documentation

- Removed duplicated information from the README ( `pip install manim` is already covered in the docs)


- [#1739](https://github.com/ManimCommunity/manim/pull/1739): Added a section on creating a custom animation to the “Manim’s building blocks” tutorial

- [#1835](https://github.com/ManimCommunity/manim/pull/1835): Updated documentation with information about reworked graphical unit test system

- [#1845](https://github.com/ManimCommunity/manim/pull/1845): Improve `ThreeDSurfacePlot` example in example gallery

- [#1842](https://github.com/ManimCommunity/manim/pull/1842): Removed instructions on installing Poetry from Developer Installation documentation, reference Poetry’s documentation instead

- [#1829](https://github.com/ManimCommunity/manim/pull/1829): Switch the order of Scoop and Chocolatey in the docs for the Windows Installation

- [#1827](https://github.com/ManimCommunity/manim/pull/1827): Added `robots.txt` to prevent old versions of documentation from showing in search results

- [#1819](https://github.com/ManimCommunity/manim/pull/1819): Removed mention of `-h` CLI flag from documentation

- [#1813](https://github.com/ManimCommunity/manim/pull/1813): Removed unused variables from tutorial

- [#1815](https://github.com/ManimCommunity/manim/pull/1815): Added codespell to the list of used linters in the contribution guidelines

- [#1778](https://github.com/ManimCommunity/manim/pull/1778): Improve sidebar structure of the documentation’s reference manual

- [#1749](https://github.com/ManimCommunity/manim/pull/1749): Added documentation and example for [`VMobject.set_fill()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.set_fill "manim.mobject.types.vectorized_mobject.VMobject.set_fill")

- [#1743](https://github.com/ManimCommunity/manim/pull/1743): Edited the developer installation instructions to include information on cloning the repository

- [#1706](https://github.com/ManimCommunity/manim/pull/1706): Rework example for [`Variable`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Variable.html#manim.mobject.text.numbers.Variable "manim.mobject.text.numbers.Variable")


### Changes concerning the testing system [¶](https://docs.manim.community/en/stable/changelog/0.9.0-changelog.html\#changes-concerning-the-testing-system "Link to this heading")

- [#1836](https://github.com/ManimCommunity/manim/pull/1836): Converted all the graphical tests to the new syntax

- [#1802](https://github.com/ManimCommunity/manim/pull/1802): Refactored graphical unit testing system, and implemented multi frames tests

This PR introduces a new `@frames_comparison` decorator which allows writing simple `construct`-like functions as tests. Control data for new tests can be easily generated by calling `pytest --set_test`.


### Changes to our development infrastructure [¶](https://docs.manim.community/en/stable/changelog/0.9.0-changelog.html\#changes-to-our-development-infrastructure "Link to this heading")

- [#1830](https://github.com/ManimCommunity/manim/pull/1830): Be more concise about the documentation URL in the PR template


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.9.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#1851](https://github.com/ManimCommunity/manim/pull/1851): Renamed `Tabular` to [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

- [#1817](https://github.com/ManimCommunity/manim/pull/1817): Remove pillow version requirement

- [#1806](https://github.com/ManimCommunity/manim/pull/1806): Fixed spelling mistake

- [#1745](https://github.com/ManimCommunity/manim/pull/1745): Updated the BibTeX template in the README to Manim v0.9.0


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.9.0-changelog.html\#new-releases "Link to this heading")

- [#1850](https://github.com/ManimCommunity/manim/pull/1850): Bump version number to `v0.9.0` and generate changelog