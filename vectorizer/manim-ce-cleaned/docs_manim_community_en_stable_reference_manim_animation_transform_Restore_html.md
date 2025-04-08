# Restore [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html\#restore "Link to this heading")

Qualified name: `manim.animation.transform.Restore`

_class_ Restore( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#Restore) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html#manim.animation.transform.Restore "Link to this definition")

Bases: [`ApplyMethod`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

Transforms a mobject to its last saved state.

To save the state of a mobject, use the [`save_state()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.save_state "manim.mobject.mobject.Mobject.save_state") method.

Examples

Example: RestoreExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html#restoreexample)

```
from manim import *

class RestoreExample(Scene):
    def construct(self):
        s = Square()
        s.save_state()
        self.play(FadeIn(s))
        self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
        self.play(s.animate.shift(5*DOWN).rotate(PI/4))
        self.wait()
        self.play(Restore(s), run_time=2)

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

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

\_original\_\_init\_\_( _mobject_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.Restore.html#manim.animation.transform.Restore._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

Return type:

None

[Automate site indexing, catalog pages, & refine your search accuracy with Algolia’s website crawler](https://server.ethicalads.io/proxy/click/8328/019600f0-be0e-7ed2-ad68-718ec67e122c/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/frontend-web/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8328/019600f0-be0e-7ed2-ad68-718ec67e122c/)