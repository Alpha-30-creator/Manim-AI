ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Dot3D.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Dot3D.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Dot3D [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Dot3D.html\#dot3d "Link to this heading")

Qualified name: `manim.mobject.three\_d.three\_dimensions.Dot3D`

_class_ Dot3D( _point=array(\[0.,0.,0.\])_, _radius=0.08_, _color=ManimColor('#FFFFFF')_, _resolution=(8,8)_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Dot3D) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Dot3D.html#manim.mobject.three_d.three_dimensions.Dot3D "Link to this definition")

Bases: [`Sphere`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Sphere.html#manim.mobject.three_d.three_dimensions.Sphere "manim.mobject.three_d.three_dimensions.Sphere")

A spherical dot.

Parameters:

- **point** ( _list_ _\|_ _np.ndarray_) – The location of the dot.

- **radius** ( _float_) – The radius of the dot.

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the [`Dot3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Dot3D.html#manim.mobject.three_d.three_dimensions.Dot3D "manim.mobject.three_d.three_dimensions.Dot3D").

- **resolution** ( _tuple_ _\[_ _int_ _,_ _int_ _\]_) – The number of samples taken of the [`Dot3D`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Dot3D.html#manim.mobject.three_d.three_dimensions.Dot3D "manim.mobject.three_d.three_dimensions.Dot3D"). A tuple can be
used to define different resolutions for `u` and `v` respectively.


Examples

Example: Dot3DExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Dot3D.html#dot3dexample)

![../_images/Dot3DExample-1.png](https://docs.manim.community/en/stable/_images/Dot3DExample-1.png)

```
from manim import *

class Dot3DExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes()
        dot_1 = Dot3D(point=axes.coords_to_point(0, 0, 1), color=RED)
        dot_2 = Dot3D(point=axes.coords_to_point(2, 0, 0), radius=0.1, color=BLUE)
        dot_3 = Dot3D(point=[0, 0, 0], radius=0.1, color=ORANGE)
        self.add(axes, dot_1, dot_2,dot_3)

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

\_original\_\_init\_\_( _point=array(\[0.,0.,0.\])_, _radius=0.08_, _color=ManimColor('#FFFFFF')_, _resolution=(8,8)_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Dot3D.html#manim.mobject.three_d.three_dimensions.Dot3D._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **point** ( _list_ _\|_ _ndarray_)

- **radius** ( _float_)

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **resolution** ( _tuple_ _\[_ _int_ _,_ _int_ _\]_)


Return type:

None