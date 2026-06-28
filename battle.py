import random

from battle_attack import normal_attack
from battle_monster import monster_attack
from battle_rewards import give_rewards
from battle_loot import give_loot

from battle_status import (
    process_status,
    apply_status
)

from skills import (
    show_skills,
    use_skill
)


def battle(player, monster):

    monster_hp = monster["hp"]

    print("\n======================")
    print(f"A Wild {monster['name']} Appeared!")
    print("======================")

    while monster_hp > 0 and player.hp > 0:

        # -------------------------
        # Status Effects
        # -------------------------

        process_status(player)

        print(f"\nYour HP : {player.hp}/{player.max_hp}")
        print(f"{monster['name']} HP : {monster_hp}")

        print("\n1. Attack")
        print("2. Skills")
        print("3. Run")

        choice = input("Choice: ")

        # -------------------------
        # Normal Attack
        # -------------------------

        if choice == "1":

            damage = normal_attack(player)

            monster_hp -= damage

            print(f"\nYou dealt {damage} damage!")

        # -------------------------
        # Skills
        # -------------------------

        elif choice == "2":

            show_skills(player)

            skill = input("Skill: ").title()

            damage = use_skill(player, skill)

            if damage <= 0:

                continue

            monster_hp -= damage

            print(f"{skill} dealt {damage} damage!")

        # -------------------------
        # Run
        # -------------------------

        elif choice == "3":

            print("\nEscaped!")

            return False

        else:

            print("Invalid Choice!")

            continue

        # -------------------------
        # Monster Dead
        # -------------------------

        if monster_hp <= 0:

            print(f"\nYou defeated {monster['name']}!")

            give_rewards(player, monster)

            give_loot(player, monster)

            if monster["name"] in player.quest_progress:

                player.quest_progress[monster["name"]] += 1

            if hasattr(player, "total_kills"):

                player.total_kills += 1

            return True

        # -------------------------
        # Monster Status Skill
        # -------------------------

        if "status" in monster:

            apply_status(
                player,
                monster["status"]
            )

        # -------------------------
        # Monster Attack
        # -------------------------

        monster_attack(
            player,
            monster
        )

    print("\n===== YOU DIED =====")

    player.hp = player.max_hp

    print("Respawned in Town!")

    return False