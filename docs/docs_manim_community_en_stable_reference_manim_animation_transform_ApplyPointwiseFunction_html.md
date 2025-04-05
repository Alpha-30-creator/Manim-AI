ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ApplyPointwiseFunction [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html\#applypointwisefunction "Link to this heading")

Qualified name: `manim.animation.transform.ApplyPointwiseFunction`

_class_ ApplyPointwiseFunction( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#ApplyPointwiseFunction) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction "Link to this definition")

Bases: [`ApplyMethod`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

Animation that applies a pointwise function to a mobject.

Examples

Example: WarpSquare [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#warpsquare)

```
from manim import *

class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(
            ApplyPointwiseFunction(
                lambda point: complex_to_R3(np.exp(R3_to_complex(point))), square
            )
        )
        self.wait()

```

Copy to clipboard

Make interactive

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

Parameters:

- **function** ( _types.MethodType_)

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **run\_time** ( _float_)


\_original\_\_init\_\_( _function_, _mobject_, _run\_time=3.0_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **function** ( _MethodType_)

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **run\_time** ( _float_)


Return type:

None