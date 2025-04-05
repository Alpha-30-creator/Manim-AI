ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.creation.SpiralIn.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.creation.SpiralIn.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# SpiralIn [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.SpiralIn.html\#spiralin "Link to this heading")

Qualified name: `manim.animation.creation.SpiralIn`

_class_ SpiralIn( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#SpiralIn) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.SpiralIn.html#manim.animation.creation.SpiralIn "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

Create the Mobject with sub-Mobjects flying in on spiral trajectories.

Parameters:

- **shapes** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The Mobject on which to be operated.

- **scale\_factor** ( _float_) – The factor used for scaling the effect.

- **fade\_in\_fraction** – Fractional duration of initial fade-in of sub-Mobjects as they fly inward.


Examples

Example: SpiralInExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.SpiralIn.html#spiralinexample)

```
from manim import *

class SpiralInExample(Scene):
    def construct(self):
        pi = MathTex(r"\pi").scale(7)
        pi.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=GREEN_C, fill_opacity=1).shift(LEFT)
        square = Square(color=BLUE_D, fill_opacity=1).shift(UP)
        shapes = VGroup(pi, circle, square)
        self.play(SpiralIn(shapes))

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`interpolate_mobject`](https://docs.manim.community/en/stable/reference/manim.animation.creation.SpiralIn.html#manim.animation.creation.SpiralIn.interpolate_mobject "manim.animation.creation.SpiralIn.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _shapes_, _scale\_factor=8_, _fade\_in\_fraction=0.3_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.SpiralIn.html#manim.animation.creation.SpiralIn._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **shapes** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **scale\_factor** ( _float_)


Return type:

None

interpolate\_mobject( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#SpiralIn.interpolate_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.SpiralIn.html#manim.animation.creation.SpiralIn.interpolate_mobject "Link to this definition")

Interpolates the mobject of the `Animation` based on alpha value.

Parameters:

**alpha** ( _float_) – A float between 0 and 1 expressing the ratio to which the animation
is completed. For example, alpha-values of 0, 0.5, and 1 correspond
to the animation being completed 0%, 50%, and 100%, respectively.

Return type:

None