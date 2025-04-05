ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# BackgroundRectangle [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html\#backgroundrectangle "Link to this heading")

Qualified name: `manim.mobject.geometry.shape\_matchers.BackgroundRectangle`

_class_ BackgroundRectangle( _\*mobjects_, _color=None_, _stroke\_width=0_, _stroke\_opacity=0_, _fill\_opacity=0.75_, _buff=0_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/shape_matchers.html#BackgroundRectangle) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "Link to this definition")

Bases: [`SurroundingRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.SurroundingRectangle.html#manim.mobject.geometry.shape_matchers.SurroundingRectangle "manim.mobject.geometry.shape_matchers.SurroundingRectangle")

A background rectangle. Its default color is the background color
of the scene.

Examples

Example: ExampleBackgroundRectangle [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#examplebackgroundrectangle)

![../_images/ExampleBackgroundRectangle-1.png](https://docs.manim.community/en/stable/_images/ExampleBackgroundRectangle-1.png)

```
from manim import *

class ExampleBackgroundRectangle(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        circle.set_stroke(color=GREEN, width=20)
        triangle = Triangle().shift(2 * RIGHT)
        triangle.set_fill(PINK, opacity=0.5)
        backgroundRectangle1 = BackgroundRectangle(circle, color=WHITE, fill_opacity=0.15)
        backgroundRectangle2 = BackgroundRectangle(triangle, color=WHITE, fill_opacity=0.15)
        self.add(backgroundRectangle1)
        self.add(backgroundRectangle2)
        self.add(circle)
        self.add(triangle)
        self.play(Rotate(backgroundRectangle1, PI / 4))
        self.play(Rotate(backgroundRectangle2, PI / 2))

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`get_fill_color`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle.get_fill_color "manim.mobject.geometry.shape_matchers.BackgroundRectangle.get_fill_color") | If there are multiple colors (for gradient) this returns the first one |
| [`pointwise_become_partial`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle.pointwise_become_partial "manim.mobject.geometry.shape_matchers.BackgroundRectangle.pointwise_become_partial") | Given a 2nd [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") `vmobject`, a lower bound `a` and an upper bound `b`, modify this [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")'s points to match the portion of the Bézier spline described by `vmobject.points` with the parameter `t` between `a` and `b`. |
| `set_style` |  |

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

Parameters:

- **mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_)

- **stroke\_width** ( _float_)

- **stroke\_opacity** ( _float_)

- **fill\_opacity** ( _float_)

- **buff** ( _float_)

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _\*mobjects_, _color=None_, _stroke\_width=0_, _stroke\_opacity=0_, _fill\_opacity=0.75_, _buff=0_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_)

- **stroke\_width** ( _float_)

- **stroke\_opacity** ( _float_)

- **fill\_opacity** ( _float_)

- **buff** ( _float_)

- **kwargs** ( _Any_)


Return type:

None

get\_fill\_color() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/shape_matchers.html#BackgroundRectangle.get_fill_color) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle.get_fill_color "Link to this definition")

If there are multiple colors (for gradient)
this returns the first one

Return type:

[_ManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

pointwise\_become\_partial( _mobject_, _a_, _b_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/shape_matchers.html#BackgroundRectangle.pointwise_become_partial) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle.pointwise_become_partial "Link to this definition")

Given a 2nd [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") `vmobject`, a lower bound `a` and
an upper bound `b`, modify this [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")’s points to
match the portion of the Bézier spline described by `vmobject.points`
with the parameter `t` between `a` and `b`.

Parameters:

- **vmobject** – The [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") that will serve as a model.

- **a** ( _Any_) – The lower bound for `t`.

- **b** ( _float_) – The upper bound for `t`

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Returns:

The [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") itself, after the transformation.

Return type:

[`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

Raises:

**TypeError** – If `vmobject` is not an instance of `VMobject`.

[Develop and launch modern apps with MongoDB Atlas, a resilient data platform.](https://server.ethicalads.io/proxy/click/8269/019600eb-e59a-7410-9fcd-4e9f9f9e4fa3/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8269/019600eb-e59a-7410-9fcd-4e9f9f9e4fa3/)