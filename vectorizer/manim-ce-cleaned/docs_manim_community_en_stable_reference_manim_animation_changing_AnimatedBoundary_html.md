# AnimatedBoundary [¶](https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html\#animatedboundary "Link to this heading")

Qualified name: `manim.animation.changing.AnimatedBoundary`

_class_ AnimatedBoundary( _vmobject,colors=\[ManimColor('#29ABCA'),ManimColor('#9CDCEB'),ManimColor('#236B8E'),ManimColor('#736357')\],max\_stroke\_width=3,cycle\_rate=0.5,back\_and\_forth=True,draw\_rate\_func=<functionsmooth>,fade\_rate\_func=<functionsmooth>,\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/changing.html#AnimatedBoundary) [¶](https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html#manim.animation.changing.AnimatedBoundary "Link to this definition")

Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Boundary of a [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") with animated color change.

Examples

Example: AnimatedBoundaryExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html#animatedboundaryexample)

```
from manim import *

class AnimatedBoundaryExample(Scene):
    def construct(self):
        text = Text("So shiny!")
        boundary = AnimatedBoundary(text, colors=[RED, GREEN, BLUE],
                                    cycle_rate=3)
        self.add(text, boundary)
        self.wait(2)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `full_family_become_partial` |  |
| `update_boundary_copies` |  |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

\_original\_\_init\_\_( _vmobject,colors=\[ManimColor('#29ABCA'),ManimColor('#9CDCEB'),ManimColor('#236B8E'),ManimColor('#736357')\],max\_stroke\_width=3,cycle\_rate=0.5,back\_and\_forth=True,draw\_rate\_func=<functionsmooth>,fade\_rate\_func=<functionsmooth>,\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.changing.AnimatedBoundary.html#manim.animation.changing.AnimatedBoundary._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

[**Document Extraction for Developers** Transform docs into structured data with Sensible. **Try for free →**](https://server.ethicalads.io/proxy/click/8517/019600e4-87f1-7e42-9827-6a4e4e5dc94d/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8517/019600e4-87f1-7e42-9827-6a4e4e5dc94d/)