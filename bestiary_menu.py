def show_bestiary(player):

    print("\n========== BESTIARY ==========")

    if len(player.bestiary) == 0:

        print("No Monsters Discovered!")

        return

    for monster in player.bestiary:

        print(

            monster,

            "-",

            player.bestiary[monster]["kills"],

            "Kills"

        )