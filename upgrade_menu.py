from upgrade_system import (
    upgrade_weapon
)


def upgrade_menu(player):

    while True:

        print(
            "\n===== UPGRADE ====="
        )

        print(
            "Weapon:",
            player.weapon,
            "+",
            player.weapon_level
        )

        print("1. Upgrade Weapon")
        print("2. Exit")

        choice = input(
            "Choice: "
        )

        if choice == "1":

            upgrade_weapon(
                player
            )

        elif choice == "2":

            break