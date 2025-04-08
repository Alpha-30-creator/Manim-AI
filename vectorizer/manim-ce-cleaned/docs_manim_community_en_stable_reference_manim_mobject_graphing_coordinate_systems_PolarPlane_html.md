# PolarPlane [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html\#polarplane "Link to this heading")

Qualified name: `manim.mobject.graphing.coordinate\_systems.PolarPlane`

_class_ PolarPlane( _radius\_max=4.0_, _size=None_, _radius\_step=1_, _azimuth\_step=None_, _azimuth\_units='PIradians'_, _azimuth\_compact\_fraction=True_, _azimuth\_offset=0_, _azimuth\_direction='CCW'_, _azimuth\_label\_buff=0.1_, _azimuth\_label\_font\_size=24_, _radius\_config=None_, _background\_line\_style=None_, _faded\_line\_style=None_, _faded\_line\_ratio=1_, _make\_smooth\_after\_applying\_functions=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html#manim.mobject.graphing.coordinate_systems.PolarPlane "Link to this definition")

Bases: [`Axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes")

Creates a polar plane with background lines.

Parameters:

- **azimuth\_step** ( _float_ _\|_ _None_) –

The number of divisions in the azimuth (also known as the angular coordinate or polar angle). If `None` is specified then it will use the default
specified by `azimuth_units`:


  - `"PI radians"` or `"TAU radians"`: 20

  - `"degrees"`: 36

  - `"gradians"`: 40

  - `None`: 1


A non-integer value will result in a partial division at the end of the circle.

- **size** ( _float_ _\|_ _None_) – The diameter of the plane.

- **radius\_step** ( _float_) – The distance between faded radius lines.

- **radius\_max** ( _float_) – The maximum value of the radius.

- **azimuth\_units** ( _str_ _\|_ _None_) –

Specifies a default labelling system for the azimuth. Choices are:


  - `"PI radians"`: Fractional labels in the interval \[0,2π\] with π as a constant.

  - `"TAU radians"`: Fractional labels in the interval \[0,τ\] (where τ=2π) with τ as a constant.

  - `"degrees"`: Decimal labels in the interval \[0,360\] with a degree (∘) symbol.

  - `"gradians"`: Decimal labels in the interval \[0,400\] with a superscript “g” (g).

  - `None`: Decimal labels in the interval \[0,1\].


- **azimuth\_compact\_fraction** ( _bool_) – If the `azimuth_units` choice has fractional labels, choose whether to
combine the constant in a compact form xuy as opposed to
xyu, where u is the constant.

- **azimuth\_offset** ( _float_) – The angle offset of the azimuth, expressed in radians.

- **azimuth\_direction** ( _str_) –

The direction of the azimuth.


  - `"CW"`: Clockwise.

  - `"CCW"`: Anti-clockwise.


- **azimuth\_label\_buff** ( _float_) – The buffer for the azimuth labels.

- **azimuth\_label\_font\_size** ( _float_) – The font size of the azimuth labels.

- **radius\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_) – The axis config for the radius.

- **background\_line\_style** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **faded\_line\_style** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **faded\_line\_ratio** ( _int_)

- **make\_smooth\_after\_applying\_functions** ( _bool_)

- **kwargs** ( _Any_)


Examples

Example: PolarPlaneExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html#polarplaneexample)

![../_images/PolarPlaneExample-1.png](https://docs.manim.community/en/stable/_images/PolarPlaneExample-1.png)

```
from manim import *

class PolarPlaneExample(Scene):
    def construct(self):
        polarplane_pi = PolarPlane(
            azimuth_units="PI radians",
            size=6,
            azimuth_label_font_size=33.6,
            radius_config={"font_size": 33.6},
        ).add_coordinates()
        self.add(polarplane_pi)

```

Copy to clipboard

Make interactive

References: [`PolarPlane`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html#manim.mobject.graphing.coordinate_systems.PolarPlane "manim.mobject.graphing.coordinate_systems.PolarPlane")

Methods

|     |     |
| --- | --- |
| [`add_coordinates`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html#manim.mobject.graphing.coordinate_systems.PolarPlane.add_coordinates "manim.mobject.graphing.coordinate_systems.PolarPlane.add_coordinates") | Adds the coordinates. |
| [`get_axes`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html#manim.mobject.graphing.coordinate_systems.PolarPlane.get_axes "manim.mobject.graphing.coordinate_systems.PolarPlane.get_axes") | Gets the axes. |
| [`get_coordinate_labels`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html#manim.mobject.graphing.coordinate_systems.PolarPlane.get_coordinate_labels "manim.mobject.graphing.coordinate_systems.PolarPlane.get_coordinate_labels") | Gets labels for the coordinates |
| `get_radian_label` |  |
| `get_vector` |  |
| `prepare_for_nonlinear_transform` |  |

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

\_get\_lines() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane._get_lines) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html#manim.mobject.graphing.coordinate_systems.PolarPlane._get_lines "Link to this definition")

Generate all the lines and circles, faded and not faded.

Returns:

The first (i.e the non faded lines and circles) and second (i.e the faded lines and circles) sets of lines and circles, respectively.

Return type:

Tuple\[ [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup"), [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")\]

\_init\_background\_lines() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane._init_background_lines) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html#manim.mobject.graphing.coordinate_systems.PolarPlane._init_background_lines "Link to this definition")

Will init all the lines of NumberPlanes (faded or not)

Return type:

None

\_original\_\_init\_\_( _radius\_max=4.0_, _size=None_, _radius\_step=1_, _azimuth\_step=None_, _azimuth\_units='PIradians'_, _azimuth\_compact\_fraction=True_, _azimuth\_offset=0_, _azimuth\_direction='CCW'_, _azimuth\_label\_buff=0.1_, _azimuth\_label\_font\_size=24_, _radius\_config=None_, _background\_line\_style=None_, _faded\_line\_style=None_, _faded\_line\_ratio=1_, _make\_smooth\_after\_applying\_functions=True_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html#manim.mobject.graphing.coordinate_systems.PolarPlane._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **radius\_max** ( _float_)

- **size** ( _float_ _\|_ _None_)

- **radius\_step** ( _float_)

- **azimuth\_step** ( _float_ _\|_ _None_)

- **azimuth\_units** ( _str_ _\|_ _None_)

- **azimuth\_compact\_fraction** ( _bool_)

- **azimuth\_offset** ( _float_)

- **azimuth\_direction** ( _str_)

- **azimuth\_label\_buff** ( _float_)

- **azimuth\_label\_font\_size** ( _float_)

- **radius\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **background\_line\_style** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **faded\_line\_style** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **faded\_line\_ratio** ( _int_)

- **make\_smooth\_after\_applying\_functions** ( _bool_)

- **kwargs** ( _Any_)


Return type:

None

add\_coordinates( _r\_values=None_, _a\_values=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane.add_coordinates) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html#manim.mobject.graphing.coordinate_systems.PolarPlane.add_coordinates "Link to this definition")

Adds the coordinates.

Parameters:

- **r\_values** ( _Iterable_ _\[_ _float_ _\]_ _\|_ _None_) – Iterable of values along the radius, by default None.

- **a\_values** ( _Iterable_ _\[_ _float_ _\]_ _\|_ _None_) – Iterable of values along the azimuth, by default None.


Return type:

_Self_

get\_axes() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane.get_axes) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html#manim.mobject.graphing.coordinate_systems.PolarPlane.get_axes "Link to this definition")

Gets the axes.

Returns:

A pair of axes.

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

get\_coordinate\_labels( _r\_values=None_, _a\_values=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane.get_coordinate_labels) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.PolarPlane.html#manim.mobject.graphing.coordinate_systems.PolarPlane.get_coordinate_labels "Link to this definition")

Gets labels for the coordinates

Parameters:

- **r\_values** ( _Iterable_ _\[_ _float_ _\]_ _\|_ _None_) – Iterable of values along the radius, by default None.

- **a\_values** ( _Iterable_ _\[_ _float_ _\]_ _\|_ _None_) – Iterable of values along the azimuth, by default None.

- **kwargs** ( _Any_)


Returns:

Labels for the radius and azimuth values.

Return type:

[VDict](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict")

[Automate site indexing, catalog pages, & refine your search accuracy with Algolia’s website crawler](https://server.ethicalads.io/proxy/click/8328/019600e7-3601-7d60-8197-da0d65437eec/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8328/019600e7-3601-7d60-8197-da0d65437eec/)