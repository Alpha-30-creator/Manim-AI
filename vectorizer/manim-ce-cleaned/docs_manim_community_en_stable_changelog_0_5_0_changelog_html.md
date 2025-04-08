# v0.5.0 [¶](https://docs.manim.community/en/stable/changelog/0.5.0-changelog.html\#v0-5-0 "Link to this heading")

Date:

April 02, 2021

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.5.0-changelog.html\#contributors "Link to this heading")

A total of 35 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Abel Aebker +

- Abhijith Muthyala

- AntonBallmaier +

- Aron

- Benjamin Hackl

- Bogdan Stăncescu +

- Darylgolden

- Devin Neal

- GameDungeon +

- Hugues Devimeux

- Jason Villanueva

- Kapil Sachdeva

- KingWampy

- Lionel Ray +

- Mark Miller

- Mohammad Al-Fetyani +

- Naveen M K

- Niklas Dewally +

- Oliver +

- Roopesh +

- Seb Pearce +

- aebkea +

- friedkeenan

- hydrobeam +

- kolibril13

- sparshg

- tfglynn +


The patches included in this release have been reviewed by
the following contributors.

- Abel Aebker

- Abhijith Muthyala

- Benjamin Hackl

- Bogdan Stăncescu

- Devin Neal

- Hugues Devimeux

- Jason Villanueva

- Kapil Sachdeva

- KingWampy

- Leo Torres

- Lionel Ray

- Mark Miller

- Mohammad Al-Fetyani

- Naveen M K

- Oliver

- Ricky Chon

- vector67


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.5.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 64 pull requests were merged for this release.

### Highlights [¶](https://docs.manim.community/en/stable/changelog/0.5.0-changelog.html\#highlights "Link to this heading")

