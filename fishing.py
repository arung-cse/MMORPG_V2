import random

from fishing_data import FISHES


def fish(player):

    print("\n===== FISHING =====")

    fish_list = list(
        FISHES.keys()
    )

    caught = random.choice(
        fish_list
    )

    player.inventory[caught] = (
        player.inventory.get(
            caught,
            0
        ) + 1
    )

    print(
        "\nYou caught:",
        caught
    )