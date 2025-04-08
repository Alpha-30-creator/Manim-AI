# ImplicitFunction [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ImplicitFunction.html\#implicitfunction "Link to this heading")

Qualified name: `manim.mobject.graphing.functions.ImplicitFunction`

_class_ ImplicitFunction( _func_, _x\_range=None_, _y\_range=None_, _min\_depth=5_, _max\_quads=1500_, _use\_smoothing=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/functions.html#ImplicitFunction) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ImplicitFunction.html#manim.mobject.graphing.functions.ImplicitFunction "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

An implicit function.

Parameters:

- **func** ( _Callable_ _\[_ _\[_ _float_ _,_ _float_ _\]_ _,_ _float_ _\]_) – The implicit function in the form `f(x, y) = 0`.

- **x\_range** ( _Sequence_ _\[_ _float_ _\]_ _\|_ _None_) – The x min and max of the function.

- **y\_range** ( _Sequence_ _\[_ _float_ _\]_ _\|_ _None_) – The y min and max of the function.

- **min\_depth** ( _int_) – The minimum depth of the function to calculate.

- **max\_quads** ( _int_) – The maximum number of quads to use.

- **use\_smoothing** ( _bool_) – Whether or not to smoothen the curves.

- **kwargs** – Additional parameters to pass into `VMobject`


Note

A small `min_depth` d means that some small details might
be ignored if they don’t cross an edge of one of the
4d uniform quads.

The value of `max_quads` strongly corresponds to the
quality of the curve, but a higher number of quads
may take longer to render.

Examples

Example: ImplicitFunctionExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ImplicitFunction.html#implicitfunctionexample)

![../_images/ImplicitFunctionExample-1.png](https://docs.manim.community/en/stable/_images/ImplicitFunctionExample-1.png)

```
from manim import *

class ImplicitFunctionExample(Scene):
    def construct(self):
        graph = ImplicitFunction(
            lambda x, y: x * y ** 2 - x ** 2 * y - 2,
            color=YELLOW
        )
        self.add(NumberPlane(), graph)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`generate_points`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ImplicitFunction.html#manim.mobject.graphing.functions.ImplicitFunction.generate_points "manim.mobject.graphing.functions.ImplicitFunction.generate_points") | Initializes `points` and therefore the shape. |
| [`init_points`](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ImplicitFunction.html#manim.mobject.graphing.functions.ImplicitFunction.init_points "manim.mobject.graphing.functions.ImplicitFunction.init_points") | Initializes `points` and therefore the shape. |

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

\_original\_\_init\_\_( _func_, _x\_range=None_, _y\_range=None_, _min\_depth=5_, _max\_quads=1500_, _use\_smoothing=True_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ImplicitFunction.html#manim.mobject.graphing.functions.ImplicitFunction._original__init__ "Link to this definition")

An implicit function.

Parameters:

- **func** ( _Callable_ _\[_ _\[_ _float_ _,_ _float_ _\]_ _,_ _float_ _\]_) – The implicit function in the form `f(x, y) = 0`.

- **x\_range** ( _Sequence_ _\[_ _float_ _\]_ _\|_ _None_) – The x min and max of the function.

- **y\_range** ( _Sequence_ _\[_ _float_ _\]_ _\|_ _None_) – The y min and max of the function.

- **min\_depth** ( _int_) – The minimum depth of the function to calculate.

- **max\_quads** ( _int_) – The maximum number of quads to use.

- **use\_smoothing** ( _bool_) – Whether or not to smoothen the curves.

- **kwargs** – Additional parameters to pass into `VMobject`


Note

A small `min_depth` d means that some small details might
be ignored if they don’t cross an edge of one of the
4d uniform quads.

The value of `max_quads` strongly corresponds to the
quality of the curve, but a higher number of quads
may take longer to render.

Examples

Example: ImplicitFunctionExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ImplicitFunction.html#implicitfunctionexample)

![../_images/ImplicitFunctionExample-2.png](https://docs.manim.community/en/stable/_images/ImplicitFunctionExample-2.png)

```
from manim import *

class ImplicitFunctionExample(Scene):
    def construct(self):
        graph = ImplicitFunction(
            lambda x, y: x * y ** 2 - x ** 2 * y - 2,
            color=YELLOW
        )
        self.add(NumberPlane(), graph)

```

Copy to clipboard

Make interactive

generate\_points() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graphing/functions.html#ImplicitFunction.generate_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ImplicitFunction.html#manim.mobject.graphing.functions.ImplicitFunction.generate_points "Link to this definition")

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

init\_points() [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ImplicitFunction.html#manim.mobject.graphing.functions.ImplicitFunction.init_points "Link to this definition")

Initializes `points` and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.