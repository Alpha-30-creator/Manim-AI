# Camera [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html\#camera "Link to this heading")

Qualified name: `manim.camera.camera.Camera`

_class_ Camera( _background\_image=None_, _frame\_center=array(\[0.,0.,0.\])_, _image\_mode='RGBA'_, _n\_channels=4_, _pixel\_array\_dtype='uint8'_, _cairo\_line\_width\_multiple=0.01_, _use\_z\_index=True_, _background=None_, _pixel\_height=None_, _pixel\_width=None_, _frame\_height=None_, _frame\_width=None_, _frame\_rate=None_, _background\_color=None_, _background\_opacity=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "Link to this definition")

Bases: `object`

Base camera class.

This is the object which takes care of what exactly is displayed
on screen at any given moment.

Parameters:

- **background\_image** ( _str_ _\|_ _None_) – The path to an image that should be the background image.
If not set, the background is filled with `self.background_color`

- **background** ( _np.ndarray_ _\|_ _None_) – What `background` is set to. By default, `None`.

- **pixel\_height** ( _int_ _\|_ _None_) – The height of the scene in pixels.

- **pixel\_width** ( _int_ _\|_ _None_) – The width of the scene in pixels.

- **kwargs** – Additional arguments ( `background_color`, `background_opacity`)
to be set.

- **frame\_center** ( _np.ndarray_)

- **image\_mode** ( _str_)

- **n\_channels** ( _int_)

- **pixel\_array\_dtype** ( _str_)

- **cairo\_line\_width\_multiple** ( _float_)

- **use\_z\_index** ( _bool_)

- **frame\_height** ( _float_ _\|_ _None_)

- **frame\_width** ( _float_ _\|_ _None_)

- **frame\_rate** ( _float_ _\|_ _None_)

- **background\_color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_)

- **background\_opacity** ( _float_ _\|_ _None_)


Methods

