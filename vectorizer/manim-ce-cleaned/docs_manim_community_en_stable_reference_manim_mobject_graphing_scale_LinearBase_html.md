# LinearBase [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LinearBase.html\#linearbase "Link to this heading")

Qualified name: `manim.mobject.graphing.scale.LinearBase`

_class_ LinearBase( _scale\_factor=1.0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/scale.html#LinearBase) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LinearBase.html#manim.mobject.graphing.scale.LinearBase "Link to this definition")

Bases: `_ScaleBase`

The default scaling class.

Parameters:

**scale\_factor** ( _float_) – The slope of the linear function, by default 1.0

Methods

|     |     |
| --- | --- |
| [`function`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LinearBase.html#manim.mobject.graphing.scale.LinearBase.function "manim.mobject.graphing.scale.LinearBase.function") | Multiplies the value by the scale factor. |
| [`inverse_function`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LinearBase.html#manim.mobject.graphing.scale.LinearBase.inverse_function "manim.mobject.graphing.scale.LinearBase.inverse_function") | Inverse of function. |

function( _value_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/scale.html#LinearBase.function) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LinearBase.html#manim.mobject.graphing.scale.LinearBase.function "Link to this definition")

Multiplies the value by the scale factor.

Parameters:

**value** ( _float_) – Value to be multiplied by the scale factor.

Return type:

float

inverse\_function( _value_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/scale.html#LinearBase.inverse_function) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LinearBase.html#manim.mobject.graphing.scale.LinearBase.inverse_function "Link to this definition")

Inverse of function. Divides the value by the scale factor.

Parameters:

**value** ( _float_) – value to be divided by the scale factor.

Return type:

float