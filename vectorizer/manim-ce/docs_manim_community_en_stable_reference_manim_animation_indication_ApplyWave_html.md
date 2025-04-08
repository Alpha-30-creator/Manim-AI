ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.indication.ApplyWave.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.indication.ApplyWave.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ApplyWave [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.ApplyWave.html\#applywave "Link to this heading")

Qualified name: `manim.animation.indication.ApplyWave`

_class_ ApplyWave( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html#ApplyWave) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.ApplyWave.html#manim.animation.indication.ApplyWave "Link to this definition")

Bases: [`Homotopy`](https://docs.manim.community/en/stable/reference/manim.animation.movement.Homotopy.html#manim.animation.movement.Homotopy "manim.animation.movement.Homotopy")

Send a wave through the Mobject distorting it temporarily.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be distorted.

- **direction** ( _np.ndarray_) – The direction in which the wave nudges points of the shape

- **amplitude** ( _float_) – The distance points of the shape get shifted

- **wave\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_) – The function defining the shape of one wave flank.

- **time\_width** ( _float_) – The length of the wave relative to the width of the mobject.

- **ripples** ( _int_) – The number of ripples of the wave

- **run\_time** ( _float_) – The duration of the animation.


Examples

Example: ApplyingWaves [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.ApplyWave.html#applyingwaves)

```
from manim import *

class ApplyingWaves(Scene):
    def construct(self):
        tex = Tex("WaveWaveWaveWaveWave").scale(2)
        self.play(ApplyWave(tex))
        self.play(ApplyWave(
            tex,
            direction=RIGHT,
            time_width=0.5,
            amplitude=0.3
        ))
        self.play(ApplyWave(
            tex,
            rate_func=linear,
            ripples=4
        ))

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

\_original\_\_init\_\_( _mobject_, _direction=array(\[0._, _1._, _0.\])_, _amplitude=0.2_, _wave\_func=<functionsmooth>_, _time\_width=1_, _ripples=1_, _run\_time=2_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.ApplyWave.html#manim.animation.indication.ApplyWave._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **direction** ( _ndarray_)

- **amplitude** ( _float_)

- **wave\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)

- **time\_width** ( _float_)

- **ripples** ( _int_)

- **run\_time** ( _float_)


Return type:

None

[**Simplify infrastructure** with MongoDB Atlas, the leading developer data platform](https://server.ethicalads.io/proxy/click/8268/019600e4-e236-77c1-be16-28e91261ee0d/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8268/019600e4-e236-77c1-be16-28e91261ee0d/)