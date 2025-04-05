ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Octahedron.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Octahedron.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Octahedron [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Octahedron.html\#octahedron "Link to this heading")

Qualified name: `manim.mobject.three\_d.polyhedra.Octahedron`

_class_ Octahedron( _edge\_length=1_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/polyhedra.html#Octahedron) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Octahedron.html#manim.mobject.three_d.polyhedra.Octahedron "Link to this definition")

Bases: [`Polyhedron`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Polyhedron.html#manim.mobject.three_d.polyhedra.Polyhedron "manim.mobject.three_d.polyhedra.Polyhedron")

An octahedron, one of the five platonic solids. It has 8 faces, 12 edges and 6 vertices.

Parameters:

**edge\_length** ( _float_) – The length of an edge between any two vertices.

Examples

Example: OctahedronScene [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Octahedron.html#octahedronscene)

![../_images/OctahedronScene-1.png](https://docs.manim.community/en/stable/_images/OctahedronScene-1.png)

```
from manim import *

class OctahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        obj = Octahedron()
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

\_original\_\_init\_\_( _edge\_length=1_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Octahedron.html#manim.mobject.three_d.polyhedra.Octahedron._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**edge\_length** ( _float_)

[**The AI Agent that gets your codebase** Copilot & Cursor letting you down? Try Augment. **Install Now**](https://server.ethicalads.io/proxy/click/8458/019600e1-a464-71e2-baac-eb6a5afe0fb4/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8458/019600e1-a464-71e2-baac-eb6a5afe0fb4/)