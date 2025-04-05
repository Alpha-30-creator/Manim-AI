ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.constants.LineJointType.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.constants.LineJointType.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# LineJointType [¶](https://docs.manim.community/en/stable/reference/manim.constants.LineJointType.html\#linejointtype "Link to this heading")

Qualified name: `manim.constants.LineJointType`

_class_ LineJointType( _value_, _names=<notgiven>_, _\*values_, _module=None_, _qualname=None_, _type=None_, _start=1_, _boundary=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/constants.html#LineJointType) [¶](https://docs.manim.community/en/stable/reference/manim.constants.LineJointType.html#manim.constants.LineJointType "Link to this definition")

Bases: `Enum`

Collection of available line joint types.

See the example below for a visual illustration of the different
joint types.

Examples

Example: LineJointVariants [¶](https://docs.manim.community/en/stable/reference/manim.constants.LineJointType.html#linejointvariants)

![../_images/LineJointVariants-1.png](https://docs.manim.community/en/stable/_images/LineJointVariants-1.png)

```
from manim import *

class LineJointVariants(Scene):
    def construct(self):
        mob = VMobject(stroke_width=20, color=GREEN).set_points_as_corners([\
            np.array([-2, 0, 0]),\
            np.array([0, 0, 0]),\
            np.array([-2, 1, 0]),\
        ])
        lines = VGroup(*[mob.copy() for _ in range(len(LineJointType))])
        for line, joint_type in zip(lines, LineJointType):
            line.joint_type = joint_type

        lines.arrange(RIGHT, buff=1)
        self.add(lines)
        for line in lines:
            label = Text(line.joint_type.name).next_to(line, DOWN)
            self.add(label)

```

Copy to clipboard

Make interactive

Attributes

|     |     |
| --- | --- |
| `AUTO` |  |
| `ROUND` |  |
| `BEVEL` |  |
| `MITER` |  |

[**The AI Agent that gets your codebase** Copilot & Cursor letting you down? Try Augment. **Install Now**](https://server.ethicalads.io/proxy/click/8458/019600f7-58c6-7fd3-9136-8c3d88bf2854/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8458/019600f7-58c6-7fd3-9136-8c3d88bf2854/)