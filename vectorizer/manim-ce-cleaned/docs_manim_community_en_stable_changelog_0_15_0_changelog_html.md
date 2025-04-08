# v0.15.0 [¶](https://docs.manim.community/en/stable/changelog/0.15.0-changelog.html\#v0-15-0 "Link to this heading")

Date:

February 26, 2022

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.15.0-changelog.html\#contributors "Link to this heading")

A total of 34 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Alex Lembcke

- AnonymoZ +

- Benjamin Hackl

- Darylgolden

- Eshaan Naga Venkata +

- Faruk D. +

- GameDungeon

- Kevin Cen +

- Laith Bahodi

- Leo Xu

- Lucas Ricci

- Marcin Serwin

- Michael McNeil Forbes +

- Mysaa

- Naveen M K

- Pierre Couy +

- Simon Ellmann +

- Tommy Chu +

- Viicos

- ad\_chaos

- betafcc +

- friedkeenan

- icedcoffeeee

- vmoros +

- 鹤翔万里


The patches included in this release have been reviewed by
the following contributors.

- Benjamin Hackl

- Christopher Besch

- Darylgolden

- Eshaan Naga Venkata

- GameDungeon

- Jan-Hendrik Müller

- Laith Bahodi

- Marcin Kurczewski

- Marcin Serwin

- Naveen M K

- Raghav Goel

- RomainJMend

- Ryan McCauley

- Tommy Chu

- ad\_chaos

- betafcc

- icedcoffeeee


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.15.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 71 pull requests were merged for this release.

### Breaking changes [¶](https://docs.manim.community/en/stable/changelog/0.15.0-changelog.html\#breaking-changes "Link to this heading")

