# Blink [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html\#blink "Link to this heading")

Qualified name: `manim.animation.indication.Blink`

_class_ Blink( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html#Blink) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html#manim.animation.indication.Blink "Link to this definition")

Bases: [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession")

Blink the mobject.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be blinked.

- **time\_on** ( _float_) – The duration that the mobject is shown for one blink.

- **time\_off** ( _float_) – The duration that the mobject is hidden for one blink.

- **blinks** ( _int_) – The number of blinks

- **hide\_at\_end** ( _bool_) – Whether to hide the mobject at the end of the animation.

- **kwargs** – Additional arguments to be passed to the [`Succession`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession "manim.animation.composition.Succession") constructor.


Examples

Example: BlinkingExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html#blinkingexample)

```
from manim import *

class BlinkingExample(Scene):
    def construct(self):
        text = Text("Blinking").scale(1.5)
        self.add(text)
        self.play(Blink(text, blinks=3))

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

\_original\_\_init\_\_( _mobject_, _time\_on=0.5_, _time\_off=0.5_, _blinks=1_, _hide\_at\_end=False_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.Blink.html#manim.animation.indication.Blink._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **time\_on** ( _float_)

- **time\_off** ( _float_)

- **blinks** ( _int_)

- **hide\_at\_end** ( _bool_)


[Develop and launch modern apps with MongoDB Atlas, a resilient data platform.](https://server.ethicalads.io/proxy/click/8269/019600ee-30e0-7d90-9919-d26be4f0a315/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8269/019600ee-30e0-7d90-9919-d26be4f0a315/)