ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CubicBezier.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CubicBezier.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# CubicBezier [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CubicBezier.html\#cubicbezier "Link to this heading")

Qualified name: `manim.mobject.geometry.arc.CubicBezier`

_class_ CubicBezier( _start\_anchor_, _start\_handle_, _end\_handle_, _end\_anchor_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#CubicBezier) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CubicBezier.html#manim.mobject.geometry.arc.CubicBezier "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

A cubic Bézier curve.

Example

Example: BezierSplineExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CubicBezier.html#beziersplineexample)

![../_images/BezierSplineExample-1.png](https://docs.manim.community/en/stable/_images/BezierSplineExample-1.png)

```
from manim import *

class BezierSplineExample(Scene):
    def construct(self):
        p1 = np.array([-3, 1, 0])
        p1b = p1 + [1, 0, 0]
        d1 = Dot(point=p1).set_color(BLUE)
        l1 = Line(p1, p1b)
        p2 = np.array([3, -1, 0])
        p2b = p2 - [1, 0, 0]
        d2 = Dot(point=p2).set_color(RED)
        l2 = Line(p2, p2b)
        bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
        self.add(l1, d1, l2, d2, bezier)

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

Parameters:

- **start\_anchor** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **start\_handle** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **end\_handle** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **end\_anchor** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _start\_anchor_, _start\_handle_, _end\_handle_, _end\_anchor_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CubicBezier.html#manim.mobject.geometry.arc.CubicBezier._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **start\_anchor** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **start\_handle** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **end\_handle** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **end\_anchor** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **kwargs** ( _Any_)


Return type:

None

[Develop and launch modern apps with MongoDB Atlas, a resilient data platform.](https://server.ethicalads.io/proxy/click/8269/019600ed-3c82-7053-b0f1-9fa09ad5f74c/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8269/019600ed-3c82-7053-b0f1-9fa09ad5f74c/)