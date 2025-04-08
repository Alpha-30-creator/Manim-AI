# MaintainPositionRelativeTo [¶](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.MaintainPositionRelativeTo.html\#maintainpositionrelativeto "Link to this heading")

Qualified name: `manim.animation.updaters.update.MaintainPositionRelativeTo`

_class_ MaintainPositionRelativeTo( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/updaters/update.html#MaintainPositionRelativeTo) [¶](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.MaintainPositionRelativeTo.html#manim.animation.updaters.update.MaintainPositionRelativeTo "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

Methods

|     |     |
| --- | --- |
| [`interpolate_mobject`](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.MaintainPositionRelativeTo.html#manim.animation.updaters.update.MaintainPositionRelativeTo.interpolate_mobject "manim.animation.updaters.update.MaintainPositionRelativeTo.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **tracked\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


\_original\_\_init\_\_( _mobject_, _tracked\_mobject_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.MaintainPositionRelativeTo.html#manim.animation.updaters.update.MaintainPositionRelativeTo._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **tracked\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:

None

interpolate\_mobject( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/updaters/update.html#MaintainPositionRelativeTo.interpolate_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.MaintainPositionRelativeTo.html#manim.animation.updaters.update.MaintainPositionRelativeTo.interpolate_mobject "Link to this definition")

Interpolates the mobject of the `Animation` based on alpha value.

Parameters:

**alpha** ( _float_) – A float between 0 and 1 expressing the ratio to which the animation
is completed. For example, alpha-values of 0, 0.5, and 1 correspond
to the animation being completed 0%, 50%, and 100%, respectively.

Return type:

None

[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/8271/019600f4-e684-7d71-a8e3-2b683c03c18e/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8271/019600f4-e684-7d71-a8e3-2b683c03c18e/)