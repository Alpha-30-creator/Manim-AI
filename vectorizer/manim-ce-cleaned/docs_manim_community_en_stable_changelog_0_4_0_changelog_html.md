# v0.4.0 [¶](https://docs.manim.community/en/stable/changelog/0.4.0-changelog.html\#v0-4-0 "Link to this heading")

Date:

March 3, 2021

The changes since Manim Community release v0.3.0 are listed below.

## Breaking Changes [¶](https://docs.manim.community/en/stable/changelog/0.4.0-changelog.html\#breaking-changes "Link to this heading")

- [#915](https://github.com/ManimCommunity/manim/pull/915): Manim’s SVG engine has been reworked and is able to handle a wider variations of SVG files. In particular: fill and stroke properties are now retained from the original files. Breaking change: `VMobjectFromSVGPathstring` is deprecated and has been renamed to `SVGPathMobject`.


## New Features [¶](https://docs.manim.community/en/stable/changelog/0.4.0-changelog.html\#new-features "Link to this heading")

- [#1026](https://github.com/ManimCommunity/manim/pull/1026): Add 3D Mobjects: [`Cone`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone "manim.mobject.three_d.three_dimensions.Cone"), [`Cylinder`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cylinder.html#manim.mobject.three_d.three_dimensions.Cylinder "manim.mobject.three_d.three_dimensions.Cylinder"), [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D"), [`Arrow3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Arrow3D.html#manim.mobject.three_d.three_dimensions.Arrow3D "manim.mobject.three_d.three_dimensions.Arrow3D") and [`Torus`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html#manim.mobject.three_d.three_dimensions.Torus "manim.mobject.three_d.three_dimensions.Torus")

- [#1047](https://github.com/ManimCommunity/manim/pull/1047): Add documentation and examples for [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

- [#1044](https://github.com/ManimCommunity/manim/pull/1044): `register_font` is available for macOS

- [#995](https://github.com/ManimCommunity/manim/pull/995): Add generic `set()` method and compatibility layer between properties and `get_*`/ `set_*` methods


## Bugfixes and Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.4.0-changelog.html\#bugfixes-and-enhancements "Link to this heading")

- [#981](https://github.com/ManimCommunity/manim/pull/981): Fixed hot reload functionality for the WebGL renderer on Windows

- [#1053](https://github.com/ManimCommunity/manim/pull/1053): Repair links to source code in stable version of documentation

- [#1067](https://github.com/ManimCommunity/manim/pull/1067): Add ManimPango to ReadTheDocs requirements

- [#1058](https://github.com/ManimCommunity/manim/pull/1058): Replace `<color>` syntax by Pango’s `<span foreground>` for coloring parts of [`MarkupText`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText") and allow using colors for underline, overline and strikethrough in MarkupText

- [#1063](https://github.com/ManimCommunity/manim/pull/1063): Fix documentation related to `.animate`

- [#1065](https://github.com/ManimCommunity/manim/pull/1065): Remove duplicate word ‘vector’

- [#1060](https://github.com/ManimCommunity/manim/pull/1060): Update Linux installation instructions to mention the installation of Pango

- [#1050](https://github.com/ManimCommunity/manim/pull/1050): Ensure that the user-supplied stroke color and width gets applied to [`Cross`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.Cross.html#manim.mobject.geometry.shape_matchers.Cross "manim.mobject.geometry.shape_matchers.Cross")

- [#1059](https://github.com/ManimCommunity/manim/pull/1059): More descriptive error when accessing an unhandled mobject attribute

- [#1048](https://github.com/ManimCommunity/manim/pull/1048): Use absolute path in `make_and_open_docs.py`

- [#1000](https://github.com/ManimCommunity/manim/pull/1000): Remove `MovingCameraScene.setup` and `MovingCameraScene.camera_frame`

- [#1051](https://github.com/ManimCommunity/manim/pull/1051): Corrections for setting stroke related attributes on [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

- [#1043](https://github.com/ManimCommunity/manim/pull/1043): Make [`CubicBezier`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CubicBezier.html#manim.mobject.geometry.arc.CubicBezier "manim.mobject.geometry.arc.CubicBezier") explicitly accept four points

- [#1046](https://github.com/ManimCommunity/manim/pull/1046): Use any version of `importlib-metadata`

- [#1030](https://github.com/ManimCommunity/manim/pull/1030): Parse `.log` file and try to print LaTeX errors if compilation fails

- [#1015](https://github.com/ManimCommunity/manim/pull/1015): Documentation: Add more explicit instructions related to `tlmgr`

- [#1028](https://github.com/ManimCommunity/manim/pull/1028): Documentation: Update installation guide on mac with Apple Silicon

- [#1032](https://github.com/ManimCommunity/manim/pull/1032): Remove `Square.side_length` property

- [#1031](https://github.com/ManimCommunity/manim/pull/1031): Fix link to wikipedia vector graphics page

- [#1021](https://github.com/ManimCommunity/manim/pull/1021): Documentation: Added example to [`CubicBezier`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CubicBezier.html#manim.mobject.geometry.arc.CubicBezier "manim.mobject.geometry.arc.CubicBezier")

- [#1017](https://github.com/ManimCommunity/manim/pull/1017): Added `progress_bar` to `digest_args` to fix the `--progress_bar` CLI flag

- [#1018](https://github.com/ManimCommunity/manim/pull/1018): Remove redundancy in [`FunctionGraph`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.FunctionGraph.html#manim.mobject.graphing.functions.FunctionGraph "manim.mobject.graphing.functions.FunctionGraph") arguments

- [#1024](https://github.com/ManimCommunity/manim/pull/1024): Migrate `width` / `height` / `depth` to properties

- [#1022](https://github.com/ManimCommunity/manim/pull/1022): Fix `-p` flag when passing `-s`

- [#1008](https://github.com/ManimCommunity/manim/pull/1008): CI pipeline: fix release asset upload

- [#983](https://github.com/ManimCommunity/manim/pull/983): Make sure last frame for animations with updaters is correct

- [#984](https://github.com/ManimCommunity/manim/pull/984): Add manim version to CLI output, append version name for generated `.gif` and `.png` files, add version to metadata of rendered videos, change dark blue terminal text to default green

- [#993](https://github.com/ManimCommunity/manim/pull/993): Fix setting Mobject color to a gradient by passing a list of colors in [`set_color()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.set_color "manim.mobject.types.vectorized_mobject.VMobject.set_color")

- [#1003](https://github.com/ManimCommunity/manim/pull/1003): Fix animation [`GrowArrow`](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowArrow.html#manim.animation.growing.GrowArrow "manim.animation.growing.GrowArrow")

- [#1010](https://github.com/ManimCommunity/manim/pull/1010): Disable STDIN interaction for ffmpeg concat.

- [#969](https://github.com/ManimCommunity/manim/pull/969): Fix the `--tex_template` CLI flag

- [#989](https://github.com/ManimCommunity/manim/pull/989): Fix the `manim cfg export` subcommand

- [#1005](https://github.com/ManimCommunity/manim/pull/1005): Fix the feature where `-` is used as the filename

- [#998](https://github.com/ManimCommunity/manim/pull/998): Allow using hexadecimal color codes with 3 characters

- [#996](https://github.com/ManimCommunity/manim/pull/996): Changed the message of `manim --version` to not include “Edition”