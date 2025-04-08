# StealthTip [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html\#stealthtip "Link to this heading")

Qualified name: `manim.mobject.geometry.tips.StealthTip`

_class_ StealthTip( _fill\_opacity=1_, _stroke\_width=3_, _length=0.175_, _start\_angle=3.141592653589793_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/tips.html#StealthTip) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html#manim.mobject.geometry.tips.StealthTip "Link to this definition")

Bases: [`ArrowTip`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip "manim.mobject.geometry.tips.ArrowTip")

‘Stealth’ fighter / kite arrow shape.

Naming is inspired by the corresponding
[TikZ arrow shape](https://tikz.dev/tikz-arrows#sec-16.3).

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `base` | The base point of the arrow tip. |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| [`length`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html#manim.mobject.geometry.tips.StealthTip.length "manim.mobject.geometry.tips.StealthTip.length") | The length of the arrow tip. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `tip_angle` | The angle of the arrow tip. |
| `tip_point` | The tip point of the arrow tip. |
| `vector` | The vector pointing from the base point to the tip point. |
| `width` | The width of the mobject. |

Parameters:

- **fill\_opacity** ( _float_)

- **stroke\_width** ( _float_)

- **length** ( _float_)

- **start\_angle** ( _float_)

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _fill\_opacity=1_, _stroke\_width=3_, _length=0.175_, _start\_angle=3.141592653589793_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html#manim.mobject.geometry.tips.StealthTip._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **fill\_opacity** ( _float_)

- **stroke\_width** ( _float_)

- **length** ( _float_)

- **start\_angle** ( _float_)

- **kwargs** ( _Any_)


_property_ length _:float_ [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.tips.StealthTip.html#manim.mobject.geometry.tips.StealthTip.length "Link to this definition")

The length of the arrow tip.

In this case, the length is computed as the height of
the triangle encompassing the stealth tip (otherwise,
the tip is scaled too large).