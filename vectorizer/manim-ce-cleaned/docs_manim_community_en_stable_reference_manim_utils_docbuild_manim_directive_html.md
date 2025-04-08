# manim\_directive [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.html\#module-manim.utils.docbuild.manim_directive "Link to this heading")

## A directive for including Manim videos in a Sphinx document [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.html\#a-directive-for-including-manim-videos-in-a-sphinx-document "Link to this heading")

When rendering the HTML documentation, the `.. manim::` directive
implemented here allows to include rendered videos.

Its basic usage that allows processing **inline content**
looks as follows:

```
.. manim:: MyScene

    class MyScene(Scene):
        def construct(self):
            ...

```

Copy to clipboard

It is required to pass the name of the class representing the
scene to be rendered to the directive.

As a second application, the directive can also be used to
render scenes that are defined within doctests, for example:

```
.. manim:: DirectiveDoctestExample
    :ref_classes: Dot

    >>> from manim import Create, Dot, RED, Scene
    >>> dot = Dot(color=RED)
    >>> dot.color
    ManimColor('#FC6255')
    >>> class DirectiveDoctestExample(Scene):
    ...     def construct(self):
    ...         self.play(Create(dot))

```

Copy to clipboard

### Options [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.html\#options "Link to this heading")

Options can be passed as follows:

```
.. manim:: <Class name>
    :<option name>: <value>

```

Copy to clipboard

The following configuration options are supported by the
directive:

> hide\_source
>
> If this flag is present without argument,
> the source code is not displayed above the rendered video.
>
> no\_autoplay
>
> If this flag is present without argument,
> the video will not autoplay.
>
> quality{‘low’, ‘medium’, ‘high’, ‘fourk’}
>
> Controls render quality of the video, in analogy to
> the corresponding command line flags.
>
> save\_as\_gif
>
> If this flag is present without argument,
> the scene is rendered as a gif.
>
> save\_last\_frame
>
> If this flag is present without argument,
> an image representing the last frame of the scene will
> be rendered and displayed, instead of a video.
>
> ref\_classes
>
> A list of classes, separated by spaces, that is
> rendered in a reference block after the source code.
>
> ref\_functions
>
> A list of functions, separated by spaces,
> that is rendered in a reference block after the source code.
>
> ref\_methods
>
> A list of methods, separated by spaces,
> that is rendered in a reference block after the source code.

Classes

|     |     |
| --- | --- |
| [`ManimDirective`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#manim.utils.docbuild.manim_directive.ManimDirective "manim.utils.docbuild.manim_directive.ManimDirective") | The manim directive, rendering videos while building the documentation. |
| [`SetupMetadata`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.SetupMetadata.html#manim.utils.docbuild.manim_directive.SetupMetadata "manim.utils.docbuild.manim_directive.SetupMetadata") |  |
| [`SkipManimNode`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.SkipManimNode.html#manim.utils.docbuild.manim_directive.SkipManimNode "manim.utils.docbuild.manim_directive.SkipManimNode") | Auxiliary node class that is used when the `skip-manim` tag is present or `.pot` files are being built. |

Functions

depart( _self_, _node_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/manim_directive.html#depart) [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.html#manim.utils.docbuild.manim_directive.depart "Link to this definition")Parameters:

- **self** ( [_SkipManimNode_](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.SkipManimNode.html#manim.utils.docbuild.manim_directive.SkipManimNode "manim.utils.docbuild.manim_directive.SkipManimNode"))

- **node** ( _Element_)


Return type:

None

process\_name\_list( _option\_input_, _reference\_type_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/manim_directive.html#process_name_list) [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.html#manim.utils.docbuild.manim_directive.process_name_list "Link to this definition")

Reformats a string of space separated class names
as a list of strings containing valid Sphinx references.

Tests

```
>>> process_name_list("Tex TexTemplate", "class")
[':class:`~.Tex`', ':class:`~.TexTemplate`']
>>> process_name_list("Scene.play Mobject.rotate", "func")
[':func:`~.Scene.play`', ':func:`~.Mobject.rotate`']

```

Copy to clipboard

Parameters:

- **option\_input** ( _str_)

- **reference\_type** ( _str_)


Return type:

list\[str\]

setup( _app_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/manim_directive.html#setup) [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.html#manim.utils.docbuild.manim_directive.setup "Link to this definition")Parameters:

**app** ( _Sphinx_)

Return type:

[SetupMetadata](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.SetupMetadata.html#manim.utils.docbuild.manim_directive.SetupMetadata "manim.utils.docbuild.manim_directive.SetupMetadata")

visit( _self_, _node_, _name=''_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/manim_directive.html#visit) [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.html#manim.utils.docbuild.manim_directive.visit "Link to this definition")Parameters:

- **self** ( [_SkipManimNode_](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.SkipManimNode.html#manim.utils.docbuild.manim_directive.SkipManimNode "manim.utils.docbuild.manim_directive.SkipManimNode"))

- **node** ( _Element_)

- **name** ( _str_)


Return type:

None