from auction_system import (
    list_item,
    browse_auction
)


def auction_menu(player):

    while True:

        print(
            "\n===== AUCTION HOUSE ====="
        )

        print("1. Browse")
        print("2. Sell Item")
        print("3. Exit")

        choice = input(
            "Choice: "
        )

        if choice == "1":

            browse_auction(
                player
            )

        elif choice == "2":

            list_item(
                player
            )

        elif choice == "3":

            break