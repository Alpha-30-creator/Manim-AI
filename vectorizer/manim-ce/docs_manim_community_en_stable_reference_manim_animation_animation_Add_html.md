ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Add [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html\#add "Link to this heading")

Qualified name: `manim.animation.animation.Add`

_class_ Add( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#Add) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

Add Mobjects to a scene, without animating them in any other way. This
is similar to the [`Scene.add()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") method, but [`Add`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add "manim.animation.animation.Add") is an
animation which can be grouped into other animations.

Parameters:

- **mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – One [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") or more to add to a scene.

- **run\_time** ( _float_) – The duration of the animation after adding the `mobjects`. Defaults
to 0, which means this is an instant animation without extra wait time
after adding them.

- **\*\*kwargs** ( _Any_) – Additional arguments to pass to the parent [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") class.


Examples

Example: DefaultAddScene [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#defaultaddscene)

```
from manim import *

class DefaultAddScene(Scene):
    def construct(self):
        text_1 = Text("I was added with Add!")
        text_2 = Text("Me too!")
        text_3 = Text("And me!")
        texts = VGroup(text_1, text_2, text_3).arrange(DOWN)
        rect = SurroundingRectangle(texts, buff=0.5)

        self.play(
            Create(rect, run_time=3.0),
            Succession(
                Wait(1.0),
                # You can Add a Mobject in the middle of an animation...
                Add(text_1),
                Wait(1.0),
                # ...or multiple Mobjects at once!
                Add(text_2, text_3),
            ),
        )
        self.wait()

```

Copy to clipboard

Make interactive

Example: AddWithRunTimeScene [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#addwithruntimescene)

```
from manim import *

class AddWithRunTimeScene(Scene):
    def construct(self):
        # A 5x5 grid of circles
        circles = VGroup(
            *[Circle(radius=0.5) for _ in range(25)]
        ).arrange_in_grid(5, 5)

        self.play(
            Succession(
                # Add a run_time of 0.2 to wait for 0.2 seconds after
                # adding the circle, instead of using Wait(0.2) after Add!
                *[Add(circle, run_time=0.2) for circle in circles],
                rate_func=smooth,
            )
        )
        self.wait()

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`begin`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add.begin "manim.animation.animation.Add.begin") | Begin the animation. |
| [`clean_up_from_scene`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add.clean_up_from_scene "manim.animation.animation.Add.clean_up_from_scene") | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
| [`finish`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add.finish "manim.animation.animation.Add.finish") | Finish the animation. |
| [`interpolate`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add.interpolate "manim.animation.animation.Add.interpolate") | Set the animation progress. |
| [`update_mobjects`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add.update_mobjects "manim.animation.animation.Add.update_mobjects") | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _\*mobjects_, _run\_time=0.0_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **run\_time** ( _float_)

- **kwargs** ( _Any_)


Return type:

None

begin() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#Add.begin) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add.begin "Link to this definition")

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

Return type:

None

clean\_up\_from\_scene( _scene_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#Add.clean_up_from_scene) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add.clean_up_from_scene "Link to this definition")

Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

Parameters:

**scene** ( [_Scene_](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

Return type:

None

finish() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#Add.finish) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add.finish "Link to this definition")

Finish the animation.

This method gets called when the animation is over.

Return type:

None

interpolate( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#Add.interpolate) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add.interpolate "Link to this definition")

Set the animation progress.

This method gets called for every frame during an animation.

Parameters:

**alpha** ( _float_) – The relative time to set the animation to, 0 meaning the start, 1 meaning
the end.

Return type:

None

update\_mobjects( _dt_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#Add.update_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add.update_mobjects "Link to this definition")

Updates things like starting\_mobject, and (for
Transforms) target\_mobject. Note, since typically
(always?) self.mobject will have its updating
suspended during the animation, this will do
nothing to self.mobject.

Parameters:

**dt** ( _float_)

Return type:

None