# manim-nx
An interface between `networkx` and `manim` to make animating graphs easier.

An example animation which transforms between two random graphs:

![](random_graphs.gif)


# Install

Install using this command:

`pip install git+https://github.com/rajatvd/manim-nx`

Requires `manimlib` and `networkx`.

# Example

To generate the example shown above, run this command after cloning this repo:

`manim example.py RandomGraphs -mi`

The `-m` flag is for medium quality, and `-i` is to generate a gif instead of an mp4.


Here is the code to generate the example gif. You can find it in [`example.py`](https://github.com/rajatvd/manim-nx/blob/master/example.py).

```py
from manimlib.imports import *
import networkx as nx
import manimnx.manimnx as mnx
import numpy as np
import random


# Define methods to create vmobjects for nodes and edges using their networkx attributes

def get_node(n, G):
    """Get a Dot node."""
    n = G.node[n]
    node = Dot(color=n.get('color', RED))
    x, y = n['pos']
    node.move_to(x*RIGHT + y*UP)
    return node


def get_edge(n1, n2, G):
    """Get a Line edge."""
    n1 = G.node[n1]
    n2 = G.node[n2]
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

        # make two random graphs with 10 nodes
        G1 = nx.erdos_renyi_graph(10, 0.5)
        G2 = nx.erdos_renyi_graph(10, 0.5)

        # choose random colors for the nodes
        for node in G1.nodes:
            G1.nodes[node]['color'] = random.choice(COLORS)
            G2.nodes[node]['color'] = random.choice(COLORS)

        # make the manim graphs
        mng1 = mnx.ManimGraph(G1, get_node, get_edge)
        mng2 = mnx.ManimGraph(G2, get_node, get_edge)

        self.play(*[ShowCreation(m) for m in mng1])  # create G1
        self.wait(1)
        self.play(Transform(mng1, mng2))  # transform G1 to G2
        self.wait(1)

```
