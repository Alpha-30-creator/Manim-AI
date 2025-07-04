ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DoubleArrow.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DoubleArrow.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# DoubleArrow [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DoubleArrow.html\#doublearrow "Link to this heading")

Qualified name: `manim.mobject.geometry.line.DoubleArrow`

_class_ DoubleArrow( _\*args_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#DoubleArrow) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DoubleArrow.html#manim.mobject.geometry.line.DoubleArrow "Link to this definition")

Bases: [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")

An arrow with tips on both ends.

Parameters:

- **args** ( _Any_) – Arguments to be passed to [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")

- **kwargs** ( _Any_) – Additional arguments to be passed to [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")


See also

`ArrowTip` `CurvedDoubleArrow`

Examples

Example: DoubleArrowExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DoubleArrow.html#doublearrowexample)

![../_images/DoubleArrowExample-1.png](https://docs.manim.community/en/stable/_images/DoubleArrowExample-1.png)

```
from manim import *

from manim.mobject.geometry.tips import ArrowCircleFilledTip
class DoubleArrowExample(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        d_arrow = DoubleArrow(start=circle.get_left(), end=circle.get_right())
        d_arrow_2 = DoubleArrow(tip_shape_end=ArrowCircleFilledTip, tip_shape_start=ArrowCircleFilledTip)
        group = Group(Group(circle, d_arrow), d_arrow_2).arrange(UP, buff=1)
        self.add(group)

```

Copy to clipboard

Make interactive

Example: DoubleArrowExample2 [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DoubleArrow.html#doublearrowexample2)

![../_images/DoubleArrowExample2-1.png](https://docs.manim.community/en/stable/_images/DoubleArrowExample2-1.png)

```
from manim import *

class DoubleArrowExample2(Scene):
    def construct(self):
        box = Square()
        p1 = box.get_left()
        p2 = box.get_right()
        d1 = DoubleArrow(p1, p2, buff=0)
        d2 = DoubleArrow(p1, p2, buff=0, tip_length=0.2, color=YELLOW)
        d3 = DoubleArrow(p1, p2, buff=0, tip_length=0.4, color=BLUE)
        Group(d1, d2, d3).arrange(DOWN)
        self.add(box, d1, d2, d3)

```

Copy to clipboard

Make interactive

Methods

|
|

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

\_original\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DoubleArrow.html#manim.mobject.geometry.line.DoubleArrow._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **args** ( _Any_)

- **kwargs** ( _Any_)


Return type:

None