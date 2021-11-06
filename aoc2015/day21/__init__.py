from dataclasses import dataclass
from itertools import chain, combinations, product
from typing import List


@dataclass
class Person:
    name: str
    hit_points: int
    damage: int
    armor: int

    def attack(self, other) -> None:
        other.take_damage(self.damage)

    def take_damage(self, amount: int) -> None:
        damage = max(1, amount - self.armor)
        self.hit_points = max(0, self.hit_points - damage)

    def is_dead(self) -> bool:
        return self.hit_points == 0


def test():
    boss = Person(
        name="Boss",
        hit_points=12,
        damage=7,
        armor=2,
    )
    you = Person(
        name="You",
        hit_points=8,
        damage=5,
        armor=5,
    )
    battle(you, boss)


def battle(you: Person, boss: Person):
    max_hp = max(you.hit_points, boss.hit_points)
    for _ in range(max_hp):
        you.attack(boss)
        if boss.is_dead():
            break
        boss.attack(you)
        if you.is_dead():
            break
    you_won = True
    if you.is_dead():
        you_won = False
    return you_won


def pay_for_gear(defense, attack):
    weapons = [
        (8, 4),
        (10, 5),
        (25, 6),
        (40, 7),
        (74, 8),
    ]
    armors = [
        (13, 1),
        (31, 2),
        (53, 3),
        (75, 4),
        (102, 5),
    ]
    damage_rings = [
        (25, 1),
        (50, 2),
        (100, 3),
    ]
    armor_rings = [
        (20, 1),
        (40, 2),
        (80, 3),
    ]
    offense_kits = []
    for weapon in weapons:
        if weapon[1] < attack:
            for rings in chain(combinations(damage_rings, 1), combinations(damage_rings, 2)):
                ring_damage = sum(i[1] for i in rings)
                if ring_damage == attack - weapon[1]:
                    offense_kits.append({
                        "weapon": weapon,
                        "rings": rings,
                    })
        elif weapon[1] == attack:
            offense_kits.append({
                "weapon": weapon,
                "rings": [],
            })
    defense_kits = []
    if defense == 0:
        defense_kits.append({
            "armor": (0, 0),
            "rings": [],
        })
    for rings in chain(combinations(armor_rings, 1), combinations(armor_rings, 2)):
        ring_armor = sum(i[1] for i in rings)
        if ring_armor == defense:
            defense_kits.append({
                "armor": (0, 0),
                "rings": rings,
            })
    for armor in armors:
        if armor[1] < defense:
            for rings in chain(combinations(armor_rings, 1), combinations(armor_rings, 2)):
                ring_armor = sum(i[1] for i in rings)
                if ring_armor == defense - armor[1]:
                    defense_kits.append({
                        "armor": armor,
                        "rings": rings,
                    })
        if armor[1] == defense:
            defense_kits.append({
                "armor": armor,
                "rings": [],
            })
    prices = []
    for o_kit, d_kit in product(offense_kits, defense_kits):
        if len(o_kit["rings"]) + len(d_kit["rings"]) > 2:
            continue
        price = o_kit["weapon"][0] + d_kit["armor"][0]
        price += sum(i[0] for i in o_kit["rings"])
        price += sum(i[0] for i in d_kit["rings"])
        prices.append(price)
    return prices



def part1(lines: List[str]):
    winning_combos = []
    prices = []
    for armor in range(11):
        for damage in range(4, 13):
            boss = Person(
                name="Boss",
                hit_points=103,
                damage=9,
                armor=2,
            )
            you = Person(
                name="You",
                hit_points=100,
                damage=damage,
                armor=armor,
            )
            you_won = battle(you, boss)
            if you_won:
                winning_combos.append((armor, damage))
                prices.append(min(pay_for_gear(armor, damage)))
                break
    print(winning_combos)
    print(prices)
    return min(prices)


def part2(lines: List[str]):
    losing_combos = []
    prices = []
    for armor in range(11):
        for damage in range(4, 14):
            boss = Person(
                name="Boss",
                hit_points=103,
                damage=9,
                armor=2,
            )
            you = Person(
                name="You",
                hit_points=100,
                damage=damage,
                armor=armor,
            )
            you_won = battle(you, boss)
            if not you_won:
                losing_combos.append((armor, damage))
                prices.append(max(pay_for_gear(armor, damage)))
    print(losing_combos)
    print(prices)
    return max(prices)
