from cooking_data import RECIPES


def cooking_menu(player):

    while True:

        print(
            "\n===== COOKING ====="
        )

        recipes = list(
            RECIPES.keys()
        )

        for i, recipe in enumerate(
            recipes
        ):

            print(
                f"{i+1}. {recipe}"
            )

        print("0. Exit")

        choice = input(
            "Choice: "
        )

        if choice == "0":

            return

        try:

            food = recipes[
                int(choice)-1
            ]

        except:

            continue

        recipe = RECIPES[food]

        can_make = True

        for item, amount in recipe.items():

            if player.inventory.get(
                item,
                0
            ) < amount:

                can_make = False

        if not can_make:

            print(
                "\nMissing Materials!"
            )

            continue

        for item, amount in recipe.items():

            player.inventory[item] -= amount

        player.inventory[food] = (
            player.inventory.get(
                food,
                0
            ) + 1
        )

        print(
            "\nCooked:",
            food
        )