from auction_data import AUCTIONS


def list_item(player):

    print("\n===== SELL ITEM =====")

    for item, amount in player.inventory.items():

        print(
            item,
            "x",
            amount
        )

    item_name = input(
        "\nItem Name: "
    )

    if item_name not in player.inventory:

        print("Item Not Found!")
        return

    price = int(
        input("Price: ")
    )

    AUCTIONS.append({

        "seller": player.name,

        "item": item_name,

        "price": price

    })

    player.inventory[item_name] -= 1

    if player.inventory[item_name] <= 0:

        del player.inventory[item_name]

    print(
        "\nItem Listed!"
    )


def browse_auction(player):

    print(
        "\n===== AUCTION ====="
    )

    if len(AUCTIONS) == 0:

        print("No Items Listed!")
        return

    for i, auction in enumerate(AUCTIONS):

        print(
            f"{i+1}. "
            f"{auction['item']} "
            f"- {auction['price']} Gold"
        )

    choice = input(
        "\nBuy Item (0 Exit): "
    )

    if choice == "0":

        return

    try:

        auction = AUCTIONS[
            int(choice)-1
        ]

    except:

        return

    if player.gold < auction["price"]:

        print(
            "Not Enough Gold!"
        )

        return

    player.gold -= auction["price"]

    player.inventory[
        auction["item"]
    ] = (
        player.inventory.get(
            auction["item"],
            0
        ) + 1
    )

    AUCTIONS.remove(
        auction
    )

    print(
        "\nPurchased!"
    )