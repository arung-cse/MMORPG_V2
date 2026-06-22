from dungeon_data import DUNGEONS
from dungeon_monsters import DUNGEON_MONSTERS
from battle import battle


def dungeon_menu(player):

    while True:

        print("\n===== DUNGEONS =====")

        names = list(DUNGEONS.keys())

        for i, dungeon in enumerate(names):

            print(
                f"{i+1}. {dungeon}"
            )

        print("0. Exit")

        choice = input("Choice: ")

        if choice == "0":

            return

        try:

            dungeon_name = names[
                int(choice) - 1
            ]

        except:

            print("Invalid Choice!")
            continue

        dungeon = DUNGEONS[
            dungeon_name
        ]

        if player.level < dungeon[
            "required_level"
        ]:

            print(
                "\nRequired Level:",
                dungeon[
                    "required_level"
                ]
            )

            continue

        monster = (
            DUNGEON_MONSTERS[
                dungeon_name
            ].copy()
        )

        print(
            "\nEntering:",
            dungeon_name
        )

        battle(
            player,
            monster
        )

        if player.hp > 0:

            reward_exp = (
                monster["exp"]
            )

            reward_gold = (
                monster["gold"]
            )

            # Mount Bonus

            if (
                hasattr(player, "mount")
                and player.mount
            ):

                from mount_data import (
                    MOUNTS
                )

                percent = MOUNTS[
                    player.mount
                ][
                    "exp_bonus"
                ]

                reward_exp += (
                    reward_exp
                    * percent
                ) // 100

            player.gain_exp(
                reward_exp
            )

            player.gold += (
                reward_gold
            )

            print(
                "\nDungeon Cleared!"
            )

            print(
                "+",
                reward_exp,
                "EXP"
            )

            print(
                "+",
                reward_gold,
                "Gold"
            )