from crafting_data import RECIPES

def craft_item(player):

    print("\n===== CRAFTING =====")

    recipes = list(
        RECIPES.keys()
    )

    for i, item in enumerate(recipes):

        print(
            f"{i+1}. {item}"
        )

    choice = input(
        "Choice: "
    )

    try:

        item = recipes[
            int(choice)-1
        ]

    except:

        print("Invalid Choice!")
        return

    recipe = RECIPES[item]

    for material, amount in recipe.items():

        if player.inventory.get(
            material,
            0
        ) < amount:

            print(
                "\nNot enough",
                material
            )

            return

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