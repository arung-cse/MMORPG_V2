from crafting import craft_item
from mining import mine


def blacksmith_menu(player):

    while True:

        print("\n===== BLACKSMITH =====")

        print("1. Mine Ore")
        print("2. Craft Item")
        print("3. Leave")

        choice = input(
            "Choice: "
        )

        if choice == "1":

            mine(player)

        elif choice == "2":

            craft_item(player)

        elif choice == "3":

            break