|     |     |
| --- | --- |
| [`adjust_out_of_range_points`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.adjust_out_of_range_points "manim.camera.camera.Camera.adjust_out_of_range_points") | If any of the points in the passed array are out of the viable range, they are adjusted suitably. |
| [`adjusted_thickness`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.adjusted_thickness "manim.camera.camera.Camera.adjusted_thickness") | Computes the adjusted stroke width for a zoomed camera. |
| [`apply_fill`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.apply_fill "manim.camera.camera.Camera.apply_fill") | Fills the cairo context |
| [`apply_stroke`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.apply_stroke "manim.camera.camera.Camera.apply_stroke") | Applies a stroke to the VMobject in the cairo context. |
| [`cache_cairo_context`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.cache_cairo_context "manim.camera.camera.Camera.cache_cairo_context") | Caches the passed Pixel array into a Cairo Context |
| [`capture_mobject`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.capture_mobject "manim.camera.camera.Camera.capture_mobject") | Capture mobjects by storing it in `pixel_array`. |
| [`capture_mobjects`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.capture_mobjects "manim.camera.camera.Camera.capture_mobjects") | Capture mobjects by printing them on `pixel_array`. |
| [`convert_pixel_array`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.convert_pixel_array "manim.camera.camera.Camera.convert_pixel_array") | Converts a pixel array from values that have floats in then to proper RGB values. |
| [`display_image_mobject`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_image_mobject "manim.camera.camera.Camera.display_image_mobject") | Displays an ImageMobject by changing the pixel\_array suitably. |
| [`display_multiple_background_colored_vmobjects`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_multiple_background_colored_vmobjects "manim.camera.camera.Camera.display_multiple_background_colored_vmobjects") | Displays multiple vmobjects that have the same color as the background. |
| [`display_multiple_image_mobjects`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_multiple_image_mobjects "manim.camera.camera.Camera.display_multiple_image_mobjects") | Displays multiple image mobjects by modifying the passed pixel\_array. |
| [`display_multiple_non_background_colored_vmobjects`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_multiple_non_background_colored_vmobjects "manim.camera.camera.Camera.display_multiple_non_background_colored_vmobjects") | Displays multiple VMobjects in the cairo context, as long as they don't have background colors. |
| [`display_multiple_point_cloud_mobjects`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_multiple_point_cloud_mobjects "manim.camera.camera.Camera.display_multiple_point_cloud_mobjects") | Displays multiple PMobjects by modifying the passed pixel array. |
| [`display_multiple_vectorized_mobjects`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_multiple_vectorized_mobjects "manim.camera.camera.Camera.display_multiple_vectorized_mobjects") | Displays multiple VMobjects in the pixel\_array |
| [`display_point_cloud`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_point_cloud "manim.camera.camera.Camera.display_point_cloud") | Displays a PMobject by modifying the pixel array suitably. |
| [`display_vectorized`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_vectorized "manim.camera.camera.Camera.display_vectorized") | Displays a VMobject in the cairo context |
| [`get_background_colored_vmobject_displayer`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_background_colored_vmobject_displayer "manim.camera.camera.Camera.get_background_colored_vmobject_displayer") | Returns the background\_colored\_vmobject\_displayer if it exists or makes one and returns it if not. |
| [`get_cached_cairo_context`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_cached_cairo_context "manim.camera.camera.Camera.get_cached_cairo_context") | Returns the cached cairo context of the passed pixel array if it exists, and None if it doesn't. |
| [`get_cairo_context`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_cairo_context "manim.camera.camera.Camera.get_cairo_context") | Returns the cairo context for a pixel array after caching it to self.pixel\_array\_to\_cairo\_context If that array has already been cached, it returns the cached version instead. |
| [`get_coords_of_all_pixels`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_coords_of_all_pixels "manim.camera.camera.Camera.get_coords_of_all_pixels") | Returns the cartesian coordinates of each pixel. |
| [`get_fill_rgbas`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_fill_rgbas "manim.camera.camera.Camera.get_fill_rgbas") | Returns the RGBA array of the fill of the passed VMobject |
| [`get_image`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_image "manim.camera.camera.Camera.get_image") | Returns an image from the passed pixel array, or from the current frame if the passed pixel array is none. |
| [`get_mobjects_to_display`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_mobjects_to_display "manim.camera.camera.Camera.get_mobjects_to_display") | Used to get the list of mobjects to display with the camera. |
| [`get_stroke_rgbas`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_stroke_rgbas "manim.camera.camera.Camera.get_stroke_rgbas") | Gets the RGBA array for the stroke of the passed VMobject. |
| [`get_thickening_nudges`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_thickening_nudges "manim.camera.camera.Camera.get_thickening_nudges") | Determine a list of vectors used to nudge two-dimensional pixel coordinates. |
| [`init_background`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.init_background "manim.camera.camera.Camera.init_background") | Initialize the background. |
| [`is_in_frame`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.is_in_frame "manim.camera.camera.Camera.is_in_frame") | Checks whether the passed mobject is in frame or not. |
| [`make_background_from_func`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.make_background_from_func "manim.camera.camera.Camera.make_background_from_func") | Makes a pixel array for the background by using coords\_to\_colors\_func to determine each pixel's color. |
| [`on_screen_pixels`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.on_screen_pixels "manim.camera.camera.Camera.on_screen_pixels") | Returns array of pixels that are on the screen from a given array of pixel\_coordinates |
| [`overlay_PIL_image`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.overlay_PIL_image "manim.camera.camera.Camera.overlay_PIL_image") | Overlays a PIL image on the passed pixel array. |
| [`overlay_rgba_array`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.overlay_rgba_array "manim.camera.camera.Camera.overlay_rgba_array") | Overlays an RGBA array on top of the given Pixel array. |
| `points_to_pixel_coords` |  |
| [`reset`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.reset "manim.camera.camera.Camera.reset") | Resets the camera's pixel array to that of the background |
| [`reset_pixel_shape`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.reset_pixel_shape "manim.camera.camera.Camera.reset_pixel_shape") | This method resets the height and width of a single pixel to the passed new\_height and new\_width. |
| [`resize_frame_shape`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.resize_frame_shape "manim.camera.camera.Camera.resize_frame_shape") | Changes frame\_shape to match the aspect ratio of the pixels, where fixed\_dimension determines whether frame\_height or frame\_width remains fixed while the other changes accordingly. |
| [`set_background`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.set_background "manim.camera.camera.Camera.set_background") | Sets the background to the passed pixel\_array after converting to valid RGB values. |
| [`set_background_from_func`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.set_background_from_func "manim.camera.camera.Camera.set_background_from_func") | Sets the background to a pixel array using coords\_to\_colors\_func to determine each pixel's color. |
| [`set_cairo_context_color`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.set_cairo_context_color "manim.camera.camera.Camera.set_cairo_context_color") | Sets the color of the cairo context |
| [`set_cairo_context_path`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.set_cairo_context_path "manim.camera.camera.Camera.set_cairo_context_path") | Sets a path for the cairo context with the vmobject passed |
| `set_frame_to_background` |  |
| [`set_pixel_array`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.set_pixel_array "manim.camera.camera.Camera.set_pixel_array") | Sets the pixel array of the camera to the passed pixel array. |
| [`thickened_coordinates`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.thickened_coordinates "manim.camera.camera.Camera.thickened_coordinates") | Returns thickened coordinates for a passed array of pixel coords and a thickness to thicken by. |
| `transform_points_pre_display` |  |
| [`type_or_raise`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.type_or_raise "manim.camera.camera.Camera.type_or_raise") | Return the type of mobject, if it is a type that can be rendered. |

