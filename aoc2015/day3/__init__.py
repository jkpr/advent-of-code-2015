from collections import Counter, defaultdict
from typing import List

from ..utils import lines_to_int


def move(current, direction):
    new = current
    if direction == "^":
        new = (current[0], current[1] + 1)
    elif direction == "v":
        new = (current[0], current[1] - 1)
    elif direction == "<":
        new = (current[0] - 1, current[1])
    elif direction == ">":
        new = (current[0] + 1, current[1])
    return new


def part1(lines: List[str]):
    presents = defaultdict(int)
    current = (0, 0)
    presents[current] += 1
    directions = lines[0]
    for direction in directions:
        current = move(current, direction)
        presents[current] += 1
    return len(presents)


def part2(lines: List[str]):
    presents = defaultdict(int)
    santa = (0, 0)
    robot = (0, 0)
    presents[santa] += 1
    directions = lines[0]
    for i, direction in enumerate(directions):
        if i % 2 == 0:
            santa = move(santa, direction)
            presents[santa] += 1
        else:
            robot = move(robot, direction)
            presents[robot] += 1
    return len(presents)