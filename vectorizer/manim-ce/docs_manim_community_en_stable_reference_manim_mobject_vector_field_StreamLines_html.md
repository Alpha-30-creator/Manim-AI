ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# StreamLines [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html\#streamlines "Link to this heading")

Qualified name: `manim.mobject.vector\_field.StreamLines`

_class_ StreamLines( _func_, _color=None_, _color\_scheme=None_, _min\_color\_scheme\_value=0_, _max\_color\_scheme\_value=2_, _colors=\[ManimColor('#236B8E'),ManimColor('#83C167'),ManimColor('#FFFF00'),ManimColor('#FC6255')\]_, _x\_range=None_, _y\_range=None_, _z\_range=None_, _three\_dimensions=False_, _noise\_factor=None_, _n\_repeats=1_, _dt=0.05_, _virtual\_time=3_, _max\_anchors\_per\_line=100_, _padding=3_, _stroke\_width=1_, _opacity=1_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#StreamLines) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#manim.mobject.vector_field.StreamLines "Link to this definition")

Bases: [`VectorField`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField")

StreamLines represent the flow of a [`VectorField`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.VectorField.html#manim.mobject.vector_field.VectorField "manim.mobject.vector_field.VectorField") using the trace of moving agents.

Vector fields are always based on a function defining the vector at every position.
The values of this functions is displayed by moving many agents along the vector field
and showing their trace.

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

- **noise\_factor** ( _float_ _\|_ _None_) – The amount by which the starting position of each agent is altered along each axis. Defaults to `delta_y / 2` if not defined.

- **n\_repeats** – The number of agents generated at each starting point.

- **dt** – The factor by which the distance an agent moves per step is stretched. Lower values result in a better approximation of the trajectories in the vector field.

- **virtual\_time** – The time the agents get to move in the vector field. Higher values therefore result in longer stream lines. However, this whole time gets simulated upon creation.

- **max\_anchors\_per\_line** – The maximum number of anchors per line. Lines with more anchors get reduced in complexity, not in length.

- **padding** – The distance agents can move out of the generation area before being terminated.

- **stroke\_width** – The stroke with of the stream lines.

- **opacity** – The opacity of the stream lines.


Examples

Example: BasicUsage [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#basicusage)

![../_images/BasicUsage-2.png](https://docs.manim.community/en/stable/_images/BasicUsage-2.png)

```
from manim import *

class BasicUsage(Scene):
    def construct(self):
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        self.add(StreamLines(func))

```

Copy to clipboard

Make interactive

Example: SpawningAndFlowingArea [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#spawningandflowingarea)

![../_images/SpawningAndFlowingArea-1.png](https://docs.manim.community/en/stable/_images/SpawningAndFlowingArea-1.png)

```
from manim import *

class SpawningAndFlowingArea(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0]) * UR + np.cos(pos[1]) * LEFT + pos / 5
        stream_lines = StreamLines(
            func, x_range=[-3, 3, 0.2], y_range=[-2, 2, 0.2], padding=1
        )

        spawning_area = Rectangle(width=6, height=4)
        flowing_area = Rectangle(width=8, height=6)
        labels = [Tex("Spawning Area"), Tex("Flowing Area").shift(DOWN * 2.5)]
        for lbl in labels:
            lbl.add_background_rectangle(opacity=0.6, buff=0.05)

        self.add(stream_lines, spawning_area, flowing_area, *labels)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`create`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#manim.mobject.vector_field.StreamLines.create "manim.mobject.vector_field.StreamLines.create") | The creation animation of the stream lines. |
| [`end_animation`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#manim.mobject.vector_field.StreamLines.end_animation "manim.mobject.vector_field.StreamLines.end_animation") | End the stream line animation smoothly. |
| [`start_animation`](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#manim.mobject.vector_field.StreamLines.start_animation "manim.mobject.vector_field.StreamLines.start_animation") | Animates the stream lines using an updater. |

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

\_original\_\_init\_\_( _func_, _color=None_, _color\_scheme=None_, _min\_color\_scheme\_value=0_, _max\_color\_scheme\_value=2_, _colors=\[ManimColor('#236B8E'),ManimColor('#83C167'),ManimColor('#FFFF00'),ManimColor('#FC6255')\]_, _x\_range=None_, _y\_range=None_, _z\_range=None_, _three\_dimensions=False_, _noise\_factor=None_, _n\_repeats=1_, _dt=0.05_, _virtual\_time=3_, _max\_anchors\_per\_line=100_, _padding=3_, _stroke\_width=1_, _opacity=1_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#manim.mobject.vector_field.StreamLines._original__init__ "Link to this definition")

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

- **noise\_factor** ( _float_ _\|_ _None_)


create( _lag\_ratio=None_, _run\_time=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#StreamLines.create) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#manim.mobject.vector_field.StreamLines.create "Link to this definition")

The creation animation of the stream lines.

The stream lines appear in random order.

Parameters:

- **lag\_ratio** ( _float_ _\|_ _None_) – The lag ratio of the animation.
If undefined, it will be selected so that the total animation length is 1.5 times the run time of each stream line creation.

- **run\_time** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_ _\|_ _None_) – The run time of every single stream line creation. The runtime of the whole animation might be longer due to the lag\_ratio.
If undefined, the virtual time of the stream lines is used as run time.


Returns:

The creation animation of the stream lines.

Return type:

[`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

Examples

Example: StreamLineCreation [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#streamlinecreation)

```
from manim import *

class StreamLineCreation(Scene):
    def construct(self):
        func = lambda pos: (pos[0] * UR + pos[1] * LEFT) - pos
        stream_lines = StreamLines(
            func,
            color=YELLOW,
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            stroke_width=3,
            virtual_time=1,  # use shorter lines
            max_anchors_per_line=5,  # better performance with fewer anchors
        )
        self.play(stream_lines.create())  # uses virtual_time as run_time
        self.wait()

```

Copy to clipboard

Make interactive

end\_animation() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#StreamLines.end_animation) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#manim.mobject.vector_field.StreamLines.end_animation "Link to this definition")

End the stream line animation smoothly.

Returns an animation resulting in fully displayed stream lines without a noticeable cut.

Returns:

The animation fading out the running stream animation.

Return type:

[`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

Raises:

**ValueError** – if no stream line animation is running

Examples

Example: EndAnimation [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#endanimation)

```
from manim import *

class EndAnimation(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(
            func, stroke_width=3, max_anchors_per_line=5, virtual_time=1, color=BLUE
        )
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5, time_width=0.5)
        self.wait(1)
        self.play(stream_lines.end_animation())

```

Copy to clipboard

Make interactive

start\_animation( _warm\_up=True_, _flow\_speed=1_, _time\_width=0.3_, _rate\_func=<functionlinear>_, _line\_animation\_class=<class'manim.animation.indication.ShowPassingFlash'>_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/vector_field.html#StreamLines.start_animation) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#manim.mobject.vector_field.StreamLines.start_animation "Link to this definition")

Animates the stream lines using an updater.

The stream lines will continuously flow

Parameters:

- **warm\_up** ( _bool_) – If True the animation is initialized line by line. Otherwise it starts with all lines shown.

- **flow\_speed** ( _float_) – At flow\_speed=1 the distance the flow moves per second is equal to the magnitude of the vector field along its path. The speed value scales the speed of this flow.

- **time\_width** ( _float_) – The proportion of the stream line shown while being animated

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_) – The rate function of each stream line flashing

- **line\_animation\_class** ( _type_ _\[_ [_ShowPassingFlash_](https://docs.manim.community/en/stable/reference/manim.animation.indication.ShowPassingFlash.html#manim.animation.indication.ShowPassingFlash "manim.animation.indication.ShowPassingFlash") _\]_) – The animation class being used


Return type:

None

Examples

Example: ContinuousMotion [¶](https://docs.manim.community/en/stable/reference/manim.mobject.vector_field.StreamLines.html#continuousmotion)

```
from manim import *

class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

```

Copy to clipboard

Make interactive