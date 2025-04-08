ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.growing.SpinInFromNothing.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.growing.SpinInFromNothing.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# SpinInFromNothing [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.SpinInFromNothing.html\#spininfromnothing "Link to this heading")

Qualified name: `manim.animation.growing.SpinInFromNothing`

_class_ SpinInFromNothing( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/growing.html#SpinInFromNothing) [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.SpinInFromNothing.html#manim.animation.growing.SpinInFromNothing "Link to this definition")

Bases: [`GrowFromCenter`](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromCenter.html#manim.animation.growing.GrowFromCenter "manim.animation.growing.GrowFromCenter")

Introduce an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") spinning and growing it from its center.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to be introduced.

- **angle** ( _float_) – The amount of spinning before mobject reaches its full size. E.g. 2\*PI means
that the object will do one full spin before being fully introduced.

- **point\_color** ( _str_) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.


Examples

Example: SpinInFromNothingExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.SpinInFromNothing.html#spininfromnothingexample)

```
from manim import *

class SpinInFromNothingExample(Scene):
    def construct(self):
        squares = [Square() for _ in range(3)]
        VGroup(*squares).set_x(0).arrange(buff=2)
        self.play(SpinInFromNothing(squares[0]))
        self.play(SpinInFromNothing(squares[1], angle=2 * PI))
        self.play(SpinInFromNothing(squares[2], point_color=RED))

```

Copy to clipboard

Make interactive

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

\_original\_\_init\_\_( _mobject_, _angle=1.5707963267948966_, _point\_color=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.SpinInFromNothing.html#manim.animation.growing.SpinInFromNothing._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **angle** ( _float_)

- **point\_color** ( _str_)


Return type:

None