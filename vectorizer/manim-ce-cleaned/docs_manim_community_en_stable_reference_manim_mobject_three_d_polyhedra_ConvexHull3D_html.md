# ConvexHull3D [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.ConvexHull3D.html\#convexhull3d "Link to this heading")

Qualified name: `manim.mobject.three\_d.polyhedra.ConvexHull3D`

_class_ ConvexHull3D( _\*points_, _tolerance=1e-05_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/polyhedra.html#ConvexHull3D) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.ConvexHull3D.html#manim.mobject.three_d.polyhedra.ConvexHull3D "Link to this definition")

Bases: [`Polyhedron`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Polyhedron.html#manim.mobject.three_d.polyhedra.Polyhedron "manim.mobject.three_d.polyhedra.Polyhedron")

A convex hull for a set of points

Parameters:

- **points** ( [_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")) – The points to consider.

- **tolerance** ( _float_) – The tolerance used for quickhull.

- **kwargs** – Forwarded to the parent constructor.


Examples

Example: ConvexHull3DExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.ConvexHull3D.html#convexhull3dexample)

![../_images/ConvexHull3DExample-1.png](https://docs.manim.community/en/stable/_images/ConvexHull3DExample-1.png)

```
from manim import *

class ConvexHull3DExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        points = [\
            [ 1.93192757,  0.44134585, -1.52407061],\
            [-0.93302521,  1.23206983,  0.64117067],\
            [-0.44350918, -0.61043677,  0.21723705],\
            [-0.42640268, -1.05260843,  1.61266094],\
            [-1.84449637,  0.91238739, -1.85172623],\
            [ 1.72068132, -0.11880457,  0.51881751],\
            [ 0.41904805,  0.44938012, -1.86440686],\
            [ 0.83864666,  1.66653337,  1.88960123],\
            [ 0.22240514, -0.80986286,  1.34249326],\
            [-1.29585759,  1.01516189,  0.46187522],\
            [ 1.7776499,  -1.59550796, -1.70240747],\
            [ 0.80065226, -0.12530398,  1.70063977],\
            [ 1.28960948, -1.44158255,  1.39938582],\
            [-0.93538943,  1.33617705, -0.24852643],\
            [-1.54868271,  1.7444399,  -0.46170734]\
        ]
        hull = ConvexHull3D(
            *points,
            faces_config = {"stroke_opacity": 0},
            graph_config = {
                "vertex_type": Dot3D,
                "edge_config": {
                    "stroke_color": BLUE,
                    "stroke_width": 2,
                    "stroke_opacity": 0.05,
                }
            }
        )
        dots = VGroup(*[Dot3D(point) for point in points])
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

\_original\_\_init\_\_( _\*points_, _tolerance=1e-05_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.ConvexHull3D.html#manim.mobject.three_d.polyhedra.ConvexHull3D._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **points** ( [_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"))

- **tolerance** ( _float_)


[**The AI Agent that gets your codebase** Copilot & Cursor letting you down? Try Augment. **Install Now**](https://server.ethicalads.io/proxy/click/8458/019600f4-c436-74f3-916f-35c3186d4d9d/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8458/019600f4-c436-74f3-916f-35c3186d4d9d/)