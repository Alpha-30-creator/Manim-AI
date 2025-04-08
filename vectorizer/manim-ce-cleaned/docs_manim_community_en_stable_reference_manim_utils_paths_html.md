# paths [¶](https://docs.manim.community/en/stable/reference/manim.utils.paths.html\#module-manim.utils.paths "Link to this heading")

Functions determining transformation paths between sets of points.

Functions

clockwise\_path() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/paths.html#clockwise_path) [¶](https://docs.manim.community/en/stable/reference/manim.utils.paths.html#manim.utils.paths.clockwise_path "Link to this definition")

This function transforms each point by moving clockwise around a half circle.

Examples

Example: ClockwisePathExample [¶](https://docs.manim.community/en/stable/reference/manim.utils.paths.html#clockwisepathexample)

```
from manim import *

class ClockwisePathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[\
                Dot(LEFT + pos, color=color)\
                for pos, color in zip([UP, DOWN, LEFT], colors)\
            ]
        )

        finish_points = VGroup(
            *[\
                Dot(RIGHT + pos, color=color)\
                for pos, color in zip([ORIGIN, UP, DOWN], colors)\
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.clockwise_path(),
                run_time=2,
            )
        )
        self.wait()

```

Copy to clipboard

Make interactive

Return type:

[_PathFuncType_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PathFuncType "manim.typing.PathFuncType")

counterclockwise\_path() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/paths.html#counterclockwise_path) [¶](https://docs.manim.community/en/stable/reference/manim.utils.paths.html#manim.utils.paths.counterclockwise_path "Link to this definition")

This function transforms each point by moving counterclockwise around a half circle.

Examples

Example: CounterclockwisePathExample [¶](https://docs.manim.community/en/stable/reference/manim.utils.paths.html#counterclockwisepathexample)

```
from manim import *

class CounterclockwisePathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[\
                Dot(LEFT + pos, color=color)\
                for pos, color in zip([UP, DOWN, LEFT], colors)\
            ]
        )

        finish_points = VGroup(
            *[\
                Dot(RIGHT + pos, color=color)\
                for pos, color in zip([ORIGIN, UP, DOWN], colors)\
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.counterclockwise_path(),
                run_time=2,
            )
        )
        self.wait()

```

Copy to clipboard

Make interactive

Return type:

[_PathFuncType_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PathFuncType "manim.typing.PathFuncType")

path\_along\_arc( _arc\_angle_, _axis=array(\[0.,0.,1.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/paths.html#path_along_arc) [¶](https://docs.manim.community/en/stable/reference/manim.utils.paths.html#manim.utils.paths.path_along_arc "Link to this definition")

This function transforms each point by moving it along a circular arc.

Parameters:

- **arc\_angle** ( _float_) – The angle each point traverses around a circular arc.

- **axis** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The axis of rotation.


Return type:

[_PathFuncType_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PathFuncType "manim.typing.PathFuncType")

Examples

Example: PathAlongArcExample [¶](https://docs.manim.community/en/stable/reference/manim.utils.paths.html#pathalongarcexample)

```
from manim import *

class PathAlongArcExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[\
                Dot(LEFT + pos, color=color)\
                for pos, color in zip([UP, DOWN, LEFT], colors)\
            ]
        )

        finish_points = VGroup(
            *[\
                Dot(RIGHT + pos, color=color)\
                for pos, color in zip([ORIGIN, UP, DOWN], colors)\
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.path_along_arc(TAU * 2 / 3),
                run_time=3,
            )
        )
        self.wait()

```

Copy to clipboard

Make interactive

path\_along\_circles( _arc\_angle_, _circles\_centers_, _axis=array(\[0.,0.,1.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/paths.html#path_along_circles) [¶](https://docs.manim.community/en/stable/reference/manim.utils.paths.html#manim.utils.paths.path_along_circles "Link to this definition")

This function transforms each point by moving it roughly along a circle, each with its own specified center.

The path may be seen as each point smoothly changing its orbit from its starting position to its destination.

Parameters:

- **arc\_angle** ( _float_) – The angle each point traverses around the quasicircle.

- **circles\_centers** ( _ndarray_) – The centers of each point’s quasicircle to rotate around.

- **axis** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The axis of rotation.


Return type:

[_PathFuncType_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PathFuncType "manim.typing.PathFuncType")

Examples

Example: PathAlongCirclesExample [¶](https://docs.manim.community/en/stable/reference/manim.utils.paths.html#pathalongcirclesexample)

```
from manim import *

class PathAlongCirclesExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[\
                Dot(LEFT + pos, color=color)\
                for pos, color in zip([UP, DOWN, LEFT], colors)\
            ]
        )

        finish_points = VGroup(
            *[\
                Dot(RIGHT + pos, color=color)\
                for pos, color in zip([ORIGIN, UP, DOWN], colors)\
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        circle_center = Dot(3 * LEFT)
        self.add(circle_center)

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.path_along_circles(
                    2 * PI, circle_center.get_center()
                ),
                run_time=3,
            )
        )
        self.wait()

```

Copy to clipboard

Make interactive

spiral\_path( _angle_, _axis=array(\[0.,0.,1.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/paths.html#spiral_path) [¶](https://docs.manim.community/en/stable/reference/manim.utils.paths.html#manim.utils.paths.spiral_path "Link to this definition")

This function transforms each point by moving along a spiral to its destination.

Parameters:

- **angle** ( _float_) – The angle each point traverses around a spiral.

- **axis** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The axis of rotation.


Return type:

[_PathFuncType_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PathFuncType "manim.typing.PathFuncType")

Examples

Example: SpiralPathExample [¶](https://docs.manim.community/en/stable/reference/manim.utils.paths.html#spiralpathexample)

```
from manim import *

class SpiralPathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[\
                Dot(LEFT + pos, color=color)\
                for pos, color in zip([UP, DOWN, LEFT], colors)\
            ]
        )

        finish_points = VGroup(
            *[\
                Dot(RIGHT + pos, color=color)\
                for pos, color in zip([ORIGIN, UP, DOWN], colors)\
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.spiral_path(2 * TAU),
                run_time=5,
            )
        )
        self.wait()

```

Copy to clipboard

Make interactive

straight\_path() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/paths.html#straight_path) [¶](https://docs.manim.community/en/stable/reference/manim.utils.paths.html#manim.utils.paths.straight_path "Link to this definition")

Simplest path function. Each point in a set goes in a straight path toward its destination.

Examples

Example: StraightPathExample [¶](https://docs.manim.community/en/stable/reference/manim.utils.paths.html#straightpathexample)

```
from manim import *

class StraightPathExample(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE]

        starting_points = VGroup(
            *[\
                Dot(LEFT + pos, color=color)\
                for pos, color in zip([UP, DOWN, LEFT], colors)\
            ]
        )

        finish_points = VGroup(
            *[\
                Dot(RIGHT + pos, color=color)\
                for pos, color in zip([ORIGIN, UP, DOWN], colors)\
            ]
        )

        self.add(starting_points)
        self.add(finish_points)
        for dot in starting_points:
            self.add(TracedPath(dot.get_center, stroke_color=dot.get_color()))

        self.wait()
        self.play(
            Transform(
                starting_points,
                finish_points,
                path_func=utils.paths.straight_path(),
                run_time=2,
            )
        )
        self.wait()

```

Copy to clipboard

Make interactive

Return type:

[_PathFuncType_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PathFuncType "manim.typing.PathFuncType")