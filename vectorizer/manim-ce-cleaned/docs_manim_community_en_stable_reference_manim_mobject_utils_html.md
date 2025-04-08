# utils [¶](https://docs.manim.community/en/stable/reference/manim.mobject.utils.html\#module-manim.mobject.utils "Link to this heading")

Utilities for working with mobjects.

Functions

get\_mobject\_class() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/utils.html#get_mobject_class) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.utils.html#manim.mobject.utils.get_mobject_class "Link to this definition")

Gets the base mobject class, depending on the currently active renderer.

Note

This method is intended to be used in the code base of Manim itself
or in plugins where code should work independent of the selected
renderer.

Examples

The function has to be explicitly imported. We test that
the name of the returned class is one of the known mobject
base classes:

```
>>> from manim.mobject.utils import get_mobject_class
>>> get_mobject_class().__name__ in ['Mobject', 'OpenGLMobject']
True

```

Copy to clipboard

Return type:

type

get\_point\_mobject\_class() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/utils.html#get_point_mobject_class) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.utils.html#manim.mobject.utils.get_point_mobject_class "Link to this definition")

Gets the point cloud mobject class, depending on the currently
active renderer.

Note

This method is intended to be used in the code base of Manim itself
or in plugins where code should work independent of the selected
renderer.

Examples

The function has to be explicitly imported. We test that
the name of the returned class is one of the known mobject
base classes:

```
>>> from manim.mobject.utils import get_point_mobject_class
>>> get_point_mobject_class().__name__ in ['PMobject', 'OpenGLPMobject']
True

```

Copy to clipboard

Return type:

type

get\_vectorized\_mobject\_class() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/utils.html#get_vectorized_mobject_class) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.utils.html#manim.mobject.utils.get_vectorized_mobject_class "Link to this definition")

Gets the vectorized mobject class, depending on the currently
active renderer.

Note

This method is intended to be used in the code base of Manim itself
or in plugins where code should work independent of the selected
renderer.

Examples

The function has to be explicitly imported. We test that
the name of the returned class is one of the known mobject
base classes:

```
>>> from manim.mobject.utils import get_vectorized_mobject_class
>>> get_vectorized_mobject_class().__name__ in ['VMobject', 'OpenGLVMobject']
True

```

Copy to clipboard

Return type:

type