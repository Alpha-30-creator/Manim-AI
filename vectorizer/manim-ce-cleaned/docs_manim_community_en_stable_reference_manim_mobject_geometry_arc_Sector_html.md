# Sector [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Sector.html\#sector "Link to this heading")

Qualified name: `manim.mobject.geometry.arc.Sector`

_class_ Sector( _radius=1_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#Sector) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Sector.html#manim.mobject.geometry.arc.Sector "Link to this definition")

Bases: [`AnnularSector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.AnnularSector.html#manim.mobject.geometry.arc.AnnularSector "manim.mobject.geometry.arc.AnnularSector")

A sector of a circle.

Examples

Example: ExampleSector [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Sector.html#examplesector)

![../_images/ExampleSector-1.png](https://docs.manim.community/en/stable/_images/ExampleSector-1.png)

```
from manim import *

class ExampleSector(Scene):
    def construct(self):
        sector = Sector(radius=2)
        sector2 = Sector(radius=2.5, angle=60*DEGREES).move_to([-3, 0, 0])
        sector.set_color(RED)
        sector2.set_color(PINK)
        self.add(sector, sector2)

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

- **radius** ( _float_)

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _radius=1_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Sector.html#manim.mobject.geometry.arc.Sector._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **radius** ( _float_)

- **kwargs** ( _Any_)


Return type:

None

[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/8270/019600e7-877e-7663-abcc-a0bd223f6333/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8270/019600e7-877e-7663-abcc-a0bd223f6333/)