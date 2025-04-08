ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.camera.mapping_camera.MappingCamera.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.camera.mapping_camera.MappingCamera.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# MappingCamera [¶](https://docs.manim.community/en/stable/reference/manim.camera.mapping_camera.MappingCamera.html\#mappingcamera "Link to this heading")

Qualified name: `manim.camera.mapping\_camera.MappingCamera`

_class_ MappingCamera( _mapping\_func=<functionMappingCamera.<lambda>>_, _min\_num\_curves=50_, _allow\_object\_intrusion=False_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/mapping_camera.html#MappingCamera) [¶](https://docs.manim.community/en/stable/reference/manim.camera.mapping_camera.MappingCamera.html#manim.camera.mapping_camera.MappingCamera "Link to this definition")

Bases: [`Camera`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera")

Camera object that allows mapping
between objects.

Methods

|     |     |
| --- | --- |
| [`capture_mobjects`](https://docs.manim.community/en/stable/reference/manim.camera.mapping_camera.MappingCamera.html#manim.camera.mapping_camera.MappingCamera.capture_mobjects "manim.camera.mapping_camera.MappingCamera.capture_mobjects") | Capture mobjects by printing them on `pixel_array`. |
| `points_to_pixel_coords` |  |

Attributes

|     |     |
| --- | --- |
| `background_color` |  |
| `background_opacity` |  |

capture\_mobjects( _mobjects_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/mapping_camera.html#MappingCamera.capture_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.camera.mapping_camera.MappingCamera.html#manim.camera.mapping_camera.MappingCamera.capture_mobjects "Link to this definition")

Capture mobjects by printing them on `pixel_array`.

This is the essential function that converts the contents of a Scene
into an array, which is then converted to an image or video.

Parameters:

- **mobjects** – Mobjects to capture.

- **kwargs** – Keyword arguments to be passed to `get_mobjects_to_display()`.


Notes

For a list of classes that can currently be rendered, see `display_funcs()`.