# LinearTransformationScene [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html\#lineartransformationscene "Link to this heading")

Qualified name: `manim.scene.vector\_space\_scene.LinearTransformationScene`

_class_ LinearTransformationScene( _include\_background\_plane=True_, _include\_foreground\_plane=True_, _background\_plane\_kwargs=None_, _foreground\_plane\_kwargs=None_, _show\_coordinates=False_, _show\_basis\_vectors=True_, _basis\_vector\_stroke\_width=6_, _i\_hat\_color=ManimColor('#83C167')_, _j\_hat\_color=ManimColor('#FC6255')_, _leave\_ghost\_vectors=False_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene "Link to this definition")

Bases: [`VectorScene`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.VectorScene.html#manim.scene.vector_space_scene.VectorScene "manim.scene.vector_space_scene.VectorScene")

This scene contains special methods that make it
especially suitable for showing linear transformations.

Parameters:

- **include\_background\_plane** ( _bool_) – Whether or not to include the background plane in the scene.

- **include\_foreground\_plane** ( _bool_) – Whether or not to include the foreground plane in the scene.

- **background\_plane\_kwargs** ( _dict_ _\|_ _None_) – Parameters to be passed to `NumberPlane` to adjust the background plane.

- **foreground\_plane\_kwargs** ( _dict_ _\|_ _None_) – Parameters to be passed to `NumberPlane` to adjust the foreground plane.

- **show\_coordinates** ( _bool_) – Whether or not to include the coordinates for the background plane.

- **show\_basis\_vectors** ( _bool_) – Whether to show the basis x\_axis -> `i_hat` and y\_axis -> `j_hat` vectors.

- **basis\_vector\_stroke\_width** ( _float_) – The `stroke_width` of the basis vectors.

- **i\_hat\_color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the `i_hat` vector.

- **j\_hat\_color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the `j_hat` vector.

- **leave\_ghost\_vectors** ( _bool_) – Indicates the previous position of the basis vectors following a transformation.


Examples

Example: LinearTransformationSceneExample [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#lineartransformationsceneexample)

```
from manim import *

class LinearTransformationSceneExample(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def construct(self):
        matrix = [[1, 1], [0, 1]]
        self.apply_matrix(matrix)
        self.wait()

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`add_background_mobject`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_background_mobject "manim.scene.vector_space_scene.LinearTransformationScene.add_background_mobject") | Adds the mobjects to the special list self.background\_mobjects. |
| [`add_foreground_mobject`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_foreground_mobject "manim.scene.vector_space_scene.LinearTransformationScene.add_foreground_mobject") | Adds the mobjects to the special list self.foreground\_mobjects. |
| [`add_moving_mobject`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_moving_mobject "manim.scene.vector_space_scene.LinearTransformationScene.add_moving_mobject") | Adds the mobject to the special list self.moving\_mobject, and adds a property to the mobject called mobject.target, which keeps track of what the mobject will move to or become etc. |
| [`add_special_mobjects`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_special_mobjects "manim.scene.vector_space_scene.LinearTransformationScene.add_special_mobjects") | Adds mobjects to a separate list that can be tracked, if these mobjects have some extra importance. |
| [`add_title`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_title "manim.scene.vector_space_scene.LinearTransformationScene.add_title") | Adds a title, after scaling it, adding a background rectangle, moving it to the top and adding it to foreground\_mobjects adding it as a local variable of self. |
| [`add_transformable_label`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_label "manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_label") | Method for creating, and animating the addition of a transformable label for the vector. |
| [`add_transformable_mobject`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_mobject "manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_mobject") | Adds the mobjects to the special list self.transformable\_mobjects. |
| [`add_unit_square`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_unit_square "manim.scene.vector_space_scene.LinearTransformationScene.add_unit_square") | Adds a unit square to the scene via self.get\_unit\_square. |
| [`add_vector`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_vector "manim.scene.vector_space_scene.LinearTransformationScene.add_vector") | Adds a vector to the scene, and puts it in the special list self.moving\_vectors. |
| [`apply_function`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.apply_function "manim.scene.vector_space_scene.LinearTransformationScene.apply_function") | Applies the given function to each of the mobjects in self.transformable\_mobjects, and plays the animation showing this. |
| [`apply_inverse`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse "manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse") | This method applies the linear transformation represented by the inverse of the passed matrix to the number plane, and each vector/similar mobject on it. |
| [`apply_inverse_transpose`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse_transpose "manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse_transpose") | Applies the inverse of the transformation represented by the given transposed matrix to the number plane and each vector/similar mobject on it. |
| [`apply_matrix`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.apply_matrix "manim.scene.vector_space_scene.LinearTransformationScene.apply_matrix") | Applies the transformation represented by the given matrix to the number plane, and each vector/similar mobject on it. |
| [`apply_nonlinear_transformation`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.apply_nonlinear_transformation "manim.scene.vector_space_scene.LinearTransformationScene.apply_nonlinear_transformation") | Applies the non-linear transformation represented by the given function to the number plane and each vector/similar mobject on it. |
| [`apply_transposed_matrix`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.apply_transposed_matrix "manim.scene.vector_space_scene.LinearTransformationScene.apply_transposed_matrix") | Applies the transformation represented by the given transposed matrix to the number plane, and each vector/similar mobject on it. |
| [`get_ghost_vectors`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_ghost_vectors "manim.scene.vector_space_scene.LinearTransformationScene.get_ghost_vectors") | Returns all ghost vectors ever added to `self`. |
| [`get_matrix_transformation`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_matrix_transformation "manim.scene.vector_space_scene.LinearTransformationScene.get_matrix_transformation") | Returns a function corresponding to the linear transformation represented by the matrix passed. |
| [`get_moving_mobject_movement`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_moving_mobject_movement "manim.scene.vector_space_scene.LinearTransformationScene.get_moving_mobject_movement") | This method returns an animation that moves a mobject in "self.moving\_mobjects" to its corresponding .target value. |
| [`get_piece_movement`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_piece_movement "manim.scene.vector_space_scene.LinearTransformationScene.get_piece_movement") | This method returns an animation that moves an arbitrary mobject in "pieces" to its corresponding .target value. |
| [`get_transformable_label_movement`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_transformable_label_movement "manim.scene.vector_space_scene.LinearTransformationScene.get_transformable_label_movement") | This method returns an animation that moves all labels in "self.transformable\_labels" to its corresponding .target . |
| [`get_transposed_matrix_transformation`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_transposed_matrix_transformation "manim.scene.vector_space_scene.LinearTransformationScene.get_transposed_matrix_transformation") | Returns a function corresponding to the linear transformation represented by the transposed matrix passed. |
| [`get_unit_square`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_unit_square "manim.scene.vector_space_scene.LinearTransformationScene.get_unit_square") | Returns a unit square for the current NumberPlane. |
| [`get_vector_movement`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_vector_movement "manim.scene.vector_space_scene.LinearTransformationScene.get_vector_movement") | This method returns an animation that moves a mobject in "self.moving\_vectors" to its corresponding .target value. |
| [`setup`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.setup "manim.scene.vector_space_scene.LinearTransformationScene.setup") | This is meant to be implemented by any scenes which are commonly subclassed, and have some common setup involved before the construct method is called. |
| `update_default_configs` |  |
| [`write_vector_coordinates`](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.write_vector_coordinates "manim.scene.vector_space_scene.LinearTransformationScene.write_vector_coordinates") | Returns a column matrix indicating the vector coordinates, after writing them to the screen, and adding them to the special list self.foreground\_mobjects |

Attributes

|     |     |
| --- | --- |
| `camera` |  |
| `time` | The time since the start of the scene. |

add\_background\_mobject( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_background_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_background_mobject "Link to this definition")

Adds the mobjects to the special list
self.background\_mobjects.

Parameters:

**\*mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add to the list.

add\_foreground\_mobject( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_foreground_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_foreground_mobject "Link to this definition")

Adds the mobjects to the special list
self.foreground\_mobjects.

Parameters:

**\*mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add to the list

add\_moving\_mobject( _mobject_, _target\_mobject=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_moving_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_moving_mobject "Link to this definition")

Adds the mobject to the special list
self.moving\_mobject, and adds a property
to the mobject called mobject.target, which
keeps track of what the mobject will move to
or become etc.

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add to the list

- **target\_mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\|_ _None_) – What the moving\_mobject goes to, etc.


add\_special\_mobjects( _mob\_list_, _\*mobs\_to\_add_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_special_mobjects) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_special_mobjects "Link to this definition")

Adds mobjects to a separate list that can be tracked,
if these mobjects have some extra importance.

Parameters:

- **mob\_list** ( _list_) – The special list to which you want to add
these mobjects.

- **\*mobs\_to\_add** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add.


add\_title( _title_, _scale\_factor=1.5_, _animate=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_title) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_title "Link to this definition")

Adds a title, after scaling it, adding a background rectangle,
moving it to the top and adding it to foreground\_mobjects adding
it as a local variable of self. Returns the Scene.

Parameters:

- **title** ( _str_ _\|_ [_MathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") _\|_ [_Tex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")) – What the title should be.

- **scale\_factor** ( _float_) – How much the title should be scaled by.

- **animate** ( _bool_) – Whether or not to animate the addition.


Returns:

The scene with the title added to it.

Return type:

[LinearTransformationScene](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene "manim.scene.vector_space_scene.LinearTransformationScene")

add\_transformable\_label( _vector_, _label_, _transformation\_name='L'_, _new\_label=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_transformable_label) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_label "Link to this definition")

Method for creating, and animating the addition of
a transformable label for the vector.

Parameters:

- **vector** ( [_Vector_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector")) – The vector for which the label must be added.

- **label** ( [_MathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") _\|_ _str_) – The MathTex/string of the label.

- **transformation\_name** ( _str_ _\|_ [_MathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")) – The name to give the transformation as a label.

- **new\_label** ( _str_ _\|_ [_MathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") _\|_ _None_) – What the label should display after a Linear Transformation

- **\*\*kwargs** – Any valid keyword argument of get\_vector\_label


Returns:

The MathTex of the label.

Return type:

[`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")

add\_transformable\_mobject( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_transformable_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_transformable_mobject "Link to this definition")

Adds the mobjects to the special list
self.transformable\_mobjects.

Parameters:

**\*mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add to the list.

add\_unit\_square( _animate=False_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_unit_square) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_unit_square "Link to this definition")

Adds a unit square to the scene via
self.get\_unit\_square.

Parameters:

- **animate** ( _bool_) – Whether or not to animate the addition
with DrawBorderThenFill.

- **\*\*kwargs** – Any valid keyword arguments of
self.get\_unit\_square()


Returns:

The unit square.

Return type:

[Square](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html#manim.mobject.geometry.polygram.Square "manim.mobject.geometry.polygram.Square")

add\_vector( _vector_, _color=ManimColor('#FFFF00')_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.add_vector) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.add_vector "Link to this definition")

Adds a vector to the scene, and puts it in the special
list self.moving\_vectors.

Parameters:

- **vector** ( [_Arrow_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow") _\|_ _list_ _\|_ _tuple_ _\|_ _ndarray_) – It can be a pre-made graphical vector, or the
coordinates of one.

- **color** ( _str_) – The string of the hex color of the vector.
This is only taken into consideration if
‘vector’ is not an Arrow. Defaults to YELLOW.

- **\*\*kwargs** – Any valid keyword argument of VectorScene.add\_vector.


Returns:

The arrow representing the vector.

Return type:

[Arrow](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")

apply\_function( _function_, _added\_anims=\[\]_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.apply_function) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.apply_function "Link to this definition")

Applies the given function to each of the mobjects in
self.transformable\_mobjects, and plays the animation showing
this.

Parameters:

- **function** ( _Callable_ _\[_ _\[_ _ndarray_ _\]_ _,_ _ndarray_ _\]_) – The function that affects each point
of each mobject in self.transformable\_mobjects.

- **added\_anims** ( _list_) – Any other animations that need to be played
simultaneously with this.

- **\*\*kwargs** – Any valid keyword argument of a self.play() call.


apply\_inverse( _matrix_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.apply_inverse) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse "Link to this definition")

This method applies the linear transformation
represented by the inverse of the passed matrix
to the number plane, and each vector/similar mobject on it.

Parameters:

- **matrix** ( _ndarray_ _\|_ _list_ _\|_ _tuple_) – The matrix whose inverse is to be applied.

- **\*\*kwargs** – Any valid keyword argument of self.apply\_matrix()


apply\_inverse\_transpose( _t\_matrix_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.apply_inverse_transpose) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.apply_inverse_transpose "Link to this definition")

Applies the inverse of the transformation represented
by the given transposed matrix to the number plane and each
vector/similar mobject on it.

Parameters:

- **t\_matrix** ( _ndarray_ _\|_ _list_ _\|_ _tuple_) – The matrix.

- **\*\*kwargs** – Any valid keyword argument of self.apply\_transposed\_matrix()


apply\_matrix( _matrix_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.apply_matrix) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.apply_matrix "Link to this definition")