Attributes

|     |     |
| --- | --- |
| `background_color` |  |
| `background_opacity` |  |

adjust\_out\_of\_range\_points( _points_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.adjust_out_of_range_points) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.adjust_out_of_range_points "Link to this definition")

If any of the points in the passed array are out of
the viable range, they are adjusted suitably.

Parameters:

**points** ( _ndarray_) – The points to adjust

Returns:

The adjusted points.

Return type:

np.array

adjusted\_thickness( _thickness_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.adjusted_thickness) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.adjusted_thickness "Link to this definition")

Computes the adjusted stroke width for a zoomed camera.

Parameters:

**thickness** ( _float_) – The stroke width of a mobject.

Returns:

The adjusted stroke width that reflects zooming in with
the camera.

Return type:

float

apply\_fill( _ctx_, _vmobject_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.apply_fill) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.apply_fill "Link to this definition")

Fills the cairo context

Parameters:

- **ctx** ( _Context_) – The cairo context

- **vmobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject


Returns:

The camera object.

Return type:

[Camera](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera")

apply\_stroke( _ctx_, _vmobject_, _background=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.apply_stroke) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.apply_stroke "Link to this definition")

Applies a stroke to the VMobject in the cairo context.

Parameters:

- **ctx** ( _Context_) – The cairo context

- **vmobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject

- **background** ( _bool_) – Whether or not to consider the background when applying this
stroke width, by default False


Returns:

The camera object with the stroke applied.

Return type:

[Camera](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera")

cache\_cairo\_context( _pixel\_array_, _ctx_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.cache_cairo_context) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.cache_cairo_context "Link to this definition")

Caches the passed Pixel array into a Cairo Context

Parameters:

- **pixel\_array** ( _ndarray_) – The pixel array to cache

- **ctx** ( _Context_) – The context to cache it into.


capture\_mobject( _mobject_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.capture_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.capture_mobject "Link to this definition")

Capture mobjects by storing it in `pixel_array`.

This is a single-mobject version of [`capture_mobjects()`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.capture_mobjects "manim.camera.camera.Camera.capture_mobjects").

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – Mobject to capture.

- **kwargs** ( _Any_) – Keyword arguments to be passed to [`get_mobjects_to_display()`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_mobjects_to_display "manim.camera.camera.Camera.get_mobjects_to_display").


capture\_mobjects( _mobjects_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.capture_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.capture_mobjects "Link to this definition")

Capture mobjects by printing them on `pixel_array`.

This is the essential function that converts the contents of a Scene
into an array, which is then converted to an image or video.

Parameters:

- **mobjects** ( _Iterable_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – Mobjects to capture.

- **kwargs** – Keyword arguments to be passed to [`get_mobjects_to_display()`](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_mobjects_to_display "manim.camera.camera.Camera.get_mobjects_to_display").


Notes

For a list of classes that can currently be rendered, see `display_funcs()`.

convert\_pixel\_array( _pixel\_array_, _convert\_from\_floats=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.convert_pixel_array) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.convert_pixel_array "Link to this definition")

Converts a pixel array from values that have floats in then
to proper RGB values.

Parameters:

- **pixel\_array** ( _ndarray_ _\|_ _list_ _\|_ _tuple_) – Pixel array to convert.

- **convert\_from\_floats** ( _bool_) – Whether or not to convert float values to ints, by default False


Returns:

The new, converted pixel array.

Return type:

np.array

display\_image\_mobject( _image\_mobject_, _pixel\_array_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.display_image_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_image_mobject "Link to this definition")

Displays an ImageMobject by changing the pixel\_array suitably.

Parameters:

