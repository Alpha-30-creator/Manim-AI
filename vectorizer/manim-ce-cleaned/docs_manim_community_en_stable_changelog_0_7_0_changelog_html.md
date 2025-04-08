# v0.7.0 [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#v0-7-0 "Link to this heading")

Date:

June 01, 2021

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#contributors "Link to this heading")

A total of 45 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- André +

- Anton Ballmaier

- Benjamin Hackl

- Clar Fon

- Darylgolden

- Devin Neal

- Hugues Devimeux

- Iced-Tea3 +

- Jan-Hendrik Müller

- Jason Villanueva

- Jerónimo Squartini +

- KingWampy

- Laith Bahodi

- Max Stoumen +

- Mohammad Al-Fetyani

- Naveen M K

- NeoPlato

- Newell Jensen

- Nikhil Garuda

- Nikhil Sharma +

- PaulCMurdoch +

- Philipp Imhof

- Raghav Goel

- Robert West +

- Ryan McCauley +

- Skaft +

- SwiddisZwei +

- e4coder +

- friedkeenan

- malte-v +

- ralphieraccoon

- sparshg


The patches included in this release have been reviewed by
the following contributors.

- Aathish Sivasubrahmanian

- Abhijith Muthyala

- Anton Ballmaier

- Aron

- Benjamin Hackl

- Darylgolden

- Devin Neal

- GameDungeon

- Hugues Devimeux

- Iced-Tea3

- Jan-Hendrik Müller

- Jason Villanueva

- Jerónimo Squartini

- KingWampy

- Laith Bahodi

- Mark Miller

- Mohammad Al-Fetyani

- Naveen M K

- Nikhil Garuda

- Oliver

- Philipp Imhof

- Raghav Goel

- Ricky Chon

- Ryan McCauley

- Skaft

- SwiddisZwei

- e4coder

- friedkeenan

- ralphieraccoon

- sparshg


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 87 pull requests were merged for this release.

### Breaking changes [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#breaking-changes "Link to this heading")

