import networkx as nx

from manimlib.imports import *

# outsource exact details of node and edge creation to user
# provide convenience functions for moving nodes and edges
# that... should be all i guess


class ManimNX(VGroup):
    def __init__(self, graph, get_node, get_edge, **kwargs):
        super().__init__(**kwargs)
        self.graph = graph
        self.get_edge = get_edge
        self.get_node = get_node
        self.add_nodes()
        self.add_edges()

    def add_nodes(self):
        for node in self.graph.nodes:
            n = self.get_node(self.graph.node[node])
            self.add(n)

    def add_edges(self):
        for n1, n2 in self.graph.edges:
            e = self.get_edge(self.graph.node[n1], self.graph.node[n2])
            self.add_to_back(e)
