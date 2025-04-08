# RightAngle [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.RightAngle.html\#rightangle "Link to this heading")

Qualified name: `manim.mobject.geometry.line.RightAngle`

_class_ RightAngle( _line1_, _line2_, _length=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/line.html#RightAngle) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.RightAngle.html#manim.mobject.geometry.line.RightAngle "Link to this definition")

Bases: [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle")

An elbow-type mobject representing a right angle between two lines.

Parameters:

- **line1** ( [_Line_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")) – The first line.

- **line2** ( [_Line_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")) – The second line.

- **length** ( _float_ _\|_ _None_) – The length of the arms.

- **\*\*kwargs** ( _Any_) – Further keyword arguments that are passed to the constructor of [`Angle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Angle.html#manim.mobject.geometry.line.Angle "manim.mobject.geometry.line.Angle").


Examples

Example: RightAngleExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.RightAngle.html#rightangleexample)

![../_images/RightAngleExample-1.png](https://docs.manim.community/en/stable/_images/RightAngleExample-1.png)

```
from manim import *

class RightAngleExample(Scene):
    def construct(self):
        line1 = Line( LEFT, RIGHT )
        line2 = Line( DOWN, UP )
        rightangles = [\
            RightAngle(line1, line2),\
            RightAngle(line1, line2, length=0.4, quadrant=(1,-1)),\
            RightAngle(line1, line2, length=0.5, quadrant=(-1,1), stroke_width=8),\
            RightAngle(line1, line2, length=0.7, quadrant=(-1,-1), color=RED),\
        ]
        plots = VGroup()
        for rightangle in rightangles:
            plot=VGroup(line1.copy(),line2.copy(), rightangle)
            plots.add(plot)
        plots.arrange(buff=1.5)
        self.add(plots)

```

Copy to clipboard

Make interactive

Methods

|
|

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

\_original\_\_init\_\_( _line1_, _line2_, _length=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.RightAngle.html#manim.mobject.geometry.line.RightAngle._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **line1** ( [_Line_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line"))

- **line2** ( [_Line_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line"))

- **length** ( _float_ _\|_ _None_)

- **kwargs** ( _Any_)


Return type:

None