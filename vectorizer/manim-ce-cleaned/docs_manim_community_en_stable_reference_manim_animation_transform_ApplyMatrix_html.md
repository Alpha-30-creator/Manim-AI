# ApplyMatrix [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html\#applymatrix "Link to this heading")

Qualified name: `manim.animation.transform.ApplyMatrix`

_class_ ApplyMatrix( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/transform.html#ApplyMatrix) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html#manim.animation.transform.ApplyMatrix "Link to this definition")

Bases: [`ApplyPointwiseFunction`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction "manim.animation.transform.ApplyPointwiseFunction")

Applies a matrix transform to an mobject.

Parameters:

- **matrix** ( _np.ndarray_) – The transformation matrix.

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **about\_point** ( _np.ndarray_) – The origin point for the transform. Defaults to `ORIGIN`.

- **kwargs** – Further keyword arguments that are passed to [`ApplyPointwiseFunction`](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction "manim.animation.transform.ApplyPointwiseFunction").


Examples

Example: ApplyMatrixExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html#applymatrixexample)

```
from manim import *

class ApplyMatrixExample(Scene):
    def construct(self):
        matrix = [[1, 1], [0, 2/3]]
        self.play(ApplyMatrix(matrix, Text("Hello World!")), ApplyMatrix(matrix, NumberPlane()))

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| `initialize_matrix` |  |

Attributes

|     |     |
| --- | --- |
| `path_arc` |  |
| `path_func` |  |
| `run_time` |  |

\_original\_\_init\_\_( _matrix_, _mobject_, _about\_point=array(\[0.,0.,0.\])_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html#manim.animation.transform.ApplyMatrix._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **matrix** ( _ndarray_)

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **about\_point** ( _ndarray_)


Return type:

None