Applies the transformation represented by the
given matrix to the number plane, and each vector/similar
mobject on it.

Parameters:

- **matrix** ( _ndarray_ _\|_ _list_ _\|_ _tuple_) – The matrix.

- **\*\*kwargs** – Any valid keyword argument of self.apply\_transposed\_matrix()


apply\_nonlinear\_transformation( _function_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.apply_nonlinear_transformation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.apply_nonlinear_transformation "Link to this definition")

Applies the non-linear transformation represented
by the given function to the number plane and each
vector/similar mobject on it.

Parameters:

- **function** ( _Callable_ _\[_ _\[_ _ndarray_ _\]_ _,_ _ndarray_ _\]_) – The function.

- **\*\*kwargs** – Any valid keyword argument of self.apply\_function()


apply\_transposed\_matrix( _transposed\_matrix_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.apply_transposed_matrix) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.apply_transposed_matrix "Link to this definition")

Applies the transformation represented by the
given transposed matrix to the number plane,
and each vector/similar mobject on it.

Parameters:

- **transposed\_matrix** ( _ndarray_ _\|_ _list_ _\|_ _tuple_) – The matrix.

- **\*\*kwargs** – Any valid keyword argument of self.apply\_function()


get\_ghost\_vectors() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_ghost_vectors) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_ghost_vectors "Link to this definition")

