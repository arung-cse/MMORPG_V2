import random

def boss_battle(player, boss):

    boss_hp = boss["hp"]

    print("\n===== BOSS BATTLE =====")
    print(boss["name"])

    while boss_hp > 0 and player.hp > 0:

        print("\nYour HP:", player.hp)
        print("Boss HP:", boss_hp)

        print("1. Attack")
        print("2. Run")

        choice = input("Choice: ")

        if choice == "1":

            damage = random.randint(
                player.attack,
                player.attack + 20
            )

            boss_hp -= damage

            print(
                "You dealt",
                damage,
                "damage!"
            )

            if boss_hp <= 0:

                print(
                    "\nBoss Defeated!"
                )

                player.gain_exp(
                    boss["exp"]
                )

                player.gold += (
                    boss["gold"]
                )

                return True

            player.take_damage(
                boss["attack"]
            )

        elif choice == "2":

            return False

    return False