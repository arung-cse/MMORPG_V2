import random

from upgrade_data import UPGRADE_COST


def upgrade_weapon(player):

    if player.weapon == "None":

        print("\nNo Weapon Equipped!")

        return

    next_level = (
        player.weapon_level + 1
    )

    if next_level > 15:

        print("\nMax Upgrade!")

        return

    cost = UPGRADE_COST[
        next_level
    ]

    if player.gold < cost:

        print(
            "\nNot Enough Gold!"
        )

        return

    player.gold -= cost

    success_rate = max(
        100 - (next_level * 5),
        20
    )

    roll = random.randint(
        1,
        100
    )

    if roll <= success_rate:

        player.weapon_level += 1

        player.attack += 10

        print(
            "\nSUCCESS!"
        )

        print(
            player.weapon,
            "+",
            player.weapon_level
        )

    else:

        print(
            "\nUpgrade Failed!"
        )