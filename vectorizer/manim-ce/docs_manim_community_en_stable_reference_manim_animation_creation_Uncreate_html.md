ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.creation.Uncreate.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.creation.Uncreate.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Uncreate [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.Uncreate.html\#uncreate "Link to this heading")

Qualified name: `manim.animation.creation.Uncreate`

_class_ Uncreate( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#Uncreate) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.Uncreate.html#manim.animation.creation.Uncreate "Link to this definition")

Bases: [`Create`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create")

Like [`Create`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create") but in reverse.

Examples

Example: ShowUncreate [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.Uncreate.html#showuncreate)

```
from manim import *

class ShowUncreate(Scene):
    def construct(self):
        self.play(Uncreate(Square()))

```

Copy to clipboard

Make interactive

See also

[`Create`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create")

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

Parameters:

- **mobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ _OpenGLVMobject_)

- **reverse\_rate\_function** ( _bool_)

- **remover** ( _bool_)


\_original\_\_init\_\_( _mobject_, _reverse\_rate\_function=True_, _remover=True_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.Uncreate.html#manim.animation.creation.Uncreate._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ _OpenGLVMobject_)

- **reverse\_rate\_function** ( _bool_)

- **remover** ( _bool_)


Return type:

None

[**Simplify infrastructure** with MongoDB Atlas, the leading developer data platform](https://server.ethicalads.io/proxy/click/8268/019600e4-e236-77c1-be16-28e91261ee0d/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8268/019600e4-e236-77c1-be16-28e91261ee0d/)