# ComplexPlane [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html\#complexplane "Link to this heading")

Qualified name: `manim.mobject.graphing.coordinate\_systems.ComplexPlane`

_class_ ComplexPlane( _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane "Link to this definition")

Bases: [`NumberPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane")

A [`NumberPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "manim.mobject.graphing.coordinate_systems.NumberPlane") specialized for use with complex numbers.

Examples

Example: ComplexPlaneExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#complexplaneexample)

![../_images/ComplexPlaneExample-1.png](https://docs.manim.community/en/stable/_images/ComplexPlaneExample-1.png)

```
from manim import *

class ComplexPlaneExample(Scene):
    def construct(self):
        plane = ComplexPlane().add_coordinates()
        self.add(plane)
        d1 = Dot(plane.n2p(2 + 1j), color=YELLOW)
        d2 = Dot(plane.n2p(-3 - 2j), color=YELLOW)
        label1 = MathTex("2+i").next_to(d1, UR, 0.1)
        label2 = MathTex("-3-2i").next_to(d2, UR, 0.1)
        self.add(
            d1,
            label1,
            d2,
            label2,
        )

```

Copy to clipboard

Make interactive

References: [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot "manim.mobject.geometry.arc.Dot") [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")

Methods

|     |     |
| --- | --- |
| [`add_coordinates`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.add_coordinates "manim.mobject.graphing.coordinate_systems.ComplexPlane.add_coordinates") | Adds the labels produced from `get_coordinate_labels()` to the plane. |
| [`get_coordinate_labels`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.get_coordinate_labels "manim.mobject.graphing.coordinate_systems.ComplexPlane.get_coordinate_labels") | Generates the [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") mobjects for the coordinates of the plane. |
| [`n2p`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.n2p "manim.mobject.graphing.coordinate_systems.ComplexPlane.n2p") | Abbreviation for [`number_to_point()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point "manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point"). |
| [`number_to_point`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point "manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point") | Accepts a float/complex number and returns the equivalent point on the plane. |
| [`p2n`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.p2n "manim.mobject.graphing.coordinate_systems.ComplexPlane.p2n") | Abbreviation for [`point_to_number()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number "manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number"). |
| [`point_to_number`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number "manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number") | Accepts a point and returns a complex number equivalent to that point on the plane. |

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

**kwargs** ( _Any_)

\_get\_default\_coordinate\_values() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane._get_default_coordinate_values) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane._get_default_coordinate_values "Link to this definition")

Generate a list containing the numerical values of the plane’s labels.

Returns:

A list of floats representing the x-axis and complex numbers representing the y-axis.

Return type:

List\[float \| complex\]

\_original\_\_init\_\_( _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**kwargs** ( _Any_)

Return type:

None

add\_coordinates( _\*numbers_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane.add_coordinates) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.add_coordinates "Link to this definition")

Adds the labels produced from `get_coordinate_labels()` to the plane.

Parameters:

- **numbers** ( _Iterable_ _\[_ _float_ _\|_ _complex_ _\]_) – An iterable of floats/complex numbers. Floats are positioned along the x-axis, complex numbers along the y-axis.

- **kwargs** ( _Any_) – Additional arguments to be passed to [`get_number_mobject()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine.get_number_mobject "manim.mobject.graphing.number_line.NumberLine.get_number_mobject"), i.e. [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber").


Return type:

_Self_

get\_coordinate\_labels( _\*numbers_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane.get_coordinate_labels) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.get_coordinate_labels "Link to this definition")

Generates the [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") mobjects for the coordinates of the plane.

Parameters:

- **numbers** ( _Iterable_ _\[_ _float_ _\|_ _complex_ _\]_) – An iterable of floats/complex numbers. Floats are positioned along the x-axis, complex numbers along the y-axis.

- **kwargs** ( _Any_) – Additional arguments to be passed to [`get_number_mobject()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine.get_number_mobject "manim.mobject.graphing.number_line.NumberLine.get_number_mobject"), i.e. [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber").


Returns:

A [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") containing the positioned label mobjects.

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

n2p( _number_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane.n2p) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.n2p "Link to this definition")

Abbreviation for [`number_to_point()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point "manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point").

Parameters:

**number** ( _float_ _\|_ _complex_)

Return type:

_ndarray_

number\_to\_point( _number_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane.number_to_point) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.number_to_point "Link to this definition")

Accepts a float/complex number and returns the equivalent point on the plane.

Parameters:

**number** ( _float_ _\|_ _complex_) – The number. Can be a float or a complex number.

Returns:

The point on the plane.

Return type:

np.ndarray

p2n( _point_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane.p2n) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.p2n "Link to this definition")

Abbreviation for [`point_to_number()`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number "manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number").

Parameters:

**point** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

Return type:

complex

point\_to\_number( _point_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#ComplexPlane.point_to_number) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.ComplexPlane.html#manim.mobject.graphing.coordinate_systems.ComplexPlane.point_to_number "Link to this definition")

Accepts a point and returns a complex number equivalent to that point on the plane.

Parameters:

**point** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The point in manim’s coordinate-system

Returns:

A complex number consisting of real and imaginary components.

Return type:

complex

[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/8271/019600f0-adc7-7480-a364-f220a4fe0770/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8271/019600f0-adc7-7480-a364-f220a4fe0770/)