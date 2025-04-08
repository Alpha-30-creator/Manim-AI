ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ManimBanner [¶](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html\#manimbanner "Link to this heading")

Qualified name: `manim.mobject.logo.ManimBanner`

_class_ ManimBanner( _dark\_theme=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/logo.html#ManimBanner) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner "Link to this definition")

Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Convenience class representing Manim’s banner.

Can be animated using custom methods.

Parameters:

**dark\_theme** ( _bool_) – If `True` (the default), the dark theme version of the logo
(with light text font) will be rendered. Otherwise, if `False`,
the light theme version (with dark text font) is used.

Examples

Example: DarkThemeBanner [¶](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#darkthemebanner)

```
from manim import *

class DarkThemeBanner(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))

```

Copy to clipboard

Make interactive

Example: LightThemeBanner [¶](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#lightthemebanner)

```
from manim import *

class LightThemeBanner(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        banner = ManimBanner(dark_theme=False)
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`create`](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner.create "manim.mobject.logo.ManimBanner.create") | The creation animation for Manim's logo. |
| [`expand`](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner.expand "manim.mobject.logo.ManimBanner.expand") | An animation that expands Manim's logo into its banner. |
| [`scale`](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner.scale "manim.mobject.logo.ManimBanner.scale") | Scale the banner by the specified scale factor. |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

\_original\_\_init\_\_( _dark\_theme=True_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**dark\_theme** ( _bool_)

create( _run\_time=2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/logo.html#ManimBanner.create) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner.create "Link to this definition")

The creation animation for Manim’s logo.

Parameters:

**run\_time** ( _float_) – The run time of the animation.

Returns:

An animation to be used in a [`Scene.play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") call.

Return type:

[`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

expand( _run\_time=1.5_, _direction='center'_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/logo.html#ManimBanner.expand) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner.expand "Link to this definition")

An animation that expands Manim’s logo into its banner.

The returned animation transforms the banner from its initial
state (representing Manim’s logo with just the icons) to its
expanded state (showing the full name together with the icons).

See the class documentation for how to use this.

Note

Before calling this method, the text “anim” is not a
submobject of the banner object. After the expansion,
it is added as a submobject so subsequent animations
to the banner object apply to the text “anim” as well.

Parameters:

- **run\_time** ( _float_) – The run time of the animation.

- **direction** – The direction in which the logo is expanded.


Returns:

An animation to be used in a [`Scene.play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") call.

Return type:

[`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession")

Examples

Example: ExpandDirections [¶](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#expanddirections)

```
from manim import *

class ExpandDirections(Scene):
    def construct(self):
        banners = [ManimBanner().scale(0.5).shift(UP*x) for x in [-2, 0, 2]]
        self.play(
            banners[0].expand(direction="right"),
            banners[1].expand(direction="center"),
            banners[2].expand(direction="left"),
        )

```

Copy to clipboard

Make interactive

scale( _scale\_factor_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/logo.html#ManimBanner.scale) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner.scale "Link to this definition")

Scale the banner by the specified scale factor.

Parameters:

**scale\_factor** ( _float_) – The factor used for scaling the banner.

Returns:

The scaled banner.

Return type:

[`ManimBanner`](https://docs.manim.community/en/stable/reference/manim.mobject.logo.ManimBanner.html#manim.mobject.logo.ManimBanner "manim.mobject.logo.ManimBanner")