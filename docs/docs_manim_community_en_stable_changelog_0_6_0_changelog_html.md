ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# v0.6.0 [¶](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html\#v0-6-0 "Link to this heading")

Date:

May 02, 2021

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html\#contributors "Link to this heading")

A total of 40 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Abel Aebker

- Abhijith Muthyala

- Adam Ryczkowski +

- Alex Lembcke +

- Anton Ballmaier

- Aron

- Benjamin Hackl

- Darylgolden

- Deniz Hasler +

- Devin Neal

- Elisha Hollander +

- Erik Tastepe +

- Jan-Hendrik Müller

- Jason Villanueva

- Laith Bahodi

- Mark Miller

- Mohammad Al-Fetyani

- Naveen M K

- Newell Jensen +

- Nidhal Baccouri +

- Nikhil Garuda +

- Peilonrayz +

- Raghav Goel

- Ricky Chon +

- friedkeenan

- kamilczerwinski22 +

- sparshg


The patches included in this release have been reviewed by
the following contributors.

- Aathish Sivasubrahmanian

- Abel Aebker

- Abhijith Muthyala

- Adam Ryczkowski

- Alex Lembcke

- Anton Ballmaier

- Aron

- Benjamin Hackl

- Darylgolden

- Deniz Hasler

- Devin Neal

- Elisha Hollander

- GameDungeon

- Hugues Devimeux

- Jan-Hendrik Müller

- Jason Villanueva

- KingWampy

- Laith Bahodi

- Mark Miller

- Mohammad Al-Fetyani

- Naveen M K

- Nidhal Baccouri

- Nikhil Garuda

- Oliver

- Philipp Imhof

- Raghav Goel

- Ricky Chon

- friedkeenan

- sparshg


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 112 pull requests were merged for this release.

### Breaking changes [¶](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html\#breaking-changes "Link to this heading")

