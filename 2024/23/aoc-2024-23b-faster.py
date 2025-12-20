#!/usr/bin/env python3

"""LAN party is at the largest fully connected group of PCs"""

from collections import defaultdict


def extend_networks(networks, connected_pcs, seen):
    result = set()
    for network in networks:
        network = list(network)
        for pc in connected_pcs:
            if pc in seen or pc in network:
                continue
            if all(n in connections[pc] for n in network):
                result.add(tuple(sorted(network + [pc])))
    return result


connections = defaultdict(set)
with open("input.txt") as f:
    for line in f:
        pc = line.strip().split("-")
        connections[pc[0]].add(pc[1])
        connections[pc[1]].add(pc[0])

largest_networks, seen = set(), set()
for pc, connected_pcs in connections.items():
    networks = set([tuple([pc])])  # start with a single node network
    while True:  # keep extending it with nodes while still fully connected
        if not (ext_net := extend_networks(networks, connected_pcs, seen)):
            break  # one step to far, largest network was found in previous step
        networks = ext_net
    largest_networks.update(networks)
    seen.add(pc)

# find the largest network, this is where the lan party is
lan_party = set()
for network in largest_networks:
    if len(network) > len(lan_party):
        lan_party = network
print(",".join(lan_party))  # cc,ff,fh,fr,ny,oa,pl,rg,uj,wd,xn,xs,zw