- [#2476](https://github.com/ManimCommunity/manim/pull/2476): Improved structure of the [`mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html#module-manim.mobject.mobject "manim.mobject.mobject") module

Arrow tips now have to be imported from `manim.mobject.geometry.tips` instead of `manim.mobject.geometry`.

- [#2387](https://github.com/ManimCommunity/manim/pull/2387): Refactored [`BarChart`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.probability.BarChart.html#manim.mobject.graphing.probability.BarChart "manim.mobject.graphing.probability.BarChart") and made it inherit from [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes")

- [`BarChart`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.probability.BarChart.html#manim.mobject.graphing.probability.BarChart "manim.mobject.graphing.probability.BarChart") now inherits from [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes"), allowing it to use [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes")’ methods. Also improves [`BarChart`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.probability.BarChart.html#manim.mobject.graphing.probability.BarChart "manim.mobject.graphing.probability.BarChart")’s configuration and ease of use.

- Added [`get_bar_labels()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.probability.BarChart.html#manim.mobject.graphing.probability.BarChart.get_bar_labels "manim.mobject.graphing.probability.BarChart.get_bar_labels") to annotate the value of each bar of a [`BarChart`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.probability.BarChart.html#manim.mobject.graphing.probability.BarChart "manim.mobject.graphing.probability.BarChart").


### Deprecated classes and functions [¶](https://docs.manim.community/en/stable/changelog/0.15.0-changelog.html\#deprecated-classes-and-functions "Link to this heading")

- [#2568](https://github.com/ManimCommunity/manim/pull/2568): Removed Deprecated Methods

Removed methods and classes that were deprecated since v0.10.0 and v0.11.0

- [#2457](https://github.com/ManimCommunity/manim/pull/2457): Deprecated `ShowCreationThenFadeOut`


### New features [¶](https://docs.manim.community/en/stable/changelog/0.15.0-changelog.html\#new-features "Link to this heading")

- [#2442](https://github.com/ManimCommunity/manim/pull/2442): Added `media_embed` config option to control whether media in Jupyter notebooks is embedded

- [#2504](https://github.com/ManimCommunity/manim/pull/2504): Added finer control over [`Scene.wait()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait "manim.scene.scene.Scene.wait") being static (i.e., no updaters) or not

- Added keyword argument `frozen_frame` to [`Wait`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait "manim.animation.animation.Wait") and [`Scene.wait()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait "manim.scene.scene.Scene.wait")

- New convenience method: [`Scene.pause()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.pause "manim.scene.scene.Scene.pause") (alias for `Scene.wait(frozen_frame=True)`)

- Changed default behavior for OpenGL updaters: updater functions are now not called by default when they are added

- Changed default behavior of `Scene.should_mobjects_update()`: made it respect the set value of `Wait.frozen_frame`, changed automatic determination of frozen frame state to also consider Scene updaters


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.15.0-changelog.html\#enhancements "Link to this heading")

- [#2478](https://github.com/ManimCommunity/manim/pull/2478): Alternative scaling for tree graph layout

- [#2565](https://github.com/ManimCommunity/manim/pull/2565): Allowed passing vertex configuration keyword arguments to `Graph.add_edges()`

- [#2467](https://github.com/ManimCommunity/manim/pull/2467): [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex"), [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex"), [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") and [`MarkupText`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText") inherit color from their parent mobjects

- [#2537](https://github.com/ManimCommunity/manim/pull/2537): Added support for PySide coordinate system

- [#2158](https://github.com/ManimCommunity/manim/pull/2158): Added OpenGL compatibility to [`ThreeDScene.add_fixed_orientation_mobjects()`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.add_fixed_orientation_mobjects "manim.scene.three_d_scene.ThreeDScene.add_fixed_orientation_mobjects") and [`ThreeDScene.add_fixed_in_frame_mobjects()`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects "manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects")

- [#2535](https://github.com/ManimCommunity/manim/pull/2535): Implemented performance enhancement for [`VMobject.insert_n_curves_to_point_list()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.insert_n_curves_to_point_list "manim.mobject.types.vectorized_mobject.VMobject.insert_n_curves_to_point_list")

- [#2516](https://github.com/ManimCommunity/manim/pull/2516): Cached view matrix for `OpenGLCamera`

- [#2508](https://github.com/ManimCommunity/manim/pull/2508): Improve performance for [`Mobject.become()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.become "manim.mobject.mobject.Mobject.become")

- [#2332](https://github.com/ManimCommunity/manim/pull/2332): Changed `color`, `stroke_color` and `fill_color` attributes to properties

- [#2396](https://github.com/ManimCommunity/manim/pull/2396): Fixed animations introducing or removing objects

- [`ShowPassingFlash`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash "manim.animation.indication.ShowPassingFlash") now removes objects when the animation is finished

- Added `introducer` keyword argument to [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") analogous to `remover`

- Updated [`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph") vertex addition handling


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.15.0-changelog.html\#fixed-bugs "Link to this heading")

- [#2574](https://github.com/ManimCommunity/manim/pull/2574): Improved Error in [`utils.tex_file_writing`](https://docs.manim.community/en/stable/reference/manim.utils.tex_file_writing.html#module-manim.utils.tex_file_writing "manim.utils.tex_file_writing")

- [#2580](https://github.com/ManimCommunity/manim/pull/2580): Fixed [`find_intersection()`](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.find_intersection "manim.utils.space_ops.find_intersection") in [`space_ops`](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#module-manim.utils.space_ops "manim.utils.space_ops")

- [#2576](https://github.com/ManimCommunity/manim/pull/2576): Fixed a bug with animation of removal of edges from a [`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph")

- [#2556](https://github.com/ManimCommunity/manim/pull/2556): Fixed showing highlighted cells when creating [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

- [#2559](https://github.com/ManimCommunity/manim/pull/2559): Fix setting line numbers in [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") when using ManimPango settings

- [#2557](https://github.com/ManimCommunity/manim/pull/2557): Fixed logger bug in [`Camera.make_background_from_func()`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.make_background_from_func "manim.camera.camera.Camera.make_background_from_func")

- [#2548](https://github.com/ManimCommunity/manim/pull/2548): Fixed [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes") plotting bug with logarithmic x-axis

- [#1547](https://github.com/ManimCommunity/manim/pull/1547): Fixed certain unicode characters in users’ paths causing issues on Windows

- [#2526](https://github.com/ManimCommunity/manim/pull/2526): Fixed segfault when using `--enable_gui`

- [#2538](https://github.com/ManimCommunity/manim/pull/2538): Fixed flickering OpenGL preview when using `frozen_frame`

- [#2528](https://github.com/ManimCommunity/manim/pull/2528): Fixed custom naming of gifs and added some tests

- [#2487](https://github.com/ManimCommunity/manim/pull/2487): Fixed [`ThreeDCamera.remove_fixed_orientation_mobjects()`](https://docs.manim.community/en/stable/reference/manim.camera.three_d_camera.ThreeDCamera.html#manim.camera.three_d_camera.ThreeDCamera.remove_fixed_orientation_mobjects "manim.camera.three_d_camera.ThreeDCamera.remove_fixed_orientation_mobjects")

- [#2530](https://github.com/ManimCommunity/manim/pull/2530): Use single source of truth for default text values

- [#2494](https://github.com/ManimCommunity/manim/pull/2494): Fixed an issue related to previewing gifs

- [#2490](https://github.com/ManimCommunity/manim/pull/2490): Fixed order of transformation application in [`SVGMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject "manim.mobject.svg.svg_mobject.SVGMobject")

- [#2357](https://github.com/ManimCommunity/manim/pull/2357): Fixed `screeninfo.get_monitors` for MacOS

- [#2444](https://github.com/ManimCommunity/manim/pull/2444): Fixed [`VectorScene.add_axes()`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.VectorScene.html#manim.scene.vector_space_scene.VectorScene.add_axes "manim.scene.vector_space_scene.VectorScene.add_axes")


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.15.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#2560](https://github.com/ManimCommunity/manim/pull/2560): Refactored more docstrings in [`geometry`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.html#module-manim.mobject.geometry "manim.mobject.geometry")

- [#2571](https://github.com/ManimCommunity/manim/pull/2571): Refactored docstrings in [`graphing`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.html#module-manim.mobject.graphing "manim.mobject.graphing")

- [#2569](https://github.com/ManimCommunity/manim/pull/2569): Refactored docstrings in [`geometry`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.html#module-manim.mobject.geometry "manim.mobject.geometry")

- [#2549](https://github.com/ManimCommunity/manim/pull/2549): Added a page for internals which links to our GitHub wiki

- [#2458](https://github.com/ManimCommunity/manim/pull/2458): Improved documentation for [`Rotate`](https://docs.manim.community/en/stable/reference/manim.animation.rotation.Rotate.html#manim.animation.rotation.Rotate "manim.animation.rotation.Rotate")

- [#2459](https://github.com/ManimCommunity/manim/pull/2459): Added examples to some transform animations

- [#2517](https://github.com/ManimCommunity/manim/pull/2517): Added guide on profiling and improving performance

- [#2518](https://github.com/ManimCommunity/manim/pull/2518): Added imports to examples for `deprecation` decorator

- [#2499](https://github.com/ManimCommunity/manim/pull/2499): Improved help text for `--write_to_movie`

- [#2465](https://github.com/ManimCommunity/manim/pull/2465): Added documentation for [`index_labels()`](https://docs.manim.community/en/stable/reference/manim.utils.debug.html#manim.utils.debug.index_labels "manim.utils.debug.index_labels")

- [#2495](https://github.com/ManimCommunity/manim/pull/2495): Updated minimal LaTeX installation instructions

- [#2500](https://github.com/ManimCommunity/manim/pull/2500): Added note about contributions during refactor period

- [#2431](https://github.com/ManimCommunity/manim/pull/2431): Changed example in [`Surface.set_fill_by_value()`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface.set_fill_by_value "manim.mobject.three_d.three_dimensions.Surface.set_fill_by_value")

- [#2485](https://github.com/ManimCommunity/manim/pull/2485): Fixed some typos in documentation

- [#2493](https://github.com/ManimCommunity/manim/pull/2493): Fixed typo in documentation for parameters of [`Square`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html#manim.mobject.geometry.polygram.Square "manim.mobject.geometry.polygram.Square")

- [#2482](https://github.com/ManimCommunity/manim/pull/2482): Updated Python version requirement in installation guide

- [#2438](https://github.com/ManimCommunity/manim/pull/2438): Removed unnecessary rotation from example

- [#2468](https://github.com/ManimCommunity/manim/pull/2468): Hid more private methods from the docs

- [#2466](https://github.com/ManimCommunity/manim/pull/2466): Fixed a typo in the documentation for plugins

- [#2448](https://github.com/ManimCommunity/manim/pull/2448): Improvements to the `.pot` files cleaning system

- [#2436](https://github.com/ManimCommunity/manim/pull/2436): Fixed typo and improved example in building blocks tutorial


### Changes to our development infrastructure [¶](https://docs.manim.community/en/stable/changelog/0.15.0-changelog.html\#changes-to-our-development-infrastructure "Link to this heading")

- [#2554](https://github.com/ManimCommunity/manim/pull/2554): Removed `Remove-Item` calls for MSYS2 Python

- [#2531](https://github.com/ManimCommunity/manim/pull/2531): Added a GitHub Action for automatic validation of citation metadata

- [#2536](https://github.com/ManimCommunity/manim/pull/2536): Upgraded version of setup-ffmpeg CI action

- [#2484](https://github.com/ManimCommunity/manim/pull/2484): Updated tinytex download URL


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.15.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#2573](https://github.com/ManimCommunity/manim/pull/2573): Moved [`value_tracker`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.html#module-manim.mobject.value_tracker "manim.mobject.value_tracker") back inside [`mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html#module-manim.mobject.mobject "manim.mobject.mobject")

- [#2566](https://github.com/ManimCommunity/manim/pull/2566): Removed unused livestream-related imports and functions from [`scene_file_writer`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.html#module-manim.scene.scene_file_writer "manim.scene.scene_file_writer")

- [#2524](https://github.com/ManimCommunity/manim/pull/2524): Reworked [`space_ops`](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#module-manim.utils.space_ops "manim.utils.space_ops")

- [#2519](https://github.com/ManimCommunity/manim/pull/2519): Removed outdated comment

- [#2503](https://github.com/ManimCommunity/manim/pull/2503): Removed unused imports

- [#2475](https://github.com/ManimCommunity/manim/pull/2475): Removed setuptools dependency

- [#2472](https://github.com/ManimCommunity/manim/pull/2472): Removed unnecessary comment in [`simple_functions`](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html#module-manim.utils.simple_functions "manim.utils.simple_functions")

- [#2429](https://github.com/ManimCommunity/manim/pull/2429): Upgraded to future-style type annotations

- [#2464](https://github.com/ManimCommunity/manim/pull/2464): Bump pillow from 8.4.0 to 9.0.0

- [#2376](https://github.com/ManimCommunity/manim/pull/2376): Updated dependencies for Python 3.10

- [#2437](https://github.com/ManimCommunity/manim/pull/2437): Cleaned up [`simple_functions`](https://docs.manim.community/en/stable/reference/manim.utils.simple_functions.html#module-manim.utils.simple_functions "manim.utils.simple_functions")

- Removed `fdiv` as in all cases where it was used, it was just doing the same thing as numpy array division.

- Replaced old implementation of the choose function with scipy’s implementation

- Use `lru_cache` (least recently used cache) for caching the choose function. Since it’s only used for beziers, only 2 choose k and 3 choose k will be used, hence a size of 10 should be enough.

- Removed `clip_in_place` in favor of `np.clip`

- Removed one use of `clip_in_place` that wasn’t actually doing anything


- [#2439](https://github.com/ManimCommunity/manim/pull/2439): Removed twitter template from scripts


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.15.0-changelog.html\#new-releases "Link to this heading")

- [#2547](https://github.com/ManimCommunity/manim/pull/2547): Prepared new release, `v0.15.0`


[Develop and launch modern apps with MongoDB Atlas, a resilient data platform.](https://server.ethicalads.io/proxy/click/8269/019600e8-faa4-7f71-9bfc-1b120575ca28/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8269/019600e8-faa4-7f71-9bfc-1b120575ca28/)