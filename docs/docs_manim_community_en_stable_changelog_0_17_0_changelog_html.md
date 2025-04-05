ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# v0.17.0 [¶](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html\#v0-17-0 "Link to this heading")

Date:

December 02, 2022

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html\#contributors "Link to this heading")

A total of 32 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Alex Lembcke

- Alexander Vázquez

- Benjamin Hackl

- Duc Phat +

- Hugues Devimeux

- Ievgen Pyrogov +

- Isaac Beh +

- Jeff Hanke +

- John Hammond +

- Jérome Eertmans +

- Kevin Lubick

- Kian-Meng Ang +

- Naveen M K

- Nick Skriloff +

- NotWearingPants

- Onur Solmaz +

- OpenRefactory, Inc +

- Owen Samuel +

- Pavel Zwerschke +

- Sparsh Goenka

- Taxo Rubio

- ad-chaos +

- fcrozatier

- mostly documentation +

- vahndi +


The patches included in this release have been reviewed by
the following contributors.

- Benjamin Hackl

- Darylgolden

- Hugues Devimeux

- Jan-Hendrik Müller

- Kevin Lubick

- Mohammed Belgoumri

- Naveen M K

- NotWearingPants

- Raghav Goel

- Sparsh Goenka

- Tristan Schulz

- ad-chaos

- friedkeenan


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 63 pull requests were merged for this release.

### Breaking changes [¶](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html\#breaking-changes "Link to this heading")

