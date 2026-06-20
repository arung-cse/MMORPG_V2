import random


def battle(player, monster):

    monster_hp = monster["hp"]

    print("\n======================")
    print("A Wild", monster["name"], "Appeared!")
    print("======================")

    while monster_hp > 0 and player.hp > 0:

        print("\nYour HP :", player.hp, "/", player.max_hp)
        print(monster["name"], "HP :", monster_hp)

        print("\n1. Attack")
        print("2. Skills")
        print("3. Run")

        choice = input("Choice: ")

        # =========================
        # NORMAL ATTACK
        # =========================

        if choice == "1":

            damage = random.randint(
                max(1, player.attack - 3),
                player.attack + 3
            )

            monster_hp -= damage

            print("\nYou dealt", damage, "damage!")

        # =========================
        # SKILLS
        # =========================

        elif choice == "2":

            from skills import show_skills
            from skills import use_skill

            show_skills(player)

            skill_name = input("Skill: ")

            damage = use_skill(
                player,
                skill_name
            )

            if damage > 0:

                monster_hp -= damage

                print(
                    skill_name,
                    "dealt",
                    damage,
                    "damage!"
                )

        # =========================
        # RUN
        # =========================

        elif choice == "3":

            print("\nEscaped!")

            return

        else:

            print("\nInvalid Choice!")

            continue

        # =========================
        # MONSTER DEAD
        # =========================

        if monster_hp <= 0:

            print(
                "\nYou defeated",
                monster["name"]
            )

            player.gain_exp(
                monster["exp"]
            )

            player.gold += monster["gold"]

            monster_name = monster["name"]

            if monster_name in player.quest_progress:

             player.quest_progress[monster_name] += 1

            print(
                "+",
                monster["gold"],
                "Gold"
            )

            # Item Drop

            drop = random.randint(1, 100)

            if drop <= 20:

                player.inventory["Iron Sword"] = (
                    player.inventory.get(
                        "Iron Sword",
                        0
                    ) + 1
                )

                print(
                    "Monster Dropped Iron Sword!"
                )

            return

        # =========================
        # MONSTER ATTACK
        # =========================

        enemy_damage = random.randint(
            max(1, monster["attack"] - 2),
            monster["attack"] + 2
        )

        player.hp -= enemy_damage

        print(
            monster["name"],
            "dealt",
            enemy_damage,
            "damage!"
        )

    # =========================
    # PLAYER DEAD
    # =========================

    if player.hp <= 0:

        print("\nYOU DIED!")

        player.hp = player.max_hp

        print(
            "Respawned in town!"
        )