ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# SingleStringMathTex [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html\#singlestringmathtex "Link to this heading")

Qualified name: `manim.mobject.text.tex\_mobject.SingleStringMathTex`

_class_ SingleStringMathTex( _tex\_string_, _stroke\_width=0_, _should\_center=True_, _height=None_, _organize\_left\_to\_right=False_, _tex\_environment='align\*'_, _tex\_template=None_, _font\_size=48_, _color=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html#SingleStringMathTex) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex "Link to this definition")

Bases: [`SVGMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject "manim.mobject.svg.svg_mobject.SVGMobject")

Elementary building block for rendering text with LaTeX.

Tests

Check that creating a [`SingleStringMathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex "manim.mobject.text.tex_mobject.SingleStringMathTex") object works:

```
>>> SingleStringMathTex('Test')
SingleStringMathTex('Test')

```

Copy to clipboard

Methods

|     |     |
| --- | --- |
| `get_tex_string` |  |
| [`init_colors`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors "manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors") | Initializes the colors. |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| [`font_size`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex.font_size "manim.mobject.text.tex_mobject.SingleStringMathTex.font_size") | The font size of the tex mobject. |
| `hash_seed` | A unique hash representing the result of the generated mobject points. |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

Parameters:

- **tex\_string** ( _str_)

- **stroke\_width** ( _float_)

- **should\_center** ( _bool_)

- **height** ( _float_ _\|_ _None_)

- **organize\_left\_to\_right** ( _bool_)

- **tex\_environment** ( _str_)

- **tex\_template** ( [_TexTemplate_](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate "manim.utils.tex.TexTemplate") _\|_ _None_)

- **font\_size** ( _float_)

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_)


\_original\_\_init\_\_( _tex\_string_, _stroke\_width=0_, _should\_center=True_, _height=None_, _organize\_left\_to\_right=False_, _tex\_environment='align\*'_, _tex\_template=None_, _font\_size=48_, _color=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **tex\_string** ( _str_)

- **stroke\_width** ( _float_)

- **should\_center** ( _bool_)

- **height** ( _float_ _\|_ _None_)

- **organize\_left\_to\_right** ( _bool_)

- **tex\_environment** ( _str_)

- **tex\_template** ( [_TexTemplate_](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate "manim.utils.tex.TexTemplate") _\|_ _None_)

- **font\_size** ( _float_)

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_)


\_remove\_stray\_braces( _tex_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html#SingleStringMathTex._remove_stray_braces) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex._remove_stray_braces "Link to this definition")

Makes [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") resilient to unmatched braces.

This is important when the braces in the TeX code are spread over
multiple arguments as in, e.g., `MathTex(r"e^{i", r"\tau} = 1")`.

_property_ font\_size [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex.font_size "Link to this definition")

The font size of the tex mobject.

init\_colors( _propagate\_colors=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html#SingleStringMathTex.init_colors) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors "Link to this definition")

Initializes the colors.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.