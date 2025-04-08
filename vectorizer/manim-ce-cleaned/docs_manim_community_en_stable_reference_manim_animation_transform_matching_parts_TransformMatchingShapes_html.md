# TransformMatchingShapes [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html\#transformmatchingshapes "Link to this heading")

Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingShapes`

_class_ TransformMatchingShapes( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform_matching_parts.html#TransformMatchingShapes) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html#manim.animation.transform_matching_parts.TransformMatchingShapes "Link to this definition")

Bases: [`TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")

An animation trying to transform groups by matching the shape
of their submobjects.

Two submobjects match if the hash of their point coordinates after
normalization (i.e., after translation to the origin, fixing the submobject
height at 1 unit, and rounding the coordinates to three decimal places)
matches.

See also

[`TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")

Examples

Example: Anagram [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html#anagram)

```
from manim import *

class Anagram(Scene):
    def construct(self):
        src = Text("the morse code")
        tar = Text("here come dots")
        self.play(Write(src))
        self.wait(0.5)
        self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))
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


\_original\_\_init\_\_( _mobject_, _target\_mobject_, _transform\_mismatches=False_, _fade\_transform\_mismatches=False_, _key\_map=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html#manim.animation.transform_matching_parts.TransformMatchingShapes._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **target\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **transform\_mismatches** ( _bool_)

- **fade\_transform\_mismatches** ( _bool_)

- **key\_map** ( _dict_ _\|_ _None_)