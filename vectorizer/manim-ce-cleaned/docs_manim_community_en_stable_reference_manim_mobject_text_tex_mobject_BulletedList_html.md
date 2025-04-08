# BulletedList [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.BulletedList.html\#bulletedlist "Link to this heading")

Qualified name: `manim.mobject.text.tex\_mobject.BulletedList`

_class_ BulletedList( _\*items_, _buff=0.5_, _dot\_scale\_factor=2_, _tex\_environment=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/tex_mobject.html#BulletedList) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.BulletedList.html#manim.mobject.text.tex_mobject.BulletedList "Link to this definition")

Bases: [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")

A bulleted list.

Examples

Example: BulletedListExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.BulletedList.html#bulletedlistexample)

![../_images/BulletedListExample-1.png](https://docs.manim.community/en/stable/_images/BulletedListExample-1.png)

```
from manim import *

class BulletedListExample(Scene):
    def construct(self):
        blist = BulletedList("Item 1", "Item 2", "Item 3", height=2, width=2)
        blist.set_color_by_tex("Item 1", RED)
        blist.set_color_by_tex("Item 2", GREEN)
        blist.set_color_by_tex("Item 3", BLUE)
        self.add(blist)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `fade_all_but` |  |

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

\_original\_\_init\_\_( _\*items_, _buff=0.5_, _dot\_scale\_factor=2_, _tex\_environment=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.BulletedList.html#manim.mobject.text.tex_mobject.BulletedList._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

[**The AI Agent that gets your codebase** Copilot & Cursor letting you down? Try Augment. **Install Now**](https://server.ethicalads.io/proxy/click/8458/019600e1-b31d-7593-9b8c-f13589958136/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/frontend-web/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8458/019600e1-b31d-7593-9b8c-f13589958136/)