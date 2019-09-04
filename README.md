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


class RandomGraphs(Scene):

    def construct(self):
        import time
        # list of colors to choose from
        COLORS = [RED, BLUE, GREEN, ORANGE, YELLOW]
        np.random.seed(int(time.time()))

        # make a random graph
        G1 = nx.erdos_renyi_graph(10, 0.5)
        # choose random colors for the nodes
        for node in G1.nodes.values():
            node['color'] = random.choice(COLORS)

        # make the manim graph
        mng = mnx.ManimGraph(G1)

        self.play(*[ShowCreation(m) for m in mng])  # create G1
        self.wait(1)

        # lets get a new graph
        G2 = G1.copy()
        mnx.assign_positions(G2)  # assign new node positions

        # add and remove random edges
        new_G = nx.erdos_renyi_graph(10, 0.5)
        G2.add_edges_from(new_G.edges)
        for edge in G1.edges:
            if edge not in new_G.edges:
                G2.remove_edge(*edge)

        # recolor nodes randomly
        for node in G2.nodes.values():
            node['color'] = random.choice(COLORS)

        # the transform_graph function neatly moves nodes to their new
        # positions along with edges that remain. New edges are faded in and
        # removed ones are faded out. Try to replace this with a vanilla
        # Transform and notice the difference.
        self.play(*mnx.transform_graph(mng, G2))  # transform G1 to G2

        # vanilla transform mixes up all mobjects, and doesn't look as good
        # self.play(Transform(mng, mnx.ManimGraph(G2)))
        self.wait(1)
```
