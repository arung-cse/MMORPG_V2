import json
import os

SAVE_FILE = "save_data.json"


def save_player(player):

    data = {

        "name": player.name,
        "job": player.job,

        "level": player.level,
        "exp": player.exp,

        "gold": player.gold,

        "hp": player.hp,
        "max_hp": player.max_hp,

        "attack": player.attack,

        "inventory": player.inventory
    }

    with open(SAVE_FILE, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )

    print("\nGame Saved Successfully!")


def load_player(player):

    if not os.path.exists(SAVE_FILE):

        print("\nNo Save File Found!")

        return False

    with open(SAVE_FILE, "r") as file:

        data = json.load(file)

    player.name = data["name"]
    player.job = data["job"]

    player.level = data["level"]
    player.exp = data["exp"]

    player.gold = data["gold"]

    player.hp = data["hp"]
    player.max_hp = data["max_hp"]

    player.attack = data["attack"]

    player.inventory = data["inventory"]

    print("\nGame Loaded Successfully!")

    return True