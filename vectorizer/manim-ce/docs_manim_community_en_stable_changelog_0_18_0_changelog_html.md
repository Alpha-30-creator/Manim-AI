ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# v0.18.0 [¶](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html\#v0-18-0 "Link to this heading")

Date:

November 11, 2023

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html\#contributors "Link to this heading")

A total of 41 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Abulafia +

- Adhyyan Sekhsaria +

- Adrien Ludwig +

- Alex Kempen +

- Andres Berejnoi +

- Anousheh Moonen +

- Benjamin Hackl

- Francisco Manríquez Novoa

- Harald Schilly +

- Immanuel-Alvaro-Bhirawa +

- Jason Grace +

- Jason Villanueva

- Jinchu Li

- John Lynch +

- Jérome Eertmans

- Matt Turner +

- Narahari Rao +

- Naveen M K

- Nikhil Iyer +

- Ron Li +

- Sujal Singh +

- Tristan Schulz

- Uwe Zimmermann +

- Václav Blažej +

- Zachary Winkeler +


The patches included in this release have been reviewed by
the following contributors.

- Alex Lembcke

- Andres Berejnoi

- Axel

- Benjamin Hackl

- Francisco Manríquez Novoa

- Immanuel-Alvaro-Bhirawa

- Jan-Hendrik Müller

- Jason Grace

- Jason Villanueva

- Jinchu Li

- John Lynch

- Jérome Eertmans

- Kevin Lubick

- Narahari Rao

- Naveen M K

- NotWearingPants

- SsNiPeR1

- TheMathematicFanatic

- Tristan Schulz

- Uwe Zimmermann

- Viicos

- icedcoffeeee


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 59 pull requests were merged for this release.

### Breaking changes [¶](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html\#breaking-changes "Link to this heading")

