import random
from loot_data import LOOT_TABLE


def give_loot(player, monster_name):

    if monster_name not in LOOT_TABLE:

        return

    loot = LOOT_TABLE[monster_name]

    gold = random.randint(
        loot["gold"][0],
        loot["gold"][1]
    )

    player.gold += gold

    print("+", gold, "Gold")

    for item, chance in loot["drops"]:

        roll = random.randint(1,100)

        if roll <= chance:

            player.inventory[item] = (
                player.inventory.get(
                    item,
                    0
                ) + 1
            )

            print(
                "Dropped:",
                item
            )