# v0.19.0 [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#v0-19-0 "Link to this heading")

Date:

January 20, 2025

## Major Changes [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#major-changes "Link to this heading")

With the release of Manim v0.19.0, we’ve made lots of progress with making
Manim easier to install!

One of the biggest changes in this release is the replacement of the external
`ffmpeg` dependency with the `pyav` library. This means that users no longer
have to install `ffmpeg` in order to use Manim - they can just `pip install manim`
and it will work!

In light of this change, we also rewrote our [installation docs](https://docs.manim.community/en/stable/installation.html#local-installation)
to recommend using a new tool called [uv](https://docs.astral.sh/uv/) to install Manim.

Note

Do not worry if you installed Manim with any previous methods, like homebrew, pip,
choco, or scoop. Those methods will still work, and are not deprecated. However,
the recommended way to install Manim is now with [uv](https://docs.astral.sh/uv/).

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#contributors "Link to this heading")

A total of 54 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Aarush Deshpande

- Abulafia

- Achille Fouilleul +

- Benjamin Hackl

- CJ Lee +

- Cameron Burdgick +

- Chin Zhe Ning

- Christopher Hampson +

- ChungLeeCN +

- Eddie Ruiz +

6. Muenkel +
- Francisco Manríquez Novoa

- Geoo Chi +

- Henrik Skov Midtiby +

- Hugo Chargois +

- Irvanal Haq +

- Jay Gupta +

- Laifsyn +

- Larry Skuse +

- Nemo2510 +

- Nikhil Iyer

- Nikhila Gurusinghe +

- Rehmatpal Singh +

- Romit Mohane +

- Saveliy Yusufov +

- Sir James Clark Maxwell

- Sophia Wisdom +

- Tristan Schulz

- VPC +

- Victorien

- Xiuyuan (Jack) Yuan +

- alembcke

- anagorko +

- czuzu +

- fogsong233 +

- jkjkil4 +

- modjfy +

- nitzanbueno +

- yang-tsao +


The patches included in this release have been reviewed by
the following contributors.

- Aarush Deshpande

- Achille Fouilleul

- Benjamin Hackl

- Christopher Hampson

- Eddie Ruiz

- Francisco Manríquez Novoa

- Henrik Skov Midtiby

- Hugo Chargois

- Irvanal Haq

- Jay Gupta

- Jérome Eertmans

- Nemo2510

- Nikhila Gurusinghe

- OliverStrait

- Saveliy Yusufov

- Sir James Clark Maxwell

- Tristan Schulz

- VPC

- Victorien

- Xiuyuan (Jack) Yuan

- alembcke

- github-advanced-security\[bot\]


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#pull-requests-merged "Link to this heading")

A total of 138 pull requests were merged for this release.

### Highlights [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#highlights "Link to this heading")

- [#3501](https://github.com/ManimCommunity/manim/pull/3501): Replaced external `ffmpeg` dependency with `pyav`

This change removes the need to have `ffmpeg` available as a command line tool
when using Manim. While `pyav` technically also uses `ffmpeg` internally,
the maintainers of `pyav` distribute it in their binary wheels.

- [#3518](https://github.com/ManimCommunity/manim/pull/3518): Created a [`HSV`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html#manim.utils.color.core.HSV "manim.utils.color.core.HSV") color class, and added support for custom color spaces

This extends the color system of Manim and adds support to implement custom color spaces.
See the implementation of [`HSV`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html#manim.utils.color.core.HSV "manim.utils.color.core.HSV") for a practical example.

- [#3930](https://github.com/ManimCommunity/manim/pull/3930): Completely reworked the installation instructions

As a consequence of removing the need for the external `ffmpeg` dependency,
we have reworked and massively simplified the installation instructions. Given
that practically, user-written scenes are effectively small self-contained Python
projects, the new instructions strongly recommend using the
[project and dependency management tool uv](https://docs.astral.sh/uv/) to ensure
a consistent and reproducible environment.

- [#3967](https://github.com/ManimCommunity/manim/pull/3967): Added support for Python 3.13

This adds support for Python 3.13, which brings the range of currently supported
Python versions to 3.9 – 3.13.

- [#3966](https://github.com/ManimCommunity/manim/pull/3966): [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") can now be initialized with [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") iterables

Groups of Mobjects can now be created by passing an iterable to the [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")
constructors:







```
my_group = VGroup(Dot() for _ in range(10))

```

Copy to clipboard


### Breaking changes [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#breaking-changes "Link to this heading")

- [#3797](https://github.com/ManimCommunity/manim/pull/3797): Replaced `Code.styles_list` with [`Code.get_styles_list()`](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code.get_styles_list "manim.mobject.text.code_mobject.Code.get_styles_list")

The `styles_list` attribute of the [`Code`](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code "manim.mobject.text.code_mobject.Code") class has been replaced with
a class method [`Code.get_styles_list()`](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code.get_styles_list "manim.mobject.text.code_mobject.Code.get_styles_list"). This method returns a list of all
available values for the `formatter_style` argument of [`Code`](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code "manim.mobject.text.code_mobject.Code").

- [#3884](https://github.com/ManimCommunity/manim/pull/3884): Renamed parameters and variables conflicting with builtin functions

To avoid having keyword arguments named after builtin functions, the following
two changes were made to user-facing functions:



- `ManimColor.from_hex(hex=...)` is now `ManimColor.from_hex(hex_str=...)`

- `Scene.next_section(type=...)` is now `Scene.next_section(section_type=...)`


- [#3922](https://github.com/ManimCommunity/manim/pull/3922): Removed `inner_radius` and `outer_radius` from [`Sector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Sector.html#manim.mobject.geometry.arc.Sector "manim.mobject.geometry.arc.Sector") constructor

To construct a [`Sector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Sector.html#manim.mobject.geometry.arc.Sector "manim.mobject.geometry.arc.Sector"), you now need to specify a `radius` (and an `angle`).
In particular, [`AnnularSector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.AnnularSector.html#manim.mobject.geometry.arc.AnnularSector "manim.mobject.geometry.arc.AnnularSector") still accepts both `inner_radius` and `outer_radius`
arguments.

- [#3964](https://github.com/ManimCommunity/manim/pull/3964): Allow [`SurroundingRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html#manim.mobject.geometry.shape_matchers.SurroundingRectangle "manim.mobject.geometry.shape_matchers.SurroundingRectangle") to accept multiple Mobjects

This changes the signature of [`SurroundingRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html#manim.mobject.geometry.shape_matchers.SurroundingRectangle "manim.mobject.geometry.shape_matchers.SurroundingRectangle") to accept
a sequence of Mobjects instead of a single Mobject. As a consequence, other
arguments that could be specified as positional ones before now need to be
specified as keyword arguments:







```
SurroundingRectangle(some_mobject, RED, 0.3)  # raises error now
SurroundingRectangle(some_mobject, color=RED, buff=0.3)  # correct usage

```

Copy to clipboard

- [#4115](https://github.com/ManimCommunity/manim/pull/4115): Completely rewrite the implementation of the [`Code`](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code "manim.mobject.text.code_mobject.Code") mobject

This includes several breaking changes to the interface of the class to make it
more consistent. See the documentation of [`Code`](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code "manim.mobject.text.code_mobject.Code") for a detailed description
of the new interface, and the description of the pull request [#4115](https://github.com/ManimCommunity/manim/pull/4115) for
an overview of changes to the old keyword arguments.


### New features [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#new-features "Link to this heading")

- [#3148](https://github.com/ManimCommunity/manim/pull/3148): Added a `colorscale` argument to [`CoordinateSystem.plot()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot "manim.mobject.graphing.coordinate_systems.CoordinateSystem.plot")

- [#3612](https://github.com/ManimCommunity/manim/pull/3612): Add three animations that together simulate a typing animation

- [#3754](https://github.com/ManimCommunity/manim/pull/3754): Add `@` shorthand for [`Axes.coords_to_point()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes.coords_to_point "manim.mobject.graphing.coordinate_systems.Axes.coords_to_point") and [`Axes.point_to_coords()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes.point_to_coords "manim.mobject.graphing.coordinate_systems.Axes.point_to_coords")

- [#3876](https://github.com/ManimCommunity/manim/pull/3876): Add [`Animation.set_default()`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.set_default "manim.animation.animation.Animation.set_default") class method

- [#3903](https://github.com/ManimCommunity/manim/pull/3903): Preserve colors of LaTeX coloring commands

- [#3913](https://github.com/ManimCommunity/manim/pull/3913): Added [`DVIPSNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.DVIPSNAMES.html#module-manim.utils.color.DVIPSNAMES "manim.utils.color.DVIPSNAMES") and [`SVGNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.SVGNAMES.html#module-manim.utils.color.SVGNAMES "manim.utils.color.SVGNAMES") color palettes

- [#3933](https://github.com/ManimCommunity/manim/pull/3933): Added [`ConvexHull`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.ConvexHull.html#manim.mobject.geometry.polygram.ConvexHull "manim.mobject.geometry.polygram.ConvexHull"), [`ConvexHull3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.ConvexHull3D.html#manim.mobject.three_d.polyhedra.ConvexHull3D "manim.mobject.three_d.polyhedra.ConvexHull3D"), [`Label`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.Label.html#manim.mobject.geometry.labeled.Label "manim.mobject.geometry.labeled.Label") and [`LabeledPolygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledPolygram.html#manim.mobject.geometry.labeled.LabeledPolygram "manim.mobject.geometry.labeled.LabeledPolygram")

- [#3992](https://github.com/ManimCommunity/manim/pull/3992): Add darker, lighter and contrasting methods to [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

- [#3997](https://github.com/ManimCommunity/manim/pull/3997): Add a time property to scene ( [`Scene.time`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.time "manim.scene.scene.Scene.time"))

- [#4039](https://github.com/ManimCommunity/manim/pull/4039): Added the `delay` parameter to [`turn_animation_into_updater()`](https://docs.manim.community/en/stable/reference/manim.animation.updaters.mobject_update_utils.html#manim.animation.updaters.mobject_update_utils.turn_animation_into_updater "manim.animation.updaters.mobject_update_utils.turn_animation_into_updater")


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#enhancements "Link to this heading")

- [#3829](https://github.com/ManimCommunity/manim/pull/3829): Rewrite [`get_quadratic_approximation_of_cubic()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.get_quadratic_approximation_of_cubic "manim.utils.bezier.get_quadratic_approximation_of_cubic") to produce smoother animated curves

- [#3855](https://github.com/ManimCommunity/manim/pull/3855): Log execution time of sample scene in the `manim checkhealth` command

- [#3888](https://github.com/ManimCommunity/manim/pull/3888): Significantly reduce rendering time with a separate thread for writing frames to stream

- [#3890](https://github.com/ManimCommunity/manim/pull/3890): Better error messages for [`DrawBorderThenFill`](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html#manim.animation.creation.DrawBorderThenFill "manim.animation.creation.DrawBorderThenFill")

- [#3893](https://github.com/ManimCommunity/manim/pull/3893): Improve line rendering performance of [`Cylinder`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cylinder.html#manim.mobject.three_d.three_dimensions.Cylinder "manim.mobject.three_d.three_dimensions.Cylinder")

- [#3901](https://github.com/ManimCommunity/manim/pull/3901): Changed `Square.side_length` attribute to a property

- [#3965](https://github.com/ManimCommunity/manim/pull/3965): Added the `scale_stroke` boolean parameter to [`VMobject.scale()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.scale "manim.mobject.types.vectorized_mobject.VMobject.scale")

- [#3974](https://github.com/ManimCommunity/manim/pull/3974): Made videos embedded in Google Colab by default

- [#3982](https://github.com/ManimCommunity/manim/pull/3982): Refactored `run_time` validation for [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") and [`Scene.wait()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait "manim.scene.scene.Scene.wait")

- [#4017](https://github.com/ManimCommunity/manim/pull/4017): Allow animations with `run_time=0` and implement convenience [`Add`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add "manim.animation.animation.Add") animation

- [#4034](https://github.com/ManimCommunity/manim/pull/4034): Draw more accurate circular [`Arc`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc") mobjects for large angles

- [#4051](https://github.com/ManimCommunity/manim/pull/4051): Add `__hash__` method to [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

- [#4108](https://github.com/ManimCommunity/manim/pull/4108): Remove duplicate declaration of `__all__` in [`vectorized_mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.html#module-manim.mobject.types.vectorized_mobject "manim.mobject.types.vectorized_mobject")


### Optimizations [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#optimizations "Link to this heading")

- [#3760](https://github.com/ManimCommunity/manim/pull/3760): Optimize [`VMobject.pointwise_become_partial()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.pointwise_become_partial "manim.mobject.types.vectorized_mobject.VMobject.pointwise_become_partial")

- [#3765](https://github.com/ManimCommunity/manim/pull/3765): Optimize [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") methods which append to `points`

- [#3766](https://github.com/ManimCommunity/manim/pull/3766): Created and optimized Bézier splitting functions such as [`partial_bezier_points()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.partial_bezier_points "manim.utils.bezier.partial_bezier_points") in [`manim.utils.bezier`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#module-manim.utils.bezier "manim.utils.bezier")

- [#3767](https://github.com/ManimCommunity/manim/pull/3767): Optimized [`manim.utils.bezier.get_smooth_cubic_bezier_handle_points()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.get_smooth_cubic_bezier_handle_points "manim.utils.bezier.get_smooth_cubic_bezier_handle_points")

- [#3768](https://github.com/ManimCommunity/manim/pull/3768): Optimized [`manim.utils.bezier.is_closed()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.is_closed "manim.utils.bezier.is_closed")

- [#3960](https://github.com/ManimCommunity/manim/pull/3960): Optimized [`interpolate()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.interpolate "manim.utils.bezier.interpolate") and [`bezier()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.bezier "manim.utils.bezier.bezier") in [`manim.utils.bezier`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#module-manim.utils.bezier "manim.utils.bezier")


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#fixed-bugs "Link to this heading")

- [#3706](https://github.com/ManimCommunity/manim/pull/3706): Fixed [`Line.put_start_and_end_on()`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line.put_start_and_end_on "manim.mobject.geometry.line.Line.put_start_and_end_on") to use the actual end of an [`Arrow3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Arrow3D.html#manim.mobject.three_d.three_dimensions.Arrow3D "manim.mobject.three_d.three_dimensions.Arrow3D")

- [#3732](https://github.com/ManimCommunity/manim/pull/3732): Fixed infinite loop in OpenGL `BackgroundRectangle.get_color()`

- [#3756](https://github.com/ManimCommunity/manim/pull/3756): Fix assertions and improve error messages when adding submobjects

- [#3778](https://github.com/ManimCommunity/manim/pull/3778): Fixed [`there_and_back_with_pause()`](https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.html#manim.utils.rate_functions.there_and_back_with_pause "manim.utils.rate_functions.there_and_back_with_pause") rate function behaviour with different `pause_ratio` values

- [#3786](https://github.com/ManimCommunity/manim/pull/3786): Fix [`DiGraph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph") edges not fading correctly on [`FadeIn`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeIn.html#manim.animation.fading.FadeIn "manim.animation.fading.FadeIn") and [`FadeOut`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html#manim.animation.fading.FadeOut "manim.animation.fading.FadeOut")

- [#3790](https://github.com/ManimCommunity/manim/pull/3790): Fixed the `get_nth_subpath()` function expecting a numpy array

- [#3832](https://github.com/ManimCommunity/manim/pull/3832): Convert audio files to `.wav` before passing to pydub

- [#3680](https://github.com/ManimCommunity/manim/pull/3680): Fixed behavior of `config.background_opacity < 1`

- [#3839](https://github.com/ManimCommunity/manim/pull/3839): Fixed [`ManimConfig.format`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.format "manim._config.utils.ManimConfig.format") not updating movie file extension

- [#3885](https://github.com/ManimCommunity/manim/pull/3885): Fixed `OpenGLMobject.invert()` not reassembling family

- [#3951](https://github.com/ManimCommunity/manim/pull/3951): Call [`Animation.finish()`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.finish "manim.animation.animation.Animation.finish") for animations in an [`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

- [#4013](https://github.com/ManimCommunity/manim/pull/4013): Fixed scene skipping for `ManimConfig.upto_animation_number` set to 0

- [#4089](https://github.com/ManimCommunity/manim/pull/4089): Fixed bug with opacity of [`ImageMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.image_mobject.ImageMobject.html#manim.mobject.types.image_mobject.ImageMobject "manim.mobject.types.image_mobject.ImageMobject")

- [#4091](https://github.com/ManimCommunity/manim/pull/4091): Fixed [`VMobject.add_points_as_corners()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.add_points_as_corners "manim.mobject.types.vectorized_mobject.VMobject.add_points_as_corners") to safely handle empty `points` parameter


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#documentation-related-changes "Link to this heading")

- [#3669](https://github.com/ManimCommunity/manim/pull/3669): Added a [`manim.typing`](https://docs.manim.community/en/stable/reference/manim.typing.html#module-manim.typing "manim.typing") guide

- [#3715](https://github.com/ManimCommunity/manim/pull/3715): Added docstrings to Brace

- [#3745](https://github.com/ManimCommunity/manim/pull/3745): Underline tag should be `<u></u>` in the documentation

- [#3818](https://github.com/ManimCommunity/manim/pull/3818): Automatically document usages of `typing.TypeVar`

- [#3849](https://github.com/ManimCommunity/manim/pull/3849): Fix incorrect `versionadded` version number in plugin section in docs

- [#3851](https://github.com/ManimCommunity/manim/pull/3851): Rename `manim.typing.Image` type aliases to [`PixelArray`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PixelArray "manim.typing.PixelArray") to avoid conflict with `PIL.Image`

- [#3857](https://github.com/ManimCommunity/manim/pull/3857): Update installation instructions for MacOS (via dedicated brew formula)

- [#3878](https://github.com/ManimCommunity/manim/pull/3878): Fixed typehint in `types.rst` and replaced outdated reference to `manim.typing.Image` with [`manim.typing.PixelArray`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PixelArray "manim.typing.PixelArray")

- [#3924](https://github.com/ManimCommunity/manim/pull/3924): Fix `SyntaxWarning` when building docs + use Python 3.13 for readthedocs build

- [#3958](https://github.com/ManimCommunity/manim/pull/3958): Fix: `.to_edge`’s example demonstration in docs

- [#3972](https://github.com/ManimCommunity/manim/pull/3972): Refining documentations for [`moving_camera_scene`](https://docs.manim.community/en/stable/reference/manim.scene.moving_camera_scene.html#module-manim.scene.moving_camera_scene "manim.scene.moving_camera_scene") module

- [#4032](https://github.com/ManimCommunity/manim/pull/4032): Bump version and create changelog for `v0.19.0`

- [#4044](https://github.com/ManimCommunity/manim/pull/4044): Added support for autodocumenting type aliases that use the `type` syntax

- [#4065](https://github.com/ManimCommunity/manim/pull/4065): Polish documentation of [`utils.color.core`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#module-manim.utils.color.core "manim.utils.color.core") and remove `interpolate_array` function

- [#4077](https://github.com/ManimCommunity/manim/pull/4077): Update README and documentation landing page, improve way how 3b1b is credited

- [#4100](https://github.com/ManimCommunity/manim/pull/4100): Add wavy square example to [`Homotopy`](https://docs.manim.community/en/stable/reference/manim.animation.movement.Homotopy.html#manim.animation.movement.Homotopy "manim.animation.movement.Homotopy")

- [#4107](https://github.com/ManimCommunity/manim/pull/4107): Corrected a typo in the deep dive guide

- [#4116](https://github.com/ManimCommunity/manim/pull/4116): Fix broken link to Poetry installation in contribution docs


### Type Hints [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#type-hints "Link to this heading")

- [#3751](https://github.com/ManimCommunity/manim/pull/3751): Added typehints to [`manim.utils.iterables`](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#module-manim.utils.iterables "manim.utils.iterables")

- [#3803](https://github.com/ManimCommunity/manim/pull/3803): Added typings to `OpenGLMobject`

- [#3902](https://github.com/ManimCommunity/manim/pull/3902): fixed a wrong type hint in [`Scene.restructure_mobjects()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.restructure_mobjects "manim.scene.scene.Scene.restructure_mobjects")

- [#3916](https://github.com/ManimCommunity/manim/pull/3916): fixed type hint in `DrawBorderThenFill.interpolate_submobject()`

- [#3926](https://github.com/ManimCommunity/manim/pull/3926): Fixed some typehints of [`ParametricFunction`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ParametricFunction.html#manim.mobject.graphing.functions.ParametricFunction "manim.mobject.graphing.functions.ParametricFunction")

- [#3940](https://github.com/ManimCommunity/manim/pull/3940): Fixed `np.float_` to `np.float64` while using numpy versions above 2.0

- [#3961](https://github.com/ManimCommunity/manim/pull/3961): Added typehints to [`manim.mobject.geometry`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.html#module-manim.mobject.geometry "manim.mobject.geometry")

- [#3980](https://github.com/ManimCommunity/manim/pull/3980): Added new [`PointND`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PointND "manim.typing.PointND") and [`PointND_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PointND_Array "manim.typing.PointND_Array") type aliases

- [#3988](https://github.com/ManimCommunity/manim/pull/3988): Added type hints to [`manim.cli`](https://docs.manim.community/en/stable/reference/manim.cli.html#module-manim.cli "manim.cli") module

- [#3999](https://github.com/ManimCommunity/manim/pull/3999): Add type annotations to `manim.utils`

- [#4006](https://github.com/ManimCommunity/manim/pull/4006): Stopped ignoring `manim.plugins` errors in `mypy.ini`

- [#4007](https://github.com/ManimCommunity/manim/pull/4007): Added typings to `manim.__main__`

- [#4027](https://github.com/ManimCommunity/manim/pull/4027): Rename `InternalPoint3D` to [`Point3D`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"), `Point3D` to [`Point3DLike`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") and other point-related type aliases

- [#4038](https://github.com/ManimCommunity/manim/pull/4038): Fixed type hint of [`Scene.play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") to allow [`Mobject.animate`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.animate "manim.mobject.mobject.Mobject.animate")


### Internal Improvements and Automation [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#internal-improvements-and-automation "Link to this heading")

- [#3737](https://github.com/ManimCommunity/manim/pull/3737): Fixed action for building downloadable documentation

- [#3761](https://github.com/ManimCommunity/manim/pull/3761): Use `--py39-plus` in pre-commit

- [#3777](https://github.com/ManimCommunity/manim/pull/3777): Add pyproject for ruff formatting

- [#3779](https://github.com/ManimCommunity/manim/pull/3779): Switch pre-commit to use `ruff` for linting

- [#3795](https://github.com/ManimCommunity/manim/pull/3795): Replace Pyupgrade with Ruff rule

- [#3812](https://github.com/ManimCommunity/manim/pull/3812): Fix MacOS LaTeX CI

- [#3853](https://github.com/ManimCommunity/manim/pull/3853): Change from tempconfig to a config fixture in tests

- [#3858](https://github.com/ManimCommunity/manim/pull/3858): Update docker to use ENV x=y instead of ENV x y

- [#3872](https://github.com/ManimCommunity/manim/pull/3872): Use ruff for pytest style

- [#3873](https://github.com/ManimCommunity/manim/pull/3873): Use ruff instead of flake8-simplify

- [#3877](https://github.com/ManimCommunity/manim/pull/3877): Fix pre-commit linting

- [#3780](https://github.com/ManimCommunity/manim/pull/3780): Add Ruff Lint

- [#3781](https://github.com/ManimCommunity/manim/pull/3781): Ignore Ruff format in git blame

- [#3881](https://github.com/ManimCommunity/manim/pull/3881): Standardize docstrings with ruff pydocstyle rules

- [#3882](https://github.com/ManimCommunity/manim/pull/3882): Change flake8-comprehensions and flake8-bugbear to ruff

- [#3887](https://github.com/ManimCommunity/manim/pull/3887): Fix typo from HSV PR

- [#3923](https://github.com/ManimCommunity/manim/pull/3923): Use Ruff pygrep rules

- [#3925](https://github.com/ManimCommunity/manim/pull/3925): Use Github Markdown on README

- [#3955](https://github.com/ManimCommunity/manim/pull/3955): Use `subprocess` instead of `os.system`.

- [#3956](https://github.com/ManimCommunity/manim/pull/3956): Set AAC codec for audio in mp4 files, add transcoding utility

- [#4069](https://github.com/ManimCommunity/manim/pull/4069): Include Noto fonts in Docker image

- [#4102](https://github.com/ManimCommunity/manim/pull/4102): Remove PT004 from Ruff ignore rules


### Dependencies [¶](https://docs.manim.community/en/stable/changelog/0.19.0-changelog.html\#dependencies "Link to this heading")

- [#3739](https://github.com/ManimCommunity/manim/pull/3739): \[pre-commit.ci\] pre-commit autoupdate

- [#3746](https://github.com/ManimCommunity/manim/pull/3746): Bump tqdm from 4.66.1 to 4.66.3

- [#3750](https://github.com/ManimCommunity/manim/pull/3750): Bump jinja2 from 3.1.3 to 3.1.4

- [#3776](https://github.com/ManimCommunity/manim/pull/3776): Bump requests from 2.31.0 to 2.32.0

- [#3784](https://github.com/ManimCommunity/manim/pull/3784): \[pre-commit.ci\] pre-commit autoupdate

- [#3794](https://github.com/ManimCommunity/manim/pull/3794): \[pre-commit.ci\] pre-commit autoupdate

- [#3796](https://github.com/ManimCommunity/manim/pull/3796): Bump tornado from 6.4 to 6.4.1

- [#3801](https://github.com/ManimCommunity/manim/pull/3801): \[pre-commit.ci\] pre-commit autoupdate

- [#3809](https://github.com/ManimCommunity/manim/pull/3809): \[pre-commit.ci\] pre-commit autoupdate

- [#3810](https://github.com/ManimCommunity/manim/pull/3810): Bump urllib3 from 2.2.1 to 2.2.2

- [#3823](https://github.com/ManimCommunity/manim/pull/3823): \[pre-commit.ci\] pre-commit autoupdate

- [#3827](https://github.com/ManimCommunity/manim/pull/3827): Fix docker build

- [#3834](https://github.com/ManimCommunity/manim/pull/3834): \[pre-commit.ci\] pre-commit autoupdate

- [#3835](https://github.com/ManimCommunity/manim/pull/3835): Bump docker/build-push-action from 5 to 6

- [#3841](https://github.com/ManimCommunity/manim/pull/3841): Bump certifi from 2024.2.2 to 2024.7.4

- [#3844](https://github.com/ManimCommunity/manim/pull/3844): \[pre-commit.ci\] pre-commit autoupdate

- [#3847](https://github.com/ManimCommunity/manim/pull/3847): Bump zipp from 3.18.2 to 3.19.1

- [#3865](https://github.com/ManimCommunity/manim/pull/3865): \[pre-commit.ci\] pre-commit autoupdate

- [#3880](https://github.com/ManimCommunity/manim/pull/3880): \[pre-commit.ci\] pre-commit autoupdate

- [#3889](https://github.com/ManimCommunity/manim/pull/3889): \[pre-commit.ci\] pre-commit autoupdate

- [#3895](https://github.com/ManimCommunity/manim/pull/3895): Lock poetry.lock

- [#3896](https://github.com/ManimCommunity/manim/pull/3896): \[pre-commit.ci\] pre-commit autoupdate

- [#3904](https://github.com/ManimCommunity/manim/pull/3904): \[pre-commit.ci\] pre-commit autoupdate

- [#3911](https://github.com/ManimCommunity/manim/pull/3911): \[pre-commit.ci\] pre-commit autoupdate

- [#3918](https://github.com/ManimCommunity/manim/pull/3918): \[pre-commit.ci\] pre-commit autoupdate

- [#3929](https://github.com/ManimCommunity/manim/pull/3929): \[pre-commit.ci\] pre-commit autoupdate

- [#3931](https://github.com/ManimCommunity/manim/pull/3931): Bump cryptography from 43.0.0 to 43.0.1

- [#3987](https://github.com/ManimCommunity/manim/pull/3987): \[pre-commit.ci\] pre-commit autoupdate

- [#4023](https://github.com/ManimCommunity/manim/pull/4023): Bump tornado from 6.4.1 to 6.4.2

- [#4035](https://github.com/ManimCommunity/manim/pull/4035): \[pre-commit.ci\] pre-commit autoupdate

- [#4037](https://github.com/ManimCommunity/manim/pull/4037): Cap `pyav` version