ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ManimConfig [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html\#manimconfig "Link to this heading")

Qualified name: `manim.\_config.utils.ManimConfig`

_class_ ManimConfig [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "Link to this definition")

Bases: `MutableMapping`

Dict-like class storing all config options.

The global `config` object is an instance of this class, and acts as a
single source of truth for all of the library’s customizable behavior.

The global `config` object is capable of digesting different types of
sources and converting them into a uniform interface. These sources are
(in ascending order of precedence): configuration files, command line
arguments, and programmatic changes. Regardless of how the user chooses to
set a config option, she can access its current value using
[`ManimConfig`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "manim._config.utils.ManimConfig")’s attributes and properties.

Notes

Each config option is implemented as a property of this class.

Each config option can be set via a config file, using the full name of the
property. If a config option has an associated CLI flag, then the flag is
equal to the full name of the property. Those that admit an alternative
flag or no flag at all are documented in the individual property’s
docstring.

Examples

We use a copy of the global configuration object in the following
examples for the sake of demonstration; you can skip these lines
and just import `config` directly if you actually want to modify
the configuration:

```
>>> from manim import config as global_config
>>> config = global_config.copy()

```

Copy to clipboard

Each config option allows for dict syntax and attribute syntax. For
example, the following two lines are equivalent,

```
>>> from manim import WHITE
>>> config.background_color = WHITE
>>> config["background_color"] = WHITE

```

Copy to clipboard

The former is preferred; the latter is provided mostly for backwards
compatibility.

The config options are designed to keep internal consistency. For example,
setting `frame_y_radius` will affect `frame_height`:

```
>>> config.frame_height
8.0
>>> config.frame_y_radius = 5.0
>>> config.frame_height
10.0

```

Copy to clipboard

There are many ways of interacting with config options. Take for example
the config option `background_color`. There are three ways to change it:
via a config file, via CLI flags, or programmatically.

To set the background color via a config file, save the following
`manim.cfg` file with the following contents.

```
[CLI]
background_color = WHITE

```

Copy to clipboard

In order to have this `.cfg` file apply to a manim scene, it needs to be
placed in the same directory as the script,

```
project/
├─scene.py
└─manim.cfg

```

Copy to clipboard

Now, when the user executes

```
manim scene.py

```

Copy to clipboard

the background of the scene will be set to `WHITE`. This applies regardless
of where the manim command is invoked from.

Command line arguments override `.cfg` files. In the previous example,
executing

```
manim scene.py -c BLUE

```

Copy to clipboard

will set the background color to BLUE, regardless of the contents of
`manim.cfg`.

Finally, any programmatic changes made within the scene script itself will
override the command line arguments. For example, if `scene.py` contains
the following

```
from manim import *

config.background_color = RED

class MyScene(Scene): ...

```

Copy to clipboard

the background color will be set to RED, regardless of the contents of
`manim.cfg` or the CLI arguments used when invoking manim.

Methods

|     |     |
| --- | --- |
| [`copy`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.copy "manim._config.utils.ManimConfig.copy") | Deepcopy the contents of this ManimConfig. |
| [`digest_args`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_args "manim._config.utils.ManimConfig.digest_args") | Process the config options present in CLI arguments. |
| [`digest_file`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_file "manim._config.utils.ManimConfig.digest_file") | Process the config options present in a `.cfg` file. |
| [`digest_parser`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_parser "manim._config.utils.ManimConfig.digest_parser") | Process the config options present in a `ConfigParser` object. |
| [`get_dir`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.get_dir "manim._config.utils.ManimConfig.get_dir") | Resolve a config option that stores a directory. |
| `resolve_movie_file_extension` |  |
| [`update`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.update "manim._config.utils.ManimConfig.update") | Digest the options found in another [`ManimConfig`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "manim._config.utils.ManimConfig") or in a dict. |

Attributes

|     |     |
| --- | --- |
| [`aspect_ratio`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.aspect_ratio "manim._config.utils.ManimConfig.aspect_ratio") | Aspect ratio (width / height) in pixels (--resolution, -r). |
| [`assets_dir`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.assets_dir "manim._config.utils.ManimConfig.assets_dir") | Directory to locate video assets (no flag). |
| [`background_color`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.background_color "manim._config.utils.ManimConfig.background_color") | Background color of the scene (-c). |
| [`background_opacity`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.background_opacity "manim._config.utils.ManimConfig.background_opacity") | A number between 0.0 (fully transparent) and 1.0 (fully opaque). |
| [`bottom`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.bottom "manim._config.utils.ManimConfig.bottom") | Coordinate at the center bottom of the frame. |
| [`custom_folders`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.custom_folders "manim._config.utils.ManimConfig.custom_folders") | Whether to use custom folder output. |
| [`disable_caching`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.disable_caching "manim._config.utils.ManimConfig.disable_caching") | Whether to use scene caching. |
| [`disable_caching_warning`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.disable_caching_warning "manim._config.utils.ManimConfig.disable_caching_warning") | Whether a warning is raised if there are too much submobjects to hash. |
| [`dry_run`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.dry_run "manim._config.utils.ManimConfig.dry_run") | Whether dry run is enabled. |
| [`enable_gui`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.enable_gui "manim._config.utils.ManimConfig.enable_gui") | Enable GUI interaction. |
| [`enable_wireframe`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.enable_wireframe "manim._config.utils.ManimConfig.enable_wireframe") | Whether to enable wireframe debugging mode in opengl. |
| [`ffmpeg_loglevel`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.ffmpeg_loglevel "manim._config.utils.ManimConfig.ffmpeg_loglevel") | Verbosity level of ffmpeg (no flag). |
| [`flush_cache`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.flush_cache "manim._config.utils.ManimConfig.flush_cache") | Whether to delete all the cached partial movie files. |
| [`force_window`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.force_window "manim._config.utils.ManimConfig.force_window") | Whether to force window when using the opengl renderer. |
| [`format`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.format "manim._config.utils.ManimConfig.format") | File format; "png", "gif", "mp4", "webm" or "mov". |
| [`frame_height`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.frame_height "manim._config.utils.ManimConfig.frame_height") | Frame height in logical units (no flag). |
| [`frame_rate`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.frame_rate "manim._config.utils.ManimConfig.frame_rate") | Frame rate in frames per second. |
| [`frame_size`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.frame_size "manim._config.utils.ManimConfig.frame_size") | Tuple with (pixel width, pixel height) (no flag). |
| [`frame_width`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.frame_width "manim._config.utils.ManimConfig.frame_width") | Frame width in logical units (no flag). |
| [`frame_x_radius`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.frame_x_radius "manim._config.utils.ManimConfig.frame_x_radius") | Half the frame width (no flag). |
| [`frame_y_radius`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.frame_y_radius "manim._config.utils.ManimConfig.frame_y_radius") | Half the frame height (no flag). |
| [`from_animation_number`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.from_animation_number "manim._config.utils.ManimConfig.from_animation_number") | Start rendering animations at this number (-n). |
| [`fullscreen`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.fullscreen "manim._config.utils.ManimConfig.fullscreen") | Expand the window to its maximum possible size. |
| [`gui_location`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.gui_location "manim._config.utils.ManimConfig.gui_location") | Enable GUI interaction. |
| [`images_dir`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.images_dir "manim._config.utils.ManimConfig.images_dir") | Directory to place images (no flag). |
| [`input_file`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.input_file "manim._config.utils.ManimConfig.input_file") | Input file name. |
| [`left_side`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.left_side "manim._config.utils.ManimConfig.left_side") | Coordinate at the middle left of the frame. |
| [`log_dir`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.log_dir "manim._config.utils.ManimConfig.log_dir") | Directory to place logs. |
| [`log_to_file`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.log_to_file "manim._config.utils.ManimConfig.log_to_file") | Whether to save logs to a file. |
| [`max_files_cached`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.max_files_cached "manim._config.utils.ManimConfig.max_files_cached") | Maximum number of files cached. |
| [`media_dir`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.media_dir "manim._config.utils.ManimConfig.media_dir") | Main output directory. |
| [`media_embed`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.media_embed "manim._config.utils.ManimConfig.media_embed") | Whether to embed videos in Jupyter notebook. |
| [`media_width`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.media_width "manim._config.utils.ManimConfig.media_width") | Media width in Jupyter notebook. |
| [`movie_file_extension`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.movie_file_extension "manim._config.utils.ManimConfig.movie_file_extension") | Either .mp4, .webm or .mov. |
| [`no_latex_cleanup`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.no_latex_cleanup "manim._config.utils.ManimConfig.no_latex_cleanup") | Prevents deletion of .aux, .dvi, and .log files produced by Tex and MathTex. |
| [`notify_outdated_version`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.notify_outdated_version "manim._config.utils.ManimConfig.notify_outdated_version") | Whether to notify if there is a version update available. |
| [`output_file`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.output_file "manim._config.utils.ManimConfig.output_file") | Output file name (-o). |
| [`partial_movie_dir`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.partial_movie_dir "manim._config.utils.ManimConfig.partial_movie_dir") | Directory to place partial movie files (no flag). |
| [`pixel_height`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.pixel_height "manim._config.utils.ManimConfig.pixel_height") | Frame height in pixels (--resolution, -r). |
| [`pixel_width`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.pixel_width "manim._config.utils.ManimConfig.pixel_width") | Frame width in pixels (--resolution, -r). |
| [`plugins`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.plugins "manim._config.utils.ManimConfig.plugins") | List of plugins to enable. |
| [`preview`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.preview "manim._config.utils.ManimConfig.preview") | Whether to play the rendered movie (-p). |
| `preview_command` |  |
| [`progress_bar`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.progress_bar "manim._config.utils.ManimConfig.progress_bar") | Whether to show progress bars while rendering animations. |
| [`quality`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.quality "manim._config.utils.ManimConfig.quality") | Video quality (-q). |
| [`renderer`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.renderer "manim._config.utils.ManimConfig.renderer") | The currently active renderer. |
| [`right_side`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.right_side "manim._config.utils.ManimConfig.right_side") | Coordinate at the middle right of the frame. |
| [`save_as_gif`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.save_as_gif "manim._config.utils.ManimConfig.save_as_gif") | Whether to save the rendered scene in .gif format (-i). |
| [`save_last_frame`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.save_last_frame "manim._config.utils.ManimConfig.save_last_frame") | Whether to save the last frame of the scene as an image file (-s). |
| [`save_pngs`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.save_pngs "manim._config.utils.ManimConfig.save_pngs") | Whether to save all frames in the scene as images files (-g). |
| [`save_sections`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.save_sections "manim._config.utils.ManimConfig.save_sections") | Whether to save single videos for each section in addition to the movie file. |
| [`scene_names`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.scene_names "manim._config.utils.ManimConfig.scene_names") | Scenes to play from file. |
| [`sections_dir`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.sections_dir "manim._config.utils.ManimConfig.sections_dir") | Directory to place section videos (no flag). |
| [`show_in_file_browser`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.show_in_file_browser "manim._config.utils.ManimConfig.show_in_file_browser") | Whether to show the output file in the file browser (-f). |
| [`tex_dir`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.tex_dir "manim._config.utils.ManimConfig.tex_dir") | Directory to place tex (no flag). |
| [`tex_template`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.tex_template "manim._config.utils.ManimConfig.tex_template") | Template used when rendering Tex. |
| [`tex_template_file`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.tex_template_file "manim._config.utils.ManimConfig.tex_template_file") | File to read Tex template from (no flag). |
| [`text_dir`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.text_dir "manim._config.utils.ManimConfig.text_dir") | Directory to place text (no flag). |
| [`top`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.top "manim._config.utils.ManimConfig.top") | Coordinate at the center top of the frame. |
| [`transparent`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.transparent "manim._config.utils.ManimConfig.transparent") | Whether the background opacity is less than 1.0 (-t). |
| [`upto_animation_number`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.upto_animation_number "manim._config.utils.ManimConfig.upto_animation_number") | Stop rendering animations at this number. |
| [`use_projection_fill_shaders`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.use_projection_fill_shaders "manim._config.utils.ManimConfig.use_projection_fill_shaders") | Use shaders for OpenGLVMobject fill which are compatible with transformation matrices. |
| [`use_projection_stroke_shaders`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.use_projection_stroke_shaders "manim._config.utils.ManimConfig.use_projection_stroke_shaders") | Use shaders for OpenGLVMobject stroke which are compatible with transformation matrices. |
| [`verbosity`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.verbosity "manim._config.utils.ManimConfig.verbosity") | Logger verbosity; "DEBUG", "INFO", "WARNING", "ERROR", or "CRITICAL" (-v). |
| [`video_dir`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.video_dir "manim._config.utils.ManimConfig.video_dir") | Directory to place videos (no flag). |
| [`window_monitor`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.window_monitor "manim._config.utils.ManimConfig.window_monitor") | The monitor on which the scene will be rendered. |
| [`window_position`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.window_position "manim._config.utils.ManimConfig.window_position") | Set the position of preview window. |
| [`window_size`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.window_size "manim._config.utils.ManimConfig.window_size") | The size of the opengl window. |
| [`write_all`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.write_all "manim._config.utils.ManimConfig.write_all") | Whether to render all scenes in the input file (-a). |
| [`write_to_movie`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.write_to_movie "manim._config.utils.ManimConfig.write_to_movie") | Whether to render the scene to a movie file (-w). |
| [`zero_pad`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.zero_pad "manim._config.utils.ManimConfig.zero_pad") | PNG zero padding. |

\_set\_between( _key_, _val_, _lo_, _hi_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig._set_between) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig._set_between "Link to this definition")

