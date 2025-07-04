ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/faq/general.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/faq/general.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# FAQ: General Usage [¶](https://docs.manim.community/en/stable/faq/general.html\#faq-general-usage "Link to this heading")

## Why does Manim say that “there are no scenes inside that module”? [¶](https://docs.manim.community/en/stable/faq/general.html\#why-does-manim-say-that-there-are-no-scenes-inside-that-module "Link to this heading")

There are two main reasons why this error appears: if you have edited
the file containing your `Scene` class and forgot to save it, or if you
have accidentally passed the name of a wrong file to `manim`, this is
a likely outcome. Check that you have spelled everything correctly.

Otherwise, you are likely mixing up Manim versions. See [this FAQ answer](https://docs.manim.community/en/stable/faq/installation.html#different-versions)
for an explanation regarding why there are different versions. Under the
assumption that you are trying to use the `manim` executable from the terminal to run
a scene that has been written for the community version (i.e., there is
`from manim import *`, or more specifically `from manim import Scene`),
then this error indicates that the `manim` executable has been overwritten
by the one provided by `manimgl` (unfortunately, both `manim` and `manimgl`
provide a `manim` executable).

You can check whether this is the case by running `manim --version`, the output of
the community maintained version starts with `Manim Community v...`. If this is not
the case, you are running `manimgl`.

You can resolve this by either of the following steps:

- Un- and reinstalling `manim`,

- using the `manimce` executable in place of the `manim` one,

- or replacing the call to the executable with a direct call to the
Python module via `python -m manim`.


* * *

## No matter what code I put in my file, Manim only renders a black frame! Why? [¶](https://docs.manim.community/en/stable/faq/general.html\#no-matter-what-code-i-put-in-my-file-manim-only-renders-a-black-frame-why "Link to this heading")

If you are using the usual pattern to write a `Scene`, i.e.,

```
class MyAwesomeScene(Scene):
    def construct(self):
        ...
        # your animation code

```

Copy to clipboard

then double check whether you have spelled `construct` correctly.
If the method containing your code is not called `construct` (or
if you are not calling a different, custom method from `construct`),
Manim will not call your method and simply output a black frame.

* * *

## What are the default measurements for Manim’s scene? [¶](https://docs.manim.community/en/stable/faq/general.html\#what-are-the-default-measurements-for-manim-s-scene "Link to this heading")

The scene measures 8 units in height and has a default ratio of 16:9,
which means that it measures 8⋅16/9=14+2/9 units in width.
The origin is in the center of the scene, which means that, for example, the
upper left corner of the scene has coordinates `[-7-1/9, 4, 0]`.

* * *

## How do I find out which keyword arguments I can pass when creating a `Mobject`? [¶](https://docs.manim.community/en/stable/faq/general.html\#how-do-i-find-out-which-keyword-arguments-i-can-pass-when-creating-a-mobject "Link to this heading")

Let us consider a specific example, like the [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle") class. When looking
at its documentation page, only two specific keyword arguments are listed
( `radius`, and `color`). Besides these concrete arguments, there is also a
catchall `**kwargs` argument which captures all other arguments that are passed
to `Circle`, and passes them on to the base class of [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle"), [`Arc`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc").

The same holds for [`Arc`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc"): some arguments are explicitly documented, and
there is again a catchall `**kwargs` argument that passes unprocessed arguments
to the next base class – and so on.

The most important keyword arguments relevant to styling your mobjects are the
ones that are documented for the base classes [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") and
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

* * *

## Can Manim render a video with transparent background? [¶](https://docs.manim.community/en/stable/faq/general.html\#can-manim-render-a-video-with-transparent-background "Link to this heading")

Yes: simply pass the CLI flag `-t` (or its long form `--transparent`).
Note that the default video file format does not support transparency,
which is why Manim will output a `.mov` instead of a `.mp4` when
rendering with a transparent background. Other movie file formats
that support transparency can be obtained by passing
`--format=webm` or `--format=gif`.

* * *

## I have watched a video where a creator ran command X, but it does not work for me. Why? [¶](https://docs.manim.community/en/stable/faq/general.html\#i-have-watched-a-video-where-a-creator-ran-command-x-but-it-does-not-work-for-me-why "Link to this heading")

The video you have been watching is likely outdated. If you want to follow
along, you either need to use the same version used in the video, or
modify the code (in many cases it is just a method having been renamed etc.)
accordingly. Check the video description, in some cases creators point out
whether changes need to be applied to the code shown in the video.

* * *

## When using `Tex` or `MathTex`, some letters are missing. How can I fix this? [¶](https://docs.manim.community/en/stable/faq/general.html\#when-using-tex-or-mathtex-some-letters-are-missing-how-can-i-fix-this "Link to this heading")

It is possible that you have to (re)build some fonts used by LaTeX. For
some distributions, you can do this manually by running

```
fmtutil -sys --all

```

Copy to clipboard

We recommend consulting the documentation of your LaTeX distribution
for more information.

* * *

## I want to translate some code from `manimgl` to `manim`, what do I do with `CONFIG` dictionaries? [¶](https://docs.manim.community/en/stable/faq/general.html\#i-want-to-translate-some-code-from-manimgl-to-manim-what-do-i-do-with-config-dictionaries "Link to this heading")

The community-maintained version has dropped the use of `CONFIG` dictionaries very
early, with [version v0.2.0](https://docs.manim.community/en/stable/changelog/0.2.0-changelog.html) released in
January 2021.

Before that, Manim’s classes basically processed `CONFIG` dictionaries
by mimicking inheritance (to properly process `CONFIG` dictionaries set
by parent classes) and then assigning all of the key-value-pairs in the
dictionary as attributes of the corresponding object.

In situations where there is not much inheritance going on,
or for any custom setting, you should set these attributes yourself.
For example, for an old-style `Scene` with custom attributes like

```
class OldStyle(Scene):
    CONFIG = {"a": 1, "b": 2}

```

Copy to clipboard

should be written as

```
class NewStyle(Scene):
    a = 1
    b = 2

```

Copy to clipboard

In situations where values should be properly inherited, the arguments
should be added to the initialization function of the class. An old-style
mobject `Thing` could look like

```
class Thing(VMobject):
    CONFIG = {
        "stroke_color": RED,
        "fill_opacity": 0.7,
        "my_awesome_argument": 42,
    }

```

Copy to clipboard

where `stroke_color` and `fill_opacity` are arguments that concern the
parent class of `Thing`, and `my_awesome_argument` is a custom argument
that only concerns `Thing`. A version without `CONFIG` could look like this:

```
class Thing(VMobject):
    def __init__(
        self, stroke_color=RED, fill_opacity=0.7, my_awesome_argument=42, **kwargs
    ):
        self.my_awesome_argument = my_awesome_argument
        super().__init__(stroke_color=stroke_color, fill_opacity=fill_opacity, **kwargs)

```

Copy to clipboard

* * *

## My installation does not support converting PDF to SVG, help? [¶](https://docs.manim.community/en/stable/faq/general.html\#my-installation-does-not-support-converting-pdf-to-svg-help "Link to this heading")

This is an issue with `dvisvgm`, the tool shipped with LaTeX that
transforms LaTeX output to a `.svg` file that
Manim can parse.

First, make sure your `dvisvgm` version is at least 2.4 by
checking the output of

```
dvisvgm --version

```

Copy to clipboard

If you do not know how to update `dvisvgm`, please refer to your
LaTeX distributions documentation (or the documentation of your
operating system, if `dvisvgm` was installed as a system package).

Second, check whether your `dvisvgm` supports PostScript specials. This is
needed to convert from PDF to SVG. Run:

```
dvisvgm -l

```

Copy to clipboard

If the output to this command does **not** contain `ps  dvips PostScript specials`,
this is a bad sign. In this case, run

```
dvisvgm -h

```

Copy to clipboard

If the output does **not** contain `--libgs=filename`, this means your
`dvisvgm` does not currently support PostScript. You must get another binary.

If, however, `--libgs=filename` appears in the help, that means that your
`dvisvgm` needs the Ghostscript library to support PostScript. Search for
`libgs.so` (on Linux, probably in `/usr/local/lib` or `/usr/lib`) or
`gsdll32.dll` (on 32-bit Windows, probably in `C:\windows\system32`) or
`gsdll64.dll` (on 64-bit Windows, also probably in `C:\windows\system32`)
or `libgsl.dylib` (on MacOS, probably in `/usr/local/lib` or
`/opt/local/lib`). Please look carefully, as the file might be located
elsewhere, e.g. in the directory where Ghostscript is installed.

When you have found the library, try (on MacOS or Linux)

```
export LIBGS=<path to your library including the file name>
dvisvgm -l

```

Copy to clipboard

or (on Windows)

```
set LIBGS=<path to your library including the file name>
dvisvgm -l

```

Copy to clipboard

You should now see `ps    dvips PostScript specials` in the output. Refer to
your operating system’s documentation to find out how you can set or export the
environment variable `LIBGS` automatically whenever you open a shell.

As a last check, you can run

```
dvisvgm -V1

```

Copy to clipboard

(while still having `LIBGS` set to the correct path, of course.) If `dvisvgm`
can find your Ghostscript installation, it will be shown in the output together
with the version number.

If you do not have the necessary library on your system, please refer to your
operating system’s documentation to find out where you can get it and how you
have to install it.

If you are unable to solve your problem, check out the
[dvisvgm FAQ](https://dvisvgm.de/FAQ/).

* * *

## Where can I find more resources for learning Manim? [¶](https://docs.manim.community/en/stable/faq/general.html\#where-can-i-find-more-resources-for-learning-manim "Link to this heading")

In our [Discord server](https://manim.community/discord), we have the community-maintained
`#beginner-resources` channel in which links to helpful learning resources are collected.
You are welcome to join our Discord and take a look yourself! If you have found some
guides or tutorials yourself that are not on our list yet, feel free to add them!