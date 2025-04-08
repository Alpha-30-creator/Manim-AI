ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform.CounterclockwiseTransform.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform.CounterclockwiseTransform.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# CounterclockwiseTransform [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.CounterclockwiseTransform.html\#counterclockwisetransform "Link to this heading")

Qualified name: `manim.animation.transform.CounterclockwiseTransform`

_class_ CounterclockwiseTransform( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#CounterclockwiseTransform) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.CounterclockwiseTransform.html#manim.animation.transform.CounterclockwiseTransform "Link to this definition")

Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

Transforms the points of a mobject along a counterclockwise oriented arc.

See also

[`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform"), [`ClockwiseTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ClockwiseTransform.html#manim.animation.transform.ClockwiseTransform "manim.animation.transform.ClockwiseTransform")

Examples

Example: CounterclockwiseTransform\_vs\_Transform [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.CounterclockwiseTransform.html#counterclockwisetransform_vs_transform)

```
from manim import *

class CounterclockwiseTransform_vs_Transform(Scene):
    def construct(self):
        # set up the numbers
        c_transform = VGroup(DecimalNumber(number=3.141, num_decimal_places=3), DecimalNumber(number=1.618, num_decimal_places=3))
        text_1 = Text("CounterclockwiseTransform", color=RED)
        c_transform.add(text_1)

        transform = VGroup(DecimalNumber(number=1.618, num_decimal_places=3), DecimalNumber(number=3.141, num_decimal_places=3))
        text_2 = Text("Transform", color=BLUE)
        transform.add(text_2)

        ints = VGroup(c_transform, transform)
        texts = VGroup(text_1, text_2).scale(0.75)
        c_transform.arrange(direction=UP, buff=1)
        transform.arrange(direction=UP, buff=1)

        ints.arrange(buff=2)
        self.add(ints, texts)

        # The mobs move in clockwise direction for ClockwiseTransform()
        self.play(CounterclockwiseTransform(c_transform[0], c_transform[1]))

        # The mobs move straight up for Transform()
        self.play(Transform(transform[0], transform[1]))

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


\_original\_\_init\_\_( _mobject_, _target\_mobject_, _path\_arc=3.141592653589793_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.CounterclockwiseTransform.html#manim.animation.transform.CounterclockwiseTransform._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **target\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **path\_arc** ( _float_)


Return type:

None

[Develop and launch modern apps with MongoDB Atlas, a resilient data platform.](https://server.ethicalads.io/proxy/click/8269/019600e5-ec87-7df1-aff1-36ef3d691f11/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8269/019600e5-ec87-7df1-aff1-36ef3d691f11/)