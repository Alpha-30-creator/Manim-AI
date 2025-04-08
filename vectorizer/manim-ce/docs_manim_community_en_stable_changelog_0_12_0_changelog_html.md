ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# v0.12.0 [¶](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html\#v0-12-0 "Link to this heading")

Date:

November 02, 2021

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html\#contributors "Link to this heading")

A total of 40 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Anima. +

- Arcstur +

- Benjamin Hackl

- Christopher Besch

- Darylgolden

- David Yang +

- Dhananjay Goratela +

- Ethan Rooke +

- Eugene Chung +

- GameDungeon

- Gustav-Rixon +

- Jan-Hendrik Müller

- Josiah Winslow +

- Laith Bahodi

- Martmists +

- Michael Hill +

- Naveen M K

- Nick +

- NotWearingPants +

- Peeter Joot +

- Ryan McCauley

- Viicos +

- heitor +

- icedcoffeeee

- kieran-pringle +

- Виктор Виктор +


The patches included in this release have been reviewed by
the following contributors.

- Alex Lembcke

- Anima.

- Benjamin Hackl

- Christopher Besch

- Darylgolden

- David Yang

- Dhananjay Goratela

- Ethan Rooke

- Eugene Chung

- Gustav-Rixon

- Hugues Devimeux

- Jan-Hendrik Müller

- Jason Villanueva

- Laith Bahodi

- Mysaa

- Naveen M K

- Nick

- Oliver

- Ryan McCauley

- Viicos

- icedcoffeeee

- kieran-pringle


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 52 pull requests were merged for this release.

### Highlights [¶](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html\#highlights "Link to this heading")

