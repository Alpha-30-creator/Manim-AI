# MathTex [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html\#mathtex "Link to this heading")

Qualified name: `manim.mobject.text.tex\_mobject.MathTex`

_class_ MathTex( _\*tex\_strings_, _arg\_separator=''_, _substrings\_to\_isolate=None_, _tex\_to\_color\_map=None_, _tex\_environment='align\*'_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html#MathTex) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "Link to this definition")

Bases: [`SingleStringMathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex "manim.mobject.text.tex_mobject.SingleStringMathTex")

A string compiled with LaTeX in math mode.

Examples

Example: Formula [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#formula)

![../_images/Formula-1.png](https://docs.manim.community/en/stable/_images/Formula-1.png)

```
from manim import *

class Formula(Scene):
    def construct(self):
        t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
        self.add(t)

```

Copy to clipboard

Make interactive

Tests

Check that creating a [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") works:

```
>>> MathTex('a^2 + b^2 = c^2')
MathTex('a^2 + b^2 = c^2')

```

Copy to clipboard

Check that double brace group splitting works correctly:

```
>>> t1 = MathTex('{{ a }} + {{ b }} = {{ c }}')
>>> len(t1.submobjects)
5
>>> t2 = MathTex(r"\frac{1}{a+b\sqrt{2}}")
>>> len(t2.submobjects)
1

```

Copy to clipboard

Methods

|     |     |
| --- | --- |
| `get_part_by_tex` |  |
| `get_parts_by_tex` |  |
| `index_of_part` |  |
| `index_of_part_by_tex` |  |
| `set_color_by_tex` |  |
| `set_color_by_tex_to_color_map` |  |
| [`set_opacity_by_tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex "manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex") | Sets the opacity of the tex specified. |
| `sort_alphabetically` |  |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `font_size` | The font size of the tex mobject. |
| `hash_seed` | A unique hash representing the result of the generated mobject points. |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

Parameters:

- **arg\_separator** ( _str_)

- **substrings\_to\_isolate** ( _Iterable_ _\[_ _str_ _\]_ _\|_ _None_)

- **tex\_to\_color\_map** ( _dict_ _\[_ _str_ _,_ [_ManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") _\]_)

- **tex\_environment** ( _str_)


\_break\_up\_by\_substrings() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html#MathTex._break_up_by_substrings) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex._break_up_by_substrings "Link to this definition")

Reorganize existing submobjects one layer
deeper based on the structure of tex\_strings (as a list
of tex\_strings)

\_original\_\_init\_\_( _\*tex\_strings_, _arg\_separator=''_, _substrings\_to\_isolate=None_, _tex\_to\_color\_map=None_, _tex\_environment='align\*'_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **arg\_separator** ( _str_)

- **substrings\_to\_isolate** ( _Iterable_ _\[_ _str_ _\]_ _\|_ _None_)

- **tex\_to\_color\_map** ( _dict_ _\[_ _str_ _,_ [_ManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") _\]_)

- **tex\_environment** ( _str_)


set\_opacity\_by\_tex( _tex_, _opacity=0.5_, _remaining\_opacity=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html#MathTex.set_opacity_by_tex) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex "Link to this definition")

Sets the opacity of the tex specified. If ‘remaining\_opacity’ is specified,
then the remaining tex will be set to that opacity.

Parameters:

- **tex** ( _str_) – The tex to set the opacity of.

- **opacity** ( _float_) – Default 0.5. The opacity to set the tex to

- **remaining\_opacity** ( _float_) – Default None. The opacity to set the remaining tex to.
If None, then the remaining tex will not be changed


[Simplified data ingestion for developers **Get Algolia Crawler**](https://server.ethicalads.io/proxy/click/8327/019600f1-f64e-79e2-84a6-23ad7a1ba869/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/frontend-web/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8327/019600f1-f64e-79e2-84a6-23ad7a1ba869/)