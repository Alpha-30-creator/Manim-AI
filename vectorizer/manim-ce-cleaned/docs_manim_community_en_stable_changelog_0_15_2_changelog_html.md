# v0.15.2 [¶](https://docs.manim.community/en/stable/changelog/0.15.2-changelog.html\#v0-15-2 "Link to this heading")

Date:

April 25, 2022

## Contributors [¶](https://docs.manim.community/en/stable/changelog/0.15.2-changelog.html\#contributors "Link to this heading")

A total of 33 people contributed to this
release. People with a ‘+’ by their names authored a patch for the first
time.

- Bailey Powers +

- Benjamin Hackl

- Dan Walsh +

- Darigov Research

- Darylgolden

- David Millard +

- Hamidreza Hashemi +

- Jan-Hendrik Müller

- Jason Villanueva

- Jonathan Alpert +

- Joy Bhalla

- Kian Cross +

- Luca +

- Mohsin Shaikh +

- Naveen M K

- Prismo +

- Ryan McCauley

- WillSoltas +

- ad\_chaos

- darkways +

- dawn\*squirryl +

- icedcoffeeee

- peaceheis

- sparshg

- trickypr +


The patches included in this release have been reviewed by
the following contributors.

- Benjamin Hackl

- Dan Walsh

- Darylgolden

- GameDungeon

- Hugues Devimeux

- Jan-Hendrik Müller

- Jason Villanueva

- Jonathan Alpert

- Luca

- Naveen M K

- Prismo

- Ryan McCauley

- ad\_chaos

- darkways

- hickmott99

- icedcoffeeee

- peaceheis


## Pull requests merged [¶](https://docs.manim.community/en/stable/changelog/0.15.2-changelog.html\#pull-requests-merged "Link to this heading")

A total of 39 pull requests were merged for this release.

### New features [¶](https://docs.manim.community/en/stable/changelog/0.15.2-changelog.html\#new-features "Link to this heading")

