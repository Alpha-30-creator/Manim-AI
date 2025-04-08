# NumberPlane [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html\#numberplane "Link to this heading")

Qualified name: `manim.mobject.graphing.coordinate\_systems.NumberPlane`

_class_ NumberPlane( _x\_range=(-7.111111111111111,7.111111111111111,1)_, _y\_range=(-4.0,4.0,1)_, _x\_length=None_, _y\_length=None_, _background\_line\_style=None_, _faded\_line\_style=None_, _faded\_line\_ratio=1_, _make\_smooth\_after\_applying\_functions=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#NumberPlane) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane "Link to this definition")

Bases: [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes")

Creates a cartesian plane with background lines.

Parameters:

- **x\_range** ( _Sequence_ _\[_ _float_ _\]_ _\|_ _None_) – The `[x_min, x_max, x_step]` values of the plane in the horizontal direction.

- **y\_range** ( _Sequence_ _\[_ _float_ _\]_ _\|_ _None_) – The `[y_min, y_max, y_step]` values of the plane in the vertical direction.

- **x\_length** ( _float_ _\|_ _None_) – The width of the plane.

- **y\_length** ( _float_ _\|_ _None_) – The height of the plane.

- **background\_line\_style** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_) – Arguments that influence the construction of the background lines of the plane.

- **faded\_line\_style** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_) – Similar to `background_line_style`, affects the construction of the scene’s background lines.

- **faded\_line\_ratio** ( _int_) – Determines the number of boxes within the background lines: `2` = 4 boxes, `3` = 9 boxes.

- **make\_smooth\_after\_applying\_functions** ( _bool_) – Currently non-functional.

- **kwargs** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_) – Additional arguments to be passed to [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes").


Note

If `x_length` or `y_length` are not defined, they are automatically calculated such that
one unit on each axis is one Manim unit long.

Examples

Example: NumberPlaneExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#numberplaneexample)

![../_images/NumberPlaneExample-1.png](https://docs.manim.community/en/stable/_images/NumberPlaneExample-1.png)

```
from manim import *

class NumberPlaneExample(Scene):
    def construct(self):
        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )
        self.add(number_plane)

```

Copy to clipboard

Make interactive

Example: NumberPlaneScaled [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#numberplanescaled)

![../_images/NumberPlaneScaled-1.png](https://docs.manim.community/en/stable/_images/NumberPlaneScaled-1.png)

```
from manim import *

class NumberPlaneScaled(Scene):
    def construct(self):
        number_plane = NumberPlane(
            x_range=(-4, 11, 1),
            y_range=(-3, 3, 1),
            x_length=5,
            y_length=2,
        ).move_to(LEFT*3)

        number_plane_scaled_y = NumberPlane(
            x_range=(-4, 11, 1),
            x_length=5,
            y_length=4,
        ).move_to(RIGHT*3)

        self.add(number_plane)
        self.add(number_plane_scaled_y)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `get_vector` |  |
| `prepare_for_nonlinear_transform` |  |

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

\_get\_lines() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#NumberPlane._get_lines) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane._get_lines "Link to this definition")Generate all the lines, faded and not faded.

Two sets of lines are generated: one parallel to the X-axis, and parallel to the Y-axis.

Returns:

The first (i.e the non faded lines) and second (i.e the faded lines) sets of lines, respectively.

Return type:

Tuple\[ [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup"), [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")\]

\_get\_lines\_parallel\_to\_axis( _axis\_parallel\_to_, _axis\_perpendicular\_to_, _freq_, _ratio\_faded\_lines_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#NumberPlane._get_lines_parallel_to_axis) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane._get_lines_parallel_to_axis "Link to this definition")

Generate a set of lines parallel to an axis.

Parameters:

- **axis\_parallel\_to** ( [_NumberLine_](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")) – The axis with which the lines will be parallel.

- **axis\_perpendicular\_to** ( [_NumberLine_](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")) – The axis with which the lines will be perpendicular.

- **ratio\_faded\_lines** ( _int_) – The ratio between the space between faded lines and the space between non-faded lines.

- **freq** ( _float_) – Frequency of non-faded lines (number of non-faded lines per graph unit).


Returns:

The first (i.e the non-faded lines parallel to axis\_parallel\_to) and second

(i.e the faded lines parallel to axis\_parallel\_to) sets of lines, respectively.

Return type:

Tuple\[ [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup"), [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")\]

\_init\_background\_lines() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#NumberPlane._init_background_lines) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane._init_background_lines "Link to this definition")

Will init all the lines of NumberPlanes (faded or not)

Return type:

None

\_original\_\_init\_\_( _x\_range=(-7.111111111111111,7.111111111111111,1)_, _y\_range=(-4.0,4.0,1)_, _x\_length=None_, _y\_length=None_, _background\_line\_style=None_, _faded\_line\_style=None_, _faded\_line\_ratio=1_, _make\_smooth\_after\_applying\_functions=True_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html#manim.mobject.graphing.coordinate_systems.NumberPlane._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **x\_range** ( _Sequence_ _\[_ _float_ _\]_ _\|_ _None_)

- **y\_range** ( _Sequence_ _\[_ _float_ _\]_ _\|_ _None_)

- **x\_length** ( _float_ _\|_ _None_)

- **y\_length** ( _float_ _\|_ _None_)

- **background\_line\_style** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **faded\_line\_style** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **faded\_line\_ratio** ( _int_)

- **make\_smooth\_after\_applying\_functions** ( _bool_)

- **kwargs** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_)