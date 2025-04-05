ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Point.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Point.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Point [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Point.html\#point "Link to this heading")

Qualified name: `manim.mobject.types.point\_cloud\_mobject.Point`

_class_ Point( _location=array(\[0.,0.,0.\])_, _color=ManimColor('#000000')_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html#Point) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Point.html#manim.mobject.types.point_cloud_mobject.Point "Link to this definition")

Bases: [`PMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject "manim.mobject.types.point_cloud_mobject.PMobject")

A mobject representing a point.

Examples

Example: ExamplePoint [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Point.html#examplepoint)

![../_images/ExamplePoint-1.png](https://docs.manim.community/en/stable/_images/ExamplePoint-1.png)

```
from manim import *

class ExamplePoint(Scene):
    def construct(self):
        colorList = [RED, GREEN, BLUE, YELLOW]
        for i in range(200):
            point = Point(location=[0.63 * np.random.randint(-4, 4), 0.37 * np.random.randint(-4, 4), 0], color=np.random.choice(colorList))
            self.add(point)
        for i in range(200):
            point = Point(location=[0.37 * np.random.randint(-4, 4), 0.63 * np.random.randint(-4, 4), 0], color=np.random.choice(colorList))
            self.add(point)
        self.add(point)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`generate_points`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Point.html#manim.mobject.types.point_cloud_mobject.Point.generate_points "manim.mobject.types.point_cloud_mobject.Point.generate_points") | Initializes `points` and therefore the shape. |
| `init_points` |  |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `depth` | The depth of the mobject. |
| `height` | The height of the mobject. |
| `width` | The width of the mobject. |

Parameters:

- **location** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

- **color** ( [_ManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _location=array(\[0.,0.,0.\])_, _color=ManimColor('#000000')_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Point.html#manim.mobject.types.point_cloud_mobject.Point._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **location** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

- **color** ( [_ManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))

- **kwargs** ( _Any_)


Return type:

None

generate\_points() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html#Point.generate_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Point.html#manim.mobject.types.point_cloud_mobject.Point.generate_points "Link to this definition")

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

Return type:

None