import random
from upgrade_data import UPGRADE


MAX_UPGRADE = 15


def upgrade_weapon(player):

    if player.weapon == "None":

        print("\nNo weapon equipped!")

        return

    if player.weapon_upgrade >= MAX_UPGRADE:

        print("\nWeapon already max!")

        return

    info = UPGRADE[player.weapon_upgrade]

    cost = info["cost"]

    chance = info["success"]

    print("\n===== WEAPON UPGRADE =====")

    print("Weapon :", player.weapon)

    print("Current :", "+" + str(player.weapon_upgrade))

    print("Success :", str(chance) + "%")

    print("Cost :", cost)

    if player.gold < cost:

        print("\nNot enough Gold!")

        return

    player.gold -= cost

    roll = random.randint(1,100)

    if roll <= chance:

        player.weapon_upgrade += 1

        player.attack += 5

        print("\n★★★★★ SUCCESS ★★★★★")

        print(player.weapon)

        print("+" + str(player.weapon_upgrade))

    else:

        print("\nUpgrade Failed!")