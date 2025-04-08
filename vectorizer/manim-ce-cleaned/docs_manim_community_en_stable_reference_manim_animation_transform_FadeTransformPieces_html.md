# FadeTransformPieces [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransformPieces.html\#fadetransformpieces "Link to this heading")

Qualified name: `manim.animation.transform.FadeTransformPieces`

_class_ FadeTransformPieces( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#FadeTransformPieces) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransformPieces.html#manim.animation.transform.FadeTransformPieces "Link to this definition")

Bases: [`FadeTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform "manim.animation.transform.FadeTransform")

Fades submobjects of one mobject into submobjects of another one.

See also

[`FadeTransform`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform "manim.animation.transform.FadeTransform")

Examples

Example: FadeTransformSubmobjects [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransformPieces.html#fadetransformsubmobjects)

```
from manim import *

class FadeTransformSubmobjects(Scene):
    def construct(self):
        src = VGroup(Square(), Circle().shift(LEFT + UP))
        src.shift(3*LEFT + 2*UP)
        src_copy = src.copy().shift(4*DOWN)

        target = VGroup(Circle(), Triangle().shift(RIGHT + DOWN))
        target.shift(3*RIGHT + 2*UP)
        target_copy = target.copy().shift(4*DOWN)

        self.play(FadeIn(src), FadeIn(src_copy))
        self.play(
            FadeTransform(src, target),
            FadeTransformPieces(src_copy, target_copy)
        )
        self.play(*[FadeOut(mobj) for mobj in self.mobjects])

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`begin`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransformPieces.html#manim.animation.transform.FadeTransformPieces.begin "manim.animation.transform.FadeTransformPieces.begin") | Initial setup for the animation. |
| [`ghost_to`](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransformPieces.html#manim.animation.transform.FadeTransformPieces.ghost_to "manim.animation.transform.FadeTransformPieces.ghost_to") | Replaces the source submobjects by the target submobjects and sets the opacity to 0. |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

\_original\_\_init\_\_( _mobject_, _target\_mobject_, _stretch=True_, _dim\_to\_match=1_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransformPieces.html#manim.animation.transform.FadeTransformPieces._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

begin() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#FadeTransformPieces.begin) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransformPieces.html#manim.animation.transform.FadeTransformPieces.begin "Link to this definition")

Initial setup for the animation.

The mobject to which this animation is bound is a group consisting of
both the starting and the ending mobject. At the start, the ending
mobject replaces the starting mobject (and is completely faded). In the
end, it is set to be the other way around.

ghost\_to( _source_, _target_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#FadeTransformPieces.ghost_to) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.FadeTransformPieces.html#manim.animation.transform.FadeTransformPieces.ghost_to "Link to this definition")

Replaces the source submobjects by the target submobjects and sets
the opacity to 0.