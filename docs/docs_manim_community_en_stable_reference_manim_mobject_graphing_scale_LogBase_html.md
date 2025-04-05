ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LogBase.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LogBase.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# LogBase [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LogBase.html\#logbase "Link to this heading")

Qualified name: `manim.mobject.graphing.scale.LogBase`

_class_ LogBase( _base=10_, _custom\_labels=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/scale.html#LogBase) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LogBase.html#manim.mobject.graphing.scale.LogBase "Link to this definition")

Bases: `_ScaleBase`

Scale for logarithmic graphs/functions.

Parameters:

- **base** ( _float_) – The base of the log, by default 10.

- **custom\_labels** ( _bool_) – For use with [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes"):
Whether or not to include `LaTeX` axis labels, by default True.


Examples

```
func = ParametricFunction(lambda x: x, scaling=LogBase(base=2))

```

Copy to clipboard

Methods

|     |     |
| --- | --- |
| [`function`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LogBase.html#manim.mobject.graphing.scale.LogBase.function "manim.mobject.graphing.scale.LogBase.function") | Scales the value to fit it to a logarithmic scale.\`\`self.function(5)==10\*\*5\`\` |
| [`get_custom_labels`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LogBase.html#manim.mobject.graphing.scale.LogBase.get_custom_labels "manim.mobject.graphing.scale.LogBase.get_custom_labels") | Produces custom [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer") labels in the form of `10^2`. |
| [`inverse_function`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LogBase.html#manim.mobject.graphing.scale.LogBase.inverse_function "manim.mobject.graphing.scale.LogBase.inverse_function") | Inverse of `function`. |

function( _value_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/scale.html#LogBase.function) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LogBase.html#manim.mobject.graphing.scale.LogBase.function "Link to this definition")

Scales the value to fit it to a logarithmic scale.\`\`self.function(5)==10\*\*5\`\`

Parameters:

**value** ( _float_)

Return type:

float

get\_custom\_labels( _val\_range_, _unit\_decimal\_places=0_, _\*\*base\_config_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/scale.html#LogBase.get_custom_labels) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LogBase.html#manim.mobject.graphing.scale.LogBase.get_custom_labels "Link to this definition")

Produces custom [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer") labels in the form of `10^2`.

Parameters:

- **val\_range** ( _Iterable_ _\[_ _float_ _\]_) – The iterable of values used to create the labels. Determines the exponent.

- **unit\_decimal\_places** ( _int_) – The number of decimal places to include in the exponent

- **base\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_) – Additional arguments to be passed to [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").


Return type:

list\[ [Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")\]

inverse\_function( _value_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/scale.html#LogBase.inverse_function) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.scale.LogBase.html#manim.mobject.graphing.scale.LogBase.inverse_function "Link to this definition")

Inverse of `function`. The value must be greater than 0

Parameters:

**value** ( _float_)

Return type:

float

[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/8271/019600e6-c73e-7662-8631-ce054850e143/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8271/019600e6-c73e-7662-8631-ce054850e143/)