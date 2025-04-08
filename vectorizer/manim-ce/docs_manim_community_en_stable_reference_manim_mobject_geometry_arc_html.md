ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# arc [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.html\#module-manim.mobject.geometry.arc "Link to this heading")

Mobjects that are curved.

Examples

Example: UsefulAnnotations [¶](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.html#usefulannotations)

![../_images/UsefulAnnotations-1.png](https://docs.manim.community/en/stable/_images/UsefulAnnotations-1.png)

```
from manim import *

class UsefulAnnotations(Scene):
    def construct(self):
        m0 = Dot()
        m1 = AnnotationDot()
        m2 = LabeledDot("ii")
        m3 = LabeledDot(MathTex(r"\alpha").set_color(ORANGE))
        m4 = CurvedArrow(2*LEFT, 2*RIGHT, radius= -5)
        m5 = CurvedArrow(2*LEFT, 2*RIGHT, radius= 8)
        m6 = CurvedDoubleArrow(ORIGIN, 2*RIGHT)

        self.add(m0, m1, m2, m3, m4, m5, m6)
        for i, mobj in enumerate(self.mobjects):
            mobj.shift(DOWN * (i-3))

```

Copy to clipboard

Make interactive

Classes

|     |     |
| --- | --- |
| [`AnnotationDot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.AnnotationDot.html#manim.mobject.geometry.arc.AnnotationDot "manim.mobject.geometry.arc.AnnotationDot") | A dot with bigger radius and bold stroke to annotate scenes. |
| [`AnnularSector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.AnnularSector.html#manim.mobject.geometry.arc.AnnularSector "manim.mobject.geometry.arc.AnnularSector") | A sector of an annulus. |
| [`Annulus`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html#manim.mobject.geometry.arc.Annulus "manim.mobject.geometry.arc.Annulus") | Region between two concentric [`Circles`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle"). |
| [`Arc`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc") | A circular arc. |
| [`ArcBetweenPoints`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcBetweenPoints.html#manim.mobject.geometry.arc.ArcBetweenPoints "manim.mobject.geometry.arc.ArcBetweenPoints") | Inherits from Arc and additionally takes 2 points between which the arc is spanned. |
| [`ArcPolygon`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcPolygon.html#manim.mobject.geometry.arc.ArcPolygon "manim.mobject.geometry.arc.ArcPolygon") | A generalized polygon allowing for points to be connected with arcs. |
| [`ArcPolygonFromArcs`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.ArcPolygonFromArcs.html#manim.mobject.geometry.arc.ArcPolygonFromArcs "manim.mobject.geometry.arc.ArcPolygonFromArcs") | A generalized polygon allowing for points to be connected with arcs. |
| [`Circle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle") | A circle. |
| [`CubicBezier`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CubicBezier.html#manim.mobject.geometry.arc.CubicBezier "manim.mobject.geometry.arc.CubicBezier") | A cubic Bézier curve. |
| [`CurvedArrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CurvedArrow.html#manim.mobject.geometry.arc.CurvedArrow "manim.mobject.geometry.arc.CurvedArrow") |  |
| [`CurvedDoubleArrow`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.CurvedDoubleArrow.html#manim.mobject.geometry.arc.CurvedDoubleArrow "manim.mobject.geometry.arc.CurvedDoubleArrow") |  |
| [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot "manim.mobject.geometry.arc.Dot") | A circle with a very small radius. |
| [`Ellipse`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Ellipse.html#manim.mobject.geometry.arc.Ellipse "manim.mobject.geometry.arc.Ellipse") | A circular shape; oval, circle. |
| [`LabeledDot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.LabeledDot.html#manim.mobject.geometry.arc.LabeledDot "manim.mobject.geometry.arc.LabeledDot") | A [`Dot`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot "manim.mobject.geometry.arc.Dot") containing a label in its center. |
| [`Sector`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Sector.html#manim.mobject.geometry.arc.Sector "manim.mobject.geometry.arc.Sector") | A sector of a circle. |
| [`TipableVMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.TipableVMobject.html#manim.mobject.geometry.arc.TipableVMobject "manim.mobject.geometry.arc.TipableVMobject") | Meant for shared functionality between Arc and Line. |