import random


def monster_attack(player, monster):

    damage = random.randint(

        max(1, monster["attack"] - 2),

        monster["attack"] + 2

    )

    player.take_damage(damage)

    print(

        monster["name"],

        "dealt",

        damage,

        "damage!"

    )