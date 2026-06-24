from guild_system import (
    create_guild,
    show_guild
)


def guild_menu(player):

    while True:

        print(
            "\n===== GUILD ====="
        )

        print(
            "1. Create Guild"
        )

        print(
            "2. View Guild"
        )

        print(
            "3. Exit"
        )

        choice = input(
            "Choice: "
        )

        if choice == "1":

            create_guild(
                player
            )

        elif choice == "2":

            show_guild(
                player
            )

        elif choice == "3":

            break