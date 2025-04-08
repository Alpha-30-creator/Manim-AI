# v0.8.0 [¶](https://docs.manim.community/en/stable/changelog/0.8.0-changelog.html\#v0-8-0 "Link to this heading")

Date:

July 02, 2021

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.8.0-changelog.html\#contributors "Link to this heading")

A total of 37 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Benjamin Hackl

- Bill Shillito +

- Darigov Research +

- Darylgolden

- Devin Neal

- Iced-Tea3

- Jan-Hendrik Müller

- Jason Villanueva

- KingWampy

- Laith Bahodi

- MathInvariance +

- Max Stoumen

- Mehmet Ali Özer +

- Michael Pilosov +

- Mohammad Al-Fetyani

- Naveen M K

- Nikhil Garuda

- Oliver

- PaulCMurdoch

- Philipp Imhof

- PipedQuintes +

- Raghav Goel

- Ryan McCauley

- Ujjayanta +

- Vagrid +

- andrehisatsuga +

- friedkeenan

- peaceheis +

- yit6 +


The patches included in this release have been reviewed by
the following contributors.

- Abhijith Muthyala

- Anton Ballmaier

- Aron

- Benjamin Hackl

- Clar Fon

- Darylgolden

- Devin Neal

- Jan-Hendrik Müller

- Jason Villanueva

- KingWampy

- Laith Bahodi

- Mark Miller

- MathInvariance

- Mohammad Al-Fetyani

- Naveen M K

- Nikhil Garuda

- Oliver

- Philipp Imhof

- Raghav Goel

- Ryan McCauley

- Ujjayanta

- Vagrid

- friedkeenan


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.8.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 76 pull requests were merged for this release.

### Deprecated classes and functions [¶](https://docs.manim.community/en/stable/changelog/0.8.0-changelog.html\#deprecated-classes-and-functions "Link to this heading")

