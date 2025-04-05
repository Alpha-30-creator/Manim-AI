ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# GenericGraph [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html\#genericgraph "Link to this heading")

Qualified name: `manim.mobject.graph.GenericGraph`

_class_ GenericGraph( _vertices_, _edges_, _labels=False_, _label\_fill\_color=ManimColor('#000000')_, _layout='spring'_, _layout\_scale=2_, _layout\_config=None_, _vertex\_type=<class'manim.mobject.geometry.arc.Dot'>_, _vertex\_config=None_, _vertex\_mobjects=None_, _edge\_type=<class'manim.mobject.geometry.line.Line'>_, _partitions=None_, _root\_vertex=None_, _edge\_config=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#GenericGraph) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

Abstract base class for graphs (that is, a collection of vertices
connected with edges).

Graphs can be instantiated by passing both a list of (distinct, hashable)
vertex names, together with list of edges (as tuples of vertex names). See
the examples for concrete implementations of this class for details.

Note

This implementation uses updaters to make the edges move with
the vertices.

See also

[`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph"), [`DiGraph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph")

Parameters:

- **vertices** ( _Sequence_ _\[_ _Hashable_ _\]_) – A list of vertices. Must be hashable elements.

- **edges** ( _Sequence_ _\[_ _tuple_ _\[_ _Hashable_ _,_ _Hashable_ _\]_ _\]_) – A list of edges, specified as tuples `(u, v)` where both `u`
and `v` are vertices.

- **labels** ( _bool_ _\|_ _dict_) – Controls whether or not vertices are labeled. If `False` (the default),
the vertices are not labeled; if `True` they are labeled using their
names (as specified in `vertices`) via [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex"). Alternatively,
custom labels can be specified by passing a dictionary whose keys are
the vertices, and whose values are the corresponding vertex labels
(rendered via, e.g., [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") or [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")).

- **label\_fill\_color** ( _str_) – Sets the fill color of the default labels generated when `labels`
is set to `True`. Has no effect for other values of `labels`.

- **layout** ( _LayoutName_ _\|_ _dict_ _\[_ _Hashable_ _,_ [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\]_ _\|_ [_LayoutFunction_](https://docs.manim.community/en/stable/reference/manim.mobject.graph.LayoutFunction.html#manim.mobject.graph.LayoutFunction "manim.mobject.graph.LayoutFunction")) – Either one of `"spring"` (the default), `"circular"`, `"kamada_kawai"`,
`"planar"`, `"random"`, `"shell"`, `"spectral"`, `"spiral"`, `"tree"`, and `"partite"`
for automatic vertex positioning primarily using `networkx`
(see [their documentation](https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout)
for more details), a dictionary specifying a coordinate (value)
for each vertex (key) for manual positioning, or a .:class:~.LayoutFunction with a user-defined automatic layout.

- **layout\_config** ( _dict_ _\|_ _None_) – Only for automatic layouts. A dictionary whose entries
are passed as keyword arguments to the named layout or automatic layout function
specified via `layout`.
The `tree` layout also accepts a special parameter `vertex_spacing`
passed as a keyword argument inside the `layout_config` dictionary.
Passing a tuple `(space_x, space_y)` as this argument overrides
the value of `layout_scale` and ensures that vertices are arranged
in a way such that the centers of siblings in the same layer are
at least `space_x` units apart horizontally, and neighboring layers
are spaced `space_y` units vertically.

- **layout\_scale** ( _float_ _\|_ _tuple_ _\[_ _float_ _,_ _float_ _,_ _float_ _\]_) – The scale of automatically generated layouts: the vertices will
be arranged such that the coordinates are located within the
interval `[-scale, scale]`. Some layouts accept a tuple `(scale_x, scale_y)`
causing the first coordinate to be in the interval `[-scale_x, scale_x]`,
and the second in `[-scale_y, scale_y]`. Default: 2.

- **vertex\_type** ( _type_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – The mobject class used for displaying vertices in the scene.

- **vertex\_config** ( _dict_ _\|_ _None_) – Either a dictionary containing keyword arguments to be passed to
the class specified via `vertex_type`, or a dictionary whose keys
are the vertices, and whose values are dictionaries containing keyword
arguments for the mobject related to the corresponding vertex.

- **vertex\_mobjects** ( _dict_ _\|_ _None_) – A dictionary whose keys are the vertices, and whose values are
mobjects to be used as vertices. Passing vertices here overrides
all other configuration options for a vertex.

- **edge\_type** ( _type_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – The mobject class used for displaying edges in the scene.
Must be a subclass of [`Line`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line") for default updaters to work.

- **edge\_config** ( _dict_ _\|_ _None_) – Either a dictionary containing keyword arguments to be passed
to the class specified via `edge_type`, or a dictionary whose
keys are the edges, and whose values are dictionaries containing
keyword arguments for the mobject related to the corresponding edge.

- **partitions** ( _Sequence_ _\[_ _Sequence_ _\[_ _Hashable_ _\]_ _\]_ _\|_ _None_)

- **root\_vertex** ( _Hashable_ _\|_ _None_)


Methods

|     |     |
| --- | --- |
| [`add_edges`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph.add_edges "manim.mobject.graph.GenericGraph.add_edges") | Add new edges to the graph. |
| [`add_vertices`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph.add_vertices "manim.mobject.graph.GenericGraph.add_vertices") | Add a list of vertices to the graph. |
| [`change_layout`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph.change_layout "manim.mobject.graph.GenericGraph.change_layout") | Change the layout of this graph. |
| [`from_networkx`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph.from_networkx "manim.mobject.graph.GenericGraph.from_networkx") | Build a [`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph") or [`DiGraph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph") from a given `networkx` graph. |
| [`remove_edges`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph.remove_edges "manim.mobject.graph.GenericGraph.remove_edges") | Remove several edges from the graph. |
| [`remove_vertices`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph.remove_vertices "manim.mobject.graph.GenericGraph.remove_vertices") | Remove several vertices from the graph. |

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

\_add\_edge( _edge_, _edge\_type=<class'manim.mobject.geometry.line.Line'>_, _edge\_config=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#GenericGraph._add_edge) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph._add_edge "Link to this definition")

Add a new edge to the graph.

Parameters:

- **edge** ( _tuple_ _\[_ _Hashable_ _,_ _Hashable_ _\]_) – The edge (as a tuple of vertex identifiers) to be added. If a non-existing
vertex is passed, a new vertex with default settings will be created. Create
new vertices yourself beforehand to customize them.

- **edge\_type** ( _type_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – The mobject class used for displaying edges in the scene.

- **edge\_config** ( _dict_ _\|_ _None_) – A dictionary containing keyword arguments to be passed
to the class specified via `edge_type`.


Returns:

A group containing all newly added vertices and edges.

Return type:

[Group](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")

\_add\_vertex( _vertex_, _position=None_, _label=False_, _label\_fill\_color=ManimColor('#000000')_, _vertex\_type=<class'manim.mobject.geometry.arc.Dot'>_, _vertex\_config=None_, _vertex\_mobject=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#GenericGraph._add_vertex) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph._add_vertex "Link to this definition")

Add a vertex to the graph.

Parameters:

- **vertex** ( _Hashable_) – A hashable vertex identifier.

- **position** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\|_ _None_) – The coordinates where the new vertex should be added. If `None`, the center
of the graph is used.

- **label** ( _bool_) – Controls whether or not the vertex is labeled. If `False` (the default),
the vertex is not labeled; if `True` it is labeled using its
names (as specified in `vertex`) via [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex"). Alternatively,
any [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") can be passed to be used as the label.

- **label\_fill\_color** ( _str_) – Sets the fill color of the default labels generated when `labels`
is set to `True`. Has no effect for other values of `label`.

- **vertex\_type** ( _type_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – The mobject class used for displaying vertices in the scene.

- **vertex\_config** ( _dict_ _\|_ _None_) – A dictionary containing keyword arguments to be passed to
the class specified via `vertex_type`.

- **vertex\_mobject** ( _dict_ _\|_ _None_) – The mobject to be used as the vertex. Overrides all other
vertex customization options.


Return type:

[Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

_static_\_empty\_networkx\_graph() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#GenericGraph._empty_networkx_graph) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph._empty_networkx_graph "Link to this definition")

Return an empty networkx graph for the given graph type.

Return type:

_Graph_

\_original\_\_init\_\_( _vertices_, _edges_, _labels=False_, _label\_fill\_color=ManimColor('#000000')_, _layout='spring'_, _layout\_scale=2_, _layout\_config=None_, _vertex\_type=<class'manim.mobject.geometry.arc.Dot'>_, _vertex\_config=None_, _vertex\_mobjects=None_, _edge\_type=<class'manim.mobject.geometry.line.Line'>_, _partitions=None_, _root\_vertex=None_, _edge\_config=None_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **vertices** ( _Sequence_ _\[_ _Hashable_ _\]_)

- **edges** ( _Sequence_ _\[_ _tuple_ _\[_ _Hashable_ _,_ _Hashable_ _\]_ _\]_)

- **labels** ( _bool_ _\|_ _dict_)

- **label\_fill\_color** ( _str_)

- **layout** ( _Literal_ _\[_ _'circular'_ _,_ _'kamada\_kawai'_ _,_ _'partite'_ _,_ _'planar'_ _,_ _'random'_ _,_ _'shell'_ _,_ _'spectral'_ _,_ _'spiral'_ _,_ _'spring'_ _,_ _'tree'_ _\]_ _\|_ _dict_ _\[_ _~collections.abc.Hashable_ _,_ _~manim.typing.Point3DLike_ _\]_ _\|_ _~manim.mobject.graph.LayoutFunction_)

- **layout\_scale** ( _float_ _\|_ _tuple_ _\[_ _float_ _,_ _float_ _,_ _float_ _\]_)

- **layout\_config** ( _dict_ _\|_ _None_)

- **vertex\_type** ( _type_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_)

- **vertex\_config** ( _dict_ _\|_ _None_)

- **vertex\_mobjects** ( _dict_ _\|_ _None_)

- **edge\_type** ( _type_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_)

- **partitions** ( _Sequence_ _\[_ _Sequence_ _\[_ _Hashable_ _\]_ _\]_ _\|_ _None_)

- **root\_vertex** ( _Hashable_ _\|_ _None_)

- **edge\_config** ( _dict_ _\|_ _None_)


Return type:

None

\_populate\_edge\_dict( _edges_, _edge\_type_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#GenericGraph._populate_edge_dict) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph._populate_edge_dict "Link to this definition")

Helper method for populating the edges of the graph.

Parameters:

- **edges** ( _list_ _\[_ _tuple_ _\[_ _Hashable_ _,_ _Hashable_ _\]_ _\]_)

- **edge\_type** ( _type_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_)


\_remove\_edge( _edge_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#GenericGraph._remove_edge) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph._remove_edge "Link to this definition")

Remove an edge from the graph.

Parameters:

**edge** ( _tuple_ _\[_ _Hashable_ _\]_) – The edge (i.e., a tuple of vertex identifiers) to be removed from the graph.

Returns:

The removed edge.

Return type:

[Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

\_remove\_vertex( _vertex_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#GenericGraph._remove_vertex) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph._remove_vertex "Link to this definition")

Remove a vertex (as well as all incident edges) from the graph.

Parameters:

**vertex** – The identifier of a vertex to be removed.

Returns:

A mobject containing all removed objects.

Return type:

[Group](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")

add\_edges( _\*edges_, _edge\_type=<class'manim.mobject.geometry.line.Line'>_, _edge\_config=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#GenericGraph.add_edges) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph.add_edges "Link to this definition")

Add new edges to the graph.

Parameters:

- **edges** ( _tuple_ _\[_ _Hashable_ _,_ _Hashable_ _\]_) – Edges (as tuples of vertex identifiers) to be added. If a non-existing
vertex is passed, a new vertex with default settings will be created. Create
new vertices yourself beforehand to customize them.

- **edge\_type** ( _type_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – The mobject class used for displaying edges in the scene.

- **edge\_config** ( _dict_ _\|_ _None_) – A dictionary either containing keyword arguments to be passed
to the class specified via `edge_type`, or a dictionary
whose keys are the edge tuples, and whose values are dictionaries
containing keyword arguments to be passed for the construction
of the corresponding edge.

- **kwargs** – Any further keyword arguments are passed to [`add_vertices()`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph.add_vertices "manim.mobject.graph.GenericGraph.add_vertices")
which is used to create new vertices in the passed edges.


Returns:

A group containing all newly added vertices and edges.

Return type:

[Group](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")

add\_vertices( _\*vertices_, _positions=None_, _labels=False_, _label\_fill\_color=ManimColor('#000000')_, _vertex\_type=<class'manim.mobject.geometry.arc.Dot'>_, _vertex\_config=None_, _vertex\_mobjects=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#GenericGraph.add_vertices) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph.add_vertices "Link to this definition")

Add a list of vertices to the graph.

Parameters:

- **vertices** ( _Hashable_) – Hashable vertex identifiers.

- **positions** ( _dict_ _\|_ _None_) – A dictionary specifying the coordinates where the new vertices should be added.
If `None`, all vertices are created at the center of the graph.

- **labels** ( _bool_) – Controls whether or not the vertex is labeled. If `False` (the default),
the vertex is not labeled; if `True` it is labeled using its
names (as specified in `vertex`) via [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex"). Alternatively,
any [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") can be passed to be used as the label.

- **label\_fill\_color** ( _str_) – Sets the fill color of the default labels generated when `labels`
is set to `True`. Has no effect for other values of `labels`.

- **vertex\_type** ( _type_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – The mobject class used for displaying vertices in the scene.

- **vertex\_config** ( _dict_ _\|_ _None_) – A dictionary containing keyword arguments to be passed to
the class specified via `vertex_type`.

- **vertex\_mobjects** ( _dict_ _\|_ _None_) – A dictionary whose keys are the vertex identifiers, and whose
values are mobjects that should be used as vertices. Overrides
all other vertex customization options.

- **self** ( [_Graph_](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph"))


change\_layout( _layout='spring'_, _layout\_scale=2_, _layout\_config=None_, _partitions=None_, _root\_vertex=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#GenericGraph.change_layout) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph.change_layout "Link to this definition")

Change the layout of this graph.

See the documentation of [`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph") for details about the
keyword arguments.

Examples

Example: ChangeGraphLayout [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#changegraphlayout)

```
from manim import *

class ChangeGraphLayout(Scene):
    def construct(self):
        G = Graph([1, 2, 3, 4, 5], [(1, 2), (2, 3), (3, 4), (4, 5)],
                  layout={1: [-2, 0, 0], 2: [-1, 0, 0], 3: [0, 0, 0],
                          4: [1, 0, 0], 5: [2, 0, 0]}
                  )
        self.play(Create(G))
        self.play(G.animate.change_layout("circular"))
        self.wait()

```

Copy to clipboard

Make interactive

Parameters:

- **layout** ( _Literal_ _\[_ _'circular'_ _,_ _'kamada\_kawai'_ _,_ _'partite'_ _,_ _'planar'_ _,_ _'random'_ _,_ _'shell'_ _,_ _'spectral'_ _,_ _'spiral'_ _,_ _'spring'_ _,_ _'tree'_ _\]_ _\|_ _dict_ _\[_ _~collections.abc.Hashable_ _,_ _~manim.typing.Point3DLike_ _\]_ _\|_ _~manim.mobject.graph.LayoutFunction_)

- **layout\_scale** ( _float_ _\|_ _tuple_ _\[_ _float_ _,_ _float_ _,_ _float_ _\]_)

- **layout\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **partitions** ( _list_ _\[_ _list_ _\[_ _Hashable_ _\]_ _\]_ _\|_ _None_)

- **root\_vertex** ( _Hashable_ _\|_ _None_)


Return type:

[_Graph_](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph")

_classmethod_ from\_networkx( _nxgraph_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#GenericGraph.from_networkx) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph.from_networkx "Link to this definition")

Build a [`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph") or [`DiGraph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph") from a
given `networkx` graph.

Parameters:

- **nxgraph** ( _Graph_ _\|_ _DiGraph_) – A `networkx` graph or digraph.

- **\*\*kwargs** – Keywords to be passed to the constructor of [`Graph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "manim.mobject.graph.Graph").


Examples

Example: ImportNetworkxGraph [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#importnetworkxgraph)

```
from manim import *

import networkx as nx

nxgraph = nx.erdos_renyi_graph(14, 0.5)

class ImportNetworkxGraph(Scene):
    def construct(self):
        G = Graph.from_networkx(nxgraph, layout="spring", layout_scale=3.5)
        self.play(Create(G))
        self.play(*[G[v].animate.move_to(5*RIGHT*np.cos(ind/7 * PI) +\
                                         3*UP*np.sin(ind/7 * PI))\
                    for ind, v in enumerate(G.vertices)])
        self.play(Uncreate(G))

```

Copy to clipboard

Make interactive

remove\_edges( _\*edges_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#GenericGraph.remove_edges) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph.remove_edges "Link to this definition")

Remove several edges from the graph.

Parameters:

**edges** ( _tuple_ _\[_ _Hashable_ _\]_) – Edges to be removed from the graph.

Returns:

A group containing all removed edges.

Return type:

[Group](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group")

remove\_vertices( _\*vertices_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#GenericGraph.remove_vertices) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph.remove_vertices "Link to this definition")

Remove several vertices from the graph.

Parameters:

**vertices** – Vertices to be removed from the graph.

Examples

```
>>> G = Graph([1, 2, 3], [(1, 2), (2, 3)])
>>> removed = G.remove_vertices(2, 3); removed
VGroup(Line, Line, Dot, Dot)
>>> G
Undirected graph on 1 vertices and 0 edges

```

Copy to clipboard