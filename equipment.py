from equipment_data import EQUIPMENT


# ==========================================
# SHOW EQUIPMENT
# ==========================================

def show_equipment(player):

    print("\n========================")
    print("     EQUIPMENT")
    print("========================")

    print("Weapon     :", player.weapon)
    print("Armor      :", player.armor)
    print("Accessory  :", player.accessory)

    print("\nCurrent Stats")

    print("Attack   :", player.attack)
    print("Defense  :", player.defense)
    print("HP       :", player.hp, "/", player.max_hp)
    print("MP       :", player.mp, "/", player.max_mp)
    print("Critical :", str(player.critical) + "%")


# ==========================================
# EQUIP MENU
# ==========================================

def equip_menu(player):

    while True:

        print("\n========== EQUIP ==========")

        equip_list = []

        for item in player.inventory:

            if item in EQUIPMENT:

                equip_list.append(item)

        if len(equip_list) == 0:

            print("No equipment found.")

            return

        for i, item in enumerate(equip_list):

            data = EQUIPMENT[item]

            print(
                f"{i+1}. {item}"
            )

            print(
                "   Type   :",
                data["type"]
            )

            print(
                "   Rarity :",
                data["rarity"]
            )

            print(
                "   Level  :",
                data.get("level", 1)
            )

        print("0. Exit")

        choice = input("Choice: ")

        if choice == "0":

            return

        try:

            item = equip_list[
                int(choice)-1
            ]

            equip_item(
                player,
                item
            )

        except:

            print(
                "Invalid Choice!"
            )


# ==========================================
# EQUIP ITEM
# ==========================================

def equip_item(player, item_name):

    if item_name not in EQUIPMENT:

        print("Unknown Item!")

        return

    if item_name not in player.inventory:

        print("Item not in inventory!")

        return

    data = EQUIPMENT[item_name]

    if player.level < data.get("level", 1):

        print(
            "Need Level",
            data["level"]
        )

        return

    # Remove old equipment stats

    remove_stats(player)

    # Equip

    if data["type"] == "Weapon":

        player.weapon = item_name

    elif data["type"] == "Armor":

        player.armor = item_name

    elif data["type"] == "Accessory":

        player.accessory = item_name

    # Apply stats

    apply_stats(player)

    print(
        "\nEquipped:",
        item_name
    )


# ==========================================
# APPLY STATS
# ==========================================

def apply_stats(player):

    for item in [

        player.weapon,

        player.armor,

        player.accessory

    ]:

        if item == "None":

            continue

        data = EQUIPMENT[item]

        player.attack += data.get(
            "attack",
            0
        )

        player.defense += data.get(
            "defense",
            0
        )

        player.max_hp += data.get(
            "hp",
            0
        )

        player.max_mp += data.get(
            "mp",
            0
        )

        player.critical += data.get(
            "critical",
            0
        )


# ==========================================
# REMOVE STATS
# ==========================================

def remove_stats(player):

    for item in [

        player.weapon,

        player.armor,

        player.accessory

    ]:

        if item == "None":

            continue

        data = EQUIPMENT[item]

        player.attack -= data.get(
            "attack",
            0
        )

        player.defense -= data.get(
            "defense",
            0
        )

        player.max_hp -= data.get(
            "hp",
            0
        )

        player.max_mp -= data.get(
            "mp",
            0
        )

        player.critical -= data.get(
            "critical",
            0
        )