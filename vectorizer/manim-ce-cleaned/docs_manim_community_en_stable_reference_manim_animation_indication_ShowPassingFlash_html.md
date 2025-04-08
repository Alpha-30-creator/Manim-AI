# ShowPassingFlash [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html\#showpassingflash "Link to this heading")

Qualified name: `manim.animation.indication.ShowPassingFlash`

_class_ ShowPassingFlash( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html#ShowPassingFlash) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash "Link to this definition")

Bases: [`ShowPartial`](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowPartial.html#manim.animation.creation.ShowPartial "manim.animation.creation.ShowPartial")

Show only a sliver of the VMobject each frame.

Parameters:

- **mobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The mobject whose stroke is animated.

- **time\_width** ( _float_) – The length of the sliver relative to the length of the stroke.


Examples

Example: TimeWidthValues [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html#timewidthvalues)

```
from manim import *

class TimeWidthValues(Scene):
    def construct(self):
        p = RegularPolygon(5, color=DARK_GRAY, stroke_width=6).scale(3)
        lbl = VMobject()
        self.add(p, lbl)
        p = p.copy().set_color(BLUE)
        for time_width in [0.2, 0.5, 1, 2]:
            lbl.become(Tex(r"\texttt{time\_width={{%.1f}}}"%time_width))
            self.play(ShowPassingFlash(
                p.copy().set_color(BLUE),
                run_time=2,
                time_width=time_width
            ))

```

Copy to clipboard

Make interactive

See also

[`Create`](https://docs.manim.community/en/stable/reference/manim.animation.creation.Create.html#manim.animation.creation.Create "manim.animation.creation.Create")

Methods

|     |     |
| --- | --- |
| [`clean_up_from_scene`](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash.clean_up_from_scene "manim.animation.indication.ShowPassingFlash.clean_up_from_scene") | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _mobject_, _time\_width=0.1_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

- **time\_width** ( _float_)


Return type:

None

clean\_up\_from\_scene( _scene_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/indication.html#ShowPassingFlash.clean_up_from_scene) [¶](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash.clean_up_from_scene "Link to this definition")

Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

Parameters:

**scene** ( [_Scene_](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

Return type:

None

[**The AI Agent that gets your codebase** Copilot & Cursor letting you down? Try Augment. **Install Now**](https://server.ethicalads.io/proxy/click/8458/019600f8-bac5-7fd0-8e43-7fb6a4aa3772/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/frontend-web/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8458/019600f8-bac5-7fd0-8e43-7fb6a4aa3772/)