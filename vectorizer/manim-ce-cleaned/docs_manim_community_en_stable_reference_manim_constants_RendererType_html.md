# RendererType [¶](https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html\#renderertype "Link to this heading")

Qualified name: `manim.constants.RendererType`

_class_ RendererType( _value_, _names=<notgiven>_, _\*values_, _module=None_, _qualname=None_, _type=None_, _start=1_, _boundary=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/constants.html#RendererType) [¶](https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html#manim.constants.RendererType "Link to this definition")

Bases: `Enum`

An enumeration of all renderer types that can be assigned to
the `config.renderer` attribute.

Manim’s configuration allows assigning string values to the renderer
setting, the values are then replaced by the corresponding enum object.
In other words, you can run:

```
config.renderer = "opengl"

```

Copy to clipboard

and checking the renderer afterwards reveals that the attribute has
assumed the value:

```
<RendererType.OPENGL: 'opengl'>

```

Copy to clipboard

Attributes

|     |     |
| --- | --- |
| [`CAIRO`](https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html#manim.constants.RendererType.CAIRO "manim.constants.RendererType.CAIRO") | A renderer based on the cairo backend. |
| [`OPENGL`](https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html#manim.constants.RendererType.OPENGL "manim.constants.RendererType.OPENGL") | An OpenGL-based renderer. |

CAIRO _='cairo'_ [¶](https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html#manim.constants.RendererType.CAIRO "Link to this definition")

A renderer based on the cairo backend.

OPENGL _='opengl'_ [¶](https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html#manim.constants.RendererType.OPENGL "Link to this definition")

An OpenGL-based renderer.