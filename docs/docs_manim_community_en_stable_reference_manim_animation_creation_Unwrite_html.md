ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.creation.Unwrite.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.creation.Unwrite.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Unwrite [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.Unwrite.html\#unwrite "Link to this heading")

Qualified name: `manim.animation.creation.Unwrite`

_class_ Unwrite( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#Unwrite) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.Unwrite.html#manim.animation.creation.Unwrite "Link to this definition")

Bases: [`Write`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Write.html#manim.animation.creation.Write "manim.animation.creation.Write")

Simulate erasing by hand a [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or a [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").

Parameters:

- **reverse** ( _bool_) – Set True to have the animation start erasing from the last submobject first.

- **vmobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)


Examples

Example: UnwriteReverseTrue [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.Unwrite.html#unwritereversetrue)

```
from manim import *

class UnwriteReverseTrue(Scene):
    def construct(self):
        text = Tex("Alice and Bob").scale(3)
        self.add(text)
        self.play(Unwrite(text))

```

Copy to clipboard

Make interactive

Example: UnwriteReverseFalse [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.Unwrite.html#unwritereversefalse)

```
from manim import *

class UnwriteReverseFalse(Scene):
    def construct(self):
        text = Tex("Alice and Bob").scale(3)
        self.add(text)
        self.play(Unwrite(text, reverse=False))

```

Copy to clipboard

Make interactive

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _vmobject_, _rate\_func=<functionlinear>_, _reverse=True_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.Unwrite.html#manim.animation.creation.Unwrite._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **vmobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)

- **reverse** ( _bool_)


Return type:

None