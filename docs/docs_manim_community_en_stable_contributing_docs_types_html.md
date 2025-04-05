ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/contributing/docs/types.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/contributing/docs/types.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Choosing Type Hints [¶](https://docs.manim.community/en/stable/contributing/docs/types.html\#choosing-type-hints "Link to this heading")

In order to provide the best user experience,
it’s important that type hints are chosen correctly.
With the large variety of types provided by Manim, choosing
which one to use can be difficult. This guide aims to
aid you in the process of choosing the right type for the scenario.

The first step is figuring out which category your type hint fits into.

## Coordinates [¶](https://docs.manim.community/en/stable/contributing/docs/types.html\#coordinates "Link to this heading")

Coordinates encompass two main categories: points, and vectors.

### Points [¶](https://docs.manim.community/en/stable/contributing/docs/types.html\#points "Link to this heading")

The purpose of points is pretty straightforward: they represent a point
in space. For example:

```
def print_point2D(coord: Point2DLike) -> None:
    x, y = coord
    print(f"Point at {x=},{y=}")

def print_point3D(coord: Point3DLike) -> None:
    x, y, z = coord
    print(f"Point at {x=},{y=},{z=}")

def print_point_array(coords: Point2DLike_Array | Point3DLike_Array) -> None:
    for coord in coords:
        if len(coord) == 2:
            # it's a Point2DLike
            print_point2D(coord)
        else:
            # it's a Point3DLike
            print_point3D(coord)

def shift_point_up(coord: Point3DLike) -> Point3D:
    result = np.asarray(coord)
    result += UP
    print(f"New point: {result}")
    return result

```

Copy to clipboard

Notice that the last function, `shift_point_up()`, accepts a
[`Point3DLike`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") as a parameter and returns a [`Point3D`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"). A
[`Point3D`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D") always represents a NumPy array consisting of 3 floats,
whereas a [`Point3DLike`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") can represent anything resembling a 3D point:
either a NumPy array or a tuple/list of 3 floats, hence the `Like` word. The
same happens with [`Point2D`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point2D "manim.typing.Point2D"), [`Point2D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point2D_Array "manim.typing.Point2D_Array") and
[`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array"), and their `Like` counterparts
[`Point2DLike`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point2DLike "manim.typing.Point2DLike"), [`Point2DLike_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point2DLike_Array "manim.typing.Point2DLike_Array") and
[`Point3DLike_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array").

The rule for typing functions is: **make parameter types as broad as possible,**
**and return types as specific as possible.** Therefore, for functions which are
intended to be called by users, **we should always, if possible, accept** `Like` **types as parameters and return NumPy, non-** `Like` **types.** The
main reason is to be more flexible with users who might want to pass tuples or
lists as arguments rather than NumPy arrays, because it’s more convenient. The
last function, `shift_point_up()`, is an example of it.

Internal functions which are _not_ meant to be called by users may accept
non- `Like` parameters if necessary.

### Vectors [¶](https://docs.manim.community/en/stable/contributing/docs/types.html\#vectors "Link to this heading")

Vectors share many similarities to points. However, they have a different
connotation. Vectors should be used to represent direction. For example,
consider this slightly contrived function:

```
M = TypeVar("M", bound=Mobject)  # allow any mobject
def shift_mobject(mob: M, direction: Vector3D, scale_factor: float = 1) -> M:
    return mob.shift(direction * scale_factor)

```

Copy to clipboard

Here we see an important example of the difference. `direction` should not be
typed as a [`Point3D`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"), because it represents a direction along
which to shift a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), not a position in space.

As a general rule, if a parameter is called `direction` or `axis`,
it should be type hinted as some form of [`VectorND`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.VectorND "manim.typing.VectorND").

Warning

This is not always true. For example, as of Manim 0.18.0, the direction
parameter of the [`Vector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector") Mobject should be
`Point2DLike | Point3DLike`, as it can also accept `tuple[float, float]`
and `tuple[float, float, float]`.

## Colors [¶](https://docs.manim.community/en/stable/contributing/docs/types.html\#colors "Link to this heading")

The interface Manim provides for working with colors is [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").
The main color types Manim supports are RGB, RGBA, and HSV. You will want
to add type hints to a function depending on which type it uses. If any color will work,
you will need something like:

```
if TYPE_CHECKING:
    from manim.utils.color import ParsableManimColor

# type hint stuff with ParsableManimColor

```

Copy to clipboard

## Béziers [¶](https://docs.manim.community/en/stable/contributing/docs/types.html\#beziers "Link to this heading")

Manim internally represents a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") by a collection of points. In the case of [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"),
the most commonly used subclass of [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), these points represent Bézier curves,
which are a way of representing a curve using a sequence of points.

Note

To learn more about Béziers, take a look at [https://pomax.github.io/bezierinfo/](https://pomax.github.io/bezierinfo/)

Manim supports two different renderers, which each have different representations of
Béziers: Cairo uses cubic Bézier curves, while OpenGL uses quadratic Bézier curves.

Type hints like [`BezierPoints`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.BezierPoints "manim.typing.BezierPoints") represent a single bezier curve, and [`BezierPath`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.BezierPath "manim.typing.BezierPath")
represents multiple Bézier curves. A [`Spline`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Spline "manim.typing.Spline") is when the Bézier curves in a [`BezierPath`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.BezierPath "manim.typing.BezierPath")
forms a single connected curve. Manim also provides more specific type aliases when working with
quadratic or cubic curves, and they are prefixed with their respective type (e.g. [`CubicBezierPoints`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.CubicBezierPoints "manim.typing.CubicBezierPoints"),
is a [`BezierPoints`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.BezierPoints "manim.typing.BezierPoints") consisting of exactly 4 points representing a cubic Bézier curve).

## Functions [¶](https://docs.manim.community/en/stable/contributing/docs/types.html\#functions "Link to this heading")

Throughout the codebase, many different types of functions are used. The most obvious example
is a rate function, which takes in a float and outputs a float ( `Callable[[float], float]`).
Another example is for overriding animations. One will often need to map a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")
to an overridden [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"), and for that we have the [`FunctionOverride`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.FunctionOverride "manim.typing.FunctionOverride") type hint.

[`PathFuncType`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PathFuncType "manim.typing.PathFuncType") and [`MappingFunction`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.MappingFunction "manim.typing.MappingFunction") are more niche, but are related to moving objects
along a path, or applying functions. If you need to use it, you’ll know.

## Images [¶](https://docs.manim.community/en/stable/contributing/docs/types.html\#images "Link to this heading")

There are several representations of images in Manim. The most common is
the representation as a NumPy array of floats representing the pixels of an image.
This is especially common when it comes to the OpenGL renderer.

This is the use case of the [`PixelArray`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PixelArray "manim.typing.PixelArray") type hint. Sometimes, Manim may use `PIL.Image.Image`,
which is not the same as [`PixelArray`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PixelArray "manim.typing.PixelArray"). In this case, use the `PIL.Image.Image` typehint.
Of course, if a more specific type of image is needed, it can be annotated as such.