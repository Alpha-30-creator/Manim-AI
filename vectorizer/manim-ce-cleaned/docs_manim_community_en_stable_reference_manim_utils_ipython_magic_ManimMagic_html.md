# ManimMagic [¶](https://docs.manim.community/en/stable/reference/manim.utils.ipython_magic.ManimMagic.html\#manimmagic "Link to this heading")

Qualified name: `manim.utils.ipython\_magic.ManimMagic`

_class_ ManimMagic( _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/ipython_magic.html#ManimMagic) [¶](https://docs.manim.community/en/stable/reference/manim.utils.ipython_magic.ManimMagic.html#manim.utils.ipython_magic.ManimMagic "Link to this definition")

Bases: `Magics`

Create a configurable given a config config.

Parameters:

- **config** ( _Config_) – If this is empty, default values are used. If config is a
`Config` instance, it will be used to configure the
instance.

- **parent** ( _Configurable instance_ _,_ _optional_) – The parent Configurable instance of this object.

- **shell** ( _InteractiveShell_)


Notes

Subclasses of Configurable must call the `__init__()` method of
`Configurable` _before_ doing anything else and using
`super()`:

```
class MyConfigurable(Configurable):
    def __init__(self, config=None):
        super(MyConfigurable, self).__init__(config=config)
        # Then any other code you need to finish initialization.

```

Copy to clipboard

This ensures that instances will be configured properly.

Methods

|     |     |
| --- | --- |
| `add_additional_args` |  |
| [`manim`](https://docs.manim.community/en/stable/reference/manim.utils.ipython_magic.ManimMagic.html#manim.utils.ipython_magic.ManimMagic.manim "manim.utils.ipython_magic.ManimMagic.manim") | Render Manim scenes contained in IPython cells. |

Attributes

|     |     |
| --- | --- |
| `config` | A trait whose value must be an instance of a specified class. |
| `cross_validation_lock` | A contextmanager for running a block with our cross validation lock set to True. |
| `magics` |  |
| `options_table` |  |
| `parent` | A trait whose value must be an instance of a specified class. |
| `registered` |  |
| `shell` |  |

manim( _line_, _cell=None_, _local\_ns=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/ipython_magic.html#ManimMagic.manim) [¶](https://docs.manim.community/en/stable/reference/manim.utils.ipython_magic.ManimMagic.html#manim.utils.ipython_magic.ManimMagic.manim "Link to this definition")

Render Manim scenes contained in IPython cells.
Works as a line or cell magic.

Hint

This line and cell magic works best when used in a JupyterLab
environment: while all of the functionality is available for
classic Jupyter notebooks as well, it is possible that videos
sometimes don’t update on repeated execution of the same cell
if the scene name stays the same.

This problem does not occur when using JupyterLab.

Please refer to [https://jupyter.org/](https://jupyter.org/) for more information about JupyterLab
and Jupyter notebooks.

Usage in line mode:

```
%manim [CLI options] MyAwesomeScene

```

Copy to clipboard

Usage in cell mode:

```
%%manim [CLI options] MyAwesomeScene

class MyAweseomeScene(Scene):
    def construct(self):
        ...

```

Copy to clipboard

Run `%manim --help` and `%manim render --help` for possible command line interface options.

Note

The maximal width of the rendered videos that are displayed in the notebook can be
configured via the `media_width` configuration option. The default is set to `25vw`,
which is 25% of your current viewport width. To allow the output to become as large
as possible, set `config.media_width = "100%"`.

The `media_embed` option will embed the image/video output in the notebook. This is
generally undesirable as it makes the notebooks very large, but is required on some
platforms (notably Google’s CoLab, where it is automatically enabled unless suppressed
by `config.embed = False`) and needed in cases when the notebook (or converted HTML
file) will be moved relative to the video locations. Use-cases include building
documentation with Sphinx and JupyterBook. See also the [`manim directive for Sphinx`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.html#module-manim.utils.docbuild.manim_directive "manim.utils.docbuild.manim_directive").

Examples

First make sure to put `import manim`, or even `from manim import *`
in a cell and evaluate it. Then, a typical Jupyter notebook cell for Manim
could look as follows:

```
%%manim -v WARNING --disable_caching -qm BannerExample

config.media_width = "75%"
config.media_embed = True

class BannerExample(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        banner_large = ManimBanner(dark_theme=False).scale(0.7)
        self.play(banner_large.create())
        self.play(banner_large.expand())

```

Copy to clipboard

Evaluating this cell will render and display the `BannerExample` scene defined in the body of the cell.

Note

In case you want to hide the red box containing the output progress bar, the `progress_bar` config
option should be set to `None`. This can also be done by passing `--progress_bar None` as a
CLI flag.

Parameters:

- **line** ( _str_)

- **cell** ( _str_ _\|_ _None_)

- **local\_ns** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)


Return type:

None