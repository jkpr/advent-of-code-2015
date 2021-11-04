from collections import Counter
from itertools import combinations
from typing import List

from ..utils import lines_to_int


@lines_to_int
def part1(lines: List[str]):
    count = 0
    for i in range(1, len(lines) + 1):
        for combo in combinations(lines, i):
            if sum(combo) == 150:
                count += 1
    return count


@lines_to_int
def part2(lines: List[str]):
    counter = Counter()
    for i in range(1, len(lines) + 1):
        for combo in combinations(lines, i):
            if sum(combo) == 150:
                counter[i] += 1
    return counter[min(counter)]