- [#1347](https://github.com/ManimCommunity/manim/pull/1347): Restructure vector\_field module and add documentation

:class\`~.VectorField\` is renamed to [`ArrowVectorField`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#manim.mobject.vector_field.ArrowVectorField "manim.mobject.vector_field.ArrowVectorField") and a new class [`VectorField`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField") is added as a superclass for [`ArrowVectorField`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#manim.mobject.vector_field.ArrowVectorField "manim.mobject.vector_field.ArrowVectorField") and [`StreamLines`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#manim.mobject.vector_field.StreamLines "manim.mobject.vector_field.StreamLines"). `AnimatedStreamLines` is removed. It’s functionality is moved to [`StreamLines`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#manim.mobject.vector_field.StreamLines "manim.mobject.vector_field.StreamLines"). Added a lot of new options when working with vector fields. [`ShowPassingFlashWithThinningStrokeWidth`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth.html#manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth "manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth") was moved to the indication module.

- [#1161](https://github.com/ManimCommunity/manim/pull/1161): Upgrades to CoordinateSystem and graphing.

Breaking changes were introduced to [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes"), [`ThreeDAxes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ThreeDAxes.html#manim.mobject.graphing.coordinate_systems.ThreeDAxes "manim.mobject.graphing.coordinate_systems.ThreeDAxes"), [`NumberPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane") and [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")
All the above now use lists to construct their ranges as opposed to explicitly defining these values. x\_range has replaced x\_min, x\_max and defining the step is much easier with x\_step –\> `x_range` : `[x_min, x_max, x_step]`. There were also many upgrades to these classes which improve their functionality and appearance.



`NumberLineOld` was introduced to continue support for `GraphScene`, although we are moving away from GraphScene and intend to deprecate it in a future release.

- [#1013](https://github.com/ManimCommunity/manim/pull/1013): Refactored the Command Line Interface to use Click instead of Argparse

This change breaks the CLI API to organize the structure of Manim Community’s commands, options, and arguments.



To be more in line with POSIX compliant CLI conventions, options for commands are given _BEFORE_ their arguments.
In Argparse: `manim basic.py -p -ql`
With Click: `manim -p -ql basic.py`



Although this is primarily a refactor and most of the common options are still there, some options have been added/removed. Use the `manim` command’s `--help` option, or simply run the command without providing options/arguments to view the help page with the full list of subcommands/options/arguments.



- Added a `--fps`/ `--frame_rate` option which allows for custom fps that don’t have to be integer (i.e. 29.97, 23.98, etc.). Users no longer have to specify the FPS from within a config file. Additionally, the `--webgl_renderer_fps` option has been removed. Use `--fps` or `--frame_rate` instead.

- Added a `--renderer` option which you can use to select your choice of renderer (e.g. `--renderer=opengl`). There are currently _THREE_ renderers to choose from!

- Removed the `--background_color` option. Reassigned the `--background_color` option’s shorthand `-c` to `--config_file`.

- Removed the `--leave_progress_bars` option. Use `--progress_bars=leave` instead.

- Removed the deprecated render quality flags, in particular: `-l`, `-m`, `-h`, `-k`.

- Removed the `--sound` option. It lost support long ago with the removal of SoX.


### Deprecated classes and functions [¶](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html\#deprecated-classes-and-functions "Link to this heading")

- [#1431](https://github.com/ManimCommunity/manim/pull/1431): Fix CLI bugs

- Fixed conflict with `-f` which was previously assigned to both `--show_in_file_browser` and `--format` by removing `-f` from `--format`. A warning is issued that `-f` will soon move to `--format`.

- Added back in flags to render the files as gif/last frame. Deprecated them in favor of `--format`.

- Fixed the broken `--output_file`/ `-o` option.

- Fixed an issue where the `-qh` quality option was interpreted as `-q` `-h`, prompting the help page.


- [#1354](https://github.com/ManimCommunity/manim/pull/1354): Refactored a few functions in space\_ops.py, deprecated `angle_between()`

- [#1370](https://github.com/ManimCommunity/manim/pull/1370): Remove TexMobject and TextMobject

TexMobject and TextMobject have been deprecated for a while, they are now fully removed. Use Tex or MathTex instead.

- [#1349](https://github.com/ManimCommunity/manim/pull/1349): Removed the deprecated `SmallDot` mobject

- [#1259](https://github.com/ManimCommunity/manim/pull/1259): Removed deprecated CairoText class


### New features [¶](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html\#new-features "Link to this heading")

- [#1386](https://github.com/ManimCommunity/manim/pull/1386): Implement utility methods for adding/removing vertices and edges of graphs; allow custom mobjects as vertices

- [#1385](https://github.com/ManimCommunity/manim/pull/1385): Added `get_line_graph()` for plotting a line graph

Added `get_line_graph()` that returns a line graph from lists of points along x, y and z (optional) axes.

- [#1381](https://github.com/ManimCommunity/manim/pull/1381): Hot reloading for the OpenGL renderer

Rerun scene when the input file is modified

- [#1383](https://github.com/ManimCommunity/manim/pull/1383): Overhaul of the [`indication`](https://docs.manim.community/en/stable/reference/manim.animation.indication.html#module-manim.animation.indication "manim.animation.indication") module interfaces

- Added class Circumscribe combining functionality of CircleIndicate, AnimationOnSurroundingRectangle, ShowPassingFlashAround, ShowCreationThenDestructionAround, ShowCreationThenFadeAround, which have all been deprecated.

- Changes to Flash: flash\_radius parameter now defines inner radius of the animation. Added new parameter time\_width.

- ShowCreationThenDestruction has been deprecated in favor of ShowPassingFlash

- Changes to ApplyWave: New implementation giving more flexibility with new parameters wave\_func, time\_width and\`ripples\`

- Renamed WiggleOutThenIn to Wiggle (WiggleOutThenIn has been deprecated)

- Added documentation and examples to all the above

- Other minor enhancements and bug-fixes


- [#1348](https://github.com/ManimCommunity/manim/pull/1348): Added [`Polyhedron`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Polyhedron.html#manim.mobject.three_d.polyhedra.Polyhedron "manim.mobject.three_d.polyhedra.Polyhedron"), and platonic solids [`Tetrahedron`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html#manim.mobject.three_d.polyhedra.Tetrahedron "manim.mobject.three_d.polyhedra.Tetrahedron"), [`Octahedron`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Octahedron.html#manim.mobject.three_d.polyhedra.Octahedron "manim.mobject.three_d.polyhedra.Octahedron"), [`Icosahedron`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Icosahedron.html#manim.mobject.three_d.polyhedra.Icosahedron "manim.mobject.three_d.polyhedra.Icosahedron") and [`Dodecahedron`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Dodecahedron.html#manim.mobject.three_d.polyhedra.Dodecahedron "manim.mobject.three_d.polyhedra.Dodecahedron")

- [#1285](https://github.com/ManimCommunity/manim/pull/1285): Add [`interactive_embed()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.interactive_embed "manim.scene.scene.Scene.interactive_embed") for OpenGL rendering

[`interactive_embed()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.interactive_embed "manim.scene.scene.Scene.interactive_embed") allows interaction with Scene via mouse and keyboard as well as dynamic commands via an iPython terminal.

- [#1261](https://github.com/ManimCommunity/manim/pull/1261): Render image automatically if no animation is played in a scene

- If no animations in scene and asked to preview/render a video, preview/render an image instead of raising a confusing error.


- [#1200](https://github.com/ManimCommunity/manim/pull/1200): Add text and SVG mobjects to OpenGL

Added OpenGL-compatible text and SVG mobjects


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html\#enhancements "Link to this heading")

- [#1398](https://github.com/ManimCommunity/manim/pull/1398): Fix and enhance Mobject.arrange\_in\_grid

arrange\_in\_grid now actually arranges submobjects in a grid. Added new parameters buff, cell\_alignment, row\_alignments, col\_alignments, row\_heights, col\_widths, flow\_order.

- [#1407](https://github.com/ManimCommunity/manim/pull/1407): Fix bug and rename `vector_coordinate_label()` to [`coordinate_label()`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector.coordinate_label "manim.mobject.geometry.line.Vector.coordinate_label") and move it to `geometry.py`

- [#1380](https://github.com/ManimCommunity/manim/pull/1380): Allow image objects as background images

- [#1391](https://github.com/ManimCommunity/manim/pull/1391): Add path\_arc support to .animate syntax

The parameter path\_arc of [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform") now works with the .animate syntax

- [#1364](https://github.com/ManimCommunity/manim/pull/1364): Added [`match_points()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_points "manim.mobject.mobject.Mobject.match_points")

- Added `match_points()`, which transforms the points, positions and submobjects of a Mobject to match that of the other while keeping style unchanged.


- [#1363](https://github.com/ManimCommunity/manim/pull/1363): Change of TeX compiler and output file format

- [#1359](https://github.com/ManimCommunity/manim/pull/1359): Make FILE a required argument

- Make FILE a required argument, manim/cli/render/commands.py:L30


- [#1304](https://github.com/ManimCommunity/manim/pull/1304): Improve Tex string splitting at double braces: only split for double brace groups

- [#1340](https://github.com/ManimCommunity/manim/pull/1340): Add OpenGL support to the new transform animations

Made FadeTransform, FadeTransformPieces, TransformMatchingShapes and TransformMatchingTex compatible with OpenGL rendering.

- [#1343](https://github.com/ManimCommunity/manim/pull/1343): Make TexTemplate() simple, but keep Tex()’s default template

TexTemplate() now returns a simple tex template.

- [#1321](https://github.com/ManimCommunity/manim/pull/1321): Add OpenGL support to [`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

- [#1302](https://github.com/ManimCommunity/manim/pull/1302): Raise appropriate errors in [`point_from_proportion()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.point_from_proportion "manim.mobject.types.vectorized_mobject.VMobject.point_from_proportion")

- Raise an error if the `alpha` argument is not between 0 and 1.

- Raise an error if the [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") has no points.


- [#1315](https://github.com/ManimCommunity/manim/pull/1315): Fix performance issues with [`get_arc_length()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.get_arc_length "manim.mobject.types.vectorized_mobject.VMobject.get_arc_length"), stemming from [#1274](https://github.com/ManimCommunity/manim/pull/1274)

- [#1320](https://github.com/ManimCommunity/manim/pull/1320): Add jpeg extension to the default image extensions

- [#1234](https://github.com/ManimCommunity/manim/pull/1234): Added new method [`get_midpoint()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_midpoint "manim.mobject.mobject.Mobject.get_midpoint")

Implemented [`get_midpoint()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_midpoint "manim.mobject.mobject.Mobject.get_midpoint") to return the point that is the middle of the stroke line of an mobject.

- [#1237](https://github.com/ManimCommunity/manim/pull/1237): Notify user if they are using an outdated version of Manim

- [#1308](https://github.com/ManimCommunity/manim/pull/1308): Improved [`ManimBanner`](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner "manim.mobject.logo.ManimBanner") animations

- [#1275](https://github.com/ManimCommunity/manim/pull/1275): Add SVG <line> element support to [`SVGMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject "manim.mobject.svg.svg_mobject.SVGMobject")

- [#1238](https://github.com/ManimCommunity/manim/pull/1238): Add parameter `about_point` for [`rotate()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.rotate "manim.mobject.mobject.Mobject.rotate")

- [#1260](https://github.com/ManimCommunity/manim/pull/1260): Change Brace from Tex to SVG (#1258)

- [#1122](https://github.com/ManimCommunity/manim/pull/1122): Support for specifying the interpolation algorithms for individual ImageMobjects

- [#1283](https://github.com/ManimCommunity/manim/pull/1283): Set default value of keyword `random_seed` in [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") to `None` (was 0 and fixed before)

- [#1220](https://github.com/ManimCommunity/manim/pull/1220): Added sanity checks to [`add_to_back()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_to_back "manim.mobject.mobject.Mobject.add_to_back") for Mobjects

Add Mobject add\_to\_back sanity checks:
\- Raises ValueError when Mobject tries to add itself
\- Raises TypeError when a non-Mobject is added
\- Filters out incoming duplicate submobjects if at least one instance of that submobject exists in the list

- [#1249](https://github.com/ManimCommunity/manim/pull/1249): Set corners of [`Rectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle") in counterclockwise direction

This improves the look of transformations between rectangles and other simple mobjects.

- [#1248](https://github.com/ManimCommunity/manim/pull/1248): Add Copy function to TexTemplate


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html\#fixed-bugs "Link to this heading")

- [#1368](https://github.com/ManimCommunity/manim/pull/1368): Added a check to ensure checking for the latest version was successful

- [#1413](https://github.com/ManimCommunity/manim/pull/1413): Prevent duplication of the same mobject when adding to submobjects via [`add_to_back()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_to_back "manim.mobject.mobject.Mobject.add_to_back")

Fixes #1412

- [#1395](https://github.com/ManimCommunity/manim/pull/1395): SVG transforms now handle exponent notation (6.02e23)

- [#1355](https://github.com/ManimCommunity/manim/pull/1355): Rewrite put\_start\_and\_end\_on to work in 3D

- [#1346](https://github.com/ManimCommunity/manim/pull/1346): Fixed errors introduced by stray print in [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")

- [#1305](https://github.com/ManimCommunity/manim/pull/1305): Automatically remove long tick marks not within the range of the `NumberLine`

- [#1296](https://github.com/ManimCommunity/manim/pull/1296): Fix random pipeline TeX failures

- [#1274](https://github.com/ManimCommunity/manim/pull/1274): Fix [`point_from_proportion()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.point_from_proportion "manim.mobject.types.vectorized_mobject.VMobject.point_from_proportion") to account for the length of curves.

- Add [`get_nth_curve_function_with_length()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_function_with_length "manim.mobject.types.vectorized_mobject.VMobject.get_nth_curve_function_with_length") and associated functions.

- Change [`point_from_proportion()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.point_from_proportion "manim.mobject.types.vectorized_mobject.VMobject.point_from_proportion") to use these functions to account for curve length.


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#1430](https://github.com/ManimCommunity/manim/pull/1430): Un-deprecated GraphScene (will be deprecated later), fixed an old-style call to NumberPlane

- More work is required in order to fully replace GraphScene via Axes, thus GraphScene is not deprecated yet.

- Fixed one example in which the old NumberPlane syntax was used.


- [#1425](https://github.com/ManimCommunity/manim/pull/1425): Added a “How to Cite Manim” section to the Readme

- [#1387](https://github.com/ManimCommunity/manim/pull/1387): Added Guide to Contribute Examples from GitHub Wiki to Documentation

Added a Guide

- [#1424](https://github.com/ManimCommunity/manim/pull/1424): Fixed all current docbuild warnings

- [#1389](https://github.com/ManimCommunity/manim/pull/1389): Adding Admonitions Tutorial to docs

- [#1341](https://github.com/ManimCommunity/manim/pull/1341): Reduce complexity of ThreeDSurfacePlot example

- [#1362](https://github.com/ManimCommunity/manim/pull/1362): Quick reference to modules

- [#1376](https://github.com/ManimCommunity/manim/pull/1376): Add flake8 and isort in docs

added ‘flake8’ and ‘isort’ usages to docs

- [#1360](https://github.com/ManimCommunity/manim/pull/1360): Grammatical error corrections in documentation

changed a few sentences in docs/source

- [#1351](https://github.com/ManimCommunity/manim/pull/1351): Some more typehints

- [#1358](https://github.com/ManimCommunity/manim/pull/1358): Fixed link to installation instructions for developers

- [#1338](https://github.com/ManimCommunity/manim/pull/1338): Added documentation guidelines for type hints

- [#1342](https://github.com/ManimCommunity/manim/pull/1342): Multiple ValueTracker example for docs

- [#1210](https://github.com/ManimCommunity/manim/pull/1210): Added tutorial chapter on coordinates of an mobject

- [#1335](https://github.com/ManimCommunity/manim/pull/1335): Added import statements to examples in documentation

- [#1245](https://github.com/ManimCommunity/manim/pull/1245): Added filled angle Example

- [#1328](https://github.com/ManimCommunity/manim/pull/1328): Docs: Update Brace example

- [#1326](https://github.com/ManimCommunity/manim/pull/1326): Improve documentation of [`ManimMagic`](https://docs.manim.community/en/stable/reference/manim.utils.ipython_magic.ManimMagic.html#manim.utils.ipython_magic.ManimMagic "manim.utils.ipython_magic.ManimMagic") (in particular: fix documented order of CLI flags)

- [#1323](https://github.com/ManimCommunity/manim/pull/1323): Blacken Docs Strings

- [#1300](https://github.com/ManimCommunity/manim/pull/1300): Added typehints for [`ValueTracker`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html#manim.mobject.value_tracker.ValueTracker "manim.mobject.value_tracker.ValueTracker")

- [#1301](https://github.com/ManimCommunity/manim/pull/1301): Added further docstrings and typehints to [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

- [#1298](https://github.com/ManimCommunity/manim/pull/1298): Add double backquotes for rst code samples (value\_tracker.py)

- [#1297](https://github.com/ManimCommunity/manim/pull/1297): Change docs to use viewcode extension instead of linkcode

Switched `sphinx.ext.linkcode` to `sphinx.ext.viewcode` and removed `linkcode_resolve` in `conf.py`.

- [#1246](https://github.com/ManimCommunity/manim/pull/1246): Added docstrings for [`ValueTracker`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html#manim.mobject.value_tracker.ValueTracker "manim.mobject.value_tracker.ValueTracker")

- [#1251](https://github.com/ManimCommunity/manim/pull/1251): Switch documentation from guzzle-sphinx-theme to furo

- [#1232](https://github.com/ManimCommunity/manim/pull/1232): Further docstrings and examples for [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

- [#1291](https://github.com/ManimCommunity/manim/pull/1291): Grammar improvements in README.md

- [#1269](https://github.com/ManimCommunity/manim/pull/1269): Add documentation about `set_color_by_tex()`

- [#1284](https://github.com/ManimCommunity/manim/pull/1284): Updated readme by providing the correct link to the example\_scenes

- [#1029](https://github.com/ManimCommunity/manim/pull/1029): Added example jupyter notebook into the examples folders

- [#1279](https://github.com/ManimCommunity/manim/pull/1279): Added sphinx requirements to pyproject.toml

New contributors who wanted to build the sphinx documentation had an extra step that could be removed by making use of `poetry install`. This removes the developer’s need for `pip install -r requirements.txt`.

- [#1268](https://github.com/ManimCommunity/manim/pull/1268): Added documentation explaining the differences between manim versions

- [#1247](https://github.com/ManimCommunity/manim/pull/1247): Added warning for the usage of animate

- [#1242](https://github.com/ManimCommunity/manim/pull/1242): Added an example for the manim colormap

- [#1239](https://github.com/ManimCommunity/manim/pull/1239): Add TinyTex installation instructions

- [#1231](https://github.com/ManimCommunity/manim/pull/1231): Improve changelog generation script


### Changes concerning the testing system [¶](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html\#changes-concerning-the-testing-system "Link to this heading")

- [#1299](https://github.com/ManimCommunity/manim/pull/1299): Red pixels (different value) now appear over green pixels (same value) in GraphicalUnitTest


### Changes to our development infrastructure [¶](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html\#changes-to-our-development-infrastructure "Link to this heading")

- [#1436](https://github.com/ManimCommunity/manim/pull/1436): Cache poetry venv with pyproject.toml hash in key

Cache poetry venv with pyproject.toml hash in key

- [#1435](https://github.com/ManimCommunity/manim/pull/1435): CI: Update poetry cache when new version is released

Fix test\_version failure in CI when using cached poetry venv

- [#1427](https://github.com/ManimCommunity/manim/pull/1427): Add URL’s to pyproject.toml

- [#1421](https://github.com/ManimCommunity/manim/pull/1421): Updated changelog generator’s labels and removed pre-commit bot from changelog

- [#1339](https://github.com/ManimCommunity/manim/pull/1339): CI: Fix macOS installation error from creating file in read-only file system

- [#1257](https://github.com/ManimCommunity/manim/pull/1257): CI: Caching ffmpeg, tinytex dependencies and poetry venv

CI: Caching ffmpeg, tinytex dependencies and poetry venv

- [#1294](https://github.com/ManimCommunity/manim/pull/1294): Added mixed-line-ending to .pre-commit-config.yaml

- [#1278](https://github.com/ManimCommunity/manim/pull/1278): Fixed flake8 errors and removed linter/formatter workflows

- [#1270](https://github.com/ManimCommunity/manim/pull/1270): Added isort to pre\_commit file

- [#1263](https://github.com/ManimCommunity/manim/pull/1263): CI: Turn off experimental installer for poetry to fix installation errors

- Turn off experimental installer for poetry to prevent manim installation errors for packages.

- Downgrade py39 to py38 for flake checks as pip does not enjoy py39, along with poetry.


- [#1255](https://github.com/ManimCommunity/manim/pull/1255): CI: Fix macOS pipeline failure

Update ci.yml to update and upgrade brew if necessary before installing dependencies, and remove the unsupported dvisvgm.86\_64-darwin package.

- [#1254](https://github.com/ManimCommunity/manim/pull/1254): Removed the comment warning that GitHub doesn’t allow uploading video in the issue templates.

- [#1216](https://github.com/ManimCommunity/manim/pull/1216): Use actions/checkout for cloning repository; black-checks

- [#1235](https://github.com/ManimCommunity/manim/pull/1235): Fixed version of decorator at <5.0.0


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#1411](https://github.com/ManimCommunity/manim/pull/1411): Change Union\[float, int\] to just float according to PEP 484

- [#1241](https://github.com/ManimCommunity/manim/pull/1241): Type Annotations: Fixing errors showing up in static type checking tool mypy

- [#1319](https://github.com/ManimCommunity/manim/pull/1319): Fix mean/meant typo

Fix typo in docs

- [#1313](https://github.com/ManimCommunity/manim/pull/1313): Singular typo fix on the Quickstart page in documentation

- [#1292](https://github.com/ManimCommunity/manim/pull/1292): Remove unnecessary imports from files

Imports reduced in a bunch of files

- [#1295](https://github.com/ManimCommunity/manim/pull/1295): Fix grammar and typos in the CODE OF CONDUCT

- [#1293](https://github.com/ManimCommunity/manim/pull/1293): Minor fixes - reduce lines

Remove unnecessary lines

- [#1281](https://github.com/ManimCommunity/manim/pull/1281): Remove all Carriage Return characters in our files

- [#1178](https://github.com/ManimCommunity/manim/pull/1178): Format Imports using Isort

- [#1233](https://github.com/ManimCommunity/manim/pull/1233): Fix deprecation warning for `--use_opengl_renderer` and `--use_webgl_renderer`

- [#1282](https://github.com/ManimCommunity/manim/pull/1282): Fix typing hints in vectorized\_mobject.py based on mypy


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.6.0-changelog.html\#new-releases "Link to this heading")

- [#1434](https://github.com/ManimCommunity/manim/pull/1434): Prepare v0.6.0