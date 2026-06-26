from upgrade_system import upgrade_weapon


def upgrade_menu(player):

    while True:

        print("\n===== UPGRADE SHOP =====")

        print(
            "Weapon :",
            player.weapon,
            "+" + str(player.weapon_upgrade)
        )

        print("\n1. Upgrade Weapon")
        print("2. Exit")

        choice = input("Choice: ")

        if choice == "1":

            upgrade_weapon(player)

        elif choice == "2":

            break

        else:

            print("Invalid Choice!")