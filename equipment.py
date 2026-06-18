def show_equipment(player):

    print("\n===== EQUIPMENT =====")

    print("Weapon:",
          player.weapon)

    print("Armor:",
          player.armor)


def equip_item(player, item):

    if item == "Iron Sword":

        player.weapon = item

        player.attack += 10

        print("\nIron Sword Equipped!")

    elif item == "Steel Sword":

        player.weapon = item

        player.attack += 20

        print("\nSteel Sword Equipped!")

    elif item == "Leather Armor":

        player.armor = item

        player.max_hp += 50

        player.hp += 50

        print("\nLeather Armor Equipped!")