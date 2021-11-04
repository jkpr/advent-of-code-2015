from collections import Counter, defaultdict, namedtuple
from dataclasses import dataclass
import re
from typing import List

import numpy as np
import pandas as pd


@dataclass
class Reindeer:
    name: str
    speed: int
    move: int
    rest: int

    def get_distance(self, time):
        intervals, remainder = divmod(time, self.move + self.rest)
        return intervals * self.speed * self.move + self.speed * min(self.move, remainder)

def parse_names_speeds(lines):
    reindeer = []
    for line in lines:
        if found := re.match(r"(\w+)\D+(\d+)\D+(\d+)\D+(\d+)", line):
            name = found.group(1)
            speed = int(found.group(2))
            move = int(found.group(3))
            rest = int(found.group(4))
            reindeer.append(Reindeer(
                name=name,
                speed=speed,
                move=move,
                rest=rest,
            ))
    return reindeer


def part1(lines: List[str]):
    reindeer = parse_names_speeds(lines)
    return max(deer.get_distance(2503) for deer in reindeer)


def part2(lines: List[str]):
    reindeer = parse_names_speeds(lines)
    time = 2503
    for i in range(1, time + 1):
        winner_dist = max(deer.get_distance(i) for deer in reindeer)
    series = np.arange(stop=time) + 1
    deer_distances = {}
    for deer in reindeer:
        distances = [deer.get_distance(i) for i in series]
        deer_distances[deer.name] = distances
    df = pd.DataFrame(deer_distances)
    lead = df.max(axis=1)
    winners = df.apply(lambda x: x == lead)
    return winners.sum().max()
