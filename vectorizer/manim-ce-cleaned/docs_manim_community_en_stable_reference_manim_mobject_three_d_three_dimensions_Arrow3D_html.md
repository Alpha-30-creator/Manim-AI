# Arrow3D [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Arrow3D.html\#arrow3d "Link to this heading")

Qualified name: `manim.mobject.three\_d.three\_dimensions.Arrow3D`

_class_ Arrow3D( _start=array(\[-1.,0.,0.\])_, _end=array(\[1.,0.,0.\])_, _thickness=0.02_, _height=0.3_, _base\_radius=0.08_, _color=ManimColor('#FFFFFF')_, _resolution=24_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Arrow3D) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Arrow3D.html#manim.mobject.three_d.three_dimensions.Arrow3D "Link to this definition")

Bases: [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D")

An arrow made out of a cylindrical line and a conical tip.

Parameters:

- **start** ( _np.ndarray_) – The start position of the arrow.

- **end** ( _np.ndarray_) – The end position of the arrow.

- **thickness** ( _float_) – The thickness of the arrow.

- **height** ( _float_) – The height of the conical tip.

- **base\_radius** ( _float_) – The base radius of the conical tip.

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the arrow.

- **resolution** ( _int_ _\|_ _Sequence_ _\[_ _int_ _\]_) – The resolution of the arrow line.


Examples

Example: ExampleArrow3D [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Arrow3D.html#examplearrow3d)

![../_images/ExampleArrow3D-1.png](https://docs.manim.community/en/stable/_images/ExampleArrow3D-1.png)

```
from manim import *

class ExampleArrow3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        arrow = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, 2, 2]),
            resolution=8
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, arrow)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`get_end`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Arrow3D.html#manim.mobject.three_d.three_dimensions.Arrow3D.get_end "manim.mobject.three_d.three_dimensions.Arrow3D.get_end") | Returns the ending point of the [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D"). |

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

\_original\_\_init\_\_( _start=array(\[-1.,0.,0.\])_, _end=array(\[1.,0.,0.\])_, _thickness=0.02_, _height=0.3_, _base\_radius=0.08_, _color=ManimColor('#FFFFFF')_, _resolution=24_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Arrow3D.html#manim.mobject.three_d.three_dimensions.Arrow3D._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **start** ( _ndarray_)

- **end** ( _ndarray_)

- **thickness** ( _float_)

- **height** ( _float_)

- **base\_radius** ( _float_)

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **resolution** ( _int_ _\|_ _Sequence_ _\[_ _int_ _\]_)


Return type:

None

get\_end() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Arrow3D.get_end) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Arrow3D.html#manim.mobject.three_d.three_dimensions.Arrow3D.get_end "Link to this definition")

Returns the ending point of the [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D").

Returns:

**end** – Ending point of the [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D").

Return type:

`numpy.array`

[**Document Extraction for Developers** Transform docs into structured data with Sensible. **Try for free →**](https://server.ethicalads.io/proxy/click/8517/019600ef-0de2-7a63-8ca5-d6b3dedee3c7/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8517/019600ef-0de2-7a63-8ca5-d6b3dedee3c7/)