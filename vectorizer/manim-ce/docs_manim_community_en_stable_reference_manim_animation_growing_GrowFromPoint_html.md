ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# GrowFromPoint [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html\#growfrompoint "Link to this heading")

Qualified name: `manim.animation.growing.GrowFromPoint`

_class_ GrowFromPoint( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/growing.html#GrowFromPoint) [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html#manim.animation.growing.GrowFromPoint "Link to this definition")

Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

Introduce an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") by growing it from a point.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to be introduced.

- **point** ( _np.ndarray_) – The point from which the mobject grows.

- **point\_color** ( _str_) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.


Examples

Example: GrowFromPointExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html#growfrompointexample)

```
from manim import *

class GrowFromPointExample(Scene):
    def construct(self):
        dot = Dot(3 * UR, color=GREEN)
        squares = [Square() for _ in range(4)]
        VGroup(*squares).set_x(0).arrange(buff=1)
        self.add(dot)
        self.play(GrowFromPoint(squares[0], ORIGIN))
        self.play(GrowFromPoint(squares[1], [-2, 2, 0]))
        self.play(GrowFromPoint(squares[2], [3, -2, 0], RED))
        self.play(GrowFromPoint(squares[3], dot, dot.get_color()))

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `create_starting_mobject` |  |
| `create_target` |  |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

\_original\_\_init\_\_( _mobject_, _point_, _point\_color=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html#manim.animation.growing.GrowFromPoint._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **point** ( _np.ndarray_)

- **point\_color** ( _str_)


Return type:

None