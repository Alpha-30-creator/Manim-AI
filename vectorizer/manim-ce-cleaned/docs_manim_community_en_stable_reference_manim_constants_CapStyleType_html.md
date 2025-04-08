# CapStyleType [¶](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html\#capstyletype "Link to this heading")

Qualified name: `manim.constants.CapStyleType`

_class_ CapStyleType( _value_, _names=<notgiven>_, _\*values_, _module=None_, _qualname=None_, _type=None_, _start=1_, _boundary=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/constants.html#CapStyleType) [¶](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html#manim.constants.CapStyleType "Link to this definition")

Bases: `Enum`

Collection of available cap styles.

See the example below for a visual illustration of the different
cap styles.

Examples

Example: CapStyleVariants [¶](https://docs.manim.community/en/stable/reference/manim.constants.CapStyleType.html#capstylevariants)

![../_images/CapStyleVariants-1.png](https://docs.manim.community/en/stable/_images/CapStyleVariants-1.png)

```
from manim import *

class CapStyleVariants(Scene):
    def construct(self):
        arcs = VGroup(*[\
            Arc(\
                radius=1,\
                start_angle=0,\
                angle=TAU / 4,\
                stroke_width=20,\
                color=GREEN,\
                cap_style=cap_style,\
            )\
            for cap_style in CapStyleType\
        ])
        arcs.arrange(RIGHT, buff=1)
        self.add(arcs)
        for arc in arcs:
            label = Text(arc.cap_style.name, font_size=24).next_to(arc, DOWN)
            self.add(label)

```

Copy to clipboard

Make interactive

Attributes

|     |     |
| --- | --- |
| `AUTO` |  |
| `ROUND` |  |
| `BUTT` |  |
| `SQUARE` |  |

[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/8270/019600f1-b82e-7f23-a14b-6db5b9223e77/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8270/019600f1-b82e-7f23-a14b-6db5b9223e77/)