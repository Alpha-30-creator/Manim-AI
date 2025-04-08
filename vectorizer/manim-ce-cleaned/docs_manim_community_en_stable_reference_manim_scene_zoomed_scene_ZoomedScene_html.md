# ZoomedScene [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html\#zoomedscene "Link to this heading")

Qualified name: `manim.scene.zoomed\_scene.ZoomedScene`

_class_ ZoomedScene( _camera\_class=<class'manim.camera.multi\_camera.MultiCamera'>_, _zoomed\_display\_height=3_, _zoomed\_display\_width=3_, _zoomed\_display\_center=None_, _zoomed\_display\_corner=array(\[1._, _1._, _0.\])_, _zoomed\_display\_corner\_buff=0.5_, _zoomed\_camera\_config={'background\_opacity':1_, _'default\_frame\_stroke\_width':2}_, _zoomed\_camera\_image\_mobject\_config={}_, _zoomed\_camera\_frame\_starting\_position=array(\[0._, _0._, _0.\])_, _zoom\_factor=0.15_, _image\_frame\_stroke\_width=3_, _zoom\_activated=False_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html#ZoomedScene) [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene "Link to this definition")

Bases: [`MovingCameraScene`](https://docs.manim.community/en/stable/reference/manim.scene.moving_camera_scene.MovingCameraScene.html#manim.scene.moving_camera_scene.MovingCameraScene "manim.scene.moving_camera_scene.MovingCameraScene")

This is a Scene with special configurations made for when
a particular part of the scene must be zoomed in on and displayed
separately.

Methods

|     |     |
| --- | --- |
| [`activate_zooming`](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.activate_zooming "manim.scene.zoomed_scene.ZoomedScene.activate_zooming") | This method is used to activate the zooming for the zoomed\_camera. |
| [`get_zoom_factor`](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.get_zoom_factor "manim.scene.zoomed_scene.ZoomedScene.get_zoom_factor") | Returns the Zoom factor of the Zoomed camera. |
| [`get_zoom_in_animation`](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.get_zoom_in_animation "manim.scene.zoomed_scene.ZoomedScene.get_zoom_in_animation") | Returns the animation of camera zooming in. |
| [`get_zoomed_display_pop_out_animation`](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.get_zoomed_display_pop_out_animation "manim.scene.zoomed_scene.ZoomedScene.get_zoomed_display_pop_out_animation") | This is the animation of the popping out of the mini-display that shows the content of the zoomed camera. |
| [`setup`](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.setup "manim.scene.zoomed_scene.ZoomedScene.setup") | This method is used internally by Manim to setup the scene for proper use. |

Attributes

|     |     |
| --- | --- |
| `camera` |  |
| `time` | The time since the start of the scene. |

activate\_zooming( _animate=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html#ZoomedScene.activate_zooming) [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.activate_zooming "Link to this definition")

This method is used to activate the zooming for
the zoomed\_camera.

Parameters:

**animate** ( _bool_) – Whether or not to animate the activation
of the zoomed camera.

get\_zoom\_factor() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html#ZoomedScene.get_zoom_factor) [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.get_zoom_factor "Link to this definition")

Returns the Zoom factor of the Zoomed camera.
Defined as the ratio between the height of the
zoomed camera and the height of the zoomed mini
display.
:returns: The zoom factor.
:rtype: float

get\_zoom\_in\_animation( _run\_time=2_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html#ZoomedScene.get_zoom_in_animation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.get_zoom_in_animation "Link to this definition")

Returns the animation of camera zooming in.

Parameters:

- **run\_time** ( _float_) – The run\_time of the animation of the camera zooming in.

- **\*\*kwargs** – Any valid keyword arguments of ApplyMethod()


Returns:

The animation of the camera zooming in.

Return type:

[ApplyMethod](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

get\_zoomed\_display\_pop\_out\_animation( _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html#ZoomedScene.get_zoomed_display_pop_out_animation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.get_zoomed_display_pop_out_animation "Link to this definition")

This is the animation of the popping out of the
mini-display that shows the content of the zoomed
camera.

Returns:

The Animation of the Zoomed Display popping out.

Return type:

[ApplyMethod](https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

setup() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/zoomed_scene.html#ZoomedScene.setup) [¶](https://docs.manim.community/en/stable/reference/manim.scene.zoomed_scene.ZoomedScene.html#manim.scene.zoomed_scene.ZoomedScene.setup "Link to this definition")

This method is used internally by Manim to
setup the scene for proper use.

[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/8270/019600e6-29d6-77a3-a3a2-75f92aff2992/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8270/019600e6-29d6-77a3-a3a2-75f92aff2992/)