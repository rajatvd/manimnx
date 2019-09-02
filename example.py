from manimlib.imports import *
import networkx as nx
import manimnx.manimnx as mnx
import numpy as np
import random


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
        mng1 = mnx.ManimGraph(G1)
        mng2 = mnx.ManimGraph(G2)

        self.play(*[ShowCreation(m) for m in mng1])  # create G1
        self.wait(1)

        self.play(Transform(mng1, mng2))  # transform G1 to G2
        self.wait(1)
