ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# v0.11.0 [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#v0-11-0 "Link to this heading")

Date:

October 02, 2021

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#contributors "Link to this heading")

A total of 31 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Aathish Sivasubrahmanian

- Benjamin Hackl

- Charlie +

- Christopher Besch +

- Darylgolden

- Evan Boehs +

- GameDungeon

- Hugues Devimeux

- Jerónimo Squartini

- Laith Bahodi

- Meredith Espinosa +

- Mysaa

- Naveen M K

- Nicolai Weitkemper +

- Oliver

- Ryan McCauley

- Tim +

- icedcoffeeee

- imadjamil +

- leleogere +

- Максим Заякин +


The patches included in this release have been reviewed by
the following contributors.

- Aathish Sivasubrahmanian

- Benjamin Hackl

- Charlie

- Darylgolden

- Evan Boehs

- GameDungeon

- Hugues Devimeux

- Jan-Hendrik Müller

- Jason Villanueva

- Laith Bahodi

- Mark Miller

- Mysaa

- Naveen M K

- Nicolai Weitkemper

- Oliver

- Raghav Goel

- Ryan McCauley

- Skaft

- friedkeenan

- icedcoffeeee

- leleogere


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 55 pull requests were merged for this release.

### Breaking changes [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#breaking-changes "Link to this heading")