Set `key` to `val` if lo <= val <= hi.

Parameters:

- **key** ( _str_)

- **val** ( _float_)

- **lo** ( _float_)

- **hi** ( _float_)


Return type:

None

\_set\_boolean( _key_, _val_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig._set_boolean) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig._set_boolean "Link to this definition")

Set `key` to `val` if `val` is Boolean.

Parameters:

- **key** ( _str_)

- **val** ( _Any_)


Return type:

None

\_set\_from\_enum( _key_, _enum\_value_, _enum\_class_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig._set_from_enum) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig._set_from_enum "Link to this definition")

Set `key` to the enum object with value `enum_value` in the given
`enum_class`.

Tests:

```
>>> from enum import Enum
>>> class Fruit(Enum):
...     APPLE = 1
...     BANANA = 2
...     CANTALOUPE = 3
>>> test_config = ManimConfig()
>>> test_config._set_from_enum("fruit", 1, Fruit)
>>> test_config._d['fruit']
<Fruit.APPLE: 1>
>>> test_config._set_from_enum("fruit", Fruit.BANANA, Fruit)
>>> test_config._d['fruit']
<Fruit.BANANA: 2>
>>> test_config._set_from_enum("fruit", 42, Fruit)
Traceback (most recent call last):
...
ValueError: 42 is not a valid Fruit

```

