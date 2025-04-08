# CurvesAsSubmobjects [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html\#curvesassubmobjects "Link to this heading")

Qualified name: `manim.mobject.types.vectorized\_mobject.CurvesAsSubmobjects`

_class_ CurvesAsSubmobjects( _vmobject_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html#CurvesAsSubmobjects) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "Link to this definition")

Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Convert a curve’s elements to submobjects.

Examples

Example: LineGradientExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html#linegradientexample)

![../_images/LineGradientExample-1.png](https://docs.manim.community/en/stable/_images/LineGradientExample-1.png)

```
from manim import *

class LineGradientExample(Scene):
    def construct(self):
        curve = ParametricFunction(lambda t: [t, np.sin(t), 0], t_range=[-PI, PI, 0.01], stroke_width=10)
        new_curve = CurvesAsSubmobjects(curve)
        new_curve.set_color_by_gradient(BLUE, RED)
        self.add(new_curve.shift(UP), curve)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`point_from_proportion`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.point_from_proportion "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.point_from_proportion") | Gets the point at a proportion along the path of the [`CurvesAsSubmobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects"). |

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

**vmobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

\_original\_\_init\_\_( _vmobject_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**vmobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

Return type:

None

point\_from\_proportion( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html#CurvesAsSubmobjects.point_from_proportion) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.point_from_proportion "Link to this definition")

Gets the point at a proportion along the path of the [`CurvesAsSubmobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects").

Parameters:

**alpha** ( _float_) – The proportion along the the path of the [`CurvesAsSubmobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects").

Returns:

The point on the [`CurvesAsSubmobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects").

Return type:

`numpy.ndarray`

Raises:

- **ValueError** – If `alpha` is not between 0 and 1.

- **Exception** – If the [`CurvesAsSubmobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects") has no submobjects, or no submobject has points.


[**Watch Our Demo** video to see firsthand how to upgrade your site with end-to-end AI Search.](https://server.ethicalads.io/proxy/click/8294/019600e7-8ff6-75d1-a0c4-cbf072d6581b/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/frontend-web/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8294/019600e7-8ff6-75d1-a0c4-cbf072d6581b/)