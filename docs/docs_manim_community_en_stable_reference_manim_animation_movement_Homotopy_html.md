ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.movement.Homotopy.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.movement.Homotopy.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Homotopy [¶](https://docs.manim.community/en/stable/reference/manim.animation.movement.Homotopy.html\#homotopy "Link to this heading")

Qualified name: `manim.animation.movement.Homotopy`

_class_ Homotopy( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/movement.html#Homotopy) [¶](https://docs.manim.community/en/stable/reference/manim.animation.movement.Homotopy.html#manim.animation.movement.Homotopy "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

A Homotopy.

This is an animation transforming the points of a mobject according
to the specified transformation function. With the parameter t
moving from 0 to 1 throughout the animation and (x,y,z)
describing the coordinates of the point of a mobject,
the function passed to the `homotopy` keyword argument should
transform the tuple (x,y,z,t) to (x′,y′,z′),
the coordinates the original point is transformed to at time t.

Parameters:

- **homotopy** ( _Callable_ _\[_ _\[_ _float_ _,_ _float_ _,_ _float_ _,_ _float_ _\]_ _,_ _tuple_ _\[_ _float_ _,_ _float_ _,_ _float_ _\]_ _\]_) – A function mapping (x,y,z,t) to (x′,y′,z′).

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject transformed under the given homotopy.

- **run\_time** ( _float_) – The run time of the animation.

- **apply\_function\_kwargs** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_) – Keyword arguments propagated to `Mobject.apply_function()`.

- **kwargs** – Further keyword arguments passed to the parent class.


Examples

Example: HomotopyExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.movement.Homotopy.html#homotopyexample)

```
from manim import *

class HomotopyExample(Scene):
    def construct(self):
        square = Square()

        def homotopy(x, y, z, t):
            if t <= 0.25:
                progress = t / 0.25
                return (x, y + progress * 0.2 * np.sin(x), z)
            else:
                wave_progress = (t - 0.25) / 0.75
                return (x, y + 0.2 * np.sin(x + 10 * wave_progress), z)

        self.play(Homotopy(homotopy, square, rate_func= linear, run_time=2))

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `function_at_time_t` |  |
| `interpolate_submobject` |  |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _homotopy_, _mobject_, _run\_time=3_, _apply\_function\_kwargs=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.movement.Homotopy.html#manim.animation.movement.Homotopy._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **homotopy** ( _Callable_ _\[_ _\[_ _float_ _,_ _float_ _,_ _float_ _,_ _float_ _\]_ _,_ _tuple_ _\[_ _float_ _,_ _float_ _,_ _float_ _\]_ _\]_)

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **run\_time** ( _float_)

- **apply\_function\_kwargs** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)


Return type:

None