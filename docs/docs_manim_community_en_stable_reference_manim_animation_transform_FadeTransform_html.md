ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# FadeTransform [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html\#fadetransform "Link to this heading")

Qualified name: `manim.animation.transform.FadeTransform`

_class_ FadeTransform( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#FadeTransform) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform "Link to this definition")

Bases: [`Transform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

Fades one mobject into another.

Parameters:

- **mobject** – The starting [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **target\_mobject** – The target [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **stretch** – Controls whether the target [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") is stretched during
the animation. Default: `True`.

- **dim\_to\_match** – If the target mobject is not stretched automatically, this allows
to adjust the initial scale of the target [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") while
it is shifted in. Setting this to 0, 1, and 2, respectively,
matches the length of the target with the length of the starting
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") in x, y, and z direction, respectively.

- **kwargs** – Further keyword arguments are passed to the parent class.


Examples

Example: DifferentFadeTransforms [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#differentfadetransforms)

```
from manim import *

class DifferentFadeTransforms(Scene):
    def construct(self):
        starts = [Rectangle(width=4, height=1) for _ in range(3)]
        VGroup(*starts).arrange(DOWN, buff=1).shift(3*LEFT)
        targets = [Circle(fill_opacity=1).scale(0.25) for _ in range(3)]
        VGroup(*targets).arrange(DOWN, buff=1).shift(3*RIGHT)

        self.play(*[FadeIn(s) for s in starts])
        self.play(
            FadeTransform(starts[0], targets[0], stretch=True),
            FadeTransform(starts[1], targets[1], stretch=False, dim_to_match=0),
            FadeTransform(starts[2], targets[2], stretch=False, dim_to_match=1)
        )

        self.play(*[FadeOut(mobj) for mobj in self.mobjects])

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`begin`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform.begin "manim.animation.transform.FadeTransform.begin") | Initial setup for the animation. |
| [`clean_up_from_scene`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform.clean_up_from_scene "manim.animation.transform.FadeTransform.clean_up_from_scene") | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
| `get_all_families_zipped` |  |
| [`get_all_mobjects`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform.get_all_mobjects "manim.animation.transform.FadeTransform.get_all_mobjects") | Get all mobjects involved in the animation. |
| [`ghost_to`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform.ghost_to "manim.animation.transform.FadeTransform.ghost_to") | Replaces the source by the target and sets the opacity to 0. |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

\_original\_\_init\_\_( _mobject_, _target\_mobject_, _stretch=True_, _dim\_to\_match=1_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

begin() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#FadeTransform.begin) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform.begin "Link to this definition")

Initial setup for the animation.

The mobject to which this animation is bound is a group consisting of
both the starting and the ending mobject. At the start, the ending
mobject replaces the starting mobject (and is completely faded). In the
end, it is set to be the other way around.

clean\_up\_from\_scene( _scene_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#FadeTransform.clean_up_from_scene) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform.clean_up_from_scene "Link to this definition")

Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

Parameters:

**scene** – The scene the animation should be cleaned up from.

get\_all\_mobjects() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#FadeTransform.get_all_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform.get_all_mobjects "Link to this definition")

Get all mobjects involved in the animation.

Ordering must match the ordering of arguments to interpolate\_submobject

Returns:

The sequence of mobjects.

Return type:

Sequence\[ [Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")\]

ghost\_to( _source_, _target_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#FadeTransform.ghost_to) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform.ghost_to "Link to this definition")

Replaces the source by the target and sets the opacity to 0.

If the provided target has no points, and thus a location of \[0, 0, 0\]
the source will simply fade out where it currently is.

[**Simplify infrastructure** with MongoDB Atlas, the leading developer data platform](https://server.ethicalads.io/proxy/click/8268/019600f3-547a-7e50-8ef1-848e5c1c7634/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8268/019600f3-547a-7e50-8ef1-848e5c1c7634/)