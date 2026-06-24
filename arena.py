from arena_data import ARENA_RANKS
import random


def arena_menu(player):

    if not hasattr(player, "arena_rank"):

        player.arena_rank = 0

    while True:

        print("\n===== ARENA =====")

        current = ARENA_RANKS[
            player.arena_rank
        ]

        print(
            "Current Rank:",
            current["rank"]
        )

        print("1. Challenge")
        print("2. Exit")

        choice = input("Choice: ")

        if choice == "1":

            enemy_hp = current[
                "enemy_hp"
            ]

            while enemy_hp > 0 and player.hp > 0:

                damage = random.randint(
                    player.attack,
                    player.attack + 20
                )

                enemy_hp -= damage

                print(
                    "You dealt",
                    damage
                )

                if enemy_hp <= 0:

                    print(
                        "\nArena Victory!"
                    )

                    player.gold += current[
                        "reward"
                    ]

                    print(
                        "+",
                        current["reward"],
                        "Gold"
                    )

                    if (
                        player.arena_rank
                        < len(
                            ARENA_RANKS
                        ) - 1
                    ):

                        player.arena_rank += 1

                        print(
                            "Promoted!"
                        )

                    break

                player.take_damage(
                    current[
                        "enemy_attack"
                    ]
                )

            if player.hp <= 0:

                print(
                    "\nArena Defeat!"
                )

                player.hp = player.max_hp

        elif choice == "2":

            break