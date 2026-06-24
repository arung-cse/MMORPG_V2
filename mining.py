import random

from mining_data import ORES

def mine(player):

    print("\n===== MINING =====")

    roll = random.randint(1, 100)

    total = 0

    for ore, data in ORES.items():

        total += data["chance"]

        if roll <= total:

            player.inventory[ore] = (
                player.inventory.get(
                    ore,
                    0
                ) + 1
            )

            print(
                "\nYou mined:",
                ore
            )

            return