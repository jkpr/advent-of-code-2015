import re
from typing import List


def part1(lines: List[str]):
    total = 0
    for line in lines:
        if found := re.findall(r"-?\d+", line):
            total += sum(int(i) for i in found)
    return total


def find_next_closing_brace(line, pos):
    found = 1
    for i, ch in enumerate(line[pos:], start=pos):
        if ch == "{":
            found += 1
        elif ch == "}":
            found -= 1
        if found == 0:
            return i
    raise Exception("No } found")


def part2(lines: List[str]):
    line = lines[0]
    stack = []
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "{":
            stack.append(i)
        elif ch == "}":
            stack.pop()
        if ch == ":" and stack and line[i:(i+6)] == ':"red"':
            first = stack[-1]
            closer = find_next_closing_brace(line, i)
            line = line[:first] + line[(closer+1):]
            i = 0
            stack.clear()
        else:
            i += 1
    return part1([line])