Copy to clipboard

Parameters:

- **key** ( _str_)

- **enum\_value** ( _Any_)

- **enum\_class** ( _EnumMeta_)


Return type:

None

\_set\_from\_list( _key_, _val_, _values_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig._set_from_list) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig._set_from_list "Link to this definition")

Set `key` to `val` if `val` is contained in `values`.

Parameters:

- **key** ( _str_)

- **val** ( _Any_)

- **values** ( _list_ _\[_ _Any_ _\]_)


Return type:

None

\_set\_int\_between( _key_, _val_, _lo_, _hi_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig._set_int_between) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig._set_int_between "Link to this definition")

Set `key` to `val` if lo <= val <= hi.

Parameters:

- **key** ( _str_)

- **val** ( _int_)

- **lo** ( _int_)

- **hi** ( _int_)


Return type:

None

\_set\_pos\_number( _key_, _val_, _allow\_inf_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig._set_pos_number) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig._set_pos_number "Link to this definition")

Set `key` to `val` if `val` is a positive integer.

Parameters:

- **key** ( _str_)

- **val** ( _int_)

- **allow\_inf** ( _bool_)


Return type:

None

\_set\_str( _key_, _val_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig._set_str) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig._set_str "Link to this definition")

Set `key` to `val` if `val` is a string.

