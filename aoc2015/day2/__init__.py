from typing import List


def part1(lines: List[str]):
    total_sq_ft = 0
    for line in lines:
        a, b, c = sorted(int(i) for i in line.split("x"))
        total_sq_ft += 3 * a * b + 2 * a * c + 2 * b * c
    return total_sq_ft


def part2(lines: List[str]):
    total_ft = 0
    for line in lines:
        a, b, c = sorted(int(i) for i in line.split("x"))
        total_ft += 2 * a + 2 * b + a * b * c
    return total_ft
