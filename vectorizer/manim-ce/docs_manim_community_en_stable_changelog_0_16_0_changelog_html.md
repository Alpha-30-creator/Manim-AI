ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# v0.16.0 [¶](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html\#v0-16-0 "Link to this heading")

Date:

July 13, 2022

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html\#contributors "Link to this heading")

A total of 44 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Alex Lembcke

- Baroudi Aymen +

- Benjamin Hackl

- Charalampos Georgiou +

- Cindy Park +

- Ejar +

- Francesco Frassinelli +

- Francisco Manríquez Novoa +

- Jacob Evan Shreve +

- Jaime Santos +

- Jonathan Alpert

- Joshua Mankelow +

- Kevin Lubick +

- Laith Bahodi

- Lingren Kong +

- Logen +

- Naveen M K

- Noam Zaks

- Pedro Lamkowski +

- Raghav Goel

- Simeon Widdis

- Sparsh Goenka

- TornaxO7 +

- Tristan Schulz +

- WillSoltas

- ad\_chaos

- conor-oneill-2 +

- fcrozatier +

- mooncaker816 +

- niklebedenko +

- nyabkun +

- quark67


The patches included in this release have been reviewed by
the following contributors.

- Alex Lembcke

- Benjamin Hackl

- Darylgolden

- Francesco Frassinelli

- Francisco Manríquez Novoa

- Gianluca Gippetto

- Jan-Hendrik Müller

- Jonathan Alpert

- Kevin Lubick

- Laith Bahodi

- Naveen M K

- Pedro Lamkowski

- Philipp Imhof

- Raghav Goel

- Ryan McCauley

- Sparsh Goenka

- TornaxO7

- Tristan Schulz

- ad\_chaos

- hickmott99


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 56 pull requests were merged for this release.

### Highlights [¶](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html\#highlights "Link to this heading")

