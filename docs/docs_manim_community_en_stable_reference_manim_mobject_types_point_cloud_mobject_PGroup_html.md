ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PGroup.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PGroup.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# PGroup [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PGroup.html\#pgroup "Link to this heading")

Qualified name: `manim.mobject.types.point\_cloud\_mobject.PGroup`

_class_ PGroup( _\*pmobs_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html#PGroup) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PGroup.html#manim.mobject.types.point_cloud_mobject.PGroup "Link to this definition")

Bases: [`PMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject "manim.mobject.types.point_cloud_mobject.PMobject")

A group for several point mobjects.

Examples

Example: PgroupExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PGroup.html#pgroupexample)

![../_images/PgroupExample-1.png](https://docs.manim.community/en/stable/_images/PgroupExample-1.png)

```
from manim import *

class PgroupExample(Scene):
    def construct(self):

        p1 = PointCloudDot(radius=1, density=20, color=BLUE)
        p1.move_to(4.5 * LEFT)
        p2 = PointCloudDot()
        p3 = PointCloudDot(radius=1.5, stroke_width=2.5, color=PINK)
        p3.move_to(4.5 * RIGHT)
        pList = PGroup(p1, p2, p3)

        self.add(pList)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `fade_to` |  |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `depth` | The depth of the mobject. |
| `height` | The height of the mobject. |
| `width` | The width of the mobject. |

Parameters:

- **pmobs** ( _Any_)

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _\*pmobs_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PGroup.html#manim.mobject.types.point_cloud_mobject.PGroup._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **pmobs** ( _Any_)

- **kwargs** ( _Any_)


Return type:

None

[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/8271/019600e8-279d-7533-a0c1-65368b6ca97f/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8271/019600e8-279d-7533-a0c1-65368b6ca97f/)