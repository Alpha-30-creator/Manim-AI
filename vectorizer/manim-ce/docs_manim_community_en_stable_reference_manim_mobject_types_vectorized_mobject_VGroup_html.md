ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# VGroup [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html\#vgroup "Link to this heading")

Qualified name: `manim.mobject.types.vectorized\_mobject.VGroup`

_class_ VGroup( _\*vmobjects_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html#VGroup) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

A group of vectorized mobjects.

This can be used to group multiple [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") instances together
in order to scale, move, … them together.

Notes

When adding the same mobject more than once, repetitions are ignored.
Use [`Mobject.copy()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.copy "manim.mobject.mobject.Mobject.copy") to create a separate copy which can then
be added to the group.

Examples

To add `VGroup`, you can either use the
[`add()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup.add "manim.mobject.types.vectorized_mobject.VGroup.add") method, or use the + and += operators. Similarly, you
can subtract elements of a VGroup via `remove()` method, or
- and -= operators:

```
>>> from manim import Triangle, Square, VGroup
>>> vg = VGroup()
>>> triangle, square = Triangle(), Square()
>>> vg.add(triangle)
VGroup(Triangle)
>>> vg + square  # a new VGroup is constructed
VGroup(Triangle, Square)
>>> vg  # not modified
VGroup(Triangle)
>>> vg += square
>>> vg  # modifies vg
VGroup(Triangle, Square)
>>> vg.remove(triangle)
VGroup(Square)
>>> vg - square  # a new VGroup is constructed
VGroup()
>>> vg  # not modified
VGroup(Square)
>>> vg -= square
>>> vg  # modifies vg
VGroup()

```

Copy to clipboard

Example: ArcShapeIris [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#arcshapeiris)

![../_images/ArcShapeIris-1.png](https://docs.manim.community/en/stable/_images/ArcShapeIris-1.png)

```
from manim import *

class ArcShapeIris(Scene):
    def construct(self):
        colors = [DARK_BROWN, BLUE_E, BLUE_D, BLUE_A, TEAL_B, GREEN_B, YELLOW_E]
        radius = [1 + rad * 0.1 for rad in range(len(colors))]

        circles_group = VGroup()

        # zip(radius, color) makes the iterator [(radius[i], color[i]) for i in range(radius)]
        circles_group.add(*[Circle(radius=rad, stroke_width=10, color=col)\
                            for rad, col in zip(radius, colors)])
        self.add(circles_group)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`add`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup.add "manim.mobject.types.vectorized_mobject.VGroup.add") | Checks if all passed elements are an instance, or iterables of VMobject and then adds them to submobjects |

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

Parameters:

- **vmobjects** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ _Iterable_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_)

- **kwargs** ( _Any_)


\_original\_\_init\_\_( _\*vmobjects_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **vmobjects** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ _Iterable_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_)

- **kwargs** ( _Any_)


Return type:

None

add( _\*vmobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html#VGroup.add) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup.add "Link to this definition")

Checks if all passed elements are an instance, or iterables of VMobject and then adds them to submobjects

Parameters:

**vmobjects** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ _Iterable_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_) – List or iterable of VMobjects to add

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Raises:

**TypeError** – If one element of the list, or iterable is not an instance of VMobject

Examples

The following example shows how to add individual or multiple VMobject instances through the VGroup
constructor and its .add() method.

Example: AddToVGroup [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#addtovgroup)

```
from manim import *

class AddToVGroup(Scene):
    def construct(self):
        circle_red = Circle(color=RED)
        circle_green = Circle(color=GREEN)
        circle_blue = Circle(color=BLUE)
        circle_red.shift(LEFT)
        circle_blue.shift(RIGHT)
        gr = VGroup(circle_red, circle_green)
        gr2 = VGroup(circle_blue) # Constructor uses add directly
        self.add(gr,gr2)
        self.wait()
        gr += gr2 # Add group to another
        self.play(
            gr.animate.shift(DOWN),
        )
        gr -= gr2 # Remove group
        self.play( # Animate groups separately
            gr.animate.shift(LEFT),
            gr2.animate.shift(UP),
        )
        self.play( #Animate groups without modification
            (gr+gr2).animate.shift(RIGHT)
        )
        self.play( # Animate group without component
            (gr-circle_red).animate.shift(RIGHT)
        )

```

Copy to clipboard

Make interactive

A VGroup can be created using iterables as well. Keep in mind that all generated values from an
iterable must be an instance of VMobject. This is demonstrated below:

Example: AddIterableToVGroupExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#additerabletovgroupexample)

![../_images/AddIterableToVGroupExample-1.png](https://docs.manim.community/en/stable/_images/AddIterableToVGroupExample-1.png)

```
from manim import *

class AddIterableToVGroupExample(Scene):
    def construct(self):
        v = VGroup(
            Square(),               # Singular VMobject instance
            [Circle(), Triangle()], # List of VMobject instances
            Dot(),
            (Dot() for _ in range(2)), # Iterable that generates VMobjects
        )
        v.arrange()
        self.add(v)

```

Copy to clipboard

Make interactive

To facilitate this, the iterable is unpacked before its individual instances are added to the VGroup.
As a result, when you index a VGroup, you will never get back an iterable.
Instead, you will always receive VMobject instances, including those
that were part of the iterable/s that you originally added to the VGroup.