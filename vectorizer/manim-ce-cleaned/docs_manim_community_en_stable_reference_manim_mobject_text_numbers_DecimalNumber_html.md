# DecimalNumber [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html\#decimalnumber "Link to this heading")

Qualified name: `manim.mobject.text.numbers.DecimalNumber`

_class_ DecimalNumber( _number=0_, _num\_decimal\_places=2_, _mob\_class=<class'manim.mobject.text.tex\_mobject.MathTex'>_, _include\_sign=False_, _group\_with\_commas=True_, _digit\_buff\_per\_font\_unit=0.001_, _show\_ellipsis=False_, _unit=None_, _unit\_buff\_per\_font\_unit=0_, _include\_background\_rectangle=False_, _edge\_to\_fix=array(\[-1._, _0._, _0.\])_, _font\_size=48_, _stroke\_width=0_, _fill\_opacity=1.0_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/numbers.html#DecimalNumber) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

An mobject representing a decimal number.

Parameters:

- **number** ( _float_) – The numeric value to be displayed. It can later be modified using [`set_value()`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber.set_value "manim.mobject.text.numbers.DecimalNumber.set_value").

- **num\_decimal\_places** ( _int_) – The number of decimal places after the decimal separator. Values are automatically rounded.

- **mob\_class** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The class for rendering digits and units, by default [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").

- **include\_sign** ( _bool_) – Set to `True` to include a sign for positive numbers and zero.

- **group\_with\_commas** ( _bool_) – When `True` thousands groups are separated by commas for readability.

- **digit\_buff\_per\_font\_unit** ( _float_) – Additional spacing between digits. Scales with font size.

- **show\_ellipsis** ( _bool_) – When a number has been truncated by rounding, indicate with an ellipsis ( `...`).

- **unit** ( _str_ _\|_ _None_) – A unit string which can be placed to the right of the numerical values.

- **unit\_buff\_per\_font\_unit** ( _float_) – An additional spacing between the numerical values and the unit. A value
of `unit_buff_per_font_unit=0.003` gives a decent spacing. Scales with font size.

- **include\_background\_rectangle** ( _bool_) – Adds a background rectangle to increase contrast on busy scenes.

- **edge\_to\_fix** ( _Sequence_ _\[_ _float_ _\]_) – Assuring right- or left-alignment of the full object.

- **font\_size** ( _float_) – Size of the font.

- **stroke\_width** ( _float_)

- **fill\_opacity** ( _float_)


Examples

Example: MovingSquareWithUpdaters [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#movingsquarewithupdaters)

```
from manim import *

class MovingSquareWithUpdaters(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
            unit=r"\text{M-Units}",
            unit_buff_per_font_unit=0.003
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.animate.to_edge(DOWN),
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `get_value` |  |
| `increment_value` |  |
| [`set_value`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber.set_value "manim.mobject.text.numbers.DecimalNumber.set_value") | Set the value of the [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") to a new number. |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| [`font_size`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber.font_size "manim.mobject.text.numbers.DecimalNumber.font_size") | The font size of the tex mobject. |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

\_get\_formatter( _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/numbers.html#DecimalNumber._get_formatter) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber._get_formatter "Link to this definition")

Configuration is based first off instance attributes,
but overwritten by any kew word argument. Relevant
key words:
\- include\_sign
\- group\_with\_commas
\- num\_decimal\_places
\- field\_name (e.g. 0 or 0.real)

\_original\_\_init\_\_( _number=0_, _num\_decimal\_places=2_, _mob\_class=<class'manim.mobject.text.tex\_mobject.MathTex'>_, _include\_sign=False_, _group\_with\_commas=True_, _digit\_buff\_per\_font\_unit=0.001_, _show\_ellipsis=False_, _unit=None_, _unit\_buff\_per\_font\_unit=0_, _include\_background\_rectangle=False_, _edge\_to\_fix=array(\[-1._, _0._, _0.\])_, _font\_size=48_, _stroke\_width=0_, _fill\_opacity=1.0_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **number** ( _float_)

- **num\_decimal\_places** ( _int_)

- **mob\_class** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

- **include\_sign** ( _bool_)

- **group\_with\_commas** ( _bool_)

- **digit\_buff\_per\_font\_unit** ( _float_)

- **show\_ellipsis** ( _bool_)

- **unit** ( _str_ _\|_ _None_)

- **unit\_buff\_per\_font\_unit** ( _float_)

- **include\_background\_rectangle** ( _bool_)

- **edge\_to\_fix** ( _Sequence_ _\[_ _float_ _\]_)

- **font\_size** ( _float_)

- **stroke\_width** ( _float_)

- **fill\_opacity** ( _float_)


_property_ font\_size [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber.font_size "Link to this definition")

The font size of the tex mobject.

set\_value( _number_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/numbers.html#DecimalNumber.set_value) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber.set_value "Link to this definition")

Set the value of the [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") to a new number.

Parameters:

**number** ( _float_) – The value that will overwrite the current number of the [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber").