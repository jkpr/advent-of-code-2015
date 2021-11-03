from itertools import groupby
from typing import List


def next_num(num: str):
    digits = []
    for k, g in groupby(num):
        digits.append(len(list(g)))
        digits.append(k)
    return ''.join(str(d) for d in digits)


def part1(lines: List[str]):
    line = lines[0]
    for _ in range(40):
        line = next_num(line)
    return len(line)


def part2(lines: List[str]):
    line = lines[0]
    for _ in range(50):
        line = next_num(line)
    return len(line)
