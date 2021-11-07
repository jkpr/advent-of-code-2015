from typing import List


def row_col_to_n(row, col):
    return (col + row - 1) * (col + row) // 2 - (row - 1)


def get_next(num):
    return (num * 252533) % 33554393


def part1(lines: List[str]):
    num = 20151125
    n = row_col_to_n(2978, 3083)
    for _ in range(n - 1):
        num = get_next(num)
    return num


def part2(lines: List[str]):
    pass
