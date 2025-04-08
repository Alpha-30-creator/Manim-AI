# MultiCamera [¶](https://docs.manim.community/en/stable/reference/manim.camera.multi_camera.MultiCamera.html\#multicamera "Link to this heading")

Qualified name: `manim.camera.multi\_camera.MultiCamera`

_class_ MultiCamera( _image\_mobjects\_from\_cameras=None_, _allow\_cameras\_to\_capture\_their\_own\_display=False_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/multi_camera.html#MultiCamera) [¶](https://docs.manim.community/en/stable/reference/manim.camera.multi_camera.MultiCamera.html#manim.camera.multi_camera.MultiCamera "Link to this definition")

Bases: [`MovingCamera`](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera "manim.camera.moving_camera.MovingCamera")

Camera Object that allows for multiple perspectives.

Initialises the MultiCamera

Parameters:

- **image\_mobjects\_from\_cameras** ( [_ImageMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.image_mobject.ImageMobject.html#manim.mobject.types.image_mobject.ImageMobject "manim.mobject.types.image_mobject.ImageMobject") _\|_ _None_)

- **kwargs** – Any valid keyword arguments of MovingCamera.


Methods

|     |     |
| --- | --- |
| [`add_image_mobject_from_camera`](https://docs.manim.community/en/stable/reference/manim.camera.multi_camera.MultiCamera.html#manim.camera.multi_camera.MultiCamera.add_image_mobject_from_camera "manim.camera.multi_camera.MultiCamera.add_image_mobject_from_camera") | Adds an ImageMobject that's been obtained from the camera into the list `self.image_mobject_from_cameras` |
| [`capture_mobjects`](https://docs.manim.community/en/stable/reference/manim.camera.multi_camera.MultiCamera.html#manim.camera.multi_camera.MultiCamera.capture_mobjects "manim.camera.multi_camera.MultiCamera.capture_mobjects") | Capture mobjects by printing them on `pixel_array`. |
| [`get_mobjects_indicating_movement`](https://docs.manim.community/en/stable/reference/manim.camera.multi_camera.MultiCamera.html#manim.camera.multi_camera.MultiCamera.get_mobjects_indicating_movement "manim.camera.multi_camera.MultiCamera.get_mobjects_indicating_movement") | Returns all mobjects whose movement implies that the camera should think of all other mobjects on the screen as moving |
| [`reset`](https://docs.manim.community/en/stable/reference/manim.camera.multi_camera.MultiCamera.html#manim.camera.multi_camera.MultiCamera.reset "manim.camera.multi_camera.MultiCamera.reset") | Resets the MultiCamera. |
| [`update_sub_cameras`](https://docs.manim.community/en/stable/reference/manim.camera.multi_camera.MultiCamera.html#manim.camera.multi_camera.MultiCamera.update_sub_cameras "manim.camera.multi_camera.MultiCamera.update_sub_cameras") | Reshape sub\_camera pixel\_arrays |

Attributes

|     |     |
| --- | --- |
| `background_color` |  |
| `background_opacity` |  |
| `frame_center` | Returns the centerpoint of the frame in cartesian coordinates. |
| `frame_height` | Returns the height of the frame. |
| `frame_width` | Returns the width of the frame |

add\_image\_mobject\_from\_camera( _image\_mobject\_from\_camera_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/multi_camera.html#MultiCamera.add_image_mobject_from_camera) [¶](https://docs.manim.community/en/stable/reference/manim.camera.multi_camera.MultiCamera.html#manim.camera.multi_camera.MultiCamera.add_image_mobject_from_camera "Link to this definition")

Adds an ImageMobject that’s been obtained from the camera
into the list `self.image_mobject_from_cameras`

Parameters:

**image\_mobject\_from\_camera** ( [_ImageMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.image_mobject.ImageMobject.html#manim.mobject.types.image_mobject.ImageMobject "manim.mobject.types.image_mobject.ImageMobject")) – The ImageMobject to add to self.image\_mobject\_from\_cameras

capture\_mobjects( _mobjects_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/multi_camera.html#MultiCamera.capture_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.camera.multi_camera.MultiCamera.html#manim.camera.multi_camera.MultiCamera.capture_mobjects "Link to this definition")

Capture mobjects by printing them on `pixel_array`.

This is the essential function that converts the contents of a Scene
into an array, which is then converted to an image or video.

Parameters:

- **mobjects** – Mobjects to capture.

- **kwargs** – Keyword arguments to be passed to `get_mobjects_to_display()`.


Notes

For a list of classes that can currently be rendered, see `display_funcs()`.

get\_mobjects\_indicating\_movement() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/multi_camera.html#MultiCamera.get_mobjects_indicating_movement) [¶](https://docs.manim.community/en/stable/reference/manim.camera.multi_camera.MultiCamera.html#manim.camera.multi_camera.MultiCamera.get_mobjects_indicating_movement "Link to this definition")

Returns all mobjects whose movement implies that the camera
should think of all other mobjects on the screen as moving

Return type:

list

reset() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/multi_camera.html#MultiCamera.reset) [¶](https://docs.manim.community/en/stable/reference/manim.camera.multi_camera.MultiCamera.html#manim.camera.multi_camera.MultiCamera.reset "Link to this definition")

Resets the MultiCamera.

Returns:

The reset MultiCamera

Return type:

[MultiCamera](https://docs.manim.community/en/stable/reference/manim.camera.multi_camera.MultiCamera.html#manim.camera.multi_camera.MultiCamera "manim.camera.multi_camera.MultiCamera")

update\_sub\_cameras() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/multi_camera.html#MultiCamera.update_sub_cameras) [¶](https://docs.manim.community/en/stable/reference/manim.camera.multi_camera.MultiCamera.html#manim.camera.multi_camera.MultiCamera.update_sub_cameras "Link to this definition")

Reshape sub\_camera pixel\_arrays