from shop_data import SHOP_ITEMS


def show_shop():

    print("\n===== SHOP =====")

    count = 1

    for item, data in SHOP_ITEMS.items():

        print(
            str(count) + ".",
            item,
            "-",
            data["price"],
            "Gold"
        )

        count += 1

    print("0. Exit")


def buy_item(player):

    while True:

        show_shop()

        choice = input("\nBuy Item: ")

        if choice == "0":

            return

        items = list(SHOP_ITEMS.keys())

        try:

            item_name = items[
                int(choice) - 1
            ]

        except:

            print("Invalid Choice!")
            continue

        item_price = SHOP_ITEMS[
            item_name
        ]["price"]

        if player.gold < item_price:

            print(
                "\nNot enough Gold!"
            )

            continue

        player.gold -= item_price

        player.inventory[item_name] = (
            player.inventory.get(
                item_name,
                0
            ) + 1
        )

        print(
            "\nBought",
            item_name
        )


def sell_item(player):

    print("\n===== SELL =====")

    inventory_items = list(
        player.inventory.keys()
    )

    if len(inventory_items) == 0:

        print("Inventory Empty!")

        return

    for i, item in enumerate(
        inventory_items,
        start=1
    ):

        print(
            str(i) + ".",
            item,
            "x",
            player.inventory[item]
        )

    print("0. Exit")

    choice = input(
        "\nSell Item: "
    )

    if choice == "0":

        return

    try:

        item_name = inventory_items[
            int(choice) - 1
        ]

    except:

        print("Invalid Choice!")

        return

    player.inventory[item_name] -= 1

    if player.inventory[item_name] <= 0:

        del player.inventory[item_name]

    sell_price = 10

    if item_name in SHOP_ITEMS:

        sell_price = (
            SHOP_ITEMS[item_name]["price"]
            // 2
        )

    player.gold += sell_price

    print(
        "\nSold",
        item_name,
        "for",
        sell_price,
        "Gold"
    )