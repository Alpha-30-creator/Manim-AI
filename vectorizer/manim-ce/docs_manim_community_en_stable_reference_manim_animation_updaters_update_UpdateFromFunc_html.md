ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromFunc.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromFunc.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# UpdateFromFunc [¶](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromFunc.html\#updatefromfunc "Link to this heading")

Qualified name: `manim.animation.updaters.update.UpdateFromFunc`

_class_ UpdateFromFunc( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/updaters/update.html#UpdateFromFunc) [¶](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromFunc.html#manim.animation.updaters.update.UpdateFromFunc "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

update\_function of the form func(mobject), presumably
to be used when the state of one mobject is dependent
on another simultaneously animated mobject

Methods

|     |     |
| --- | --- |
| [`interpolate_mobject`](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromFunc.html#manim.animation.updaters.update.UpdateFromFunc.interpolate_mobject "manim.animation.updaters.update.UpdateFromFunc.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **update\_function** ( _Callable_ _\[_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_ _,_ _Any_ _\]_)

- **suspend\_mobject\_updating** ( _bool_)


\_original\_\_init\_\_( _mobject_, _update\_function_, _suspend\_mobject\_updating=False_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromFunc.html#manim.animation.updaters.update.UpdateFromFunc._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **update\_function** ( _Callable_ _\[_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_ _,_ _Any_ _\]_)

- **suspend\_mobject\_updating** ( _bool_)


Return type:

None

interpolate\_mobject( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/updaters/update.html#UpdateFromFunc.interpolate_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromFunc.html#manim.animation.updaters.update.UpdateFromFunc.interpolate_mobject "Link to this definition")

Interpolates the mobject of the `Animation` based on alpha value.

Parameters:

**alpha** ( _float_) – A float between 0 and 1 expressing the ratio to which the animation
is completed. For example, alpha-values of 0, 0.5, and 1 correspond
to the animation being completed 0%, 50%, and 100%, respectively.

Return type:

None

[Simplified data ingestion for developers **Get Algolia Crawler**](https://server.ethicalads.io/proxy/click/8327/019600ea-25fb-7873-aa1d-31401d7bcf99/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/frontend-web/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8327/019600ea-25fb-7873-aa1d-31401d7bcf99/)