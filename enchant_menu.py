from enchant_system import enchant_weapon


def enchant_menu(player):

    while True:

        print("\n===== ENCHANT =====")

        print(

            "Weapon :",

            player.weapon

        )

        print(

            "Enchant :",

            player.weapon_enchant

        )

        print()

        print("1. Enchant Weapon")

        print("2. Exit")

        choice = input("Choice: ")

        if choice == "1":

            enchant_weapon(player)

        elif choice == "2":

            break

        else:

            print("Invalid Choice!")