Parameters:

- **key** ( _str_)

- **val** ( _Any_)


Return type:

None

_property_ aspect\_ratio _:int_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.aspect_ratio "Link to this definition")

Aspect ratio (width / height) in pixels (–resolution, -r).

_property_ assets\_dir _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.assets_dir "Link to this definition")

Directory to locate video assets (no flag).

_property_ background\_color _: [ManimColor](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.background_color "Link to this definition")

Background color of the scene (-c).

_property_ background\_opacity _:float_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.background_opacity "Link to this definition")

A number between 0.0 (fully transparent) and 1.0 (fully opaque).

_property_ bottom _: [Vector3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.bottom "Link to this definition")

Coordinate at the center bottom of the frame.

copy() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig.copy) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.copy "Link to this definition")

Deepcopy the contents of this ManimConfig.

Returns:

A copy of this object containing no shared references.

Return type:

[`ManimConfig`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "manim._config.utils.ManimConfig")

See also

`tempconfig()`

Notes

This is the main mechanism behind `tempconfig()`.

_property_ custom\_folders _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.custom_folders "Link to this definition")

Whether to use custom folder output.

digest\_args( _args_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig.digest_args) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_args "Link to this definition")

Process the config options present in CLI arguments.

Parameters:

**args** ( _argparse.Namespace_) – An object returned by `main_utils.parse_args()`.

