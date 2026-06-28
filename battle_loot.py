import random


def give_loot(player, monster):

    if monster["name"] == "Goblin":

        player.inventory["Herb"] = (

            player.inventory.get("Herb", 0) + 1

        )

    if random.randint(1, 100) <= 20:

        player.inventory["Iron Sword"] = (

            player.inventory.get("Iron Sword", 0) + 1

        )

        print("Dropped: Iron Sword")