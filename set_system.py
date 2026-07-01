from set_data import EQUIPMENT_SETS


def check_set_bonus(player):

    equipped = [

        player.weapon,

        player.armor,

        player.accessory

    ]

    for set_name, data in EQUIPMENT_SETS.items():

        if all(

            item in equipped

            for item in data["items"]

        ):

            print(f"\n★★★★★ {set_name} Activated! ★★★★★")

            return data["bonus"]

    return None