from typing import List


def part1(lines: List[str]):
    char_count = 0
    symbol_count = 0
    for line in lines:
        char_count += len(line)
        subline = line[1:-1]
        it = iter(subline)
        result = ""
        try:
            while ch := next(it):
                if ch == "\\":
                    next_ch = next(it)
                    if next_ch != "x":
                        result += next_ch
                    else:
                        code = ''.join((next(it), next(it)))
                        result += "X"
                else:
                    result += ch
        except StopIteration:
            pass
        symbol_count += len(result)
    return char_count - symbol_count


def part2(lines: List[str]):
    char_count = 0
    escaped_count = 0
    for line in lines:
        char_count += len(line)
        for ch in line:
            if ch == "\\":
                escaped_count += 2
            elif ch == "\"":
                escaped_count += 2
            else:
                escaped_count += 1
        escaped_count += 2
    return escaped_count - char_count
