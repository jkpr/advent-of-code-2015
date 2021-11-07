from collections import namedtuple
from functools import cache
from typing import List

Game = namedtuple(
    "Game",
    [
        "player_hp",
        "player_armor",
        "player_mana",
        "boss_hp",
        "boss_damage",
        "shield_counter",
        "poison_counter",
        "recharge_counter",
        "player_turn",
        "hard_rules",
    ],
)


def pre_turn_counters(game: Game) -> Game:
    if game.shield_counter > 0:
        game = game._replace(
            shield_counter=game.shield_counter - 1,
        )
        if game.shield_counter == 0:
            game = game._replace(
                player_armor=0,
            )
    if game.poison_counter > 0:
        game = game._replace(
            boss_hp=game.boss_hp - 3,
            poison_counter=game.poison_counter - 1,
        )
    if game.recharge_counter > 0:
        game = game._replace(
            player_mana=game.player_mana + 101,
            recharge_counter=game.recharge_counter - 1,
        )
    return game


MANA_MAGIC_MISSILE = 53


def magic_missile(game: Game) -> Game:
    return game._replace(
        player_mana=game.player_mana - MANA_MAGIC_MISSILE,
        boss_hp=game.boss_hp - 4,
    )


MANA_DRAIN = 73


def drain(game: Game) -> Game:
    return game._replace(
        player_mana=game.player_mana - MANA_DRAIN,
        player_hp=game.player_hp + 2,
        boss_hp=game.boss_hp - 2,
    )


MANA_SHIELD = 113


def shield(game: Game) -> Game:
    return game._replace(
        player_mana=game.player_mana - MANA_SHIELD,
        player_armor=7,
        shield_counter=6,
    )


MANA_POISON = 173


def poison(game: Game) -> Game:
    return game._replace(
        player_mana=game.player_mana - MANA_POISON,
        poison_counter=6,
    )


MANA_RECHARGE = 229


def recharge(game: Game) -> Game:
    return game._replace(
        player_mana=game.player_mana - MANA_RECHARGE,
        recharge_counter=5,
    )


def boss_attack(game: Game) -> Game:
    damage = max(game.boss_damage - game.player_armor, 1)
    return game._replace(player_hp=game.player_hp - damage)


def change_turn(game: Game) -> Game:
    return game._replace(player_turn=not game.player_turn)


def game_over(game: Game) -> bool:
    return game.boss_hp <= 0 or game.player_hp <= 0


def player_wins(game: Game) -> bool:
    return game.boss_hp <= 0


def hard_rules_damage(game: Game) -> Game:
    return game._replace(player_hp=game.player_hp - 1)


@cache
def get_best(game: Game) -> int:
    if game_over(game) and player_wins(game):
        return 0
    elif game_over(game) and not player_wins(game):
        return -1
    game = change_turn(game)
    if game.hard_rules and game.player_turn:
        game = hard_rules_damage(game)
        if game_over(game):
            return -1
    game = pre_turn_counters(game)
    if game_over(game):  # player wins
        return 0
    if game.player_turn:
        options = []
        if game.player_mana > MANA_MAGIC_MISSILE:
            options.append((get_best(magic_missile(game)), MANA_MAGIC_MISSILE))
        if game.player_mana > MANA_DRAIN:
            options.append((get_best(drain(game)), MANA_DRAIN))
        if game.player_mana > MANA_SHIELD and game.shield_counter == 0:
            options.append((get_best(shield(game)), MANA_SHIELD))
        if game.player_mana > MANA_POISON and game.poison_counter == 0:
            options.append((get_best(poison(game)), MANA_POISON))
        if game.player_mana > MANA_RECHARGE and game.recharge_counter == 0:
            options.append((get_best(recharge(game)), MANA_RECHARGE))
        if not options:
            return -1
        elif all(i[0] == -1 for i in options):
            return -1
        else:
            return min(sum(i) for i in options if i[0] >= 0)
    else:
        return get_best(boss_attack(game))


def test():
    game = Game(10, 0, 250, 13, 8, 0, 0, 0, False)
    print(game)
    game = change_turn(game)
    print(game)
    game = pre_turn_counters(game)
    print(game)
    game = poison(game)
    print(game)
    game = change_turn(game)
    print(game)
    game = pre_turn_counters(game)
    print(game)
    game = boss_attack(game)
    print(game)
    game = change_turn(game)
    print(game)
    game = pre_turn_counters(game)
    print(game)
    game = magic_missile(game)
    print(game)
    game = change_turn(game)
    print(game)
    game = pre_turn_counters(game)
    print(game)
    assert game_over(game) and player_wins(game)


def part1(lines: List[str]):
    game = Game(50, 0, 500, 51, 9, 0, 0, 0, False, False)
    return get_best(game)


def part2(lines: List[str]):
    game = Game(50, 0, 500, 51, 9, 0, 0, 0, False, True)
    return get_best(game)
