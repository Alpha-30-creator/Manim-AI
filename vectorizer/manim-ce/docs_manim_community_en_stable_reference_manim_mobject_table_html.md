ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.table.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.table.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# table [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.html\#module-manim.mobject.table "Link to this heading")

Mobjects representing tables.

Examples

Example: TableExamples [¶](https://docs.manim.community/en/stable/reference/manim.mobject.table.html#tableexamples)

![../_images/TableExamples-1.png](https://docs.manim.community/en/stable/_images/TableExamples-1.png)

```
from manim import *

class TableExamples(Scene):
    def construct(self):
        t0 = Table(
            [["First", "Second"],\
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Text("TOP"))
        t0.add_highlighted_cell((2,2), color=GREEN)
        x_vals = np.linspace(-2,2,5)
        y_vals = np.exp(x_vals)
        t1 = DecimalTable(
            [x_vals, y_vals],
            row_labels=[MathTex("x"), MathTex("f(x)")],
            include_outer_lines=True)
        t1.add(t1.get_cell((2,2), color=RED))
        t2 = MathTable(
            [["+", 0, 5, 10],\
            [0, 0, 5, 10],\
            [2, 2, 7, 12],\
            [4, 4, 9, 14]],
            include_outer_lines=True)
        t2.get_horizontal_lines()[:3].set_color(BLUE)
        t2.get_vertical_lines()[:3].set_color(BLUE)
        t2.get_horizontal_lines()[:3].set_z_index(1)
        cross = VGroup(
            Line(UP + LEFT, DOWN + RIGHT),
            Line(UP + RIGHT, DOWN + LEFT))
        a = Circle().set_color(RED).scale(0.5)
        b = cross.set_color(BLUE).scale(0.5)
        t3 = MobjectTable(
            [[a.copy(),b.copy(),a.copy()],\
            [b.copy(),a.copy(),a.copy()],\
            [a.copy(),b.copy(),b.copy()]])
        t3.add(Line(
            t3.get_corner(DL), t3.get_corner(UR)
        ).set_color(RED))
        vals = np.arange(1,21).reshape(5,4)
        t4 = IntegerTable(
            vals,
            include_outer_lines=True
        )
        g1 = Group(t0, t1).scale(0.5).arrange(buff=1).to_edge(UP, buff=1)
        g2 = Group(t2, t3, t4).scale(0.5).arrange(buff=1).to_edge(DOWN, buff=1)
        self.add(g1, g2)

```

Copy to clipboard

Make interactive

Classes

|     |     |
| --- | --- |
| [`DecimalTable`](https://docs.manim.community/en/stable/reference/manim.mobject.table.DecimalTable.html#manim.mobject.table.DecimalTable "manim.mobject.table.DecimalTable") | A specialized [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") mobject for use with [`DecimalNumber`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") to display decimal entries. |
| [`IntegerTable`](https://docs.manim.community/en/stable/reference/manim.mobject.table.IntegerTable.html#manim.mobject.table.IntegerTable "manim.mobject.table.IntegerTable") | A specialized [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") mobject for use with [`Integer`](https://docs.manim.community/en/stable/reference/manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer"). |
| [`MathTable`](https://docs.manim.community/en/stable/reference/manim.mobject.table.MathTable.html#manim.mobject.table.MathTable "manim.mobject.table.MathTable") | A specialized [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") mobject for use with LaTeX. |
| [`MobjectTable`](https://docs.manim.community/en/stable/reference/manim.mobject.table.MobjectTable.html#manim.mobject.table.MobjectTable "manim.mobject.table.MobjectTable") | A specialized [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") mobject for use with [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`Table`](https://docs.manim.community/en/stable/reference/manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") | A mobject that displays a table on the screen. |