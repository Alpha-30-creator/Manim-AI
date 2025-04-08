ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromAlphaFunc.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromAlphaFunc.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# UpdateFromAlphaFunc [¶](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromAlphaFunc.html\#updatefromalphafunc "Link to this heading")

Qualified name: `manim.animation.updaters.update.UpdateFromAlphaFunc`

_class_ UpdateFromAlphaFunc( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/updaters/update.html#UpdateFromAlphaFunc) [¶](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromAlphaFunc.html#manim.animation.updaters.update.UpdateFromAlphaFunc "Link to this definition")

Bases: [`UpdateFromFunc`](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromFunc.html#manim.animation.updaters.update.UpdateFromFunc "manim.animation.updaters.update.UpdateFromFunc")

Methods

|     |     |
| --- | --- |
| [`interpolate_mobject`](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromAlphaFunc.html#manim.animation.updaters.update.UpdateFromAlphaFunc.interpolate_mobject "manim.animation.updaters.update.UpdateFromAlphaFunc.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **update\_function** ( _Callable_ _\[_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_ _,_ _Any_ _\]_)

- **suspend\_mobject\_updating** ( _bool_)


\_original\_\_init\_\_( _mobject_, _update\_function_, _suspend\_mobject\_updating=False_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromAlphaFunc.html#manim.animation.updaters.update.UpdateFromAlphaFunc._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **update\_function** ( _Callable_ _\[_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_ _,_ _Any_ _\]_)

- **suspend\_mobject\_updating** ( _bool_)


Return type:

None

interpolate\_mobject( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/updaters/update.html#UpdateFromAlphaFunc.interpolate_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromAlphaFunc.html#manim.animation.updaters.update.UpdateFromAlphaFunc.interpolate_mobject "Link to this definition")

Interpolates the mobject of the `Animation` based on alpha value.

Parameters:

**alpha** ( _float_) – A float between 0 and 1 expressing the ratio to which the animation
is completed. For example, alpha-values of 0, 0.5, and 1 correspond
to the animation being completed 0%, 50%, and 100%, respectively.

Return type:

None