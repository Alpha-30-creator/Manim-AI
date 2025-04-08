# Variable [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Variable.html\#variable "Link to this heading")

Qualified name: `manim.mobject.text.numbers.Variable`

_class_ Variable( _var_, _label_, _var\_type=<class'manim.mobject.text.numbers.DecimalNumber'>_, _num\_decimal\_places=2_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/numbers.html#Variable) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Variable.html#manim.mobject.text.numbers.Variable "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

A class for displaying text that shows “label = value” with
the value continuously updated from a [`ValueTracker`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html#manim.mobject.value_tracker.ValueTracker "manim.mobject.value_tracker.ValueTracker").

Parameters:

- **var** ( _float_) – The initial value you need to keep track of and display.

- **label** ( _str_ _\|_ [_Tex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") _\|_ [_MathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") _\|_ [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") _\|_ [_SingleStringMathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex "manim.mobject.text.tex_mobject.SingleStringMathTex")) – The label for your variable. Raw strings are convertex to [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") objects.

- **var\_type** ( [_DecimalNumber_](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") _\|_ [_Integer_](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer")) – The class used for displaying the number. Defaults to [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber").

- **num\_decimal\_places** ( _int_) – The number of decimal places to display in your variable. Defaults to 2.
If var\_type is an [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer"), this parameter is ignored.

- **kwargs** – Other arguments to be passed to ~.Mobject.


label [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Variable.html#manim.mobject.text.numbers.Variable.label "Link to this definition")

The label for your variable, for example `x = ...`.

Type:

Union\[ `str`, [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex"), [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex"), [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"), [`SingleStringMathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex "manim.mobject.text.tex_mobject.SingleStringMathTex")\]

tracker [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Variable.html#manim.mobject.text.numbers.Variable.tracker "Link to this definition")

Useful in updating the value of your variable on-screen.

Type:

[`ValueTracker`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html#manim.mobject.value_tracker.ValueTracker "manim.mobject.value_tracker.ValueTracker")

value [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Variable.html#manim.mobject.text.numbers.Variable.value "Link to this definition")

The tex for the value of your variable.

Type:

Union\[ [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber"), [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer")\]

Examples

Normal usage:

```
# DecimalNumber type
var = 0.5
on_screen_var = Variable(var, Text("var"), num_decimal_places=3)
# Integer type
int_var = 0
on_screen_int_var = Variable(int_var, Text("int_var"), var_type=Integer)
# Using math mode for the label
on_screen_int_var = Variable(int_var, "{a}_{i}", var_type=Integer)

```

Copy to clipboard

Example: VariablesWithValueTracker [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Variable.html#variableswithvaluetracker)

```
from manim import *

class VariablesWithValueTracker(Scene):
    def construct(self):
        var = 0.5
        on_screen_var = Variable(var, Text("var"), num_decimal_places=3)

        # You can also change the colours for the label and value
        on_screen_var.label.set_color(RED)
        on_screen_var.value.set_color(GREEN)

        self.play(Write(on_screen_var))
        # The above line will just display the variable with
        # its initial value on the screen. If you also wish to
        # update it, you can do so by accessing the `tracker` attribute
        self.wait()
        var_tracker = on_screen_var.tracker
        var = 10.5
        self.play(var_tracker.animate.set_value(var))
        self.wait()

        int_var = 0
        on_screen_int_var = Variable(
            int_var, Text("int_var"), var_type=Integer
        ).next_to(on_screen_var, DOWN)
        on_screen_int_var.label.set_color(RED)
        on_screen_int_var.value.set_color(GREEN)

        self.play(Write(on_screen_int_var))
        self.wait()
        var_tracker = on_screen_int_var.tracker
        var = 10.5
        self.play(var_tracker.animate.set_value(var))
        self.wait()

        # If you wish to have a somewhat more complicated label for your
        # variable with subscripts, superscripts, etc. the default class
        # for the label is MathTex
        subscript_label_var = 10
        on_screen_subscript_var = Variable(subscript_label_var, "{a}_{i}").next_to(
            on_screen_int_var, DOWN
        )
        self.play(Write(on_screen_subscript_var))
        self.wait()

```

Copy to clipboard

Make interactive

Example: VariableExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Variable.html#variableexample)

```
from manim import *

class VariableExample(Scene):
    def construct(self):
        start = 2.0

        x_var = Variable(start, 'x', num_decimal_places=3)
        sqr_var = Variable(start**2, 'x^2', num_decimal_places=3)
        Group(x_var, sqr_var).arrange(DOWN)

        sqr_var.add_updater(lambda v: v.tracker.set_value(x_var.tracker.get_value()**2))

        self.add(x_var, sqr_var)
        self.play(x_var.tracker.animate.set_value(5), run_time=2, rate_func=linear)
        self.wait(0.1)

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

\_original\_\_init\_\_( _var_, _label_, _var\_type=<class'manim.mobject.text.numbers.DecimalNumber'>_, _num\_decimal\_places=2_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Variable.html#manim.mobject.text.numbers.Variable._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **var** ( _float_)

- **label** ( _str_ _\|_ [_Tex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") _\|_ [_MathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") _\|_ [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") _\|_ [_SingleStringMathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex "manim.mobject.text.tex_mobject.SingleStringMathTex"))

- **var\_type** ( [_DecimalNumber_](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") _\|_ [_Integer_](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer"))

- **num\_decimal\_places** ( _int_)


[Develop and launch modern apps with MongoDB Atlas, a resilient data platform.](https://server.ethicalads.io/proxy/click/8269/019600f1-f310-76d3-a580-e6248ee84154/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8269/019600f1-f310-76d3-a580-e6248ee84154/)