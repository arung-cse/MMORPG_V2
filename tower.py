def tower_menu(player):

    if not hasattr(player, "tower_floor"):
        player.tower_floor = 1

    while True:

        print("\n===== TOWER =====")

        print(
            "Current Floor:",
            player.tower_floor
        )

        print("1. Challenge Floor")
        print("2. Leave Tower")

        choice = input("Choice: ")

        if choice == "1":

            reward_exp = (
                player.tower_floor * 20
            )

            reward_gold = (
                player.tower_floor * 10
            )

            print(
                "\nFloor",
                player.tower_floor,
                "Cleared!"
            )

            # =====================
            # MOUNT EXP BONUS
            # =====================

            if hasattr(player, "mount") and player.mount:

                from mount_data import MOUNTS

                percent = MOUNTS[player.mount]["exp_bonus"]

                reward_exp += (
                    reward_exp * percent
                ) // 100

            # =====================
            # GIVE REWARDS
            # =====================

            player.gain_exp(
                reward_exp
            )

            player.gold += (
                reward_gold
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

            player.tower_floor += 1

        elif choice == "2":

            break

        else:

            print(
                "Invalid Choice!"
            )