# v0.1.0 [¶](https://docs.manim.community/en/stable/changelog/0.1.0-changelog.html\#v0-1-0 "Link to this heading")

Date:

October 21, 2020

This is the first release of manimce after forking from 3b1b/manim. As such,
developers have focused on cleaning up and refactoring the codebase while still
maintaining backwards compatibility wherever possible.

## New Features [¶](https://docs.manim.community/en/stable/changelog/0.1.0-changelog.html\#new-features "Link to this heading")

### Command line [¶](https://docs.manim.community/en/stable/changelog/0.1.0-changelog.html\#command-line "Link to this heading")

01. Output of ‘manim –help’ has been improved

02. Implement logging with the `rich` library and a `logger` object instead of plain ol’ prints

03. Added a flag `--dry_run`, which doesn’t write any media

04. Allow for running manim with `python3 -m manim`

05. Refactored Tex Template management. You can now use custom templates with command line args using `--tex_template`!

06. Re-add `--save_frames` flag, which will save each frame as a png

07. Re-introduce manim feature that allows you to type manim code in `stdin` if you pass a minus sign `(-)` as filename

08. Added the `--custom_folders` flag which yields a simpler output folder structure

09. Re-implement GIF export with the `-i` flag (using this flag outputs ONLY a .gif file, and no .mp4 file)

10. Added a `--verbose` flag

11. You can save the logs to a file by using `--log_to_file`

12. Read `tex_template` from config file if not specified by `--tex_template`.

13. Add experimental javascript rendering with `--use_js_renderer`

14. Add `-q/--quality [k|p|h|m|l]` flag and removed `-m/-l` flags.

15. Removed `--sound` flag


### Config system [¶](https://docs.manim.community/en/stable/changelog/0.1.0-changelog.html\#config-system "Link to this heading")

1. Implement a `manim.cfg` config file system, that consolidates the global configuration, the command line argument parsing, and some of the constants defined in `constants.py`

2. Added utilities for manipulating Manim’s `.cfg` files.

3. Added a subcommand structure for easier use of utilities managing `.cfg` files

4. Also some variables have been moved from `constants.py` to the new config system:


> 1. `FRAME_HEIGHT` to `config["frame_width"]`
>
> 2. `TOP` to `config["frame_height"] / 2 * UP`
>
> 3. `BOTTOM` to `config["frame_height"] / 2 * DOWN`
>
> 4. `LEFT_SIDE` to `config["frame_width"] / 2 * LEFT`
>
> 5. `RIGHT_SIDE` to `config["frame_width"] / 2 * RIGHT`
>
> 6. `self.camera.frame_rate` to `config["frame_rate"]`


### Mobjects, Scenes, and Animations [¶](https://docs.manim.community/en/stable/changelog/0.1.0-changelog.html\#mobjects-scenes-and-animations "Link to this heading")

01. Add customizable left and right bracket for `Matrix` mobject and `set_row_colors` method for matrix mobject

02. Add `AddTeXLetterByLetter` animation

03. Enhanced GraphScene


    > 1. You can now add arrow tips to axes
    >
    > 2. extend axes a bit at the start and/or end
    >
    > 3. have invisible axes
    >
    > 4. highlight the area between two curves

04. ThreeDScene now supports 3dillusion\_camera\_rotation

05. Add `z_index` for manipulating depth of Objects on scene.

06. Add a `VDict` class: a `VDict` is to a `VGroup` what a `dict` is to a `list`

07. Added Scene-caching feature. Now, if a partial movie file is unchanged in your code, it isn’t rendered again! \[HIGHLY UNSTABLE We’re working on it ;)\]

08. Most `get_` and `set_` methods have been removed in favor of instance attributes and properties

09. The `Container` class has been made into an AbstractBaseClass, i.e. in cannot be instantiated. Instead, use one of its children classes

10. The `TextMobject` and `TexMobject` objects have been deprecated, due to their confusing names, in favour of `Tex` and `MathTex`. You can still, however, continue to use `TextMobject` and `TexMobject`, albeit with Deprecation Warnings constantly reminding you to switch.

11. Add a `Variable` class for displaying text that continuously updates to reflect the value of a python variable.

12. The `Tex` and `MathTex` objects allow you to specify a custom TexTemplate using the `template` keyword argument.

13. `VGroup` now supports printing the class names of contained mobjects and `VDict` supports printing the internal dict of mobjects

14. Add all the standard easing functions

15. `Scene` now renders when `Scene.render()` is called rather than upon instantiation.

16. `ValueTracker` now supports increment using the += operator (in addition to the already existing increment\_value method)

17. Add `PangoText` for rendering texts using Pango.


## Documentation [¶](https://docs.manim.community/en/stable/changelog/0.1.0-changelog.html\#documentation "Link to this heading")

1. Added clearer installation instructions, tutorials, examples, and API reference \[WIP\]


## Fixes [¶](https://docs.manim.community/en/stable/changelog/0.1.0-changelog.html\#fixes "Link to this heading")

1. Initialization of directories has been moved to `config.py`, and a bunch of bugs associated to file structure generation have been fixed

2. Nonfunctional file `media_dir.txt` has been removed

3. Nonfunctional `if` statements in `scene_file_writer.py` have been removed

4. Fix a bug where trying to render the example scenes without specifying the scene would show all scene objects in the library

5. Many `Exceptions` have been replaced for more specific exception subclasses

6. Fixed a couple of subtle bugs in `ArcBetweenPoints`


## Of interest to developers [¶](https://docs.manim.community/en/stable/changelog/0.1.0-changelog.html\#of-interest-to-developers "Link to this heading")

01. Python code formatting is now enforced by using the `black` tool

02. PRs now require two approving code reviews from community devs before they can be merged

03. Added tests to ensure stuff doesn’t break between commits (For developers) \[Uses Github CI, and Pytest\]

04. Add contribution guidelines (for developers)

05. Added autogenerated documentation with sphinx and autodoc/autosummary \[WIP\]

06. Made manim internally use relative imports

07. Since the introduction of the `TexTemplate` class, the files `tex_template.tex` and `ctex_template.tex` have been removed

08. Added logging tests tools.

09. Added ability to save logs in json

10. Move to Poetry.

11. Colors have moved to an Enum


## Other Changes [¶](https://docs.manim.community/en/stable/changelog/0.1.0-changelog.html\#other-changes "Link to this heading")

1. Cleanup 3b1b Specific Files

2. Rename package from manimlib to manim

3. Move all imports to `__init__`, so `from manim import *` replaces `from manimlib.imports import *`

4. Global dir variable handling has been removed. Instead `initialize_directories`, if needed, overrides the values from the cfg files at runtime.


[**Simplify infrastructure** with MongoDB Atlas, the leading developer data platform](https://server.ethicalads.io/proxy/click/8268/019600e7-1c16-7260-9199-341ea9ebef17/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8268/019600e7-1c16-7260-9199-341ea9ebef17/)