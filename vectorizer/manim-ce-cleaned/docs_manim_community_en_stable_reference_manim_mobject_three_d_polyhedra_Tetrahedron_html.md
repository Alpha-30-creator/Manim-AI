# Tetrahedron [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html\#tetrahedron "Link to this heading")

Qualified name: `manim.mobject.three\_d.polyhedra.Tetrahedron`

_class_ Tetrahedron( _edge\_length=1_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/polyhedra.html#Tetrahedron) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html#manim.mobject.three_d.polyhedra.Tetrahedron "Link to this definition")

Bases: [`Polyhedron`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Polyhedron.html#manim.mobject.three_d.polyhedra.Polyhedron "manim.mobject.three_d.polyhedra.Polyhedron")

A tetrahedron, one of the five platonic solids. It has 4 faces, 6 edges, and 4 vertices.

Parameters:

**edge\_length** ( _float_) – The length of an edge between any two vertices.

Examples

Example: TetrahedronScene [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html#tetrahedronscene)

![../_images/TetrahedronScene-1.png](https://docs.manim.community/en/stable/_images/TetrahedronScene-1.png)

```
from manim import *

class TetrahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        obj = Tetrahedron()
        self.add(obj)

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

\_original\_\_init\_\_( _edge\_length=1_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Tetrahedron.html#manim.mobject.three_d.polyhedra.Tetrahedron._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**edge\_length** ( _float_)

[**The AI Agent that gets your codebase** Copilot & Cursor letting you down? Try Augment. **Install Now**](https://server.ethicalads.io/proxy/click/8458/019600e7-c054-7493-99a8-ad194c02b457/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8458/019600e7-c054-7493-99a8-ad194c02b457/)