Returns all ghost vectors ever added to `self`. Each element is a `VGroup` of
two ghost vectors.

Return type:

[_VGroup_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

get\_matrix\_transformation( _matrix_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_matrix_transformation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_matrix_transformation "Link to this definition")

Returns a function corresponding to the linear
transformation represented by the matrix passed.

Parameters:

**matrix** ( _ndarray_ _\|_ _list_ _\|_ _tuple_) – The matrix.

get\_moving\_mobject\_movement( _func_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_moving_mobject_movement) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_moving_mobject_movement "Link to this definition")

This method returns an animation that moves a mobject
in “self.moving\_mobjects” to its corresponding .target value.
func is a function that determines where the .target goes.

Parameters:

**func** ( _Callable_ _\[_ _\[_ _ndarray_ _\]_ _,_ _ndarray_ _\]_) – The function that determines where the .target of
the moving mobject goes.

Returns:

The animation of the movement.

Return type:

[Animation](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

get\_piece\_movement( _pieces_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_piece_movement) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_piece_movement "Link to this definition")

This method returns an animation that moves an arbitrary
mobject in “pieces” to its corresponding .target value.
If self.leave\_ghost\_vectors is True, ghosts of the original
positions/mobjects are left on screen

Parameters:

**pieces** ( _list_ _\|_ _tuple_ _\|_ _ndarray_) – The pieces for which the movement must be shown.

