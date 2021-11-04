from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import product
import math
import re
from typing import List


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def get_score(self):
        all_values = (
            self.capacity,
            self.durability,
            self.flavor,
            self.texture,
            # self.calories,
        )
        if any(i <= 0 for i in all_values):
            return 0
        return math.prod(all_values)
    
    def __mul__(self, other):
        if other == 1:
            return self
        return Ingredient(
            name=self.name,
            capacity=other * self.capacity,
            durability=other * self.durability,
            flavor=other * self.flavor,
            texture=other * self.texture,
            calories=other * self.calories,
        )
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __add__(self, other):
        if other == 0:
            return self
        return Ingredient(
            name=self.name + "," + other.name,
            capacity=other.capacity + self.capacity,
            durability=other.durability + self.durability,
            flavor=other.flavor + self.flavor,
            texture=other.texture + self.texture,
            calories=other.calories + self.calories,
        )
    
    def __radd__(self, other):
        return self.__add__(other)

def get_ingredients(lines):
    ingredients = []
    for line in lines:
        if found := re.match(r"(\w+): \D+ (-?\d+)\D+ (-?\d+)\D+ (-?\d+)\D+ (-?\d+)\D+ (-?\d+)", line):
            name = found.group(1)
            capacity = int(found.group(2))
            durability = int(found.group(3))
            flavor = int(found.group(4))
            texture = int(found.group(5))
            calories = int(found.group(6))
            ingredients.append(Ingredient(
                name=name,
                capacity=capacity,
                durability=durability,
                flavor=flavor,
                texture=texture,
                calories=calories,
            ))
    return ingredients


def part1(lines: List[str]):
    ingredients = get_ingredients(lines)
    coefficients = [range(101) for _ in ingredients]
    max_score = 0
    for beta in product(*coefficients):
        if sum(beta) != 100:
            continue
        result = sum(b * i for b, i in zip(beta, ingredients))
        max_score = max(max_score, result.get_score())
    return max_score


def part2(lines: List[str]):
    ingredients = get_ingredients(lines)
    coefficients = [range(101) for _ in ingredients]
    max_score = 0
    for beta in product(*coefficients):
        if sum(beta) != 100:
            continue
        result = sum(b * i for b, i in zip(beta, ingredients))
        if result.calories != 500:
            continue
        max_score = max(max_score, result.get_score())
    return max_score