- [#2898](https://github.com/ManimCommunity/manim/pull/2898): Ported improved implementation of [`SVGMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject "manim.mobject.svg.svg_mobject.SVGMobject") from 3b1b/manim

The implementation of [`SVGMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject "manim.mobject.svg.svg_mobject.SVGMobject") is completely changed in this release.
Manim now uses the Python library `svgelements` to parse SVGs, instead of trying
to do it itself. The former class for SVG path objects, `SVGPathMobject` has been
replaced (without deprecation) with [`VMobjectFromSVGPath`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.html#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath "manim.mobject.svg.svg_mobject.VMobjectFromSVGPath").



If you need to create a mobject from an SVG path string, you can do so via:







```
import svgelements as se
my_path_mobject = VMobjectFromSVGPath(se.Path(my_path_string))

```

Copy to clipboard





The unused class `TexSymbol` has been removed. The modules
`manim.mobject.svg.svg_path` and `manim.mobject.svg.style_utils` became
superfluous due to the rework and have been removed.

- [#3030](https://github.com/ManimCommunity/manim/pull/3030): Added support for Python 3.11, dropped support for Python 3.7


### Highlights [¶](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html\#highlights "Link to this heading")

- [#3049](https://github.com/ManimCommunity/manim/pull/3049): Added thematic guide for the `manim-voiceover` plugin

This new [thematic guide](https://docs.manim.community/en/stable/guides/add_voiceovers.html) provides a brief
introduction to `manim-voiceover`, a plugin that helps to add voiceovers
to your manimations. Supports both working with your own voice as well as
synthetically generated voices.


### New features [¶](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html\#new-features "Link to this heading")

- [#2883](https://github.com/ManimCommunity/manim/pull/2883): Added animation [`RemoveTextLetterByLetter`](https://docs.manim.community/en/stable/reference/manim.animation.creation.RemoveTextLetterByLetter.html#manim.animation.creation.RemoveTextLetterByLetter "manim.animation.creation.RemoveTextLetterByLetter")

- [#3016](https://github.com/ManimCommunity/manim/pull/3016): Implemented `LineJointTypes` for both Cairo and OpenGL renderer

- [#3017](https://github.com/ManimCommunity/manim/pull/3017): Replaced renderer strings with [`RendererType`](https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html#manim.constants.RendererType "manim.constants.RendererType") enum entries


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html\#enhancements "Link to this heading")

- [#2927](https://github.com/ManimCommunity/manim/pull/2927): Allowed `networkx` to return 3D layouts when passing `dim=3` in the `layout_config` of a [`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph")

- [#3014](https://github.com/ManimCommunity/manim/pull/3014): Enabled code completion for [`Mobject.animate()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.animate "manim.mobject.mobject.Mobject.animate") for some IDEs

Uses a Union of the existing Generic Mobject Type T and \_Animation Builder as the declared return type from Mobject.animate to improve code completion.


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html\#fixed-bugs "Link to this heading")

- [#2846](https://github.com/ManimCommunity/manim/pull/2846): Prevent [`TransformMatchingTex`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html#manim.animation.transform_matching_parts.TransformMatchingTex "manim.animation.transform_matching_parts.TransformMatchingTex") from crashing when there is nothing to fade

- [#2885](https://github.com/ManimCommunity/manim/pull/2885): Always expand user when validating file-paths

- [#2888](https://github.com/ManimCommunity/manim/pull/2888): Fixed bug with propagation of `tex_template` value when using `tempconfig`

- [#2895](https://github.com/ManimCommunity/manim/pull/2895): Fixed broken [`ShowPassingFlashWithThinningStrokeWidth`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth.html#manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth "manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth")

- [#2920](https://github.com/ManimCommunity/manim/pull/2920): Fixed alignment of faded lines when passing `faded_line_ratio` to [`NumberPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane")

- [#2977](https://github.com/ManimCommunity/manim/pull/2977): Allow rendering of empty text strings

- [#2992](https://github.com/ManimCommunity/manim/pull/2992): Fixed `CLI.tex_template_file` config file setting

- [#3003](https://github.com/ManimCommunity/manim/pull/3003): Fixed setting `run_time` of [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession") after creating the animation object

- [#3019](https://github.com/ManimCommunity/manim/pull/3019): Fixed rendering SVG paths with multiple move commands


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#2881](https://github.com/ManimCommunity/manim/pull/2881): Fixed small typo in deep dive guide

- [#2886](https://github.com/ManimCommunity/manim/pull/2886): Added docstring to and fixed type hint of [`get_winding_number()`](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.get_winding_number "manim.utils.space_ops.get_winding_number")

- [#2892](https://github.com/ManimCommunity/manim/pull/2892): Corrected error in the `PolygonOnAxes` example

- [#2903](https://github.com/ManimCommunity/manim/pull/2903): Fixed minor grammar issues in [FAQ: General Usage](https://docs.manim.community/en/stable/faq/general.html)

- [#2904](https://github.com/ManimCommunity/manim/pull/2904): Fixed formatting and grammar issues in [Manim Development Process](https://docs.manim.community/en/stable/contributing/development.html)

- [#2911](https://github.com/ManimCommunity/manim/pull/2911): Disabled autoplay for `SoundExample` in documentation

- [#2914](https://github.com/ManimCommunity/manim/pull/2914): Added conda installation instructions

- [#2915](https://github.com/ManimCommunity/manim/pull/2915): Added documentation to [`three_dimensions`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.html#module-manim.mobject.three_d.three_dimensions "manim.mobject.three_d.three_dimensions")

- [#2919](https://github.com/ManimCommunity/manim/pull/2919): Corrected parameters and enhanced the description of [`ImageMobject.interpolate_color()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.image_mobject.ImageMobject.html#manim.mobject.types.image_mobject.ImageMobject.interpolate_color "manim.mobject.types.image_mobject.ImageMobject.interpolate_color")

- [#2932](https://github.com/ManimCommunity/manim/pull/2932): Fixed whitespace formatting issue

- [#2933](https://github.com/ManimCommunity/manim/pull/2933): Improved answer to the “no scenes in this module” error

- [#2936](https://github.com/ManimCommunity/manim/pull/2936): Added installation instructions for Windows via `winget`

- [#2962](https://github.com/ManimCommunity/manim/pull/2962): Disabled “Edit on GitHub” button in documentation

- [#2978](https://github.com/ManimCommunity/manim/pull/2978): Added documentation and example for [`CyclicReplace`](https://docs.manim.community/en/stable/reference/manim.animation.transform.CyclicReplace.html#manim.animation.transform.CyclicReplace "manim.animation.transform.CyclicReplace")

- [#3001](https://github.com/ManimCommunity/manim/pull/3001): Added FAQ entry regarding failed `manimpango` build

- [#3004](https://github.com/ManimCommunity/manim/pull/3004): Fixed docbuild warnings

- [#3018](https://github.com/ManimCommunity/manim/pull/3018): Follow-up to [#2988](https://github.com/ManimCommunity/manim/pull/2988) – fixes and improvements to some docstrings

- [#3022](https://github.com/ManimCommunity/manim/pull/3022): Corrected type hint in `Axes.coords_to_point()`

- [#3035](https://github.com/ManimCommunity/manim/pull/3035): Include latex install instructions on ubuntu

- [#3044](https://github.com/ManimCommunity/manim/pull/3044): Added Debian dependencies required for pycairo and manimpango


### Changes concerning the testing system [¶](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html\#changes-concerning-the-testing-system "Link to this heading")

- [#2893](https://github.com/ManimCommunity/manim/pull/2893): Improved performance of `test_threed.py`

- [#2981](https://github.com/ManimCommunity/manim/pull/2981): Implemented fallback save behavior for `pytest --show_diff`

- [#2982](https://github.com/ManimCommunity/manim/pull/2982): Rewrote unstable tests for [`text_mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.html#module-manim.mobject.text.text_mobject "manim.mobject.text.text_mobject") to be non-graphical

- [#2991](https://github.com/ManimCommunity/manim/pull/2991): Migrated `os.path` to `pathlib.Path` in tests

- [#3053](https://github.com/ManimCommunity/manim/pull/3053): Added threshold for pixel value errors in frame comparison tests


### Changes to our development infrastructure [¶](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html\#changes-to-our-development-infrastructure "Link to this heading")

- [#2925](https://github.com/ManimCommunity/manim/pull/2925): CI (test-arm): Updated python version to `3.10.6`

- [#2963](https://github.com/ManimCommunity/manim/pull/2963): CI (test-arm): Always select the correct python version

- [#3029](https://github.com/ManimCommunity/manim/pull/3029): CI: Updated actions version and added dependabot config

- [#3045](https://github.com/ManimCommunity/manim/pull/3045): Updated python-opengl -> python3-opengl for Ubuntu CI task


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#2872](https://github.com/ManimCommunity/manim/pull/2872): Add `extract_frames.py` utility script to help visualize test control data

- [#2877](https://github.com/ManimCommunity/manim/pull/2877): Fixed binder launch problem by adding missing optional `notebook` dependency

- [#2887](https://github.com/ManimCommunity/manim/pull/2887): Removed empty i18n files that caused filename clashes

- [#2931](https://github.com/ManimCommunity/manim/pull/2931): Updated `mapbox-earcut`

- [#2938](https://github.com/ManimCommunity/manim/pull/2938): Suggested fixes by iCR, OpenRefactory, Inc.

- [#2954](https://github.com/ManimCommunity/manim/pull/2954): Fixed click version string in `pyproject.toml`

- [#2958](https://github.com/ManimCommunity/manim/pull/2958): Fix missing stub packages for mypy

- [#2975](https://github.com/ManimCommunity/manim/pull/2975): Fixed broken links in README

- [#2980](https://github.com/ManimCommunity/manim/pull/2980): Migrate more `os.path` to `pathlib.Path`

- [#2983](https://github.com/ManimCommunity/manim/pull/2983): Fixed Windows CI Pipeline

- [#2988](https://github.com/ManimCommunity/manim/pull/2988): Converted all types of parameters in docstrings to proper type annotations

- [#2994](https://github.com/ManimCommunity/manim/pull/2994): Fixed segmentation faults from doctests under Python 3.10

- [#2995](https://github.com/ManimCommunity/manim/pull/2995): Added encoding to `open` in `utils.text_file_writing`

- [#3032](https://github.com/ManimCommunity/manim/pull/3032): Bump jupyter-core from 4.11.1 to 4.11.2

- [#3033](https://github.com/ManimCommunity/manim/pull/3033): Bump pillow from 9.2.0 to 9.3.0

- [#3054](https://github.com/ManimCommunity/manim/pull/3054): Removed unused `GraphicalUnitTester`


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.17.0-changelog.html\#new-releases "Link to this heading")

- [#3023](https://github.com/ManimCommunity/manim/pull/3023): Prepared new release: v0.17.0