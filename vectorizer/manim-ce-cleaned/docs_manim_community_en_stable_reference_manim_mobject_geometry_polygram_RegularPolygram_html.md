# RegularPolygram [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygram.html\#regularpolygram "Link to this heading")

Qualified name: `manim.mobject.geometry.polygram.RegularPolygram`

_class_ RegularPolygram( _num\_vertices_, _\*_, _density=2_, _radius=1_, _start\_angle=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/polygram.html#RegularPolygram) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygram.html#manim.mobject.geometry.polygram.RegularPolygram "Link to this definition")

Bases: [`Polygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram")

A [`Polygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram "manim.mobject.geometry.polygram.Polygram") with regularly spaced vertices.

Parameters:

- **num\_vertices** ( _int_) – The number of vertices.

- **density** ( _int_) –

The density of the [`RegularPolygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygram.html#manim.mobject.geometry.polygram.RegularPolygram "manim.mobject.geometry.polygram.RegularPolygram").

Can be thought of as how many vertices to hop
to draw a line between them. Every `density`-th
vertex is connected.

- **radius** ( _float_) – The radius of the circle that the vertices are placed on.

- **start\_angle** ( _float_ _\|_ _None_) – The angle the vertices start at; the rotation of
the [`RegularPolygram`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygram.html#manim.mobject.geometry.polygram.RegularPolygram "manim.mobject.geometry.polygram.RegularPolygram").

- **kwargs** ( _Any_) – Forwarded to the parent constructor.


Examples

Example: RegularPolygramExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygram.html#regularpolygramexample)

![../_images/RegularPolygramExample-1.png](https://docs.manim.community/en/stable/_images/RegularPolygramExample-1.png)

```
from manim import *

class RegularPolygramExample(Scene):
    def construct(self):
        pentagram = RegularPolygram(5, radius=2)
        self.add(pentagram)

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

\_original\_\_init\_\_( _num\_vertices_, _\*_, _density=2_, _radius=1_, _start\_angle=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygram.html#manim.mobject.geometry.polygram.RegularPolygram._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **num\_vertices** ( _int_)

- **density** ( _int_)

- **radius** ( _float_)

- **start\_angle** ( _float_ _\|_ _None_)

- **kwargs** ( _Any_)


Return type:

None