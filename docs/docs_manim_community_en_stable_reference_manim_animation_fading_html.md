ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.fading.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.fading.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# fading [¶](https://docs.manim.community/en/stable/reference/manim.animation.fading.html\#module-manim.animation.fading "Link to this heading")

Fading in and out of view.

Example: Fading [¶](https://docs.manim.community/en/stable/reference/manim.animation.fading.html#fading)

```
from manim import *

class Fading(Scene):
    def construct(self):
        tex_in = Tex("Fade", "In").scale(3)
        tex_out = Tex("Fade", "Out").scale(3)
        self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
        self.play(ReplacementTransform(tex_in, tex_out))
        self.play(FadeOut(tex_out, shift=DOWN * 2, scale=1.5))

```

Copy to clipboard

Make interactive

Classes

|     |     |
| --- | --- |
| [`FadeIn`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeIn.html#manim.animation.fading.FadeIn "manim.animation.fading.FadeIn") | Fade in [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") s. |
| [`FadeOut`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html#manim.animation.fading.FadeOut "manim.animation.fading.FadeOut") | Fade out [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") s. |