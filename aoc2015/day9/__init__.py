from itertools import permutations
import re
from typing import List

import networkx as nx


def get_all_distances(lines):
    G = nx.Graph()
    for line in lines:
        found = re.fullmatch(r"(.+) to (.+) = (\d+)", line)
        node1 = found.group(1)
        node2 = found.group(2)
        distance = int(found.group(3))
        G.add_edge(node1, node2, distance=distance)
    all_dist = set()
    for path in permutations(G.nodes):
        dist = 0
        for a, b in zip(path, path[1:]):
            dist += G.get_edge_data(a, b)["distance"]
        all_dist.add(dist)
    return all_dist


def part1(lines: List[str]):
    return min(get_all_distances(lines))


def part2(lines: List[str]):
    return max(get_all_distances(lines))
