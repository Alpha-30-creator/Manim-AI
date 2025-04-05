ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Torus [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html\#torus "Link to this heading")

Qualified name: `manim.mobject.three\_d.three\_dimensions.Torus`

_class_ Torus( _major\_radius=3_, _minor\_radius=1_, _u\_range=(0,6.283185307179586)_, _v\_range=(0,6.283185307179586)_, _resolution=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Torus) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html#manim.mobject.three_d.three_dimensions.Torus "Link to this definition")

Bases: [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface")

A torus.

Parameters:

- **major\_radius** ( _float_) – Distance from the center of the tube to the center of the torus.

- **minor\_radius** ( _float_) – Radius of the tube.

- **u\_range** ( _Sequence_ _\[_ _float_ _\]_) – The range of the `u` variable: `(u_min, u_max)`.

- **v\_range** ( _Sequence_ _\[_ _float_ _\]_) – The range of the `v` variable: `(v_min, v_max)`.

- **resolution** ( _tuple_ _\[_ _int_ _,_ _int_ _\]_ _\|_ _None_) – The number of samples taken of the [`Torus`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html#manim.mobject.three_d.three_dimensions.Torus "manim.mobject.three_d.three_dimensions.Torus"). A tuple can be
used to define different resolutions for `u` and `v` respectively.


Examples

Example: ExampleTorus [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html#exampletorus)

![../_images/ExampleTorus-1.png](https://docs.manim.community/en/stable/_images/ExampleTorus-1.png)

```
from manim import *

class ExampleTorus(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        torus = Torus()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, torus)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`func`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html#manim.mobject.three_d.three_dimensions.Torus.func "manim.mobject.three_d.three_dimensions.Torus.func") | The z values defining the [`Torus`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html#manim.mobject.three_d.three_dimensions.Torus "manim.mobject.three_d.three_dimensions.Torus") being plotted. |

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

\_original\_\_init\_\_( _major\_radius=3_, _minor\_radius=1_, _u\_range=(0,6.283185307179586)_, _v\_range=(0,6.283185307179586)_, _resolution=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html#manim.mobject.three_d.three_dimensions.Torus._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **major\_radius** ( _float_)

- **minor\_radius** ( _float_)

- **u\_range** ( _Sequence_ _\[_ _float_ _\]_)

- **v\_range** ( _Sequence_ _\[_ _float_ _\]_)

- **resolution** ( _tuple_ _\[_ _int_ _,_ _int_ _\]_ _\|_ _None_)


Return type:

None

func( _u_, _v_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Torus.func) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html#manim.mobject.three_d.three_dimensions.Torus.func "Link to this definition")

The z values defining the [`Torus`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html#manim.mobject.three_d.three_dimensions.Torus "manim.mobject.three_d.three_dimensions.Torus") being plotted.

Returns:

The z values defining the [`Torus`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html#manim.mobject.three_d.three_dimensions.Torus "manim.mobject.three_d.three_dimensions.Torus").

Return type:

`numpy.ndarray`

Parameters:

- **u** ( _float_)

- **v** ( _float_)