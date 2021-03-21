from collections import Counter, defaultdict
from hashlib import md5
from typing import List

from ..utils import lines_to_int


def match_md5_zeroes(key, count=5):
    for i in range(10_000_000):
        this_md5 = md5(key)
        number = str(i).encode("utf-8")
        this_md5.update(number)
        digest = this_md5.hexdigest()
        if digest[slice(0, count)] == '0' * count:
            return i
    else:
        raise ValueError("Could not find a match")



def part1(lines: List[str]):
    key = lines[0].encode("utf-8")
    return match_md5_zeroes(key, count=5)



def part2(lines: List[str]):
    key = lines[0].encode("utf-8")
    return match_md5_zeroes(key, count=6)