- [#1812](https://github.com/ManimCommunity/manim/pull/1812): Implemented logarithmic scaling for [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine") / [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes")

This implements scaling bases that can be passed to the `scaling` keyword
argument of [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine"). See [`LogBase`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LogBase.html#manim.mobject.graphing.scale.LogBase "manim.mobject.graphing.scale.LogBase") (for a logarithmic scale) and
[`LinearBase`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LinearBase.html#manim.mobject.graphing.scale.LinearBase "manim.mobject.graphing.scale.LinearBase") (for the default scale) for more details and examples.

- [#2152](https://github.com/ManimCommunity/manim/pull/2152): Introduced API for scene sections via [`Scene.next_section()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.next_section "manim.scene.scene.Scene.next_section")

Sections divide a scene into multiple parts, resulting in multiple output videos (when using the `--save_sections` flag).
The cuts between two sections are defined by the user in the [`construct()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct") method.
Each section has an optional name and type, which can be used by a plugin ( [see an example](https://github.com/ManimEditorProject/manim_editor)).
You can skip rendering specific sections with the `skip_animations` keyword argument.


### Deprecated classes and functions [¶](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html\#deprecated-classes-and-functions "Link to this heading")

- [#1926](https://github.com/ManimCommunity/manim/pull/1926): OpenGL: changed `submobjects` to be a property

- [#2245](https://github.com/ManimCommunity/manim/pull/2245): Removed deprecated method `get_center_point` and parameters `azimuth_label_scale`, `number_scale_value`, `label_scale`, `scale_factor`, `size`, `x_min`, `x_max`, `delta_x`, `y_min`, `y_max`, `delta_y`

- [#2187](https://github.com/ManimCommunity/manim/pull/2187): Renamed `get_graph` and its variants to [`plot()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot "manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot")

- [#2065](https://github.com/ManimCommunity/manim/pull/2065): Deprecated `FullScreenFadeRectangle` and `PictureInPictureFrame`


### New features [¶](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html\#new-features "Link to this heading")

- [#2025](https://github.com/ManimCommunity/manim/pull/2025): Implemented [`CoordinateSystem.input_to_graph_coords()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.input_to_graph_coords "manim.mobject.graphing.coordinate_systems.CoordinateSystem.input_to_graph_coords") and fixed [`CoordinateSystem.angle_of_tangent()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.angle_of_tangent "manim.mobject.graphing.coordinate_systems.CoordinateSystem.angle_of_tangent")

- [#2151](https://github.com/ManimCommunity/manim/pull/2151): Added option to set the input file from a config file

- [#2128](https://github.com/ManimCommunity/manim/pull/2128): Added keyword arguments `match_center`, `match_width` etc. to [`Mobject.become()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.become "manim.mobject.mobject.Mobject.become")

- [#2162](https://github.com/ManimCommunity/manim/pull/2162): Implemented [`MovingCamera.auto_zoom()`](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.auto_zoom "manim.camera.moving_camera.MovingCamera.auto_zoom") for automatically zooming onto specified mobjects

- [#2236](https://github.com/ManimCommunity/manim/pull/2236): Added `skip_animations` argument to [`Scene.next_section()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.next_section "manim.scene.scene.Scene.next_section")

- [#2196](https://github.com/ManimCommunity/manim/pull/2196): Implemented [`Line3D.parallel_to()`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.parallel_to "manim.mobject.three_d.three_dimensions.Line3D.parallel_to") and [`Line3D.perpendicular_to()`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.perpendicular_to "manim.mobject.three_d.three_dimensions.Line3D.perpendicular_to")


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html\#enhancements "Link to this heading")

- [#2138](https://github.com/ManimCommunity/manim/pull/2138): Fixed example for [`coordinate_label()`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector.coordinate_label "manim.mobject.geometry.line.Vector.coordinate_label") and added more customization for [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

- Additional keyword arguments for [`coordinate_label()`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector.coordinate_label "manim.mobject.geometry.line.Vector.coordinate_label") are passed to the constructed matrix.

- [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix") now accepts a `bracket_config` keyword argument.


- [#2139](https://github.com/ManimCommunity/manim/pull/2139): Changed the color of [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine") from `LIGHT_GREY` to `WHITE`

- [#2157](https://github.com/ManimCommunity/manim/pull/2157): Added [`CoordinateSystem.plot_polar_graph()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_polar_graph "manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot_polar_graph")

- [#2243](https://github.com/ManimCommunity/manim/pull/2243): Fixed wasteful recursion in [`Mobject.get_merged_array()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_merged_array "manim.mobject.mobject.Mobject.get_merged_array")

- [#2205](https://github.com/ManimCommunity/manim/pull/2205): Improved last frame output handling for the OpenGL renderer

- [#2172](https://github.com/ManimCommunity/manim/pull/2172): Added `should_render` attribute to disable rendering mobjects

- [#2182](https://github.com/ManimCommunity/manim/pull/2182): Changed the default width of videos in Jupyter notebooks to 60%


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html\#fixed-bugs "Link to this heading")

- [#2244](https://github.com/ManimCommunity/manim/pull/2244): Fixed [`CoordinateSystem.get_area()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_area "manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_area") when using few plot points and a boundary graph

- [#2232](https://github.com/ManimCommunity/manim/pull/2232): Fixed [`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph") stopping to update after animating additions/deletions of vertices or edges

- [#2142](https://github.com/ManimCommunity/manim/pull/2142): Fixed issue with duplicates in OpenGL family and added tests

- [#2168](https://github.com/ManimCommunity/manim/pull/2168): Fixed order of return values of [`space_ops.cartesian_to_spherical()`](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.cartesian_to_spherical "manim.utils.space_ops.cartesian_to_spherical")

- [#2160](https://github.com/ManimCommunity/manim/pull/2160): Made projection shaders compatible with [`StreamLines`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#manim.mobject.vector_field.StreamLines "manim.mobject.vector_field.StreamLines")

- [#2140](https://github.com/ManimCommunity/manim/pull/2140): Fixed passing color lists to [`Mobject.set_color()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_color "manim.mobject.mobject.Mobject.set_color") for the OpenGL renderer

- [#2211](https://github.com/ManimCommunity/manim/pull/2211): Fixed animations not respecting the specified rate function

- [#2161](https://github.com/ManimCommunity/manim/pull/2161): Fixed `IndexOutOfBoundsError` in TeX logging

- [#2148](https://github.com/ManimCommunity/manim/pull/2148): Fixed [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow") tip disorientation with [`Line.put_start_and_end_on()`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line.put_start_and_end_on "manim.mobject.geometry.line.Line.put_start_and_end_on")

- [#2192](https://github.com/ManimCommunity/manim/pull/2192): Fixed `svg_path.string_to_numbers()` sometimes returning strings

- [#2185](https://github.com/ManimCommunity/manim/pull/2185): Fixed type mismatch for height and width parameters of [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#2228](https://github.com/ManimCommunity/manim/pull/2228): Added a new boolean operation example to the gallery

- [#2239](https://github.com/ManimCommunity/manim/pull/2239): Removed erroneous raw string from text tutorial

- [#2184](https://github.com/ManimCommunity/manim/pull/2184): Moved comments in [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") to documentation

- [#2217](https://github.com/ManimCommunity/manim/pull/2217): Removed superfluous dots in documentation of [`Section`](https://docs.manim.community/en/stable/reference/manim.scene.section.Section.html#manim.scene.section.Section "manim.scene.section.Section")

- [#2215](https://github.com/ManimCommunity/manim/pull/2215): Fixed typo in docstring of [`ThreeDAxes.get_z_axis_label()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ThreeDAxes.html#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label")

- [#2212](https://github.com/ManimCommunity/manim/pull/2212): Fixed Documentation for Sections

- [#2201](https://github.com/ManimCommunity/manim/pull/2201): Fixed a typo in the documentation

- [#2165](https://github.com/ManimCommunity/manim/pull/2165): Added Crowdin configuration and changed source files to `.pot` format

- [#2130](https://github.com/ManimCommunity/manim/pull/2130): Transferred troubleshooting installation related snippets from Discord to the documentation

- [#2176](https://github.com/ManimCommunity/manim/pull/2176): Modified [`Mobject.set_default()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_default "manim.mobject.mobject.Mobject.set_default") example to prevent leaking across the docs


### Changes concerning the testing system [¶](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html\#changes-concerning-the-testing-system "Link to this heading")

- [#2197](https://github.com/ManimCommunity/manim/pull/2197): Added tests for resolution flag

- [#2146](https://github.com/ManimCommunity/manim/pull/2146): Increased test coverage for OpenGL renderer


### Changes to our development infrastructure [¶](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html\#changes-to-our-development-infrastructure "Link to this heading")

- [#2191](https://github.com/ManimCommunity/manim/pull/2191): Removed `add-trailing-comma` pre-commit hook


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#2136](https://github.com/ManimCommunity/manim/pull/2136): Added type hints to all colors

- [#2220](https://github.com/ManimCommunity/manim/pull/2220): Cleanup: let `Scene.renderer.time` return something that makes sense

- [#2222](https://github.com/ManimCommunity/manim/pull/2222): Updated Classifiers in `pyproject.toml`: removed Python 3.6, added Python 3.9

- [#2213](https://github.com/ManimCommunity/manim/pull/2213): Removed redundant `partial_movie_files` parameter in [`SceneFileWriter.combine_to_movie()`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.combine_to_movie "manim.scene.scene_file_writer.SceneFileWriter.combine_to_movie")

- [#2200](https://github.com/ManimCommunity/manim/pull/2200): Addressed some maintenance TODOs

- Changed an Exception to ValueError

- Fixed `MappingCamera.points_to_pixel_coords()` by adding the `mobject` argument of the parent

- Rounded up width in [`SplitScreenCamera`](https://docs.manim.community/en/stable/reference/manim.camera.mapping_camera.SplitScreenCamera.html#manim.camera.mapping_camera.SplitScreenCamera "manim.camera.mapping_camera.SplitScreenCamera")

- Added docstring to [`Camera.capture_mobject()`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.capture_mobject "manim.camera.camera.Camera.capture_mobject")


- [#2194](https://github.com/ManimCommunity/manim/pull/2194): Added type hints to [`utils.images`](https://docs.manim.community/en/stable/reference/manim.utils.images.html#module-manim.utils.images "manim.utils.images")

- [#2171](https://github.com/ManimCommunity/manim/pull/2171): Added type hints to [`utils.ipython_magic`](https://docs.manim.community/en/stable/reference/manim.utils.ipython_magic.html#module-manim.utils.ipython_magic "manim.utils.ipython_magic")

- [#2164](https://github.com/ManimCommunity/manim/pull/2164): Improved readability of regular expression


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.12.0-changelog.html\#new-releases "Link to this heading")

- [#2247](https://github.com/ManimCommunity/manim/pull/2247): Prepared new release `v0.12.0`