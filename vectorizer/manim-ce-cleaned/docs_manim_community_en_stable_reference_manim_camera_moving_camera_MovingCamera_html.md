# MovingCamera [¶](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html\#movingcamera "Link to this heading")

Qualified name: `manim.camera.moving\_camera.MovingCamera`

_class_ MovingCamera( _frame=None_, _fixed\_dimension=0_, _default\_frame\_stroke\_color=ManimColor('#FFFFFF')_, _default\_frame\_stroke\_width=0_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/moving_camera.html#MovingCamera) [¶](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera "Link to this definition")

Bases: [`Camera`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera")

Stays in line with the height, width and position of it’s ‘frame’, which is a Rectangle

See also

[`MovingCameraScene`](https://docs.manim.community/en/stable/reference/manim.scene.moving_camera_scene.MovingCameraScene.html#manim.scene.moving_camera_scene.MovingCameraScene "manim.scene.moving_camera_scene.MovingCameraScene")

Frame is a Mobject, (should almost certainly be a rectangle)
determining which region of space the camera displays

Methods

|     |     |
| --- | --- |
| [`auto_zoom`](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.auto_zoom "manim.camera.moving_camera.MovingCamera.auto_zoom") | Zooms on to a given array of mobjects (or a singular mobject) and automatically resizes to frame all the mobjects. |
| [`cache_cairo_context`](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.cache_cairo_context "manim.camera.moving_camera.MovingCamera.cache_cairo_context") | Since the frame can be moving around, the cairo context used for updating should be regenerated at each frame. |
| [`capture_mobjects`](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.capture_mobjects "manim.camera.moving_camera.MovingCamera.capture_mobjects") | Capture mobjects by printing them on `pixel_array`. |
| [`get_cached_cairo_context`](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.get_cached_cairo_context "manim.camera.moving_camera.MovingCamera.get_cached_cairo_context") | Since the frame can be moving around, the cairo context used for updating should be regenerated at each frame. |
| [`get_mobjects_indicating_movement`](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.get_mobjects_indicating_movement "manim.camera.moving_camera.MovingCamera.get_mobjects_indicating_movement") | Returns all mobjects whose movement implies that the camera should think of all other mobjects on the screen as moving |

Attributes

|     |     |
| --- | --- |
| `background_color` |  |
| `background_opacity` |  |
| [`frame_center`](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.frame_center "manim.camera.moving_camera.MovingCamera.frame_center") | Returns the centerpoint of the frame in cartesian coordinates. |
| [`frame_height`](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.frame_height "manim.camera.moving_camera.MovingCamera.frame_height") | Returns the height of the frame. |
| [`frame_width`](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.frame_width "manim.camera.moving_camera.MovingCamera.frame_width") | Returns the width of the frame |

auto\_zoom( _mobjects_, _margin=0_, _only\_mobjects\_in\_frame=False_, _animate=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/moving_camera.html#MovingCamera.auto_zoom) [¶](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.auto_zoom "Link to this definition")

Zooms on to a given array of mobjects (or a singular mobject)
and automatically resizes to frame all the mobjects.

Note

This method only works when 2D-objects in the XY-plane are considered, it
will not work correctly when the camera has been rotated.

Parameters:

- **mobjects** ( _list_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – The mobject or array of mobjects that the camera will focus on.

- **margin** ( _float_) – The width of the margin that is added to the frame (optional, 0 by default).

- **only\_mobjects\_in\_frame** ( _bool_) – If set to `True`, only allows focusing on mobjects that are already in frame.

- **animate** ( _bool_) – If set to `False`, applies the changes instead of returning the corresponding animation


Returns:

\_AnimationBuilder that zooms the camera view to a given list of mobjects
or ScreenRectangle with position and size updated to zoomed position.

Return type:

[Union](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Union.html#manim.mobject.geometry.boolean_ops.Union "manim.mobject.geometry.boolean_ops.Union")\[\_AnimationBuilder, [ScreenRectangle](https://docs.manim.community/en/stable/reference/manim.mobject.frame.ScreenRectangle.html#manim.mobject.frame.ScreenRectangle "manim.mobject.frame.ScreenRectangle")\]

cache\_cairo\_context( _pixel\_array_, _ctx_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/moving_camera.html#MovingCamera.cache_cairo_context) [¶](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.cache_cairo_context "Link to this definition")

Since the frame can be moving around, the cairo
context used for updating should be regenerated
at each frame. So no caching.

capture\_mobjects( _mobjects_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/moving_camera.html#MovingCamera.capture_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.capture_mobjects "Link to this definition")

Capture mobjects by printing them on `pixel_array`.

This is the essential function that converts the contents of a Scene
into an array, which is then converted to an image or video.

Parameters:

- **mobjects** – Mobjects to capture.

- **kwargs** – Keyword arguments to be passed to `get_mobjects_to_display()`.


Notes

For a list of classes that can currently be rendered, see `display_funcs()`.

_property_ frame\_center [¶](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.frame_center "Link to this definition")

Returns the centerpoint of the frame in cartesian coordinates.

Returns:

The cartesian coordinates of the center of the frame.

Return type:

np.array

_property_ frame\_height [¶](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.frame_height "Link to this definition")

Returns the height of the frame.

Returns:

The height of the frame.

Return type:

float

_property_ frame\_width [¶](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.frame_width "Link to this definition")

Returns the width of the frame

Returns:

The width of the frame.

Return type:

float

get\_cached\_cairo\_context( _pixel\_array_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/moving_camera.html#MovingCamera.get_cached_cairo_context) [¶](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.get_cached_cairo_context "Link to this definition")

Since the frame can be moving around, the cairo
context used for updating should be regenerated
at each frame. So no caching.

get\_mobjects\_indicating\_movement() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/moving_camera.html#MovingCamera.get_mobjects_indicating_movement) [¶](https://docs.manim.community/en/stable/reference/manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera.get_mobjects_indicating_movement "Link to this definition")

Returns all mobjects whose movement implies that the camera
should think of all other mobjects on the screen as moving

Return type:

list