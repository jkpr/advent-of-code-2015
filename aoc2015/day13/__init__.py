from collections import defaultdict
from itertools import chain, permutations
import re
from typing import List


def get_happiness(lines, self = False):
    happiness = defaultdict(int)
    for line in lines:
        if found := re.match(r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).", line):
            name1 = found.group(1)
            name2 = found.group(4)
            sign = found.group(2)
            amount = int(found.group(3))
            if sign == "lose":
                amount *= -1
            happiness[(name1, name2)] += amount
            happiness[(name2, name1)] += amount
    return happiness


def get_max_happiness(lines, self=False):
    happiness = get_happiness(lines)
    people = set(chain.from_iterable(happiness))
    if self:
        people.add("self")
    max_happiness = 0
    for perm in permutations(people):
        total = 0
        for pair in zip(perm, perm[1:]):
            total += happiness[pair]
        total += happiness[(perm[0], perm[-1])]
        max_happiness = max(max_happiness, total)
    return max_happiness


def part1(lines: List[str]):
    return get_max_happiness(lines)


def part2(lines: List[str]):
    return get_max_happiness(lines, self=True)
