ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Scene [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html\#scene "Link to this heading")

Qualified name: `manim.scene.scene.Scene`

_class_ Scene( _renderer=None_, _camera\_class=<class'manim.camera.camera.Camera'>_, _always\_update\_mobjects=False_, _random\_seed=None_, _skip\_animations=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "Link to this definition")

Bases: `object`

A Scene is the canvas of your animation.

The primary role of [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") is to provide the user with tools to manage
mobjects and animations. Generally speaking, a manim script consists of a class
that derives from [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") whose [`Scene.construct()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct") method is overridden
by the user’s code.

Mobjects are displayed on screen by calling [`Scene.add()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") and removed from
screen by calling [`Scene.remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove"). All mobjects currently on screen are kept
in `Scene.mobjects`. Animations are played by calling [`Scene.play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play").

A [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") is rendered internally by calling [`Scene.render()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.render "manim.scene.scene.Scene.render"). This in
turn calls [`Scene.setup()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.setup "manim.scene.scene.Scene.setup"), [`Scene.construct()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct"), and
[`Scene.tear_down()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.tear_down "manim.scene.scene.Scene.tear_down"), in that order.

It is not recommended to override the `__init__` method in user Scenes. For code
that should be ran before a Scene is rendered, use [`Scene.setup()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.setup "manim.scene.scene.Scene.setup") instead.

Examples

Override the [`Scene.construct()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct") method with your code.

```
class MyScene(Scene):
    def construct(self):
        self.play(Write(Text("Hello World!")))

```

Copy to clipboard

Methods

|     |     |
| --- | --- |
| [`add`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") | Mobjects will be displayed, from background to foreground in the order with which they are added. |
| [`add_foreground_mobject`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_foreground_mobject "manim.scene.scene.Scene.add_foreground_mobject") | Adds a single mobject to the foreground, and internally to the list foreground\_mobjects, and mobjects. |
| [`add_foreground_mobjects`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_foreground_mobjects "manim.scene.scene.Scene.add_foreground_mobjects") | Adds mobjects to the foreground, and internally to the list foreground\_mobjects, and mobjects. |
| `add_mobjects_from_animations` |  |
| [`add_sound`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_sound "manim.scene.scene.Scene.add_sound") | This method is used to add a sound to the animation. |
| [`add_subcaption`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_subcaption "manim.scene.scene.Scene.add_subcaption") | Adds an entry in the corresponding subcaption file at the current time stamp. |
| [`add_updater`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_updater "manim.scene.scene.Scene.add_updater") | Add an update function to the scene. |
| [`begin_animations`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.begin_animations "manim.scene.scene.Scene.begin_animations") | Start the animations of the scene. |
| [`bring_to_back`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.bring_to_back "manim.scene.scene.Scene.bring_to_back") | Removes the mobject from the scene and adds them to the back of the scene. |
| [`bring_to_front`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.bring_to_front "manim.scene.scene.Scene.bring_to_front") | Adds the passed mobjects to the scene again, pushing them to he front of the scene. |
| `check_interactive_embed_is_valid` |  |
| [`clear`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.clear "manim.scene.scene.Scene.clear") | Removes all mobjects present in self.mobjects and self.foreground\_mobjects from the scene. |
| [`compile_animation_data`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.compile_animation_data "manim.scene.scene.Scene.compile_animation_data") | Given a list of animations, compile the corresponding static and moving mobjects, and gather the animation durations. |
| [`compile_animations`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.compile_animations "manim.scene.scene.Scene.compile_animations") | Creates \_MethodAnimations from any \_AnimationBuilders and updates animation kwargs with kwargs passed to play(). |
| [`construct`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct") | Add content to the Scene. |
| `embed` |  |
| [`get_attrs`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_attrs "manim.scene.scene.Scene.get_attrs") | Gets attributes of a scene given the attribute's identifier/name. |
| [`get_mobject_family_members`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_mobject_family_members "manim.scene.scene.Scene.get_mobject_family_members") | Returns list of family-members of all mobjects in scene. |
| `get_moving_and_static_mobjects` |  |
| [`get_moving_mobjects`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_moving_mobjects "manim.scene.scene.Scene.get_moving_mobjects") | Gets all moving mobjects in the passed animation(s). |
| [`get_restructured_mobject_list`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_restructured_mobject_list "manim.scene.scene.Scene.get_restructured_mobject_list") | Given a list of mobjects and a list of mobjects to be removed, this filters out the removable mobjects from the list of mobjects. |
| [`get_run_time`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_run_time "manim.scene.scene.Scene.get_run_time") | Gets the total run time for a list of animations. |
| [`get_time_progression`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_time_progression "manim.scene.scene.Scene.get_time_progression") | You will hardly use this when making your own animations. |
| [`get_top_level_mobjects`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_top_level_mobjects "manim.scene.scene.Scene.get_top_level_mobjects") | Returns all mobjects which are not submobjects. |
| `interact` |  |
| [`interactive_embed`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.interactive_embed "manim.scene.scene.Scene.interactive_embed") | Like embed(), but allows for screen interaction. |
| [`is_current_animation_frozen_frame`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.is_current_animation_frozen_frame "manim.scene.scene.Scene.is_current_animation_frozen_frame") | Returns whether the current animation produces a static frame (generally a Wait). |
| `mouse_drag_orbit_controls` |  |
| `mouse_scroll_orbit_controls` |  |
| [`next_section`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.next_section "manim.scene.scene.Scene.next_section") | Create separation here; the last section gets finished and a new one gets created. |
| `on_key_press` |  |
| `on_key_release` |  |
| `on_mouse_drag` |  |
| `on_mouse_motion` |  |
| `on_mouse_press` |  |
| `on_mouse_scroll` |  |
| [`pause`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.pause "manim.scene.scene.Scene.pause") | Pauses the scene (i.e., displays a frozen frame). |
| [`play`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") | Plays an animation in this scene. |
| [`play_internal`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play_internal "manim.scene.scene.Scene.play_internal") | This method is used to prep the animations for rendering, apply the arguments and parameters required to them, render them, and write them to the video file. |
| [`remove`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") | Removes mobjects in the passed list of mobjects from the scene and the foreground, by removing them from "mobjects" and "foreground\_mobjects" |
| [`remove_foreground_mobject`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove_foreground_mobject "manim.scene.scene.Scene.remove_foreground_mobject") | Removes a single mobject from the foreground, and internally from the list foreground\_mobjects. |
| [`remove_foreground_mobjects`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove_foreground_mobjects "manim.scene.scene.Scene.remove_foreground_mobjects") | Removes mobjects from the foreground, and internally from the list foreground\_mobjects. |
| [`remove_updater`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove_updater "manim.scene.scene.Scene.remove_updater") | Remove an update function from the scene. |
| [`render`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.render "manim.scene.scene.Scene.render") | Renders this Scene. |
| [`replace`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.replace "manim.scene.scene.Scene.replace") | Replace one mobject in the scene with another, preserving draw order. |
| [`restructure_mobjects`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.restructure_mobjects "manim.scene.scene.Scene.restructure_mobjects") | tl:wr |
| `set_key_function` |  |
| [`setup`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.setup "manim.scene.scene.Scene.setup") | This is meant to be implemented by any scenes which are commonly subclassed, and have some common setup involved before the construct method is called. |
| [`should_update_mobjects`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.should_update_mobjects "manim.scene.scene.Scene.should_update_mobjects") | Returns True if the mobjects of this scene should be updated. |
| [`tear_down`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.tear_down "manim.scene.scene.Scene.tear_down") | This is meant to be implemented by any scenes which are commonly subclassed, and have some common method to be invoked before the scene ends. |
| `update_meshes` |  |
| [`update_mobjects`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.update_mobjects "manim.scene.scene.Scene.update_mobjects") | Begins updating all mobjects in the Scene. |
| [`update_self`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.update_self "manim.scene.scene.Scene.update_self") | Run all scene updater functions. |
| `update_to_time` |  |
| `validate_run_time` |  |
| [`wait`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait "manim.scene.scene.Scene.wait") | Plays a "no operation" animation. |
| [`wait_until`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait_until "manim.scene.scene.Scene.wait_until") | Wait until a condition is satisfied, up to a given maximum duration. |

Attributes

|     |     |
| --- | --- |
| `camera` |  |
| [`time`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.time "manim.scene.scene.Scene.time") | The time since the start of the scene. |

Parameters:

- **renderer** ( _CairoRenderer_ _\|_ _OpenGLRenderer_ _\|_ _None_)

- **camera\_class** ( _type_ _\[_ [_Camera_](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera") _\]_)

- **always\_update\_mobjects** ( _bool_)

- **random\_seed** ( _int_ _\|_ _None_)

- **skip\_animations** ( _bool_)


\_get\_animation\_time\_progression( _animations_, _duration_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene._get_animation_time_progression) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene._get_animation_time_progression "Link to this definition")

You will hardly use this when making your own animations.
This method is for Manim’s internal use.

Uses `get_time_progression()` to obtain a
CommandLine ProgressBar whose `fill_time` is
dependent on the qualities of the passed Animation,

Parameters:

- **animations** ( _list_ _\[_ [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\]_) – The list of animations to get
the time progression for.

- **duration** ( _float_) – duration of wait time


Returns:

The CommandLine Progress Bar.

Return type:

time\_progression

add( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.add) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "Link to this definition")

Mobjects will be displayed, from background to
foreground in the order with which they are added.

Parameters:

**\*mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – Mobjects to add.

Returns:

The same scene after adding the Mobjects in.

Return type:

[Scene](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")

add\_foreground\_mobject( _mobject_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.add_foreground_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_foreground_mobject "Link to this definition")

Adds a single mobject to the foreground, and internally to the list
foreground\_mobjects, and mobjects.

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The Mobject to add to the foreground.

Returns:

The Scene, with the foreground mobject added.

Return type:

[Scene](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")

add\_foreground\_mobjects( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.add_foreground_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_foreground_mobjects "Link to this definition")

Adds mobjects to the foreground, and internally to the list
foreground\_mobjects, and mobjects.

Parameters:

**\*mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The Mobjects to add to the foreground.

Returns:

The Scene, with the foreground mobjects added.

Return type:

[Scene](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")

add\_sound( _sound\_file_, _time\_offset=0_, _gain=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.add_sound) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_sound "Link to this definition")

This method is used to add a sound to the animation.

Parameters:

- **sound\_file** ( _str_) – The path to the sound file.

- **time\_offset** ( _float_) – The offset in the sound file after which
the sound can be played.

- **gain** ( _float_ _\|_ _None_) – Amplification of the sound.


Examples

Example: SoundExample [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#soundexample)

```
from manim import *

class SoundExample(Scene):
    # Source of sound under Creative Commons 0 License. https://freesound.org/people/Druminfected/sounds/250551/
    def construct(self):
        dot = Dot().set_color(GREEN)
        self.add_sound("click.wav")
        self.add(dot)
        self.wait()
        self.add_sound("click.wav")
        dot.set_color(BLUE)
        self.wait()
        self.add_sound("click.wav")
        dot.set_color(RED)
        self.wait()

```

Copy to clipboard

Make interactive

Download the resource for the previous example [here](https://github.com/ManimCommunity/manim/blob/main/docs/source/_static/click.wav) .

add\_subcaption( _content_, _duration=1_, _offset=0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.add_subcaption) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_subcaption "Link to this definition")

Adds an entry in the corresponding subcaption file
at the current time stamp.

The current time stamp is obtained from `Scene.time`.

Parameters:

- **content** ( _str_) – The subcaption content.

- **duration** ( _float_) – The duration (in seconds) for which the subcaption is shown.

- **offset** ( _float_) – This offset (in seconds) is added to the starting time stamp
of the subcaption.


Return type:

None

Examples

This example illustrates both possibilities for adding
subcaptions to Manimations:

```
class SubcaptionExample(Scene):
    def construct(self):
        square = Square()
        circle = Circle()

        # first option: via the add_subcaption method
        self.add_subcaption("Hello square!", duration=1)
        self.play(Create(square))

        # second option: within the call to Scene.play
        self.play(
            Transform(square, circle), subcaption="The square transforms."
        )

```

Copy to clipboard

add\_updater( _func_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.add_updater) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_updater "Link to this definition")

Add an update function to the scene.

The scene updater functions are run every frame,
and they are the last type of updaters to run.

Warning

When using the Cairo renderer, scene updaters that
modify mobjects are not detected in the same way
that mobject updaters are. To be more concrete,
a mobject only modified via a scene updater will
not necessarily be added to the list of _moving_
_mobjects_ and thus might not be updated every frame.

TL;DR: Use mobject updaters to update mobjects.

Parameters:

**func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _None_ _\]_) – The updater function. It takes a float, which is the
time difference since the last update (usually equal
to the frame rate).

Return type:

None

See also

[`Scene.remove_updater()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove_updater "manim.scene.scene.Scene.remove_updater"), [`Scene.update_self()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.update_self "manim.scene.scene.Scene.update_self")

begin\_animations() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.begin_animations) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.begin_animations "Link to this definition")

Start the animations of the scene.

Return type:

None

bring\_to\_back( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.bring_to_back) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.bring_to_back "Link to this definition")

Removes the mobject from the scene and
adds them to the back of the scene.

Parameters:

**\*mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject(s) to push to the back of the scene.

Returns:

The Scene, with the mobjects pushed to the back
of the scene.

Return type:

[Scene](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")

bring\_to\_front( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.bring_to_front) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.bring_to_front "Link to this definition")

Adds the passed mobjects to the scene again,
pushing them to he front of the scene.

Parameters:

**\*mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject(s) to bring to the front of the scene.

Returns:

The Scene, with the mobjects brought to the front
of the scene.

Return type:

[Scene](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")

clear() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.clear) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.clear "Link to this definition")

Removes all mobjects present in self.mobjects
and self.foreground\_mobjects from the scene.

Returns:

The Scene, with all of its mobjects in
self.mobjects and self.foreground\_mobjects
removed.

Return type:

[Scene](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")

compile\_animation\_data( _\*animations_, _\*\*play\_kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.compile_animation_data) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.compile_animation_data "Link to this definition")

Given a list of animations, compile the corresponding
static and moving mobjects, and gather the animation durations.

This also begins the animations.

Parameters:

- **animations** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\|_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\|_ _\_AnimationBuilder_) – Animation or mobject with mobject method and params

- **play\_kwargs** – Named parameters affecting what was passed in `animations`,
e.g. `run_time`, `lag_ratio` and so on.


Returns:

None if there is nothing to play, or self otherwise.

Return type:

self, None

compile\_animations( _\*args_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.compile_animations) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.compile_animations "Link to this definition")

Creates \_MethodAnimations from any \_AnimationBuilders and updates animation
kwargs with kwargs passed to play().

Parameters:

- **\*args** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\|_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\|_ _\_AnimationBuilder_) – Animations to be played.

- **\*\*kwargs** – Configuration for the call to play().


Returns:

Animations to be played.

Return type:

Tuple\[ `Animation`\]

construct() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.construct) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "Link to this definition")

Add content to the Scene.

From within [`Scene.construct()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct"), display mobjects on screen by calling
[`Scene.add()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") and remove them from screen by calling [`Scene.remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove").
All mobjects currently on screen are kept in `Scene.mobjects`. Play
animations by calling [`Scene.play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play").

Notes

Initialization code should go in [`Scene.setup()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.setup "manim.scene.scene.Scene.setup"). Termination code should
go in [`Scene.tear_down()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.tear_down "manim.scene.scene.Scene.tear_down").

Examples

A typical manim script includes a class derived from [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") with an
overridden [`Scene.construct()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.construct "manim.scene.scene.Scene.construct") method:

```
class MyScene(Scene):
    def construct(self):
        self.play(Write(Text("Hello World!")))

```

Copy to clipboard

See also

[`Scene.setup()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.setup "manim.scene.scene.Scene.setup"), [`Scene.render()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.render "manim.scene.scene.Scene.render"), [`Scene.tear_down()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.tear_down "manim.scene.scene.Scene.tear_down")

get\_attrs( _\*keys_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.get_attrs) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_attrs "Link to this definition")

Gets attributes of a scene given the attribute’s identifier/name.

Parameters:

**\*keys** ( _str_) – Name(s) of the argument(s) to return the attribute of.

Returns:

List of attributes of the passed identifiers.

Return type:

list

get\_mobject\_family\_members() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.get_mobject_family_members) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_mobject_family_members "Link to this definition")

Returns list of family-members of all mobjects in scene.
If a Circle() and a VGroup(Rectangle(),Triangle()) were added,
it returns not only the Circle(), Rectangle() and Triangle(), but
also the VGroup() object.

Returns:

List of mobject family members.

Return type:

list

get\_moving\_mobjects( _\*animations_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.get_moving_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_moving_mobjects "Link to this definition")

Gets all moving mobjects in the passed animation(s).

Parameters:

**\*animations** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")) – The animations to check for moving mobjects.

Returns:

The list of mobjects that could be moving in
the Animation(s)

Return type:

list

get\_restructured\_mobject\_list( _mobjects_, _to\_remove_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.get_restructured_mobject_list) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_restructured_mobject_list "Link to this definition")

Given a list of mobjects and a list of mobjects to be removed, this
filters out the removable mobjects from the list of mobjects.

Parameters:

- **mobjects** ( _list_) – The Mobjects to check.

- **to\_remove** ( _list_) – The list of mobjects to remove.


Returns:

The list of mobjects with the mobjects to remove removed.

Return type:

list

get\_run\_time( _animations_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.get_run_time) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_run_time "Link to this definition")

Gets the total run time for a list of animations.

Parameters:

**animations** ( _list_ _\[_ [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\]_) – A list of the animations whose total
`run_time` is to be calculated.

Returns:

The total `run_time` of all of the animations in the list.

Return type:

float

get\_time\_progression( _run\_time_, _description_, _n\_iterations=None_, _override\_skip\_animations=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.get_time_progression) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_time_progression "Link to this definition")

You will hardly use this when making your own animations.
This method is for Manim’s internal use.

Returns a CommandLine ProgressBar whose `fill_time`
is dependent on the `run_time` of an animation,
the iterations to perform in that animation
and a bool saying whether or not to consider
the skipped animations.

Parameters:

- **run\_time** ( _float_) – The `run_time` of the animation.

- **n\_iterations** ( _int_ _\|_ _None_) – The number of iterations in the animation.

- **override\_skip\_animations** ( _bool_) – Whether or not to show skipped animations in the progress bar.


Returns:

The CommandLine Progress Bar.

Return type:

time\_progression

get\_top\_level\_mobjects() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.get_top_level_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.get_top_level_mobjects "Link to this definition")

Returns all mobjects which are not submobjects.

Returns:

List of top level mobjects.

Return type:

list

interactive\_embed() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.interactive_embed) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.interactive_embed "Link to this definition")

Like embed(), but allows for screen interaction.

is\_current\_animation\_frozen\_frame() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.is_current_animation_frozen_frame) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.is_current_animation_frozen_frame "Link to this definition")

Returns whether the current animation produces a static frame (generally a Wait).

Return type:

bool

next\_section( _name='unnamed'_, _section\_type=DefaultSectionType.NORMAL_, _skip\_animations=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.next_section) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.next_section "Link to this definition")

Create separation here; the last section gets finished and a new one gets created.
`skip_animations` skips the rendering of all animations in this section.
Refer to [the documentation](https://docs.manim.community/en/stable/tutorials/output_and_config.html) on how to use sections.

Parameters:

- **name** ( _str_)

- **section\_type** ( _str_)

- **skip\_animations** ( _bool_)


Return type:

None

pause( _duration=1.0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.pause) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.pause "Link to this definition")

Pauses the scene (i.e., displays a frozen frame).

This is an alias for [`wait()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait "manim.scene.scene.Scene.wait") with `frozen_frame`
set to `True`.

Parameters:

**duration** ( _float_) – The duration of the pause.

See also

[`wait()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait "manim.scene.scene.Scene.wait"), [`Wait`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait "manim.animation.animation.Wait")

play( _\*args_, _subcaption=None_, _subcaption\_duration=None_, _subcaption\_offset=0_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.play) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "Link to this definition")

Plays an animation in this scene.

Parameters:

- **args** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\|_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\|_ _\_AnimationBuilder_) – Animations to be played.

- **subcaption** – The content of the external subcaption that should
be added during the animation.

- **subcaption\_duration** – The duration for which the specified subcaption is
added. If `None` (the default), the run time of the
animation is taken.

- **subcaption\_offset** – An offset (in seconds) for the start time of the
added subcaption.

- **kwargs** – All other keywords are passed to the renderer.


play\_internal( _skip\_rendering=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.play_internal) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play_internal "Link to this definition")

This method is used to prep the animations for rendering,
apply the arguments and parameters required to them,
render them, and write them to the video file.

Parameters:

**skip\_rendering** ( _bool_) – Whether the rendering should be skipped, by default False

remove( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.remove) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "Link to this definition")

Removes mobjects in the passed list of mobjects
from the scene and the foreground, by removing them
from “mobjects” and “foreground\_mobjects”

Parameters:

**\*mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to remove.

remove\_foreground\_mobject( _mobject_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.remove_foreground_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove_foreground_mobject "Link to this definition")

Removes a single mobject from the foreground, and internally from the list
foreground\_mobjects.

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to remove from the foreground.

Returns:

The Scene, with the foreground mobject removed.

Return type:

[Scene](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")

remove\_foreground\_mobjects( _\*to\_remove_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.remove_foreground_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove_foreground_mobjects "Link to this definition")

Removes mobjects from the foreground, and internally from the list
foreground\_mobjects.

Parameters:

**\*to\_remove** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject(s) to remove from the foreground.

Returns:

The Scene, with the foreground mobjects removed.

Return type:

[Scene](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")

remove\_updater( _func_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.remove_updater) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove_updater "Link to this definition")

Remove an update function from the scene.

Parameters:

**func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _None_ _\]_) – The updater function to be removed.

Return type:

None

See also

[`Scene.add_updater()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_updater "manim.scene.scene.Scene.add_updater"), [`Scene.update_self()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.update_self "manim.scene.scene.Scene.update_self")

render( _preview=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.render) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.render "Link to this definition")

Renders this Scene.

Parameters:

**preview** ( _bool_) – If true, opens scene in a file viewer.

replace( _old\_mobject_, _new\_mobject_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.replace) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.replace "Link to this definition")

Replace one mobject in the scene with another, preserving draw order.

If `old_mobject` is a submobject of some other Mobject (e.g. a
[`Group`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")), the new\_mobject will replace it inside the group,
without otherwise changing the parent mobject.

Parameters:

- **old\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be replaced. Must be present in the scene.

- **new\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – A mobject which must not already be in the scene.


Return type:

None

restructure\_mobjects( _to\_remove_, _mobject\_list\_name='mobjects'_, _extract\_families=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.restructure_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.restructure_mobjects "Link to this definition")tl:wr

If your scene has a Group(), and you removed a mobject from the Group,
this dissolves the group and puts the rest of the mobjects directly
in self.mobjects or self.foreground\_mobjects.

In cases where the scene contains a group, e.g. Group(m1, m2, m3), but one
of its submobjects is removed, e.g. scene.remove(m1), the list of mobjects
will be edited to contain other submobjects, but not m1, e.g. it will now
insert m2 and m3 to where the group once was.

Parameters:

- **to\_remove** ( _Sequence_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – The Mobject to remove.

- **mobject\_list\_name** ( _str_) – The list of mobjects (“mobjects”, “foreground\_mobjects” etc) to remove from.

- **extract\_families** ( _bool_) – Whether the mobject’s families should be recursively extracted.


Returns:

The Scene mobject with restructured Mobjects.

Return type:

[Scene](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")

setup() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.setup) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.setup "Link to this definition")

This is meant to be implemented by any scenes which
are commonly subclassed, and have some common setup
involved before the construct method is called.

should\_update\_mobjects() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.should_update_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.should_update_mobjects "Link to this definition")

Returns True if the mobjects of this scene should be updated.

In particular, this checks whether

- the `always_update_mobjects` attribute of [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")
is set to `True`,

- the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") itself has time-based updaters attached,

- any mobject in this [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") has time-based updaters attached.


This is only called when a single Wait animation is played.

Return type:

bool

tear\_down() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.tear_down) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.tear_down "Link to this definition")

This is meant to be implemented by any scenes which
are commonly subclassed, and have some common method
to be invoked before the scene ends.

_property_ time _:float_ [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.time "Link to this definition")

The time since the start of the scene.

update\_mobjects( _dt_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.update_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.update_mobjects "Link to this definition")

Begins updating all mobjects in the Scene.

Parameters:

**dt** ( _float_) – Change in time between updates. Defaults (mostly) to 1/frames\_per\_second

update\_self( _dt_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.update_self) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.update_self "Link to this definition")

Run all scene updater functions.

Among all types of update functions (mobject updaters, mesh updaters,
scene updaters), scene update functions are called last.

Parameters:

**dt** ( _float_) – Scene time since last update.

See also

[`Scene.add_updater()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.add_updater "manim.scene.scene.Scene.add_updater"), [`Scene.remove_updater()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove_updater "manim.scene.scene.Scene.remove_updater")

wait( _duration=1.0_, _stop\_condition=None_, _frozen\_frame=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.wait) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait "Link to this definition")

Plays a “no operation” animation.

Parameters:

- **duration** ( _float_) – The run time of the animation.

- **stop\_condition** ( _Callable_ _\[_ _\[_ _\]_ _,_ _bool_ _\]_ _\|_ _None_) – A function without positional arguments that is evaluated every time
a frame is rendered. The animation only stops when the return value
of the function is truthy, or when the time specified in `duration`
passes.

- **frozen\_frame** ( _bool_ _\|_ _None_) – If True, updater functions are not evaluated, and the animation outputs
a frozen frame. If False, updater functions are called and frames
are rendered as usual. If None (the default), the scene tries to
determine whether or not the frame is frozen on its own.


See also

[`Wait`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait "manim.animation.animation.Wait"), `should_mobjects_update()`

wait\_until( _stop\_condition_, _max\_time=60_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#Scene.wait_until) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.wait_until "Link to this definition")

Wait until a condition is satisfied, up to a given maximum duration.

Parameters:

- **stop\_condition** ( _Callable_ _\[_ _\[_ _\]_ _,_ _bool_ _\]_) – A function with no arguments that determines whether or not the
scene should keep waiting.

- **max\_time** ( _float_) – The maximum wait time in seconds.