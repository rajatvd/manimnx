import networkx as nx

from manimlib.imports import *

# outsource exact details of node and edge creation to user
# provide convenience functions for moving nodes and edges
# that... should be all i guess


class ManimNX(VGroup):
    def __init__(self, graph, **kwargs):
        super().__init__(**kwargs)
        self.graph = graph
        self.add_edges()
        self.add_nodes()

    def add_nodes(self):
        pass

    def add_edges(self):
        pass
