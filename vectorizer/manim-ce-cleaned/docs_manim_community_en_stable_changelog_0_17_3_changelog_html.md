# v0.17.3 [¶](https://docs.manim.community/en/stable/changelog/0.17.3-changelog.html\#v0-17-3 "Link to this heading")

Date:

April 06, 2023

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.17.3-changelog.html\#contributors "Link to this heading")

A total of 35 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Alex Lembcke

- Benjamin Hackl

- DegrangeM +

- Elyanah Aco +

- Francisco Manríquez Novoa

- Fredrik Lundström +

- Frédéric Crozatier

- Ikko Eltociear Ashimine +

- ItIsJoeyG +

- JinchuLi2002 +

- Kevin Lubick

- KingAndCross +

1. Ali +
- Matthew Lee +

- Max Coplan +

- Naveen M K

- NotWearingPants

- Oscar Rangel +

- Papierkorb2292 +

- Phoenix2157 +

- Tristan Schulz

- ciobaca +

- coreyp1 +

- davidot +

- icedcoffeeee

- karpfediem +

- vahndi


The patches included in this release have been reviewed by
the following contributors.

- Benjamin Hackl

- Fredrik Lundström

- Frédéric Crozatier

- Hugues Devimeux

- Kevin Lubick

- KingAndCross

- Matthew Lee

- Naveen M K

- Tristan Schulz

- coreyp1

- davidot

- strager


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.17.3-changelog.html\#pull-requests-merged "Link to this heading")

A total of 42 pull requests were merged for this release.

### Deprecated classes and functions [¶](https://docs.manim.community/en/stable/changelog/0.17.3-changelog.html\#deprecated-classes-and-functions "Link to this heading")