- [#1990](https://github.com/ManimCommunity/manim/pull/1990): Changed and improved the implementation of [`CoordinateSystem.get_area()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_area "manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_area") to work without Riemann rectangles

This changes how [`CoordinateSystem.get_area()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_area "manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_area") is implemented. To mimic the old behavior (tiny Riemann rectangles), use [`CoordinateSystem.get_riemann_rectangles()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_riemann_rectangles "manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_riemann_rectangles") with a small value for `dx`.

- [#2095](https://github.com/ManimCommunity/manim/pull/2095): Changed angles for polar coordinates to use math convention

This PR switches the parameter names `phi` and `theta` in `cartesian_to_spherical()` and `spherical_to_cartesian()` to align with the [usual definition in mathematics](https://user-images.githubusercontent.com/83535735/131709630-87290522-7747-4b21-9411-dd3d35ebaf0f.png).


### Highlights [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#highlights "Link to this heading")

- [#2094](https://github.com/ManimCommunity/manim/pull/2094): Implemented [`ImplicitFunction`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ImplicitFunction.html#manim.mobject.graphing.functions.ImplicitFunction "manim.mobject.graphing.functions.ImplicitFunction") and `CoordinateSystem.get_implicit_curve()` for plotting implicit curves

An [`ImplicitFunction`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ImplicitFunction.html#manim.mobject.graphing.functions.ImplicitFunction "manim.mobject.graphing.functions.ImplicitFunction") that plots the points (x,y) which satisfy some equation f(x,y)=0.

- [#2075](https://github.com/ManimCommunity/manim/pull/2075): Implemented [`Mobject.set_default()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_default "manim.mobject.mobject.Mobject.set_default"), a mechanism for changing default values of keyword arguments

- [#1998](https://github.com/ManimCommunity/manim/pull/1998): Added support for Boolean Operations on VMobjects

This PR introduces boolean operations for [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"); see details and examples at
[`Union`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Union.html#manim.mobject.geometry.boolean_ops.Union "manim.mobject.geometry.boolean_ops.Union"), [`Difference`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html#manim.mobject.geometry.boolean_ops.Difference "manim.mobject.geometry.boolean_ops.Difference"), [`Intersection`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Intersection.html#manim.mobject.geometry.boolean_ops.Intersection "manim.mobject.geometry.boolean_ops.Intersection") and [`Exclusion`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Exclusion.html#manim.mobject.geometry.boolean_ops.Exclusion "manim.mobject.geometry.boolean_ops.Exclusion").


### Deprecated classes and functions [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#deprecated-classes-and-functions "Link to this heading")

- [#2123](https://github.com/ManimCommunity/manim/pull/2123): Renamed `distance` parameter of [`ThreeDScene`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene "manim.scene.three_d_scene.ThreeDScene") and [`ThreeDCamera`](https://docs.manim.community/en/stable/reference/manim.camera.three_d_camera.ThreeDCamera.html#manim.camera.three_d_camera.ThreeDCamera "manim.camera.three_d_camera.ThreeDCamera") to `focal_distance`

- [#2102](https://github.com/ManimCommunity/manim/pull/2102): Deprecated `SampleSpaceScene` and `ReconfigurableScene`

- [#2061](https://github.com/ManimCommunity/manim/pull/2061): Removed deprecated `u_min`, `u_max`, `v_min`, `v_max` in [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface")

- [#2024](https://github.com/ManimCommunity/manim/pull/2024): Deprecated redundant methods `Mobject.rotate_in_place()`, `Mobject.scale_in_place()`, `Mobject.scale_about_point()`

- [#1991](https://github.com/ManimCommunity/manim/pull/1991): Deprecated `VMobject.get_points()`


### New features [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#new-features "Link to this heading")

- [#2118](https://github.com/ManimCommunity/manim/pull/2118): Added 3D support for [`ArrowVectorField`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#manim.mobject.vector_field.ArrowVectorField "manim.mobject.vector_field.ArrowVectorField") and [`StreamLines`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#manim.mobject.vector_field.StreamLines "manim.mobject.vector_field.StreamLines")

- [#1469](https://github.com/ManimCommunity/manim/pull/1469): Added [`VMobject.proportion_from_point()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.proportion_from_point "manim.mobject.types.vectorized_mobject.VMobject.proportion_from_point") to measure the proportion of points along a Bezier curve


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#enhancements "Link to this heading")

- [#2111](https://github.com/ManimCommunity/manim/pull/2111): Improved setting of OpenGL colors

- [#2113](https://github.com/ManimCommunity/manim/pull/2113): Added OpenGL compatibility to [`ThreeDScene.begin_ambient_camera_rotation()`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.begin_ambient_camera_rotation "manim.scene.three_d_scene.ThreeDScene.begin_ambient_camera_rotation") and [`ThreeDScene.move_camera()`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.move_camera "manim.scene.three_d_scene.ThreeDScene.move_camera")

- [#2016](https://github.com/ManimCommunity/manim/pull/2016): Added OpenGL support for `boolean_ops`

- [#2084](https://github.com/ManimCommunity/manim/pull/2084): Added `get_highlighted_cell()` and fixed `add_highlighted_cell()`

- [#2013](https://github.com/ManimCommunity/manim/pull/2013): Removed unnecessary check in [`TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")

- [#1971](https://github.com/ManimCommunity/manim/pull/1971): Added OpenGL support for [`StreamLines`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#manim.mobject.vector_field.StreamLines "manim.mobject.vector_field.StreamLines")

- [#2041](https://github.com/ManimCommunity/manim/pull/2041): Added config option to enable OpenGL wireframe for debugging


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#fixed-bugs "Link to this heading")

- [#2070](https://github.com/ManimCommunity/manim/pull/2070): Fixed `get_frame()` when window is created

- [#2071](https://github.com/ManimCommunity/manim/pull/2071): Fixed `AnimationGroup` OpenGL compatibility

- [#2108](https://github.com/ManimCommunity/manim/pull/2108): Fixed swapped axis step values in [`NumberPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane")

- [#2072](https://github.com/ManimCommunity/manim/pull/2072): Added OpenGL compatibility for [`Cube`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cube.html#manim.mobject.three_d.three_dimensions.Cube "manim.mobject.three_d.three_dimensions.Cube").

- [#2060](https://github.com/ManimCommunity/manim/pull/2060): Fixed OpenGL compatibility issue for meth:~Line.set\_opacity

- [#2037](https://github.com/ManimCommunity/manim/pull/2037): Fixed return value of `apply_complex_function()`

- [#2039](https://github.com/ManimCommunity/manim/pull/2039): Added OpenGL compatibility for `add_bases()`.

- [#2066](https://github.com/ManimCommunity/manim/pull/2066): Fixed error raised by logging when cache is full

- [#2026](https://github.com/ManimCommunity/manim/pull/2026): Fixed OpenGL shift animation for [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")

- [#2028](https://github.com/ManimCommunity/manim/pull/2028): Fixed OpenGL overriding SVG fill color

- [#2043](https://github.com/ManimCommunity/manim/pull/2043): Fixed bug where [`NumberLine.add_labels()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine.add_labels "manim.mobject.graphing.number_line.NumberLine.add_labels") cannot accept non-mobject labels

- [#2011](https://github.com/ManimCommunity/manim/pull/2011): Fixed `-a` flag for OpenGL rendering

- [#1994](https://github.com/ManimCommunity/manim/pull/1994): Fix [`input_to_graph_point()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.input_to_graph_point "manim.mobject.graphing.coordinate_systems.CoordinateSystem.input_to_graph_point") when passing a line graph (from `Axes.get_line_graph()`)

- [#2017](https://github.com/ManimCommunity/manim/pull/2017): Avoided using deprecated `get_points` method and fixed `OpenGLPMPoint` color


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#2131](https://github.com/ManimCommunity/manim/pull/2131): Copyedited the configuration tutorial in the documentation

- [#2120](https://github.com/ManimCommunity/manim/pull/2120): Changed `manim_directive` to use a clean configuration via `tempconfig`

- [#2122](https://github.com/ManimCommunity/manim/pull/2122): Fixed broken links in inheritance graphs by moving them to `reference.rst`

- [#2115](https://github.com/ManimCommunity/manim/pull/2115): Improved docstring of [`PMobject.add_points()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.add_points "manim.mobject.types.point_cloud_mobject.PMobject.add_points")

- [#2116](https://github.com/ManimCommunity/manim/pull/2116): Made type hint for `line_spacing` argument of [`Paragraph`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph") more accurate

- [#2117](https://github.com/ManimCommunity/manim/pull/2117): Changed the way the background color was set in a documentation example to avoid leaking the setting to other examples

- [#2101](https://github.com/ManimCommunity/manim/pull/2101): Added note that translation process is not ready

- [#2055](https://github.com/ManimCommunity/manim/pull/2055): Fixed parameter types of `Graph.add_edges()` and `Graph.add_vertices()`

- [#862](https://github.com/ManimCommunity/manim/pull/862): Prepared documentation for translation (still work in progress)

- [#2035](https://github.com/ManimCommunity/manim/pull/2035): Fixed broken link in README

- [#2020](https://github.com/ManimCommunity/manim/pull/2020): Corrected paths to user-wide configuration files for MacOS and Linux


### Changes concerning the testing system [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#changes-concerning-the-testing-system "Link to this heading")

- [#2008](https://github.com/ManimCommunity/manim/pull/2008): Reuse CLI flag tests for OpenGL

- [#2080](https://github.com/ManimCommunity/manim/pull/2080): Reused [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") tests for `OpenGLMobject`


### Changes to our development infrastructure [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#changes-to-our-development-infrastructure "Link to this heading")

- [#2004](https://github.com/ManimCommunity/manim/pull/2004): Cancel previous workflows in the same branch in Github Actions


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#2050](https://github.com/ManimCommunity/manim/pull/2050): Make colour aliases IDE-friendly

- [#2126](https://github.com/ManimCommunity/manim/pull/2126): Fixed whitespace in info message issued by [`SceneFileWriter.clean_cache()`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.clean_cache "manim.scene.scene_file_writer.SceneFileWriter.clean_cache")

- [#2124](https://github.com/ManimCommunity/manim/pull/2124): Upgraded several dependencies (in particular: `skia-pathops`)

- [#2001](https://github.com/ManimCommunity/manim/pull/2001): Fixed several warnings issued by LGTM

- [#2064](https://github.com/ManimCommunity/manim/pull/2064): Removed duplicate insert shader directory

- [#2027](https://github.com/ManimCommunity/manim/pull/2027): Improved wording in info message issued by [`SceneFileWriter.clean_cache()`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.clean_cache "manim.scene.scene_file_writer.SceneFileWriter.clean_cache")

- [#1968](https://github.com/ManimCommunity/manim/pull/1968): Sharpened Flake8 configuration and fixed resulting warnings


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.11.0-changelog.html\#new-releases "Link to this heading")

- [#2114](https://github.com/ManimCommunity/manim/pull/2114): Prepared new release, `v0.11.0`