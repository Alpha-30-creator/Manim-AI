ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Title.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Title.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Title [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Title.html\#title "Link to this heading")

Qualified name: `manim.mobject.text.tex\_mobject.Title`

_class_ Title( _\*text\_parts_, _include\_underline=True_, _match\_underline\_width\_to\_text=False_, _underline\_buff=0.25_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html#Title) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Title.html#manim.mobject.text.tex_mobject.Title "Link to this definition")

Bases: [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")

A mobject representing an underlined title.

Examples

Example: TitleExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Title.html#titleexample)

![../_images/TitleExample-1.png](https://docs.manim.community/en/stable/_images/TitleExample-1.png)

```
from manim import *

import manim

class TitleExample(Scene):
    def construct(self):
        banner = ManimBanner()
        title = Title(f"Manim version {manim.__version__}")
        self.add(banner, title)

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
| `font_size` | The font size of the tex mobject. |
| `hash_seed` | A unique hash representing the result of the generated mobject points. |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

\_original\_\_init\_\_( _\*text\_parts_, _include\_underline=True_, _match\_underline\_width\_to\_text=False_, _underline\_buff=0.25_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Title.html#manim.mobject.text.tex_mobject.Title._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.