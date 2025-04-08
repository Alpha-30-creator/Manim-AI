ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowArrow.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowArrow.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# GrowArrow [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowArrow.html\#growarrow "Link to this heading")

Qualified name: `manim.animation.growing.GrowArrow`

_class_ GrowArrow( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/growing.html#GrowArrow) [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowArrow.html#manim.animation.growing.GrowArrow "Link to this definition")

Bases: [`GrowFromPoint`](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowFromPoint.html#manim.animation.growing.GrowFromPoint "manim.animation.growing.GrowFromPoint")

Introduce an [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow") by growing it from its start toward its tip.

Parameters:

- **arrow** ( [_Arrow_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")) – The arrow to be introduced.

- **point\_color** ( _str_) – Initial color of the arrow before growing to its full size. Leave empty to match arrow’s color.


Examples

Example: GrowArrowExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowArrow.html#growarrowexample)

```
from manim import *

class GrowArrowExample(Scene):
    def construct(self):
        arrows = [Arrow(2 * LEFT, 2 * RIGHT), Arrow(2 * DR, 2 * UL)]
        VGroup(*arrows).set_x(0).arrange(buff=2)
        self.play(GrowArrow(arrows[0]))
        self.play(GrowArrow(arrows[1], point_color=RED))

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `create_starting_mobject` |  |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

\_original\_\_init\_\_( _arrow_, _point\_color=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.growing.GrowArrow.html#manim.animation.growing.GrowArrow._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **arrow** ( [_Arrow_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow"))

- **point\_color** ( _str_)


Return type:

None