from alchemy_data import RECIPES


def alchemy_menu(player):

    while True:

        print("\n===== ALCHEMY =====")

        recipes = list(
            RECIPES.keys()
        )

        for i, item in enumerate(recipes):

            print(
                f"{i+1}. {item}"
            )

        print("0. Exit")

        choice = input(
            "Choice: "
        )

        if choice == "0":

            return

        try:

            item = recipes[
                int(choice)-1
            ]

        except:

            print(
                "Invalid Choice!"
            )

            continue

        recipe = RECIPES[item]

        for material, amount in recipe.items():

            if player.inventory.get(
                material,
                0
            ) < amount:

                print(
                    "\nMissing:",
                    material
                )

                break

        else:

            for material, amount in recipe.items():

                player.inventory[
                    material
                ] -= amount

            player.inventory[item] = (
                player.inventory.get(
                    item,
                    0
                ) + 1
            )

            print(
                "\nCrafted:",
                item
            )