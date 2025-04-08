# ApplyMethod [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html\#applymethod "Link to this heading")

Qualified name: `manim.animation.transform.ApplyMethod`

_class_ ApplyMethod( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#ApplyMethod) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "Link to this definition")

Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

Animates a mobject by applying a method.

Note that only the method needs to be passed to this animation,
it is not required to pass the corresponding mobject. Furthermore,
this animation class only works if the method returns the modified
mobject.

Parameters:

- **method** ( _Callable_) – The method that will be applied in the animation.

- **args** – Any positional arguments to be passed when applying the method.

- **kwargs** – Any keyword arguments passed to [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform").


Methods

|     |     |
| --- | --- |
| `check_validity_of_input` |  |
| `create_target` |  |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

\_original\_\_init\_\_( _method_, _\*args_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**method** ( _Callable_)

Return type:

None

[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/8271/019600f3-6224-76b2-95da-db8aa4169878/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8271/019600f3-6224-76b2-95da-db8aa4169878/)