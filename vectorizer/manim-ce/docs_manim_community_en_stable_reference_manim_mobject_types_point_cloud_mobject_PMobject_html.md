ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# PMobject [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html\#pmobject "Link to this heading")

Qualified name: `manim.mobject.types.point\_cloud\_mobject.PMobject`

_class_ PMobject( _stroke\_width=4_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html#PMobject) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject "Link to this definition")

Bases: [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

A disc made of a cloud of Dots

Examples

Example: PMobjectExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#pmobjectexample)

![../_images/PMobjectExample-1.png](https://docs.manim.community/en/stable/_images/PMobjectExample-1.png)

```
from manim import *

class PMobjectExample(Scene):
    def construct(self):

        pG = PGroup()  # This is just a collection of PMobject's

        # As the scale factor increases, the number of points
        # removed increases.
        for sf in range(1, 9 + 1):
            p = PointCloudDot(density=20, radius=1).thin_out(sf)
            # PointCloudDot is a type of PMobject
            # and can therefore be added to a PGroup
            pG.add(p)

        # This organizes all the shapes in a grid.
        pG.arrange_in_grid()

        self.add(pG)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`add_points`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.add_points "manim.mobject.types.point_cloud_mobject.PMobject.add_points") | Add points. |
| `align_points_with_larger` |  |
| `fade_to` |  |
| `filter_out` |  |
| `get_all_rgbas` |  |
| `get_array_attrs` |  |
| [`get_color`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.get_color "manim.mobject.types.point_cloud_mobject.PMobject.get_color") | Returns the color of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
| [`get_mobject_type_class`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.get_mobject_type_class "manim.mobject.types.point_cloud_mobject.PMobject.get_mobject_type_class") | Return the base class of this mobject type. |
| [`get_point_mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.get_point_mobject "manim.mobject.types.point_cloud_mobject.PMobject.get_point_mobject") | The simplest [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to be transformed to or from self. |
| `get_stroke_width` |  |
| `ingest_submobjects` |  |
| `interpolate_color` |  |
| `match_colors` |  |
| `point_from_proportion` |  |
| `pointwise_become_partial` |  |
| [`reset_points`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.reset_points "manim.mobject.types.point_cloud_mobject.PMobject.reset_points") | Sets `points` to be an empty array. |
| [`set_color`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.set_color "manim.mobject.types.point_cloud_mobject.PMobject.set_color") | Condition is function which takes in one arguments, (x, y, z). |
| [`set_color_by_gradient`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.set_color_by_gradient "manim.mobject.types.point_cloud_mobject.PMobject.set_color_by_gradient") |  |
| `set_colors_by_radial_gradient` |  |
| `set_stroke_width` |  |
| [`sort_points`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.sort_points "manim.mobject.types.point_cloud_mobject.PMobject.sort_points") | Function is any map from R^3 to R |
| [`thin_out`](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.thin_out "manim.mobject.types.point_cloud_mobject.PMobject.thin_out") | Removes all but every nth point for n = factor |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `depth` | The depth of the mobject. |
| `height` | The height of the mobject. |
| `width` | The width of the mobject. |

Parameters:

- **stroke\_width** ( _int_)

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _stroke\_width=4_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **stroke\_width** ( _int_)

- **kwargs** ( _Any_)


Return type:

None

add\_points( _points_, _rgbas=None_, _color=None_, _alpha=1_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.add_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.add_points "Link to this definition")

Add points.

Points must be a Nx3 numpy array.
Rgbas must be a Nx4 numpy array if it is not None.

Parameters:

- **points** ( _npt.NDArray_)

- **rgbas** ( _npt.NDArray_ _\|_ _None_)

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_)

- **alpha** ( _float_)


Return type:

Self

get\_color() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.get_color) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.get_color "Link to this definition")

Returns the color of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Examples

```
>>> from manim import Square, RED
>>> Square(color=RED).get_color() == RED
True

```

Copy to clipboard

Return type:

[_ManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

_static_ get\_mobject\_type\_class() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.get_mobject_type_class) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.get_mobject_type_class "Link to this definition")

Return the base class of this mobject type.

Return type:

type\[ [_PMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject "manim.mobject.types.point_cloud_mobject.PMobject")\]

get\_point\_mobject( _center=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.get_point_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.get_point_mobject "Link to this definition")

The simplest [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to be transformed to or from self.
Should by a point of the appropriate type

Parameters:

**center** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\|_ _None_)

Return type:

[Point](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Point.html#manim.mobject.types.point_cloud_mobject.Point "manim.mobject.types.point_cloud_mobject.Point")

reset\_points() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.reset_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.reset_points "Link to this definition")

Sets `points` to be an empty array.

Return type:

Self

set\_color( _color=ManimColor('#FFFF00')_, _family=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.set_color) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.set_color "Link to this definition")

Condition is function which takes in one arguments, (x, y, z).
Here it just recurses to submobjects, but in subclasses this
should be further implemented based on the the inner workings
of color

Parameters:

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **family** ( _bool_)


Return type:

Self

set\_color\_by\_gradient( _\*colors_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.set_color_by_gradient) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.set_color_by_gradient "Link to this definition")Parameters:

- **colors** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The colors to use for the gradient. Use like set\_color\_by\_gradient(RED, BLUE, GREEN).

- **ManimColor.parse** **(** **color** **)** ( _self.color =_)

- **self** ( _return_)


Return type:

Self

sort\_points( _function=<functionPMobject.<lambda>>_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.sort_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.sort_points "Link to this definition")

Function is any map from R^3 to R

Parameters:

**function** ( _Callable_ _\[_ _\[_ _npt.NDArray_ _\[_ [_ManimFloat_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimFloat "manim.typing.ManimFloat") _\]_ _\]_ _,_ _float_ _\]_)

Return type:

Self

thin\_out( _factor=5_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.thin_out) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject.thin_out "Link to this definition")

Removes all but every nth point for n = factor

Parameters:

**factor** ( _int_)

Return type:

Self