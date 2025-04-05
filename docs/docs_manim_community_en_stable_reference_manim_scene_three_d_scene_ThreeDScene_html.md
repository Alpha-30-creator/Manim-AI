ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ThreeDScene [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html\#threedscene "Link to this heading")

Qualified name: `manim.scene.three\_d\_scene.ThreeDScene`

_class_ ThreeDScene( _camera\_class=<class'manim.camera.three\_d\_camera.ThreeDCamera'>_, _ambient\_camera\_rotation=None_, _default\_angled\_camera\_orientation\_kwargs=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/three_d_scene.html#ThreeDScene) [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene "Link to this definition")

Bases: [`Scene`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")

This is a Scene, with special configurations and properties that
make it suitable for Three Dimensional Scenes.

Methods

|     |     |
| --- | --- |
| [`add_fixed_in_frame_mobjects`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects "manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects") | This method is used to prevent the rotation and movement of mobjects as the camera moves around. |
| [`add_fixed_orientation_mobjects`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.add_fixed_orientation_mobjects "manim.scene.three_d_scene.ThreeDScene.add_fixed_orientation_mobjects") | This method is used to prevent the rotation and tilting of mobjects as the camera moves around. |
| [`begin_3dillusion_camera_rotation`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.begin_3dillusion_camera_rotation "manim.scene.three_d_scene.ThreeDScene.begin_3dillusion_camera_rotation") | This method creates a 3D camera rotation illusion around the current camera orientation. |
| [`begin_ambient_camera_rotation`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.begin_ambient_camera_rotation "manim.scene.three_d_scene.ThreeDScene.begin_ambient_camera_rotation") | This method begins an ambient rotation of the camera about the Z\_AXIS, in the anticlockwise direction |
| [`get_moving_mobjects`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.get_moving_mobjects "manim.scene.three_d_scene.ThreeDScene.get_moving_mobjects") | This method returns a list of all of the Mobjects in the Scene that are moving, that are also in the animations passed. |
| [`move_camera`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.move_camera "manim.scene.three_d_scene.ThreeDScene.move_camera") | This method animates the movement of the camera to the given spherical coordinates. |
| [`remove_fixed_in_frame_mobjects`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.remove_fixed_in_frame_mobjects "manim.scene.three_d_scene.ThreeDScene.remove_fixed_in_frame_mobjects") | This method undoes what add\_fixed\_in\_frame\_mobjects does. |
| [`remove_fixed_orientation_mobjects`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.remove_fixed_orientation_mobjects "manim.scene.three_d_scene.ThreeDScene.remove_fixed_orientation_mobjects") | This method "unfixes" the orientation of the mobjects passed, meaning they will no longer be at the same angle relative to the camera. |
| [`set_camera_orientation`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.set_camera_orientation "manim.scene.three_d_scene.ThreeDScene.set_camera_orientation") | This method sets the orientation of the camera in the scene. |
| [`set_to_default_angled_camera_orientation`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.set_to_default_angled_camera_orientation "manim.scene.three_d_scene.ThreeDScene.set_to_default_angled_camera_orientation") | This method sets the default\_angled\_camera\_orientation to the keyword arguments passed, and sets the camera to that orientation. |
| [`stop_3dillusion_camera_rotation`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.stop_3dillusion_camera_rotation "manim.scene.three_d_scene.ThreeDScene.stop_3dillusion_camera_rotation") | This method stops all illusion camera rotations. |
| [`stop_ambient_camera_rotation`](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.stop_ambient_camera_rotation "manim.scene.three_d_scene.ThreeDScene.stop_ambient_camera_rotation") | This method stops all ambient camera rotation. |

Attributes

|     |     |
| --- | --- |
| `camera` |  |
| `time` | The time since the start of the scene. |

add\_fixed\_in\_frame\_mobjects( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/three_d_scene.html#ThreeDScene.add_fixed_in_frame_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects "Link to this definition")

This method is used to prevent the rotation and movement
of mobjects as the camera moves around. The mobject is
essentially overlaid, and is not impacted by the camera’s
movement in any way.

Parameters:

**\*mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The Mobjects whose orientation must be fixed.

add\_fixed\_orientation\_mobjects( _\*mobjects_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/three_d_scene.html#ThreeDScene.add_fixed_orientation_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.add_fixed_orientation_mobjects "Link to this definition")

This method is used to prevent the rotation and tilting
of mobjects as the camera moves around. The mobject can
still move in the x,y,z directions, but will always be
at the angle (relative to the camera) that it was at
when it was passed through this method.)

Parameters:

- **\*mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The Mobject(s) whose orientation must be fixed.

- **\*\*kwargs** –
Some valid kwargs are

use\_static\_center\_func : bool
center\_func : function


begin\_3dillusion\_camera\_rotation( _rate=1_, _origin\_phi=None_, _origin\_theta=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/three_d_scene.html#ThreeDScene.begin_3dillusion_camera_rotation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.begin_3dillusion_camera_rotation "Link to this definition")

This method creates a 3D camera rotation illusion around
the current camera orientation.

Parameters:

- **rate** ( _float_) – The rate at which the camera rotation illusion should operate.

- **origin\_phi** ( _float_ _\|_ _None_) – The polar angle the camera should move around. Defaults
to the current phi angle.

- **origin\_theta** ( _float_ _\|_ _None_) – The azimutal angle the camera should move around. Defaults
to the current theta angle.


begin\_ambient\_camera\_rotation( _rate=0.02_, _about='theta'_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/three_d_scene.html#ThreeDScene.begin_ambient_camera_rotation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.begin_ambient_camera_rotation "Link to this definition")

This method begins an ambient rotation of the camera about the Z\_AXIS,
in the anticlockwise direction

Parameters:

- **rate** ( _float_) – The rate at which the camera should rotate about the Z\_AXIS.
Negative rate means clockwise rotation.

- **about** ( _str_) – one of 3 options: \[“theta”, “phi”, “gamma”\]. defaults to theta.


get\_moving\_mobjects( _\*animations_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/three_d_scene.html#ThreeDScene.get_moving_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.get_moving_mobjects "Link to this definition")

This method returns a list of all of the Mobjects in the Scene that
are moving, that are also in the animations passed.

Parameters:

**\*animations** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")) – The animations whose mobjects will be checked.

move\_camera( _phi=None_, _theta=None_, _gamma=None_, _zoom=None_, _focal\_distance=None_, _frame\_center=None_, _added\_anims=\[\]_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/three_d_scene.html#ThreeDScene.move_camera) [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.move_camera "Link to this definition")

This method animates the movement of the camera
to the given spherical coordinates.

Parameters:

- **phi** ( _float_ _\|_ _None_) – The polar angle i.e the angle between Z\_AXIS and Camera through ORIGIN in radians.

- **theta** ( _float_ _\|_ _None_) – The azimuthal angle i.e the angle that spins the camera around the Z\_AXIS.

- **focal\_distance** ( _float_ _\|_ _None_) – The radial focal\_distance between ORIGIN and Camera.

- **gamma** ( _float_ _\|_ _None_) – The rotation of the camera about the vector from the ORIGIN to the Camera.

- **zoom** ( _float_ _\|_ _None_) – The zoom factor of the camera.

- **frame\_center** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\|_ _Sequence_ _\[_ _float_ _\]_ _\|_ _None_) – The new center of the camera frame in cartesian coordinates.

- **added\_anims** ( _Iterable_ _\[_ [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\]_) – Any other animations to be played at the same time.


remove\_fixed\_in\_frame\_mobjects( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/three_d_scene.html#ThreeDScene.remove_fixed_in_frame_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.remove_fixed_in_frame_mobjects "Link to this definition")

> This method undoes what add\_fixed\_in\_frame\_mobjects does.
> It allows the mobject to be affected by the movement of
> the camera.

Parameters:

**\*mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The Mobjects whose position and orientation must be unfixed.

remove\_fixed\_orientation\_mobjects( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/three_d_scene.html#ThreeDScene.remove_fixed_orientation_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.remove_fixed_orientation_mobjects "Link to this definition")

This method “unfixes” the orientation of the mobjects
passed, meaning they will no longer be at the same angle
relative to the camera. This only makes sense if the
mobject was passed through add\_fixed\_orientation\_mobjects first.

Parameters:

**\*mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The Mobjects whose orientation must be unfixed.

set\_camera\_orientation( _phi=None_, _theta=None_, _gamma=None_, _zoom=None_, _focal\_distance=None_, _frame\_center=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/three_d_scene.html#ThreeDScene.set_camera_orientation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.set_camera_orientation "Link to this definition")

This method sets the orientation of the camera in the scene.

Parameters:

- **phi** ( _float_ _\|_ _None_) – The polar angle i.e the angle between Z\_AXIS and Camera through ORIGIN in radians.

- **theta** ( _float_ _\|_ _None_) – The azimuthal angle i.e the angle that spins the camera around the Z\_AXIS.

- **focal\_distance** ( _float_ _\|_ _None_) – The focal\_distance of the Camera.

- **gamma** ( _float_ _\|_ _None_) – The rotation of the camera about the vector from the ORIGIN to the Camera.

- **zoom** ( _float_ _\|_ _None_) – The zoom factor of the scene.

- **frame\_center** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\|_ _Sequence_ _\[_ _float_ _\]_ _\|_ _None_) – The new center of the camera frame in cartesian coordinates.


set\_to\_default\_angled\_camera\_orientation( _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/three_d_scene.html#ThreeDScene.set_to_default_angled_camera_orientation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.set_to_default_angled_camera_orientation "Link to this definition")

This method sets the default\_angled\_camera\_orientation to the
keyword arguments passed, and sets the camera to that orientation.

Parameters:

**\*\*kwargs** – Some recognised kwargs are phi, theta, focal\_distance, gamma,
which have the same meaning as the parameters in set\_camera\_orientation.

stop\_3dillusion\_camera\_rotation() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/three_d_scene.html#ThreeDScene.stop_3dillusion_camera_rotation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.stop_3dillusion_camera_rotation "Link to this definition")

This method stops all illusion camera rotations.

stop\_ambient\_camera\_rotation( _about='theta'_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/three_d_scene.html#ThreeDScene.stop_ambient_camera_rotation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene.stop_ambient_camera_rotation "Link to this definition")

This method stops all ambient camera rotation.

[**Document Extraction for Developers** Transform docs into structured data with Sensible. **Try for free →**](https://server.ethicalads.io/proxy/click/8518/019600e2-1cda-79d2-af8c-7a9ad51709e6/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8518/019600e2-1cda-79d2-af8c-7a9ad51709e6/)