# ChangingDecimal [¶](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html\#changingdecimal "Link to this heading")

Qualified name: `manim.animation.numbers.ChangingDecimal`

_class_ ChangingDecimal( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/numbers.html#ChangingDecimal) [¶](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html#manim.animation.numbers.ChangingDecimal "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

Methods

|     |     |
| --- | --- |
| `check_validity_of_input` |  |
| [`interpolate_mobject`](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html#manim.animation.numbers.ChangingDecimal.interpolate_mobject "manim.animation.numbers.ChangingDecimal.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

Parameters:

- **decimal\_mob** ( [_DecimalNumber_](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber"))

- **number\_update\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)

- **suspend\_mobject\_updating** ( _bool_ _\|_ _None_)


\_original\_\_init\_\_( _decimal\_mob_, _number\_update\_func_, _suspend\_mobject\_updating=False_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html#manim.animation.numbers.ChangingDecimal._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **decimal\_mob** ( [_DecimalNumber_](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber"))

- **number\_update\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)

- **suspend\_mobject\_updating** ( _bool_ _\|_ _None_)


Return type:

None

interpolate\_mobject( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/numbers.html#ChangingDecimal.interpolate_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.animation.numbers.ChangingDecimal.html#manim.animation.numbers.ChangingDecimal.interpolate_mobject "Link to this definition")

Interpolates the mobject of the `Animation` based on alpha value.

Parameters:

**alpha** ( _float_) – A float between 0 and 1 expressing the ratio to which the animation
is completed. For example, alpha-values of 0, 0.5, and 1 correspond
to the animation being completed 0%, 50%, and 100%, respectively.

Return type:

None

[Develop and launch modern apps with MongoDB Atlas, a resilient data platform.](https://server.ethicalads.io/proxy/click/8269/019600eb-e59a-7410-9fcd-4e9f9f9e4fa3/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8269/019600eb-e59a-7410-9fcd-4e9f9f9e4fa3/)