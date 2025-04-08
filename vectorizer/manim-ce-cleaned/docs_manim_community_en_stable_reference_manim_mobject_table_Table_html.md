# Table [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html\#table "Link to this heading")

Qualified name: `manim.mobject.table.Table`

_class_ Table( _table_, _row\_labels=None_, _col\_labels=None_, _top\_left\_entry=None_, _v\_buff=0.8_, _h\_buff=1.3_, _include\_outer\_lines=False_, _add\_background\_rectangles\_to\_entries=False_, _entries\_background\_color=ManimColor('#000000')_, _include\_background\_rectangle=False_, _background\_rectangle\_color=ManimColor('#000000')_, _element\_to\_mobject=<class'manim.mobject.text.text\_mobject.Paragraph'>_, _element\_to\_mobject\_config={}_, _arrange\_in\_grid\_config={}_, _line\_config={}_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "Link to this definition")

Bases: [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

A mobject that displays a table on the screen.

Parameters:

- **table** ( _Iterable_ _\[_ _Iterable_ _\[_ _float_ _\|_ _str_ _\|_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\]_) – A 2D array or list of lists. Content of the table has to be a valid input
for the callable set in `element_to_mobject`.

- **row\_labels** ( _Iterable_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\|_ _None_) – List of [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") representing the labels of each row.

- **col\_labels** ( _Iterable_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\|_ _None_) – List of [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") representing the labels of each column.

- **top\_left\_entry** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ _None_) – The top-left entry of the table, can only be specified if row and
column labels are given.

- **v\_buff** ( _float_) – Vertical buffer passed to [`arrange_in_grid()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange_in_grid "manim.mobject.mobject.Mobject.arrange_in_grid"), by default 0.8.

- **h\_buff** ( _float_) – Horizontal buffer passed to [`arrange_in_grid()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange_in_grid "manim.mobject.mobject.Mobject.arrange_in_grid"), by default 1.3.

- **include\_outer\_lines** ( _bool_) – `True` if the table should include outer lines, by default False.

- **add\_background\_rectangles\_to\_entries** ( _bool_) – `True` if background rectangles should be added to entries, by default `False`.

- **entries\_background\_color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – Background color of entries if `add_background_rectangles_to_entries` is `True`.

- **include\_background\_rectangle** ( _bool_) – `True` if the table should have a background rectangle, by default `False`.

- **background\_rectangle\_color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – Background color of table if `include_background_rectangle` is `True`.

- **element\_to\_mobject** ( _Callable_ _\[_ _\[_ _float_ _\|_ _str_ _\|_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_) – The [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class applied to the table entries. by default [`Paragraph`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph"). For common choices, see [`text_mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.html#module-manim.mobject.text.text_mobject "manim.mobject.text.text_mobject")/ [`tex_mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.html#module-manim.mobject.text.tex_mobject "manim.mobject.text.tex_mobject").

- **element\_to\_mobject\_config** ( _dict_) – Custom configuration passed to `element_to_mobject`, by default {}.

- **arrange\_in\_grid\_config** ( _dict_) – Dict passed to [`arrange_in_grid()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange_in_grid "manim.mobject.mobject.Mobject.arrange_in_grid"), customizes the arrangement of the table.

- **line\_config** ( _dict_) – Dict passed to [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line"), customizes the lines of the table.

- **kwargs** – Additional arguments to be passed to [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup").


Examples

Example: TableExamples [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#tableexamples)

![../_images/TableExamples-2.png](https://docs.manim.community/en/stable/_images/TableExamples-2.png)

```
from manim import *

class TableExamples(Scene):
    def construct(self):
        t0 = Table(
            [["This", "is a"],\
            ["simple", "Table in \\n Manim."]])
        t1 = Table(
            [["This", "is a"],\
            ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        t1.add_highlighted_cell((2,2), color=YELLOW)
        t2 = Table(
            [["This", "is a"],\
            ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": RIGHT})
        t2.add(t2.get_cell((2,2), color=RED))
        t3 = Table(
            [["This", "is a"],\
            ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": YELLOW})
        t3.remove(*t3.get_vertical_lines())
        g = Group(
            t0,t1,t2,t3
        ).scale(0.7).arrange_in_grid(buff=1)
        self.add(g)

```

Copy to clipboard

Make interactive

Example: BackgroundRectanglesExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#backgroundrectanglesexample)

![../_images/BackgroundRectanglesExample-2.png](https://docs.manim.community/en/stable/_images/BackgroundRectanglesExample-2.png)

```
from manim import *

class BackgroundRectanglesExample(Scene):
    def construct(self):
        background = Rectangle(height=6.5, width=13)
        background.set_fill(opacity=.5)
        background.set_color([TEAL, RED, YELLOW])
        self.add(background)
        t0 = Table(
            [["This", "is a"],\
            ["simple", "Table."]],
            add_background_rectangles_to_entries=True)
        t1 = Table(
            [["This", "is a"],\
            ["simple", "Table."]],
            include_background_rectangle=True)
        g = Group(t0, t1).scale(0.7).arrange(buff=0.5)
        self.add(g)

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`add_background_to_entries`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.add_background_to_entries "manim.mobject.table.Table.add_background_to_entries") | Adds a black [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "manim.mobject.geometry.shape_matchers.BackgroundRectangle") to each entry of the table. |
| [`add_highlighted_cell`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.add_highlighted_cell "manim.mobject.table.Table.add_highlighted_cell") | Highlights one cell at a specific position on the table by adding a [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "manim.mobject.geometry.shape_matchers.BackgroundRectangle"). |
| [`create`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.create "manim.mobject.table.Table.create") | Customized create-type function for tables. |
| [`get_cell`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_cell "manim.mobject.table.Table.get_cell") | Returns one specific cell as a rectangular [`Polygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon") without the entry. |
| [`get_col_labels`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_col_labels "manim.mobject.table.Table.get_col_labels") | Return the column labels of the table. |
| [`get_columns`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_columns "manim.mobject.table.Table.get_columns") | Return columns of the table as a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") of [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup"). |
| [`get_entries`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_entries "manim.mobject.table.Table.get_entries") | Return the individual entries of the table (including labels) or one specific entry if the parameter, `pos`, is set. |
| [`get_entries_without_labels`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_entries_without_labels "manim.mobject.table.Table.get_entries_without_labels") | Return the individual entries of the table (without labels) or one specific entry if the parameter, `pos`, is set. |
| [`get_highlighted_cell`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_highlighted_cell "manim.mobject.table.Table.get_highlighted_cell") | Returns a [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "manim.mobject.geometry.shape_matchers.BackgroundRectangle") of the cell at the given position. |
| [`get_horizontal_lines`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_horizontal_lines "manim.mobject.table.Table.get_horizontal_lines") | Return the horizontal lines of the table. |
| [`get_labels`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_labels "manim.mobject.table.Table.get_labels") | Returns the labels of the table. |
| [`get_row_labels`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_row_labels "manim.mobject.table.Table.get_row_labels") | Return the row labels of the table. |
| [`get_rows`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_rows "manim.mobject.table.Table.get_rows") | Return the rows of the table as a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") of [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup"). |
| [`get_vertical_lines`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_vertical_lines "manim.mobject.table.Table.get_vertical_lines") | Return the vertical lines of the table. |
| [`scale`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.scale "manim.mobject.table.Table.scale") | Scale the size by a factor. |
| [`set_column_colors`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.set_column_colors "manim.mobject.table.Table.set_column_colors") | Set individual colors for each column of the table. |
| [`set_row_colors`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.set_row_colors "manim.mobject.table.Table.set_row_colors") | Set individual colors for each row of the table. |

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

\_add\_horizontal\_lines() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table._add_horizontal_lines) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table._add_horizontal_lines "Link to this definition")

Adds the horizontal lines to the table.

Return type:

[_Table_](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

\_add\_labels( _mob\_table_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table._add_labels) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table._add_labels "Link to this definition")

Adds labels to an in a grid arranged [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup").

Parameters:

**mob\_table** ( [_VGroup_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")) – An in a grid organized class:~.VGroup.

Returns:

Returns the `mob_table` with added labels.

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

\_add\_vertical\_lines() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table._add_vertical_lines) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table._add_vertical_lines "Link to this definition")

Adds the vertical lines to the table

Return type:

[_Table_](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

\_organize\_mob\_table( _table_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table._organize_mob_table) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table._organize_mob_table "Link to this definition")

Arranges the [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") of `table` in a grid.

Parameters:

**table** ( _Iterable_ _\[_ _Iterable_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\]_) – A 2D iterable object with [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") entries.

Returns:

The [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") of the `table` in a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") already
arranged in a table-like grid.

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

\_original\_\_init\_\_( _table_, _row\_labels=None_, _col\_labels=None_, _top\_left\_entry=None_, _v\_buff=0.8_, _h\_buff=1.3_, _include\_outer\_lines=False_, _add\_background\_rectangles\_to\_entries=False_, _entries\_background\_color=ManimColor('#000000')_, _include\_background\_rectangle=False_, _background\_rectangle\_color=ManimColor('#000000')_, _element\_to\_mobject=<class'manim.mobject.text.text\_mobject.Paragraph'>_, _element\_to\_mobject\_config={}_, _arrange\_in\_grid\_config={}_, _line\_config={}_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **table** ( _Iterable_ _\[_ _Iterable_ _\[_ _float_ _\|_ _str_ _\|_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\]_)

- **row\_labels** ( _Iterable_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\|_ _None_)

- **col\_labels** ( _Iterable_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\|_ _None_)

- **top\_left\_entry** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ _None_)

- **v\_buff** ( _float_)

- **h\_buff** ( _float_)

- **include\_outer\_lines** ( _bool_)

- **add\_background\_rectangles\_to\_entries** ( _bool_)

- **entries\_background\_color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **include\_background\_rectangle** ( _bool_)

- **background\_rectangle\_color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **element\_to\_mobject** ( _Callable_ _\[_ _\[_ _float_ _\|_ _str_ _\|_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_)

- **element\_to\_mobject\_config** ( _dict_)

- **arrange\_in\_grid\_config** ( _dict_)

- **line\_config** ( _dict_)


\_table\_to\_mob\_table( _table_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table._table_to_mob_table) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table._table_to_mob_table "Link to this definition")

Initilaizes the entries of `table` as [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").

Parameters:

**table** ( _Iterable_ _\[_ _Iterable_ _\[_ _float_ _\|_ _str_ _\|_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\]_) – A 2D array or list of lists. Content of the table has to be a valid input
for the callable set in `element_to_mobject`.

Returns:

List of [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") from the entries of `table`.

Return type:

List

add\_background\_to\_entries( _color=ManimColor('#000000')_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.add_background_to_entries) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.add_background_to_entries "Link to this definition")

Adds a black [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "manim.mobject.geometry.shape_matchers.BackgroundRectangle") to each entry of the table.

Parameters:

**color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

Return type:

[_Table_](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

add\_highlighted\_cell( _pos=(1,1)_, _color=ManimColor('#FFFF00')_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.add_highlighted_cell) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.add_highlighted_cell "Link to this definition")

Highlights one cell at a specific position on the table by adding a [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "manim.mobject.geometry.shape_matchers.BackgroundRectangle").

Parameters:

- **pos** ( _Sequence_ _\[_ _int_ _\]_) – The position of a specific entry on the table. `(1,1)` being the top left entry
of the table.

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color used to highlight the cell.

- **kwargs** – Additional arguments to be passed to [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "manim.mobject.geometry.shape_matchers.BackgroundRectangle").


Return type:

[_Table_](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

Examples

Example: AddHighlightedCellExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#addhighlightedcellexample)

![../_images/AddHighlightedCellExample-1.png](https://docs.manim.community/en/stable/_images/AddHighlightedCellExample-1.png)

```
from manim import *

class AddHighlightedCellExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.add_highlighted_cell((2,2), color=GREEN)
        self.add(table)

```

Copy to clipboard

Make interactive

create( _lag\_ratio=1_, _line\_animation=<class'manim.animation.creation.Create'>_, _label\_animation=<class'manim.animation.creation.Write'>_, _element\_animation=<class'manim.animation.creation.Create'>_, _entry\_animation=<class'manim.animation.fading.FadeIn'>_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.create) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.create "Link to this definition")

Customized create-type function for tables.

Parameters:

- **lag\_ratio** ( _float_) – The lag ratio of the animation.

- **line\_animation** ( _Callable_ _\[_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ [_VGroup_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") _\]_ _,_ [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\]_) – The animation style of the table lines, see [`creation`](https://docs.manim.community/en/stable/reference/manim.animation.creation.html#module-manim.animation.creation "manim.animation.creation") for examples.

- **label\_animation** ( _Callable_ _\[_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ [_VGroup_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") _\]_ _,_ [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\]_) – The animation style of the table labels, see [`creation`](https://docs.manim.community/en/stable/reference/manim.animation.creation.html#module-manim.animation.creation "manim.animation.creation") for examples.

- **element\_animation** ( _Callable_ _\[_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ [_VGroup_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") _\]_ _,_ [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\]_) – The animation style of the table elements, see [`creation`](https://docs.manim.community/en/stable/reference/manim.animation.creation.html#module-manim.animation.creation "manim.animation.creation") for examples.

- **entry\_animation** ( _Callable_ _\[_ _\[_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\|_ [_VGroup_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") _\]_ _,_ [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\]_) – The entry animation of the table background, see [`creation`](https://docs.manim.community/en/stable/reference/manim.animation.creation.html#module-manim.animation.creation "manim.animation.creation") for examples.

- **kwargs** – Further arguments passed to the creation animations.


Returns:

AnimationGroup containing creation of the lines and of the elements.

Return type:

[`AnimationGroup`](https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

Examples

Example: CreateTableExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#createtableexample)

```
from manim import *

class CreateTableExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            include_outer_lines=True)
        self.play(table.create())
        self.wait()

```

Copy to clipboard

Make interactive

get\_cell( _pos=(1,1)_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.get_cell) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_cell "Link to this definition")

Returns one specific cell as a rectangular [`Polygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon") without the entry.

Parameters:

- **pos** ( _Sequence_ _\[_ _int_ _\]_) – The position of a specific entry on the table. `(1,1)` being the top left entry
of the table.

- **kwargs** – Additional arguments to be passed to [`Polygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon").


Returns:

Polygon mimicking one specific cell of the Table.

Return type:

[`Polygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon")

Examples

Example: GetCellExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#getcellexample)

![../_images/GetCellExample-1.png](https://docs.manim.community/en/stable/_images/GetCellExample-1.png)

```
from manim import *

class GetCellExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        cell = table.get_cell((2,2), color=RED)
        self.add(table, cell)

```

Copy to clipboard

Make interactive

get\_col\_labels() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.get_col_labels) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_col_labels "Link to this definition")

Return the column labels of the table.

Returns:

VGroup containing the column labels of the table.

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Examples

Example: GetColLabelsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#getcollabelsexample)

![../_images/GetColLabelsExample-1.png](https://docs.manim.community/en/stable/_images/GetColLabelsExample-1.png)

```
from manim import *

class GetColLabelsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        lab = table.get_col_labels()
        for item in lab:
            item.set_color(random_bright_color())
        self.add(table)

```

Copy to clipboard

Make interactive

get\_columns() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.get_columns) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_columns "Link to this definition")

Return columns of the table as a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") of [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup").

Returns:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") containing each column in a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup").

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Examples

Example: GetColumnsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#getcolumnsexample)

![../_images/GetColumnsExample-2.png](https://docs.manim.community/en/stable/_images/GetColumnsExample-2.png)

```
from manim import *

class GetColumnsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.add(SurroundingRectangle(table.get_columns()[1]))
        self.add(table)

```

Copy to clipboard

Make interactive

get\_entries( _pos=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.get_entries) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_entries "Link to this definition")

Return the individual entries of the table (including labels) or one specific entry
if the parameter, `pos`, is set.

Parameters:

**pos** ( _Sequence_ _\[_ _int_ _\]_ _\|_ _None_) – The position of a specific entry on the table. `(1,1)` being the top left entry
of the table.

Returns:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") containing all entries of the table (including labels)
or the [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") at the given position if `pos` is set.

Return type:

Union\[ [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"), [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")\]

Examples

Example: GetEntriesExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#getentriesexample)

![../_images/GetEntriesExample-2.png](https://docs.manim.community/en/stable/_images/GetEntriesExample-2.png)

```
from manim import *

class GetEntriesExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        ent = table.get_entries()
        for item in ent:
            item.set_color(random_bright_color())
        table.get_entries((2,2)).rotate(PI)
        self.add(table)

```

Copy to clipboard

Make interactive

get\_entries\_without\_labels( _pos=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.get_entries_without_labels) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_entries_without_labels "Link to this definition")

Return the individual entries of the table (without labels) or one specific entry
if the parameter, `pos`, is set.

Parameters:

**pos** ( _Sequence_ _\[_ _int_ _\]_ _\|_ _None_) – The position of a specific entry on the table. `(1,1)` being the top left entry
of the table (without labels).

Returns:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") containing all entries of the table (without labels)
or the [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") at the given position if `pos` is set.

Return type:

Union\[ [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"), [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")\]

Examples

Example: GetEntriesWithoutLabelsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#getentrieswithoutlabelsexample)

![../_images/GetEntriesWithoutLabelsExample-1.png](https://docs.manim.community/en/stable/_images/GetEntriesWithoutLabelsExample-1.png)

```
from manim import *

class GetEntriesWithoutLabelsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        ent = table.get_entries_without_labels()
        colors = [BLUE, GREEN, YELLOW, RED]
        for k in range(len(colors)):
            ent[k].set_color(colors[k])
        table.get_entries_without_labels((2,2)).rotate(PI)
        self.add(table)

```

Copy to clipboard

Make interactive

get\_highlighted\_cell( _pos=(1,1)_, _color=ManimColor('#FFFF00')_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.get_highlighted_cell) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_highlighted_cell "Link to this definition")

Returns a [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "manim.mobject.geometry.shape_matchers.BackgroundRectangle") of the cell at the given position.

Parameters:

- **pos** ( _Sequence_ _\[_ _int_ _\]_) – The position of a specific entry on the table. `(1,1)` being the top left entry
of the table.

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color used to highlight the cell.

- **kwargs** – Additional arguments to be passed to [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "manim.mobject.geometry.shape_matchers.BackgroundRectangle").


Return type:

[_BackgroundRectangle_](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "manim.mobject.geometry.shape_matchers.BackgroundRectangle")

Examples

Example: GetHighlightedCellExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#gethighlightedcellexample)

![../_images/GetHighlightedCellExample-1.png](https://docs.manim.community/en/stable/_images/GetHighlightedCellExample-1.png)

```
from manim import *

class GetHighlightedCellExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        highlight = table.get_highlighted_cell((2,2), color=GREEN)
        table.add_to_back(highlight)
        self.add(table)

```

Copy to clipboard

Make interactive

get\_horizontal\_lines() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.get_horizontal_lines) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_horizontal_lines "Link to this definition")

Return the horizontal lines of the table.

Returns:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") containing all the horizontal lines of the table.

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Examples

Example: GetHorizontalLinesExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#gethorizontallinesexample)

![../_images/GetHorizontalLinesExample-1.png](https://docs.manim.community/en/stable/_images/GetHorizontalLinesExample-1.png)

```
from manim import *

class GetHorizontalLinesExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.get_horizontal_lines().set_color(RED)
        self.add(table)

```

Copy to clipboard

Make interactive

get\_labels() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.get_labels) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_labels "Link to this definition")

Returns the labels of the table.

Returns:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") containing all the labels of the table.

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Examples

Example: GetLabelsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#getlabelsexample)

![../_images/GetLabelsExample-1.png](https://docs.manim.community/en/stable/_images/GetLabelsExample-1.png)

```
from manim import *

class GetLabelsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        lab = table.get_labels()
        colors = [BLUE, GREEN, YELLOW, RED]
        for k in range(len(colors)):
            lab[k].set_color(colors[k])
        self.add(table)

```

Copy to clipboard

Make interactive

get\_row\_labels() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.get_row_labels) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_row_labels "Link to this definition")

Return the row labels of the table.

Returns:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") containing the row labels of the table.

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Examples

Example: GetRowLabelsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#getrowlabelsexample)

![../_images/GetRowLabelsExample-1.png](https://docs.manim.community/en/stable/_images/GetRowLabelsExample-1.png)

```
from manim import *

class GetRowLabelsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        lab = table.get_row_labels()
        for item in lab:
            item.set_color(random_bright_color())
        self.add(table)

```

Copy to clipboard

Make interactive

get\_rows() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.get_rows) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_rows "Link to this definition")

Return the rows of the table as a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") of [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup").

Returns:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") containing each row in a [`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup").

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Examples

Example: GetRowsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#getrowsexample)

![../_images/GetRowsExample-2.png](https://docs.manim.community/en/stable/_images/GetRowsExample-2.png)

```
from manim import *

class GetRowsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.add(SurroundingRectangle(table.get_rows()[1]))
        self.add(table)

```

Copy to clipboard

Make interactive

get\_vertical\_lines() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.get_vertical_lines) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.get_vertical_lines "Link to this definition")

Return the vertical lines of the table.

Returns:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") containing all the vertical lines of the table.

Return type:

[`VGroup`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

Examples

Example: GetVerticalLinesExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#getverticallinesexample)

![../_images/GetVerticalLinesExample-1.png](https://docs.manim.community/en/stable/_images/GetVerticalLinesExample-1.png)

```
from manim import *

class GetVerticalLinesExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.get_vertical_lines()[0].set_color(RED)
        self.add(table)

```

Copy to clipboard

Make interactive

scale( _scale\_factor_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.scale) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.scale "Link to this definition")

Scale the size by a factor.

Default behavior is to scale about the center of the vmobject.

Parameters:

- **scale\_factor** ( _float_) – The scaling factor α. If 0<\|α\|<1, the mobject
will shrink, and for \|α\|>1 it will grow. Furthermore,
if α<0, the mobject is also flipped.

- **scale\_stroke** – Boolean determining if the object’s outline is scaled when the object is scaled.
If enabled, and object with 2px outline is scaled by a factor of .5, it will have an outline of 1px.

- **kwargs** – Additional keyword arguments passed to
[`scale()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale "manim.mobject.mobject.Mobject.scale").


Returns:

`self`

Return type:

`VMobject`

Examples

Example: MobjectScaleExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#mobjectscaleexample)

![../_images/MobjectScaleExample-2.png](https://docs.manim.community/en/stable/_images/MobjectScaleExample-2.png)

```
from manim import *

class MobjectScaleExample(Scene):
    def construct(self):
        c1 = Circle(1, RED).set_x(-1)
        c2 = Circle(1, GREEN).set_x(1)

        vg = VGroup(c1, c2)
        vg.set_stroke(width=50)
        self.add(vg)

        self.play(
            c1.animate.scale(.25),
            c2.animate.scale(.25,
                scale_stroke=True)
        )

```

Copy to clipboard

Make interactive

See also

`move_to()`

set\_column\_colors( _\*colors_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.set_column_colors) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.set_column_colors "Link to this definition")

Set individual colors for each column of the table.

Parameters:

**colors** ( _Iterable_ _\[_ [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\]_) – An iterable of colors; each color corresponds to a column.

Return type:

[_Table_](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

Examples

Example: SetColumnColorsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#setcolumncolorsexample)

![../_images/SetColumnColorsExample-2.png](https://docs.manim.community/en/stable/_images/SetColumnColorsExample-2.png)

```
from manim import *

class SetColumnColorsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")]
        ).set_column_colors([RED,BLUE], GREEN)
        self.add(table)

```

Copy to clipboard

Make interactive

set\_row\_colors( _\*colors_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/table.html#Table.set_row_colors) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table.set_row_colors "Link to this definition")

Set individual colors for each row of the table.

Parameters:

**colors** ( _Iterable_ _\[_ [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\]_) – An iterable of colors; each color corresponds to a row.

Return type:

[_Table_](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

Examples

Example: SetRowColorsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#setrowcolorsexample)

![../_images/SetRowColorsExample-2.png](https://docs.manim.community/en/stable/_images/SetRowColorsExample-2.png)

```
from manim import *

class SetRowColorsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")]
        ).set_row_colors([RED,BLUE], GREEN)
        self.add(table)

```

Copy to clipboard

Make interactive