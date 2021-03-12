from collections import Counter
from typing import List


def part1(lines: List[str]):
    instructions = lines[0]
    counter = Counter(instructions)
    return counter.get("(") - counter.get(")")


def part2(lines: List[str]):
    location = 0
    instructions = lines[0]
    for i, item in enumerate(instructions, start=1):
        if item == "(":
            location += 1
        else:
            location -= 1
        if location < 0:
            return i
    raise ValueError("Never went negative!")
