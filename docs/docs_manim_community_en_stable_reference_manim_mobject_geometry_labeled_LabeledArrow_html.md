ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledArrow.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledArrow.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# LabeledArrow [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledArrow.html\#labeledarrow "Link to this heading")

Qualified name: `manim.mobject.geometry.labeled.LabeledArrow`

_class_ LabeledArrow( _\*args_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/labeled.html#LabeledArrow) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledArrow.html#manim.mobject.geometry.labeled.LabeledArrow "Link to this definition")

Bases: [`LabeledLine`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledLine.html#manim.mobject.geometry.labeled.LabeledLine "manim.mobject.geometry.labeled.LabeledLine"), [`Arrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")

Constructs an arrow containing a label box somewhere along its length.
This class inherits its label properties from LabeledLine, so the main parameters controlling it are the same.

Parameters:

- **label** – Label that will be displayed on the Arrow.

- **label\_position** – A ratio in the range \[0-1\] to indicate the position of the label with respect to the length of the line. Default value is 0.5.

- **label\_config** – A dictionary containing the configuration for the label.
This is only applied if `label` is of type `str`.

- **box\_config** – A dictionary containing the configuration for the background box.

- **frame\_config** –

A dictionary containing the configuration for the frame.



See also



[`LabeledLine`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledLine.html#manim.mobject.geometry.labeled.LabeledLine "manim.mobject.geometry.labeled.LabeledLine")

- **args** ( _Any_)

- **kwargs** ( _Any_)


Examples

Example: LabeledArrowExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledArrow.html#labeledarrowexample)

![../_images/LabeledArrowExample-1.png](https://docs.manim.community/en/stable/_images/LabeledArrowExample-1.png)

```
from manim import *

class LabeledArrowExample(Scene):
    def construct(self):
        l_arrow = LabeledArrow("0.5", start=LEFT*3, end=RIGHT*3 + UP*2, label_position=0.5)

        self.add(l_arrow)

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

\_original\_\_init\_\_( _\*args_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledArrow.html#manim.mobject.geometry.labeled.LabeledArrow._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **args** ( _Any_)

- **kwargs** ( _Any_)


Return type:

None