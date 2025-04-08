ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Integer [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html\#integer "Link to this heading")

Qualified name: `manim.mobject.text.numbers.Integer`

_class_ Integer( _number=0_, _num\_decimal\_places=0_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/numbers.html#Integer) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "Link to this definition")

Bases: [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber")

A class for displaying Integers.

Examples

Example: IntegerExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#integerexample)

![../_images/IntegerExample-1.png](https://docs.manim.community/en/stable/_images/IntegerExample-1.png)

```
from manim import *

class IntegerExample(Scene):
    def construct(self):
        self.add(Integer(number=2.5).set_color(ORANGE).scale(2.5).set_x(-0.5).set_y(0.8))
        self.add(Integer(number=3.14159, show_ellipsis=True).set_x(3).set_y(3.3).scale(3.14159))
        self.add(Integer(number=42).set_x(2.5).set_y(-2.3).set_color_by_gradient(BLUE, TEAL).scale(1.7))
        self.add(Integer(number=6.28).set_x(-1.5).set_y(-2).set_color(YELLOW).scale(1.4))

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `get_value` |  |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `font_size` | The font size of the tex mobject. |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

Parameters:

- **number** ( _float_)

- **num\_decimal\_places** ( _int_)

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _number=0_, _num\_decimal\_places=0_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **number** ( _float_)

- **num\_decimal\_places** ( _int_)

- **kwargs** ( _Any_)


Return type:

None