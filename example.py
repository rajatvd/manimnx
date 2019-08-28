from manimlib.imports import *
import networkx as nx
import manimnx.manimnx as mnx
import numpy as np
import random


def get_node(n):
    """Create a dot node with a given color.

    Uses RED by default.

    Parameters
    ----------
    n : dict
        The node attributes.

    Returns
    -------
    Dot
        The Dot VMobject.

    """
    node = Dot(color=n.get('color', RED))
    x, y = n['pos']
    node.move_to(x*RIGHT + y*UP)
    return node


def get_edge(n1, n2):
    """Create a line edge using the color of node n1.

    Uses WHITE by default.

    Parameters
    ----------
    n1, n2: dict
        Attributes of the nodes between which the edge exists

    Returns
    -------
    Line
        The Line VMobject.

    """
    x1, y1 = n1['pos']
    x2, y2 = n2['pos']
    start = x1*RIGHT + y1*UP
    end = x2*RIGHT + y2*UP
    return Line(start, end, color=n1.get('color', WHITE))


class RandomGraphs(Scene):

    def construct(self):

        # list of colors to choose from
        COLORS = [RED, BLUE, GREEN, ORANGE, YELLOW]
        np.random.seed()

        # make two random graphs
        G1 = nx.erdos_renyi_graph(10, 0.5)
        G2 = nx.erdos_renyi_graph(10, 0.5)

        # choose random colors for the nodes
        for node in G1.nodes:
            G1.nodes[node]['color'] = random.choice(COLORS)
            G2.nodes[node]['color'] = random.choice(COLORS)

        # make the manim graphs
        mng1 = mnx.ManimGraph(G1, get_node, get_edge)

#         for node in G2.nodes:
#             G2.nodes[node]['pos'] = G1.nodes[node]['pos']

        mng2 = mnx.ManimGraph(G2, get_node, get_edge)

        self.play(*[ShowCreation(m) for m in mng1])  # create G1
        self.wait(2)

#         edges1 = VGroup()
#         edges1.add(*mng1.edges.values())

#         edges2 = VGroup()
#         edges2.add(*mng2.edges.values())

#         self.play(Transform(edges1, edges2))
        self.play(Transform(mng1, mng2))  # transform G1 to G2
        self.wait(2)
