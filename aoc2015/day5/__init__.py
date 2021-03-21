from collections import Counter, defaultdict
from typing import List


def is_nice(line):
    counter = Counter(line)
    vowel_count = (
        counter["a"] + counter["e"] + counter["i"] + counter["o"] + counter["u"]
    )
    if vowel_count < 3:
        return False
    for a, b in zip(line, line[1:]):
        if a == b:
            break
    else:
        return False
    bad_contain = any(i in line for i in ("ab", "cd", "pq", "xy"))
    if bad_contain:
        return False
    return True


def is_nice_part2(line):
    found = defaultdict(set)
    for i in range(len(line) - 1):
        pair = line[i : (i + 2)]
        if any(abs(i - j) >= 2 for j in found[pair]):
            break
        found[pair].add(i)
    else:
        return False
    for a, b in zip(line, line[2:]):
        if a == b:
            break
    else:
        return False
    return True


def part1(lines: List[str]):
    return len([i for i in lines if is_nice(i)])


def part2(lines: List[str]):
    return len([i for i in lines if is_nice_part2(i)])
