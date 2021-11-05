from collections import Counter, defaultdict
from itertools import product
from typing import List

from ..utils import lines_to_int


def get_from_text(lines):
    grid = defaultdict(int)
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == "#":
                grid[(x, y)] = 1
    return grid


def get_next_grid(grid, length=100, sticky_corners=True):
    new = defaultdict(int)
    for i, j in product(range(length), range(length)):
        if sticky_corners and (i, j) in [(0, 0), (0, length-1), (length-1, 0), (length-1, length-1)]:
            new[(i, j)] = 1
            continue
        curr = grid[(i, j)]
        on = 0
        for diff in product([-1, 0, 1], [-1, 0, 1]):
            if diff == (0, 0):
                continue
            x = i + diff[0]
            y = j + diff[1]
            on += grid[(x, y)]
        if curr == 1 and on in (2, 3):
            new[(i, j)] = 1
        elif curr == 0 and on == 3:
            new[(i, j)] = 1
    return new


def print_grid(grid, length=100):
    for i in range(length):
        for j in range(length):
            if grid[(j, i)] == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def part1(lines: List[str]):
    grid = get_from_text(lines)
    for _ in range(100):
        grid = get_next_grid(grid)
    return sum(grid.values())


def part2(lines: List[str]):
    grid = get_from_text(lines)
    for _ in range(100):
        grid = get_next_grid(grid, sticky_corners=True)
    return sum(grid.values())
