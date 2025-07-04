ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Graph [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html\#graph "Link to this heading")

Qualified name: `manim.mobject.graph.Graph`

_class_ Graph( _vertices_, _edges_, _labels=False_, _label\_fill\_color=ManimColor('#000000')_, _layout='spring'_, _layout\_scale=2_, _layout\_config=None_, _vertex\_type=<class'manim.mobject.geometry.arc.Dot'>_, _vertex\_config=None_, _vertex\_mobjects=None_, _edge\_type=<class'manim.mobject.geometry.line.Line'>_, _partitions=None_, _root\_vertex=None_, _edge\_config=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#Graph) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph "Link to this definition")

Bases: [`GenericGraph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph "manim.mobject.graph.GenericGraph")

An undirected graph (vertices connected with edges).

The graph comes with an updater which makes the edges stick to
the vertices when moved around. See [`DiGraph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.DiGraph.html#manim.mobject.graph.DiGraph "manim.mobject.graph.DiGraph") for
a version with directed edges.

See also

[`GenericGraph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html#manim.mobject.graph.GenericGraph "manim.mobject.graph.GenericGraph")

Parameters:

- **vertices** ( _Sequence_ _\[_ _Hashable_ _\]_) – A list of vertices. Must be hashable elements.

- **edges** ( _Sequence_ _\[_ _tuple_ _\[_ _Hashable_ _,_ _Hashable_ _\]_ _\]_) – A list of edges, specified as tuples `(u, v)` where both `u`
and `v` are vertices. The vertex order is irrelevant.

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
for automatic vertex positioning using `networkx`
(see [their documentation](https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout)
for more details), or a dictionary specifying a coordinate (value)
for each vertex (key) for manual positioning.

- **layout\_config** ( _dict_ _\|_ _None_) – Only for automatically generated layouts. A dictionary whose entries
are passed as keyword arguments to the automatic layout algorithm
specified via `layout` of `networkx`.
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

- **edge\_config** ( _dict_ _\|_ _None_) – Either a dictionary containing keyword arguments to be passed
to the class specified via `edge_type`, or a dictionary whose
keys are the edges, and whose values are dictionaries containing
keyword arguments for the mobject related to the corresponding edge.

- **partitions** ( _Sequence_ _\[_ _Sequence_ _\[_ _Hashable_ _\]_ _\]_ _\|_ _None_)

- **root\_vertex** ( _Hashable_ _\|_ _None_)


Examples

First, we create a small graph and demonstrate that the edges move
together with the vertices.

Example: MovingVertices [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#movingvertices)

```
from manim import *

class MovingVertices(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        g = Graph(vertices, edges)
        self.play(Create(g))
        self.wait()
        self.play(g[1].animate.move_to([1, 1, 0]),
                  g[2].animate.move_to([-1, 1, 0]),
                  g[3].animate.move_to([1, -1, 0]),
                  g[4].animate.move_to([-1, -1, 0]))
        self.wait()

```

Copy to clipboard

Make interactive

There are several automatic positioning algorithms to choose from:

Example: GraphAutoPosition [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#graphautoposition)

![../_images/GraphAutoPosition-1.png](https://docs.manim.community/en/stable/_images/GraphAutoPosition-1.png)

```
from manim import *

class GraphAutoPosition(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),\
                 (2, 8), (3, 4), (6, 1), (6, 2),\
                 (6, 3), (7, 2), (7, 4)]
        autolayouts = ["spring", "circular", "kamada_kawai",\
                       "planar", "random", "shell",\
                       "spectral", "spiral"]
        graphs = [Graph(vertices, edges, layout=lt).scale(0.5)\
                  for lt in autolayouts]
        r1 = VGroup(*graphs[:3]).arrange()
        r2 = VGroup(*graphs[3:6]).arrange()
        r3 = VGroup(*graphs[6:]).arrange()
        self.add(VGroup(r1, r2, r3).arrange(direction=DOWN))

```

Copy to clipboard

Make interactive

Vertices can also be positioned manually:

Example: GraphManualPosition [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#graphmanualposition)

![../_images/GraphManualPosition-1.png](https://docs.manim.community/en/stable/_images/GraphManualPosition-1.png)

```
from manim import *

class GraphManualPosition(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        lt = {1: [0, 0, 0], 2: [1, 1, 0], 3: [1, -1, 0], 4: [-1, 0, 0]}
        G = Graph(vertices, edges, layout=lt)
        self.add(G)

```

Copy to clipboard

Make interactive

The vertices in graphs can be labeled, and configurations for vertices
and edges can be modified both by default and for specific vertices and
edges.

Note

In `edge_config`, edges can be passed in both directions: if
`(u, v)` is an edge in the graph, both `(u, v)` as well
as `(v, u)` can be used as keys in the dictionary.

Example: LabeledModifiedGraph [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#labeledmodifiedgraph)

![../_images/LabeledModifiedGraph-1.png](https://docs.manim.community/en/stable/_images/LabeledModifiedGraph-1.png)

```
from manim import *

class LabeledModifiedGraph(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),\
                 (2, 8), (3, 4), (6, 1), (6, 2),\
                 (6, 3), (7, 2), (7, 4)]
        g = Graph(vertices, edges, layout="circular", layout_scale=3,
                  labels=True, vertex_config={7: {"fill_color": RED}},
                  edge_config={(1, 7): {"stroke_color": RED},
                               (2, 7): {"stroke_color": RED},
                               (4, 7): {"stroke_color": RED}})
        self.add(g)

```

Copy to clipboard

Make interactive

You can also lay out a partite graph on columns by specifying
a list of the vertices on each side and choosing the partite layout.

Note

All vertices in your graph which are not listed in any of the partitions
are collected in their own partition and rendered in the rightmost column.

Example: PartiteGraph [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#partitegraph)

![../_images/PartiteGraph-1.png](https://docs.manim.community/en/stable/_images/PartiteGraph-1.png)

```
from manim import *

import networkx as nx

class PartiteGraph(Scene):
    def construct(self):
        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3])
        G.add_edges_from([(0, 2), (0,3), (1, 2)])
        graph = Graph(list(G.nodes), list(G.edges), layout="partite", partitions=[[0, 1]])
        self.play(Create(graph))

```

Copy to clipboard

Make interactive

The representation of a linear artificial neural network is facilitated
by the use of the partite layout and defining partitions for each layer.

Example: LinearNN [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#linearnn)

![../_images/LinearNN-1.png](https://docs.manim.community/en/stable/_images/LinearNN-1.png)

```
from manim import *

class LinearNN(Scene):
    def construct(self):
        edges = []
        partitions = []
        c = 0
        layers = [2, 3, 3, 2]  # the number of neurons in each layer

        for i in layers:
            partitions.append(list(range(c + 1, c + i + 1)))
            c += i
        for i, v in enumerate(layers[1:]):
                last = sum(layers[:i+1])
                for j in range(v):
                    for k in range(last - layers[i], last):
                        edges.append((k + 1, j + last + 1))

        vertices = np.arange(1, sum(layers) + 1)

        graph = Graph(
            vertices,
            edges,
            layout='partite',
            partitions=partitions,
            layout_scale=3,
            vertex_config={'radius': 0.20},
        )
        self.add(graph)

```

Copy to clipboard

Make interactive

The custom tree layout can be used to show the graph
by distance from the root vertex. You must pass the root vertex
of the tree.

Example: Tree [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#tree)

```
from manim import *

import networkx as nx

class Tree(Scene):
    def construct(self):
        G = nx.Graph()

        G.add_node("ROOT")

        for i in range(5):
            G.add_node("Child_%i" % i)
            G.add_node("Grandchild_%i" % i)
            G.add_node("Greatgrandchild_%i" % i)

            G.add_edge("ROOT", "Child_%i" % i)
            G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
            G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

        self.play(Create(
            Graph(list(G.nodes), list(G.edges), layout="tree", root_vertex="ROOT")))

```

Copy to clipboard

Make interactive

The following code sample illustrates the use of the `vertex_spacing`
layout parameter specific to the `"tree"` layout. As mentioned
above, setting `vertex_spacing` overrides the specified value
for `layout_scale`, and as such it is harder to control the size
of the mobject. However, we can adjust the captured frame and
zoom out by using a [`MovingCameraScene`](https://docs.manim.community/en/stable/reference/manim.scene.moving_camera_scene.MovingCameraScene.html#manim.scene.moving_camera_scene.MovingCameraScene "manim.scene.moving_camera_scene.MovingCameraScene"):

```
class LargeTreeGeneration(MovingCameraScene):
    DEPTH = 4
    CHILDREN_PER_VERTEX = 3
    LAYOUT_CONFIG = {"vertex_spacing": (0.5, 1)}
    VERTEX_CONF = {"radius": 0.25, "color": BLUE_B, "fill_opacity": 1}

    def expand_vertex(self, g, vertex_id: str, depth: int):
        new_vertices = [\
            f"{vertex_id}/{i}" for i in range(self.CHILDREN_PER_VERTEX)\
        ]
        new_edges = [(vertex_id, child_id) for child_id in new_vertices]
        g.add_edges(
            *new_edges,
            vertex_config=self.VERTEX_CONF,
            positions={
                k: g.vertices[vertex_id].get_center() + 0.1 * DOWN
                for k in new_vertices
            },
        )
        if depth < self.DEPTH:
            for child_id in new_vertices:
                self.expand_vertex(g, child_id, depth + 1)

        return g

    def construct(self):
        g = Graph(["ROOT"], [], vertex_config=self.VERTEX_CONF)
        g = self.expand_vertex(g, "ROOT", 1)
        self.add(g)

        self.play(
            g.animate.change_layout(
                "tree",
                root_vertex="ROOT",
                layout_config=self.LAYOUT_CONFIG,
            )
        )
        self.play(self.camera.auto_zoom(g, margin=1), run_time=0.5)

```

Copy to clipboard

Methods

|     |     |
| --- | --- |
| `update_edges` |  |

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

_static_\_empty\_networkx\_graph() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#Graph._empty_networkx_graph) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph._empty_networkx_graph "Link to this definition")

Return an empty networkx graph for the given graph type.

Return type:

_Graph_

\_original\_\_init\_\_( _vertices_, _edges_, _labels=False_, _label\_fill\_color=ManimColor('#000000')_, _layout='spring'_, _layout\_scale=2_, _layout\_config=None_, _vertex\_type=<class'manim.mobject.geometry.arc.Dot'>_, _vertex\_config=None_, _vertex\_mobjects=None_, _edge\_type=<class'manim.mobject.geometry.line.Line'>_, _partitions=None_, _root\_vertex=None_, _edge\_config=None_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph._original__init__ "Link to this definition")

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

\_populate\_edge\_dict( _edges_, _edge\_type_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html#Graph._populate_edge_dict) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html#manim.mobject.graph.Graph._populate_edge_dict "Link to this definition")

Helper method for populating the edges of the graph.

Parameters:

- **edges** ( _list_ _\[_ _tuple_ _\[_ _Hashable_ _,_ _Hashable_ _\]_ _\]_)

- **edge\_type** ( _type_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_)