ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/changelog/0.1.1-changelog.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/changelog/0.1.1-changelog.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# v0.1.1 [¶](https://docs.manim.community/en/stable/changelog/0.1.1-changelog.html\#v0-1-1 "Link to this heading")

Date:

December 1, 2020

Changes since Manim Community release v0.1.0

## Plugins [¶](https://docs.manim.community/en/stable/changelog/0.1.1-changelog.html\#plugins "Link to this heading")

1. Provided a standardized method for plugin discoverability, creation,
installation, and usage. See the [documentation](https://docs.manim.community/en/stable/plugins.html#plugins).


## Fixes [¶](https://docs.manim.community/en/stable/changelog/0.1.1-changelog.html\#fixes "Link to this heading")

1. JsRender is optional to install. (via [#697](https://github.com/ManimCommunity/manim/pull/697)).

2. Allow importing modules from the same directory as the input
file when using `manim` from the command line (via [#724](https://github.com/ManimCommunity/manim/pull/724)).

3. Remove some unnecessary or unpythonic methods from [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")
( `get_mobjects`, `add_mobjects_among`, `get_mobject_copies`),
via [#758](https://github.com/ManimCommunity/manim/pull/758).

4. Fix formatting of [`Code`](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code "manim.mobject.text.code_mobject.Code") (via [#798](https://github.com/ManimCommunity/manim/pull/798)).


## Configuration [¶](https://docs.manim.community/en/stable/changelog/0.1.1-changelog.html\#configuration "Link to this heading")

1. Removed the `skip_animations` config option and added the
`Renderer.skip_animations` attribute instead (via [#696](https://github.com/ManimCommunity/manim/pull/696)).

2. The global `config` dict has been replaced by a global `config` instance
of the new class [`ManimConfig`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "manim._config.utils.ManimConfig"). This class has a dict-like API, so
this should not break user code, only make it more robust. See the
Configuration tutorial for details.

3. Added the option to configure a directory for external assets (via [#649](https://github.com/ManimCommunity/manim/pull/649)).


## Documentation [¶](https://docs.manim.community/en/stable/changelog/0.1.1-changelog.html\#documentation "Link to this heading")

1. Add `:issue:` and `:pr:` directives for simplifying linking to issues and
pull requests on GitHub (via [#685](https://github.com/ManimCommunity/manim/pull/685)).

2. Add a `skip-manim` tag for skipping the `.. manim::` directive when
building the documentation locally (via [#796](https://github.com/ManimCommunity/manim/pull/796)).


## Mobjects, Scenes, and Animations [¶](https://docs.manim.community/en/stable/changelog/0.1.1-changelog.html\#mobjects-scenes-and-animations "Link to this heading")

01. The `alignment` attribute to Tex and MathTex has been removed in favour of `tex_environment`.

02. [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") now uses Pango for rendering. `PangoText` has been removed. The old implementation is still available as a fallback as `CairoText`.

03. Variations of [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot "manim.mobject.geometry.arc.Dot") have been added as [`AnnotationDot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.AnnotationDot.html#manim.mobject.geometry.arc.AnnotationDot "manim.mobject.geometry.arc.AnnotationDot")
    (a bigger dot with bolder stroke) and [`LabeledDot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.LabeledDot.html#manim.mobject.geometry.arc.LabeledDot "manim.mobject.geometry.arc.LabeledDot") (a dot containing a
    label).

04. Scene.set\_variables\_as\_attrs has been removed (via [#692](https://github.com/ManimCommunity/manim/pull/692)).

05. Ensure that the axes for graphs ( `GraphScene`) always intersect ( [#580](https://github.com/ManimCommunity/manim/pull/580)).

06. Now Mobject.add\_updater does not call the newly-added updater by default
    (use `call_updater=True` instead) (via [#710](https://github.com/ManimCommunity/manim/pull/710))

07. VMobject now has methods to determine and change the direction of the points (via [#647](https://github.com/ManimCommunity/manim/pull/647)).

08. Added BraceBetweenPoints (via [#693](https://github.com/ManimCommunity/manim/pull/693)).

09. Added ArcPolygon and ArcPolygonFromArcs (via [#707](https://github.com/ManimCommunity/manim/pull/707)).

10. Added Cutout (via [#760](https://github.com/ManimCommunity/manim/pull/760)).

11. Added Mobject raise not implemented errors for dunder methods and implementations for VGroup dunder methods (via [#790](https://github.com/ManimCommunity/manim/pull/790)).

12. Added [`ManimBanner`](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner "manim.mobject.logo.ManimBanner") for a animated version of our logo and banner (via [#729](https://github.com/ManimCommunity/manim/pull/729))

13. The background color of a scene can now be changed reliably by setting, e.g.,
    `self.camera.background_color = RED` (via [#716](https://github.com/ManimCommunity/manim/pull/716)).