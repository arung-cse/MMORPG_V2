from title_system import (
    equip_title,
    show_title
)


def title_menu(player):

    while True:

        print(
            "\n===== TITLE MENU ====="
        )

        print("1. View Title")
        print("2. Equip Title")
        print("3. Exit")

        choice = input(
            "Choice: "
        )

        if choice == "1":

            show_title(
                player
            )

        elif choice == "2":

            equip_title(
                player
            )

        elif choice == "3":

            break