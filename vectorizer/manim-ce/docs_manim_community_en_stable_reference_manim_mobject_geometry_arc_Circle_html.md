ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Circle [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html\#circle "Link to this heading")

Qualified name: `manim.mobject.geometry.arc.Circle`

_class_ Circle( _radius=None_, _color=ManimColor('#FC6255')_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#Circle) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "Link to this definition")

Bases: [`Arc`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc")

A circle.

Parameters:

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the shape.

- **kwargs** ( _Any_) – Additional arguments to be passed to [`Arc`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc")

- **radius** ( _float_ _\|_ _None_)


Examples

Example: CircleExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#circleexample)

![../_images/CircleExample-1.png](https://docs.manim.community/en/stable/_images/CircleExample-1.png)

```
from manim import *

class CircleExample(Scene):
    def construct(self):
        circle_1 = Circle(radius=1.0)
        circle_2 = Circle(radius=1.5, color=GREEN)
        circle_3 = Circle(radius=1.0, color=BLUE_B, fill_opacity=1)

        circle_group = Group(circle_1, circle_2, circle_3).arrange(buff=1)
        self.add(circle_group)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`from_three_points`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle.from_three_points "manim.mobject.geometry.arc.Circle.from_three_points") | Returns a circle passing through the specified three points. |
| [`point_at_angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle.point_at_angle "manim.mobject.geometry.arc.Circle.point_at_angle") | Returns the position of a point on the circle. |
| [`surround`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle.surround "manim.mobject.geometry.arc.Circle.surround") | Modifies a circle so that it surrounds a given mobject. |

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

\_original\_\_init\_\_( _radius=None_, _color=ManimColor('#FC6255')_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **radius** ( _float_ _\|_ _None_)

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **kwargs** ( _Any_)


Return type:

None

_static_ from\_three\_points( _p1_, _p2_, _p3_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#Circle.from_three_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle.from_three_points "Link to this definition")

Returns a circle passing through the specified
three points.

Example

Example: CircleFromPointsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#circlefrompointsexample)

![../_images/CircleFromPointsExample-1.png](https://docs.manim.community/en/stable/_images/CircleFromPointsExample-1.png)

```
from manim import *

class CircleFromPointsExample(Scene):
    def construct(self):
        circle = Circle.from_three_points(LEFT, LEFT + UP, UP * 2, color=RED)
        dots = VGroup(
            Dot(LEFT),
            Dot(LEFT + UP),
            Dot(UP * 2),
        )
        self.add(NumberPlane(), circle, dots)

```

Copy to clipboard

Make interactive

Parameters:

- **p1** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **p2** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **p3** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **kwargs** ( _Any_)


Return type:

[Circle](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle")

point\_at\_angle( _angle_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#Circle.point_at_angle) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle.point_at_angle "Link to this definition")

Returns the position of a point on the circle.

Parameters:

**angle** ( _float_) – The angle of the point along the circle in radians.

Returns:

The location of the point along the circle’s circumference.

Return type:

`numpy.ndarray`

Examples

Example: PointAtAngleExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#pointatangleexample)

![../_images/PointAtAngleExample-1.png](https://docs.manim.community/en/stable/_images/PointAtAngleExample-1.png)

```
from manim import *

class PointAtAngleExample(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        p1 = circle.point_at_angle(PI/2)
        p2 = circle.point_at_angle(270*DEGREES)

        s1 = Square(side_length=0.25).move_to(p1)
        s2 = Square(side_length=0.25).move_to(p2)
        self.add(circle, s1, s2)

```

Copy to clipboard

Make interactive

surround( _mobject_, _dim\_to\_match=0_, _stretch=False_, _buffer\_factor=1.2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#Circle.surround) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle.surround "Link to this definition")

Modifies a circle so that it surrounds a given mobject.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject that the circle will be surrounding.

- **dim\_to\_match** ( _int_)

- **buffer\_factor** ( _float_) – Scales the circle with respect to the mobject. A buffer\_factor < 1 makes the circle smaller than the mobject.

- **stretch** ( _bool_) – Stretches the circle to fit more tightly around the mobject. Note: Does not work with `Line`


Return type:

Self

Examples

Example: CircleSurround [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#circlesurround)

![../_images/CircleSurround-1.png](https://docs.manim.community/en/stable/_images/CircleSurround-1.png)

```
from manim import *

class CircleSurround(Scene):
    def construct(self):
        triangle1 = Triangle()
        circle1 = Circle().surround(triangle1)
        group1 = Group(triangle1,circle1) # treat the two mobjects as one

        line2 = Line()
        circle2 = Circle().surround(line2, buffer_factor=2.0)
        group2 = Group(line2,circle2)

        # buffer_factor < 1, so the circle is smaller than the square
        square3 = Square()
        circle3 = Circle().surround(square3, buffer_factor=0.5)
        group3 = Group(square3, circle3)

        group = Group(group1, group2, group3).arrange(buff=1)
        self.add(group)

```

Copy to clipboard

Make interactive