# Matrix [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html\#matrix "Link to this heading")

Qualified name: `manim.mobject.matrix.Matrix`

_class_ Matrix( _matrix_, _v\_buff=0.8_, _h\_buff=1.3_, _bracket\_h\_buff=0.25_, _bracket\_v\_buff=0.25_, _add\_background\_rectangles\_to\_entries=False_, _include\_background\_rectangle=False_, _element\_to\_mobject=<class'manim.mobject.text.tex\_mobject.MathTex'>_, _element\_to\_mobject\_config={}_, _element\_alignment\_corner=array(\[1._, _-1._, _0.\])_, _left\_bracket='\['_, _right\_bracket='\]'_, _stretch\_brackets=True_, _bracket\_config={}_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#Matrix) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

A mobject that displays a matrix on the screen.

Parameters:

- **matrix** ( _Iterable_) – A numpy 2d array or list of lists.

- **v\_buff** ( _float_) – Vertical distance between elements, by default 0.8.

- **h\_buff** ( _float_) – Horizontal distance between elements, by default 1.3.

- **bracket\_h\_buff** ( _float_) – Distance of the brackets from the matrix, by default `MED_SMALL_BUFF`.

- **bracket\_v\_buff** ( _float_) – Height of the brackets, by default `MED_SMALL_BUFF`.

- **add\_background\_rectangles\_to\_entries** ( _bool_) – `True` if should add backgraound rectangles to entries, by default `False`.

- **include\_background\_rectangle** ( _bool_) – `True` if should include background rectangle, by default `False`.

- **element\_to\_mobject** ( _type_ _\[_ [_MathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") _\]_) – The mobject class used to construct the elements, by default [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").

- **element\_to\_mobject\_config** ( _dict_) – Additional arguments to be passed to the constructor in `element_to_mobject`,
by default `{}`.

- **element\_alignment\_corner** ( _Sequence_ _\[_ _float_ _\]_) – The corner to which elements are aligned, by default `DR`.

- **left\_bracket** ( _str_) – The left bracket type, by default `"["`.\
\
- **right\_bracket** ( _str_) – The right bracket type, by default `"]"`.

- **stretch\_brackets** ( _bool_) – `True` if should stretch the brackets to fit the height of matrix contents, by default `True`.

- **bracket\_config** ( _dict_) – Additional arguments to be passed to [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") when constructing
the brackets.


Examples

The first example shows a variety of uses of this module while the second example
exlpains the use of the options add\_background\_rectangles\_to\_entries and
include\_background\_rectangle.

Example: MatrixExamples [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#matrixexamples)

![../_images/MatrixExamples-2.png](https://docs.manim.community/en/stable/_images/MatrixExamples-2.png)

```
from manim import *

class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([[2, r"\pi"], [-1, 1]])
        m1 = Matrix([[2, 0, 4], [-1, 1, 5]],
            v_buff=1.3,
            h_buff=0.8,
            bracket_h_buff=SMALL_BUFF,
            bracket_v_buff=SMALL_BUFF,
            left_bracket=r"\{",
            right_bracket=r"\}")
        m1.add(SurroundingRectangle(m1.get_columns()[1]))
        m2 = Matrix([[2, 1], [-1, 3]],
            element_alignment_corner=UL,
            left_bracket="(",
            right_bracket=")")
        m3 = Matrix([[2, 1], [-1, 3]],
            left_bracket=r"\langle",
            right_bracket=r"\rangle")
        m4 = Matrix([[2, 1], [-1, 3]],
        ).set_column_colors(RED, GREEN)
        m5 = Matrix([[2, 1], [-1, 3]],
        ).set_row_colors(RED, GREEN)
        g = Group(
            m0,m1,m2,m3,m4,m5
        ).arrange_in_grid(buff=2)
        self.add(g)

```

Copy to clipboard

Make interactive

Example: BackgroundRectanglesExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#backgroundrectanglesexample)

![../_images/BackgroundRectanglesExample-1.png](https://docs.manim.community/en/stable/_images/BackgroundRectanglesExample-1.png)

```
from manim import *

class BackgroundRectanglesExample(Scene):
    def construct(self):
        background= Rectangle().scale(3.2)
        background.set_fill(opacity=.5)
        background.set_color([TEAL, RED, YELLOW])
        self.add(background)
        m0 = Matrix([[12, -30], [-1, 15]],
            add_background_rectangles_to_entries=True)
        m1 = Matrix([[2, 0], [-1, 1]],
            include_background_rectangle=True)
        m2 = Matrix([[12, -30], [-1, 15]])
        g = Group(m0, m1, m2).arrange(buff=2)
        self.add(g)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`add_background_to_entries`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.add_background_to_entries "manim.mobject.matrix.Matrix.add_background_to_entries") | Add a black background rectangle to the matrix, see above for an example. |
| [`get_brackets`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.get_brackets "manim.mobject.matrix.Matrix.get_brackets") | Return the bracket mobjects. |
| [`get_columns`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.get_columns "manim.mobject.matrix.Matrix.get_columns") | Return columns of the matrix as VGroups. |
| [`get_entries`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.get_entries "manim.mobject.matrix.Matrix.get_entries") | Return the individual entries of the matrix. |
| [`get_mob_matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.get_mob_matrix "manim.mobject.matrix.Matrix.get_mob_matrix") | Return the underlying mob matrix mobjects. |
| [`get_rows`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.get_rows "manim.mobject.matrix.Matrix.get_rows") | Return rows of the matrix as VGroups. |
| [`set_column_colors`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.set_column_colors "manim.mobject.matrix.Matrix.set_column_colors") | Set individual colors for each columns of the matrix. |
| [`set_row_colors`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.set_row_colors "manim.mobject.matrix.Matrix.set_row_colors") | Set individual colors for each row of the matrix. |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

\_add\_brackets( _left='\['_, _right='\]'_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#Matrix._add_brackets) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix._add_brackets "Link to this definition")

Adds the brackets to the Matrix mobject.

See Latex document for various bracket types.

Parameters:

- **left** ( _str_) – the left bracket, by default “\[”\
\
- **right** ( _str_) – the right bracket, by default “\]”


Returns:

The current matrix object (self).

Return type:

[`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

\_original\_\_init\_\_( _matrix_, _v\_buff=0.8_, _h\_buff=1.3_, _bracket\_h\_buff=0.25_, _bracket\_v\_buff=0.25_, _add\_background\_rectangles\_to\_entries=False_, _include\_background\_rectangle=False_, _element\_to\_mobject=<class'manim.mobject.text.tex\_mobject.MathTex'>_, _element\_to\_mobject\_config={}_, _element\_alignment\_corner=array(\[1._, _-1._, _0.\])_, _left\_bracket='\['_, _right\_bracket='\]'_, _stretch\_brackets=True_, _bracket\_config={}_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **matrix** ( _Iterable_)

- **v\_buff** ( _float_)

- **h\_buff** ( _float_)

- **bracket\_h\_buff** ( _float_)

- **bracket\_v\_buff** ( _float_)

- **add\_background\_rectangles\_to\_entries** ( _bool_)

- **include\_background\_rectangle** ( _bool_)

- **element\_to\_mobject** ( _type_ _\[_ [_MathTex_](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") _\]_)

- **element\_to\_mobject\_config** ( _dict_)

- **element\_alignment\_corner** ( _Sequence_ _\[_ _float_ _\]_)

- **left\_bracket** ( _str_)

- **right\_bracket** ( _str_)

- **stretch\_brackets** ( _bool_)

- **bracket\_config** ( _dict_)


add\_background\_to\_entries() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#Matrix.add_background_to_entries) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.add_background_to_entries "Link to this definition")

Add a black background rectangle to the matrix,
see above for an example.

Returns:

The current matrix object (self).

Return type:

[`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

get\_brackets() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#Matrix.get_brackets) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.get_brackets "Link to this definition")

Return the bracket mobjects.

Returns:

Each VGroup contains a bracket

Return type:

List\[ [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")\]

Examples

Example: GetBracketsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#getbracketsexample)

![../_images/GetBracketsExample-1.png](https://docs.manim.community/en/stable/_images/GetBracketsExample-1.png)

```
from manim import *

class GetBracketsExample(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 3], [1, 5]])
        bra = m0.get_brackets()
        colors = [BLUE, GREEN]
        for k in range(len(colors)):
            bra[k].set_color(colors[k])
        self.add(m0)

```

Copy to clipboard

Make interactive

get\_columns() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#Matrix.get_columns) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.get_columns "Link to this definition")

Return columns of the matrix as VGroups.

Returns:

Each VGroup contains a column of the matrix.

Return type:

List\[ [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")\]

Examples

Example: GetColumnsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#getcolumnsexample)

![../_images/GetColumnsExample-1.png](https://docs.manim.community/en/stable/_images/GetColumnsExample-1.png)

```
from manim import *

class GetColumnsExample(Scene):
    def construct(self):
        m0 = Matrix([[r"\pi", 3], [1, 5]])
        m0.add(SurroundingRectangle(m0.get_columns()[1]))
        self.add(m0)

```

Copy to clipboard

Make interactive

get\_entries() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#Matrix.get_entries) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.get_entries "Link to this definition")

Return the individual entries of the matrix.

Returns:

VGroup containing entries of the matrix.

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Examples

Example: GetEntriesExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#getentriesexample)

![../_images/GetEntriesExample-1.png](https://docs.manim.community/en/stable/_images/GetEntriesExample-1.png)

```
from manim import *

class GetEntriesExample(Scene):
    def construct(self):
        m0 = Matrix([[2, 3], [1, 5]])
        ent = m0.get_entries()
        colors = [BLUE, GREEN, YELLOW, RED]
        for k in range(len(colors)):
            ent[k].set_color(colors[k])
        self.add(m0)

```

Copy to clipboard

Make interactive

get\_mob\_matrix() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#Matrix.get_mob_matrix) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.get_mob_matrix "Link to this definition")

Return the underlying mob matrix mobjects.

Returns:

Each VGroup contains a row of the matrix.

Return type:

List\[ [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")\]

get\_rows() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#Matrix.get_rows) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.get_rows "Link to this definition")

Return rows of the matrix as VGroups.

Returns:

Each VGroup contains a row of the matrix.

Return type:

List\[ [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")\]

Examples

Example: GetRowsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#getrowsexample)

![../_images/GetRowsExample-1.png](https://docs.manim.community/en/stable/_images/GetRowsExample-1.png)

```
from manim import *

class GetRowsExample(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 3], [1, 5]])
        m0.add(SurroundingRectangle(m0.get_rows()[1]))
        self.add(m0)

```

Copy to clipboard

Make interactive

set\_column\_colors( _\*colors_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#Matrix.set_column_colors) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.set_column_colors "Link to this definition")

Set individual colors for each columns of the matrix.

Parameters:

**colors** ( _str_) – The list of colors; each color specified corresponds to a column.

Returns:

The current matrix object (self).

Return type:

[`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

Examples

Example: SetColumnColorsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#setcolumncolorsexample)

![../_images/SetColumnColorsExample-1.png](https://docs.manim.community/en/stable/_images/SetColumnColorsExample-1.png)

```
from manim import *

class SetColumnColorsExample(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 1], [-1, 3]],
        ).set_column_colors([RED,BLUE], GREEN)
        self.add(m0)

```

Copy to clipboard

Make interactive

set\_row\_colors( _\*colors_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/matrix.html#Matrix.set_row_colors) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix.set_row_colors "Link to this definition")

Set individual colors for each row of the matrix.

Parameters:

**colors** ( _str_) – The list of colors; each color specified corresponds to a row.

Returns:

The current matrix object (self).

Return type:

[`Matrix`](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

Examples

Example: SetRowColorsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.matrix.Matrix.html#setrowcolorsexample)

![../_images/SetRowColorsExample-1.png](https://docs.manim.community/en/stable/_images/SetRowColorsExample-1.png)

```
from manim import *

class SetRowColorsExample(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 1], [-1, 3]],
        ).set_row_colors([RED,BLUE], GREEN)
        self.add(m0)

```

Copy to clipboard

Make interactive

[Develop and launch modern apps with MongoDB Atlas, a resilient data platform.](https://server.ethicalads.io/proxy/click/8269/019600f1-1948-7731-b693-0d66bf592bd4/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/frontend-web/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8269/019600f1-1948-7731-b693-0d66bf592bd4/)