- [#2550](https://github.com/ManimCommunity/manim/pull/2550): New thematic guide: a deep dive into the internals of the library

This new [thematic guide](https://docs.manim.community/en/stable/guides/deep_dive.html) aims to be a comprehensive walkthrough
describing all the things that Manim does when you run it to produce a video.

- [#2732](https://github.com/ManimCommunity/manim/pull/2732): Improved overall structure of deployed documentation; added a dedicated [FAQ section](https://docs.manim.community/en/stable/faq/index.html)

- [#2749](https://github.com/ManimCommunity/manim/pull/2749): Added [`ChangeSpeed`](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed "manim.animation.speedmodifier.ChangeSpeed"), an animation wrapper that allows to smoothly change the speed at which an animation is played

The speed of any animation can be changed by wrapping the animation with [`ChangeSpeed`](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed "manim.animation.speedmodifier.ChangeSpeed") and passing a dictionary as `speedinfo` whose keys are the relative animation run time stamps and whose values are the absolute speed factors; e.g., `{0.5: 2, 0.75: 0.25}` smoothly speeds up the animation by a factor of 2 once it has been completed to 50%, and then it is smoothly slowed down to 1/4 of the default run speed after 75% of the animation are completed. The `run_time` of the animation will be adjusted to match the changed play speed.



It is also possible to add time-based updaters that respect the change in speed, use the auxiliary [`ChangeSpeed.add_updater()`](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.add_updater "manim.animation.speedmodifier.ChangeSpeed.add_updater") method to do so.


### New features [¶](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html\#new-features "Link to this heading")

- [#2667](https://github.com/ManimCommunity/manim/pull/2667): Made FFmpeg executable path configurable

- [#2739](https://github.com/ManimCommunity/manim/pull/2739): Added vectorized plotting functionality via keyword argument `use_vectorized` to improve performance


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html\#enhancements "Link to this heading")

- [#2186](https://github.com/ManimCommunity/manim/pull/2186): Enabled filling color by value for `OpenGLSurface`, replaced `colors` keyword argument of [`Surface.set_fill_by_value()`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface.set_fill_by_value "manim.mobject.three_d.three_dimensions.Surface.set_fill_by_value") with `colorscale`

- [#2288](https://github.com/ManimCommunity/manim/pull/2288): Added warning when attempting to add same mobject as child twice

- [#2707](https://github.com/ManimCommunity/manim/pull/2707): Fixed missing `get_nth_curve_length_pieces` method of `OpenGLVMobject`

- Removed duplicate definition of `get_curve_functions_with_lengths` in `OpenGLVMobject`

- Added definition of `get_nth_curve_length_pieces` to `OpenGLVMobject`


- [#2709](https://github.com/ManimCommunity/manim/pull/2709): Improved the look of the brackets of [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

- [#2714](https://github.com/ManimCommunity/manim/pull/2714): Fixed `OpenGLVMobject.pointwise_become_partial()` to improve stroke rendering

- [#2727](https://github.com/ManimCommunity/manim/pull/2727): Slight performance improvement for [`ArrowVectorField`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#manim.mobject.vector_field.ArrowVectorField "manim.mobject.vector_field.ArrowVectorField") and Bézier curve computation

- [#2728](https://github.com/ManimCommunity/manim/pull/2728): Added [`VectorField.fit_to_coordinate_system()`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.fit_to_coordinate_system "manim.mobject.vector_field.VectorField.fit_to_coordinate_system") to fit a vector field to a given coordinate system

- [#2730](https://github.com/ManimCommunity/manim/pull/2730): Added note to let users find documentation of default CLI subcommand easier

- [#2746](https://github.com/ManimCommunity/manim/pull/2746): Installed ghostscript in the docker image

- [#2841](https://github.com/ManimCommunity/manim/pull/2841): Added `split_quadratic_bezier()` and `subdivide_quadratic_bezier()`

- [#2842](https://github.com/ManimCommunity/manim/pull/2842): CLI: Moved functionality from `manim new` to `manim init` and added deprecation warning for `manim new`

- [#2866](https://github.com/ManimCommunity/manim/pull/2866): Reorganize test files to match library module structure


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html\#fixed-bugs "Link to this heading")

- [#2567](https://github.com/ManimCommunity/manim/pull/2567): Use tempconfig for every scene render

- [#2638](https://github.com/ManimCommunity/manim/pull/2638): Fixed `BarChart.change_bar_values()` not updating when height is 0

- [#2661](https://github.com/ManimCommunity/manim/pull/2661): Fixed tip resize functionality for [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes") to match documentation

- [#2703](https://github.com/ManimCommunity/manim/pull/2703): Default to utf-8 when reading files in [`Code`](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code "manim.mobject.text.code_mobject.Code")

- [#2721](https://github.com/ManimCommunity/manim/pull/2721): Fixed bad text slicing for lines in [`Paragraph`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph")

- [#2725](https://github.com/ManimCommunity/manim/pull/2725): Fixed wrong indentation in [`Code`](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code "manim.mobject.text.code_mobject.Code")

- [#2734](https://github.com/ManimCommunity/manim/pull/2734): Fixed OpenGL segfaults when running [`Scene.play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") or [`Scene.wait()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait "manim.scene.scene.Scene.wait") in interactive mode

- [#2753](https://github.com/ManimCommunity/manim/pull/2753): Fixed multiplatform builds for docker images in pipeline

- [#2757](https://github.com/ManimCommunity/manim/pull/2757): Added missing `__init__.py` file in [`docbuild`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.html#module-manim.utils.docbuild "manim.utils.docbuild") module

- [#2770](https://github.com/ManimCommunity/manim/pull/2770): Fixed bug in [`VMobject.proportion_from_point()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.proportion_from_point "manim.mobject.types.vectorized_mobject.VMobject.proportion_from_point") that caused proportions greater than 1 to be returned

- [#2826](https://github.com/ManimCommunity/manim/pull/2826): Fixed leaked mobjects coming from [`TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")

- [#2870](https://github.com/ManimCommunity/manim/pull/2870): Fixed issue with `manim init scene SCENE_NAME filename.py` and removed necessity of `main.py` to be present in working directory


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#2704](https://github.com/ManimCommunity/manim/pull/2704): Updated URL to Pango Markup formatting page

- [#2716](https://github.com/ManimCommunity/manim/pull/2716): Improved the order of the reference manuals

- [#2720](https://github.com/ManimCommunity/manim/pull/2720): Fixed typo in docstring of [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle")

- [#2722](https://github.com/ManimCommunity/manim/pull/2722): Fixed typos in docstrings of classes in [`mobject.table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.html#module-manim.mobject.table "manim.mobject.table")

- [#2726](https://github.com/ManimCommunity/manim/pull/2726): Edited note on [`NumberPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane") length and added another example

- [#2740](https://github.com/ManimCommunity/manim/pull/2740): Fixed documentation of [`Cylinder.get_direction()`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cylinder.html#manim.mobject.three_d.three_dimensions.Cylinder.get_direction "manim.mobject.three_d.three_dimensions.Cylinder.get_direction")

- [#2755](https://github.com/ManimCommunity/manim/pull/2755): Fixed docstring of [`VMobject.get_end_anchors()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.get_end_anchors "manim.mobject.types.vectorized_mobject.VMobject.get_end_anchors")

- [#2760](https://github.com/ManimCommunity/manim/pull/2760): Removed `cmake` from the MacOS installation section

- [#2767](https://github.com/ManimCommunity/manim/pull/2767): Added more questions and answers to FAQ section, new [OpenGL FAQ](https://docs.manim.community/en/stable/faq/opengl.html)

- [#2771](https://github.com/ManimCommunity/manim/pull/2771): Added documentation and testing for `path_func` keyword argument of [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

- [#2828](https://github.com/ManimCommunity/manim/pull/2828): Removed suggestion issue template, added FAQ answer regarding proposing new features

- [#2849](https://github.com/ManimCommunity/manim/pull/2849): Added example for `path_arc` keyword argument of [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

- [#2851](https://github.com/ManimCommunity/manim/pull/2851): Added an example on constructing a (neural) network using a partite [`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph")

- [#2855](https://github.com/ManimCommunity/manim/pull/2855): Added implicit `docker.io/` URL base in reference to docker images

- [#2861](https://github.com/ManimCommunity/manim/pull/2861): Added docstring for [`CoordinateSystem.plot_parametric_curve()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_parametric_curve "manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_parametric_curve")


### Changes concerning the testing system [¶](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html\#changes-concerning-the-testing-system "Link to this heading")

- [#2743](https://github.com/ManimCommunity/manim/pull/2743): Replaced `assert` statements with with assertion functions from `np.testing`


### Changes to our development infrastructure [¶](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html\#changes-to-our-development-infrastructure "Link to this heading")

- [#2700](https://github.com/ManimCommunity/manim/pull/2700): CI: updated Python versions

- [#2701](https://github.com/ManimCommunity/manim/pull/2701): CI: added a workflow to publish docker image after releases and commits to main branch


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#2680](https://github.com/ManimCommunity/manim/pull/2680): Increased minimum required version of `numpy` to 1.19

- [#2687](https://github.com/ManimCommunity/manim/pull/2687): Migrated from `os.path` to `pathlib` in [`SVGMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject "manim.mobject.svg.svg_mobject.SVGMobject") and other locations

- [#2715](https://github.com/ManimCommunity/manim/pull/2715): Updated deprecated `pillow` constants

- [#2735](https://github.com/ManimCommunity/manim/pull/2735): Bump pyjwt from 2.3.0 to 2.4.0

- [#2748](https://github.com/ManimCommunity/manim/pull/2748): Bump pillow from 9.1.0 to 9.1.1

- [#2751](https://github.com/ManimCommunity/manim/pull/2751): Fixed flake C417 and improved a comment

- [#2825](https://github.com/ManimCommunity/manim/pull/2825): Bump notebook from 6.4.11 to 6.4.12

- [#2864](https://github.com/ManimCommunity/manim/pull/2864): Updated lockfile


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.16.0-changelog.html\#new-releases "Link to this heading")

- [#2863](https://github.com/ManimCommunity/manim/pull/2863): Prepared new release, `v0.16.0`


[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/8270/019600ef-84c4-7a10-bb12-59bf43bc8d72/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/devops/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8270/019600ef-84c4-7a10-bb12-59bf43bc8d72/)