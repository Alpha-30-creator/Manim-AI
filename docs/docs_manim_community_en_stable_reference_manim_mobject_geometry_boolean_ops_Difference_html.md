ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Difference [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html\#difference "Link to this heading")

Qualified name: `manim.mobject.geometry.boolean\_ops.Difference`

_class_ Difference( _subject_, _clip_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/boolean_ops.html#Difference) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html#manim.mobject.geometry.boolean_ops.Difference "Link to this definition")

Bases: `_BooleanOps`

Subtracts one [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") from another one.

Parameters:

- **subject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The 1st [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").

- **clip** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The 2nd [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

- **kwargs** ( _Any_)


Example

Example: DifferenceExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html#differenceexample)

![../_images/DifferenceExample-1.png](https://docs.manim.community/en/stable/_images/DifferenceExample-1.png)

```
from manim import *

class DifferenceExample(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=1)
        sq.move_to([-2, 0, 0])
        cr = Circle(color=BLUE, fill_opacity=1)
        cr.move_to([-1.3, 0.7, 0])
        un = Difference(sq, cr, color=GREEN, fill_opacity=1)
        un.move_to([1.5, 0, 0])
        self.add(sq, cr, un)

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

\_original\_\_init\_\_( _subject_, _clip_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Difference.html#manim.mobject.geometry.boolean_ops.Difference._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **subject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

- **clip** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

- **kwargs** ( _Any_)


Return type:

None