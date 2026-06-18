import random

def battle(player, monster):

    monster_hp = monster["hp"]

    print("\n======================")
    print("A Wild", monster["name"], "Appeared!")
    print("======================")

    while monster_hp > 0 and player.hp > 0:

        print("\nYour HP :", player.hp)
        print(monster["name"], "HP :", monster_hp)

        print("\n1. Attack")
        print("2. Run")

        choice = input("Choice: ")

        if choice == "1":

            damage = random.randint(
                player.attack - 3,
                player.attack + 3
            )

            monster_hp -= damage

            print(
                "\nYou dealt",
                damage,
                "damage!"
            )

            if monster_hp <= 0:

                print(
                    "\nYou defeated",
                    monster["name"]
                )

                player.gain_exp(
                    monster["exp"]
                )

                player.gold += monster["gold"]

                print(
                    "+",
                    monster["exp"],
                    "EXP"
                )

                print(
                    "+",
                    monster["gold"],
                    "Gold"
                )

                return

            enemy_damage = random.randint(
                monster["attack"] - 2,
                monster["attack"] + 2
            )

            player.hp -= enemy_damage

            print(
                monster["name"],
                "dealt",
                enemy_damage,
                "damage!"
            )

        elif choice == "2":

            print("\nEscaped!")

            return

    if player.hp <= 0:

        print("\nYOU DIED!")

        player.hp = player.max_hp

        print(
            "Respawned in town!"
        )