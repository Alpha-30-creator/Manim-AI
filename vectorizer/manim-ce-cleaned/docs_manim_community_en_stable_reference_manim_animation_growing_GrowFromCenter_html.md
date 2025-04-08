# GrowFromCenter [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromCenter.html\#growfromcenter "Link to this heading")

Qualified name: `manim.animation.growing.GrowFromCenter`

_class_ GrowFromCenter( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/growing.html#GrowFromCenter) [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromCenter.html#manim.animation.growing.GrowFromCenter "Link to this definition")

Bases: [`GrowFromPoint`](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html#manim.animation.growing.GrowFromPoint "manim.animation.growing.GrowFromPoint")

Introduce an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") by growing it from its center.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to be introduced.

- **point\_color** ( _str_) – Initial color of the mobject before growing to its full size. Leave empty to match mobject’s color.


Examples

Example: GrowFromCenterExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromCenter.html#growfromcenterexample)

```
from manim import *

class GrowFromCenterExample(Scene):
    def construct(self):
        squares = [Square() for _ in range(2)]
        VGroup(*squares).set_x(0).arrange(buff=2)
        self.play(GrowFromCenter(squares[0]))
        self.play(GrowFromCenter(squares[1], point_color=RED))

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

\_original\_\_init\_\_( _mobject_, _point\_color=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromCenter.html#manim.animation.growing.GrowFromCenter._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **point\_color** ( _str_)


Return type:

None