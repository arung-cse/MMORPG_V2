import random
from enchant_data import ENCHANTS


def enchant_weapon(player):

    if player.weapon == "None":

        print("\nNo weapon equipped!")

        return

    enchant = random.choice(

        list(ENCHANTS.keys())

    )

    player.weapon_enchant = enchant

    print(

        "\nWeapon Enchanted!"

    )

    print(

        "New Enchant:",

        enchant

    )