Returns:

**self** – This object, after processing the contents of `parser`.

Return type:

[`ManimConfig`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "manim._config.utils.ManimConfig")

See also

`main_utils.parse_args()`, [`digest_parser()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_parser "manim._config.utils.ManimConfig.digest_parser"),
[`digest_file()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_file "manim._config.utils.ManimConfig.digest_file")

Notes

If `args.config_file` is a non-empty string, `ManimConfig` tries to digest the
contents of said file with [`digest_file()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_file "manim._config.utils.ManimConfig.digest_file") before
digesting any other CLI arguments.

digest\_file( _filename_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig.digest_file) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_file "Link to this definition")

Process the config options present in a `.cfg` file.

This method processes a single `.cfg` file, whereas
[`digest_parser()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_parser "manim._config.utils.ManimConfig.digest_parser") can process arbitrary parsers, built
perhaps from multiple `.cfg` files.

Parameters:

**filename** ( [_StrPath_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.StrPath "manim.typing.StrPath")) – Path to the `.cfg` file.

Returns:

**self** – This object, after processing the contents of `filename`.

Return type:

[`ManimConfig`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "manim._config.utils.ManimConfig")

See also

[`digest_file()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_file "manim._config.utils.ManimConfig.digest_file"), [`digest_args()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_args "manim._config.utils.ManimConfig.digest_args"), [`make_config_parser()`](https://docs.manim.community/en/stable/reference/manim._config.utils.html#manim._config.utils.make_config_parser "manim._config.utils.make_config_parser")

Notes

If there are multiple `.cfg` files to process, it is always more
efficient to parse them into a single `ConfigParser` object
first and digesting them with one call to
[`digest_parser()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_parser "manim._config.utils.ManimConfig.digest_parser"), instead of calling this method
multiple times.

digest\_parser( _parser_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig.digest_parser) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_parser "Link to this definition")

Process the config options present in a `ConfigParser` object.

This method processes arbitrary parsers, not only those read from a
single file, whereas [`digest_file()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_file "manim._config.utils.ManimConfig.digest_file") can only process one
file at a time.

Parameters:

**parser** ( _configparser.ConfigParser_) – An object reflecting the contents of one or many `.cfg` files. In
particular, it may reflect the contents of multiple files that have
been parsed in a cascading fashion.

Returns:

**self** – This object, after processing the contents of `parser`.

Return type:

[`ManimConfig`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "manim._config.utils.ManimConfig")

See also

[`make_config_parser()`](https://docs.manim.community/en/stable/reference/manim._config.utils.html#manim._config.utils.make_config_parser "manim._config.utils.make_config_parser"), [`digest_file()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_file "manim._config.utils.ManimConfig.digest_file"), [`digest_args()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_args "manim._config.utils.ManimConfig.digest_args")

Notes

If there are multiple `.cfg` files to process, it is always more
efficient to parse them into a single `ConfigParser` object
first, and then call this function once (instead of calling
[`digest_file()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_file "manim._config.utils.ManimConfig.digest_file") multiple times).

Examples

To digest the config options set in two files, first create a
ConfigParser and parse both files and then digest the parser:

```
parser = configparser.ConfigParser()
parser.read([file1, file2])
config = ManimConfig().digest_parser(parser)

```

Copy to clipboard

In fact, the global `config` object is initialized like so:

```
parser = make_config_parser()
config = ManimConfig().digest_parser(parser)

```

Copy to clipboard

_property_ disable\_caching _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.disable_caching "Link to this definition")

Whether to use scene caching.

_property_ disable\_caching\_warning _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.disable_caching_warning "Link to this definition")

Whether a warning is raised if there are too much submobjects to hash.

_property_ dry\_run _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.dry_run "Link to this definition")

Whether dry run is enabled.

_property_ enable\_gui _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.enable_gui "Link to this definition")

Enable GUI interaction.

_property_ enable\_wireframe _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.enable_wireframe "Link to this definition")

Whether to enable wireframe debugging mode in opengl.

_property_ ffmpeg\_loglevel _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.ffmpeg_loglevel "Link to this definition")

Verbosity level of ffmpeg (no flag).

_property_ flush\_cache _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.flush_cache "Link to this definition")

Whether to delete all the cached partial movie files.

_property_ force\_window _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.force_window "Link to this definition")

Whether to force window when using the opengl renderer.

_property_ format _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.format "Link to this definition")

File format; “png”, “gif”, “mp4”, “webm” or “mov”.

_property_ frame\_height _:float_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.frame_height "Link to this definition")

Frame height in logical units (no flag).

_property_ frame\_rate _:float_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.frame_rate "Link to this definition")

Frame rate in frames per second.

_property_ frame\_size _:tuple\[int,int\]_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.frame_size "Link to this definition")

Tuple with (pixel width, pixel height) (no flag).

_property_ frame\_width _:float_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.frame_width "Link to this definition")

Frame width in logical units (no flag).

_property_ frame\_x\_radius _:float_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.frame_x_radius "Link to this definition")

Half the frame width (no flag).

_property_ frame\_y\_radius _:float_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.frame_y_radius "Link to this definition")

Half the frame height (no flag).

_property_ from\_animation\_number _:int_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.from_animation_number "Link to this definition")

Start rendering animations at this number (-n).

_property_ fullscreen _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.fullscreen "Link to this definition")

Expand the window to its maximum possible size.

get\_dir( _key_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig.get_dir) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.get_dir "Link to this definition")

Resolve a config option that stores a directory.

Config options that store directories may depend on one another. This
method is used to provide the actual directory to the end user.

Parameters:

- **key** ( _str_) – The config option to be resolved. Must be an option ending in
`'_dir'`, for example `'media_dir'` or `'video_dir'`.

- **kwargs** ( _Any_) – Any strings to be used when resolving the directory.


Returns:

Path to the requested directory. If the path resolves to the empty
string, return `None` instead.

Return type:

`pathlib.Path`

Raises:

**KeyError** – When `key` is not a config option that stores a directory and
thus [`get_dir()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.get_dir "manim._config.utils.ManimConfig.get_dir") is not appropriate; or when
`key` is appropriate but there is not enough information to
resolve the directory.

Notes

Standard `str.format()` syntax is used to resolve the paths so the
paths may contain arbitrary placeholders using f-string notation.
However, these will require `kwargs` to contain the required values.

Examples

The value of `config.tex_dir` is `'{media_dir}/Tex'` by default,
i.e. it is a subfolder of wherever `config.media_dir` is located. In
order to get the _actual_ directory, use [`get_dir()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.get_dir "manim._config.utils.ManimConfig.get_dir").

```
>>> from manim import config as globalconfig
>>> config = globalconfig.copy()
>>> config.tex_dir
'{media_dir}/Tex'
>>> config.media_dir
'./media'
>>> config.get_dir("tex_dir").as_posix()
'media/Tex'

```

Copy to clipboard

Resolving directories is done in a lazy way, at the last possible
moment, to reflect any changes in other config options:

```
>>> config.media_dir = "my_media_dir"
>>> config.get_dir("tex_dir").as_posix()
'my_media_dir/Tex'

```

Copy to clipboard

Some directories depend on information that is not available to
[`ManimConfig`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "manim._config.utils.ManimConfig"). For example, the default value of video\_dir
includes the name of the input file and the video quality
(e.g. 480p15). This informamtion has to be supplied via `kwargs`:

```
>>> config.video_dir
'{media_dir}/videos/{module_name}/{quality}'
>>> config.get_dir("video_dir")
Traceback (most recent call last):
KeyError: 'video_dir {media_dir}/videos/{module_name}/{quality} requires the following keyword arguments: module_name'
>>> config.get_dir("video_dir", module_name="myfile").as_posix()
'my_media_dir/videos/myfile/1080p60'

```

Copy to clipboard

Note the quality does not need to be passed as keyword argument since
[`ManimConfig`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "manim._config.utils.ManimConfig") does store information about quality.

Directories may be recursively defined. For example, the config option
`partial_movie_dir` depends on `video_dir`, which in turn depends
on `media_dir`:

```
>>> config.partial_movie_dir
'{video_dir}/partial_movie_files/{scene_name}'
>>> config.get_dir("partial_movie_dir")
Traceback (most recent call last):
KeyError: 'partial_movie_dir {video_dir}/partial_movie_files/{scene_name} requires the following keyword arguments: scene_name'
>>> config.get_dir(
...     "partial_movie_dir", module_name="myfile", scene_name="myscene"
... ).as_posix()
'my_media_dir/videos/myfile/1080p60/partial_movie_files/myscene'

```

Copy to clipboard

Standard f-string syntax is used. Arbitrary names can be used when
defining directories, as long as the corresponding values are passed to
[`ManimConfig.get_dir()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.get_dir "manim._config.utils.ManimConfig.get_dir") via `kwargs`.

```
>>> config.media_dir = "{dir1}/{dir2}"
>>> config.get_dir("media_dir")
Traceback (most recent call last):
KeyError: 'media_dir {dir1}/{dir2} requires the following keyword arguments: dir1'
>>> config.get_dir("media_dir", dir1="foo", dir2="bar").as_posix()
'foo/bar'
>>> config.media_dir = "./media"
>>> config.get_dir("media_dir").as_posix()
'media'

```

Copy to clipboard

_property_ gui\_location _:tuple\[Any\]_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.gui_location "Link to this definition")

Enable GUI interaction.

_property_ images\_dir _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.images_dir "Link to this definition")

Directory to place images (no flag). See [`ManimConfig.get_dir()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.get_dir "manim._config.utils.ManimConfig.get_dir").

_property_ input\_file _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.input_file "Link to this definition")

Input file name.

_property_ left\_side _: [Vector3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.left_side "Link to this definition")

Coordinate at the middle left of the frame.

_property_ log\_dir _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.log_dir "Link to this definition")

Directory to place logs. See [`ManimConfig.get_dir()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.get_dir "manim._config.utils.ManimConfig.get_dir").

_property_ log\_to\_file _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.log_to_file "Link to this definition")

