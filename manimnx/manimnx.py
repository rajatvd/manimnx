import networkx as nx
import numpy as np

from manimlib.imports import *

# outsource exact details of node and edge creation to user
# provide convenience functions for moving nodes and edges
# get item and stuff similar to nx but return the vmobject instead of the key


def get_dot_node(n, G):
    """Create a dot node with a given color.

    Uses RED by default.

    Parameters
    ----------
    n :
        Node key for graph G.

    Returns
    -------
    Dot
        The Dot VMobject.

    """
    n = G.node[n]
    node = Dot(color=n.get('color', RED))
    x, y = n['pos']
    node.move_to(x*RIGHT + y*UP)
    return node


def get_line_edge(ed, G):
    """Create a line edge using the color of node n1.

    Uses WHITE by default.

    Parameters
    ----------
    ed:
        Edge key for the networkx graph G.

    Returns
    -------
    Line
        The Line VMobject.

    """
    n1 = G.node[ed[0]]
    n2 = G.node[ed[1]]
    x1, y1 = n1['pos']
    x2, y2 = n2['pos']
    start = x1*RIGHT + y1*UP
    end = x2*RIGHT + y2*UP
    return Line(start, end, color=n1.get('color', WHITE))


class ManimGraph(VGroup):
    """A manim VGroup which wraps a networkx Graph.

    Parameters
    ----------
    graph : networkx.Graph
        The graph to wrap.
    get_node : function (node, Graph) -> VMobject
        Create the VMobject for the given node in the given Graph.
    get_edge : function (node1, node2, Graph) -> VMobject
        Create the VMobject for the edge between the given nodes in the given
        Graph. If the graph is a MultiGraph, the edge index k is also passed
        into get_edge

    Additional kwargs are passed to VGroup.

    Attributes
    ----------
    edges : dict
        Dictionary similar to Graph.edges with elements being the created
        VMobjects for the edges.
    nodes : dict
        Dictionary similar to Graph.nodes with elements being the created
        VMobjects for the nodes.

    """

    def __init__(self, graph,
                 get_node=get_dot_node,
                 get_edge=get_line_edge, **kwargs):
        super().__init__(**kwargs)
        self.graph = graph
        self.get_edge = get_edge
        self.get_node = get_node

        self.edges = {}
        self.nodes = {}

        n = list(self.graph.nodes())[0]
        scale = np.array([6.5, 3.5])
        if 'pos' not in self.graph.node[n].keys():
            unscaled_pos = nx.spring_layout(self.graph)
            positions = {k: v*scale for k, v in unscaled_pos.items()}
            for node, pos in positions.items():
                self.graph.node[node]['pos'] = pos

        self.count = 0
        self._add_nodes()
        self._add_edges()

    def _add_nodes(self):
        """Create nodes using get_node and add to submobjects and nodes dict."""
        for node in self.graph.nodes:
            n = self.get_node(node, self.graph)
            self.graph.nodes[node]['mob_id'] = self.count
            self.nodes[self.count] = n
            self.add(n)
            self.count += 1

    def _add_edges(self):
        """Create edges using get_edge and add to submobjects and edges dict."""
        for ed in self.graph.edges:
            self.graph.edges[ed]['mob_id'] = self.count
            e = self.get_edge(ed, self.graph)
            self.edges[self.count] = e
            self.add_to_back(e)
            self.count += 1
