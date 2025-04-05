ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.movement.PhaseFlow.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.movement.PhaseFlow.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# PhaseFlow [¶](https://docs.manim.community/en/stable/reference/manim.animation.movement.PhaseFlow.html\#phaseflow "Link to this heading")

Qualified name: `manim.animation.movement.PhaseFlow`

_class_ PhaseFlow( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/movement.html#PhaseFlow) [¶](https://docs.manim.community/en/stable/reference/manim.animation.movement.PhaseFlow.html#manim.animation.movement.PhaseFlow "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

Methods

|     |     |
| --- | --- |
| [`interpolate_mobject`](https://docs.manim.community/en/stable/reference/manim.animation.movement.PhaseFlow.html#manim.animation.movement.PhaseFlow.interpolate_mobject "manim.animation.movement.PhaseFlow.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

Parameters:

- **function** ( _Callable_ _\[_ _\[_ _np.ndarray_ _\]_ _,_ _np.ndarray_ _\]_)

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **virtual\_time** ( _float_)

- **suspend\_mobject\_updating** ( _bool_)

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)


\_original\_\_init\_\_( _function_, _mobject_, _virtual\_time=1_, _suspend\_mobject\_updating=False_, _rate\_func=<functionlinear>_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.movement.PhaseFlow.html#manim.animation.movement.PhaseFlow._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **function** ( _Callable_ _\[_ _\[_ _np.ndarray_ _\]_ _,_ _np.ndarray_ _\]_)

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **virtual\_time** ( _float_)

- **suspend\_mobject\_updating** ( _bool_)

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)


Return type:

None

interpolate\_mobject( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/movement.html#PhaseFlow.interpolate_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.animation.movement.PhaseFlow.html#manim.animation.movement.PhaseFlow.interpolate_mobject "Link to this definition")

Interpolates the mobject of the `Animation` based on alpha value.

Parameters:

**alpha** ( _float_) – A float between 0 and 1 expressing the ratio to which the animation
is completed. For example, alpha-values of 0, 0.5, and 1 correspond
to the animation being completed 0%, 50%, and 100%, respectively.

Return type:

None