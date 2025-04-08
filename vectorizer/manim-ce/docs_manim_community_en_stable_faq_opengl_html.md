ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/faq/opengl.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/faq/opengl.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# FAQ: OpenGL rendering [¶](https://docs.manim.community/en/stable/faq/opengl.html\#faq-opengl-rendering "Link to this heading")

## Are there any resources on how the OpenGL renderer in the community maintained version can be used? [¶](https://docs.manim.community/en/stable/faq/opengl.html\#are-there-any-resources-on-how-the-opengl-renderer-in-the-community-maintained-version-can-be-used "Link to this heading")

Yes. Unfortunately, at this point, the official online documentation does
not contain the relevant base classes like `OpenGLMobject` and `OpenGLVMobject`
or specific OpenGL classes like `OpenGLSurface`, but documentation for some of
them is available in form of docstrings
[in the source code](https://github.com/ManimCommunity/manim/tree/main/manim/mobject/opengl).

Furthermore, [this user guide by _aquabeam_](https://www.aquabeam.me/manim/opengl_guide/)
can be helpful to get started using the OpenGL renderer.

* * *

## I am trying to run an interactive scene with `--renderer=opengl` and `Scene.interactive_embed`, but an error ( `sqlite3.ProgrammingError`) is raised. How can I fix this? [¶](https://docs.manim.community/en/stable/faq/opengl.html\#i-am-trying-to-run-an-interactive-scene-with-renderer-opengl-and-scene-interactive-embed-but-an-error-sqlite3-programmingerror-is-raised-how-can-i-fix-this "Link to this heading")

This seems to be an issue with a recent IPython release,
in our experience it helps to downgrade the installed `IPython`
package to `8.0.1`: `pip install IPython==8.0.1`.