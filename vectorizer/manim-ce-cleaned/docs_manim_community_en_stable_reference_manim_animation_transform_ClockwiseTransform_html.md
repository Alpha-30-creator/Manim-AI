# ClockwiseTransform [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ClockwiseTransform.html\#clockwisetransform "Link to this heading")

Qualified name: `manim.animation.transform.ClockwiseTransform`

_class_ ClockwiseTransform( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#ClockwiseTransform) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ClockwiseTransform.html#manim.animation.transform.ClockwiseTransform "Link to this definition")

Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

Transforms the points of a mobject along a clockwise oriented arc.

See also

[`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform"), [`CounterclockwiseTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.CounterclockwiseTransform.html#manim.animation.transform.CounterclockwiseTransform "manim.animation.transform.CounterclockwiseTransform")

Examples

Example: ClockwiseExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ClockwiseTransform.html#clockwiseexample)

```
from manim import *

class ClockwiseExample(Scene):
    def construct(self):
        dl, dr = Dot(), Dot()
        sl, sr = Square(), Square()

        VGroup(dl, sl).arrange(DOWN).shift(2*LEFT)
        VGroup(dr, sr).arrange(DOWN).shift(2*RIGHT)

        self.add(dl, dr)
        self.wait()
        self.play(
            ClockwiseTransform(dl, sl),
            Transform(dr, sr)
        )
        self.wait()

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

- **target\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **path\_arc** ( _float_)


\_original\_\_init\_\_( _mobject_, _target\_mobject_, _path\_arc=-3.141592653589793_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ClockwiseTransform.html#manim.animation.transform.ClockwiseTransform._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **target\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **path\_arc** ( _float_)


Return type:

None

[**Simplify infrastructure** with MongoDB Atlas, the leading developer data platform](https://server.ethicalads.io/proxy/click/8268/019600e9-201a-7b62-93ad-d2587790f875/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8268/019600e9-201a-7b62-93ad-d2587790f875/)