Whether to save logs to a file.

_property_ max\_files\_cached _:int_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.max_files_cached "Link to this definition")

Maximum number of files cached. Use -1 for infinity (no flag).

_property_ media\_dir _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.media_dir "Link to this definition")

Main output directory. See [`ManimConfig.get_dir()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.get_dir "manim._config.utils.ManimConfig.get_dir").

_property_ media\_embed _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.media_embed "Link to this definition")

Whether to embed videos in Jupyter notebook.

_property_ media\_width _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.media_width "Link to this definition")

Media width in Jupyter notebook.

_property_ movie\_file\_extension _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.movie_file_extension "Link to this definition")

Either .mp4, .webm or .mov.

_property_ no\_latex\_cleanup _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.no_latex_cleanup "Link to this definition")

Prevents deletion of .aux, .dvi, and .log files produced by Tex and MathTex.

_property_ notify\_outdated\_version _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.notify_outdated_version "Link to this definition")

Whether to notify if there is a version update available.

_property_ output\_file _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.output_file "Link to this definition")

Output file name (-o).

_property_ partial\_movie\_dir _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.partial_movie_dir "Link to this definition")

Directory to place partial movie files (no flag). See [`ManimConfig.get_dir()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.get_dir "manim._config.utils.ManimConfig.get_dir").

