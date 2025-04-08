ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ArrowVectorField [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html\#arrowvectorfield "Link to this heading")

Qualified name: `manim.mobject.vector\_field.ArrowVectorField`

_class_ ArrowVectorField( _func,color=None,color\_scheme=None,min\_color\_scheme\_value=0,max\_color\_scheme\_value=2,colors=\[ManimColor('#236B8E'),ManimColor('#83C167'),ManimColor('#FFFF00'),ManimColor('#FC6255')\],x\_range=None,y\_range=None,z\_range=None,three\_dimensions=False,length\_func=<functionArrowVectorField.<lambda>>,opacity=1.0,vector\_config=None,\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#ArrowVectorField) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#manim.mobject.vector_field.ArrowVectorField "Link to this definition")

Bases: [`VectorField`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")

A [`VectorField`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField") represented by a set of change vectors.

Vector fields are always based on a function defining the [`Vector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector") at every position.
The values of this functions is displayed as a grid of vectors.
By default the color of each vector is determined by it’s magnitude.
Other color schemes can be used however.

Parameters:

- **func** ( _Callable_ _\[_ _\[_ _np.ndarray_ _\]_ _,_ _np.ndarray_ _\]_) – The function defining the rate of change at every position of the vector field.

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_) – The color of the vector field. If set, position-specific coloring is disabled.

- **color\_scheme** ( _Callable_ _\[_ _\[_ _np.ndarray_ _\]_ _,_ _float_ _\]_ _\|_ _None_) – A function mapping a vector to a single value. This value gives the position in the color gradient defined using min\_color\_scheme\_value, max\_color\_scheme\_value and colors.

- **min\_color\_scheme\_value** ( _float_) – The value of the color\_scheme function to be mapped to the first color in colors. Lower values also result in the first color of the gradient.

- **max\_color\_scheme\_value** ( _float_) – The value of the color\_scheme function to be mapped to the last color in colors. Higher values also result in the last color of the gradient.

- **colors** ( _Sequence_ _\[_ [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\]_) – The colors defining the color gradient of the vector field.

- **x\_range** ( _Sequence_ _\[_ _float_ _\]_) – A sequence of x\_min, x\_max, delta\_x

- **y\_range** ( _Sequence_ _\[_ _float_ _\]_) – A sequence of y\_min, y\_max, delta\_y

- **z\_range** ( _Sequence_ _\[_ _float_ _\]_) – A sequence of z\_min, z\_max, delta\_z

- **three\_dimensions** ( _bool_) – Enables three\_dimensions. Default set to False, automatically turns True if
z\_range is not None.

- **length\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_) – The function determining the displayed size of the vectors. The actual size
of the vector is passed, the returned value will be used as display size for the
vector. By default this is used to cap the displayed size of vectors to reduce the clutter.

- **opacity** ( _float_) – The opacity of the arrows.

- **vector\_config** ( _dict_ _\|_ _None_) – Additional arguments to be passed to the [`Vector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector") constructor

- **kwargs** – Additional arguments to be passed to the [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") constructor


Examples

Example: BasicUsage [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#basicusage)

![../_images/BasicUsage-1.png](https://docs.manim.community/en/stable/_images/BasicUsage-1.png)

```
from manim import *

class BasicUsage(Scene):
    def construct(self):
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        self.add(ArrowVectorField(func))

```

Copy to clipboard

Make interactive

Example: SizingAndSpacing [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#sizingandspacing)

```
from manim import *

class SizingAndSpacing(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        vf = ArrowVectorField(func, x_range=[-7, 7, 1])
        self.add(vf)
        self.wait()

        length_func = lambda x: x / 3
        vf2 = ArrowVectorField(func, x_range=[-7, 7, 1], length_func=length_func)
        self.play(vf.animate.become(vf2))
        self.wait()

```

Copy to clipboard

Make interactive

Example: Coloring [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#coloring)

![../_images/Coloring-1.png](https://docs.manim.community/en/stable/_images/Coloring-1.png)

```
from manim import *

class Coloring(Scene):
    def construct(self):
        func = lambda pos: pos - LEFT * 5
        colors = [RED, YELLOW, BLUE, DARK_GRAY]
        min_radius = Circle(radius=2, color=colors[0]).shift(LEFT * 5)
        max_radius = Circle(radius=10, color=colors[-1]).shift(LEFT * 5)
        vf = ArrowVectorField(
            func, min_color_scheme_value=2, max_color_scheme_value=10, colors=colors
        )
        self.add(vf, min_radius, max_radius)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`get_vector`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#manim.mobject.vector_field.ArrowVectorField.get_vector "manim.mobject.vector_field.ArrowVectorField.get_vector") | Creates a vector in the vector field. |

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

\_original\_\_init\_\_( _func,color=None,color\_scheme=None,min\_color\_scheme\_value=0,max\_color\_scheme\_value=2,colors=\[ManimColor('#236B8E'),ManimColor('#83C167'),ManimColor('#FFFF00'),ManimColor('#FC6255')\],x\_range=None,y\_range=None,z\_range=None,three\_dimensions=False,length\_func=<functionArrowVectorField.<lambda>>,opacity=1.0,vector\_config=None,\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#manim.mobject.vector_field.ArrowVectorField._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **func** ( _Callable_ _\[_ _\[_ _np.ndarray_ _\]_ _,_ _np.ndarray_ _\]_)

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_)

- **color\_scheme** ( _Callable_ _\[_ _\[_ _np.ndarray_ _\]_ _,_ _float_ _\]_ _\|_ _None_)

- **min\_color\_scheme\_value** ( _float_)

- **max\_color\_scheme\_value** ( _float_)

- **colors** ( _Sequence_ _\[_ [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\]_)

- **x\_range** ( _Sequence_ _\[_ _float_ _\]_)

- **y\_range** ( _Sequence_ _\[_ _float_ _\]_)

- **z\_range** ( _Sequence_ _\[_ _float_ _\]_)

- **three\_dimensions** ( _bool_)

- **length\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)

- **opacity** ( _float_)

- **vector\_config** ( _dict_ _\|_ _None_)


get\_vector( _point_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#ArrowVectorField.get_vector) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.ArrowVectorField.html#manim.mobject.vector_field.ArrowVectorField.get_vector "Link to this definition")

Creates a vector in the vector field.

The created vector is based on the function of the vector field and is
rooted in the given point. Color and length fit the specifications of
this vector field.

Parameters:

**point** ( _ndarray_) – The root point of the vector.

[**Document Extraction for Developers** Transform docs into structured data with Sensible. **Try for free →**](https://server.ethicalads.io/proxy/click/8518/019600e6-f90f-7e23-b4c4-dfd9cb2d3811/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8518/019600e6-f90f-7e23-b4c4-dfd9cb2d3811/)