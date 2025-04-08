ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Line3D [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html\#line3d "Link to this heading")

Qualified name: `manim.mobject.three\_d.three\_dimensions.Line3D`

_class_ Line3D( _start=array(\[-1.,0.,0.\])_, _end=array(\[1.,0.,0.\])_, _thickness=0.02_, _color=None_, _resolution=24_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Line3D) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "Link to this definition")

Bases: [`Cylinder`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cylinder.html#manim.mobject.three_d.three_dimensions.Cylinder "manim.mobject.three_d.three_dimensions.Cylinder")

A cylindrical line, for use in ThreeDScene.

Parameters:

- **start** ( _np.ndarray_) – The start point of the line.

- **end** ( _np.ndarray_) – The end point of the line.

- **thickness** ( _float_) – The thickness of the line.

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_) – The color of the line.

- **resolution** ( _int_ _\|_ _Sequence_ _\[_ _int_ _\]_) – The resolution of the line.
By default this value is the number of points the line will sampled at.
If you want the line to also come out checkered, use a tuple.
For example, for a line made of 24 points with 4 checker points on each
cylinder, pass the tuple (4, 24).


Examples

Example: ExampleLine3D [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#exampleline3d)

![../_images/ExampleLine3D-1.png](https://docs.manim.community/en/stable/_images/ExampleLine3D-1.png)

```
from manim import *

class ExampleLine3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        line = Line3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 2]))
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, line)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`get_end`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.get_end "manim.mobject.three_d.three_dimensions.Line3D.get_end") | Returns the ending point of the [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D"). |
| [`get_start`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.get_start "manim.mobject.three_d.three_dimensions.Line3D.get_start") | Returns the starting point of the [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D"). |
| [`parallel_to`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.parallel_to "manim.mobject.three_d.three_dimensions.Line3D.parallel_to") | Returns a line parallel to another line going through a given point. |
| [`perpendicular_to`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.perpendicular_to "manim.mobject.three_d.three_dimensions.Line3D.perpendicular_to") | Returns a line perpendicular to another line going through a given point. |
| [`pointify`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.pointify "manim.mobject.three_d.three_dimensions.Line3D.pointify") | Gets a point representing the center of the [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`set_start_and_end_attrs`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.set_start_and_end_attrs "manim.mobject.three_d.three_dimensions.Line3D.set_start_and_end_attrs") | Sets the start and end points of the line. |

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

\_original\_\_init\_\_( _start=array(\[-1.,0.,0.\])_, _end=array(\[1.,0.,0.\])_, _thickness=0.02_, _color=None_, _resolution=24_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **start** ( _np.ndarray_)

- **end** ( _np.ndarray_)

- **thickness** ( _float_)

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_)

- **resolution** ( _int_ _\|_ _Sequence_ _\[_ _int_ _\]_)


get\_end() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Line3D.get_end) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.get_end "Link to this definition")

Returns the ending point of the [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D").

Returns:

**end** – Ending point of the [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D").

Return type:

`numpy.array`

get\_start() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Line3D.get_start) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.get_start "Link to this definition")

Returns the starting point of the [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D").

Returns:

**start** – Starting point of the [`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D").

Return type:

`numpy.array`

_classmethod_ parallel\_to( _line_, _point=array(\[0.,0.,0.\])_, _length=5_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Line3D.parallel_to) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.parallel_to "Link to this definition")

Returns a line parallel to another line going through
a given point.

Parameters:

- **line** ( [_Line3D_](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D")) – The line to be parallel to.

- **point** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The point to pass through.

- **length** ( _float_) – Length of the parallel line.

- **kwargs** – Additional parameters to be passed to the class.


Returns:

Line parallel to `line`.

Return type:

[`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D")

Examples

Example: ParallelLineExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#parallellineexample)

![../_images/ParallelLineExample-1.png](https://docs.manim.community/en/stable/_images/ParallelLineExample-1.png)

```
from manim import *

class ParallelLineExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(PI / 3, -PI / 4)
        ax = ThreeDAxes((-5, 5), (-5, 5), (-5, 5), 10, 10, 10)
        line1 = Line3D(RIGHT * 2, UP + OUT, color=RED)
        line2 = Line3D.parallel_to(line1, color=YELLOW)
        self.add(ax, line1, line2)

```

Copy to clipboard

Make interactive

_classmethod_ perpendicular\_to( _line_, _point=array(\[0.,0.,0.\])_, _length=5_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Line3D.perpendicular_to) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.perpendicular_to "Link to this definition")

Returns a line perpendicular to another line going through
a given point.

Parameters:

- **line** ( [_Line3D_](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D")) – The line to be perpendicular to.

- **point** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The point to pass through.

- **length** ( _float_) – Length of the perpendicular line.

- **kwargs** – Additional parameters to be passed to the class.


Returns:

Line perpendicular to `line`.

Return type:

[`Line3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D")

Examples

Example: PerpLineExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#perplineexample)

![../_images/PerpLineExample-1.png](https://docs.manim.community/en/stable/_images/PerpLineExample-1.png)

```
from manim import *

class PerpLineExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(PI / 3, -PI / 4)
        ax = ThreeDAxes((-5, 5), (-5, 5), (-5, 5), 10, 10, 10)
        line1 = Line3D(RIGHT * 2, UP + OUT, color=RED)
        line2 = Line3D.perpendicular_to(line1, color=BLUE)
        self.add(ax, line1, line2)

```

Copy to clipboard

Make interactive

pointify( _mob\_or\_point_, _direction=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Line3D.pointify) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.pointify "Link to this definition")

Gets a point representing the center of the [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Parameters:

- **mob\_or\_point** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\|_ [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") or point whose center should be returned.

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – If an edge of a [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") should be returned, the direction of the edge.


Returns:

Center of the [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") or point, or edge if direction is given.

Return type:

`numpy.array`

set\_start\_and\_end\_attrs( _start_, _end_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Line3D.set_start_and_end_attrs) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D.set_start_and_end_attrs "Link to this definition")

Sets the start and end points of the line.

If either `start` or `end` are [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"),
this gives their centers.

Parameters:

- **start** ( _ndarray_) – Starting point or `Mobject`.

- **end** ( _ndarray_) – Ending point or `Mobject`.


Return type:

None