- [#1975](https://github.com/ManimCommunity/manim/pull/1975): Improved CLI help page styling

- Updates dependencies on Click and Cloup libraries for CLI help page styling.

- Removed the dependency on click-default-group.

- Added `no_args_is_help` parameter for `manim render` to allow easy access to help page.

- Added note to `manim` help page epilog on how to access other command help pages.


- [#2404](https://github.com/ManimCommunity/manim/pull/2404): Add [`SpiralIn`](https://docs.manim.community/en/stable/reference/manim.animation.creation.SpiralIn.html#manim.animation.creation.SpiralIn "manim.animation.creation.SpiralIn") Animation

- Make [`ManimBanner`](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner "manim.mobject.logo.ManimBanner") to use [`SpiralIn`](https://docs.manim.community/en/stable/reference/manim.animation.creation.SpiralIn.html#manim.animation.creation.SpiralIn "manim.animation.creation.SpiralIn").


- [#2534](https://github.com/ManimCommunity/manim/pull/2534): Implement `OpenGLImageMobject`

- [#2684](https://github.com/ManimCommunity/manim/pull/2684): Created a more accessible way to create Angles with line.py angle function - [`Angle.from_three_points()`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle.from_three_points "manim.mobject.geometry.line.Angle.from_three_points")


### Enhancements [¶](https://docs.manim.community/en/stable/changelog/0.15.2-changelog.html\#enhancements "Link to this heading")

- [#2062](https://github.com/ManimCommunity/manim/pull/2062): Reuse shader wrappers and shader data

- [#2642](https://github.com/ManimCommunity/manim/pull/2642): Migrated `file_ops.py` and `scene_file_writer.py` from os.path to Pathlib

In `file_ops.py` and `scene_file_writer.py`: Uses of str type file names have been mostly (see further information) converted to pathlib’s Path objects. Uses of `os.path` methods have been converted to equivalent pathlib methods.

- [#2655](https://github.com/ManimCommunity/manim/pull/2655): Fix [`assert_is_mobject_method()`](https://docs.manim.community/en/stable/reference/manim.animation.updaters.mobject_update_utils.html#manim.animation.updaters.mobject_update_utils.assert_is_mobject_method "manim.animation.updaters.mobject_update_utils.assert_is_mobject_method") when using OpenGL

- [#2665](https://github.com/ManimCommunity/manim/pull/2665): Improved handling of attributes when using the `.animate` syntax

- [#2674](https://github.com/ManimCommunity/manim/pull/2674): Document and type `simple_functions.py`

- Add documentation for `simple_functions.py`.

- Small additions with some extra clarity for these functions.


- [#2693](https://github.com/ManimCommunity/manim/pull/2693): Allow using [`MovingCamera.auto_zoom()`](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.auto_zoom "manim.camera.moving_camera.MovingCamera.auto_zoom") without animation

Allows auto zooming camera without having to play an animation by passing an `animation=False` argument


### Fixed bugs [¶](https://docs.manim.community/en/stable/changelog/0.15.2-changelog.html\#fixed-bugs "Link to this heading")

- [#2546](https://github.com/ManimCommunity/manim/pull/2546): Fixed a file logging bug and some maintenance

- [#2597](https://github.com/ManimCommunity/manim/pull/2597): Fix Bug in [`Uncreate`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Uncreate.html#manim.animation.creation.Uncreate "manim.animation.creation.Uncreate") with `rate_func` via introducing new parameter `reversed` to [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

- Refractor the [`Uncreate`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Uncreate.html#manim.animation.creation.Uncreate "manim.animation.creation.Uncreate"). The new implementation uses a flag member `reversed`. Set it to `True` and its superclass handles the reverse.

- Introduce a bool parameter `reversed` to [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"). It decides whether the animation needs to be played backwards. Default to be False.

- Add conditional branches in [`Animation.get_sub_alpha()`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.get_sub_alpha "manim.animation.animation.Animation.get_sub_alpha"). If the parameter `reversed` is True, it would set `rate_func(t)` to `rate_func(1 - t)`.


- [#2613](https://github.com/ManimCommunity/manim/pull/2613): Fixed bug in [`Circle.point_at_angle()`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle.point_at_angle "manim.mobject.geometry.arc.Circle.point_at_angle") when the angle is not in the interval \[0,2π\]

- [#2634](https://github.com/ManimCommunity/manim/pull/2634): Fix background lines drawn twice in [`NumberPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane")

- [#2648](https://github.com/ManimCommunity/manim/pull/2648): Handle user-defined centers for Wiggle animation

- [#2658](https://github.com/ManimCommunity/manim/pull/2658): Fix arguments of overridden `set_style` for [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "manim.mobject.geometry.shape_matchers.BackgroundRectangle")

Using [`Write`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Write.html#manim.animation.creation.Write "manim.animation.creation.Write") animation on a [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") object with `.add_background_rectangle()` applied no longer generates a `TypeError`.

- [#2668](https://github.com/ManimCommunity/manim/pull/2668): (Re)set background color of `OpenGLRenderer` when initializing scene

- [#2676](https://github.com/ManimCommunity/manim/pull/2676): Fixed propagation of custom attributes in animations for the OpenGL renderer

- [#2688](https://github.com/ManimCommunity/manim/pull/2688): Fixed two minor issues of [`SpiralIn`](https://docs.manim.community/en/stable/reference/manim.animation.creation.SpiralIn.html#manim.animation.creation.SpiralIn "manim.animation.creation.SpiralIn") and [`ManimBanner`](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner "manim.mobject.logo.ManimBanner")


### Documentation-related changes [¶](https://docs.manim.community/en/stable/changelog/0.15.2-changelog.html\#documentation-related-changes "Link to this heading")

- [#2609](https://github.com/ManimCommunity/manim/pull/2609): Copyedit troubleshooting.rst

- [#2610](https://github.com/ManimCommunity/manim/pull/2610): Add example PolygonOnAxes

- [#2617](https://github.com/ManimCommunity/manim/pull/2617): Re-added [`value_tracker`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.html#module-manim.mobject.value_tracker "manim.mobject.value_tracker") documentation

- [#2619](https://github.com/ManimCommunity/manim/pull/2619): Improve Example for arrange\_in\_grid

- [#2620](https://github.com/ManimCommunity/manim/pull/2620): Fixed typo in [`Animation.is_introducer()`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation.is_introducer "manim.animation.animation.Animation.is_introducer")

- [#2640](https://github.com/ManimCommunity/manim/pull/2640): Copyedited Documentation

Reviewed `tutorials/configurations.rst`. Edited simple mistakes such as Manim not being capitalized and commas.

- [#2649](https://github.com/ManimCommunity/manim/pull/2649): Document and type utils/iterables.py

- [#2651](https://github.com/ManimCommunity/manim/pull/2651): Update copyright year in documentation to 2020-2022

- [#2663](https://github.com/ManimCommunity/manim/pull/2663): Added documentation for scene updater functions

- [#2686](https://github.com/ManimCommunity/manim/pull/2686): Add instructions to install extra dependencies with poetry


### Changes to our development infrastructure [¶](https://docs.manim.community/en/stable/changelog/0.15.2-changelog.html\#changes-to-our-development-infrastructure "Link to this heading")

- [#2561](https://github.com/ManimCommunity/manim/pull/2561): Run tests on Linux-aarch64

- [#2656](https://github.com/ManimCommunity/manim/pull/2656): Fixed incompatibility with black version


### Code quality improvements and similar refactors [¶](https://docs.manim.community/en/stable/changelog/0.15.2-changelog.html\#code-quality-improvements-and-similar-refactors "Link to this heading")

- [#2630](https://github.com/ManimCommunity/manim/pull/2630): Remove WebGL renderer

The WebGL renderer is broken and unmaintained. The support for it in Manim is removed.

- [#2652](https://github.com/ManimCommunity/manim/pull/2652): Update `cloup` version to 0.13.0 from 0.7.0

- [#2678](https://github.com/ManimCommunity/manim/pull/2678): Require `backports-cached-property` only for Python < 3.8

- [#2685](https://github.com/ManimCommunity/manim/pull/2685): Migrate from `os.path` to `pathlib` in testing scripts

This pull request changes a number of instances of `os.path` to Pathlib objects and functions. In addition, this PR modifies the SVGMobject constructor to accept both a Pathlib object or a string variable pathname its constructor.

- [#2691](https://github.com/ManimCommunity/manim/pull/2691): Removed `CameraFrame`

- [#2696](https://github.com/ManimCommunity/manim/pull/2696): Made changelog generation run in parallel plus further improvements to `scripts/dev_changelog.py`

- [#2697](https://github.com/ManimCommunity/manim/pull/2697): Sort PRs by number in changelog sections before writing


### New releases [¶](https://docs.manim.community/en/stable/changelog/0.15.2-changelog.html\#new-releases "Link to this heading")

- [#2694](https://github.com/ManimCommunity/manim/pull/2694): Prepared bugfix release v0.15.2