ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Create [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html\#create "Link to this heading")

Qualified name: `manim.animation.creation.Create`

_class_ Create( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#Create) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html#manim.animation.creation.Create "Link to this definition")

Bases: [`ShowPartial`](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowPartial.html#manim.animation.creation.ShowPartial "manim.animation.creation.ShowPartial")

Incrementally show a VMobject.

Parameters:

- **mobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ _OpenGLVMobject_ _\|_ _OpenGLSurface_) – The VMobject to animate.

- **lag\_ratio** ( _float_)

- **introducer** ( _bool_)


Raises:

**TypeError** – If `mobject` is not an instance of [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").

Examples

Example: CreateScene [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html#createscene)

```
from manim import *

class CreateScene(Scene):
    def construct(self):
        self.play(Create(Square()))

```

Copy to clipboard

Make interactive

See also

[`ShowPassingFlash`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash "manim.animation.indication.ShowPassingFlash")

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _mobject_, _lag\_ratio=1.0_, _introducer=True_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html#manim.animation.creation.Create._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ _OpenGLVMobject_ _\|_ _OpenGLSurface_)

- **lag\_ratio** ( _float_)

- **introducer** ( _bool_)


Return type:

None