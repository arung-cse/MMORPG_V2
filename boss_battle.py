from boss_data import BOSSES
from battle import battle


def boss_menu(player):

    while True:

        print("\n========== BOSS RAID ==========")

        for i, boss in enumerate(BOSSES):

            print(
                f"{i+1}. {boss['name']}  (Lv.{boss['level']})"
            )

        print("0. Back")

        choice = input("Choice: ")

        if choice == "0":

            return

        try:

            boss = BOSSES[int(choice)-1].copy()

        except:

            print("Invalid Choice!")

            continue

        if player.level < boss["level"]:

            print(
                f"\nRequired Level : {boss['level']}"
            )

            continue

        print("\n==============================")
        print("Boss :", boss["name"])
        print("Element :", boss["element"])
        print("HP :", boss["hp"])
        print("Attack :", boss["attack"])
        print("==============================")

        start = input(
            "\nStart Battle? (y/n): "
        ).lower()

        if start != "y":

            continue

        battle(
            player,
            boss
        )