- [#3103](https://github.com/ManimCommunity/manim/pull/3103): Removed deprecated function `OpenGLSurface.set_fill_by_value`


### New features [¶](https://docs.manim.community/en/stable/changelog/0.17.3-changelog.html\#new-features "Link to this heading")

- [#2974](https://github.com/ManimCommunity/manim/pull/2974): Added [`DiGraph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph"), a mobject representing directed graphs

- [#3042](https://github.com/ManimCommunity/manim/pull/3042): Added [`Scene.replace()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.replace "manim.scene.scene.Scene.replace") and use in [`ReplacementTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html#manim.animation.transform.ReplacementTransform "manim.animation.transform.ReplacementTransform")

- [#3155](https://github.com/ManimCommunity/manim/pull/3155): Added support for individualized radius values in [`Polygram.round_corners()`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram.round_corners "manim.mobject.geometry.polygram.Polygram.round_corners")

- [#3159](https://github.com/ManimCommunity/manim/pull/3159): Added [`set_opacity_by_tex()`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex "manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex") method for setting the opacity of parts of Tex mobjects

- [#3201](https://github.com/ManimCommunity/manim/pull/3201): New tip shape [`StealthTip`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html#manim.mobject.geometry.tips.StealthTip "manim.mobject.geometry.tips.StealthTip"), allow specifying tip shape of [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.17.3-changelog.html\#enhancements "Link to this heading")

- [#3046](https://github.com/ManimCommunity/manim/pull/3046): Add warning if font is not found for Text, Code, and MarkupText

- [#3083](https://github.com/ManimCommunity/manim/pull/3083): Minor performance improvement in [`bezier`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#module-manim.utils.bezier "manim.utils.bezier") with preallocating array

- [#3092](https://github.com/ManimCommunity/manim/pull/3092): Improved [`Mobject.add()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add "manim.mobject.mobject.Mobject.add") performance by checking for redundancy only once

- [#3134](https://github.com/ManimCommunity/manim/pull/3134): Performance: Store color data of `OpenGLSurface` to prevent OpenGL embed lag

- [#3180](https://github.com/ManimCommunity/manim/pull/3180): Performance: Speed up width/height/depth calculations by reducing copying

- [#3181](https://github.com/ManimCommunity/manim/pull/3181): Improved creation time for large [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") mobjects

- [#3182](https://github.com/ManimCommunity/manim/pull/3182): Reduce memory allocations when building [`SVGMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject "manim.mobject.svg.svg_mobject.SVGMobject")

- [#3191](https://github.com/ManimCommunity/manim/pull/3191): Fixed OpenGL rendering in named threads


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.17.3-changelog.html\#fixed-bugs "Link to this heading")

- [#3015](https://github.com/ManimCommunity/manim/pull/3015): Fixed bug with `label_constructor` in [`NumberLine.add_labels()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine.add_labels "manim.mobject.graphing.number_line.NumberLine.add_labels")

- [#3095](https://github.com/ManimCommunity/manim/pull/3095): Fixed `get_axis_labels` for [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes") and [`ThreeDAxes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ThreeDAxes.html#manim.mobject.graphing.coordinate_systems.ThreeDAxes "manim.mobject.graphing.coordinate_systems.ThreeDAxes")

- [#3106](https://github.com/ManimCommunity/manim/pull/3106): Fixed ignored `depth_test` argument for `OpenGLVMobjects`

- [#3149](https://github.com/ManimCommunity/manim/pull/3149): Allow to use `call_updater=True` in [`Mobject.add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater") with non-timebased updaters too

- [#3152](https://github.com/ManimCommunity/manim/pull/3152): Fixed behavior of [`Wait`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait "manim.animation.animation.Wait") and [`Scene.wait()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait "manim.scene.scene.Scene.wait") with specified `stop_condition`

- [#3163](https://github.com/ManimCommunity/manim/pull/3163): Fixed [`BraceLabel`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceLabel.html#manim.mobject.svg.brace.BraceLabel "manim.mobject.svg.brace.BraceLabel") not passing additional keyword arguments to [`Brace`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace "manim.mobject.svg.brace.Brace")

- [#3195](https://github.com/ManimCommunity/manim/pull/3195): Fixed [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes") scaling for [`plot_implicit_curve()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_implicit_curve "manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_implicit_curve")


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.17.3-changelog.html\#documentation-related-changes "Link to this heading")

- [#3105](https://github.com/ManimCommunity/manim/pull/3105): Converted types specified in docstrings to proper type hints in [`three_dimensions`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.html#module-manim.mobject.three_d.three_dimensions "manim.mobject.three_d.three_dimensions")

- [#3108](https://github.com/ManimCommunity/manim/pull/3108): Clarified documentation for `--resolution` command line flag

- [#3109](https://github.com/ManimCommunity/manim/pull/3109): Clean-up, type-hints and documentation for [`three_dimensions`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.html#module-manim.mobject.three_d.three_dimensions "manim.mobject.three_d.three_dimensions")

- [#3124](https://github.com/ManimCommunity/manim/pull/3124): Fixed docstring of [`ThreeDCamera.get_value_trackers()`](https://docs.manim.community/en/stable/reference/manim.camera.three_d_camera.ThreeDCamera.html#manim.camera.three_d_camera.ThreeDCamera.get_value_trackers "manim.camera.three_d_camera.ThreeDCamera.get_value_trackers")

- [#3126](https://github.com/ManimCommunity/manim/pull/3126): Fixed dead links to troubleshooting page

- [#3137](https://github.com/ManimCommunity/manim/pull/3137): Fixed example using `reverse=True` with [`Write`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Write.html#manim.animation.creation.Write "manim.animation.creation.Write")

- [#3160](https://github.com/ManimCommunity/manim/pull/3160): Fixed a typo

- [#3189](https://github.com/ManimCommunity/manim/pull/3189): Corrected the hinted return type for `angle_between_vectors()`

- [#3199](https://github.com/ManimCommunity/manim/pull/3199): Updated `winget` command for installing MiKTeX in documentation

- [#3204](https://github.com/ManimCommunity/manim/pull/3204): Fixed docstring formatting of [`Scene.replace()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.replace "manim.scene.scene.Scene.replace") and improved its error handling


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.17.3-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#3144](https://github.com/ManimCommunity/manim/pull/3144): Fixed typo in `stripUntranslatable.awk`

- [#3154](https://github.com/ManimCommunity/manim/pull/3154): Bump ipython from 8.7.0 to 8.10.0

- [#3156](https://github.com/ManimCommunity/manim/pull/3156): CI: Remove actions using self-hosted runners

- [#3164](https://github.com/ManimCommunity/manim/pull/3164): Bump markdown-it-py from 2.1.0 to 2.2.0

- [#3165](https://github.com/ManimCommunity/manim/pull/3165): Removed deprecated keyword argument in [`Mobject.align_to()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.align_to "manim.mobject.mobject.Mobject.align_to")

- [#3166](https://github.com/ManimCommunity/manim/pull/3166): Made [`ArrowTriangleTip`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTriangleTip.html#manim.mobject.geometry.tips.ArrowTriangleTip "manim.mobject.geometry.tips.ArrowTriangleTip"), [`ArrowTriangleFilledTip`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTriangleFilledTip.html#manim.mobject.geometry.tips.ArrowTriangleFilledTip "manim.mobject.geometry.tips.ArrowTriangleFilledTip") available to module namespace

- [#3179](https://github.com/ManimCommunity/manim/pull/3179): Fixed deprecation warning in [`ParametricFunction`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ParametricFunction.html#manim.mobject.graphing.functions.ParametricFunction "manim.mobject.graphing.functions.ParametricFunction") with `use_vectorized=True`

- [#3186](https://github.com/ManimCommunity/manim/pull/3186): Updated extlinks to work with latest version of Sphinx

- [#3196](https://github.com/ManimCommunity/manim/pull/3196): CI: updated PATH for recent changed in TinyTex

- [#3200](https://github.com/ManimCommunity/manim/pull/3200): Made import from `moderngl` compatible with more recent versions


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.17.3-changelog.html\#new-releases "Link to this heading")

- [#3198](https://github.com/ManimCommunity/manim/pull/3198): Prepare new release: v0.17.3