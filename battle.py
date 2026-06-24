import random
from pet_data import PETS

pet_bonus = 0

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

            pet_bonus = 0

        if player.pet:

            pet_bonus = PETS[
                player.pet
            ]["attack"]

            damage = random.randint(

                player.attack +
                pet_bonus - 3,

                player.attack +
                pet_bonus + 3
            )

            monster_hp -= damage

            print(
            "\nYou dealt",
             damage,
             "damage!"
            )

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

            reward_exp = monster["exp"]

            if player.mount:

                from mount_data import MOUNTS

            percent = MOUNTS[player.mount]["exp_bonus"]

            reward_exp += (
            reward_exp * percent
            ) // 100

        player.gain_exp(reward_exp)

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
    
    if monster["name"] == "Goblin":

     player.inventory["Herb"] = (
        player.inventory.get(
            "Herb",
            0
        ) + 1
    )

    if monster["name"] == "Wolf":

     player.inventory["Blue Herb"] = (
        player.inventory.get(
            "Blue Herb",
            0
        ) + 1
    )

    if monster["name"] == "Skeleton":

     player.inventory["Life Crystal"] = (
        player.inventory.get(
            "Life Crystal",
            0
        ) + 1
    )

    if monster["name"] == "Orc":

     player.inventory["Red Crystal"] = (
        player.inventory.get(
            "Red Crystal",
            0
        ) + 1
    )

    drop = random.randint(1, 100)

    if drop <= 10:

     player.inventory["Attack Gem"] = (
        player.inventory.get(
            "Attack Gem",
            0
        ) + 1
    )

    print(
        "Dropped Attack Gem!"
    ) 
    player.inventory[
    "Legendary Gem"
] = (
    player.inventory.get(
        "Legendary Gem",
        0
    ) + 1
)

    player.total_kills += 1

    player.boss_kills += 1
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

    if player.pet:

         pet_bonus = PETS[player.pet]["attack"]