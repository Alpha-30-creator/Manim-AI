ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Wait [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html\#wait "Link to this heading")

Qualified name: `manim.animation.animation.Wait`

_class_ Wait( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#Wait) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait "Link to this definition")

Bases: [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

A “no operation” animation.

Parameters:

- **run\_time** ( _float_) – The amount of time that should pass.

- **stop\_condition** ( _Callable_ _\[_ _\[_ _\]_ _,_ _bool_ _\]_ _\|_ _None_) – A function without positional arguments that evaluates to a boolean.
The function is evaluated after every new frame has been rendered.
Playing the animation stops after the return value is truthy, or
after the specified `run_time` has passed.

- **frozen\_frame** ( _bool_ _\|_ _None_) – Controls whether or not the wait animation is static, i.e., corresponds
to a frozen frame. If `False` is passed, the render loop still
progresses through the animation as usual and (among other things)
continues to call updater functions. If `None` (the default value),
the [`Scene.play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") call tries to determine whether the Wait call
can be static or not itself via `Scene.should_mobjects_update()`.

- **kwargs** – Keyword arguments to be passed to the parent class, [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation").

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)


Methods

|     |     |
| --- | --- |
| [`begin`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait.begin "manim.animation.animation.Wait.begin") | Begin the animation. |
| [`clean_up_from_scene`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait.clean_up_from_scene "manim.animation.animation.Wait.clean_up_from_scene") | Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
| [`finish`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait.finish "manim.animation.animation.Wait.finish") | Finish the animation. |
| [`interpolate`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait.interpolate "manim.animation.animation.Wait.interpolate") | Set the animation progress. |
| [`update_mobjects`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait.update_mobjects "manim.animation.animation.Wait.update_mobjects") | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _run\_time=1_, _stop\_condition=None_, _frozen\_frame=None_, _rate\_func=<functionlinear>_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **run\_time** ( _float_)

- **stop\_condition** ( _Callable_ _\[_ _\[_ _\]_ _,_ _bool_ _\]_ _\|_ _None_)

- **frozen\_frame** ( _bool_ _\|_ _None_)

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)


begin() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#Wait.begin) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait.begin "Link to this definition")

Begin the animation.

This method is called right as an animation is being played. As much
initialization as possible, especially any mobject copying, should live in this
method.

Return type:

None

clean\_up\_from\_scene( _scene_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#Wait.clean_up_from_scene) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait.clean_up_from_scene "Link to this definition")

Clean up the [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

This includes to [`remove()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

Parameters:

**scene** ( [_Scene_](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

Return type:

None

finish() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#Wait.finish) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait.finish "Link to this definition")

Finish the animation.

This method gets called when the animation is over.

Return type:

None

interpolate( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#Wait.interpolate) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait.interpolate "Link to this definition")

Set the animation progress.

This method gets called for every frame during an animation.

Parameters:

**alpha** ( _float_) – The relative time to set the animation to, 0 meaning the start, 1 meaning
the end.

Return type:

None

update\_mobjects( _dt_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#Wait.update_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait.update_mobjects "Link to this definition")

Updates things like starting\_mobject, and (for
Transforms) target\_mobject. Note, since typically
(always?) self.mobject will have its updating
suspended during the animation, this will do
nothing to self.mobject.

Parameters:

**dt** ( _float_)

Return type:

None

[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/8270/019600eb-d9df-7df0-80b9-09c5a36512ee/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8270/019600eb-d9df-7df0-80b9-09c5a36512ee/)