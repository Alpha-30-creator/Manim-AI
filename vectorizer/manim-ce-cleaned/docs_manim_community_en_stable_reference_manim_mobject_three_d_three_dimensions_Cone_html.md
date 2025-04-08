# Cone [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html\#cone "Link to this heading")

Qualified name: `manim.mobject.three\_d.three\_dimensions.Cone`

_class_ Cone( _base\_radius=1_, _height=1_, _direction=array(\[0.,0.,1.\])_, _show\_base=False_, _v\_range=\[0,6.283185307179586\]_, _u\_min=0_, _checkerboard\_colors=False_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Cone) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone "Link to this definition")

Bases: [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface")

A circular cone.
Can be defined using 2 parameters: its height, and its base radius.
The polar angle, theta, can be calculated using arctan(base\_radius /
height) The spherical radius, r, is calculated using the pythagorean
theorem.

Parameters:

- **base\_radius** ( _float_) – The base radius from which the cone tapers.

- **height** ( _float_) – The height measured from the plane formed by the base\_radius to
the apex of the cone.

- **direction** ( _np.ndarray_) – The direction of the apex.

- **show\_base** ( _bool_) – Whether to show the base plane or not.

- **v\_range** ( _Sequence_ _\[_ _float_ _\]_) – The azimuthal angle to start and end at.

- **u\_min** ( _float_) – The radius at the apex.

- **checkerboard\_colors** ( _bool_) – Show checkerboard grid texture on the cone.

- **kwargs** ( _Any_)


Examples

Example: ExampleCone [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#examplecone)

![../_images/ExampleCone-1.png](https://docs.manim.community/en/stable/_images/ExampleCone-1.png)

```
from manim import *

class ExampleCone(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cone = Cone(direction=X_AXIS+Y_AXIS+2*Z_AXIS, resolution=8)
        self.set_camera_orientation(phi=5*PI/11, theta=PI/9)
        self.add(axes, cone)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`func`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone.func "manim.mobject.three_d.three_dimensions.Cone.func") | Converts from spherical coordinates to cartesian. |
| [`get_direction`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone.get_direction "manim.mobject.three_d.three_dimensions.Cone.get_direction") | Returns the current direction of the apex of the [`Cone`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone "manim.mobject.three_d.three_dimensions.Cone"). |
| [`get_end`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone.get_end "manim.mobject.three_d.three_dimensions.Cone.get_end") | Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ends. |
| [`get_start`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone.get_start "manim.mobject.three_d.three_dimensions.Cone.get_start") | Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") starts. |
| [`set_direction`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone.set_direction "manim.mobject.three_d.three_dimensions.Cone.set_direction") | Changes the direction of the apex of the [`Cone`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone "manim.mobject.three_d.three_dimensions.Cone"). |

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

\_original\_\_init\_\_( _base\_radius=1_, _height=1_, _direction=array(\[0.,0.,1.\])_, _show\_base=False_, _v\_range=\[0,6.283185307179586\]_, _u\_min=0_, _checkerboard\_colors=False_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **base\_radius** ( _float_)

- **height** ( _float_)

- **direction** ( _ndarray_)

- **show\_base** ( _bool_)

- **v\_range** ( _Sequence_ _\[_ _float_ _\]_)

- **u\_min** ( _float_)

- **checkerboard\_colors** ( _bool_)

- **kwargs** ( _Any_)


Return type:

None

func( _u_, _v_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Cone.func) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone.func "Link to this definition")

Converts from spherical coordinates to cartesian.

Parameters:

- **u** ( _float_) – The radius.

- **v** ( _float_) – The azimuthal angle.


Returns:

Points defining the [`Cone`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone "manim.mobject.three_d.three_dimensions.Cone").

Return type:

`numpy.array`

get\_direction() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Cone.get_direction) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone.get_direction "Link to this definition")

Returns the current direction of the apex of the [`Cone`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone "manim.mobject.three_d.three_dimensions.Cone").

Returns:

**direction** – The direction of the apex.

Return type:

`numpy.array`

get\_end() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Cone.get_end) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone.get_end "Link to this definition")

Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ends.

Return type:

_ndarray_

get\_start() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Cone.get_start) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone.get_start "Link to this definition")

Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") starts.

Return type:

_ndarray_

set\_direction( _direction_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Cone.set_direction) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone.set_direction "Link to this definition")

Changes the direction of the apex of the [`Cone`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html#manim.mobject.three_d.three_dimensions.Cone "manim.mobject.three_d.three_dimensions.Cone").

Parameters:

**direction** ( _ndarray_) – The direction of the apex.

Return type:

None

[**The AI Agent that gets your codebase** Copilot & Cursor letting you down? Try Augment. **Install Now**](https://server.ethicalads.io/proxy/click/8458/019600f7-692c-7e53-834b-630fa3061182/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8458/019600f7-692c-7e53-834b-630fa3061182/)