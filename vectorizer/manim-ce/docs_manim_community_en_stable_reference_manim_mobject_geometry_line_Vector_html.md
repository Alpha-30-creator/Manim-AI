ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Vector [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html\#vector "Link to this heading")

Qualified name: `manim.mobject.geometry.line.Vector`

_class_ Vector( _direction=array(\[1.,0.,0.\])_, _buff=0_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#Vector) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "Link to this definition")

Bases: [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")

A vector specialized for use in graphs.

Caution

Do not confuse with the [`Vector2D`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector2D "manim.typing.Vector2D"),
[`Vector3D`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D") or [`VectorND`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.VectorND "manim.typing.VectorND") type aliases,
which are not Mobjects!

Parameters:

- **direction** ( [_Point2DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point2DLike "manim.typing.Point2DLike") _\|_ [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The direction of the arrow.

- **buff** ( _float_) – The distance of the vector from its endpoints.

- **kwargs** ( _Any_) – Additional arguments to be passed to [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")


Examples

Example: VectorExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#vectorexample)

![../_images/VectorExample-1.png](https://docs.manim.community/en/stable/_images/VectorExample-1.png)

```
from manim import *

class VectorExample(Scene):
    def construct(self):
        plane = NumberPlane()
        vector_1 = Vector([1,2])
        vector_2 = Vector([-5,-2])
        self.add(plane, vector_1, vector_2)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`coordinate_label`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector.coordinate_label "manim.mobject.geometry.line.Vector.coordinate_label") | Creates a label based on the coordinates of the vector. |

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

\_original\_\_init\_\_( _direction=array(\[1.,0.,0.\])_, _buff=0_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **direction** ( [_Point2DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point2DLike "manim.typing.Point2DLike") _\|_ [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **buff** ( _float_)

- **kwargs** ( _Any_)


Return type:

None

coordinate\_label( _integer\_labels=True_, _n\_dim=2_, _color=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#Vector.coordinate_label) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector.coordinate_label "Link to this definition")

Creates a label based on the coordinates of the vector.

Parameters:

- **integer\_labels** ( _bool_) – Whether or not to round the coordinates to integers.

- **n\_dim** ( _int_) – The number of dimensions of the vector.

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_) – Sets the color of label, optional.

- **kwargs** ( _Any_) – Additional arguments to be passed to [`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix").


Returns:

The label.

Return type:

[`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

Examples

Example: VectorCoordinateLabel [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#vectorcoordinatelabel)

![../_images/VectorCoordinateLabel-1.png](https://docs.manim.community/en/stable/_images/VectorCoordinateLabel-1.png)

```
from manim import *

class VectorCoordinateLabel(Scene):
    def construct(self):
        plane = NumberPlane()

        vec_1 = Vector([1, 2])
        vec_2 = Vector([-3, -2])
        label_1 = vec_1.coordinate_label()
        label_2 = vec_2.coordinate_label(color=YELLOW)

        self.add(plane, vec_1, vec_2, label_1, label_2)

```

Copy to clipboard

Make interactive