_property_ pixel\_height _:int_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.pixel_height "Link to this definition")

Frame height in pixels (–resolution, -r).

_property_ pixel\_width _:int_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.pixel_width "Link to this definition")

Frame width in pixels (–resolution, -r).

_property_ plugins _:list\[str\]_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.plugins "Link to this definition")

List of plugins to enable.

_property_ preview _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.preview "Link to this definition")

Whether to play the rendered movie (-p).

_property_ progress\_bar _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.progress_bar "Link to this definition")

Whether to show progress bars while rendering animations.

_property_ quality _:str\|None_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.quality "Link to this definition")

Video quality (-q).

_property_ renderer _: [RendererType](https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html#manim.constants.RendererType "manim.constants.RendererType")_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.renderer "Link to this definition")

The currently active renderer.

Populated with one of the available renderers in [`RendererType`](https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html#manim.constants.RendererType "manim.constants.RendererType").

Tests:

```
>>> test_config = ManimConfig()
>>> test_config.renderer is None  # a new ManimConfig is unpopulated
True
>>> test_config.renderer = 'opengl'
>>> test_config.renderer
<RendererType.OPENGL: 'opengl'>
>>> test_config.renderer = 42
Traceback (most recent call last):
...
ValueError: 42 is not a valid RendererType

```

Copy to clipboard

Check that capitalization of renderer types is irrelevant:

```
>>> test_config.renderer = 'OpenGL'
>>> test_config.renderer = 'cAirO'

```

Copy to clipboard

_property_ right\_side _: [Vector3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.right_side "Link to this definition")

Coordinate at the middle right of the frame.

_property_ save\_as\_gif _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.save_as_gif "Link to this definition")

Whether to save the rendered scene in .gif format (-i).

_property_ save\_last\_frame _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.save_last_frame "Link to this definition")