Returns:

The animation of the movement.

Return type:

[Animation](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

get\_transformable\_label\_movement() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_transformable_label_movement) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_transformable_label_movement "Link to this definition")

This method returns an animation that moves all labels
in “self.transformable\_labels” to its corresponding .target .

Returns:

The animation of the movement.

Return type:

[Animation](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

get\_transposed\_matrix\_transformation( _transposed\_matrix_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_transposed_matrix_transformation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_transposed_matrix_transformation "Link to this definition")

Returns a function corresponding to the linear
transformation represented by the transposed
matrix passed.

Parameters:

**transposed\_matrix** ( _ndarray_ _\|_ _list_ _\|_ _tuple_) – The matrix.

get\_unit\_square( _color=ManimColor('#FFFF00')_, _opacity=0.3_, _stroke\_width=3_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_unit_square) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_unit_square "Link to this definition")

Returns a unit square for the current NumberPlane.

Parameters:

- **color** ( _str_) – The string of the hex color code of the color wanted.

- **opacity** ( _float_) – The opacity of the square

- **stroke\_width** ( _float_) – The stroke\_width in pixels of the border of the square


Return type:

[Square](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html#manim.mobject.geometry.polygram.Square "manim.mobject.geometry.polygram.Square")

get\_vector\_movement( _func_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.get_vector_movement) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.get_vector_movement "Link to this definition")

This method returns an animation that moves a mobject
in “self.moving\_vectors” to its corresponding .target value.
func is a function that determines where the .target goes.

Parameters:

**func** ( _Callable_ _\[_ _\[_ _ndarray_ _\]_ _,_ _ndarray_ _\]_) – The function that determines where the .target of
the moving mobject goes.

Returns:

The animation of the movement.

Return type:

[Animation](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

setup() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.setup) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.setup "Link to this definition")

This is meant to be implemented by any scenes which
are commonly subclassed, and have some common setup
involved before the construct method is called.

write\_vector\_coordinates( _vector_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/vector_space_scene.html#LinearTransformationScene.write_vector_coordinates) [¶](https://docs.manim.community/en/stable/reference/manim.scene.vector_space_scene.LinearTransformationScene.html#manim.scene.vector_space_scene.LinearTransformationScene.write_vector_coordinates "Link to this definition")

Returns a column matrix indicating the vector coordinates,
after writing them to the screen, and adding them to the
special list self.foreground\_mobjects

Parameters:

- **vector** ( [_Arrow_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")) – The arrow representing the vector.

- **\*\*kwargs** – Any valid keyword arguments of VectorScene.write\_vector\_coordinates


Returns:

The column matrix representing the vector.

Return type:

[Matrix](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")