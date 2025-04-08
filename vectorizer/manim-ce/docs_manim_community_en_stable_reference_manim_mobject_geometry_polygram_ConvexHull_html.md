ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.ConvexHull.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.ConvexHull.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ConvexHull [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.ConvexHull.html\#convexhull "Link to this heading")

Qualified name: `manim.mobject.geometry.polygram.ConvexHull`

_class_ ConvexHull( _\*points_, _tolerance=1e-05_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/polygram.html#ConvexHull) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.ConvexHull.html#manim.mobject.geometry.polygram.ConvexHull "Link to this definition")

Bases: [`Polygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram")

Constructs a convex hull for a set of points in no particular order.

Parameters:

- **points** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The points to consider.

- **tolerance** ( _float_) – The tolerance used by quickhull.

- **kwargs** ( _Any_) – Forwarded to the parent constructor.


Examples

Example: ConvexHullExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.ConvexHull.html#convexhullexample)

![../_images/ConvexHullExample-1.png](https://docs.manim.community/en/stable/_images/ConvexHullExample-1.png)

```
from manim import *

class ConvexHullExample(Scene):
    def construct(self):
        points = [\
            [-2.35, -2.25, 0],\
            [1.65, -2.25, 0],\
            [2.65, -0.25, 0],\
            [1.65, 1.75, 0],\
            [-0.35, 2.75, 0],\
            [-2.35, 0.75, 0],\
            [-0.35, -1.25, 0],\
            [0.65, -0.25, 0],\
            [-1.35, 0.25, 0],\
            [0.15, 0.75, 0]\
        ]
        hull = ConvexHull(*points, color=BLUE)
        dots = VGroup(*[Dot(point) for point in points])
        self.add(hull)
        self.add(dots)

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

\_original\_\_init\_\_( _\*points_, _tolerance=1e-05_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.ConvexHull.html#manim.mobject.geometry.polygram.ConvexHull._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **points** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **tolerance** ( _float_)

- **kwargs** ( _Any_)


Return type:

None