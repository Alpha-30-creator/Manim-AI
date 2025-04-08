# Group [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html\#group "Link to this heading")

Qualified name: `manim.mobject.mobject.Group`

_class_ Group( _\*mobjects_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Group) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "Link to this definition")

Bases: [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Groups together multiple [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Notes

When adding the same mobject more than once, repetitions are ignored.
Use [`Mobject.copy()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.copy "manim.mobject.mobject.Mobject.copy") to create a separate copy which can then
be added to the group.

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `depth` | The depth of the mobject. |
| `height` | The height of the mobject. |
| `width` | The width of the mobject. |

\_original\_\_init\_\_( _\*mobjects_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html#manim.mobject.mobject.Group._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Return type:

None