# Prism [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html\#prism "Link to this heading")

Qualified name: `manim.mobject.three\_d.three\_dimensions.Prism`

_class_ Prism( _dimensions=\[3,2,1\]_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Prism) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism "Link to this definition")

Bases: [`Cube`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cube.html#manim.mobject.three_d.three_dimensions.Cube "manim.mobject.three_d.three_dimensions.Cube")

A right rectangular prism (or rectangular cuboid).
Defined by the length of each side in `[x, y, z]` format.

Parameters:

**dimensions** ( _tuple_ _\[_ _float_ _,_ _float_ _,_ _float_ _\]_ _\|_ _np.ndarray_) – Dimensions of the [`Prism`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism "manim.mobject.three_d.three_dimensions.Prism") in `[x, y, z]` format.

Examples

Example: ExamplePrism [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#exampleprism)

![../_images/ExamplePrism-1.png](https://docs.manim.community/en/stable/_images/ExamplePrism-1.png)

```
from manim import *

class ExamplePrism(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES)
        prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
        prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
        self.add(prismSmall, prismLarge)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`generate_points`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism.generate_points "manim.mobject.three_d.three_dimensions.Prism.generate_points") | Creates the sides of the [`Prism`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism "manim.mobject.three_d.three_dimensions.Prism"). |

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

\_original\_\_init\_\_( _dimensions=\[3,2,1\]_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

**dimensions** ( _tuple_ _\[_ _float_ _,_ _float_ _,_ _float_ _\]_ _\|_ _ndarray_)

Return type:

None

generate\_points() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/three_d/three_dimensions.html#Prism.generate_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism.generate_points "Link to this definition")

Creates the sides of the [`Prism`](https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html#manim.mobject.three_d.three_dimensions.Prism "manim.mobject.three_d.three_dimensions.Prism").

Return type:

None

[**The AI Agent that gets your codebase** Copilot & Cursor letting you down? Try Augment. **Install Now**](https://server.ethicalads.io/proxy/click/8458/019600e1-a464-71e2-baac-eb6a5afe0fb4/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8458/019600e1-a464-71e2-baac-eb6a5afe0fb4/)