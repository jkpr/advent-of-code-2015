from itertools import combinations
import math
from typing import List

from ..utils import lines_to_int


@lines_to_int
def part1(lines: List[str]):
    total = sum(lines)
    group_weight = total // 3
    minimum_group = min(
        i for i in range(1, len(lines)) if sum(lines[-i:]) >= group_weight
    )
    found = []
    for i in range(minimum_group, minimum_group + 5):
        print(i)
        for combo in combinations(lines, i):
            if sum(combo) == group_weight:
                found.append(combo)
    complexity = [math.prod(i) for i in found]
    return min(complexity)


@lines_to_int
def part2(lines: List[str]):
    total = sum(lines)
    group_weight = total // 4
    minimum_group = min(
        i for i in range(1, len(lines)) if sum(lines[-i:]) >= group_weight
    )
    found = []
    for i in range(minimum_group, minimum_group + 5):
        print(i)
        for combo in combinations(lines, i):
            if sum(combo) == group_weight:
                found.append(combo)
    complexity = [math.prod(i) for i in found]
    return min(complexity)
