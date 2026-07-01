from equipment_data import (
    WEAPONS,
    ARMORS,
    ACCESSORIES
)

from set_system import check_set_bonus


# ==========================================
# COMBINE ALL EQUIPMENT
# ==========================================

EQUIPMENT = {}

EQUIPMENT.update(WEAPONS)
EQUIPMENT.update(ARMORS)
EQUIPMENT.update(ACCESSORIES)


# ==========================================
# SHOW EQUIPMENT
# ==========================================

def show_equipment(player):

    print("\n========================")
    print("      EQUIPMENT")
    print("========================")

    print("Weapon     :", player.weapon)

    if player.weapon != "None":

        print(
            "Element    :",
            EQUIPMENT[player.weapon].get(
                "element",
                "None"
            )
        )

    print("Armor      :", player.armor)

    print("Accessory  :", player.accessory)

    print("\n========== STATS ==========")

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

        print("\n========== EQUIPMENT ==========")

        equip_list = []

        for item in player.inventory:

            if item in EQUIPMENT:

                equip_list.append(item)

        if len(equip_list) == 0:

            print("\nNo Equipment Found!")

            return

        for i, item in enumerate(equip_list):

            data = EQUIPMENT[item]

            print(
                f"\n{i+1}. {item}"
            )

            print(
                "   Type      :",
                data["type"]
            )

            print(
                "   Rarity    :",
                data["rarity"]
            )

            print(
                "   Level     :",
                data.get(
                    "level",
                    1
                )
            )

            print(
                "   Attack    :",
                data.get(
                    "attack",
                    0
                )
            )

            print(
                "   Defense   :",
                data.get(
                    "defense",
                    0
                )
            )

            print(
                "   HP        :",
                data.get(
                    "hp",
                    0
                )
            )

            print(
                "   Critical  :",
                data.get(
                    "critical",
                    0
                )
            )

            print(
                "   Element   :",
                data.get(
                    "element",
                    "None"
                )
            )

        print("\n0. Exit")

        choice = input("\nChoice: ")

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

            print("\nInvalid Choice!")


# ==========================================
# EQUIP ITEM
# ==========================================

def equip_item(player, item_name):

    if item_name not in EQUIPMENT:

        print("\nUnknown Equipment!")

        return

    if item_name not in player.inventory:

        print("\nItem not found!")

        return

    data = EQUIPMENT[item_name]

    if player.level < data.get(
        "level",
        1
    ):

        print(
            "\nRequired Level:",
            data["level"]
        )

        return

    remove_stats(player)

    if data["type"] == "Weapon":

        player.weapon = item_name

    elif data["type"] == "Armor":

        player.armor = item_name

    elif data["type"] == "Accessory":

        player.accessory = item_name

    apply_stats(player)

    apply_set_bonus(player)

    print(
        "\nEquipped:",
        item_name
    )


# ==========================================
# APPLY EQUIPMENT STATS
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

    player.hp = player.max_hp
    player.mp = player.max_mp


# ==========================================
# REMOVE EQUIPMENT STATS
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

    if player.hp > player.max_hp:

        player.hp = player.max_hp

    if player.mp > player.max_mp:

        player.mp = player.max_mp


# ==========================================
# APPLY SET BONUS
# ==========================================

def apply_set_bonus(player):

    bonus = check_set_bonus(player)

    if not bonus:

        return

    player.attack += bonus.get(
        "attack",
        0
    )

    player.defense += bonus.get(
        "defense",
        0
    )

    player.max_hp += bonus.get(
        "hp",
        0
    )

    player.critical += bonus.get(
        "critical",
        0
    )

    player.hp = player.max_hp

    print("\n★★★★★ SET BONUS ACTIVATED ★★★★★")