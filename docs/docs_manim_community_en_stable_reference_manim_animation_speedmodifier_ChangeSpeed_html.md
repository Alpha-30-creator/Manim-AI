ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ChangeSpeed [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html\#changespeed "Link to this heading")

Qualified name: `manim.animation.speedmodifier.ChangeSpeed`

_class_ ChangeSpeed( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html#ChangeSpeed) [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

Modifies the speed of passed animation.
`AnimationGroup` with different `lag_ratio` can also be used
which combines multiple animations into one.
The `run_time` of the passed animation is changed to modify the speed.

Parameters:

- **anim** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\|_ _\_AnimationBuilder_) – Animation of which the speed is to be modified.

- **speedinfo** ( _dict_ _\[_ _float_ _,_ _float_ _\]_) – Contains nodes (percentage of `run_time`) and its corresponding speed factor.

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_ _\|_ _None_) – Overrides `rate_func` of passed animation, applied before changing speed.

- **affects\_speed\_updaters** ( _bool_)


Examples

Example: SpeedModifierExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#speedmodifierexample)

```
from manim import *

class SpeedModifierExample(Scene):
    def construct(self):
        a = Dot().shift(LEFT * 4)
        b = Dot().shift(RIGHT * 4)
        self.add(a, b)
        self.play(
            ChangeSpeed(
                AnimationGroup(
                    a.animate(run_time=1).shift(RIGHT * 8),
                    b.animate(run_time=1).shift(LEFT * 8),
                ),
                speedinfo={0.3: 1, 0.4: 0.1, 0.6: 0.1, 1: 1},
                rate_func=linear,
            )
        )

```

Copy to clipboard

Make interactive

Example: SpeedModifierUpdaterExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#speedmodifierupdaterexample)

```
from manim import *

class SpeedModifierUpdaterExample(Scene):
    def construct(self):
        a = Dot().shift(LEFT * 4)
        self.add(a)

        ChangeSpeed.add_updater(a, lambda x, dt: x.shift(RIGHT * 4 * dt))
        self.play(
            ChangeSpeed(
                Wait(2),
                speedinfo={0.4: 1, 0.5: 0.2, 0.8: 0.2, 1: 1},
                affects_speed_updaters=True,
            )
        )

```

Copy to clipboard

Make interactive

Example: SpeedModifierUpdaterExample2 [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#speedmodifierupdaterexample2)

```
from manim import *

class SpeedModifierUpdaterExample2(Scene):
    def construct(self):
        a = Dot().shift(LEFT * 4)
        self.add(a)

        ChangeSpeed.add_updater(a, lambda x, dt: x.shift(RIGHT * 4 * dt))
        self.wait()
        self.play(
            ChangeSpeed(
                Wait(),
                speedinfo={1: 0},
                affects_speed_updaters=True,
            )
        )

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`add_updater`](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.add_updater "manim.animation.speedmodifier.ChangeSpeed.add_updater") | This static method can be used to apply speed change to updaters. |
| [`begin`](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.begin "manim.animation.speedmodifier.ChangeSpeed.begin") | Begin the animation. |
| [`clean_up_from_scene`](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.clean_up_from_scene "manim.animation.speedmodifier.ChangeSpeed.clean_up_from_scene") | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
| [`finish`](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.finish "manim.animation.speedmodifier.ChangeSpeed.finish") | Finish the animation. |
| [`get_scaled_total_time`](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.get_scaled_total_time "manim.animation.speedmodifier.ChangeSpeed.get_scaled_total_time") | The time taken by the animation under the assumption that the `run_time` is 1. |
| [`interpolate`](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.interpolate "manim.animation.speedmodifier.ChangeSpeed.interpolate") | Set the animation progress. |
| `setup` |  |
| [`update_mobjects`](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.update_mobjects "manim.animation.speedmodifier.ChangeSpeed.update_mobjects") | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |

Attributes

|     |     |
| --- | --- |
| `dt` |  |
| `is_changing_dt` |  |
| `run_time` |  |

\_original\_\_init\_\_( _anim_, _speedinfo_, _rate\_func=None_, _affects\_speed\_updaters=True_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **anim** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\|_ _\_AnimationBuilder_)

- **speedinfo** ( _dict_ _\[_ _float_ _,_ _float_ _\]_)

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_ _\|_ _None_)

- **affects\_speed\_updaters** ( _bool_)


Return type:

None

\_setup\_scene( _scene_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html#ChangeSpeed._setup_scene) [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed._setup_scene "Link to this definition")

Setup up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") before starting the animation.

This includes to [`add()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") the Animation’s
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is an introducer.

Parameters:

**scene** – The scene the animation should be cleaned up from.

Return type:

None

_classmethod_ add\_updater( _mobject_, _update\_function_, _index=None_, _call\_updater=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html#ChangeSpeed.add_updater) [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.add_updater "Link to this definition")

This static method can be used to apply speed change to updaters.

This updater will follow speed and rate function of any [`ChangeSpeed`](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed "manim.animation.speedmodifier.ChangeSpeed")
animation that is playing with `affects_speed_updaters=True`. By default,
updater functions added via the usual [`Mobject.add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater") method
do not respect the change of animation speed.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to which the updater should be attached.

- **update\_function** ( _Updater_) – The function that is called whenever a new frame is rendered.

- **index** ( _int_ _\|_ _None_) – The position in the list of the mobject’s updaters at which the
function should be inserted.

- **call\_updater** ( _bool_) – If `True`, calls the update function when attaching it to the
mobject.


See also

[`ChangeSpeed`](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed "manim.animation.speedmodifier.ChangeSpeed"), [`Mobject.add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater")

begin() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html#ChangeSpeed.begin) [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.begin "Link to this definition")

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

Return type:

None

clean\_up\_from\_scene( _scene_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html#ChangeSpeed.clean_up_from_scene) [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.clean_up_from_scene "Link to this definition")

Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

Parameters:

**scene** ( [_Scene_](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

Return type:

None

finish() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html#ChangeSpeed.finish) [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.finish "Link to this definition")

Finish the animation.

This method gets called when the animation is over.

Return type:

None

get\_scaled\_total\_time() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html#ChangeSpeed.get_scaled_total_time) [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.get_scaled_total_time "Link to this definition")

The time taken by the animation under the assumption that the `run_time` is 1.

Return type:

float

interpolate( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html#ChangeSpeed.interpolate) [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.interpolate "Link to this definition")

Set the animation progress.

This method gets called for every frame during an animation.

Parameters:

**alpha** ( _float_) – The relative time to set the animation to, 0 meaning the start, 1 meaning
the end.

Return type:

None

update\_mobjects( _dt_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/speedmodifier.html#ChangeSpeed.update_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.animation.speedmodifier.ChangeSpeed.html#manim.animation.speedmodifier.ChangeSpeed.update_mobjects "Link to this definition")

Updates things like starting\_mobject, and (for
Transforms) target\_mobject. Note, since typically
(always?) self.mobject will have its updating
suspended during the animation, this will do
nothing to self.mobject.

Parameters:

**dt** ( _float_)

Return type:

None