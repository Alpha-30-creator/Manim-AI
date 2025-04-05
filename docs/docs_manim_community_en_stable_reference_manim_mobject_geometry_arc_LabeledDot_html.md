ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.LabeledDot.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.LabeledDot.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# LabeledDot [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.LabeledDot.html\#labeleddot "Link to this heading")

Qualified name: `manim.mobject.geometry.arc.LabeledDot`

_class_ LabeledDot( _label_, _radius=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#LabeledDot) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.LabeledDot.html#manim.mobject.geometry.arc.LabeledDot "Link to this definition")

Bases: [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot "manim.mobject.geometry.arc.Dot")

A [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot "manim.mobject.geometry.arc.Dot") containing a label in its center.

Parameters:

- **label** ( _str_ _\|_ [_SingleStringMathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex "manim.mobject.text.tex_mobject.SingleStringMathTex") _\|_ [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") _\|_ [_Tex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")) – The label of the [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot "manim.mobject.geometry.arc.Dot"). This is rendered as [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")
by default (i.e., when passing a `str`), but other classes
representing rendered strings like [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")
can be passed as well.

- **radius** ( _float_ _\|_ _None_) – The radius of the [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot "manim.mobject.geometry.arc.Dot"). If `None` (the default), the radius
is calculated based on the size of the `label`.

- **kwargs** ( _Any_)


Examples

Example: SeveralLabeledDots [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.LabeledDot.html#severallabeleddots)

![../_images/SeveralLabeledDots-1.png](https://docs.manim.community/en/stable/_images/SeveralLabeledDots-1.png)

```
from manim import *

class SeveralLabeledDots(Scene):
    def construct(self):
        sq = Square(fill_color=RED, fill_opacity=1)
        self.add(sq)
        dot1 = LabeledDot(Tex("42", color=RED))
        dot2 = LabeledDot(MathTex("a", color=GREEN))
        dot3 = LabeledDot(Text("ii", color=BLUE))
        dot4 = LabeledDot("3")
        dot1.next_to(sq, UL)
        dot2.next_to(sq, UR)
        dot3.next_to(sq, DL)
        dot4.next_to(sq, DR)
        self.add(dot1, dot2, dot3, dot4)

```

Copy to clipboard

Make interactive

Methods

|
|

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

\_original\_\_init\_\_( _label_, _radius=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.LabeledDot.html#manim.mobject.geometry.arc.LabeledDot._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **label** ( _str_ _\|_ [_SingleStringMathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex "manim.mobject.text.tex_mobject.SingleStringMathTex") _\|_ [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") _\|_ [_Tex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex"))

- **radius** ( _float_ _\|_ _None_)

- **kwargs** ( _Any_)


Return type:

None