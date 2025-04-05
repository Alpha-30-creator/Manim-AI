ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# MobjectMatrix [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html\#mobjectmatrix "Link to this heading")

Qualified name: `manim.mobject.matrix.MobjectMatrix`

_class_ MobjectMatrix( _matrix_, _element\_to\_mobject=<functionMobjectMatrix.<lambda>>_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#MobjectMatrix) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html#manim.mobject.matrix.MobjectMatrix "Link to this definition")

Bases: [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

A mobject that displays a matrix of mobject entries on the screen.

Examples

Example: MobjectMatrixExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html#mobjectmatrixexample)

![../_images/MobjectMatrixExample-1.png](https://docs.manim.community/en/stable/_images/MobjectMatrixExample-1.png)

```
from manim import *

class MobjectMatrixExample(Scene):
    def construct(self):
        a = Circle().scale(0.3)
        b = Square().scale(0.3)
        c = MathTex("\\pi").scale(2)
        d = Star().scale(0.3)
        m0 = MobjectMatrix([[a, b], [c, d]])
        self.add(m0)

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

\_original\_\_init\_\_( _matrix_, _element\_to\_mobject=<functionMobjectMatrix.<lambda>>_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.MobjectMatrix.html#manim.mobject.matrix.MobjectMatrix._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.