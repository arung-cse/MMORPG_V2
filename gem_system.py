from gem_data import GEMS


def socket_gem(player):

    print("\n===== GEM SOCKET =====")

    gems = []

    for item in player.inventory:

        if "Gem" in item:

            gems.append(item)

    if len(gems) == 0:

        print("No Gems!")

        return

    for i, gem in enumerate(gems):

        print(f"{i+1}. {gem}")

    choice = input("Choice: ")

    try:

        gem = gems[int(choice)-1]

    except:

        print("Invalid Choice!")
        return

    player.weapon_gems.append(gem)

    player.inventory[gem] -= 1

    if player.inventory[gem] <= 0:

        del player.inventory[gem]

    data = GEMS[gem]

    if "attack" in data:

        player.attack += data["attack"]

    if "defense" in data:

        player.defense += data["defense"]

    if "hp" in data:

        player.max_hp += data["hp"]

    if "mp" in data:

        player.max_mp += data["mp"]

    if "critical" in data:

        player.critical += data["critical"]

    print(
        "\nSocketed:",
        gem
    )