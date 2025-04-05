ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/changelog/0.2.0-changelog.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/changelog/0.2.0-changelog.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# v0.2.0 [¶](https://docs.manim.community/en/stable/changelog/0.2.0-changelog.html\#v0-2-0 "Link to this heading")

Date:

January 1, 2021

The changes since Manim Community release v0.1.1 are listed below.

## Breaking Changes [¶](https://docs.manim.community/en/stable/changelog/0.2.0-changelog.html\#breaking-changes "Link to this heading")

- Remove all CONFIG dictionaries and all calls to `digest_config` and allow
passing options directly to the constructor of the corresponding classes ( [#783](https://github.com/ManimCommunity/manim/pull/783)).

Practically, this means that old constructions using `CONFIG` like:





```
class SomeMobject(Thing):
      CONFIG = {
          "my_awesome_property": 42
      }

```

Copy to clipboard



where corresponding objects were then instantiated as `my_mobject = SomeMobject()`
should now be created simply using `my_mobject = SomeMobject(my_awesome_property=42)`.

- Remove old syntax for animating mobject methods by passing the methods and arguments to `self.play`,
and use a new syntax featuring the `animate` property ( [#881](https://github.com/ManimCommunity/manim/pull/881)).

For example: the old-style `play` call





```
self.play(my_square.shift, LEFT)

```

Copy to clipboard



should be replaced with the new following call using the `animate` property:





```
self.play(my_square.animate.shift(LEFT))

```

Copy to clipboard


## New Features [¶](https://docs.manim.community/en/stable/changelog/0.2.0-changelog.html\#new-features "Link to this heading")

- Added creation animation for [`ManimBanner`](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner "manim.mobject.logo.ManimBanner") ( [#814](https://github.com/ManimCommunity/manim/pull/814))

- Added some documentation to [`construct()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct") ( [#753](https://github.com/ManimCommunity/manim/pull/753))

- Added a black and white monochromatic version of Manim’s logo ( [#826](https://github.com/ManimCommunity/manim/pull/826))

- Added support for a plugin system ( `manim plugin` subcommand + documentation) ( [#784](https://github.com/ManimCommunity/manim/pull/784))

- Implemented `__add__`, `__iadd__`, `__sub__`, and `__isub__` for [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") (allowing for notation like `some_vgroup + some_mobject`) ( [#790](https://github.com/ManimCommunity/manim/pull/790))

- Added type hints to several files in the library ( [#835](https://github.com/ManimCommunity/manim/pull/835))

- Added some examples to [`creation`](https://docs.manim.community/en/stable/reference/manim.animation.creation.html#module-manim.animation.creation "manim.animation.creation") ( [#820](https://github.com/ManimCommunity/manim/pull/820))

- Added some examples to [`DashedLine`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DashedLine.html#manim.mobject.geometry.line.DashedLine "manim.mobject.geometry.line.DashedLine") and [`CurvesAsSubmobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects") ( [#833](https://github.com/ManimCommunity/manim/pull/833))

- Added new implementation for text rendered with Pango, [`MarkupText`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText"), which can be formatted with an HTML-like syntax ( [#855](https://github.com/ManimCommunity/manim/pull/855))

- Added Fading in and out examples and deprecation of `FadeInFromDown` and `FadeOutAndShiftDown` ( [#827](https://github.com/ManimCommunity/manim/pull/827))

- Added example for [`MoveAlongPath`](https://docs.manim.community/en/stable/reference/manim.animation.movement.MoveAlongPath.html#manim.animation.movement.MoveAlongPath "manim.animation.movement.MoveAlongPath") to the docs ( [#873](https://github.com/ManimCommunity/manim/pull/873))

- Added ambient rotate for other angles - theta, phi, gamma ( [#660](https://github.com/ManimCommunity/manim/pull/660))

- Use custom bindings for Pango ( [#878](https://github.com/ManimCommunity/manim/pull/878))

- Added [`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph"), a basic implementation for (graph theory) graphs ( [#861](https://github.com/ManimCommunity/manim/pull/861))

- Allow for chaining methods when using the new `.animate` syntax in [`play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") ( [#889](https://github.com/ManimCommunity/manim/pull/889))


## Bugfixes [¶](https://docs.manim.community/en/stable/changelog/0.2.0-changelog.html\#bugfixes "Link to this heading")

- Fix doctests in .rst files ( [#797](https://github.com/ManimCommunity/manim/pull/797))

- Fix failing doctest after adding `manim plugin` subcommand ( [#831](https://github.com/ManimCommunity/manim/pull/831))

- Normalize the direction vector in `always_shift()` ( [#839](https://github.com/ManimCommunity/manim/pull/839))

- Add `disable_ligatures` to [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") (via [#804](https://github.com/ManimCommunity/manim/pull/804))

- Make scene caching aware of order of Mobjects ( [#845](https://github.com/ManimCommunity/manim/pull/845))

- Fix `CairoText` to work with new config structure ( [#858](https://github.com/ManimCommunity/manim/pull/858))

- Added missing argument to classes inheriting from [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix") ( [#859](https://github.com/ManimCommunity/manim/pull/859))

- Fixed: `z_index` of mobjects contained in others as submobjects is now properly respected ( [#872](https://github.com/ManimCommunity/manim/pull/872))

- Let `set_fill_by_checkboard()` return the modified surface to allow method chaining ( [#883](https://github.com/ManimCommunity/manim/pull/883))

- Mobjects added during an updater are added to `Scene.moving_mobjects` ( [#838](https://github.com/ManimCommunity/manim/pull/838))

- Pass background color to JS renderer ( [#876](https://github.com/ManimCommunity/manim/pull/876))

- Small fixes to docstrings. Tiny cleanups. Remove `digest_mobject_attrs`. ( [#834](https://github.com/ManimCommunity/manim/pull/834))

- Added closed shape detection in [`DashedVMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.DashedVMobject.html#manim.mobject.types.vectorized_mobject.DashedVMobject "manim.mobject.types.vectorized_mobject.DashedVMobject") in order to achieve an even dash pattern ( [#884](https://github.com/ManimCommunity/manim/pull/884))

- Fix Spelling in docstrings and variables across the library ( [#890](https://github.com/ManimCommunity/manim/pull/890))


## Other changes [¶](https://docs.manim.community/en/stable/changelog/0.2.0-changelog.html\#other-changes "Link to this heading")

- Change library name to manim ( [#811](https://github.com/ManimCommunity/manim/pull/811))

- Docker: use local files when building an image ( [#803](https://github.com/ManimCommunity/manim/pull/803))

- Let ffmpeg render partial movie files directly instead of temp files ( [#817](https://github.com/ManimCommunity/manim/pull/817))

- `manimce` to `manim` & capitalizing Manim in readme ( [#794](https://github.com/ManimCommunity/manim/pull/794))

- Added flowchart for different docstring categories ( [#828](https://github.com/ManimCommunity/manim/pull/828))

- Improve example in module docstring of [`creation`](https://docs.manim.community/en/stable/reference/manim.animation.creation.html#module-manim.animation.creation "manim.animation.creation") \+ explicitly document buff parameter in [`arrange()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange "manim.mobject.mobject.Mobject.arrange") ( [#825](https://github.com/ManimCommunity/manim/pull/825))

- Disable CI pipeline for Python 3.6 ( [#823](https://github.com/ManimCommunity/manim/pull/823))

- Update URLs in docs ( [#832](https://github.com/ManimCommunity/manim/pull/832))

- Move upcoming changelog to GitHub-wiki ( [#822](https://github.com/ManimCommunity/manim/pull/822))

- Change badges in readme ( [#854](https://github.com/ManimCommunity/manim/pull/854))

- Exclude generated gRPC files from source control ( [#868](https://github.com/ManimCommunity/manim/pull/868))

- Added linguist-generated attribute to `.gitattributes` ( [#877](https://github.com/ManimCommunity/manim/pull/877))

- Cleanup: removed inheritance from `object` for some classes, refactor some imports ( [#795](https://github.com/ManimCommunity/manim/pull/795))

- Change several `str.format()` to `f`-strings ( [#867](https://github.com/ManimCommunity/manim/pull/867))

- Update javascript renderer ( [#830](https://github.com/ManimCommunity/manim/pull/830))

- Bump version number to 0.2.0, update changelog ( [#894](https://github.com/ManimCommunity/manim/pull/894))