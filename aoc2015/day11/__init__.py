from typing import List


def has_straight(word: str) -> bool:
    return any(
        ord(i) == ord(j) - 1 == ord(k) - 2 for i, j, k in zip(word, word[1:], word[2:])
    )


def no_i_o_l(word: str) -> bool:
    return "i" not in word and "o" not in word and "l" not in word


def overlapping_pairs(word: str) -> bool:
    found = set()
    for a, b in zip(word, word[1:]):
        if a == b:
            found.add(a)
    return len(found) >= 2


def is_valid_password(word: str) -> bool:
    return all(
        (
            no_i_o_l(word),
            has_straight(word),
            overlapping_pairs(word),
        )
    )


def get_next_non_i_o_l(word: str) -> str:
    new = []
    for ch in word:
        if ch == "i":
            new.append("j")
            break
        if ch == "o":
            new.append("p")
            break
        if ch == "l":
            new.append("m")
            break
        new.append(ch)
    while len(new) < len(word):
        new.append("a")
    return "".join(new)


def get_next(word: str) -> str:
    digits = [ord(ch) - ord("a") for ch in reversed(word)]
    num = sum((26 ** i) * digit for i, digit in enumerate(digits))
    if num == sum((26 ** i) * 25 for i in range(len(word))):
        num = 0
    else:
        num += 1
    new_digits = []
    for _ in range(len(word)):
        next_digit = num % 26
        new_digits.append(next_digit)
        num //= 26
    new_letters = [chr(i + ord("a")) for i in new_digits]
    return "".join(reversed(new_letters))


def part1(lines: List[str]):
    line = lines[0]
    for _ in range(1_000_000):
        if is_valid_password(line):
            return line
        if "i" in line or "o" in line or "l" in line:
            line = get_next_non_i_o_l(line)
        else:
            line = get_next(line)


def part2(lines: List[str]):
    line = part1(lines)
    line = get_next(line)
    for _ in range(1_000_000):
        if is_valid_password(line):
            return line
        if "i" in line or "o" in line or "l" in line:
            line = get_next_non_i_o_l(line)
        else:
            line = get_next(line)
