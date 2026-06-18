def show_inventory(player):

    print("\n===== INVENTORY =====")

    for item, amount in player.inventory.items():

        print(item, "x", amount)


def use_potion(player):

    if player.inventory.get("Health Potion",0) > 0:

        player.inventory["Health Potion"] -= 1

        player.hp += 50

        if player.hp > player.max_hp:

            player.hp = player.max_hp

        print("\nRecovered 50 HP!")

    else:

        print("\nNo Potions Available!")