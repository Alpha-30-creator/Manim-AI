ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowIncreasingSubsets.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowIncreasingSubsets.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ShowIncreasingSubsets [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowIncreasingSubsets.html\#showincreasingsubsets "Link to this heading")

Qualified name: `manim.animation.creation.ShowIncreasingSubsets`

_class_ ShowIncreasingSubsets( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#ShowIncreasingSubsets) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowIncreasingSubsets.html#manim.animation.creation.ShowIncreasingSubsets "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

Show one submobject at a time, leaving all previous ones displayed on screen.

Examples

Example: ShowIncreasingSubsetsScene [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowIncreasingSubsets.html#showincreasingsubsetsscene)

```
from manim import *

class ShowIncreasingSubsetsScene(Scene):
    def construct(self):
        p = VGroup(Dot(), Square(), Triangle())
        self.add(p)
        self.play(ShowIncreasingSubsets(p))
        self.wait()

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`interpolate_mobject`](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowIncreasingSubsets.html#manim.animation.creation.ShowIncreasingSubsets.interpolate_mobject "manim.animation.creation.ShowIncreasingSubsets.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |
| `update_submobject_list` |  |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

Parameters:

- **group** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **suspend\_mobject\_updating** ( _bool_)

- **int\_func** ( _Callable_ _\[_ _\[_ _np.ndarray_ _\]_ _,_ _np.ndarray_ _\]_)


\_original\_\_init\_\_( _group_, _suspend\_mobject\_updating=False_, _int\_func=<ufunc'floor'>_, _reverse\_rate\_function=False_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowIncreasingSubsets.html#manim.animation.creation.ShowIncreasingSubsets._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **group** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **suspend\_mobject\_updating** ( _bool_)

- **int\_func** ( _Callable_ _\[_ _\[_ _ndarray_ _\]_ _,_ _ndarray_ _\]_)


Return type:

None

interpolate\_mobject( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#ShowIncreasingSubsets.interpolate_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowIncreasingSubsets.html#manim.animation.creation.ShowIncreasingSubsets.interpolate_mobject "Link to this definition")

Interpolates the mobject of the `Animation` based on alpha value.

Parameters:

**alpha** ( _float_) – A float between 0 and 1 expressing the ratio to which the animation
is completed. For example, alpha-values of 0, 0.5, and 1 correspond
to the animation being completed 0%, 50%, and 100%, respectively.

Return type:

None