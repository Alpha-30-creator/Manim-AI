# ApplyPointwiseFunctionToCenter [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunctionToCenter.html\#applypointwisefunctiontocenter "Link to this heading")

Qualified name: `manim.animation.transform.ApplyPointwiseFunctionToCenter`

_class_ ApplyPointwiseFunctionToCenter( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#ApplyPointwiseFunctionToCenter) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunctionToCenter.html#manim.animation.transform.ApplyPointwiseFunctionToCenter "Link to this definition")

Bases: [`ApplyPointwiseFunction`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction "manim.animation.transform.ApplyPointwiseFunction")

Methods

|     |     |
| --- | --- |
| [`begin`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunctionToCenter.html#manim.animation.transform.ApplyPointwiseFunctionToCenter.begin "manim.animation.transform.ApplyPointwiseFunctionToCenter.begin") | Begin the animation. |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

Parameters:

- **function** ( _types.MethodType_)

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


\_original\_\_init\_\_( _function_, _mobject_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunctionToCenter.html#manim.animation.transform.ApplyPointwiseFunctionToCenter._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **function** ( _MethodType_)

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:

None

begin() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#ApplyPointwiseFunctionToCenter.begin) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunctionToCenter.html#manim.animation.transform.ApplyPointwiseFunctionToCenter.begin "Link to this definition")

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

Return type:

None