ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# TransformMatchingTex [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html\#transformmatchingtex "Link to this heading")

Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingTex`

_class_ TransformMatchingTex( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform_matching_parts.html#TransformMatchingTex) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html#manim.animation.transform_matching_parts.TransformMatchingTex "Link to this definition")

Bases: [`TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")

A transformation trying to transform rendered LaTeX strings.

Two submobjects match if their `tex_string` matches.

See also

[`TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")

Examples

Example: MatchingEquationParts [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html#matchingequationparts)

```
from manim import *

class MatchingEquationParts(Scene):
    def construct(self):
        variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

        eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

        self.add(eq1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(0.5)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `get_mobject_key` |  |
| `get_mobject_parts` |  |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **target\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **transform\_mismatches** ( _bool_)

- **fade\_transform\_mismatches** ( _bool_)

- **key\_map** ( _dict_ _\|_ _None_)


\_original\_\_init\_\_( _mobject_, _target\_mobject_, _transform\_mismatches=False_, _fade\_transform\_mismatches=False_, _key\_map=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html#manim.animation.transform_matching_parts.TransformMatchingTex._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **target\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **transform\_mismatches** ( _bool_)

- **fade\_transform\_mismatches** ( _bool_)

- **key\_map** ( _dict_ _\|_ _None_)


[**Document Extraction for Developers** Transform docs into structured data with Sensible. **Try for free →**](https://server.ethicalads.io/proxy/click/8517/019600ee-2333-7403-9796-c0cecdf3492b/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8517/019600ee-2333-7403-9796-c0cecdf3492b/)