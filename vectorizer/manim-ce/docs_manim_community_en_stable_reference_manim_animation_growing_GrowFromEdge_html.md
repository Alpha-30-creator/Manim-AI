ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromEdge.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromEdge.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# GrowFromEdge [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromEdge.html\#growfromedge "Link to this heading")

Qualified name: `manim.animation.growing.GrowFromEdge`

_class_ GrowFromEdge( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/growing.html#GrowFromEdge) [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromEdge.html#manim.animation.growing.GrowFromEdge "Link to this definition")

Bases: [`GrowFromPoint`](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html#manim.animation.growing.GrowFromPoint "manim.animation.growing.GrowFromPoint")

Introduce an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") by growing it from one of its bounding box edges.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to be introduced.

- **edge** ( _np.ndarray_) – The direction to seek bounding box edge of mobject.

- **point\_color** ( _str_) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.


Examples

Example: GrowFromEdgeExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromEdge.html#growfromedgeexample)

```
from manim import *

class GrowFromEdgeExample(Scene):
    def construct(self):
        squares = [Square() for _ in range(4)]
        VGroup(*squares).set_x(0).arrange(buff=1)
        self.play(GrowFromEdge(squares[0], DOWN))
        self.play(GrowFromEdge(squares[1], RIGHT))
        self.play(GrowFromEdge(squares[2], UR))
        self.play(GrowFromEdge(squares[3], UP, point_color=RED))

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

\_original\_\_init\_\_( _mobject_, _edge_, _point\_color=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromEdge.html#manim.animation.growing.GrowFromEdge._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **edge** ( _np.ndarray_)

- **point\_color** ( _str_)


Return type:

None