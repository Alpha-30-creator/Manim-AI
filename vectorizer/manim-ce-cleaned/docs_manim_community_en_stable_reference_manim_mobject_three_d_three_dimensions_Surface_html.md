# Surface [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html\#surface "Link to this heading")

Qualified name: `manim.mobject.three\_d.three\_dimensions.Surface`

_class_ Surface( _func_, _u\_range=\[0,1\]_, _v\_range=\[0,1\]_, _resolution=32_, _surface\_piece\_config={}_, _fill\_color=ManimColor('#29ABCA')_, _fill\_opacity=1.0_, _checkerboard\_colors=\[ManimColor('#29ABCA'),ManimColor('#236B8E')\]_, _stroke\_color=ManimColor('#BBBBBB')_, _stroke\_width=0.5_, _should\_make\_jagged=False_, _pre\_function\_handle\_to\_anchor\_scale\_factor=1e-05_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Surface) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "Link to this definition")

Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Creates a Parametric Surface using a checkerboard pattern.

Parameters:

- **func** ( _Callable_ _\[_ _\[_ _float_ _,_ _float_ _\]_ _,_ _np.ndarray_ _\]_) – The function defining the [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface").

- **u\_range** ( _Sequence_ _\[_ _float_ _\]_) – The range of the `u` variable: `(u_min, u_max)`.

- **v\_range** ( _Sequence_ _\[_ _float_ _\]_) – The range of the `v` variable: `(v_min, v_max)`.

- **resolution** ( _Sequence_ _\[_ _int_ _\]_) – The number of samples taken of the [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface"). A tuple can be
used to define different resolutions for `u` and `v` respectively.

- **fill\_color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface"). Ignored if `checkerboard_colors`
is set.

- **fill\_opacity** ( _float_) – The opacity of the [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface"), from 0 being fully transparent
to 1 being fully opaque. Defaults to 1.

- **checkerboard\_colors** ( _Sequence_ _\[_ [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\]_ _\|_ _bool_) – ng individual faces alternating colors. Overrides `fill_color`.

- **stroke\_color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – Color of the stroke surrounding each face of [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface").

- **stroke\_width** ( _float_) – Width of the stroke surrounding each face of [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface").
Defaults to 0.5.

- **should\_make\_jagged** ( _bool_) – Changes the anchor mode of the Bézier curves from smooth to jagged.
Defaults to `False`.

- **surface\_piece\_config** ( _dict_)

- **pre\_function\_handle\_to\_anchor\_scale\_factor** ( _float_)

- **kwargs** ( _Any_)


Examples

Example: ParaSurface [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#parasurface)

![../_images/ParaSurface-1.png](https://docs.manim.community/en/stable/_images/ParaSurface-1.png)

```
from manim import *

class ParaSurface(ThreeDScene):
    def func(self, u, v):
        return np.array([np.cos(u) * np.cos(v), np.cos(u) * np.sin(v), u])

    def construct(self):
        axes = ThreeDAxes(x_range=[-4,4], x_length=8)
        surface = Surface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=[-PI, PI],
            v_range=[0, TAU],
            resolution=8,
        )
        self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
        self.add(axes, surface)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `func` |  |
| [`set_fill_by_checkerboard`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface.set_fill_by_checkerboard "manim.mobject.three_d.three_dimensions.Surface.set_fill_by_checkerboard") | Sets the fill\_color of each face of [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface") in an alternating pattern. |
| [`set_fill_by_value`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface.set_fill_by_value "manim.mobject.three_d.three_dimensions.Surface.set_fill_by_value") | Sets the color of each mobject of a parametric surface to a color relative to its axis-value. |

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

\_original\_\_init\_\_( _func_, _u\_range=\[0,1\]_, _v\_range=\[0,1\]_, _resolution=32_, _surface\_piece\_config={}_, _fill\_color=ManimColor('#29ABCA')_, _fill\_opacity=1.0_, _checkerboard\_colors=\[ManimColor('#29ABCA'),ManimColor('#236B8E')\]_, _stroke\_color=ManimColor('#BBBBBB')_, _stroke\_width=0.5_, _should\_make\_jagged=False_, _pre\_function\_handle\_to\_anchor\_scale\_factor=1e-05_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **func** ( _Callable_ _\[_ _\[_ _float_ _,_ _float_ _\]_ _,_ _ndarray_ _\]_)

- **u\_range** ( _Sequence_ _\[_ _float_ _\]_)

- **v\_range** ( _Sequence_ _\[_ _float_ _\]_)

- **resolution** ( _Sequence_ _\[_ _int_ _\]_)

- **surface\_piece\_config** ( _dict_)

- **fill\_color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **fill\_opacity** ( _float_)

- **checkerboard\_colors** ( _Sequence_ _\[_ [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\]_ _\|_ _bool_)

- **stroke\_color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **stroke\_width** ( _float_)

- **should\_make\_jagged** ( _bool_)

- **pre\_function\_handle\_to\_anchor\_scale\_factor** ( _float_)

- **kwargs** ( _Any_)


Return type:

None

set\_fill\_by\_checkerboard( _\*colors_, _opacity=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Surface.set_fill_by_checkerboard) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface.set_fill_by_checkerboard "Link to this definition")

Sets the fill\_color of each face of [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface") in
an alternating pattern.

Parameters:

- **colors** ( _Iterable_ _\[_ [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\]_) – List of colors for alternating pattern.

- **opacity** ( _float_ _\|_ _None_) – The fill\_opacity of [`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface"), from 0 being fully transparent
to 1 being fully opaque.


Returns:

The parametric surface with an alternating pattern.

Return type:

[`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface")

set\_fill\_by\_value( _axes_, _colorscale=None_, _axis=2_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Surface.set_fill_by_value) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface.set_fill_by_value "Link to this definition")

Sets the color of each mobject of a parametric surface to a color
relative to its axis-value.

Parameters:

- **axes** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The axes for the parametric surface, which will be used to map
axis-values to colors.

- **colorscale** ( _list_ _\[_ [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\]_ _\|_ [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_) – A list of colors, ordered from lower axis-values to higher axis-values.
If a list of tuples is passed containing colors paired with numbers,
then those numbers will be used as the pivots.

- **axis** ( _int_) – The chosen axis to use for the color mapping. (0 = x, 1 = y, 2 = z)


Returns:

The parametric surface with a gradient applied by value. For chaining.

Return type:

[`Surface`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface")

Examples

Example: FillByValueExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Surface.html#fillbyvalueexample)

![../_images/FillByValueExample-1.png](https://docs.manim.community/en/stable/_images/FillByValueExample-1.png)

```
from manim import *

class FillByValueExample(ThreeDScene):
    def construct(self):
        resolution_fa = 8
        self.set_camera_orientation(phi=75 * DEGREES, theta=-160 * DEGREES)
        axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))
        def param_surface(u, v):
            x = u
            y = v
            z = np.sin(x) * np.cos(y)
            return z
        surface_plane = Surface(
            lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=[0, 5],
            u_range=[0, 5],
            )
        surface_plane.set_style(fill_opacity=1)
        surface_plane.set_fill_by_value(axes=axes, colorscale=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        self.add(axes, surface_plane)

```

Copy to clipboard

Make interactive