ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Succession [¶](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html\#succession "Link to this heading")

Qualified name: `manim.animation.composition.Succession`

_class_ Succession( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html#Succession) [¶](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession "Link to this definition")

Bases: [`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

Plays a series of animations in succession.

Parameters:

- **animations** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")) – Sequence of [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") objects to be played.

- **lag\_ratio** ( _float_) –

Defines the delay after which the animation is applied to submobjects. A lag\_ratio of
`n.nn` means the next animation will play when `nnn%` of the current animation has played.
Defaults to 1.0, meaning that the next animation will begin when 100% of the current
animation has played.

This does not influence the total runtime of the animation. Instead the runtime
of individual animations is adjusted so that the complete animation has the defined
run time.


Examples

Example: SuccessionExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#successionexample)

```
from manim import *

class SuccessionExample(Scene):
    def construct(self):
        dot1 = Dot(point=LEFT * 2 + UP * 2, radius=0.16, color=BLUE)
        dot2 = Dot(point=LEFT * 2 + DOWN * 2, radius=0.16, color=MAROON)
        dot3 = Dot(point=RIGHT * 2 + DOWN * 2, radius=0.16, color=GREEN)
        dot4 = Dot(point=RIGHT * 2 + UP * 2, radius=0.16, color=YELLOW)
        self.add(dot1, dot2, dot3, dot4)

        self.play(Succession(
            dot1.animate.move_to(dot2),
            dot2.animate.move_to(dot3),
            dot3.animate.move_to(dot4),
            dot4.animate.move_to(dot1)
        ))

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`begin`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession.begin "manim.animation.composition.Succession.begin") | Begin the animation. |
| [`finish`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession.finish "manim.animation.composition.Succession.finish") | Finish the animation. |
| [`interpolate`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession.interpolate "manim.animation.composition.Succession.interpolate") | Set the animation progress. |
| [`next_animation`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession.next_animation "manim.animation.composition.Succession.next_animation") | Proceeds to the next animation. |
| `update_active_animation` |  |
| [`update_mobjects`](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession.update_mobjects "manim.animation.composition.Succession.update_mobjects") | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _\*animations_, _lag\_ratio=1_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **animations** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))

- **lag\_ratio** ( _float_)


Return type:

None

\_setup\_scene( _scene_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html#Succession._setup_scene) [¶](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession._setup_scene "Link to this definition")

Setup up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") before starting the animation.

This includes to [`add()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") the Animation’s
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is an introducer.

Parameters:

**scene** – The scene the animation should be cleaned up from.

Return type:

None

begin() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html#Succession.begin) [¶](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession.begin "Link to this definition")

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

Return type:

None

finish() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html#Succession.finish) [¶](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession.finish "Link to this definition")

Finish the animation.

This method gets called when the animation is over.

Return type:

None

interpolate( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html#Succession.interpolate) [¶](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession.interpolate "Link to this definition")

Set the animation progress.

This method gets called for every frame during an animation.

Parameters:

**alpha** ( _float_) – The relative time to set the animation to, 0 meaning the start, 1 meaning
the end.

Return type:

None

next\_animation() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html#Succession.next_animation) [¶](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession.next_animation "Link to this definition")

Proceeds to the next animation.

This method is called right when the active animation finishes.

Return type:

None

update\_mobjects( _dt_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/composition.html#Succession.update_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.animation.composition.Succession.html#manim.animation.composition.Succession.update_mobjects "Link to this definition")

Updates things like starting\_mobject, and (for
Transforms) target\_mobject. Note, since typically
(always?) self.mobject will have its updating
suspended during the animation, this will do
nothing to self.mobject.

Parameters:

**dt** ( _float_)

Return type:

None