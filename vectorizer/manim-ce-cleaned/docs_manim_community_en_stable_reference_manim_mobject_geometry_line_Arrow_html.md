# Arrow [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html\#arrow "Link to this heading")

Qualified name: `manim.mobject.geometry.line.Arrow`

_class_ Arrow( _\*args_, _stroke\_width=6_, _buff=0.25_, _max\_tip\_length\_to\_length\_ratio=0.25_, _max\_stroke\_width\_to\_length\_ratio=5_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#Arrow) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "Link to this definition")

Bases: [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")

An arrow.

Parameters:

- **args** ( _Any_) – Arguments to be passed to [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line").

- **stroke\_width** ( _float_) – The thickness of the arrow. Influenced by `max_stroke_width_to_length_ratio`.

- **buff** ( _float_) – The distance of the arrow from its start and end points.

- **max\_tip\_length\_to\_length\_ratio** ( _float_) – `tip_length` scales with the length of the arrow. Increasing this ratio raises the max value of `tip_length`.

- **max\_stroke\_width\_to\_length\_ratio** ( _float_) – `stroke_width` scales with the length of the arrow. Increasing this ratio ratios the max value of `stroke_width`.

- **kwargs** ( _Any_) – Additional arguments to be passed to [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line").


See also

`ArrowTip` `CurvedArrow`

Examples

Example: ArrowExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#arrowexample)

![../_images/ArrowExample-1.png](https://docs.manim.community/en/stable/_images/ArrowExample-1.png)

```
from manim import *

from manim.mobject.geometry.tips import ArrowSquareTip
class ArrowExample(Scene):
    def construct(self):
        arrow_1 = Arrow(start=RIGHT, end=LEFT, color=GOLD)
        arrow_2 = Arrow(start=RIGHT, end=LEFT, color=GOLD, tip_shape=ArrowSquareTip).shift(DOWN)
        g1 = Group(arrow_1, arrow_2)

        # the effect of buff
        square = Square(color=MAROON_A)
        arrow_3 = Arrow(start=LEFT, end=RIGHT)
        arrow_4 = Arrow(start=LEFT, end=RIGHT, buff=0).next_to(arrow_1, UP)
        g2 = Group(arrow_3, arrow_4, square)

        # a shorter arrow has a shorter tip and smaller stroke width
        arrow_5 = Arrow(start=ORIGIN, end=config.top).shift(LEFT * 4)
        arrow_6 = Arrow(start=config.top + DOWN, end=config.top).shift(LEFT * 3)
        g3 = Group(arrow_5, arrow_6)

        self.add(Group(g1, g2, g3).arrange(buff=2))

```

Copy to clipboard

Make interactive

Example: ArrowExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#arrowexample)

![../_images/ArrowExample-2.png](https://docs.manim.community/en/stable/_images/ArrowExample-2.png)

```
from manim import *

class ArrowExample(Scene):
    def construct(self):
        left_group = VGroup()
        # As buff increases, the size of the arrow decreases.
        for buff in np.arange(0, 2.2, 0.45):
            left_group += Arrow(buff=buff, start=2 * LEFT, end=2 * RIGHT)
        # Required to arrange arrows.
        left_group.arrange(DOWN)
        left_group.move_to(4 * LEFT)

        middle_group = VGroup()
        # As max_stroke_width_to_length_ratio gets bigger,
        # the width of stroke increases.
        for i in np.arange(0, 5, 0.5):
            middle_group += Arrow(max_stroke_width_to_length_ratio=i)
        middle_group.arrange(DOWN)

        UR_group = VGroup()
        # As max_tip_length_to_length_ratio increases,
        # the length of the tip increases.
        for i in np.arange(0, 0.3, 0.1):
            UR_group += Arrow(max_tip_length_to_length_ratio=i)
        UR_group.arrange(DOWN)
        UR_group.move_to(4 * RIGHT + 2 * UP)

        DR_group = VGroup()
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareFilledTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleFilledTip)
        DR_group.arrange(DOWN)
        DR_group.move_to(4 * RIGHT + 2 * DOWN)

        self.add(left_group, middle_group, UR_group, DR_group)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`get_default_tip_length`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow.get_default_tip_length "manim.mobject.geometry.line.Arrow.get_default_tip_length") | Returns the default tip\_length of the arrow. |
| [`get_normal_vector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow.get_normal_vector "manim.mobject.geometry.line.Arrow.get_normal_vector") | Returns the normal of a vector. |
| [`reset_normal_vector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow.reset_normal_vector "manim.mobject.geometry.line.Arrow.reset_normal_vector") | Resets the normal of a vector |
| [`scale`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow.scale "manim.mobject.geometry.line.Arrow.scale") | Scale an arrow, but keep stroke width and arrow tip size fixed. |

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

\_original\_\_init\_\_( _\*args_, _stroke\_width=6_, _buff=0.25_, _max\_tip\_length\_to\_length\_ratio=0.25_, _max\_stroke\_width\_to\_length\_ratio=5_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **args** ( _Any_)

- **stroke\_width** ( _float_)

- **buff** ( _float_)

- **max\_tip\_length\_to\_length\_ratio** ( _float_)

- **max\_stroke\_width\_to\_length\_ratio** ( _float_)

- **kwargs** ( _Any_)


Return type:

None

\_set\_stroke\_width\_from\_length() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#Arrow._set_stroke_width_from_length) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow._set_stroke_width_from_length "Link to this definition")

Sets stroke width based on length.

Return type:

Self

get\_default\_tip\_length() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#Arrow.get_default_tip_length) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow.get_default_tip_length "Link to this definition")

Returns the default tip\_length of the arrow.

Examples

```
>>> Arrow().get_default_tip_length()
0.35

```

Copy to clipboard

Return type:

float

get\_normal\_vector() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#Arrow.get_normal_vector) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow.get_normal_vector "Link to this definition")

Returns the normal of a vector.

Examples

```
>>> np.round(Arrow().get_normal_vector()) + 0. # add 0. to avoid negative 0 in output
array([ 0.,  0., -1.])

```

Copy to clipboard

Return type:

[_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")

reset\_normal\_vector() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#Arrow.reset_normal_vector) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow.reset_normal_vector "Link to this definition")

Resets the normal of a vector

Return type:

Self

scale( _factor_, _scale\_tips=False_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#Arrow.scale) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow.scale "Link to this definition")

Scale an arrow, but keep stroke width and arrow tip size fixed.

See also

[`scale()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale "manim.mobject.mobject.Mobject.scale")

Examples

```
>>> arrow = Arrow(np.array([-1, -1, 0]), np.array([1, 1, 0]), buff=0)
>>> scaled_arrow = arrow.scale(2)
>>> np.round(scaled_arrow.get_start_and_end(), 8) + 0
array([[-2., -2.,  0.],\
       [ 2.,  2.,  0.]])
>>> arrow.tip.length == scaled_arrow.tip.length
True

```

Copy to clipboard

Manually scaling the object using the default method
[`scale()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale "manim.mobject.mobject.Mobject.scale") does not have the same properties:

```
>>> new_arrow = Arrow(np.array([-1, -1, 0]), np.array([1, 1, 0]), buff=0)
>>> another_scaled_arrow = VMobject.scale(new_arrow, 2)
>>> another_scaled_arrow.tip.length == arrow.tip.length
False

```

Copy to clipboard

Parameters:

- **factor** ( _float_)

- **scale\_tips** ( _bool_)

- **kwargs** ( _Any_)


Return type:

Self