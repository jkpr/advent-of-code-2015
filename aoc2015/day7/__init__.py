import functools
import re
from typing import List


MAX_INT = 0xFFFF


def create_value_func(rules):
    @functools.cache
    def get_value(key: str):
        if key.isdigit():
            return int(key)
        value = rules[key]
        if value.isdigit():
            return int(value)
        if found := re.fullmatch(r"([a-z]+)", value):
            return get_value(found.group(1))
        if found := re.fullmatch(r"NOT (\w+)", value):
            arg1 = get_value(found.group(1))
            return MAX_INT - arg1
        if found := re.fullmatch(r"(\w+) AND (\w+)", value):
            arg1 = get_value(found.group(1))
            arg2 = get_value(found.group(2))
            return arg1 & arg2
        if found := re.fullmatch(r"(\w+) OR (\w+)", value):
            arg1 = get_value(found.group(1))
            arg2 = get_value(found.group(2))
            return arg1 | arg2
        if found := re.fullmatch(r"(\w+) RSHIFT (\d+)", value):
            arg1 = get_value(found.group(1))
            arg2 = int(found.group(2))
            return arg1 >> arg2
        if found := re.fullmatch(r"(\w+) LSHIFT (\d+)", value):
            arg1 = get_value(found.group(1))
            arg2 = int(found.group(2))
            return (arg1 << arg2) & MAX_INT
        raise NotImplementedError(value)

    return get_value


def part1(lines: List[str]):
    matched_groups = [re.match("(.*) -> (.*)", line).groups() for line in lines]
    rules = dict(reversed(match) for match in matched_groups)
    get_value = create_value_func(rules)
    return get_value("a")


def part2(lines: List[str]):
    matched_groups = [re.match("(.*) -> (.*)", line).groups() for line in lines]
    rules = dict(reversed(match) for match in matched_groups)
    part1_result = part1(lines)
    rules["b"] = str(part1_result)
    get_value = create_value_func(rules)
    return get_value("a")
