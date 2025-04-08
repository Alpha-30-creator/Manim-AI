# BraceBetweenPoints [¶](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html\#bracebetweenpoints "Link to this heading")

Qualified name: `manim.mobject.svg.brace.BraceBetweenPoints`

_class_ BraceBetweenPoints( _point\_1_, _point\_2_, _direction=array(\[0.,0.,0.\])_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/svg/brace.html#BraceBetweenPoints) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html#manim.mobject.svg.brace.BraceBetweenPoints "Link to this definition")

Bases: [`Brace`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace "manim.mobject.svg.brace.Brace")

Similar to Brace, but instead of taking a mobject it uses 2
points to place the brace.

A fitting direction for the brace is
computed, but it still can be manually overridden.
If the points go from left to right, the brace is drawn from below.
Swapping the points places the brace on the opposite side.

Parameters:

- **point\_1** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\|_ _None_) – The first point.

- **point\_2** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\|_ _None_) – The second point.

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D") _\|_ _None_) – The direction from which the brace faces towards the points.


Examples

Example: BraceBPExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html#bracebpexample)

```
from manim import *

class BraceBPExample(Scene):
    def construct(self):
        p1 = [0,0,0]
        p2 = [1,2,0]
        brace = BraceBetweenPoints(p1,p2)
        self.play(Create(NumberPlane()))
        self.play(Create(brace))
        self.wait(2)

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

\_original\_\_init\_\_( _point\_1_, _point\_2_, _direction=array(\[0.,0.,0.\])_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html#manim.mobject.svg.brace.BraceBetweenPoints._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **point\_1** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\|_ _None_)

- **point\_2** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\|_ _None_)

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D") _\|_ _None_)


[Develop and launch modern apps with MongoDB Atlas, a resilient data platform.](https://server.ethicalads.io/proxy/click/8269/019600e5-4a58-71e3-8951-b125dc3ec634/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8269/019600e5-4a58-71e3-8951-b125dc3ec634/)