from battle import battle
from tower_bosses import TOWER_MONSTERS


def tower_menu(player):

    if not hasattr(player, "tower_floor"):
        player.tower_floor = 1

    while True:

        print("\n===== TOWER =====")
        print("Current Floor:", player.tower_floor)

        print("1. Challenge Floor")
        print("2. Leave Tower")

        choice = input("Choice: ")

        if choice == "1":

            monster_index = min(
                player.tower_floor // 5,
                len(TOWER_MONSTERS) - 1
            )

            monster = TOWER_MONSTERS[
                monster_index
            ].copy()

            print(
                "\n===== FLOOR",
                player.tower_floor,
                "====="
            )

            battle(player, monster)

            if player.hp > 0:

                reward_exp = player.tower_floor * 20
                reward_gold = player.tower_floor * 10

                if hasattr(player, "mount") and player.mount:

                    from mount_data import MOUNTS

                    percent = MOUNTS[
                        player.mount
                    ]["exp_bonus"]

                    reward_exp += (
                        reward_exp * percent
                    ) // 100

                player.gain_exp(
                    reward_exp
                )

                player.gold += reward_gold

                print("\nFloor Cleared!")
                print("+", reward_exp, "EXP")
                print("+", reward_gold, "Gold")

                player.tower_floor += 1

        elif choice == "2":

            break

        else:

            print("Invalid Choice!")