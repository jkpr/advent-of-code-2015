from collections import defaultdict
from itertools import product
import re
from typing import List


def get_op_part1(line):
    if "on" in line:
        return lambda x: True
    elif "off" in line:
        return lambda x: False
    else:
        return lambda x: not x


def get_op_part2(line):
    if "on" in line:
        return lambda x: x + 1
    elif "off" in line:
        return lambda x: max(x - 1, 0)
    else:
        return lambda x: x + 2


def get_op(line, part2):
    if part2:
        return get_op_part2(line)
    return get_op_part1(line)


def run_santa_instruction(grid, line, part2):
    coords = [int(i) for i in re.findall(r"\d+", line)]
    tl_x, tl_y, br_x, br_y = coords
    range_x = range(tl_x, br_x + 1)
    range_y = range(tl_y, br_y + 1)
    op = get_op(line, part2)
    for coord in product(range_x, range_y):
        grid[coord] = op(grid[coord])


def part1(lines: List[str]):
    grid = defaultdict(bool)
    for line in lines:
        run_santa_instruction(grid, line, part2=False)
    return len([k for k in grid if grid[k]])


def part2(lines: List[str]):
    grid = defaultdict(int)
    for line in lines:
        run_santa_instruction(grid, line, part2=True)
    return sum(grid.values())
