ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.indication.FocusOn.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.indication.FocusOn.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# FocusOn [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.FocusOn.html\#focuson "Link to this heading")

Qualified name: `manim.animation.indication.FocusOn`

_class_ FocusOn( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html#FocusOn) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.FocusOn.html#manim.animation.indication.FocusOn "Link to this definition")

Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

Shrink a spotlight to a position.

Parameters:

- **focus\_point** ( _np.ndarray_ _\|_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The point at which to shrink the spotlight. If it is a `Mobject` its center will be used.

- **opacity** ( _float_) – The opacity of the spotlight.

- **color** ( _str_) – The color of the spotlight.

- **run\_time** ( _float_) – The duration of the animation.


Examples

Example: UsingFocusOn [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.FocusOn.html#usingfocuson)

```
from manim import *

class UsingFocusOn(Scene):
    def construct(self):
        dot = Dot(color=YELLOW).shift(DOWN)
        self.add(Tex("Focusing on the dot below:"), dot)
        self.play(FocusOn(dot))
        self.wait()

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `create_target` |  |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

\_original\_\_init\_\_( _focus\_point_, _opacity=0.2_, _color=ManimColor('#888888')_, _run\_time=2_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.FocusOn.html#manim.animation.indication.FocusOn._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **focus\_point** ( _ndarray_ _\|_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **opacity** ( _float_)

- **color** ( _str_)

- **run\_time** ( _float_)


Return type:

None