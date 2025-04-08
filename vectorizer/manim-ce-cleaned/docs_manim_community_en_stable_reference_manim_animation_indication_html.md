# indication [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.html\#module-manim.animation.indication "Link to this heading")

Animations drawing attention to particular mobjects.

Examples

Example: Indications [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.html#indications)

```
from manim import *

class Indications(Scene):
    def construct(self):
        indications = [ApplyWave,Circumscribe,Flash,FocusOn,Indicate,ShowPassingFlash,Wiggle]
        names = [Tex(i.__name__).scale(3) for i in indications]

        self.add(names[0])
        for i in range(len(names)):
            if indications[i] is Flash:
                self.play(Flash(UP))
            elif indications[i] is ShowPassingFlash:
                self.play(ShowPassingFlash(Underline(names[i])))
            else:
                self.play(indications[i](names[i]))
            self.play(AnimationGroup(
                FadeOut(names[i], shift=UP*1.5),
                FadeIn(names[(i+1)%len(names)], shift=UP*1.5),
            ))

```

Copy to clipboard

Make interactive

Classes

|     |     |
| --- | --- |
| [`ApplyWave`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ApplyWave.html#manim.animation.indication.ApplyWave "manim.animation.indication.ApplyWave") | Send a wave through the Mobject distorting it temporarily. |
| [`Blink`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html#manim.animation.indication.Blink "manim.animation.indication.Blink") | Blink the mobject. |
| [`Circumscribe`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Circumscribe.html#manim.animation.indication.Circumscribe "manim.animation.indication.Circumscribe") | Draw a temporary line surrounding the mobject. |
| [`Flash`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Flash.html#manim.animation.indication.Flash "manim.animation.indication.Flash") | Send out lines in all directions. |
| [`FocusOn`](https://docs.manim.community/en/stable/reference/manim.animation.indication.FocusOn.html#manim.animation.indication.FocusOn "manim.animation.indication.FocusOn") | Shrink a spotlight to a position. |
| [`Indicate`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Indicate.html#manim.animation.indication.Indicate "manim.animation.indication.Indicate") | Indicate a Mobject by temporarily resizing and recoloring it. |
| [`ShowPassingFlash`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash "manim.animation.indication.ShowPassingFlash") | Show only a sliver of the VMobject each frame. |
| [`ShowPassingFlashWithThinningStrokeWidth`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth.html#manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth "manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth") |  |
| [`Wiggle`](https://docs.manim.community/en/stable/reference/manim.animation.indication.Wiggle.html#manim.animation.indication.Wiggle "manim.animation.indication.Wiggle") | Wiggle a Mobject. |