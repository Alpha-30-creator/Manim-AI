ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.indication.Wiggle.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.indication.Wiggle.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Wiggle [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Wiggle.html\#wiggle "Link to this heading")

Qualified name: `manim.animation.indication.Wiggle`

_class_ Wiggle( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html#Wiggle) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Wiggle.html#manim.animation.indication.Wiggle "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

Wiggle a Mobject.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to wiggle.

- **scale\_value** ( _float_) – The factor by which the mobject will be temporarily scaled.

- **rotation\_angle** ( _float_) – The wiggle angle.

- **n\_wiggles** ( _int_) – The number of wiggles.

- **scale\_about\_point** ( _np.ndarray_ _\|_ _None_) – The point about which the mobject gets scaled.

- **rotate\_about\_point** ( _np.ndarray_ _\|_ _None_) – The point around which the mobject gets rotated.

- **run\_time** ( _float_) – The duration of the animation


Examples

Example: ApplyingWaves [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Wiggle.html#applyingwaves)

```
from manim import *

class ApplyingWaves(Scene):
    def construct(self):
        tex = Tex("Wiggle").scale(3)
        self.play(Wiggle(tex))
        self.wait()

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `get_rotate_about_point` |  |
| `get_scale_about_point` |  |
| `interpolate_submobject` |  |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _mobject_, _scale\_value=1.1_, _rotation\_angle=0.06283185307179587_, _n\_wiggles=6_, _scale\_about\_point=None_, _rotate\_about\_point=None_, _run\_time=2_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Wiggle.html#manim.animation.indication.Wiggle._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **scale\_value** ( _float_)

- **rotation\_angle** ( _float_)

- **n\_wiggles** ( _int_)

- **scale\_about\_point** ( _ndarray_ _\|_ _None_)

- **rotate\_about\_point** ( _ndarray_ _\|_ _None_)

- **run\_time** ( _float_)


Return type:

None

[Develop and launch modern apps with MongoDB Atlas, a resilient data platform.](https://server.ethicalads.io/proxy/click/8269/019600f0-024a-7123-aa29-913dabb51af8/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8269/019600f0-024a-7123-aa29-913dabb51af8/)