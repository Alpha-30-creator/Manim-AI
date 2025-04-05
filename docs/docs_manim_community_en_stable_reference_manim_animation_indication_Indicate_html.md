ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.indication.Indicate.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.indication.Indicate.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Indicate [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Indicate.html\#indicate "Link to this heading")

Qualified name: `manim.animation.indication.Indicate`

_class_ Indicate( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html#Indicate) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Indicate.html#manim.animation.indication.Indicate "Link to this definition")

Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

Indicate a Mobject by temporarily resizing and recoloring it.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to indicate.

- **scale\_factor** ( _float_) – The factor by which the mobject will be temporally scaled

- **color** ( _str_) – The color the mobject temporally takes.

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _,_ _float_ _\|_ _None_ _\]_ _,_ _np.ndarray_ _\]_) – The function defining the animation progress at every point in time.

- **kwargs** – Additional arguments to be passed to the [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession") constructor


Examples

Example: UsingIndicate [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Indicate.html#usingindicate)

```
from manim import *

class UsingIndicate(Scene):
    def construct(self):
        tex = Tex("Indicate").scale(3)
        self.play(Indicate(tex))
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

\_original\_\_init\_\_( _mobject_, _scale\_factor=1.2_, _color=ManimColor('#FFFF00')_, _rate\_func=<functionthere\_and\_back>_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Indicate.html#manim.animation.indication.Indicate._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **scale\_factor** ( _float_)

- **color** ( _str_)

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _,_ _float_ _\|_ _None_ _\]_ _,_ _ndarray_ _\]_)


Return type:

None