# FadeOut [¶](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html\#fadeout "Link to this heading")

Qualified name: `manim.animation.fading.FadeOut`

_class_ FadeOut( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/fading.html#FadeOut) [¶](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html#manim.animation.fading.FadeOut "Link to this definition")

Bases: `_Fade`

Fade out [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") s.

Parameters:

- **mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to be faded out.

- **shift** – The vector by which the mobject shifts while being faded out.

- **target\_position** – The position to which the mobject moves while being faded out. In case another
mobject is given as target position, its center is used.

- **scale** – The factor by which the mobject is scaled while being faded out.


Examples

Example: FadeInExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html#fadeinexample)

```
from manim import *

class FadeInExample(Scene):
    def construct(self):
        dot = Dot(UP * 2 + LEFT)
        self.add(dot)
        tex = Tex(
            "FadeOut with ", "shift ", r" or target\_position", " and scale"
        ).scale(1)
        animations = [\
            FadeOut(tex[0]),\
            FadeOut(tex[1], shift=DOWN),\
            FadeOut(tex[2], target_position=dot),\
            FadeOut(tex[3], scale=0.5),\
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`clean_up_from_scene`](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html#manim.animation.fading.FadeOut.clean_up_from_scene "manim.animation.fading.FadeOut.clean_up_from_scene") | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
| `create_target` |  |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

\_original\_\_init\_\_( _\*mobjects_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html#manim.animation.fading.FadeOut._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

Return type:

None

clean\_up\_from\_scene( _scene=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/fading.html#FadeOut.clean_up_from_scene) [¶](https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html#manim.animation.fading.FadeOut.clean_up_from_scene "Link to this definition")

Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

Parameters:

**scene** ( [_Scene_](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

Return type:

None