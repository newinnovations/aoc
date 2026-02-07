#!/usr/bin/env python3

import networkx as nx

g = nx.Graph()
with open(0) as f:
    for line in f:
        components = line.strip().replace(":", "").split()
        f = components[0]
        for t in components[1:]:
            g.add_edge(f, t)


edge_cut = nx.minimum_edge_cut(g)
assert len(edge_cut) == 3
g.remove_edges_from(edge_cut)
g1, g2 = nx.connected_components(g)
print(len(g1) * len(g2))  # 555856
