ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# VectorField [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html\#vectorfield "Link to this heading")

Qualified name: `manim.mobject.vector\_field.VectorField`

_class_ VectorField( _func_, _color=None_, _color\_scheme=None_, _min\_color\_scheme\_value=0_, _max\_color\_scheme\_value=2_, _colors=\[ManimColor('#236B8E'),ManimColor('#83C167'),ManimColor('#FFFF00'),ManimColor('#FC6255')\]_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#VectorField) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "Link to this definition")

Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

A vector field.

Vector fields are based on a function defining a vector at every position.
This class does by default not include any visible elements but provides
methods to move other [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") s along the vector field.

Parameters:

- **func** ( _Callable_ _\[_ _\[_ _np.ndarray_ _\]_ _,_ _np.ndarray_ _\]_) – The function defining the rate of change at every position of the VectorField.

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_) – The color of the vector field. If set, position-specific coloring is disabled.

- **color\_scheme** ( _Callable_ _\[_ _\[_ _np.ndarray_ _\]_ _,_ _float_ _\]_ _\|_ _None_) – A function mapping a vector to a single value. This value gives the position in the color gradient defined using min\_color\_scheme\_value, max\_color\_scheme\_value and colors.

- **min\_color\_scheme\_value** ( _float_) – The value of the color\_scheme function to be mapped to the first color in colors. Lower values also result in the first color of the gradient.

- **max\_color\_scheme\_value** ( _float_) – The value of the color\_scheme function to be mapped to the last color in colors. Higher values also result in the last color of the gradient.

- **colors** ( _Sequence_ _\[_ [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\]_) – The colors defining the color gradient of the vector field.

- **kwargs** – Additional arguments to be passed to the [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") constructor


Methods

|     |     |
| --- | --- |
| [`fit_to_coordinate_system`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.fit_to_coordinate_system "manim.mobject.vector_field.VectorField.fit_to_coordinate_system") | Scale the vector field to fit a coordinate system. |
| [`get_colored_background_image`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.get_colored_background_image "manim.mobject.vector_field.VectorField.get_colored_background_image") | Generate an image that displays the vector field. |
| [`get_nudge_updater`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.get_nudge_updater "manim.mobject.vector_field.VectorField.get_nudge_updater") | Get an update function to move a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") along the vector field. |
| [`get_vectorized_rgba_gradient_function`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.get_vectorized_rgba_gradient_function "manim.mobject.vector_field.VectorField.get_vectorized_rgba_gradient_function") | Generates a gradient of rgbas as a numpy array |
| [`nudge`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.nudge "manim.mobject.vector_field.VectorField.nudge") | Nudge a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") along the vector field. |
| [`nudge_submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.nudge_submobjects "manim.mobject.vector_field.VectorField.nudge_submobjects") | Apply a nudge along the vector field to all submobjects. |
| [`scale_func`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.scale_func "manim.mobject.vector_field.VectorField.scale_func") | Scale a vector field function. |
| [`shift_func`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.shift_func "manim.mobject.vector_field.VectorField.shift_func") | Shift a vector field function. |
| [`start_submobject_movement`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.start_submobject_movement "manim.mobject.vector_field.VectorField.start_submobject_movement") | Start continuously moving all submobjects along the vector field. |
| [`stop_submobject_movement`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.stop_submobject_movement "manim.mobject.vector_field.VectorField.stop_submobject_movement") | Stops the continuous movement started using [`start_submobject_movement()`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.start_submobject_movement "manim.mobject.vector_field.VectorField.start_submobject_movement"). |

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

\_original\_\_init\_\_( _func_, _color=None_, _color\_scheme=None_, _min\_color\_scheme\_value=0_, _max\_color\_scheme\_value=2_, _colors=\[ManimColor('#236B8E'),ManimColor('#83C167'),ManimColor('#FFFF00'),ManimColor('#FC6255')\]_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **func** ( _Callable_ _\[_ _\[_ _np.ndarray_ _\]_ _,_ _np.ndarray_ _\]_)

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_)

- **color\_scheme** ( _Callable_ _\[_ _\[_ _np.ndarray_ _\]_ _,_ _float_ _\]_ _\|_ _None_)

- **min\_color\_scheme\_value** ( _float_)

- **max\_color\_scheme\_value** ( _float_)

- **colors** ( _Sequence_ _\[_ [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\]_)


fit\_to\_coordinate\_system( _coordinate\_system_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#VectorField.fit_to_coordinate_system) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.fit_to_coordinate_system "Link to this definition")

Scale the vector field to fit a coordinate system.

This method is useful when the vector field is defined in a coordinate system
different from the one used to display the vector field.

This method can only be used once because it transforms the origin of each vector.

Parameters:

**coordinate\_system** ( [_CoordinateSystem_](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem "manim.mobject.graphing.coordinate_systems.CoordinateSystem")) – The coordinate system to fit the vector field to.

get\_colored\_background\_image( _sampling\_rate=5_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#VectorField.get_colored_background_image) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.get_colored_background_image "Link to this definition")

Generate an image that displays the vector field.

The color at each position is calculated by passing the positing through a
series of steps:
Calculate the vector field function at that position, map that vector to a
single value using self.color\_scheme and finally generate a color from
that value using the color gradient.

Parameters:

**sampling\_rate** ( _int_) – The stepsize at which pixels get included in the image. Lower values give
more accurate results, but may take a long time to compute.

Returns:

The vector field image.

Return type:

Image.Imgae

get\_nudge\_updater( _speed=1_, _pointwise=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#VectorField.get_nudge_updater) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.get_nudge_updater "Link to this definition")

Get an update function to move a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") along the vector field.

When used with [`add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater"), the mobject will move along the vector field, where its speed is determined by the magnitude of the vector field.

Parameters:

- **speed** ( _float_) – At speed=1 the distance a mobject moves per second is equal to the magnitude of the vector field along its path. The speed value scales the speed of such a mobject.

- **pointwise** ( _bool_) – Whether to move the mobject along the vector field. See [`nudge()`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.nudge "manim.mobject.vector_field.VectorField.nudge") for details.


Returns:

The update function.

Return type:

Callable\[\[ [Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), float\], [Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")\]

get\_vectorized\_rgba\_gradient\_function( _start_, _end_, _colors_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#VectorField.get_vectorized_rgba_gradient_function) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.get_vectorized_rgba_gradient_function "Link to this definition")

Generates a gradient of rgbas as a numpy array

Parameters:

- **start** ( _float_) – start value used for inverse interpolation at [`inverse_interpolate()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.inverse_interpolate "manim.utils.bezier.inverse_interpolate")

- **end** ( _float_) – end value used for inverse interpolation at [`inverse_interpolate()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.inverse_interpolate "manim.utils.bezier.inverse_interpolate")

- **colors** ( _Iterable_ _\[_ [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\]_) – list of colors to generate the gradient


Return type:

function to generate the gradients as numpy arrays representing rgba values

nudge( _mob_, _dt=1_, _substeps=1_, _pointwise=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#VectorField.nudge) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.nudge "Link to this definition")

Nudge a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") along the vector field.

Parameters:

- **mob** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to move along the vector field

- **dt** ( _float_) – A scalar to the amount the mobject is moved along the vector field.
The actual distance is based on the magnitude of the vector field.

- **substeps** ( _int_) – The amount of steps the whole nudge is divided into. Higher values
give more accurate approximations.

- **pointwise** ( _bool_) – Whether to move the mobject along the vector field. If False the
vector field takes effect on the center of the given
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). If True the vector field takes effect on the
points of the individual points of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"),
potentially distorting it.


Returns:

This vector field.

Return type:

[VectorField](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")

Examples

Example: Nudging [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#nudging)

```
from manim import *

class Nudging(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[1] / 2) * RIGHT + np.cos(pos[0] / 2) * UP
        vector_field = ArrowVectorField(
            func, x_range=[-7, 7, 1], y_range=[-4, 4, 1], length_func=lambda x: x / 2
        )
        self.add(vector_field)
        circle = Circle(radius=2).shift(LEFT)
        self.add(circle.copy().set_color(GRAY))
        dot = Dot().move_to(circle)

        vector_field.nudge(circle, -2, 60, True)
        vector_field.nudge(dot, -2, 60)

        circle.add_updater(vector_field.get_nudge_updater(pointwise=True))
        dot.add_updater(vector_field.get_nudge_updater())
        self.add(circle, dot)
        self.wait(6)

```

Copy to clipboard

Make interactive

nudge\_submobjects( _dt=1_, _substeps=1_, _pointwise=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#VectorField.nudge_submobjects) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.nudge_submobjects "Link to this definition")

Apply a nudge along the vector field to all submobjects.

Parameters:

- **dt** ( _float_) – A scalar to the amount the mobject is moved along the vector field.
The actual distance is based on the magnitude of the vector field.

- **substeps** ( _int_) – The amount of steps the whole nudge is divided into. Higher values
give more accurate approximations.

- **pointwise** ( _bool_) – Whether to move the mobject along the vector field. See [`nudge()`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.nudge "manim.mobject.vector_field.VectorField.nudge") for details.


Returns:

This vector field.

Return type:

[VectorField](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")

_static_ scale\_func( _func_, _scalar_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#VectorField.scale_func) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.scale_func "Link to this definition")

Scale a vector field function.

Parameters:

- **func** ( _Callable_ _\[_ _\[_ _ndarray_ _\]_ _,_ _ndarray_ _\]_) – The function defining a vector field.

- **scalar** ( _float_) – The scalar to be applied to the vector field.


Return type:

_Callable_\[\[ _ndarray_\], _ndarray_\]

Examples

Example: ScaleVectorFieldFunction [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#scalevectorfieldfunction)

```
from manim import *

class ScaleVectorFieldFunction(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[1]) * RIGHT + np.cos(pos[0]) * UP
        vector_field = ArrowVectorField(func)
        self.add(vector_field)
        self.wait()

        func = VectorField.scale_func(func, 0.5)
        self.play(vector_field.animate.become(ArrowVectorField(func)))
        self.wait()

```

Copy to clipboard

Make interactive

Returns:

The scaled vector field function.

Return type:

Callable\[\[np.ndarray\], np.ndarray\]

Parameters:

- **func** ( _Callable_ _\[_ _\[_ _ndarray_ _\]_ _,_ _ndarray_ _\]_)

- **scalar** ( _float_)


_static_ shift\_func( _func_, _shift\_vector_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#VectorField.shift_func) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.shift_func "Link to this definition")

Shift a vector field function.

Parameters:

- **func** ( _Callable_ _\[_ _\[_ _ndarray_ _\]_ _,_ _ndarray_ _\]_) – The function defining a vector field.

- **shift\_vector** ( _ndarray_) – The shift to be applied to the vector field.


Returns:

The shifted vector field function.

Return type:

Callable\[\[np.ndarray\], np.ndarray\]

start\_submobject\_movement( _speed=1_, _pointwise=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#VectorField.start_submobject_movement) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.start_submobject_movement "Link to this definition")

Start continuously moving all submobjects along the vector field.

Calling this method multiple times will result in removing the previous updater created by this method.

Parameters:

- **speed** ( _float_) – The speed at which to move the submobjects. See [`get_nudge_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.get_nudge_updater "manim.mobject.vector_field.VectorField.get_nudge_updater") for details.

- **pointwise** ( _bool_) – Whether to move the mobject along the vector field. See [`nudge()`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.nudge "manim.mobject.vector_field.VectorField.nudge") for details.


Returns:

This vector field.

Return type:

[VectorField](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")

stop\_submobject\_movement() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#VectorField.stop_submobject_movement) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.stop_submobject_movement "Link to this definition")

Stops the continuous movement started using [`start_submobject_movement()`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField.start_submobject_movement "manim.mobject.vector_field.VectorField.start_submobject_movement").

Returns:

This vector field.

Return type:

[VectorField](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")

[**Document Extraction for Developers** Transform docs into structured data with Sensible. **Try for free →**](https://server.ethicalads.io/proxy/click/8518/019600f7-bacd-7062-bdbb-9093eb2caf9f/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8518/019600f7-bacd-7062-bdbb-9093eb2caf9f/)