Whether to save the last frame of the scene as an image file (-s).

_property_ save\_pngs _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.save_pngs "Link to this definition")

Whether to save all frames in the scene as images files (-g).

_property_ save\_sections _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.save_sections "Link to this definition")

Whether to save single videos for each section in addition to the movie file.

_property_ scene\_names _:list\[str\]_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.scene_names "Link to this definition")

Scenes to play from file.

_property_ sections\_dir _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.sections_dir "Link to this definition")

Directory to place section videos (no flag). See [`ManimConfig.get_dir()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.get_dir "manim._config.utils.ManimConfig.get_dir").

_property_ show\_in\_file\_browser _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.show_in_file_browser "Link to this definition")

Whether to show the output file in the file browser (-f).

_property_ tex\_dir _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.tex_dir "Link to this definition")

Directory to place tex (no flag). See [`ManimConfig.get_dir()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.get_dir "manim._config.utils.ManimConfig.get_dir").

_property_ tex\_template _: [TexTemplate](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate "manim.utils.tex.TexTemplate")_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.tex_template "Link to this definition")

Template used when rendering Tex. See [`TexTemplate`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate "manim.utils.tex.TexTemplate").

_property_ tex\_template\_file _:Path_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.tex_template_file "Link to this definition")

File to read Tex template from (no flag). See [`TexTemplate`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate "manim.utils.tex.TexTemplate").

_property_ text\_dir _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.text_dir "Link to this definition")

Directory to place text (no flag). See [`ManimConfig.get_dir()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.get_dir "manim._config.utils.ManimConfig.get_dir").

_property_ top _: [Vector3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.top "Link to this definition")

Coordinate at the center top of the frame.

_property_ transparent _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.transparent "Link to this definition")

Whether the background opacity is less than 1.0 (-t).

update( _obj_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/utils.html#ManimConfig.update) [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.update "Link to this definition")

Digest the options found in another [`ManimConfig`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "manim._config.utils.ManimConfig") or in a dict.

Similar to `dict.update()`, replaces the values of this object with
those of `obj`.

Parameters:

**obj** ( [_ManimConfig_](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "manim._config.utils.ManimConfig") _\|_ _dict_ _\[_ _str_ _,_ _Any_ _\]_) – The object to copy values from.

Return type:

None

Raises:

**AttributeError** – If `obj` is a dict but contains keys that do not belong to any
config options.

See also

[`digest_file()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_file "manim._config.utils.ManimConfig.digest_file"), [`digest_args()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_args "manim._config.utils.ManimConfig.digest_args"), [`digest_parser()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.digest_parser "manim._config.utils.ManimConfig.digest_parser")

_property_ upto\_animation\_number _:int_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.upto_animation_number "Link to this definition")

Stop rendering animations at this number. Use -1 to avoid skipping (-n).

_property_ use\_projection\_fill\_shaders _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.use_projection_fill_shaders "Link to this definition")

Use shaders for OpenGLVMobject fill which are compatible with transformation matrices.

_property_ use\_projection\_stroke\_shaders _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.use_projection_stroke_shaders "Link to this definition")

Use shaders for OpenGLVMobject stroke which are compatible with transformation matrices.

_property_ verbosity _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.verbosity "Link to this definition")

Logger verbosity; “DEBUG”, “INFO”, “WARNING”, “ERROR”, or “CRITICAL” (-v).

_property_ video\_dir _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.video_dir "Link to this definition")

Directory to place videos (no flag). See [`ManimConfig.get_dir()`](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.get_dir "manim._config.utils.ManimConfig.get_dir").

_property_ window\_monitor _:int_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.window_monitor "Link to this definition")

The monitor on which the scene will be rendered.

_property_ window\_position _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.window_position "Link to this definition")

Set the position of preview window. You can use directions, e.g. UL/DR/ORIGIN/LEFT…or the position(pixel) of the upper left corner of the window, e.g. ‘960,540’.

_property_ window\_size _:str_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.window_size "Link to this definition")

The size of the opengl window. ‘default’ to automatically scale the window based on the display monitor.

_property_ write\_all _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.write_all "Link to this definition")

Whether to render all scenes in the input file (-a).

_property_ write\_to\_movie _:bool_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.write_to_movie "Link to this definition")

Whether to render the scene to a movie file (-w).

_property_ zero\_pad _:int_ [¶](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig.zero_pad "Link to this definition")

PNG zero padding. A number between 0 (no zero padding) and 9 (9 columns minimum).