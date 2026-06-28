from battle_attack import normal_attack
from battle_monster import monster_attack
from battle_rewards import give_rewards
from battle_loot import give_loot

from battle_status import (
    process_status,
    apply_status
)

from battle_element import element_bonus

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

        # ==========================
        # STATUS EFFECTS
        # ==========================

        process_status(player)

        print(f"\nYour HP : {player.hp}/{player.max_hp}")
        print(f"{monster['name']} HP : {monster_hp}")

        print("\n1. Attack")
        print("2. Skills")
        print("3. Run")

        choice = input("Choice: ")

        # ==========================
        # NORMAL ATTACK
        # ==========================

        if choice == "1":

            damage = normal_attack(player)

            # Element Damage
            damage = element_bonus(
                damage,
                "Fire",          # Replace later with weapon element
                monster.get("element")
            )

            monster_hp -= damage

            print(f"\nYou dealt {damage} damage!")

        # ==========================
        # SKILLS
        # ==========================

        elif choice == "2":

            show_skills(player)

            skill = input("Skill: ").title()

            damage = use_skill(player, skill)

            if damage <= 0:
                continue

            # Element Damage
            damage = element_bonus(
                damage,
                "Fire",          # Replace later with skill element
                monster.get("element")
            )

            monster_hp -= damage

            print(f"{skill} dealt {damage} damage!")

        # ==========================
        # RUN
        # ==========================

        elif choice == "3":

            print("\nEscaped!")

            return False

        else:

            print("Invalid Choice!")

            continue

        # ==========================
        # MONSTER DEFEATED
        # ==========================

        if monster_hp <= 0:

            print(f"\nYou defeated {monster['name']}!")

            give_rewards(player, monster)

            give_loot(player, monster)

            if hasattr(player, "quest_progress"):

                if monster["name"] in player.quest_progress:

                    player.quest_progress[monster["name"]] += 1

            if hasattr(player, "total_kills"):

                player.total_kills += 1

            return True

        # ==========================
        # MONSTER STATUS EFFECT
        # ==========================

        if "status" in monster:

            apply_status(
                player,
                monster["status"]
            )

        # ==========================
        # MONSTER ATTACK
        # ==========================

        monster_attack(
            player,
            monster
        )

    # ==========================
    # PLAYER DEAD
    # ==========================

    print("\n===== YOU DIED =====")

    player.hp = player.max_hp

    print("Respawned in Town!")

    return False