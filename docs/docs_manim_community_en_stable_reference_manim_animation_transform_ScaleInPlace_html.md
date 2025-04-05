ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform.ScaleInPlace.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform.ScaleInPlace.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ScaleInPlace [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ScaleInPlace.html\#scaleinplace "Link to this heading")

Qualified name: `manim.animation.transform.ScaleInPlace`

_class_ ScaleInPlace( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#ScaleInPlace) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ScaleInPlace.html#manim.animation.transform.ScaleInPlace "Link to this definition")

Bases: [`ApplyMethod`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

Animation that scales a mobject by a certain factor.

Examples

Example: ScaleInPlaceExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ScaleInPlace.html#scaleinplaceexample)

```
from manim import *

class ScaleInPlaceExample(Scene):
    def construct(self):
        self.play(ScaleInPlace(Text("Hello World!"), 2))

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

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **scale\_factor** ( _float_)


\_original\_\_init\_\_( _mobject_, _scale\_factor_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ScaleInPlace.html#manim.animation.transform.ScaleInPlace._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **scale\_factor** ( _float_)


Return type:

None