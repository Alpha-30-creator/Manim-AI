ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Triangle.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Triangle.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Triangle [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Triangle.html\#triangle "Link to this heading")

Qualified name: `manim.mobject.geometry.polygram.Triangle`

_class_ Triangle( _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/polygram.html#Triangle) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Triangle.html#manim.mobject.geometry.polygram.Triangle "Link to this definition")

Bases: [`RegularPolygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygon.html#manim.mobject.geometry.polygram.RegularPolygon "manim.mobject.geometry.polygram.RegularPolygon")

An equilateral triangle.

Parameters:

**kwargs** ( _Any_) – Additional arguments to be passed to [`RegularPolygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.RegularPolygon.html#manim.mobject.geometry.polygram.RegularPolygon "manim.mobject.geometry.polygram.RegularPolygon")

Examples

Example: TriangleExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Triangle.html#triangleexample)

![../_images/TriangleExample-1.png](https://docs.manim.community/en/stable/_images/TriangleExample-1.png)

```
from manim import *

class TriangleExample(Scene):
    def construct(self):
        triangle_1 = Triangle()
        triangle_2 = Triangle().scale(2).rotate(60*DEGREES)
        tri_group = Group(triangle_1, triangle_2).arrange(buff=1)
        self.add(tri_group)

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

\_original\_\_init\_\_( _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Triangle.html#manim.mobject.geometry.polygram.Triangle._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**kwargs** ( _Any_)

Return type:

None

[**Document Extraction for Developers** Transform docs into structured data with Sensible. **Try for free →**](https://server.ethicalads.io/proxy/click/8518/019600e8-a309-7c00-877e-b94ada4eb22a/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8518/019600e8-a309-7c00-877e-b94ada4eb22a/)