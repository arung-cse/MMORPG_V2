import random
from pet_data import PETS


def battle(player, monster):

    monster_hp = monster["hp"]

    print("\n======================")
    print(f"A Wild {monster['name']} Appeared!")
    print("======================")

    while monster_hp > 0 and player.hp > 0:

        print(f"\nYour HP : {player.hp}/{player.max_hp}")
        print(f"{monster['name']} HP : {monster_hp}")

        print("\n1. Attack")
        print("2. Skills")
        print("3. Run")

        choice = input("Choice: ")

        # =====================================
        # NORMAL ATTACK
        # =====================================

        if choice == "1":

            pet_bonus = 0

            if hasattr(player, "pet") and player.pet:

                pet_bonus = PETS[player.pet]["attack"]

            damage = random.randint(
                player.attack + pet_bonus - 3,
                player.attack + pet_bonus + 3
            )

            monster_hp -= damage

            print(f"\nYou dealt {damage} damage!")

        # =====================================
        # SKILL ATTACK
        # =====================================

        elif choice == "2":

            from skills import show_skills
            from skills import use_skill

            show_skills(player)

            skill = input("Skill: ").title()

            damage = use_skill(player, skill)

            if damage <= 0:
                continue

            monster_hp -= damage

            print(f"{skill} dealt {damage} damage!")

        # =====================================
        # RUN
        # =====================================

        elif choice == "3":

            print("\nYou escaped!")

            return False

        else:

            print("\nInvalid Choice!")

            continue

        # =====================================
        # MONSTER DEFEATED
        # =====================================

        if monster_hp <= 0:

            print(f"\nYou defeated {monster['name']}!")

            reward_exp = monster.get("exp", 0)
            reward_gold = monster.get("gold", 0)

            # Mount EXP Bonus

            if hasattr(player, "mount") and player.mount:

                from mount_data import MOUNTS

                bonus = MOUNTS[player.mount]["exp_bonus"]

                reward_exp += reward_exp * bonus // 100

            player.gain_exp(reward_exp)
            player.gain_gold(reward_gold)

            print(f"+ {reward_exp} EXP")
            print(f"+ {reward_gold} Gold")

            # Quest Progress

            if hasattr(player, "quest_progress"):

                if monster["name"] in player.quest_progress:

                    player.quest_progress[monster["name"]] += 1

            # Statistics

            if hasattr(player, "total_kills"):

                player.total_kills += 1

            if hasattr(player, "boss_kills"):

                if monster.get("boss", False):

                    player.boss_kills += 1

            # =====================================
            # MATERIAL DROPS
            # =====================================

            drops = {

                "Goblin": "Herb",

                "Wolf": "Blue Herb",

                "Skeleton": "Life Crystal",

                "Orc": "Red Crystal"

            }

            if monster["name"] in drops:

                item = drops[monster["name"]]

                player.inventory[item] = (
                    player.inventory.get(item, 0) + 1
                )

                print(f"Dropped: {item}")

            # =====================================
            # EQUIPMENT DROP
            # =====================================

            if random.randint(1, 100) <= 20:

                player.inventory["Iron Sword"] = (
                    player.inventory.get("Iron Sword", 0) + 1
                )

                print("Dropped: Iron Sword")

            # =====================================
            # ATTACK GEM
            # =====================================

            if random.randint(1, 100) <= 10:

                player.inventory["Attack Gem"] = (
                    player.inventory.get("Attack Gem", 0) + 1
                )

                print("Dropped: Attack Gem")

            # =====================================
            # LEGENDARY GEM
            # =====================================

            if random.randint(1, 1000) == 1:

                player.inventory["Legendary Gem"] = (
                    player.inventory.get("Legendary Gem", 0) + 1
                )

                print("★★★★★ Legendary Gem Dropped! ★★★★★")

            return True

        # =====================================
        # MONSTER ATTACK
        # =====================================

        enemy_damage = random.randint(

            max(1, monster["attack"] - 2),

            monster["attack"] + 2

        )

        player.take_damage(enemy_damage)

        print(f"{monster['name']} dealt {enemy_damage} damage!")

    # =====================================
    # PLAYER DEAD
    # =====================================

    if player.hp <= 0:

        print("\n===== YOU DIED =====")

        player.hp = player.max_hp

        print("Respawned in Town!")

        return False