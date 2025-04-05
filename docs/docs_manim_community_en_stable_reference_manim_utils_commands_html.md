ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.commands.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.commands.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# commands [¶](https://docs.manim.community/en/stable/reference/manim.utils.commands.html\#module-manim.utils.commands "Link to this heading")

Classes

|     |     |
| --- | --- |
| [`VideoMetadata`](https://docs.manim.community/en/stable/reference/manim.utils.commands.VideoMetadata.html#manim.utils.commands.VideoMetadata "manim.utils.commands.VideoMetadata") |  |

Functions

capture( _command_, _cwd=None_, _command\_input=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/commands.html#capture) [¶](https://docs.manim.community/en/stable/reference/manim.utils.commands.html#manim.utils.commands.capture "Link to this definition")Parameters:

- **command** ( _str_)

- **cwd** ( [_StrOrBytesPath_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.StrOrBytesPath "manim.typing.StrOrBytesPath") _\|_ _None_)

- **command\_input** ( _str_ _\|_ _None_)


Return type:

tuple\[str, str, int\]

get\_dir\_layout( _dirpath_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/commands.html#get_dir_layout) [¶](https://docs.manim.community/en/stable/reference/manim.utils.commands.html#manim.utils.commands.get_dir_layout "Link to this definition")

Get list of paths relative to dirpath of all files in dir and subdirs recursively.

Parameters:

**dirpath** ( _Path_)

Return type:

_Generator_\[str, None, None\]

get\_video\_metadata( _path\_to\_video_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/commands.html#get_video_metadata) [¶](https://docs.manim.community/en/stable/reference/manim.utils.commands.html#manim.utils.commands.get_video_metadata "Link to this definition")Parameters:

**path\_to\_video** ( _str_ _\|_ _PathLike_)

Return type:

[_VideoMetadata_](https://docs.manim.community/en/stable/reference/manim.utils.commands.VideoMetadata.html#manim.utils.commands.VideoMetadata "manim.utils.commands.VideoMetadata")