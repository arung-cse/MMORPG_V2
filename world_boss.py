from world_boss_data import WORLD_BOSSES
from battle import battle

def world_boss_menu(player):

    while True:

        print("\n===== WORLD BOSSES =====")

        for i, boss in enumerate(WORLD_BOSSES):

            print(
                f"{i+1}. {boss['name']}"
            )

        print("0. Exit")

        choice = input("Choice: ")

        if choice == "0":
            return

        try:

            boss = WORLD_BOSSES[
                int(choice)-1
            ].copy()

        except:

            print("Invalid Choice!")
            continue

        battle(player, boss)