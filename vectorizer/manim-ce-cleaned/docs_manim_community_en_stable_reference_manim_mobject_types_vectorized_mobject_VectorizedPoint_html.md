# VectorizedPoint [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VectorizedPoint.html\#vectorizedpoint "Link to this heading")

Qualified name: `manim.mobject.types.vectorized\_mobject.VectorizedPoint`

_class_ VectorizedPoint( _location=array(\[0.,0.,0.\])_, _color=ManimColor('#000000')_, _fill\_opacity=0_, _stroke\_width=0_, _artificial\_width=0.01_, _artificial\_height=0.01_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html#VectorizedPoint) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VectorizedPoint.html#manim.mobject.types.vectorized_mobject.VectorizedPoint "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

Methods

|     |     |
| --- | --- |
| `get_location` |  |
| `set_location` |  |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| [`height`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VectorizedPoint.html#manim.mobject.types.vectorized_mobject.VectorizedPoint.height "manim.mobject.types.vectorized_mobject.VectorizedPoint.height") | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| [`width`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VectorizedPoint.html#manim.mobject.types.vectorized_mobject.VectorizedPoint.width "manim.mobject.types.vectorized_mobject.VectorizedPoint.width") | The width of the mobject. |

Parameters:

- **location** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **color** ( [_ManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))

- **fill\_opacity** ( _float_)

- **stroke\_width** ( _float_)

- **artificial\_width** ( _float_)

- **artificial\_height** ( _float_)


\_original\_\_init\_\_( _location=array(\[0.,0.,0.\])_, _color=ManimColor('#000000')_, _fill\_opacity=0_, _stroke\_width=0_, _artificial\_width=0.01_, _artificial\_height=0.01_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VectorizedPoint.html#manim.mobject.types.vectorized_mobject.VectorizedPoint._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **location** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **color** ( [_ManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))

- **fill\_opacity** ( _float_)

- **stroke\_width** ( _float_)

- **artificial\_width** ( _float_)

- **artificial\_height** ( _float_)


Return type:

None

basecls [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VectorizedPoint.html#manim.mobject.types.vectorized_mobject.VectorizedPoint.basecls "Link to this definition")

alias of [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

_property_ height _:float_ [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VectorizedPoint.html#manim.mobject.types.vectorized_mobject.VectorizedPoint.height "Link to this definition")

The height of the mobject.

Return type:

`float`

Examples

Example: HeightExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VectorizedPoint.html#heightexample)

```
from manim import *

class HeightExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.height))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(height=5))
        self.wait()

```

Copy to clipboard

Make interactive

See also

`length_over_dim()`

_property_ width _:float_ [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VectorizedPoint.html#manim.mobject.types.vectorized_mobject.VectorizedPoint.width "Link to this definition")

The width of the mobject.

Return type:

`float`

Examples

Example: WidthExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VectorizedPoint.html#widthexample)

```
from manim import *

class WidthExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.width))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(width=7))
        self.wait()

```

Copy to clipboard

Make interactive

See also

`length_over_dim()`