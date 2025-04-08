ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.images.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.images.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# images [¶](https://docs.manim.community/en/stable/reference/manim.utils.images.html\#module-manim.utils.images "Link to this heading")

Image manipulation utilities.

Functions

change\_to\_rgba\_array( _image_, _dtype='uint8'_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/images.html#change_to_rgba_array) [¶](https://docs.manim.community/en/stable/reference/manim.utils.images.html#manim.utils.images.change_to_rgba_array "Link to this definition")

Converts an RGB array into RGBA with the alpha value opacity maxed.

Parameters:

- **image** ( [_RGBPixelArray_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGBPixelArray "manim.typing.RGBPixelArray"))

- **dtype** ( _str_)


Return type:

[_RGBPixelArray_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGBPixelArray "manim.typing.RGBPixelArray")

drag\_pixels( _frames_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/images.html#drag_pixels) [¶](https://docs.manim.community/en/stable/reference/manim.utils.images.html#manim.utils.images.drag_pixels "Link to this definition")Parameters:

**frames** ( _list_ _\[_ _array_ _\]_)

Return type:

list\[ _array_\]

get\_full\_raster\_image\_path( _image\_file\_name_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/images.html#get_full_raster_image_path) [¶](https://docs.manim.community/en/stable/reference/manim.utils.images.html#manim.utils.images.get_full_raster_image_path "Link to this definition")Parameters:

**image\_file\_name** ( _str_ _\|_ _PurePath_)

Return type:

_Path_

get\_full\_vector\_image\_path( _image\_file\_name_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/images.html#get_full_vector_image_path) [¶](https://docs.manim.community/en/stable/reference/manim.utils.images.html#manim.utils.images.get_full_vector_image_path "Link to this definition")Parameters:

**image\_file\_name** ( _str_ _\|_ _PurePath_)

Return type:

_Path_

invert\_image( _image_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/images.html#invert_image) [¶](https://docs.manim.community/en/stable/reference/manim.utils.images.html#manim.utils.images.invert_image "Link to this definition")Parameters:

**image** ( _array_)

Return type:

<module ‘PIL.Image’ from ‘/home/docs/checkouts/readthedocs.org/user\_builds/manimce/envs/stable/lib/python3.13/site-packages/PIL/Image.py’>