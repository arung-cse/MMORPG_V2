from dungeon_data import DUNGEONS

def dungeon_menu(player):

    while True:

        print("\n===== DUNGEONS =====")

        count = 1

        names = list(DUNGEONS.keys())

        for dungeon in names:

            print(count, ".", dungeon)

            count += 1

        print("0. Exit")

        choice = input("Choice: ")

        if choice == "0":

            return

        try:

            dungeon_name = names[int(choice)-1]

        except:

            print("Invalid Choice!")

            continue

        dungeon = DUNGEONS[dungeon_name]

        if player.level < dungeon["required_level"]:

            print(
                "\nRequired Level:",
                dungeon["required_level"]
            )

            continue

        print(
            "\nDungeon Cleared:",
            dungeon_name
        )

        reward_exp = dungeon["exp"]

        if player.mount:

            from mount_data import MOUNTS

            percent = MOUNTS[player.mount]["exp_bonus"]

            reward_exp += (
            reward_exp * percent
        ) // 100

        player.gain_exp(reward_exp)

        player.gold += (
            dungeon["gold"]
        )

        print(
            "+",
            dungeon["gold"],
            "Gold"
        )