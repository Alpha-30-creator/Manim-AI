ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Elbow.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Elbow.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Elbow [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Elbow.html\#elbow "Link to this heading")

Qualified name: `manim.mobject.geometry.line.Elbow`

_class_ Elbow( _width=0.2_, _angle=0_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#Elbow) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Elbow.html#manim.mobject.geometry.line.Elbow "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

Two lines that create a right angle about each other: L-shape.

Parameters:

- **width** ( _float_) – The length of the elbow’s sides.

- **angle** ( _float_) – The rotation of the elbow.

- **kwargs** ( _Any_) – Additional arguments to be passed to [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

- **seealso::** ( _.._) – [`RightAngle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.RightAngle.html#manim.mobject.geometry.line.RightAngle "manim.mobject.geometry.line.RightAngle")


Examples

Example: ElbowExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Elbow.html#elbowexample)

![../_images/ElbowExample-1.png](https://docs.manim.community/en/stable/_images/ElbowExample-1.png)

```
from manim import *

class ElbowExample(Scene):
    def construct(self):
        elbow_1 = Elbow()
        elbow_2 = Elbow(width=2.0)
        elbow_3 = Elbow(width=2.0, angle=5*PI/4)

        elbow_group = Group(elbow_1, elbow_2, elbow_3).arrange(buff=1)
        self.add(elbow_group)

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

\_original\_\_init\_\_( _width=0.2_, _angle=0_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Elbow.html#manim.mobject.geometry.line.Elbow._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **width** ( _float_)

- **angle** ( _float_)

- **kwargs** ( _Any_)


Return type:

None

[**The AI Agent that gets your codebase** Copilot & Cursor letting you down? Try Augment. **Install Now**](https://server.ethicalads.io/proxy/click/8458/019600e2-7455-7480-8f50-50ce17ea22a3/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8458/019600e2-7455-7480-8f50-50ce17ea22a3/)