- **image\_mobject** ( [_AbstractImageMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.image_mobject.AbstractImageMobject.html#manim.mobject.types.image_mobject.AbstractImageMobject "manim.mobject.types.image_mobject.AbstractImageMobject")) – The imageMobject to display

- **pixel\_array** ( _ndarray_) – The Pixel array to put the imagemobject in.


display\_multiple\_background\_colored\_vmobjects( _cvmobjects_, _pixel\_array_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.display_multiple_background_colored_vmobjects) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_multiple_background_colored_vmobjects "Link to this definition")

Displays multiple vmobjects that have the same color as the background.

Parameters:

- **cvmobjects** ( _list_) – List of Colored VMobjects

- **pixel\_array** ( _ndarray_) – The pixel array.


Returns:

The camera object.

Return type:

[Camera](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera")

display\_multiple\_image\_mobjects( _image\_mobjects_, _pixel\_array_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.display_multiple_image_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_multiple_image_mobjects "Link to this definition")

Displays multiple image mobjects by modifying the passed pixel\_array.

Parameters:

- **image\_mobjects** ( _list_) – list of ImageMobjects

- **pixel\_array** ( _ndarray_) – The pixel array to modify.


display\_multiple\_non\_background\_colored\_vmobjects( _vmobjects_, _pixel\_array_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.display_multiple_non_background_colored_vmobjects) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_multiple_non_background_colored_vmobjects "Link to this definition")

Displays multiple VMobjects in the cairo context, as long as they don’t have
background colors.

Parameters:

- **vmobjects** ( _list_) – list of the VMobjects

- **pixel\_array** ( _ndarray_) – The Pixel array to add the VMobjects to.


display\_multiple\_point\_cloud\_mobjects( _pmobjects_, _pixel\_array_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.display_multiple_point_cloud_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_multiple_point_cloud_mobjects "Link to this definition")

Displays multiple PMobjects by modifying the passed pixel array.

Parameters:

- **pmobjects** ( _list_) – List of PMobjects

- **pixel\_array** ( _ndarray_) – The pixel array to modify.


display\_multiple\_vectorized\_mobjects( _vmobjects_, _pixel\_array_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.display_multiple_vectorized_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_multiple_vectorized_mobjects "Link to this definition")

Displays multiple VMobjects in the pixel\_array

Parameters:

- **vmobjects** ( _list_) – list of VMobjects to display

- **pixel\_array** ( _ndarray_) – The pixel array


display\_point\_cloud( _pmobject_, _points_, _rgbas_, _thickness_, _pixel\_array_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.display_point_cloud) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_point_cloud "Link to this definition")

Displays a PMobject by modifying the pixel array suitably.

TODO: Write a description for the rgbas argument.

Parameters:

- **pmobject** ( [_PMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject "manim.mobject.types.point_cloud_mobject.PMobject")) – Point Cloud Mobject

- **points** ( _list_) – The points to display in the point cloud mobject

- **rgbas** ( _ndarray_)

- **thickness** ( _float_) – The thickness of each point of the PMobject

- **pixel\_array** ( _ndarray_) – The pixel array to modify.


display\_vectorized( _vmobject_, _ctx_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.display_vectorized) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.display_vectorized "Link to this definition")

Displays a VMobject in the cairo context

Parameters:

- **vmobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The Vectorized Mobject to display

- **ctx** ( _Context_) – The cairo context to use.


Returns:

The camera object

Return type:

[Camera](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera")

get\_background\_colored\_vmobject\_displayer() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.get_background_colored_vmobject_displayer) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_background_colored_vmobject_displayer "Link to this definition")

Returns the background\_colored\_vmobject\_displayer
if it exists or makes one and returns it if not.

Returns:

Object that displays VMobjects that have the same color
as the background.

Return type:

BackGroundColoredVMobjectDisplayer

get\_cached\_cairo\_context( _pixel\_array_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.get_cached_cairo_context) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_cached_cairo_context "Link to this definition")

Returns the cached cairo context of the passed
pixel array if it exists, and None if it doesn’t.

Parameters:

**pixel\_array** ( _ndarray_) – The pixel array to check.

Returns:

The cached cairo context.

Return type:

cairo.Context

get\_cairo\_context( _pixel\_array_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.get_cairo_context) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_cairo_context "Link to this definition")

Returns the cairo context for a pixel array after
caching it to self.pixel\_array\_to\_cairo\_context
If that array has already been cached, it returns the
cached version instead.

Parameters:

**pixel\_array** ( _ndarray_) – The Pixel array to get the cairo context of.

Returns:

The cairo context of the pixel array.

Return type:

cairo.Context

get\_coords\_of\_all\_pixels() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.get_coords_of_all_pixels) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_coords_of_all_pixels "Link to this definition")

