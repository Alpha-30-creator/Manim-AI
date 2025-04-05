ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# DrawBorderThenFill [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html\#drawborderthenfill "Link to this heading")

Qualified name: `manim.animation.creation.DrawBorderThenFill`

_class_ DrawBorderThenFill( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#DrawBorderThenFill) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html#manim.animation.creation.DrawBorderThenFill "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

Draw the border first and then show the fill.

Examples

Example: ShowDrawBorderThenFill [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html#showdrawborderthenfill)

```
from manim import *

class ShowDrawBorderThenFill(Scene):
    def construct(self):
        self.play(DrawBorderThenFill(Square(fill_opacity=1, fill_color=ORANGE)))

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`begin`](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html#manim.animation.creation.DrawBorderThenFill.begin "manim.animation.creation.DrawBorderThenFill.begin") | Begin the animation. |
| [`get_all_mobjects`](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html#manim.animation.creation.DrawBorderThenFill.get_all_mobjects "manim.animation.creation.DrawBorderThenFill.get_all_mobjects") | Get all mobjects involved in the animation. |
| `get_outline` |  |
| `get_stroke_color` |  |
| `interpolate_submobject` |  |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

Parameters:

- **vmobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ _OpenGLVMobject_)

- **run\_time** ( _float_)

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)

- **stroke\_width** ( _float_)

- **stroke\_color** ( _str_)

- **draw\_border\_animation\_config** ( _dict_)

- **fill\_animation\_config** ( _dict_)

- **introducer** ( _bool_)


\_original\_\_init\_\_( _vmobject_, _run\_time=2_, _rate\_func=<functiondouble\_smooth>_, _stroke\_width=2_, _stroke\_color=None_, _draw\_border\_animation\_config={}_, _fill\_animation\_config={}_, _introducer=True_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html#manim.animation.creation.DrawBorderThenFill._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **vmobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ _OpenGLVMobject_)

- **run\_time** ( _float_)

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)

- **stroke\_width** ( _float_)

- **stroke\_color** ( _str_)

- **draw\_border\_animation\_config** ( _dict_)

- **fill\_animation\_config** ( _dict_)

- **introducer** ( _bool_)


Return type:

None

begin() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#DrawBorderThenFill.begin) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html#manim.animation.creation.DrawBorderThenFill.begin "Link to this definition")

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

Return type:

None

get\_all\_mobjects() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#DrawBorderThenFill.get_all_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html#manim.animation.creation.DrawBorderThenFill.get_all_mobjects "Link to this definition")

Get all mobjects involved in the animation.

Ordering must match the ordering of arguments to interpolate\_submobject

Returns:

The sequence of mobjects.

Return type:

Sequence\[ [Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")\]