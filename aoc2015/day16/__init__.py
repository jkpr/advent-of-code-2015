import re
from typing import List


SUE = dict(
    children=3,
    cats=7,
    samoyeds=2,
    pomeranians=3,
    akitas=0,
    vizslas=0,
    goldfish=5,
    trees=3,
    cars=2,
    perfumes=1,
)


def get_my_sue_list(lines):
    sue_list = []
    for line in lines:
        if found := re.match(
            r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line
        ):
            num = int(found.group(1))
            obj1 = found.group(2)
            obj1_count = int(found.group(3))
            obj2 = found.group(4)
            obj2_count = int(found.group(5))
            obj3 = found.group(6)
            obj3_count = int(found.group(7))
            sue_list.append(
                {
                    obj1: obj1_count,
                    obj2: obj2_count,
                    obj3: obj3_count,
                }
            )
        else:
            raise Exception("Improper Sue")
    return sue_list


def part1(lines: List[str]):
    sue_list = get_my_sue_list(lines)
    for i, sue in enumerate(sue_list, start=1):
        if all(SUE[key] == value for key, value in sue.items()):
            return i


def compare(sue, detected_sue):
    good_match = True
    for key, value in sue.items():
        if key in ("cats", "trees"):
            if not value > detected_sue[key]:
                good_match = False
        elif key in ("pomeranians", "goldfish"):
            if not value < detected_sue[key]:
                good_match = False
        else:
            if value != detected_sue[key]:
                good_match = False
    return good_match


def part2(lines: List[str]):
    sue_list = get_my_sue_list(lines)
    for i, sue in enumerate(sue_list, start=1):
        if compare(sue, SUE):
            return i
