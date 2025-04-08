# TransformAnimations [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformAnimations.html\#transformanimations "Link to this heading")

Qualified name: `manim.animation.transform.TransformAnimations`

_class_ TransformAnimations( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#TransformAnimations) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformAnimations.html#manim.animation.transform.TransformAnimations "Link to this definition")

Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

Methods

|     |     |
| --- | --- |
| [`interpolate`](https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformAnimations.html#manim.animation.transform.TransformAnimations.interpolate "manim.animation.transform.TransformAnimations.interpolate") | Set the animation progress. |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

Parameters:

- **start\_anim** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))

- **end\_anim** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))

- **rate\_func** ( _Callable_)


\_original\_\_init\_\_( _start\_anim_, _end\_anim_, _rate\_func=<functionsquish\_rate\_func.<locals>.result>_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformAnimations.html#manim.animation.transform.TransformAnimations._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **start\_anim** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))

- **end\_anim** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))

- **rate\_func** ( _Callable_)


Return type:

None

interpolate( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#TransformAnimations.interpolate) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformAnimations.html#manim.animation.transform.TransformAnimations.interpolate "Link to this definition")

Set the animation progress.

This method gets called for every frame during an animation.

Parameters:

**alpha** ( _float_) – The relative time to set the animation to, 0 meaning the start, 1 meaning
the end.

Return type:

None