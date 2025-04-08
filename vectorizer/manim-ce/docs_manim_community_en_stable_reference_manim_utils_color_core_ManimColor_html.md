ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ManimColor [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html\#manimcolor "Link to this heading")

Qualified name: `manim.utils.color.core.ManimColor`

_class_ ManimColor( _value_, _alpha=1.0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "Link to this definition")

Bases: `object`

Internal representation of a color.

The [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") class is the main class for the representation of a color.
Its internal representation is an array of 4 floats corresponding to a `[r,g,b,a]`
value where `r,g,b,a` can be between 0.0 and 1.0.

This is done in order to reduce the amount of color inconsistencies by constantly
casting between integers and floats which introduces errors.

The class can accept any value of type [`ParsableManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") i.e.

`ManimColor, int, str, RGB_Tuple_Int, RGB_Tuple_Float, RGBA_Tuple_Int, RGBA_Tuple_Float, RGB_Array_Int,
RGB_Array_Float, RGBA_Array_Int, RGBA_Array_Float`

[`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") itself only accepts singular values and will directly interpret
them into a single color if possible. Be careful when passing strings to
[`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"): it can create a big overhead for the color processing.

If you want to parse a list of colors, use the [`parse()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.parse "manim.utils.color.core.ManimColor.parse") method, which assumes
that you’re going to pass a list of colors so that arrays will not be interpreted as
a single color.

Warning

If you pass an array of numbers to [`parse()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.parse "manim.utils.color.core.ManimColor.parse"), it will interpret the
`r,g,b,a` numbers in that array as colors: Instead of the expected
singular color, you will get an array with 4 colors.

For conversion behaviors, see the `_internal` functions for further documentation.

You can create a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") instance via its classmethods. See the
respective methods for more info.

```
mycolor = ManimColor.from_rgb((0, 1, 0.4, 0.5))
myothercolor = ManimColor.from_rgb((153, 255, 255))

```

Copy to clipboard

You can also convert between different color spaces:

```
mycolor_hex = mycolor.to_hex()
myoriginalcolor = ManimColor.from_hex(mycolor_hex).to_hsv()

```

Copy to clipboard

Parameters:

- **value** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_) – Some representation of a color (e.g., a string or
a suitable tuple). The default `None` is `BLACK`.

- **alpha** ( _float_) – The opacity of the color. By default, colors are
fully opaque (value 1.0).


Methods

|     |     |
| --- | --- |
| [`contrasting`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.contrasting "manim.utils.color.core.ManimColor.contrasting") | Return one of two colors, light or dark (by default white or black), that contrasts with the current color (depending on its luminance). |
| [`darker`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.darker "manim.utils.color.core.ManimColor.darker") | Return a new color that is darker than the current color, i.e. interpolated with `BLACK`. |
| [`from_hex`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.from_hex "manim.utils.color.core.ManimColor.from_hex") | Create a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") from a hex string. |
| [`from_hsl`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.from_hsl "manim.utils.color.core.ManimColor.from_hsl") | Create a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") from an HSL array. |
| [`from_hsv`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.from_hsv "manim.utils.color.core.ManimColor.from_hsv") | Create a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") from an HSV array. |
| [`from_rgb`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.from_rgb "manim.utils.color.core.ManimColor.from_rgb") | Create a ManimColor from an RGB array. |
| [`from_rgba`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.from_rgba "manim.utils.color.core.ManimColor.from_rgba") | Create a ManimColor from an RGBA Array. |
| [`gradient`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.gradient "manim.utils.color.core.ManimColor.gradient") | This method is currently not implemented. |
| [`interpolate`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.interpolate "manim.utils.color.core.ManimColor.interpolate") | Interpolate between the current and the given [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"), and return the result. |
| [`into`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.into "manim.utils.color.core.ManimColor.into") | Convert the current color into a different colorspace given by `class_type`, without changing the [`_internal_value`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._internal_value "manim.utils.color.core.ManimColor._internal_value"). |
| [`invert`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.invert "manim.utils.color.core.ManimColor.invert") | Return a new, linearly inverted version of this [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") (no inplace changes). |
| [`lighter`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.lighter "manim.utils.color.core.ManimColor.lighter") | Return a new color that is lighter than the current color, i.e. interpolated with `WHITE`. |
| [`opacity`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.opacity "manim.utils.color.core.ManimColor.opacity") | Create a new [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") with the given opacity and the same color values as before. |
| [`parse`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.parse "manim.utils.color.core.ManimColor.parse") | Parse one color as a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") or a sequence of colors as a list of [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")'s. |
| [`to_hex`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_hex "manim.utils.color.core.ManimColor.to_hex") | Convert the [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to a hexadecimal representation of the color. |
| [`to_hsl`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_hsl "manim.utils.color.core.ManimColor.to_hsl") | Convert the [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to an HSL array. |
| [`to_hsv`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_hsv "manim.utils.color.core.ManimColor.to_hsv") | Convert the [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to an HSV array. |
| [`to_int_rgb`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_int_rgb "manim.utils.color.core.ManimColor.to_int_rgb") | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGB array of integers. |
| [`to_int_rgba`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_int_rgba "manim.utils.color.core.ManimColor.to_int_rgba") | Convert the current ManimColor into an RGBA array of integers. |
| [`to_int_rgba_with_alpha`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_int_rgba_with_alpha "manim.utils.color.core.ManimColor.to_int_rgba_with_alpha") | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGBA array of integers. |
| [`to_integer`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_integer "manim.utils.color.core.ManimColor.to_integer") | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an integer. |
| [`to_rgb`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_rgb "manim.utils.color.core.ManimColor.to_rgb") | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGB array of floats. |
| [`to_rgba`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_rgba "manim.utils.color.core.ManimColor.to_rgba") | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGBA array of floats. |
| [`to_rgba_with_alpha`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_rgba_with_alpha "manim.utils.color.core.ManimColor.to_rgba_with_alpha") | Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGBA array of floats. |

_classmethod_\_construct\_from\_space( _\_space_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor._construct_from_space) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._construct_from_space "Link to this definition")

This function is used as a proxy for constructing a color with an internal
value. This can be used by subclasses to hook into the construction of new
objects using the internal value format.

Parameters:

**\_space** ( _ndarray_ _\[_ _tuple_ _\[_ _int_ _,_ _..._ _\]_ _,_ _dtype_ _\[_ [_ManimFloat_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimFloat "manim.typing.ManimFloat") _\]_ _\]_ _\|_ _tuple_ _\[_ _float_ _,_ _float_ _,_ _float_ _\]_ _\|_ _tuple_ _\[_ _float_ _,_ _float_ _,_ _float_ _,_ _float_ _\]_)

Return type:

_Self_

_classmethod_\_from\_internal( _value_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor._from_internal) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._from_internal "Link to this definition")

This method is intended to be overwritten by custom color space classes
which are subtypes of [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

The method constructs a new object of the given class by transforming the value
in the internal format `[r,g,b,a]` into a format which the constructor of the
custom class can understand. Look at [`HSV`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.HSV.html#manim.utils.color.core.HSV "manim.utils.color.core.HSV") for an example.

Parameters:

**value** ( [_ManimColorInternal_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal"))

Return type:

_Self_

_static_\_internal\_from\_hex\_string( _hex\__, _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor._internal_from_hex_string) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._internal_from_hex_string "Link to this definition")

Internal function for converting a hex string into the internal representation
of a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

Warning

This does not accept any prefixes like # or similar in front of the hex string.
This is just intended for the raw hex part.

_For internal use only_

Parameters:

- **hex** – Hex string to be parsed.

- **alpha** ( _float_) – Alpha value used for the color, if the color is only 3 bytes long. Otherwise,
if the color is 4 bytes long, this parameter will not be used.

- **hex\_** ( _str_)


Returns:

Internal color representation

Return type:

[ManimColorInternal](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal")

_static_\_internal\_from\_int\_rgb( _rgb_, _alpha=1.0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor._internal_from_int_rgb) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._internal_from_int_rgb "Link to this definition")

Internal function for converting an RGB tuple of integers into the internal
representation of a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

_For internal use only_

Parameters:

- **rgb** ( [_RGB\_Tuple\_Int_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGB_Tuple_Int "manim.typing.RGB_Tuple_Int")) – Integer RGB tuple to be parsed

- **alpha** ( _float_) – Optional alpha value. Default is 1.0.


Returns:

Internal color representation.

Return type:

[ManimColorInternal](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal")

_static_\_internal\_from\_int\_rgba( _rgba_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor._internal_from_int_rgba) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._internal_from_int_rgba "Link to this definition")

Internal function for converting an RGBA tuple of integers into the internal
representation of a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

_For internal use only_

Parameters:

**rgba** ( [_RGBA\_Tuple\_Int_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGBA_Tuple_Int "manim.typing.RGBA_Tuple_Int")) – Int RGBA tuple to be parsed.

Returns:

Internal color representation.

Return type:

[ManimColorInternal](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal")

_static_\_internal\_from\_rgb( _rgb_, _alpha=1.0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor._internal_from_rgb) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._internal_from_rgb "Link to this definition")

Internal function for converting a rgb tuple of floats into the internal
representation of a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

_For internal use only_

Parameters:

- **rgb** ( [_RGB\_Tuple\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGB_Tuple_Float "manim.typing.RGB_Tuple_Float")) – Float RGB tuple to be parsed.

- **alpha** ( _float_) – Optional alpha value. Default is 1.0.


Returns:

Internal color representation.

Return type:

[ManimColorInternal](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal")

_static_\_internal\_from\_rgba( _rgba_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor._internal_from_rgba) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._internal_from_rgba "Link to this definition")

Internal function for converting an RGBA tuple of floats into the internal
representation of a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

_For internal use only_

Parameters:

**rgba** ( [_RGBA\_Tuple\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGBA_Tuple_Float "manim.typing.RGBA_Tuple_Float")) – Int RGBA tuple to be parsed.

Returns:

Internal color representation.

Return type:

[ManimColorInternal](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal")

_static_\_internal\_from\_string( _name_, _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor._internal_from_string) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._internal_from_string "Link to this definition")

Internal function for converting a string into the internal representation of
a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"). This is not used for hex strings: please refer to
`_internal_from_hex()` for this functionality.

_For internal use only_

Parameters:

- **name** ( _str_) – The color name to be parsed into a color. Refer to the different color
modules in the documentation page to find the corresponding color names.

- **alpha** ( _float_)


Returns:

Internal color representation.

Return type:

[ManimColorInternal](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal")

Raises:

**ValueError** – If the color name is not present in Manim.

_property_\_internal\_space _:ndarray\[tuple\[int,...\],dtype\[ [ManimFloat](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimFloat "manim.typing.ManimFloat")\]\]_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._internal_space "Link to this definition")

This is a readonly property which is a custom representation for color space
operations. It is used for operators and can be used when implementing a custom
color space.

_property_\_internal\_value _: [ManimColorInternal](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal")_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._internal_value "Link to this definition")

Return the internal value of the current Manim color `[r,g,b,a]` float
array.

Returns:

Internal color representation.

Return type:

[ManimColorInternal](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal")

contrasting( _threshold=0.5_, _light=None_, _dark=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.contrasting) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.contrasting "Link to this definition")

Return one of two colors, light or dark (by default white or black),
that contrasts with the current color (depending on its luminance).
This is typically used to set text in a contrasting color that ensures
it is readable against a background of the current color.

Parameters:

- **threshold** ( _float_) – The luminance threshold which dictates whether the current color is
considered light or dark (and thus whether to return the dark or
light color, respectively). Default is 0.5.

- **light** ( _Self_ _\|_ _None_) – The light color to return if the current color is considered dark.
Default is `None`: in this case, pure `WHITE` will be returned.

- **dark** ( _Self_ _\|_ _None_) – The dark color to return if the current color is considered light,
Default is `None`: in this case, pure `BLACK` will be returned.


Returns:

The contrasting [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

Return type:

[ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

darker( _blend=0.2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.darker) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.darker "Link to this definition")

Return a new color that is darker than the current color, i.e.
interpolated with `BLACK`. The opacity is unchanged.

Parameters:

**blend** ( _float_) – The blend ratio for the interpolation, from 0.0 (the current color
unchanged) to 1.0 (pure black). Default is 0.2, which results in a
slightly darker color.

Returns:

The darker [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

Return type:

[ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

See also

[`lighter()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.lighter "manim.utils.color.core.ManimColor.lighter")

_classmethod_ from\_hex( _hex\_str_, _alpha=1.0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.from_hex) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.from_hex "Link to this definition")

Create a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") from a hex string.

Parameters:

- **hex\_str** ( _str_) – The hex string to be converted. The allowed prefixes for this string are
`#` and `0x`. Currently, this method only supports 6 nibbles, i.e. only
strings in the format `#XXXXXX` or `0xXXXXXX`.

- **alpha** ( _float_) – Alpha value to be used for the hex string. Default is 1.0.


Returns:

The [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") represented by the hex string.

Return type:

[ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

_classmethod_ from\_hsl( _hsl_, _alpha=1.0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.from_hsl) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.from_hsl "Link to this definition")

Create a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") from an HSL array.

Parameters:

- **hsl** ( [_HSL\_Array\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.HSL_Array_Float "manim.typing.HSL_Array_Float") _\|_ [_HSL\_Tuple\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.HSL_Tuple_Float "manim.typing.HSL_Tuple_Float")) – Any iterable containing 3 floats from 0.0 to 1.0.

- **alpha** ( _float_) – The alpha value to be used. Default is 1.0.


Returns:

The [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") with the corresponding RGB values to the given HSL
array.

Return type:

[ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

_classmethod_ from\_hsv( _hsv_, _alpha=1.0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.from_hsv) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.from_hsv "Link to this definition")

Create a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") from an HSV array.

Parameters:

- **hsv** ( [_HSV\_Array\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.HSV_Array_Float "manim.typing.HSV_Array_Float") _\|_ [_HSV\_Tuple\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.HSV_Tuple_Float "manim.typing.HSV_Tuple_Float")) – Any iterable containing 3 floats from 0.0 to 1.0.

- **alpha** ( _float_) – The alpha value to be used. Default is 1.0.


Returns:

The [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") with the corresponding RGB values to the given HSV
array.

Return type:

[ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

_classmethod_ from\_rgb( _rgb_, _alpha=1.0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.from_rgb) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.from_rgb "Link to this definition")

Create a ManimColor from an RGB array. Automagically decides which type it
is: `int` or `float`.

Warning

Please make sure that your elements are not floats if you want integers. A
`5.0` will result in the input being interpreted as if it was an RGB float
array with the value `5.0` and not the integer `5`.

Parameters:

- **rgb** ( [_RGB\_Array\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGB_Array_Float "manim.typing.RGB_Array_Float") _\|_ [_RGB\_Tuple\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGB_Tuple_Float "manim.typing.RGB_Tuple_Float") _\|_ [_RGB\_Array\_Int_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGB_Array_Int "manim.typing.RGB_Array_Int") _\|_ [_RGB\_Tuple\_Int_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGB_Tuple_Int "manim.typing.RGB_Tuple_Int")) – Any iterable of 3 floats or 3 integers.

- **alpha** ( _float_) – Alpha value to be used in the color. Default is 1.0.


Returns:

The [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") which corresponds to the given `rgb`.

Return type:

[ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

_classmethod_ from\_rgba( _rgba_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.from_rgba) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.from_rgba "Link to this definition")

Create a ManimColor from an RGBA Array. Automagically decides which type it
is: `int` or `float`.

Warning

Please make sure that your elements are not floats if you want integers. A
`5.0` will result in the input being interpreted as if it was a float RGB
array with the float `5.0` and not the integer `5`.

Parameters:

**rgba** ( [_RGBA\_Array\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGBA_Array_Float "manim.typing.RGBA_Array_Float") _\|_ [_RGBA\_Tuple\_Float_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGBA_Tuple_Float "manim.typing.RGBA_Tuple_Float") _\|_ [_RGBA\_Array\_Int_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGBA_Array_Int "manim.typing.RGBA_Array_Int") _\|_ [_RGBA\_Tuple\_Int_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGBA_Tuple_Int "manim.typing.RGBA_Tuple_Int")) – Any iterable of 4 floats or 4 integers.

Returns:

The [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") corresponding to the given `rgba`.

Return type:

[ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

_static_ gradient( _colors_, _length_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.gradient) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.gradient "Link to this definition")

This method is currently not implemented. Refer to [`color_gradient()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.color_gradient "manim.utils.color.core.color_gradient") for
a working implementation for now.

Parameters:

- **colors** ( _list_ _\[_ [_ManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") _\]_)

- **length** ( _int_)


Return type:

[_ManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") \| list\[ [_ManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")\]

interpolate( _other_, _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.interpolate) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.interpolate "Link to this definition")

Interpolate between the current and the given [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"), and return
the result.

Parameters:

- **other** ( _Self_) – The other [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to be used for interpolation.

- **alpha** ( _float_) – A point on the line in RGBA colorspace connecting the two colors, i.e. the
interpolation point. 0.0 corresponds to the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") and
1.0 corresponds to the other [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").


Returns:

The interpolated [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

Return type:

[ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

into( _class\_type_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.into) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.into "Link to this definition")

Convert the current color into a different colorspace given by `class_type`,
without changing the [`_internal_value`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._internal_value "manim.utils.color.core.ManimColor._internal_value").

Parameters:

**class\_type** ( _type_ _\[_ [_ManimColorT_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ManimColorT "manim.utils.color.core.ManimColorT") _\]_) – The class that is used for conversion. It must be a subclass of
[`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") which respects the specification HSV, RGBA, …

Returns:

A new color object of type `class_type` and the same
[`_internal_value`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor._internal_value "manim.utils.color.core.ManimColor._internal_value") as the original color.

Return type:

[ManimColorT](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ManimColorT "manim.utils.color.core.ManimColorT")

invert( _with\_alpha=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.invert) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.invert "Link to this definition")

Return a new, linearly inverted version of this [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") (no
inplace changes).

Parameters:

**with\_alpha** ( _bool_) –

If `True`, the alpha value will be inverted too. Default is `False`.

Note

Setting `with_alpha=True` can result in unintended behavior where
objects are not displayed because their new alpha value is suddenly 0 or
very low.

Returns:

The linearly inverted [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

Return type:

[ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

lighter( _blend=0.2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.lighter) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.lighter "Link to this definition")

Return a new color that is lighter than the current color, i.e.
interpolated with `WHITE`. The opacity is unchanged.

Parameters:

**blend** ( _float_) – The blend ratio for the interpolation, from 0.0 (the current color
unchanged) to 1.0 (pure white). Default is 0.2, which results in a
slightly lighter color.

Returns:

The lighter [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor").

Return type:

[ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

See also

[`darker()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.darker "manim.utils.color.core.ManimColor.darker")

opacity( _opacity_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.opacity) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.opacity "Link to this definition")

Create a new [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") with the given opacity and the same color
values as before.

Parameters:

**opacity** ( _float_) – The new opacity value to be used.

Returns:

The new [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") with the same color values and the new opacity.

Return type:

[ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

_classmethod_ parse( _color:[ParsableManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") \|None_, _alpha:float=1.0_)→Self [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.parse) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.parse "Link to this definition")_classmethod_ parse( _color:Sequence\[ [ParsableManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")\]_, _alpha:float=1.0_)→list\[Self\]

Parse one color as a [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") or a sequence of colors as a list of
[`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")’s.

Parameters:

- **color** – The color or list of colors to parse. Note that this function can not accept
tuples: it will assume that you mean `Sequence[ParsableManimColor]` and will
return a `list[ManimColor]`.

- **alpha** – The alpha (opacity) value to use for the passed color(s).


Returns:

Either a list of colors or a singular color, depending on the input.

Return type:

[ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") \| list\[ [ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")\]

to\_hex( _with\_alpha=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.to_hex) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_hex "Link to this definition")

Convert the [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to a hexadecimal representation of the color.

Parameters:

**with\_alpha** ( _bool_) – If `True`, append 2 extra characters to the hex string which represent the
alpha value of the color between 0 and 255. Default is `False`.

Returns:

A hex string starting with a `#`, with either 6 or 8 nibbles depending on
the `with_alpha` parameter. By default, it has 6 nibbles, i.e. `#XXXXXX`.

Return type:

str

to\_hsl() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.to_hsl) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_hsl "Link to this definition")

Convert the [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to an HSL array.

Note

Be careful: this returns an array in the form `[h, s, l]`, where the
elements are floats. This might be confusing, because RGB can also be an array
of floats. You might want to annotate the usage of this function in your code
by typing your HSL array variables as `HSL_Array_Float` in order to
differentiate them from RGB arrays.

Returns:

An HSL array of 3 floats from 0.0 to 1.0.

Return type:

[HSL\_Array\_Float](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.HSL_Array_Float "manim.typing.HSL_Array_Float")

to\_hsv() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.to_hsv) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_hsv "Link to this definition")

Convert the [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") to an HSV array.

Note

Be careful: this returns an array in the form `[h, s, v]`, where the
elements are floats. This might be confusing, because RGB can also be an array
of floats. You might want to annotate the usage of this function in your code
by typing your HSV array variables as `HSV_Array_Float` in order to
differentiate them from RGB arrays.

Returns:

An HSV array of 3 floats from 0.0 to 1.0.

Return type:

[HSV\_Array\_Float](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.HSV_Array_Float "manim.typing.HSV_Array_Float")

to\_int\_rgb() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.to_int_rgb) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_int_rgb "Link to this definition")

Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGB array of integers.

Returns:

RGB array of 3 integers from 0 to 255.

Return type:

[RGB\_Array\_Int](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGB_Array_Int "manim.typing.RGB_Array_Int")

to\_int\_rgba() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.to_int_rgba) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_int_rgba "Link to this definition")

Convert the current ManimColor into an RGBA array of integers.

Returns:

RGBA array of 4 integers from 0 to 255.

Return type:

[RGBA\_Array\_Int](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGBA_Array_Int "manim.typing.RGBA_Array_Int")

to\_int\_rgba\_with\_alpha( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.to_int_rgba_with_alpha) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_int_rgba_with_alpha "Link to this definition")

Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGBA array of integers. This
is similar to [`to_int_rgba()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_int_rgba "manim.utils.color.core.ManimColor.to_int_rgba"), but you can change the alpha value.

Parameters:

**alpha** ( _float_) – Alpha value to be used for the return value. Pass a float between 0.0 and
1.0: it will automatically be scaled to an integer between 0 and 255.

Returns:

RGBA array of 4 integers from 0 to 255.

Return type:

[RGBA\_Array\_Int](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGBA_Array_Int "manim.typing.RGBA_Array_Int")

to\_integer() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.to_integer) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_integer "Link to this definition")

Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an integer.

Warning

This will return only the RGB part of the color.

Returns:

Integer representation of the color.

Return type:

int

to\_rgb() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.to_rgb) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_rgb "Link to this definition")

Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGB array of floats.

Returns:

RGB array of 3 floats from 0.0 to 1.0.

Return type:

[RGB\_Array\_Float](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGB_Array_Float "manim.typing.RGB_Array_Float")

to\_rgba() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.to_rgba) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_rgba "Link to this definition")

Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGBA array of floats.

Returns:

RGBA array of 4 floats from 0.0 to 1.0.

Return type:

[RGBA\_Array\_Float](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGBA_Array_Float "manim.typing.RGBA_Array_Float")

to\_rgba\_with\_alpha( _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/color/core.html#ManimColor.to_rgba_with_alpha) [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_rgba_with_alpha "Link to this definition")

Convert the current [`ManimColor`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor") into an RGBA array of floats. This is
similar to [`to_rgba()`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor.to_rgba "manim.utils.color.core.ManimColor.to_rgba"), but you can change the alpha value.

Parameters:

**alpha** ( _float_) – Alpha value to be used in the return value.

Returns:

RGBA array of 4 floats from 0.0 to 1.0.

Return type:

[RGBA\_Array\_Float](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.RGBA_Array_Float "manim.typing.RGBA_Array_Float")