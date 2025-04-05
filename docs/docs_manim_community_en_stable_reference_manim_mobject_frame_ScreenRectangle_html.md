ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.frame.ScreenRectangle.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.frame.ScreenRectangle.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ScreenRectangle [¶](https://docs.manim.community/en/stable/reference/manim.mobject.frame.ScreenRectangle.html\#screenrectangle "Link to this heading")

Qualified name: `manim.mobject.frame.ScreenRectangle`

_class_ ScreenRectangle( _aspect\_ratio=1.7777777777777777_, _height=4_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/frame.html#ScreenRectangle) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.frame.ScreenRectangle.html#manim.mobject.frame.ScreenRectangle "Link to this definition")

Bases: [`Rectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle")

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| [`aspect_ratio`](https://docs.manim.community/en/stable/reference/manim.mobject.frame.ScreenRectangle.html#manim.mobject.frame.ScreenRectangle.aspect_ratio "manim.mobject.frame.ScreenRectangle.aspect_ratio") | The aspect ratio. |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

\_original\_\_init\_\_( _aspect\_ratio=1.7777777777777777_, _height=4_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.frame.ScreenRectangle.html#manim.mobject.frame.ScreenRectangle._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

_property_ aspect\_ratio [¶](https://docs.manim.community/en/stable/reference/manim.mobject.frame.ScreenRectangle.html#manim.mobject.frame.ScreenRectangle.aspect_ratio "Link to this definition")

The aspect ratio.

When set, the width is stretched to accommodate
the new aspect ratio.