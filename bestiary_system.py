def update_bestiary(player, monster):

    name = monster["name"]

    if name not in player.bestiary:

        player.bestiary[name] = {

            "kills": 0

        }

    player.bestiary[name]["kills"] += 1