- [#1521](https://github.com/ManimCommunity/manim/pull/1521): Improve [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") docs

- Improve documentation of the [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") class.

- Unify the signature of `get_all_mobjects`. Now it always returns a sequence of [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). This breaks using `FadeTransform.get_all_mobjects` as `Group`.


- [#1470](https://github.com/ManimCommunity/manim/pull/1470): Drop support for Python 3.6

Manim won’t work on Python 3.6 anymore.


### Highlights [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#highlights "Link to this heading")

- [#1447](https://github.com/ManimCommunity/manim/pull/1447): Added [`PolarPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html#manim.mobject.graphing.coordinate_systems.PolarPlane "manim.mobject.graphing.coordinate_systems.PolarPlane") for polar coordinates.

- [#1490](https://github.com/ManimCommunity/manim/pull/1490): Added [`Polygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram"), rework the polygon inheritance tree, and add [`Star`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Star.html#manim.mobject.geometry.polygram.Star "manim.mobject.geometry.polygram.Star")

- Add [`Polygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram"), a generalized [`Polygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon") that allows for disconnected sets of edges.

- Make [`Polygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon") inherit from [`Polygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram").

- Add [`regular_vertices()`](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.regular_vertices "manim.utils.space_ops.regular_vertices")

- Add [`RegularPolygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygram.html#manim.mobject.geometry.polygram.RegularPolygram "manim.mobject.geometry.polygram.RegularPolygram").

- Make [`RegularPolygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygon.html#manim.mobject.geometry.polygram.RegularPolygon "manim.mobject.geometry.polygram.RegularPolygon") inherit from [`RegularPolygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygram.html#manim.mobject.geometry.polygram.RegularPolygram "manim.mobject.geometry.polygram.RegularPolygram").

- Add [`Star`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Star.html#manim.mobject.geometry.polygram.Star "manim.mobject.geometry.polygram.Star").


- [#1462](https://github.com/ManimCommunity/manim/pull/1462): OpenGL: Added `Shader`, `Mesh`, and `FullScreenQuad`

Add Shader and Mesh objects

- [#1418](https://github.com/ManimCommunity/manim/pull/1418): Added project management commands

- `manim init` \- quickly sets up default files for a manim project.

- `manim new project` \- lets the user set project settings. It also creates the project inside a new folder of name <project\_name>

- `manim new scene` \- used to quickly insert new scenes into files. If `file name` is not provided `main.py` is used as default.


### Deprecated classes and functions [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#deprecated-classes-and-functions "Link to this heading")

- [#1598](https://github.com/ManimCommunity/manim/pull/1598): Update examples to use [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes") and deprecate `GraphScene`

`GraphScene` has been deprecated and its functionality has been shifted to [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes"). See the updated example gallery for sample usage.

- [#1454](https://github.com/ManimCommunity/manim/pull/1454): Fading module enhancements

Moved functionality of all Fading classes to [`FadeIn`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeIn.html#manim.animation.fading.FadeIn "manim.animation.fading.FadeIn") and [`FadeOut`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html#manim.animation.fading.FadeOut "manim.animation.fading.FadeOut"). All other fading classes have been deprecated.

- [#1375](https://github.com/ManimCommunity/manim/pull/1375): Deleted the deprecated `ShowCreation` in favor of [`Create`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create")


### New features [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#new-features "Link to this heading")

- [#1566](https://github.com/ManimCommunity/manim/pull/1566): Added the ability to add gridlines to a [`Rectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle")

- [#1548](https://github.com/ManimCommunity/manim/pull/1548): Added [`ArcBrace`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.ArcBrace.html#manim.mobject.svg.brace.ArcBrace "manim.mobject.svg.brace.ArcBrace"), a subclass of [`Brace`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace "manim.mobject.svg.brace.Brace").

- [#1559](https://github.com/ManimCommunity/manim/pull/1559): Update VGroup to support item assignment (#1530)

Support indexed item-assignment for VGroup

- [#1518](https://github.com/ManimCommunity/manim/pull/1518): Allow fading multiple Mobjects in one Animation

- [#1422](https://github.com/ManimCommunity/manim/pull/1422): Added [`override_animation()`](https://docs.manim.community/en/stable/reference/manim.animation.animation.html#manim.animation.animation.override_animation "manim.animation.animation.override_animation") decorator

- [#1504](https://github.com/ManimCommunity/manim/pull/1504): Color module enhancements

- Replaced `BLUE_E` with what was previously `DARK_BLUE` and removed `DARK_BLUE`

- Added alias `LIGHTER_GRAY` for `GRAY_A`

- Added `PURE_RED`, `PURE_BLUE` and renamed `GREEN_SCREEN` to `PURE_GREEN`

- All gray colors are now also available using British spelling (including `GREY_BROWN`)

- Replaced color example in the docs. It can now be used as a quick reference for all color names.


- [#1272](https://github.com/ManimCommunity/manim/pull/1272): Implement metaclass approach in geometry module to make mobjects compatible with cairo and opengl rendering

- [#1404](https://github.com/ManimCommunity/manim/pull/1404): Added two deprecation decorators

Added two function decorators `deprecated` and `deprecated_params` as a consistent way of deprecating code.


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#enhancements "Link to this heading")

- [#1572](https://github.com/ManimCommunity/manim/pull/1572): OpenGL compatibility via metaclass: [`TracedPath`](https://docs.manim.community/en/stable/reference/manim.animation.changing.TracedPath.html#manim.animation.changing.TracedPath "manim.animation.changing.TracedPath"), [`ParametricFunction`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ParametricFunction.html#manim.mobject.graphing.functions.ParametricFunction "manim.mobject.graphing.functions.ParametricFunction"), [`Brace`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace "manim.mobject.svg.brace.Brace"), [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

- [#1472](https://github.com/ManimCommunity/manim/pull/1472): Porting methods from `GraphScene` to [`CoordinateSystem`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem "manim.mobject.graphing.coordinate_systems.CoordinateSystem")

- [#1589](https://github.com/ManimCommunity/manim/pull/1589): OpenGL compatibility via metaclass: [`ValueTracker`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html#manim.mobject.value_tracker.ValueTracker "manim.mobject.value_tracker.ValueTracker")

- [#1564](https://github.com/ManimCommunity/manim/pull/1564): Add extra notes for TeX compilation errors

Add hint to use custom `TexTemplate` on TeX compilation errors

- [#1584](https://github.com/ManimCommunity/manim/pull/1584): Added a check for `0` in [`round_corners()`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram.round_corners "manim.mobject.geometry.polygram.Polygram.round_corners")

- [#1586](https://github.com/ManimCommunity/manim/pull/1586): Add OpenGLMobject support to all `isinstance` occurrences

This PR increases the support for OpenGL in the remaining animation classes and in other places where appropriate.

- [#1577](https://github.com/ManimCommunity/manim/pull/1577): Added new metaclass ConvertToOpenGL (replacing MetaVMobject), restore IntelliSense

- [#1562](https://github.com/ManimCommunity/manim/pull/1562): Improved VectorField’s Nudge Accuracy Per Step

Implemented the Runge-Kutta algorithm in VectorField’s nudge function. This increases the accuracy as an object moves along a vector field. This also increases efficiency as the nudge function requires less loops to achieve accuracy than the previous implementation.

- [#1480](https://github.com/ManimCommunity/manim/pull/1480): Add logging info to tex errors

- [#1567](https://github.com/ManimCommunity/manim/pull/1567): Compatibility Fixes with ManimPango v0.3.0

- ManimPango v0.3.0+ is required for Manim now.

- Show errors from Pango when Markup isn’t correct


- [#1512](https://github.com/ManimCommunity/manim/pull/1512): OpenGL compatibility via metaclass: graph

- [#1511](https://github.com/ManimCommunity/manim/pull/1511): OpenGL compatibility via metaclass: svg\_mobject, text\_mobject, tex\_mobject

- [#1502](https://github.com/ManimCommunity/manim/pull/1502): Added `center` parameter to [`Sphere`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Sphere.html#manim.mobject.three_d.three_dimensions.Sphere "manim.mobject.three_d.three_dimensions.Sphere") and `point` parameter to [`Dot3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Dot3D.html#manim.mobject.three_d.three_dimensions.Dot3D "manim.mobject.three_d.three_dimensions.Dot3D")

- [#1486](https://github.com/ManimCommunity/manim/pull/1486): Update of `rate_functions`

Changed the picture for the non standard rate functions.

- [#1495](https://github.com/ManimCommunity/manim/pull/1495): Ported value\_tracker to OpenGL

- [#1382](https://github.com/ManimCommunity/manim/pull/1382): Expand documentation, testing, and functionality of ValueTrackers; remove ExponentialValueTracker

Added more documentation and inline operators to ValueTracker and ComplexValueTracker. Brought coverage for value\_tracker.py to 100%. Removed ExponentialValueTracker.

- [#1475](https://github.com/ManimCommunity/manim/pull/1475): Add SVG elliptical arc support


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#fixed-bugs "Link to this heading")

- [#1574](https://github.com/ManimCommunity/manim/pull/1574): Fixed error when processing SVG with omitted elliptical arc command

- [#1596](https://github.com/ManimCommunity/manim/pull/1596): Fix indexing for non-whitespace tex arg separator

Fixes #1568



Fix issue when setting the arg\_separator of a Tex object as a non-whitespace character(s). The method break\_up\_by\_substrings(self) was not accounting for the separator when setting the index.

- [#1588](https://github.com/ManimCommunity/manim/pull/1588): Fixed multiple animations being saved in the same file

- [#1571](https://github.com/ManimCommunity/manim/pull/1571): Fix tests after introducing parallelization

- [#1545](https://github.com/ManimCommunity/manim/pull/1545): Fix outdated parameters for `LinearTransformationScene` and add an example + typing.

- [#1513](https://github.com/ManimCommunity/manim/pull/1513): Fixed rotation of gradients while rotating a VMobject

- Fixed the direction of gradient which remained the same while rotating VMobjects

- Added `rotate_sheen_direction()` method in VMobject


- [#1570](https://github.com/ManimCommunity/manim/pull/1570): Output errors to stderr

- [#1560](https://github.com/ManimCommunity/manim/pull/1560): Declare `*.npz` `*.wav` `*.png` as binary in `.gitattributes`

- [#1211](https://github.com/ManimCommunity/manim/pull/1211): Refactored scene caching and fixed issue when a different hash was produced when copying a mobject in the scene

Refactored internal scene-caching mechanism and fixed bug when an inconsistent hash was produced when copying a mobject.

- [#1527](https://github.com/ManimCommunity/manim/pull/1527): Improved handling of substring isolation within sqrt, and fixed a bug with transform\_mismatch for the matching shape transforms

- [#1526](https://github.com/ManimCommunity/manim/pull/1526): Fix fading

- [#1523](https://github.com/ManimCommunity/manim/pull/1523): Fix multiple FadeIn / Out only working on VMobjects


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#1599](https://github.com/ManimCommunity/manim/pull/1599): Added example for [`Annulus`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html#manim.mobject.geometry.arc.Annulus "manim.mobject.geometry.arc.Annulus")

- [#1415](https://github.com/ManimCommunity/manim/pull/1415): New example for gallery and some docs refinements

- [#1509](https://github.com/ManimCommunity/manim/pull/1509): Copyedited Documentation

Added a link to Manim Community GitHub page in `for_dev.rst`.
Fixed [`get_start()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_start "manim.mobject.mobject.Mobject.get_start") and added `roll` link in `building_blocks-rst`
Added language to code blocks in `configuration.rst`

- [#1384](https://github.com/ManimCommunity/manim/pull/1384): Added typings to space\_ops.py

Added Typehints to most of the functions

- [#1500](https://github.com/ManimCommunity/manim/pull/1500): Example for [`apply_complex_function()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.apply_complex_function "manim.mobject.mobject.Mobject.apply_complex_function")

- [#1551](https://github.com/ManimCommunity/manim/pull/1551): Fixed the typo for Admonitions

- [#1550](https://github.com/ManimCommunity/manim/pull/1550): Restructuring of Contribution Section

- [#1541](https://github.com/ManimCommunity/manim/pull/1541): Fixing broken links and other minor doc things

- [#1516](https://github.com/ManimCommunity/manim/pull/1516): Update docs to use `t_range` instead of `t_min` and `t_max` in [`ParametricFunction`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ParametricFunction.html#manim.mobject.graphing.functions.ParametricFunction "manim.mobject.graphing.functions.ParametricFunction")

- [#1508](https://github.com/ManimCommunity/manim/pull/1508): Update troubleshooting docs

- [#1485](https://github.com/ManimCommunity/manim/pull/1485): Added [`Title`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Title.html#manim.mobject.text.tex_mobject.Title "manim.mobject.text.tex_mobject.Title") example for the docs

- [#1439](https://github.com/ManimCommunity/manim/pull/1439): Cleaning `Sequence` typehints

- [#1440](https://github.com/ManimCommunity/manim/pull/1440): Added Scoop installation docs (Windows)

- [#1452](https://github.com/ManimCommunity/manim/pull/1452): Refine typehints at [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle")

- [#1458](https://github.com/ManimCommunity/manim/pull/1458): Refine docs of [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") ( add `disable_ligatures=True` for t2c)

- [#1449](https://github.com/ManimCommunity/manim/pull/1449): Added [`PointCloudDot`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PointCloudDot.html#manim.mobject.types.point_cloud_mobject.PointCloudDot "manim.mobject.types.point_cloud_mobject.PointCloudDot") example

- [#1473](https://github.com/ManimCommunity/manim/pull/1473): Added easy example for [`arrange_in_grid()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange_in_grid "manim.mobject.mobject.Mobject.arrange_in_grid")

- [#1402](https://github.com/ManimCommunity/manim/pull/1402): Added typestring parser checker

- [#1451](https://github.com/ManimCommunity/manim/pull/1451): Reduce complexity of AngleExample

- [#1441](https://github.com/ManimCommunity/manim/pull/1441): Add inheritance diagrams to reference page

Added inheritance diagrams to the reference page as a quick navigation method.

- [#1457](https://github.com/ManimCommunity/manim/pull/1457): Fixing broken doc links

- [#1445](https://github.com/ManimCommunity/manim/pull/1445): Remove $ from tutorial commands


### Changes concerning the testing system [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#changes-concerning-the-testing-system "Link to this heading")

- [#1556](https://github.com/ManimCommunity/manim/pull/1556): Try pytest-xdist for parallelization in tests


### Changes to our development infrastructure [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#changes-to-our-development-infrastructure "Link to this heading")

- [#1505](https://github.com/ManimCommunity/manim/pull/1505): Add docs reference to PR template

Added documentation link to the Pull Request Template.

- [#1499](https://github.com/ManimCommunity/manim/pull/1499): Updated Discord links in the docs to point towards a standardized redirect

- [#1461](https://github.com/ManimCommunity/manim/pull/1461): Build the docs - Logging

- [#1481](https://github.com/ManimCommunity/manim/pull/1481): pyproject.toml: poetry\_core -> poetry-core

- [#1477](https://github.com/ManimCommunity/manim/pull/1477): Update RDT sphinx package to version 3.5.3

- [#1460](https://github.com/ManimCommunity/manim/pull/1460): Create CONTRIBUTING.md

- [#1453](https://github.com/ManimCommunity/manim/pull/1453): manim\_directive: fix image links in docs - Windows

Use POSIX path on Windows to link images so documentation can build locally.


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#1465](https://github.com/ManimCommunity/manim/pull/1465): Added typings and description to some functions in [`coordinate_systems`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.html#module-manim.mobject.graphing.coordinate_systems "manim.mobject.graphing.coordinate_systems").

- [#1552](https://github.com/ManimCommunity/manim/pull/1552): Removed unwanted parameters in geometry

Removed `anchors_span_full_range`, `close_new_points`, `anchors_span_full_range`, `preserve_tip_size_when_scaling`, `mark_paths_closed` and `close_new_points`

- [#1597](https://github.com/ManimCommunity/manim/pull/1597): Removed hilite\_me and insert\_line\_numbers\_in\_html from global name space

- [#1535](https://github.com/ManimCommunity/manim/pull/1535): Update dependencies and fix tests

- [#1544](https://github.com/ManimCommunity/manim/pull/1544): Adding spell checker as a pre-commit hook

- [#1542](https://github.com/ManimCommunity/manim/pull/1542): Swapping a pango markup link in docs

- [#1531](https://github.com/ManimCommunity/manim/pull/1531): Don’t use deprecated methods in deprecation.py

- [#1492](https://github.com/ManimCommunity/manim/pull/1492): Remove stray print statements introduced in #1404

- [#1471](https://github.com/ManimCommunity/manim/pull/1471): Fix Some Warnings from lgtm


### Changes that needed to be reverted again [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#changes-that-needed-to-be-reverted-again "Link to this heading")

- [#1606](https://github.com/ManimCommunity/manim/pull/1606): Bring back `DARK_BLUE`


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.7.0-changelog.html\#new-releases "Link to this heading")

- [#1601](https://github.com/ManimCommunity/manim/pull/1601): Preparation for v0.7.0: added changelog and bumped version number