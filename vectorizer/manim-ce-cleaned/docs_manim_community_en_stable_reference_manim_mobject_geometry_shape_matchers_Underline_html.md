# Underline [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.Underline.html\#underline "Link to this heading")

Qualified name: `manim.mobject.geometry.shape\_matchers.Underline`

_class_ Underline( _mobject_, _buff=0.1_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/shape_matchers.html#Underline) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.Underline.html#manim.mobject.geometry.shape_matchers.Underline "Link to this definition")

Bases: [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")

Creates an underline.

Examples

Example: UnderLine [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.Underline.html#underline)

![../_images/UnderLine-1.png](https://docs.manim.community/en/stable/_images/UnderLine-1.png)

```
from manim import *

class UnderLine(Scene):
    def construct(self):
        man = Tex("Manim")  # Full Word
        ul = Underline(man)  # Underlining the word
        self.add(man, ul)

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

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **buff** ( _float_)

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _mobject_, _buff=0.1_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.Underline.html#manim.mobject.geometry.shape_matchers.Underline._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **buff** ( _float_)

- **kwargs** ( _Any_)


Return type:

None

[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/8270/019600f7-a737-7481-84a9-9dd32b80fc51/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8270/019600f7-a737-7481-84a9-9dd32b80fc51/)