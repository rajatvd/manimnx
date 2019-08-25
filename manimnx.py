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
        self.add_edges()
        self.add_nodes()

    def add_nodes(self):
        for node in self.graph.nodes:
            self.get_node(node)

    def add_edges(self):
        for n1, n2 in self.graph.edges:
            self.get_edge(n1, n2)
