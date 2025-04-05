ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Paragraph [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html\#paragraph "Link to this heading")

Qualified name: `manim.mobject.text.text\_mobject.Paragraph`

_class_ Paragraph( _\*text_, _line\_spacing=-1_, _alignment=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html#Paragraph) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph "Link to this definition")

Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Display a paragraph of text.

For a given [`Paragraph`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph") `par`, the attribute `par.chars` is a
[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") containing all the lines. In this context, every line is
constructed as a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") of characters contained in the line.

Parameters:

- **line\_spacing** ( _float_) – Represents the spacing between lines. Defaults to -1, which means auto.

- **alignment** ( _str_ _\|_ _None_) – Defines the alignment of paragraph. Defaults to None. Possible values are “left”, “right” or “center”.

- **text** ( _Sequence_ _\[_ _str_ _\]_)


Examples

Normal usage:

```
paragraph = Paragraph(
    "this is a awesome",
    "paragraph",
    "With \nNewlines",
    "\tWith Tabs",
    "  With Spaces",
    "With Alignments",
    "center",
    "left",
    "right",
)

```

Copy to clipboard

Remove unwanted invisible characters:

```
self.play(Transform(remove_invisible_chars(paragraph.chars[0:2]),
                    remove_invisible_chars(paragraph.chars[3][0:3]))

```

Copy to clipboard

Methods

|
|

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

\_change\_alignment\_for\_a\_line( _alignment_, _line\_no_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html#Paragraph._change_alignment_for_a_line) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph._change_alignment_for_a_line "Link to this definition")

Function to change one line’s alignment to a specific value.

Parameters:

- **alignment** ( _str_) – Defines the alignment of paragraph. Possible values are “left”, “right”, “center”.

- **line\_no** ( _int_) – Defines the line number for which we want to set given alignment.


Return type:

None

\_gen\_chars( _lines\_str\_list_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html#Paragraph._gen_chars) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph._gen_chars "Link to this definition")

Function to convert a list of plain strings to a VGroup of VGroups of chars.

Parameters:

**lines\_str\_list** ( _list_) – List of plain text strings.

Returns:

The generated 2d-VGroup of chars.

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

\_original\_\_init\_\_( _\*text_, _line\_spacing=-1_, _alignment=None_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **text** ( _Sequence_ _\[_ _str_ _\]_)

- **line\_spacing** ( _float_)

- **alignment** ( _str_ _\|_ _None_)


Return type:

None

\_set\_all\_lines\_alignments( _alignment_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html#Paragraph._set_all_lines_alignments) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph._set_all_lines_alignments "Link to this definition")

Function to set all line’s alignment to a specific value.

Parameters:

**alignment** ( _str_) – Defines the alignment of paragraph. Possible values are “left”, “right”, “center”.

Return type:

[_Paragraph_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph")

\_set\_all\_lines\_to\_initial\_positions() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html#Paragraph._set_all_lines_to_initial_positions) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph._set_all_lines_to_initial_positions "Link to this definition")

Set all lines to their initial positions.

Return type:

[_Paragraph_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph")

\_set\_line\_alignment( _alignment_, _line\_no_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html#Paragraph._set_line_alignment) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph._set_line_alignment "Link to this definition")

Function to set one line’s alignment to a specific value.

Parameters:

- **alignment** ( _str_) – Defines the alignment of paragraph. Possible values are “left”, “right”, “center”.

- **line\_no** ( _int_) – Defines the line number for which we want to set given alignment.


Return type:

[_Paragraph_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph")

\_set\_line\_to\_initial\_position( _line\_no_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/text_mobject.html#Paragraph._set_line_to_initial_position) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph._set_line_to_initial_position "Link to this definition")

Function to set one line to initial positions.

Parameters:

**line\_no** ( _int_) – Defines the line number for which we want to set given alignment.

Return type:

[_Paragraph_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph")