ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# v0.13.0 [¶](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html\#v0-13-0 "Link to this heading")

Date:

December 04, 2021

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html\#contributors "Link to this heading")

A total of 27 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Alex Lembcke

- Benjamin Hackl

- Christopher Besch

- Darylgolden

- Filip +

- John Ingles +

- Laith Bahodi

- Lucas Ricci +

- Marcin Serwin +

- Mysaa

- Naveen M K

- Ricky +

- Viicos

- ask09ok +

- citrusmunch +

- icedcoffeeee

- mostlyaman +

- vmiezys +

- zhujisheng +


The patches included in this release have been reviewed by
the following contributors.

- Alex Lembcke

- Benjamin Hackl

- Christopher Besch

- Darylgolden

- Filip

- Hugues Devimeux

- Jan-Hendrik Müller

- Laith Bahodi

- Lucas Ricci

- Naveen M K

- Oliver

- Ryan McCauley

- Viicos

- ask09ok

- icedcoffeeee

- mostlyaman


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 39 pull requests were merged for this release.

### Highlights [¶](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html\#highlights "Link to this heading")

- [#2313](https://github.com/ManimCommunity/manim/pull/2313): Finalized translation process and documentation


### Deprecated classes and functions [¶](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html\#deprecated-classes-and-functions "Link to this heading")

- [#2331](https://github.com/ManimCommunity/manim/pull/2331): Removed deprecations up to `v0.12.0`

- Removed `distance` parameters from [`ThreeDCamera`](https://docs.manim.community/en/stable/reference/manim.camera.three_d_camera.ThreeDCamera.html#manim.camera.three_d_camera.ThreeDCamera "manim.camera.three_d_camera.ThreeDCamera") (replacement: `focal_distance`)

- Removed `min_distance_to_new_point` parameter from [`TracedPath`](https://docs.manim.community/en/stable/reference/manim.animation.changing.TracedPath.html#manim.animation.changing.TracedPath "manim.animation.changing.TracedPath")

- Removed `positive_space_ratio` and `dash_spacing` parameters from [`DashedVMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.DashedVMobject.html#manim.mobject.types.vectorized_mobject.DashedVMobject "manim.mobject.types.vectorized_mobject.DashedVMobject")

- Removed `<method>_in_place` methods from [`mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html#module-manim.mobject.mobject "manim.mobject.mobject")

- Removed `ReconfigurableScene`

- Removed `SampleSpaceScene`


- [#2312](https://github.com/ManimCommunity/manim/pull/2312): Replaced all occurrences of `set_submobjects`


### New features [¶](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html\#new-features "Link to this heading")

- [#2314](https://github.com/ManimCommunity/manim/pull/2314): Added basic support for adding subcaptions via [`Scene.add_subcaption()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_subcaption "manim.scene.scene.Scene.add_subcaption")

- New method [`Scene.add_subcaption()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_subcaption "manim.scene.scene.Scene.add_subcaption")

- New keyword arguments `subcaption`, `subcaption_duration`, `subcaption_offset` for [`Scene.play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play")


- [#2267](https://github.com/ManimCommunity/manim/pull/2267): Implemented [`CoordinateSystem.plot_antiderivative_graph()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_antiderivative_graph "manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_antiderivative_graph")


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html\#enhancements "Link to this heading")

- [#2347](https://github.com/ManimCommunity/manim/pull/2347): Moved `manim_directive.py` to `manim.utils.docbuild`

- [#2340](https://github.com/ManimCommunity/manim/pull/2340): Added documentation for [`animation.growing`](https://docs.manim.community/en/stable/reference/manim.animation.growing.html#module-manim.animation.growing "manim.animation.growing") and improved [`SpinInFromNothing`](https://docs.manim.community/en/stable/reference/manim.animation.growing.SpinInFromNothing.html#manim.animation.growing.SpinInFromNothing "manim.animation.growing.SpinInFromNothing")

- [#2343](https://github.com/ManimCommunity/manim/pull/2343): Replaced current tree layout algorithm with SageMath’s for improved layout of large trees

- [#2351](https://github.com/ManimCommunity/manim/pull/2351): Added missing `**kwargs` parameter to [`Table.add_highlighted_cell()`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.add_highlighted_cell "manim.mobject.table.Table.add_highlighted_cell")

- [#2344](https://github.com/ManimCommunity/manim/pull/2344): Resized SVG logos, fit content to canvas


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html\#fixed-bugs "Link to this heading")

- [#2359](https://github.com/ManimCommunity/manim/pull/2359): Resolved `ValueError` when calling `manim cfg write`

- [#2276](https://github.com/ManimCommunity/manim/pull/2276): Fixed bug with alignment of z-axis in [`ThreeDAxes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ThreeDAxes.html#manim.mobject.graphing.coordinate_systems.ThreeDAxes "manim.mobject.graphing.coordinate_systems.ThreeDAxes")

- [#2325](https://github.com/ManimCommunity/manim/pull/2325): Several improvements to handling of `quality` argument

- [#2335](https://github.com/ManimCommunity/manim/pull/2335): Fixed bug with zooming camera and `PointCloud`

- [#2328](https://github.com/ManimCommunity/manim/pull/2328): Fixed bug causing incorrect RGBA values to be passed to cairo

- [#2292](https://github.com/ManimCommunity/manim/pull/2292): Fixed positioning of [`Flash`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Flash.html#manim.animation.indication.Flash "manim.animation.indication.Flash")

- [#2262](https://github.com/ManimCommunity/manim/pull/2262): Fixed wrong cell coordinates with [`Table.get_cell()`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_cell "manim.mobject.table.Table.get_cell") after scaling

- [#2280](https://github.com/ManimCommunity/manim/pull/2280): Fixed [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") color when number of displayed digits changes


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#2354](https://github.com/ManimCommunity/manim/pull/2354): Port over docs and typings from `mobject.py` and `vectorized_mobject.py` to their OpenGL counterparts

- [#2350](https://github.com/ManimCommunity/manim/pull/2350): Added mention of Manim sideview extension for VS Code

- [#2342](https://github.com/ManimCommunity/manim/pull/2342): Removed `get_graph()` usage from [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes") example

- [#2216](https://github.com/ManimCommunity/manim/pull/2216): Edited and added new sections to the quickstart tutorial

- [#2279](https://github.com/ManimCommunity/manim/pull/2279): Added documentation for discontinuous functions

- [#2319](https://github.com/ManimCommunity/manim/pull/2319): Swapped `dotL` and `dotR` in [`Mobject.interpolate()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.interpolate "manim.mobject.mobject.Mobject.interpolate") example

- [#2230](https://github.com/ManimCommunity/manim/pull/2230): Copyedited building blocks tutorial

- [#2310](https://github.com/ManimCommunity/manim/pull/2310): Clarified that Manim does not support Python 3.10 yet in the documentation

- [#2294](https://github.com/ManimCommunity/manim/pull/2294): Made documentation front page more concise and rearranged order of tutorials

- [#2287](https://github.com/ManimCommunity/manim/pull/2287): Replace link to old interactive notebook


### Changes concerning the testing system [¶](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html\#changes-concerning-the-testing-system "Link to this heading")

- [#2346](https://github.com/ManimCommunity/manim/pull/2346): Made `frames_comparsion` decorator for frame testing a proper module of the library

- [#2318](https://github.com/ManimCommunity/manim/pull/2318): Added tests for `remover` keyword argument of [`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

- [#2301](https://github.com/ManimCommunity/manim/pull/2301): Added a test for [`ThreeDScene.add_fixed_in_frame_mobjects()`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects "manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects")

- [#2274](https://github.com/ManimCommunity/manim/pull/2274): Optimized some tests to reduce duration

- [#2272](https://github.com/ManimCommunity/manim/pull/2272): Added test for [`Broadcast`](https://docs.manim.community/en/stable/reference/manim.animation.specialized.Broadcast.html#manim.animation.specialized.Broadcast "manim.animation.specialized.Broadcast")


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#2327](https://github.com/ManimCommunity/manim/pull/2327): Corrected type hint for `labels` keyword argument of [`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph")

- [#2329](https://github.com/ManimCommunity/manim/pull/2329): Remove unintended line break in README

- [#2305](https://github.com/ManimCommunity/manim/pull/2305): Corrected type hint `discontinuities` argument for [`ParametricFunction`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ParametricFunction.html#manim.mobject.graphing.functions.ParametricFunction "manim.mobject.graphing.functions.ParametricFunction")

- [#2300](https://github.com/ManimCommunity/manim/pull/2300): Add contact email for PyPi


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html\#new-releases "Link to this heading")

- [#2353](https://github.com/ManimCommunity/manim/pull/2353): Prepare new release: `v0.13.0`


### Unclassified changes [¶](https://docs.manim.community/en/stable/changelog/0.13.0-changelog.html\#unclassified-changes "Link to this heading")

- [#2348](https://github.com/ManimCommunity/manim/pull/2348): Updated translation source files