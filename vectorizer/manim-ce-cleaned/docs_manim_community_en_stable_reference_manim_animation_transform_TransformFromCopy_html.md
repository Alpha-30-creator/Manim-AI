# TransformFromCopy [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformFromCopy.html\#transformfromcopy "Link to this heading")

Qualified name: `manim.animation.transform.TransformFromCopy`

_class_ TransformFromCopy( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#TransformFromCopy) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformFromCopy.html#manim.animation.transform.TransformFromCopy "Link to this definition")

Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

Performs a reversed Transform

Methods

|     |     |
| --- | --- |
| [`interpolate`](https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformFromCopy.html#manim.animation.transform.TransformFromCopy.interpolate "manim.animation.transform.TransformFromCopy.interpolate") | Set the animation progress. |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **target\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


\_original\_\_init\_\_( _mobject_, _target\_mobject_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformFromCopy.html#manim.animation.transform.TransformFromCopy._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **target\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:

None

interpolate( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#TransformFromCopy.interpolate) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.TransformFromCopy.html#manim.animation.transform.TransformFromCopy.interpolate "Link to this definition")

Set the animation progress.

This method gets called for every frame during an animation.

Parameters:

**alpha** ( _float_) – The relative time to set the animation to, 0 meaning the start, 1 meaning
the end.

Return type:

None