- [#3020](https://github.com/ManimCommunity/manim/pull/3020): Rewrote Manim’s color system

This change removed the `colour` library as a dependency
of Manim and replaced the internal handling of colors with
the newly added [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"). This also adds hundreds
of new predefined colors, see [`utils.color`](https://docs.manim.community/en/stable/reference/manim.utils.color.html#module-manim.utils.color "manim.utils.color") for more
details.
This should only be a breaking change if you have interacted
directly with the `colour` module before. The general interface
has been kept stable.


### Highlights [¶](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html\#highlights "Link to this heading")

- [#3299](https://github.com/ManimCommunity/manim/pull/3299): Added new `manim checkhealth` CLI subcommand

This adds a new command line interface subcommand which can be used to check
whether a local installation of Manim has been configured correctly, and all
required (and optional) dependencies are available. To try it, run it via
`manim checkhealth` or `python -m manim checkhealth`.

- [#3427](https://github.com/ManimCommunity/manim/pull/3427): New feature: rendered examples in documentation can now be run directly via binder

This adds a “Make interactive” button below the examples in our documentation
that establishes a connection to binder such that examples can be modified and
rerendered directly from your browser.

- [#3086](https://github.com/ManimCommunity/manim/pull/3086): Introduced a new module [`typing`](https://docs.manim.community/en/stable/reference/manim.typing.html#module-manim.typing "manim.typing") for type hints

This also adds various type hints to integral parts of the code base.

- [#3322](https://github.com/ManimCommunity/manim/pull/3322): Implemented auto-removal of auxiliary LaTeX files, enabled by default

This automatically removes auxiliary files creating during the compilation of
LaTeX documents like `.aux` or `.dvi` files. This behavior can be controlled
via the newly introduced `no_latex_cleanup` config key ( `False` by default).
On the command line, the autoremoval can be disabled via the `--no_latex_cleanup`
CLI flag.

- [#3395](https://github.com/ManimCommunity/manim/pull/3395): Added support for Python 3.12


### New features [¶](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html\#new-features "Link to this heading")

- [#3361](https://github.com/ManimCommunity/manim/pull/3361): Added three new rate functions

This adds the rate functions [`smoothstep()`](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.html#manim.utils.rate_functions.smoothstep "manim.utils.rate_functions.smoothstep"), [`smootherstep()`](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.html#manim.utils.rate_functions.smootherstep "manim.utils.rate_functions.smootherstep"),
[`smoothererstep()`](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.html#manim.utils.rate_functions.smoothererstep "manim.utils.rate_functions.smoothererstep") based on the SmoothStep sigmoid functions.

- [#3264](https://github.com/ManimCommunity/manim/pull/3264): Added new mobjects [`LabeledLine`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledLine.html#manim.mobject.geometry.labeled.LabeledLine "manim.mobject.geometry.labeled.LabeledLine") and [`LabeledArrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledArrow.html#manim.mobject.geometry.labeled.LabeledArrow "manim.mobject.geometry.labeled.LabeledArrow")


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html\#enhancements "Link to this heading")

- [#3190](https://github.com/ManimCommunity/manim/pull/3190): Made [`CurvesAsSubmobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects") mobjects compatible with [`input_to_graph_point()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.input_to_graph_point "manim.mobject.graphing.coordinate_systems.CoordinateSystem.input_to_graph_point")

- [#3226](https://github.com/ManimCommunity/manim/pull/3226): Avoid using a mobject as a default argument of [`ArcBrace`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.ArcBrace.html#manim.mobject.svg.brace.ArcBrace "manim.mobject.svg.brace.ArcBrace")

- [#3366](https://github.com/ManimCommunity/manim/pull/3366): Added spacing between values and unit in [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber")

This adds the new keyword argument `unit_buff_per_font_unit` (default: 0, for
backwards compatibility). Setting it to some positive number creates additional
space between the numeric value and the displayed unit.


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html\#fixed-bugs "Link to this heading")

- [#3205](https://github.com/ManimCommunity/manim/pull/3205): Fixed type hint of `angle` in [`Arc`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc")

- [#3210](https://github.com/ManimCommunity/manim/pull/3210): Fixed [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") with `show_ellipsis=True` with the OpenGL renderer

- [#3211](https://github.com/ManimCommunity/manim/pull/3211): Fixed display issues with custom labels for [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes") with the OpenGL renderer

- [#3298](https://github.com/ManimCommunity/manim/pull/3298): Fixed expand animation for [`ManimBanner`](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner "manim.mobject.logo.ManimBanner")

- [#3306](https://github.com/ManimCommunity/manim/pull/3306): Fixed IPython terminal history and embedded shell instantiation for scenes using [`Scene.interactive_embed()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.interactive_embed "manim.scene.scene.Scene.interactive_embed")

- [#3315](https://github.com/ManimCommunity/manim/pull/3315): Fixed issue with parameter types in [`Scene.add_subcaption()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_subcaption "manim.scene.scene.Scene.add_subcaption")

- [#3423](https://github.com/ManimCommunity/manim/pull/3423): Fixed incorrect submobject count of multi-part [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") mobjects

This resolves various issues where formulas were not displayed completely,
like it was the case with `MathTex("1", "^{", "0")`.

- [#3284](https://github.com/ManimCommunity/manim/pull/3284): Fixed `LinearTransformationSceneExample` in Jupyter notebooks

- [#3302](https://github.com/ManimCommunity/manim/pull/3302): Fixed typo in comparison in `OpenGLVMobject.interpolate()`

- [#3340](https://github.com/ManimCommunity/manim/pull/3340): Fixed incorrect computation of bounding box for rotated [`ImageMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.image_mobject.ImageMobject.html#manim.mobject.types.image_mobject.ImageMobject "manim.mobject.types.image_mobject.ImageMobject")

- [#3343](https://github.com/ManimCommunity/manim/pull/3343): Fixed return value of [`TexTemplate.add_to_preamble()`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.add_to_preamble "manim.utils.tex.TexTemplate.add_to_preamble") and [`TexTemplate.add_to_document()`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.add_to_document "manim.utils.tex.TexTemplate.add_to_document")

- [#3282](https://github.com/ManimCommunity/manim/pull/3282): Ensure that [`ArrowVectorField.get_vector()`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#manim.mobject.vector_field.ArrowVectorField.get_vector "manim.mobject.vector_field.ArrowVectorField.get_vector") does not modify the passed inputs

- [#3392](https://github.com/ManimCommunity/manim/pull/3392): Fixed behavior of elongated tick lines for [`NumberLine`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")

- [#3430](https://github.com/ManimCommunity/manim/pull/3430): Fixed CSV reader adding empty lists in rendering summary during documentation build

- [#3404](https://github.com/ManimCommunity/manim/pull/3404): Properly raise an exception on empty inputs to [`AddTextLetterByLetter`](https://docs.manim.community/en/stable/reference/manim.animation.creation.AddTextLetterByLetter.html#manim.animation.creation.AddTextLetterByLetter "manim.animation.creation.AddTextLetterByLetter")


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#3219](https://github.com/ManimCommunity/manim/pull/3219): Enabled social cards for links to documentation

- [#3274](https://github.com/ManimCommunity/manim/pull/3274): Replaced incorrect mentions of Python 3.7 as the minimally required version

- [#3297](https://github.com/ManimCommunity/manim/pull/3297): Improved arrow tip sowcase example for [`ArrowTip`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip "manim.mobject.geometry.tips.ArrowTip")

- [#3312](https://github.com/ManimCommunity/manim/pull/3312): Added documentation for [`always_redraw()`](https://docs.manim.community/en/stable/reference/manim.animation.updaters.mobject_update_utils.html#manim.animation.updaters.mobject_update_utils.always_redraw "manim.animation.updaters.mobject_update_utils.always_redraw")

- [#3218](https://github.com/ManimCommunity/manim/pull/3218): Improved grammar in the [deep dive guide](https://docs.manim.community/en/stable/guides/deep_dive.html)

- [#3251](https://github.com/ManimCommunity/manim/pull/3251): Add LaTeX installation instructions for Fedora

- [#3290](https://github.com/ManimCommunity/manim/pull/3290): Updated required dependencies for MacOS installations

- [#3325](https://github.com/ManimCommunity/manim/pull/3325): Added documentation for functions in [`mobject_update_utils`](https://docs.manim.community/en/stable/reference/manim.animation.updaters.mobject_update_utils.html#module-manim.animation.updaters.mobject_update_utils "manim.animation.updaters.mobject_update_utils")

This adds docstrings and typehints to [`always_rotate()`](https://docs.manim.community/en/stable/reference/manim.animation.updaters.mobject_update_utils.html#manim.animation.updaters.mobject_update_utils.always_rotate "manim.animation.updaters.mobject_update_utils.always_rotate"),
[`always_shift()`](https://docs.manim.community/en/stable/reference/manim.animation.updaters.mobject_update_utils.html#manim.animation.updaters.mobject_update_utils.always_shift "manim.animation.updaters.mobject_update_utils.always_shift"), [`turn_animation_into_updater()`](https://docs.manim.community/en/stable/reference/manim.animation.updaters.mobject_update_utils.html#manim.animation.updaters.mobject_update_utils.turn_animation_into_updater "manim.animation.updaters.mobject_update_utils.turn_animation_into_updater")

- [#3353](https://github.com/ManimCommunity/manim/pull/3353): Added documentation for [`Mobject.center()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.center "manim.mobject.mobject.Mobject.center")

- [#3355](https://github.com/ManimCommunity/manim/pull/3355): Temporarily enabled `htmlzip` build on ReadTheDocs

- [#3377](https://github.com/ManimCommunity/manim/pull/3377): Fixed a typo in the [deep dive guide](https://docs.manim.community/en/stable/guides/deep_dive.html)

- [#3389](https://github.com/ManimCommunity/manim/pull/3389): Removed superfluous curly braces in a LaTeX expression

- [#3417](https://github.com/ManimCommunity/manim/pull/3417): Replaced `htmlzip` ReadTheDocs build with workflow attaching downloadable documentation to GitHub releases


### Changes concerning the testing system [¶](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html\#changes-concerning-the-testing-system "Link to this heading")

- [#3416](https://github.com/ManimCommunity/manim/pull/3416): Fixed tests to run on Cairo 1.18.0

- [#3257](https://github.com/ManimCommunity/manim/pull/3257): Fix a configuration error concerning poetry

- [#3419](https://github.com/ManimCommunity/manim/pull/3419): Fixed caching of Cairo builds on CI runners


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#3229](https://github.com/ManimCommunity/manim/pull/3229): Made docbuild errors easier to debug and fixed error from changed exception class

- [#3231](https://github.com/ManimCommunity/manim/pull/3231): Fixed errors reported by `flake8`

- [#3232](https://github.com/ManimCommunity/manim/pull/3232): Upgrade ReadTheDocs build environment to use newer image

- [#3286](https://github.com/ManimCommunity/manim/pull/3286): Optimized [`Axes.coords_to_point()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes.coords_to_point "manim.mobject.graphing.coordinate_systems.Axes.coords_to_point")

- [#3224](https://github.com/ManimCommunity/manim/pull/3224): Replace final few occurrences of `os.path` by `pathlib.Path`

- [#3236](https://github.com/ManimCommunity/manim/pull/3236): Return self in [`AbstractImageMobject.set_resampling_algorithm()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.image_mobject.AbstractImageMobject.html#manim.mobject.types.image_mobject.AbstractImageMobject.set_resampling_algorithm "manim.mobject.types.image_mobject.AbstractImageMobject.set_resampling_algorithm")

- [#3253](https://github.com/ManimCommunity/manim/pull/3253): Bump tornado from 6.3.1 to 6.3.2

- [#3272](https://github.com/ManimCommunity/manim/pull/3272): Bump docker/build-push-action from 3 to 4

- [#3287](https://github.com/ManimCommunity/manim/pull/3287): Bump cryptography from 41.0.1 to 41.0.2

- [#3350](https://github.com/ManimCommunity/manim/pull/3350): Added missing dependency `typing-extensions`

- [#3431](https://github.com/ManimCommunity/manim/pull/3431): Bump teatimeguest/setup-texlive-action from 2 to 3

- [#3433](https://github.com/ManimCommunity/manim/pull/3433): Bump dependencies

- [#3399](https://github.com/ManimCommunity/manim/pull/3399): Updated several dependencies

- [#3397](https://github.com/ManimCommunity/manim/pull/3397): Several GitHub actions updates

- [#3405](https://github.com/ManimCommunity/manim/pull/3405): Updated manimpango version to fix error regarding type strictness

- [#3421](https://github.com/ManimCommunity/manim/pull/3421): Improved order of input checks when creating a tree graph


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.18.0-changelog.html\#new-releases "Link to this heading")

- [#3439](https://github.com/ManimCommunity/manim/pull/3439): Prepared new release: v0.18.0