Returns the cartesian coordinates of each pixel.

Returns:

The array of cartesian coordinates.

Return type:

np.ndarray

get\_fill\_rgbas( _vmobject_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.get_fill_rgbas) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_fill_rgbas "Link to this definition")

Returns the RGBA array of the fill of the passed VMobject

Parameters:

**vmobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject

Returns:

The RGBA Array of the fill of the VMobject

Return type:

np.array

get\_image( _pixel\_array=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.get_image) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_image "Link to this definition")

Returns an image from the passed
pixel array, or from the current frame
if the passed pixel array is none.

Parameters:

**pixel\_array** ( _ndarray_ _\|_ _list_ _\|_ _tuple_ _\|_ _None_) – The pixel array from which to get an image, by default None

Returns:

The PIL image of the array.

Return type:

PIL.Image

get\_mobjects\_to\_display( _mobjects_, _include\_submobjects=True_, _excluded\_mobjects=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.get_mobjects_to_display) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_mobjects_to_display "Link to this definition")

Used to get the list of mobjects to display
with the camera.

Parameters:

- **mobjects** ( _Iterable_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – The Mobjects

- **include\_submobjects** ( _bool_) – Whether or not to include the submobjects of mobjects, by default True

- **excluded\_mobjects** ( _list_ _\|_ _None_) – Any mobjects to exclude, by default None


Returns:

list of mobjects

Return type:

list

get\_stroke\_rgbas( _vmobject_, _background=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.get_stroke_rgbas) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_stroke_rgbas "Link to this definition")

Gets the RGBA array for the stroke of the passed
VMobject.

Parameters:

- **vmobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject

- **background** ( _bool_) – Whether or not to consider the background when getting the stroke
RGBAs, by default False


Returns:

The RGBA array of the stroke.

Return type:

np.ndarray

get\_thickening\_nudges( _thickness_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.get_thickening_nudges) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.get_thickening_nudges "Link to this definition")

Determine a list of vectors used to nudge
two-dimensional pixel coordinates.

Parameters:

**thickness** ( _float_)

Return type:

np.array

init\_background() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.init_background) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.init_background "Link to this definition")

Initialize the background.
If self.background\_image is the path of an image
the image is set as background; else, the default
background color fills the background.

is\_in\_frame( _mobject_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.is_in_frame) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.is_in_frame "Link to this definition")

Checks whether the passed mobject is in
frame or not.

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject for which the checking needs to be done.

Returns:

True if in frame, False otherwise.

Return type:

bool

make\_background\_from\_func( _coords\_to\_colors\_func_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.make_background_from_func) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.make_background_from_func "Link to this definition")

Makes a pixel array for the background by using coords\_to\_colors\_func to determine each pixel’s color. Each input
pixel’s color. Each input to coords\_to\_colors\_func is an (x, y) pair in space (in ordinary space coordinates; not
pixel coordinates), and each output is expected to be an RGBA array of 4 floats.

Parameters:

**coords\_to\_colors\_func** ( _Callable_ _\[_ _\[_ _ndarray_ _\]_ _,_ _ndarray_ _\]_) – The function whose input is an (x,y) pair of coordinates and
whose return values must be the colors for that point

Returns:

The pixel array which can then be passed to set\_background.

Return type:

np.array

on\_screen\_pixels( _pixel\_coords_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.on_screen_pixels) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.on_screen_pixels "Link to this definition")

Returns array of pixels that are on the screen from a given
array of pixel\_coordinates

Parameters:

**pixel\_coords** ( _ndarray_) – The pixel coords to check.

Returns:

The pixel coords on screen.

Return type:

np.array

overlay\_PIL\_image( _pixel\_array_, _image_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.overlay_PIL_image) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.overlay_PIL_image "Link to this definition")

Overlays a PIL image on the passed pixel array.

Parameters:

- **pixel\_array** ( _ndarray_) – The Pixel array

- **image** ( _<module 'PIL.Image' from '/home/docs/checkouts/readthedocs.org/user\_builds/manimce/envs/stable/lib/python3.13/site-packages/PIL/Image.py'>_) – The Image to overlay.


overlay\_rgba\_array( _pixel\_array_, _new\_array_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.overlay_rgba_array) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.overlay_rgba_array "Link to this definition")

Overlays an RGBA array on top of the given Pixel array.

Parameters:

- **pixel\_array** ( _ndarray_) – The original pixel array to modify.

- **new\_array** ( _ndarray_) – The new pixel array to overlay.


reset() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.reset) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.reset "Link to this definition")

