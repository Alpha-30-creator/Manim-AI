ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcBetweenPoints.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcBetweenPoints.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ArcBetweenPoints [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcBetweenPoints.html\#arcbetweenpoints "Link to this heading")

Qualified name: `manim.mobject.geometry.arc.ArcBetweenPoints`

_class_ ArcBetweenPoints( _start_, _end_, _angle=1.5707963267948966_, _radius=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#ArcBetweenPoints) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcBetweenPoints.html#manim.mobject.geometry.arc.ArcBetweenPoints "Link to this definition")

Bases: [`Arc`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc")

Inherits from Arc and additionally takes 2 points between which the arc is spanned.

Example

Example: ArcBetweenPointsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcBetweenPoints.html#arcbetweenpointsexample)

```
from manim import *

class ArcBetweenPointsExample(Scene):
    def construct(self):
        circle = Circle(radius=2, stroke_color=GREY)
        dot_1 = Dot(color=GREEN).move_to([2, 0, 0]).scale(0.5)
        dot_1_text = Tex("(2,0)").scale(0.5).next_to(dot_1, RIGHT).set_color(BLUE)
        dot_2 = Dot(color=GREEN).move_to([0, 2, 0]).scale(0.5)
        dot_2_text = Tex("(0,2)").scale(0.5).next_to(dot_2, UP).set_color(BLUE)
        arc= ArcBetweenPoints(start=2 * RIGHT, end=2 * UP, stroke_color=YELLOW)
        self.add(circle, dot_1, dot_2, dot_1_text, dot_2_text)
        self.play(Create(arc))

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

- **start** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **end** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **angle** ( _float_)

- **radius** ( _float_ _\|_ _None_)

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _start_, _end_, _angle=1.5707963267948966_, _radius=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcBetweenPoints.html#manim.mobject.geometry.arc.ArcBetweenPoints._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **start** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **end** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **angle** ( _float_)

- **radius** ( _float_ _\|_ _None_)

- **kwargs** ( _Any_)


Return type:

None

[**Watch Our Demo** video to see firsthand how to upgrade your site with end-to-end AI Search.](https://server.ethicalads.io/proxy/click/8294/019600e5-8564-71c0-b842-497db349b313/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/frontend-web/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8294/019600e5-8564-71c0-b842-497db349b313/)