# LabeledLine [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledLine.html\#labeledline "Link to this heading")

Qualified name: `manim.mobject.geometry.labeled.LabeledLine`

_class_ LabeledLine( _label_, _label\_position=0.5_, _label\_config=None_, _box\_config=None_, _frame\_config=None_, _\*args_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/labeled.html#LabeledLine) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledLine.html#manim.mobject.geometry.labeled.LabeledLine "Link to this definition")

Bases: [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")

Constructs a line containing a label box somewhere along its length.

Parameters:

- **label** ( _str_ _\|_ [_Tex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") _\|_ [_MathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") _\|_ [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")) – Label that will be displayed on the line.

- **label\_position** ( _float_) – A ratio in the range \[0-1\] to indicate the position of the label with respect to the length of the line. Default value is 0.5.

- **label\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_) – A dictionary containing the configuration for the label.
This is only applied if `label` is of type `str`.

- **box\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_) – A dictionary containing the configuration for the background box.

- **frame\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_) –

A dictionary containing the configuration for the frame.



See also



[`LabeledArrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledArrow.html#manim.mobject.geometry.labeled.LabeledArrow "manim.mobject.geometry.labeled.LabeledArrow")

- **args** ( _Any_)

- **kwargs** ( _Any_)


Examples

Example: LabeledLineExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledLine.html#labeledlineexample)

![../_images/LabeledLineExample-1.png](https://docs.manim.community/en/stable/_images/LabeledLineExample-1.png)

```
from manim import *

class LabeledLineExample(Scene):
    def construct(self):
        line = LabeledLine(
            label          = '0.5',
            label_position = 0.8,
            label_config = {
                "font_size" : 20
            },
            start=LEFT+DOWN,
            end=RIGHT+UP)

        line.set_length(line.get_length() * 2)
        self.add(line)

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

\_original\_\_init\_\_( _label_, _label\_position=0.5_, _label\_config=None_, _box\_config=None_, _frame\_config=None_, _\*args_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledLine.html#manim.mobject.geometry.labeled.LabeledLine._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **label** ( _str_ _\|_ [_Tex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") _\|_ [_MathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") _\|_ [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))

- **label\_position** ( _float_)

- **label\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **box\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **frame\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **args** ( _Any_)

- **kwargs** ( _Any_)


Return type:

None