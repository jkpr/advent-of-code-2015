from collections import defaultdict
from typing import List


def part1(lines: List[str]):
    goal = int(lines[0])
    houses = defaultdict(int)
    house_limit = 1_000_000
    for i in range(1, house_limit + 1):
        for j in range(1, house_limit + 1):
            if i * j <= house_limit:
                houses[i * j] += i * 10
            else:
                break
        if houses[i] > goal:
            return i


def part2(lines: List[str]):
    goal = int(lines[0])
    houses = defaultdict(int)
    house_limit = 10_000_000
    for i in range(1, house_limit + 1):
        for j in range(1, 50 + 1):
            if i * j <= house_limit:
                houses[i * j] += i * 11
            else:
                break
        if houses[i] > goal:
            return i
    for i in range(1000):
        print(i, houses[i])
