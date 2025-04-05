ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Angle [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html\#angle "Link to this heading")

Qualified name: `manim.mobject.geometry.line.Angle`

_class_ Angle( _line1_, _line2_, _radius=None_, _quadrant=(1,1)_, _other\_angle=False_, _dot=False_, _dot\_radius=None_, _dot\_distance=0.55_, _dot\_color=ManimColor('#FFFFFF')_, _elbow=False_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#Angle) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

A circular arc or elbow-type mobject representing an angle of two lines.

Parameters:

- **line1** ( [_Line_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")) – The first line.

- **line2** ( [_Line_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")) – The second line.

- **radius** ( _float_ _\|_ _None_) – The radius of the `Arc`.

- **quadrant** ( [_AngleQuadrant_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.html#manim.mobject.geometry.line.AngleQuadrant "manim.mobject.geometry.line.AngleQuadrant")) – A sequence of two `int` numbers determining which of the 4 quadrants should be used.
The first value indicates whether to anchor the arc on the first line closer to the end point (1)
or start point (-1), and the second value functions similarly for the
end (1) or start (-1) of the second line.
Possibilities: (1,1), (-1,1), (1,-1), (-1,-1).

- **other\_angle** ( _bool_) – Toggles between the two possible angles defined by two points and an arc center. If set to
False (default), the arc will always go counterclockwise from the point on line1 until
the point on line2 is reached. If set to True, the angle will go clockwise from line1 to line2.

- **dot** ( _bool_) – Allows for a `Dot` in the arc. Mainly used as an convention to indicate a right angle.
The dot can be customized in the next three parameters.

- **dot\_radius** ( _float_ _\|_ _None_) – The radius of the `Dot`. If not specified otherwise, this radius will be 1/10 of the arc radius.

- **dot\_distance** ( _float_) – Relative distance from the center to the arc: 0 puts the dot in the center and 1 on the arc itself.

- **dot\_color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the `Dot`.

- **elbow** ( _bool_) – Produces an elbow-type mobject indicating a right angle, see [`RightAngle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.RightAngle.html#manim.mobject.geometry.line.RightAngle "manim.mobject.geometry.line.RightAngle") for more information
and a shorthand.

- **\*\*kwargs** ( _Any_) – Further keyword arguments that are passed to the constructor of `Arc` or [`Elbow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Elbow.html#manim.mobject.geometry.line.Elbow "manim.mobject.geometry.line.Elbow").


Examples

The first example shows some right angles with a dot in the middle while the second example shows
all 8 possible angles defined by two lines.

Example: RightArcAngleExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#rightarcangleexample)

![../_images/RightArcAngleExample-1.png](https://docs.manim.community/en/stable/_images/RightArcAngleExample-1.png)

```
from manim import *

class RightArcAngleExample(Scene):
    def construct(self):
        line1 = Line( LEFT, RIGHT )
        line2 = Line( DOWN, UP )
        rightarcangles = [\
            Angle(line1, line2, dot=True),\
            Angle(line1, line2, radius=0.4, quadrant=(1,-1), dot=True, other_angle=True),\
            Angle(line1, line2, radius=0.5, quadrant=(-1,1), stroke_width=8, dot=True, dot_color=YELLOW, dot_radius=0.04, other_angle=True),\
            Angle(line1, line2, radius=0.7, quadrant=(-1,-1), color=RED, dot=True, dot_color=GREEN, dot_radius=0.08),\
        ]
        plots = VGroup()
        for angle in rightarcangles:
            plot=VGroup(line1.copy(),line2.copy(), angle)
            plots.add(plot)
        plots.arrange(buff=1.5)
        self.add(plots)

```

Copy to clipboard

Make interactive

Example: AngleExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#angleexample)

![../_images/AngleExample-1.png](https://docs.manim.community/en/stable/_images/AngleExample-1.png)

```
from manim import *

class AngleExample(Scene):
    def construct(self):
        line1 = Line( LEFT + (1/3) * UP, RIGHT + (1/3) * DOWN )
        line2 = Line( DOWN + (1/3) * RIGHT, UP + (1/3) * LEFT )
        angles = [\
            Angle(line1, line2),\
            Angle(line1, line2, radius=0.4, quadrant=(1,-1), other_angle=True),\
            Angle(line1, line2, radius=0.5, quadrant=(-1,1), stroke_width=8, other_angle=True),\
            Angle(line1, line2, radius=0.7, quadrant=(-1,-1), color=RED),\
            Angle(line1, line2, other_angle=True),\
            Angle(line1, line2, radius=0.4, quadrant=(1,-1)),\
            Angle(line1, line2, radius=0.5, quadrant=(-1,1), stroke_width=8),\
            Angle(line1, line2, radius=0.7, quadrant=(-1,-1), color=RED, other_angle=True),\
        ]
        plots = VGroup()
        for angle in angles:
            plot=VGroup(line1.copy(),line2.copy(), angle)
            plots.add(VGroup(plot,SurroundingRectangle(plot, buff=0.3)))
        plots.arrange_in_grid(rows=2,buff=1)
        self.add(plots)

```

Copy to clipboard

Make interactive

Example: FilledAngle [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#filledangle)

![../_images/FilledAngle-1.png](https://docs.manim.community/en/stable/_images/FilledAngle-1.png)

```
from manim import *

class FilledAngle(Scene):
    def construct(self):
        l1 = Line(ORIGIN, 2 * UP + RIGHT).set_color(GREEN)
        l2 = (
            Line(ORIGIN, 2 * UP + RIGHT)
            .set_color(GREEN)
            .rotate(-20 * DEGREES, about_point=ORIGIN)
        )
        norm = l1.get_length()
        a1 = Angle(l1, l2, other_angle=True, radius=norm - 0.5).set_color(GREEN)
        a2 = Angle(l1, l2, other_angle=True, radius=norm).set_color(GREEN)
        q1 = a1.points #  save all coordinates of points of angle a1
        q2 = a2.reverse_direction().points  #  save all coordinates of points of angle a1 (in reversed direction)
        pnts = np.concatenate([q1, q2, q1[0].reshape(1, 3)])  # adds points and ensures that path starts and ends at same point
        mfill = VMobject().set_color(ORANGE)
        mfill.set_points_as_corners(pnts).set_fill(GREEN, opacity=1)
        self.add(l1, l2)
        self.add(mfill)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`from_three_points`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle.from_three_points "manim.mobject.geometry.line.Angle.from_three_points") | The angle between the lines AB and BC. |
| [`get_lines`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle.get_lines "manim.mobject.geometry.line.Angle.get_lines") | Get the lines forming an angle of the [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle") class. |
| [`get_value`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle.get_value "manim.mobject.geometry.line.Angle.get_value") | Get the value of an angle of the [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle") class. |

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

\_original\_\_init\_\_( _line1_, _line2_, _radius=None_, _quadrant=(1,1)_, _other\_angle=False_, _dot=False_, _dot\_radius=None_, _dot\_distance=0.55_, _dot\_color=ManimColor('#FFFFFF')_, _elbow=False_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **line1** ( [_Line_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line"))

- **line2** ( [_Line_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line"))

- **radius** ( _float_ _\|_ _None_)

- **quadrant** ( [_AngleQuadrant_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.html#manim.mobject.geometry.line.AngleQuadrant "manim.mobject.geometry.line.AngleQuadrant"))

- **other\_angle** ( _bool_)

- **dot** ( _bool_)

- **dot\_radius** ( _float_ _\|_ _None_)

- **dot\_distance** ( _float_)

- **dot\_color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **elbow** ( _bool_)

- **kwargs** ( _Any_)


Return type:

None

_static_ from\_three\_points( _A_, _B_, _C_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#Angle.from_three_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle.from_three_points "Link to this definition")

The angle between the lines AB and BC.

This constructs the angle angleABC.

Parameters:

- **A** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The endpoint of the first angle leg

- **B** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The vertex of the angle

- **C** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The endpoint of the second angle leg

- **\*\*kwargs** ( _Any_) – Further keyword arguments are passed to [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle")


Returns:

Angle(line1, line2, radius=0.5, quadrant=(-1,1), stroke\_width=8),
Angle(line1, line2, radius=0.7, quadrant=(-1,-1), color=RED, other\_angle=True),

Return type:

The Angle calculated from the three points

Examples

Example: AngleFromThreePointsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#anglefromthreepointsexample)

![../_images/AngleFromThreePointsExample-1.png](https://docs.manim.community/en/stable/_images/AngleFromThreePointsExample-1.png)

```
from manim import *

class AngleFromThreePointsExample(Scene):
    def construct(self):
        sample_angle = Angle.from_three_points(UP, ORIGIN, LEFT)
        red_angle = Angle.from_three_points(LEFT + UP, ORIGIN, RIGHT, radius=.8, quadrant=(-1,-1), color=RED, stroke_width=8, other_angle=True)
        self.add(red_angle, sample_angle)

```

Copy to clipboard

Make interactive

get\_lines() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#Angle.get_lines) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle.get_lines "Link to this definition")

Get the lines forming an angle of the [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle") class.

Returns:

A [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") containing the lines that form the angle of the [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle") class.

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Examples

```
>>> line_1, line_2 = Line(ORIGIN, RIGHT), Line(ORIGIN, UR)
>>> angle = Angle(line_1, line_2)
>>> angle.get_lines()
VGroup(Line, Line)

```

Copy to clipboard

get\_value( _degrees=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#Angle.get_value) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle.get_value "Link to this definition")

Get the value of an angle of the [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle") class.

Parameters:

**degrees** ( _bool_) – A boolean to decide the unit (deg/rad) in which the value of the angle is returned.

Returns:

The value in degrees/radians of an angle of the [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle") class.

Return type:

`float`

Examples

Example: GetValueExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#getvalueexample)

![../_images/GetValueExample-1.png](https://docs.manim.community/en/stable/_images/GetValueExample-1.png)

```
from manim import *

class GetValueExample(Scene):
    def construct(self):
        line1 = Line(LEFT+(1/3)*UP, RIGHT+(1/3)*DOWN)
        line2 = Line(DOWN+(1/3)*RIGHT, UP+(1/3)*LEFT)

        angle = Angle(line1, line2, radius=0.4)

        value = DecimalNumber(angle.get_value(degrees=True), unit=r"^{\circ}")
        value.next_to(angle, UR)

        self.add(line1, line2, angle, value)

```

Copy to clipboard

Make interactive

[**Document Extraction for Developers** Transform docs into structured data with Sensible. **Try for free →**](https://server.ethicalads.io/proxy/click/8517/019600ef-0de2-7a63-8ca5-d6b3dedee3c7/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8517/019600ef-0de2-7a63-8ca5-d6b3dedee3c7/)