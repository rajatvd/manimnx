import networkx as nx
import numpy as np

from manimlib.imports import *

# outsource exact details of node and edge creation to user
# provide convenience functions for moving nodes and edges
# get item and stuff similar to nx but return the vmobject instead of the key


class ManimGraph(VGroup):
    """A manim VGroup which wraps a networkx Graph.

    Parameters
    ----------
    graph : networkx.Graph
        The graph to wrap.
    get_node : function (dict) -> VMobject
        Create the VMobject for the given node attributes.
    get_edge : function (dict, dict) -> VMobject
        Create the VMobject for the edge between the given node attributes.

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

    def __init__(self, graph, get_node, get_edge, **kwargs):
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

        self.add_nodes()
        self.add_edges()

    def add_nodes(self):
        """Create nodes using get_node and add to submobjects and nodes dict."""
        for node in self.graph.nodes:
            n = self.get_node(self.graph.node[node])
            self.nodes[node] = n
            self.add(n)

    def add_edges(self):
        """Create edges using get_edge and add to submobjects and edges dict."""
        for n1, n2 in self.graph.edges:
            e = self.get_edge(self.graph.node[n1], self.graph.node[n2])
            self.edges[n1, n2] = e
            self.add_to_back(e)
