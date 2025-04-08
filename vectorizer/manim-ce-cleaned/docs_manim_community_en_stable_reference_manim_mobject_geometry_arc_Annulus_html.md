# Annulus [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html\#annulus "Link to this heading")

Qualified name: `manim.mobject.geometry.arc.Annulus`

_class_ Annulus( _inner\_radius=1_, _outer\_radius=2_, _fill\_opacity=1_, _stroke\_width=0_, _color=ManimColor('#FFFFFF')_, _mark\_paths\_closed=False_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#Annulus) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html#manim.mobject.geometry.arc.Annulus "Link to this definition")

Bases: [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle")

Region between two concentric [`Circles`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle").

Parameters:

- **inner\_radius** ( _float_) – The radius of the inner [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle").

- **outer\_radius** ( _float_) – The radius of the outer [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle").

- **kwargs** ( _Any_) – Additional arguments to be passed to [`Annulus`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html#manim.mobject.geometry.arc.Annulus "manim.mobject.geometry.arc.Annulus")

- **fill\_opacity** ( _float_)

- **stroke\_width** ( _float_)

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **mark\_paths\_closed** ( _bool_)


Examples

Example: AnnulusExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html#annulusexample)

![../_images/AnnulusExample-1.png](https://docs.manim.community/en/stable/_images/AnnulusExample-1.png)

```
from manim import *

class AnnulusExample(Scene):
    def construct(self):
        annulus_1 = Annulus(inner_radius=0.5, outer_radius=1).shift(UP)
        annulus_2 = Annulus(inner_radius=0.3, outer_radius=0.6, color=RED).next_to(annulus_1, DOWN)
        self.add(annulus_1, annulus_2)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`generate_points`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html#manim.mobject.geometry.arc.Annulus.generate_points "manim.mobject.geometry.arc.Annulus.generate_points") | Initializes `points` and therefore the shape. |
| [`init_points`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html#manim.mobject.geometry.arc.Annulus.init_points "manim.mobject.geometry.arc.Annulus.init_points") | Initializes `points` and therefore the shape. |

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

\_original\_\_init\_\_( _inner\_radius=1_, _outer\_radius=2_, _fill\_opacity=1_, _stroke\_width=0_, _color=ManimColor('#FFFFFF')_, _mark\_paths\_closed=False_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html#manim.mobject.geometry.arc.Annulus._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **inner\_radius** ( _float_)

- **outer\_radius** ( _float_)

- **fill\_opacity** ( _float_)

- **stroke\_width** ( _float_)

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **mark\_paths\_closed** ( _bool_)

- **kwargs** ( _Any_)


Return type:

None

generate\_points() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/geometry/arc.html#Annulus.generate_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html#manim.mobject.geometry.arc.Annulus.generate_points "Link to this definition")

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

Return type:

None

init\_points() [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html#manim.mobject.geometry.arc.Annulus.init_points "Link to this definition")

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

Return type:

None