Resets the camera’s pixel array
to that of the background

Returns:

The camera object after setting the pixel array.

Return type:

[Camera](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera")

reset\_pixel\_shape( _new\_height_, _new\_width_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.reset_pixel_shape) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.reset_pixel_shape "Link to this definition")

This method resets the height and width
of a single pixel to the passed new\_height and new\_width.

Parameters:

- **new\_height** ( _float_) – The new height of the entire scene in pixels

- **new\_width** ( _float_) – The new width of the entire scene in pixels


resize\_frame\_shape( _fixed\_dimension=0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.resize_frame_shape) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.resize_frame_shape "Link to this definition")

Changes frame\_shape to match the aspect ratio
of the pixels, where fixed\_dimension determines
whether frame\_height or frame\_width
remains fixed while the other changes accordingly.

Parameters:

**fixed\_dimension** ( _int_) – If 0, height is scaled with respect to width
else, width is scaled with respect to height.

set\_background( _pixel\_array_, _convert\_from\_floats=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.set_background) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.set_background "Link to this definition")

Sets the background to the passed pixel\_array after converting
to valid RGB values.

Parameters:

- **pixel\_array** ( _ndarray_ _\|_ _list_ _\|_ _tuple_) – The pixel array to set the background to.

- **convert\_from\_floats** ( _bool_) – Whether or not to convert floats values to proper RGB valid ones, by default False


set\_background\_from\_func( _coords\_to\_colors\_func_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.set_background_from_func) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.set_background_from_func "Link to this definition")

Sets the background to a pixel array using coords\_to\_colors\_func to determine each pixel’s color. Each input
pixel’s color. Each input to coords\_to\_colors\_func is an (x, y) pair in space (in ordinary space coordinates; not
pixel coordinates), and each output is expected to be an RGBA array of 4 floats.

Parameters:

**coords\_to\_colors\_func** ( _Callable_ _\[_ _\[_ _ndarray_ _\]_ _,_ _ndarray_ _\]_) – The function whose input is an (x,y) pair of coordinates and
whose return values must be the colors for that point

set\_cairo\_context\_color( _ctx_, _rgbas_, _vmobject_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.set_cairo_context_color) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.set_cairo_context_color "Link to this definition")

Sets the color of the cairo context

Parameters:

- **ctx** ( _Context_) – The cairo context

- **rgbas** ( _ndarray_) – The RGBA array with which to color the context.

- **vmobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject with which to set the color.


Returns:

The camera object

Return type:

[Camera](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera")

set\_cairo\_context\_path( _ctx_, _vmobject_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.set_cairo_context_path) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.set_cairo_context_path "Link to this definition")

Sets a path for the cairo context with the vmobject passed

Parameters:

- **ctx** ( _Context_) – The cairo context

- **vmobject** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject


Returns:

Camera object after setting cairo\_context\_path

Return type:

[Camera](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera")

set\_pixel\_array( _pixel\_array_, _convert\_from\_floats=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.set_pixel_array) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.set_pixel_array "Link to this definition")

Sets the pixel array of the camera to the passed pixel array.

Parameters:

- **pixel\_array** ( _ndarray_ _\|_ _list_ _\|_ _tuple_) – The pixel array to convert and then set as the camera’s pixel array.

- **convert\_from\_floats** ( _bool_) – Whether or not to convert float values to proper RGB values, by default False


thickened\_coordinates( _pixel\_coords_, _thickness_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.thickened_coordinates) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.thickened_coordinates "Link to this definition")

Returns thickened coordinates for a passed array of pixel coords and
a thickness to thicken by.

Parameters:

- **pixel\_coords** ( _ndarray_) – Pixel coordinates

- **thickness** ( _float_) – Thickness


Returns:

Array of thickened pixel coords.

Return type:

np.array

type\_or\_raise( _mobject_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/camera/camera.html#Camera.type_or_raise) [¶](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera.type_or_raise "Link to this definition")

Return the type of mobject, if it is a type that can be rendered.

If mobject is an instance of a class that inherits from a class that
can be rendered, return the super class. For example, an instance of a
Square is also an instance of VMobject, and these can be rendered.
Therefore, type\_or\_raise(Square()) returns True.

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The object to take the type of.

Notes

For a list of classes that can currently be rendered, see `display_funcs()`.

Returns:

The type of mobjects, if it can be rendered.

Return type:

Type\[ [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")\]

Raises:

**TypeError** – When mobject is not an instance of a class that can be rendered.

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))