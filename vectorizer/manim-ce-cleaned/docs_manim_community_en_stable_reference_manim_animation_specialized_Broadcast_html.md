# Broadcast [¶](https://docs.manim.community/en/stable/reference/manim.animation.specialized.Broadcast.html\#broadcast "Link to this heading")

Qualified name: `manim.animation.specialized.Broadcast`

_class_ Broadcast( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/specialized.html#Broadcast) [¶](https://docs.manim.community/en/stable/reference/manim.animation.specialized.Broadcast.html#manim.animation.specialized.Broadcast "Link to this definition")

Bases: [`LaggedStart`](https://docs.manim.community/en/stable/reference/manim.animation.composition.LaggedStart.html#manim.animation.composition.LaggedStart "manim.animation.composition.LaggedStart")

Broadcast a mobject starting from an `initial_width`, up to the actual size of the mobject.

Parameters:

- **mobject** – The mobject to be broadcast.

- **focal\_point** ( _Sequence_ _\[_ _float_ _\]_) – The center of the broadcast, by default ORIGIN.

- **n\_mobs** ( _int_) – The number of mobjects that emerge from the focal point, by default 5.

- **initial\_opacity** ( _float_) – The starting stroke opacity of the mobjects emitted from the broadcast, by default 1.

- **final\_opacity** ( _float_) – The final stroke opacity of the mobjects emitted from the broadcast, by default 0.

- **initial\_width** ( _float_) – The initial width of the mobjects, by default 0.0.

- **remover** ( _bool_) – Whether the mobjects should be removed from the scene after the animation, by default True.

- **lag\_ratio** ( _float_) – The time between each iteration of the mobject, by default 0.2.

- **run\_time** ( _float_) – The total duration of the animation, by default 3.

- **kwargs** ( _Any_) – Additional arguments to be passed to [`LaggedStart`](https://docs.manim.community/en/stable/reference/manim.animation.composition.LaggedStart.html#manim.animation.composition.LaggedStart "manim.animation.composition.LaggedStart").


Examples

Example: BroadcastExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.specialized.Broadcast.html#broadcastexample)

```
from manim import *

class BroadcastExample(Scene):
    def construct(self):
        mob = Circle(radius=4, color=TEAL_A)
        self.play(Broadcast(mob))

```

Copy to clipboard

Make interactive

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _mobject_, _focal\_point=array(\[0.,0.,0.\])_, _n\_mobs=5_, _initial\_opacity=1_, _final\_opacity=0_, _initial\_width=0.0_, _remover=True_, _lag\_ratio=0.2_, _run\_time=3_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.specialized.Broadcast.html#manim.animation.specialized.Broadcast._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **focal\_point** ( _Sequence_ _\[_ _float_ _\]_)

- **n\_mobs** ( _int_)

- **initial\_opacity** ( _float_)

- **final\_opacity** ( _float_)

- **initial\_width** ( _float_)

- **remover** ( _bool_)

- **lag\_ratio** ( _float_)

- **run\_time** ( _float_)

- **kwargs** ( _Any_)