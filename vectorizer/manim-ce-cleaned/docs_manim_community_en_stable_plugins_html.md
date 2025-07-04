# Plugins [¶](https://docs.manim.community/en/stable/plugins.html\#plugins "Link to this heading")

Plugins are features that extend Manim’s core functionality. Since Manim is
extensible and not everything belongs in its core, we’ll go over how to
install, use, and create your own plugins.

Note

The standard naming convention for plugins is to prefix the plugin with
`manim-`. This makes them easy for users to find on package
repositories such as PyPI.

Warning

The plugin feature is new and under active development. Expect updates
for the best practices on installing, using, and creating plugins; as
well as new subcommands/flags for `manim plugins`

Tip

See [https://plugins.manim.community/](https://plugins.manim.community/) for the list of plugins available.

## Installing Plugins [¶](https://docs.manim.community/en/stable/plugins.html\#installing-plugins "Link to this heading")

Plugins can be easily installed via the `pip`
command:

```
pip install manim-*

```

Copy to clipboard

After installing a plugin, you may use the `manim plugins` command to list
your available plugins, see the following help output:

```
manim plugins -h
Usage: manim plugins [OPTIONS]

  Manages Manim plugins.

Options:
-l, --list  List available plugins
-h, --help  Show this message and exit.

Made with <3 by Manim Community developers.

```

Copy to clipboard

You can list plugins as such:

```
manim plugins -l
Plugins:
• manim_plugintemplate

```

Copy to clipboard

## Using Plugins in Projects [¶](https://docs.manim.community/en/stable/plugins.html\#using-plugins-in-projects "Link to this heading")

For enabling a plugin `manim.cfg` or command line parameters should be used.

Important

The plugins should be module name of the plugin and not PyPi name.

Enabling plugins through `manim.cfg`

```
[CLI]
plugins = manim_rubikscube

```

Copy to clipboard

For specifying multiple plugins, comma-separated values must be used.

```
[CLI]
plugins = manim_rubikscube, manim_plugintemplate

```

Copy to clipboard

## Creating Plugins [¶](https://docs.manim.community/en/stable/plugins.html\#creating-plugins "Link to this heading")

Plugins are intended to extend Manim’s core functionality. If you aren’t sure
whether a feature should be included in Manim’s core, feel free to ask over
on the [Discord server](https://www.manim.community/discord/). Visit
[manim-plugintemplate](https://pypi.org/project/manim-plugintemplate/)
on PyPI.org which serves as an in-depth tutorial for creating plugins.

```
pip install manim-plugintemplate

```

Copy to clipboard

The only requirement of manim plugins is that they specify an entry point
with the group, `"manim.plugins"`. This allows Manim to discover plugins
available in the user’s environment. Everything regarding the plugin’s
directory structure, build system, and naming are completely up to your
discretion as an author. The aforementioned template plugin is only a model
using Poetry since this is the build system Manim uses. The plugin’s [entry\\
point](https://packaging.python.org/specifications/entry-points/) can be
specified in Poetry as:

```
[tool.poetry.plugins."manim.plugins"]
"name" = "object_reference"

```

Copy to clipboard

Removed in version 0.18.1: Plugins should be imported explicitly to be usable in user code. The plugin
system will probably be refactored in the future to provide a more structured
interface.

### A note on Renderer Compatibility [¶](https://docs.manim.community/en/stable/plugins.html\#a-note-on-renderer-compatibility "Link to this heading")

Depending on which renderer is currently active, custom mobjects
created in your plugin might want to behave differently as the
corresponding mobject base classes are (unfortunately) not fully
compatible.

The currently active renderer can be queried by checking the value
of `manim.config.renderer`. All possible renderer types are given
by [`constants.RendererType`](https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html#manim.constants.RendererType "manim.constants.RendererType"). The module [`manim.mobject.utils`](https://docs.manim.community/en/stable/reference/manim.mobject.utils.html#module-manim.mobject.utils "manim.mobject.utils")
contains utility functions that return the base class for the currently
active renderer.

A simple form of renderer compatibility (by hot-swapping the class
inheritance chain) for Mobjects directly inheriting from
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") or [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") can be achieved by using the
`mobject.opengl.opengl_compatibility.ConvertToOpenGL` metaclass.