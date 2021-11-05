import re
from typing import List


def next_gen(molecule, rules):
    molecules = set()
    for left, right in rules:
        i = 0
        while 0 <= i < len(molecule):
            index = molecule[i:].find(left)
            if index >= 0:
                replaced = molecule[i:].replace(left, right, 1)
                full = molecule[:i] + replaced
                molecules.add(full)
                i += index + 1
            else:
                i = index
    return molecules


def get_rules(lines):
    rules = []
    for line in lines:
        if found := re.match(r"(\w+) => (\w+)", line):
            left = found.group(1)
            right = found.group(2)
            rules.append((left, right))
    return rules


def part1(lines: List[str]):
    molecule = lines[-1]
    rules = get_rules(lines[:-1])
    molecules = next_gen(molecule, rules)
    return len(molecules)


def replace(molecule, compound):
    i = 0
    while compound in molecule:
        molecule = molecule.replace(compound, "X", 1)
        i += 1
    return i, molecule


def part2(lines: List[str]):
    molecule = lines[-1]
    left_paren = "Rn"
    comma = "Y"
    right_paren = "Ar"
    parens = (
        molecule.replace(left_paren, "(").replace(right_paren, ")").replace(comma, ",")
    )
    capital = "".join(ch for ch in parens if not ch.islower())
    all_x = "".join("X" if ch.isalpha() else ch for ch in capital)
    i = 0
    changed = True
    while changed:
        all_delta = 0
        for item in ("XX", "X(X)", "X(X,X)", "X(X,X,X)"):
            delta, all_x = replace(all_x, item)
            all_delta += delta
        i += all_delta
        if all_delta == 0:
            changed = False
    return i
