ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform.ShrinkToCenter.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform.ShrinkToCenter.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ShrinkToCenter [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ShrinkToCenter.html\#shrinktocenter "Link to this heading")

Qualified name: `manim.animation.transform.ShrinkToCenter`

_class_ ShrinkToCenter( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#ShrinkToCenter) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ShrinkToCenter.html#manim.animation.transform.ShrinkToCenter "Link to this definition")

Bases: [`ScaleInPlace`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ScaleInPlace.html#manim.animation.transform.ScaleInPlace "manim.animation.transform.ScaleInPlace")

Animation that makes a mobject shrink to center.

Examples

Example: ShrinkToCenterExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ShrinkToCenter.html#shrinktocenterexample)

```
from manim import *

class ShrinkToCenterExample(Scene):
    def construct(self):
        self.play(ShrinkToCenter(Text("Hello World!")))

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

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

\_original\_\_init\_\_( _mobject_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ShrinkToCenter.html#manim.animation.transform.ShrinkToCenter._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

Return type:

None