- [#1075](https://github.com/ManimCommunity/manim/pull/1075): Add OpenGL Renderer

Adds an OpenGLRenderer, OpenGLCamera, OpenGL-enabled Mobjects, and a `--use_opengl_renderer` flag. When this flag is passed, you can pass the `-p` flag to preview animations, the `-w` flag to generate video, and the `-q` flag to specify render quality. If you don’t pass either the `-p` or the `-w` flag, nothing will happen. Scenes rendered with the OpenGL renderer must _only_ use OpenGL-enabled Mobjects.


### Deprecated classes and functions [¶](https://docs.manim.community/en/stable/changelog/0.5.0-changelog.html\#deprecated-classes-and-functions "Link to this heading")

- [#1124](https://github.com/ManimCommunity/manim/pull/1124): Deprecated `ShowCreation` in favor of `Create`

1. Deprecated `ShowCreation` in favor of `Create` across the library with the exception of the show\_creation boolean variable vector\_space\_scene.py

2. Added a deprecation warning in the original `ShowCreation` class.


- [#1110](https://github.com/ManimCommunity/manim/pull/1110): Deprecated SmallDot + OpenGLSmallDot

SmallDot isn’t necessary and a deprecation warning will be raised. This will be removed in a future release.


### New features [¶](https://docs.manim.community/en/stable/changelog/0.5.0-changelog.html\#new-features "Link to this heading")

- [#1037](https://github.com/ManimCommunity/manim/pull/1037): Added new fade and transform animations ( [`TransformMatchingShapes`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html#manim.animation.transform_matching_parts.TransformMatchingShapes "manim.animation.transform_matching_parts.TransformMatchingShapes"), [`TransformMatchingTex`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html#manim.animation.transform_matching_parts.TransformMatchingTex "manim.animation.transform_matching_parts.TransformMatchingTex"), [`FadeTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform "manim.animation.transform.FadeTransform")) from 3b1b/manim

Added new Fade animation: `FadeOutToPoint`
Added `FadeTransform` and `FadeTransformPieces` for transforming mobjects and submobjects with a fade
Added `TransformMatchingShapes` and `TransformMatchingTex` for transforming mobjects and tex that have matching parts

- [#1097](https://github.com/ManimCommunity/manim/pull/1097): Added 3D Mobject [`Dot3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Dot3D.html#manim.mobject.three_d.three_dimensions.Dot3D "manim.mobject.three_d.three_dimensions.Dot3D")

- [#1074](https://github.com/ManimCommunity/manim/pull/1074): Added jupyter media\_width option to the config

- [#1107](https://github.com/ManimCommunity/manim/pull/1107): Added [`Unwrite`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Unwrite.html#manim.animation.creation.Unwrite "manim.animation.creation.Unwrite") animation class to complement [`Write`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Write.html#manim.animation.creation.Write "manim.animation.creation.Write")

Added `Unwrite` which inherits from [`Write`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Write.html#manim.animation.creation.Write "manim.animation.creation.Write"). It automatically reverses the animation of [`Write`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Write.html#manim.animation.creation.Write "manim.animation.creation.Write") by passing the reversed rate function, but it also takes an additional boolean parameter reverse which, if False, renders the animation from left to right (assuming text oriented in the usual way), but if True, it renders right to left.

- [#1085](https://github.com/ManimCommunity/manim/pull/1085): Added [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle") and [`RightAngle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.RightAngle.html#manim.mobject.geometry.line.RightAngle "manim.mobject.geometry.line.RightAngle") for intersecting lines

[`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle") and [`RightAngle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.RightAngle.html#manim.mobject.geometry.line.RightAngle "manim.mobject.geometry.line.RightAngle") both take two lines as input. If they intersect, or share a common vertex, an angle is drawn between them. Users can customize the look of the angle and also use a dotted right angle.


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.5.0-changelog.html\#enhancements "Link to this heading")

- [#1144](https://github.com/ManimCommunity/manim/pull/1144): Improved quality of GIFs

- [#1157](https://github.com/ManimCommunity/manim/pull/1157): Refresh triangulation on call to `apply_points_function()`

Rotate called apply\_points\_function, which was previous not subclassed by OpenGLMobject - now it is. Then, the vertex normals can be updated too.



Additionally, the old\_points matrix would change after rotating, making the old points / new points test irrelevant. This is addressed with a .copy call.

- [#1151](https://github.com/ManimCommunity/manim/pull/1151): Added parametric function support to `OpenGLSurface`

- [#1139](https://github.com/ManimCommunity/manim/pull/1139): In-Code config\[“preview”\] Support

- [#1123](https://github.com/ManimCommunity/manim/pull/1123): Added caching, skipping, and user-specified background colors to the OpenGL renderer

OpenGL play logic has been improved to support caching and skipping with -n argument ( it is now similar to Cairo play logic). A random bug was fixed in OpenGLSurface and OpenGL background color can now be changed via background\_color argument.

- [#1118](https://github.com/ManimCommunity/manim/pull/1118): Allow passing animation arguments with .animate syntax

Users will now be able to do things like obj.animate(run\_time=2).method(arg) if they want to specify animation arguments for an individual .animate call, and can still not specify any arguments like obj.animate.method(arg).



Passing animation arguments is only allowed directly after .animate is accessed, if passed elsewhere then a ValueError is raised.

- [#718](https://github.com/ManimCommunity/manim/pull/718): Rotating the numbers in y axis

In Axes, the y axis will be rotated 90deg but the numbers are
also rotated and shouldn’t be. Fixes this issue.

- [#1070](https://github.com/ManimCommunity/manim/pull/1070): Raise FileNotFoundError when unable to locate the .cfg file specified via `--config_file`

Raising the error will stop script execution and let the user know that there are problems with the –config\_file location instead of reverting back to the default configuration.


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.5.0-changelog.html\#fixed-bugs "Link to this heading")

- [#1224](https://github.com/ManimCommunity/manim/pull/1224): Fixed [`ShowIncreasingSubsets`](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowIncreasingSubsets.html#manim.animation.creation.ShowIncreasingSubsets "manim.animation.creation.ShowIncreasingSubsets"), [`ShowSubmobjectsOneByOne`](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowSubmobjectsOneByOne.html#manim.animation.creation.ShowSubmobjectsOneByOne "manim.animation.creation.ShowSubmobjectsOneByOne"), and [`AddTextLetterByLetter`](https://docs.manim.community/en/stable/reference/manim.animation.creation.AddTextLetterByLetter.html#manim.animation.creation.AddTextLetterByLetter "manim.animation.creation.AddTextLetterByLetter")

- [#1201](https://github.com/ManimCommunity/manim/pull/1201): Prevent crash on `embed()` for empty scenes

- [#1192](https://github.com/ManimCommunity/manim/pull/1192): Fixed issue when an animation is cached, manim can’t merge the partial movie files.

- [#1193](https://github.com/ManimCommunity/manim/pull/1193): Fixed using [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") without a child [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") in [`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

AnimationGroup may now take Animation objects which do not have a child Mobject, such as Wait.

- [#1170](https://github.com/ManimCommunity/manim/pull/1170): Fixed minor SVG parsing bugs

- [#1159](https://github.com/ManimCommunity/manim/pull/1159): Added support for multiple transforms in the same SVG element

- [#1156](https://github.com/ManimCommunity/manim/pull/1156): Fixed [`DrawBorderThenFill`](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html#manim.animation.creation.DrawBorderThenFill "manim.animation.creation.DrawBorderThenFill") to support OpenGL and improved type hints for some functions

Fixed a bug in [`DrawBorderThenFill`](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html#manim.animation.creation.DrawBorderThenFill "manim.animation.creation.DrawBorderThenFill") that prevented [`Write`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Write.html#manim.animation.creation.Write "manim.animation.creation.Write") animations from working with `OpenGLVMobjects` and slightly improved type hints for some animation functions to include `OpenGLVMobject`.

- [#1134](https://github.com/ManimCommunity/manim/pull/1134): Fixed the -a flag.

The `-a` / `--write-all` flag was broken. When used, it would cause Manim to crash just after beginning to render the second scene.

- [#1115](https://github.com/ManimCommunity/manim/pull/1115): Fixed bugs in `OpenGLMobject` and added `ApplyMethod` support

Fixed undefined variables and converted `Mobject` to `OpenGLMobject`. Also, fixed assert statement in `ApplyMethod`.

- [#1092](https://github.com/ManimCommunity/manim/pull/1092): Refactored coordinate\_systems.py, fixed bugs, added [`NumberPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane") test

The default behavior of [`rotate()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.rotate "manim.mobject.mobject.Mobject.rotate") is to rotate about the center of [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine") is symmetric about the point at the number 0 only when `|x_min|` == `|x_max|`. Ideally, the rotation should coincide with
the point at number 0 on the line.



Added a regression test and additionally fixed some bugs introduced in [#718](https://github.com/ManimCommunity/manim/pull/718).

- [#1078](https://github.com/ManimCommunity/manim/pull/1078): Removed stray print statements from \_\_main\_\_.py

Uses rich’s print traceback instead and fixes an issue in printing the version twice when manim –version is called.

- [#1086](https://github.com/ManimCommunity/manim/pull/1086): Fixed broken line spacing in [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")

The line\_spacing kwarg was missing when creating `Text` Mobjects; this adds it.

- [#1083](https://github.com/ManimCommunity/manim/pull/1083): Corrected the shape of [`Torus`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html#manim.mobject.three_d.three_dimensions.Torus "manim.mobject.three_d.three_dimensions.Torus")

`Torus` draws a surface with an elliptical cross-section when minor\_radius is different from 1. This PR ensures the cross-section is always a circle.


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.5.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#1217](https://github.com/ManimCommunity/manim/pull/1217): Copyedited the document on testing in our documentation

- [#1206](https://github.com/ManimCommunity/manim/pull/1206): Added Docstrings to [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

- [#1218](https://github.com/ManimCommunity/manim/pull/1218): Removed BezierSpline from the example gallery

- [#1219](https://github.com/ManimCommunity/manim/pull/1219): Updated Dockerfile (include dependencies for building documentation), moved documentation to main README

- [#1209](https://github.com/ManimCommunity/manim/pull/1209): Added :ref\_methods: to the manim directive

This allows class methods to be linked in the documentation. Checkout the [example references](https://docs.manim.community/en/latest/examples.html#movingaround) below the code to see how this is used!

- [#1204](https://github.com/ManimCommunity/manim/pull/1204): Added rotation example to example gallery

- [#1137](https://github.com/ManimCommunity/manim/pull/1137): Added GitHub Wiki pages on adding testing/documentation to Sphinx Docs

- [#1114](https://github.com/ManimCommunity/manim/pull/1114): Added examples for [`Ellipse`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html#manim.mobject.geometry.arc.Ellipse "manim.mobject.geometry.arc.Ellipse"), [`Polygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon"), [`RegularPolygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygon.html#manim.mobject.geometry.polygram.RegularPolygon "manim.mobject.geometry.polygram.RegularPolygon"), [`Triangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Triangle.html#manim.mobject.geometry.polygram.Triangle "manim.mobject.geometry.polygram.Triangle") and [`RoundedRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RoundedRectangle.html#manim.mobject.geometry.polygram.RoundedRectangle "manim.mobject.geometry.polygram.RoundedRectangle")

- [#1195](https://github.com/ManimCommunity/manim/pull/1195): Removed SmallDot from example

- [#1130](https://github.com/ManimCommunity/manim/pull/1130): Added pre-commit to run black and flake8, updated contributing documentation accordingly

- [#1138](https://github.com/ManimCommunity/manim/pull/1138): Moved previous version changelogs to separate files; Added a Script to generate future changelogs

This script quickly generates a changelog for whoever is making the release.

- [#1190](https://github.com/ManimCommunity/manim/pull/1190): Added note in contributing guide to read the latest version of the documentation

- [#1188](https://github.com/ManimCommunity/manim/pull/1188): Added sounds example to docs

- [#1165](https://github.com/ManimCommunity/manim/pull/1165): Added documentation for installing Manim on Colab

- [#1128](https://github.com/ManimCommunity/manim/pull/1128): Added examples for [`DashedLine`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DashedLine.html#manim.mobject.geometry.line.DashedLine "manim.mobject.geometry.line.DashedLine"), [`TangentLine`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.TangentLine.html#manim.mobject.geometry.line.TangentLine "manim.mobject.geometry.line.TangentLine"), [`Elbow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Elbow.html#manim.mobject.geometry.line.Elbow "manim.mobject.geometry.line.Elbow"), [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow"), [`Vector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector"), [`DoubleArrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DoubleArrow.html#manim.mobject.geometry.line.DoubleArrow "manim.mobject.geometry.line.DoubleArrow")

- [#1177](https://github.com/ManimCommunity/manim/pull/1177): Replace links to the latest version of the documentation to the stable version

- [#1077](https://github.com/ManimCommunity/manim/pull/1077): Added details to `get_critical_point()`

- [#1154](https://github.com/ManimCommunity/manim/pull/1154): Fixed some typing hints. (ints to floats)

- [#1036](https://github.com/ManimCommunity/manim/pull/1036): Added [`SurroundingRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html#manim.mobject.geometry.shape_matchers.SurroundingRectangle "manim.mobject.geometry.shape_matchers.SurroundingRectangle") to the example gallery

- [#1103](https://github.com/ManimCommunity/manim/pull/1103): Added documentation and examples for Square, Dot, Circle and Rectangle

- [#1101](https://github.com/ManimCommunity/manim/pull/1101): Added documentation to [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

- [#1088](https://github.com/ManimCommunity/manim/pull/1088): Added new svg files to documentation and imports

In particular, SVGPathMobject, VMobjectFromPathstring, and the style\_utils functions to manim’s namespace.

- [#1076](https://github.com/ManimCommunity/manim/pull/1076): Improve documentation for GraphScene

Updated coords\_to\_point and point\_to\_coords under manim/scene/graph\_scene.py as the dosctring of each function confusingly described the opposite of what it is supposed to do.


### Changes concerning the testing system [¶](https://docs.manim.community/en/stable/changelog/0.5.0-changelog.html\#changes-concerning-the-testing-system "Link to this heading")

- [#1160](https://github.com/ManimCommunity/manim/pull/1160): Enable CI testing for OpenGL

- [#1100](https://github.com/ManimCommunity/manim/pull/1100): Rewrote test cases to use sys.executable in the command instead of “python”

Tests would fail due to capture() not spawning a subshell in the correct environment, so when python was called, the test would be unable to find necessary packages.

- [#1079](https://github.com/ManimCommunity/manim/pull/1079): Removed the hardcoded value, manim, in test\_version.py


### Changes to our development infrastructure [¶](https://docs.manim.community/en/stable/changelog/0.5.0-changelog.html\#changes-to-our-development-infrastructure "Link to this heading")

- [#1213](https://github.com/ManimCommunity/manim/pull/1213): Updated TinyTex dependencies

- [#1187](https://github.com/ManimCommunity/manim/pull/1187): Add CodeCov to Github Workflow

- [#1166](https://github.com/ManimCommunity/manim/pull/1166): CI: Use poetry’s cache dir rather than pip

- [#1071](https://github.com/ManimCommunity/manim/pull/1071): Enable pytest-cov based code coverage

- Include pytest-cov as a python module as part of developer dependencies

- In updating poetry to include pytest-cov, manimpango moved from version 0.2.3 to 0.2.4, and libpango1.0-dev needed to be installed in Ubuntu.

- Add to the CI workflow (ci.yml) to create and upload test coverage.


- [#1073](https://github.com/ManimCommunity/manim/pull/1073): Removed “one line summary” from PULL\_REQUEST\_TEMPLATE.md


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.5.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#1167](https://github.com/ManimCommunity/manim/pull/1167): Merge `OpenGLMobject` and [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

- [#1164](https://github.com/ManimCommunity/manim/pull/1164): Fixed single PEP8 style in cairo\_renderer.py

- [#1140](https://github.com/ManimCommunity/manim/pull/1140): Flake8 Compat & Code Cleanup

- [#1019](https://github.com/ManimCommunity/manim/pull/1019): Refactored [`play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play")

- Removed the \_\*\*three\*\*\_ decorators of [`play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play"), in particular: caching logic and file writer logic are now included within [`play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") (it wasn’t possible before, because scene.wait and scene.play were two different things).

- Added is\_static\_wait attributes to Wait. (<=> if wait is a frozen frame).

- Renamed and moved scene.add\_static\_frame to renderer.freeze\_current\_frame.

- Now when calling play without animation, it raises ValueError instead of just a warning.

- Fixed [#874](https://github.com/ManimCommunity/manim/pull/874) by modifying renderer.update\_skipping\_status

- renderer starts the animation with scene.begin\_animations (scene.compile\_animation\_data used to do this)

- The run time and the time progression generation is now done in scene.play\_internal although it’d make more sense that renderer processes it later.

- Added a bunch of cool tests thanks to mocks, and thanks to the new syntax scene.render