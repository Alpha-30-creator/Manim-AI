ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.Label.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.Label.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Label [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.Label.html\#label "Link to this heading")

Qualified name: `manim.mobject.geometry.labeled.Label`

_class_ Label( _label_, _label\_config=None_, _box\_config=None_, _frame\_config=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/labeled.html#Label) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.Label.html#manim.mobject.geometry.labeled.Label "Link to this definition")

Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

A Label consisting of text surrounded by a frame.

Parameters:

- **label** ( _str_ _\|_ [_Tex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") _\|_ [_MathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") _\|_ [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")) – Label that will be displayed.

- **label\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_) – A dictionary containing the configuration for the label.
This is only applied if `label` is of type `str`.

- **box\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_) – A dictionary containing the configuration for the background box.

- **frame\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_) – A dictionary containing the configuration for the frame.

- **kwargs** ( _Any_)


Examples

Example: LabelExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.Label.html#labelexample)

![../_images/LabelExample-1.png](https://docs.manim.community/en/stable/_images/LabelExample-1.png)

```
from manim import *

class LabelExample(Scene):
    def construct(self):
        label = Label(
            label=Text('Label Text', font='sans-serif'),
            box_config = {
                "color" : BLUE,
                "fill_opacity" : 0.75
            }
        )
        label.scale(3)
        self.add(label)

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

\_original\_\_init\_\_( _label_, _label\_config=None_, _box\_config=None_, _frame\_config=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.Label.html#manim.mobject.geometry.labeled.Label._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **label** ( _str_ _\|_ [_Tex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") _\|_ [_MathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") _\|_ [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))

- **label\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **box\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **frame\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **kwargs** ( _Any_)


Return type:

None

[Simplified data ingestion for developers **Get Algolia Crawler**](https://server.ethicalads.io/proxy/click/8327/019600ee-6172-7443-b8b0-ba007bbc6f0c/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/frontend-web/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8327/019600ee-6172-7443-b8b0-ba007bbc6f0c/)