- [#1616](https://github.com/ManimCommunity/manim/pull/1616): Remove all functions and classes that were deprecated until `v0.6.0`


### New features [¶](https://docs.manim.community/en/stable/changelog/0.8.0-changelog.html\#new-features "Link to this heading")

- [#1716](https://github.com/ManimCommunity/manim/pull/1716): Rewrite stroke and fill shaders

Rewrite vectorized mobject shaders to be compatible with transformation matrices.

- [#1695](https://github.com/ManimCommunity/manim/pull/1695): Add option to justify text with [`MarkupText`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText")

A new parameter `justify` is added to [`MarkupText`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText"). It can be used to justify a paragraph of text.

- [#1660](https://github.com/ManimCommunity/manim/pull/1660): Added support for `.webm` and transparency of videos in Jupyter notebooks

- Added support for generating `webm` videos via the command line flag `--format=webm`

- Added transparency support for Jupyter notebooks


- [#1553](https://github.com/ManimCommunity/manim/pull/1553): Add dearpygui integration


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.8.0-changelog.html\#enhancements "Link to this heading")

- [#1728](https://github.com/ManimCommunity/manim/pull/1728): Improved positioning and size of the OpenGL window; added some configuration options

- [#1733](https://github.com/ManimCommunity/manim/pull/1733): Let OpenGLMobject.copy return a deep copy by default

- [#1735](https://github.com/ManimCommunity/manim/pull/1735): Metaclass compatibility for coordinate\_system.py, Code and ParametricSurface

- [#1585](https://github.com/ManimCommunity/manim/pull/1585): OpenGL compatibility via metaclass for [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix"), [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber"), [`Variable`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Variable.html#manim.mobject.text.numbers.Variable "manim.mobject.text.numbers.Variable")

- [#1713](https://github.com/ManimCommunity/manim/pull/1713): Exit the command line interface gracefully if no scene was chosen

- [#1652](https://github.com/ManimCommunity/manim/pull/1652): Refactored [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") and [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") to no longer inherit from the abstract base class `Container`

- Moved tests in `test_container.py` for `Container` that test [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") and [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to their own files.

- Corrected various instances of incorrectly passed keyword arguments, or unused keyword arguments.


- [#1693](https://github.com/ManimCommunity/manim/pull/1693): Made the default arrowhead size for [`Arrow3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Arrow3D.html#manim.mobject.three_d.three_dimensions.Arrow3D "manim.mobject.three_d.three_dimensions.Arrow3D") smaller

- [#1678](https://github.com/ManimCommunity/manim/pull/1678): Allow some rate functions to assume values outside of \[0, 1\]; introduce clamping decorators

- Fixed animations so that certain rate functions ( `running_start`, `wiggle`, `ease_in_back`, `ease_out_back`, `ease_in_out_back`, `ease_in_elastic`, `ease_out_elastic`, and `ease_out_elastic`) can go outside the range from 0 to 1.

- Fixed lag ratios so that they’re spaced out evenly within the time interval and the rate functions are applied to each animation individually, rather than having the rate function determine when the animation starts.

- Fixed faulty code for `ease_in_out_expo`, `ease_in_bounce`, `ease_out_bounce`, and `ease_in_out_bounce`.


- [#1649](https://github.com/ManimCommunity/manim/pull/1649): Made video file names in Jupyter notebook more readable

- [#1667](https://github.com/ManimCommunity/manim/pull/1667): Determine the default number of decimal places for [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine") labels automatically from the step size

As an example: If the step size is set to 0.5, labels will now show at least one decimal place.

- [#1608](https://github.com/ManimCommunity/manim/pull/1608): Color file paths in terminal; remove curly braces surrounding the file path in “Partial movie file written in…” messages

- [#1632](https://github.com/ManimCommunity/manim/pull/1632): OpenGL compatibility via metaclass: [`Group`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.8.0-changelog.html\#fixed-bugs "Link to this heading")

- [#1740](https://github.com/ManimCommunity/manim/pull/1740): Fix pillow to <8.3.0

- [#1729](https://github.com/ManimCommunity/manim/pull/1729): Fix bug when using [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") with the OpenGL renderer

- [#1675](https://github.com/ManimCommunity/manim/pull/1675): Fixed ignored fill and stroke colors for [`SVGMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject "manim.mobject.svg.svg_mobject.SVGMobject")

- [#1664](https://github.com/ManimCommunity/manim/pull/1664): Fixed accidental displacement in [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes") caused by `include_numbers` / `numbers_to_include`

- [#1670](https://github.com/ManimCommunity/manim/pull/1670): Fixed missing `numpy` import in OpenGL shader example

- [#1636](https://github.com/ManimCommunity/manim/pull/1636): Fixed bugs and added examples to methods and classes in [`manim.mobject.matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.html#module-manim.mobject.matrix "manim.mobject.matrix")

- [#1614](https://github.com/ManimCommunity/manim/pull/1614): Fix tick issues and improve tick placement for [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")

- [#1593](https://github.com/ManimCommunity/manim/pull/1593): Un-flip output of `get_frame()` when using the OpenGL renderer

- [#1619](https://github.com/ManimCommunity/manim/pull/1619): Fix output of automatically detected LaTeX errors

- [#1595](https://github.com/ManimCommunity/manim/pull/1595): Fixed a few CLI and rendering bugs

- Corrected issue where gifs were being logged with an incorrect extension

- Fixed issue where videos were output when format was set to png

- Added logging for png output

- Added precedence handling when the `write_to_movie` flag would conflict with `--format`

- Fixed issue that caused png image output to be ignored when caching was enabled


- [#1635](https://github.com/ManimCommunity/manim/pull/1635): Added missing numpy import for `manim.mobject.probability`

- [#1634](https://github.com/ManimCommunity/manim/pull/1634): Fixed OpenGL examples for MacOS

Renamed deprecated `gl_FragColor` to `fragColor`.


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.8.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#1732](https://github.com/ManimCommunity/manim/pull/1732): Remove reference to `--plugins` flag

- [#1734](https://github.com/ManimCommunity/manim/pull/1734): Fix inheritance graph background color

- [#1698](https://github.com/ManimCommunity/manim/pull/1698): Added an example for [`PMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject "manim.mobject.types.point_cloud_mobject.PMobject")

- [#1690](https://github.com/ManimCommunity/manim/pull/1690): Added an example for [`CoordinateSystem`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem "manim.mobject.graphing.coordinate_systems.CoordinateSystem")

- [#1510](https://github.com/ManimCommunity/manim/pull/1510): Add a tutorial for using [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") and [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")

- [#1685](https://github.com/ManimCommunity/manim/pull/1685): Added an example and parameter description for [`AnnularSector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.AnnularSector.html#manim.mobject.geometry.arc.AnnularSector "manim.mobject.geometry.arc.AnnularSector")

- [#1687](https://github.com/ManimCommunity/manim/pull/1687): Updated imports in `geometry.py` and added example to [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")

- [#1681](https://github.com/ManimCommunity/manim/pull/1681): Added an example for [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")

- [#1697](https://github.com/ManimCommunity/manim/pull/1697): Added an example for [`PGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PGroup.html#manim.mobject.types.point_cloud_mobject.PGroup "manim.mobject.types.point_cloud_mobject.PGroup")

- [#1594](https://github.com/ManimCommunity/manim/pull/1594): Several improvements to the documentation design and layout

- [#1696](https://github.com/ManimCommunity/manim/pull/1696): Added an example for [`DashedVMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.DashedVMobject.html#manim.mobject.types.vectorized_mobject.DashedVMobject "manim.mobject.types.vectorized_mobject.DashedVMobject")

- [#1637](https://github.com/ManimCommunity/manim/pull/1637): Added an example for [`FunctionGraph`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.FunctionGraph.html#manim.mobject.graphing.functions.FunctionGraph "manim.mobject.graphing.functions.FunctionGraph")

- [#1626](https://github.com/ManimCommunity/manim/pull/1626): Added an example for [`Prism`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism "manim.mobject.three_d.three_dimensions.Prism")

- [#1712](https://github.com/ManimCommunity/manim/pull/1712): Added a second example for [`DoubleArrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DoubleArrow.html#manim.mobject.geometry.line.DoubleArrow "manim.mobject.geometry.line.DoubleArrow")

- [#1710](https://github.com/ManimCommunity/manim/pull/1710): Update copyright year in documentation to 2020-2021

- [#1708](https://github.com/ManimCommunity/manim/pull/1708): Fixed link to interactive example notebook

- [#1657](https://github.com/ManimCommunity/manim/pull/1657): Added an example for `ParametricSurface`

- [#1642](https://github.com/ManimCommunity/manim/pull/1642): Added examples and docstrings for [`BarChart`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.probability.BarChart.html#manim.mobject.graphing.probability.BarChart "manim.mobject.graphing.probability.BarChart")

- [#1700](https://github.com/ManimCommunity/manim/pull/1700): Added an example for [`scale()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale "manim.mobject.mobject.Mobject.scale")

- [#1689](https://github.com/ManimCommunity/manim/pull/1689): Added an example for [`SurroundingRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html#manim.mobject.geometry.shape_matchers.SurroundingRectangle "manim.mobject.geometry.shape_matchers.SurroundingRectangle")

- [#1627](https://github.com/ManimCommunity/manim/pull/1627): Added an example for [`Sphere`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Sphere.html#manim.mobject.three_d.three_dimensions.Sphere "manim.mobject.three_d.three_dimensions.Sphere")

- [#1569](https://github.com/ManimCommunity/manim/pull/1569): Added example to demonstrate differences between [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform") and [`ReplacementTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ReplacementTransform.html#manim.animation.transform.ReplacementTransform "manim.animation.transform.ReplacementTransform")

- [#1647](https://github.com/ManimCommunity/manim/pull/1647): Added an example for [`Sector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Sector.html#manim.mobject.geometry.arc.Sector "manim.mobject.geometry.arc.Sector")

- [#1673](https://github.com/ManimCommunity/manim/pull/1673): Updated documentation examples for [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") and [`MarkupText`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText"): set `weight=BOLD` instead of `style`

- [#1650](https://github.com/ManimCommunity/manim/pull/1650): Added an example for [`ArcBetweenPoints`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcBetweenPoints.html#manim.mobject.geometry.arc.ArcBetweenPoints "manim.mobject.geometry.arc.ArcBetweenPoints")

- [#1628](https://github.com/ManimCommunity/manim/pull/1628): Added an example for [`NumberPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane")

- [#1646](https://github.com/ManimCommunity/manim/pull/1646): Added an example for [`Underline`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.Underline.html#manim.mobject.geometry.shape_matchers.Underline "manim.mobject.geometry.shape_matchers.Underline")

- [#1659](https://github.com/ManimCommunity/manim/pull/1659): Added more details to the Google Colab installation instructions

- [#1658](https://github.com/ManimCommunity/manim/pull/1658): Updated python requirement in the documentation

- [#1639](https://github.com/ManimCommunity/manim/pull/1639): Added an example for [`SampleSpace`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.probability.SampleSpace.html#manim.mobject.graphing.probability.SampleSpace "manim.mobject.graphing.probability.SampleSpace")

- [#1640](https://github.com/ManimCommunity/manim/pull/1640): Added an example for [`Point`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Point.html#manim.mobject.types.point_cloud_mobject.Point "manim.mobject.types.point_cloud_mobject.Point")

- [#1643](https://github.com/ManimCommunity/manim/pull/1643): Fixed `RightArcAngleExample` for [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle") in documentation

- [#1617](https://github.com/ManimCommunity/manim/pull/1617): Visually improved an example in our tutorial

- [#1641](https://github.com/ManimCommunity/manim/pull/1641): Added an example for [`ComplexPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane "manim.mobject.graphing.coordinate_systems.ComplexPlane")

- [#1644](https://github.com/ManimCommunity/manim/pull/1644): Added an example for [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "manim.mobject.geometry.shape_matchers.BackgroundRectangle")

- [#1633](https://github.com/ManimCommunity/manim/pull/1633): Added an example for [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer")

- [#1630](https://github.com/ManimCommunity/manim/pull/1630): Added an example for [`Arc`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc")

- [#1631](https://github.com/ManimCommunity/manim/pull/1631): Added an example for [`BulletedList`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.BulletedList.html#manim.mobject.text.tex_mobject.BulletedList "manim.mobject.text.tex_mobject.BulletedList")

- [#1620](https://github.com/ManimCommunity/manim/pull/1620): Fixed reference to command line interface help command


### Changes to our development infrastructure [¶](https://docs.manim.community/en/stable/changelog/0.8.0-changelog.html\#changes-to-our-development-infrastructure "Link to this heading")

- [#1623](https://github.com/ManimCommunity/manim/pull/1623): CI: branch rename: master -> main

- [#1621](https://github.com/ManimCommunity/manim/pull/1621): Revert default template and add new templates

- [#1573](https://github.com/ManimCommunity/manim/pull/1573): PR template for the manim hackathon


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.8.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#1720](https://github.com/ManimCommunity/manim/pull/1720): Renamed incorrect references of `master` to `main`

- [#1692](https://github.com/ManimCommunity/manim/pull/1692): Removed redundant warning in CLI parsing

- [#1651](https://github.com/ManimCommunity/manim/pull/1651): Small code cleanup for [`Polygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram")

- [#1610](https://github.com/ManimCommunity/manim/pull/1610): Changed one image extension to lowercase letters


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.8.0-changelog.html\#new-releases "Link to this heading")

- [#1738](https://github.com/ManimCommunity/manim/pull/1738): Preparation for v0.8.0: added changelog and bumped version number