from battle_attack import normal_attack
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

from monster_ai import monster_ai
from boss_ai import boss_phase


def battle(player, monster):

    # ==========================
    # INITIALIZE BATTLE
    # ==========================

    monster_hp = monster["hp"]
    monster["current_hp"] = monster_hp

    print("\n======================")
    print(f"A Wild {monster['name']} Appeared!")
    print("======================")

    while monster_hp > 0 and player.hp > 0:

        # ==========================
        # PLAYER STATUS EFFECTS
        # ==========================

        process_status(player)

        print("\n======================")
        print(f"Your HP : {player.hp}/{player.max_hp}")
        print(f"{monster['name']} HP : {monster_hp}")
        print("======================")

        print("1. Attack")
        print("2. Skills")
        print("3. Run")

        choice = input("Choice: ")

        # ==========================
        # NORMAL ATTACK
        # ==========================

        if choice == "1":

            damage = normal_attack(player)

            damage = element_bonus(
                damage,
                "Fire",      # Replace later with weapon element
                monster.get("element")
            )

            monster_hp -= damage

            if monster_hp < 0:
                monster_hp = 0

            monster["current_hp"] = monster_hp

            # Boss Phase System
            if "phase2" in monster:

                boss_phase(monster)

            print(f"\nYou dealt {damage} damage!")

        # ==========================
        # SKILLS
        # ==========================

        elif choice == "2":

            show_skills(player)

            skill = input("\nSkill: ").title()

            damage = use_skill(
                player,
                skill
            )

            if damage <= 0:

                continue

            damage = element_bonus(
                damage,
                "Fire",      # Replace later with skill element
                monster.get("element")
            )

            monster_hp -= damage

            if monster_hp < 0:
                monster_hp = 0

            monster["current_hp"] = monster_hp

            # Boss Phase System
            if "phase2" in monster:

                boss_phase(monster)

            print(f"\n{skill} dealt {damage} damage!")

        # ==========================
        # RUN
        # ==========================

        elif choice == "3":

            print("\nEscaped!")

            return False

        else:

            print("\nInvalid Choice!")

            continue

        # ==========================
        # MONSTER DEFEATED
        # ==========================

        if monster_hp <= 0:

            monster["current_hp"] = 0

            print(f"\nYou defeated {monster['name']}!")

            give_rewards(
                player,
                monster
            )

            give_loot(
                player,
                monster
            )

            # Quest Progress

            if hasattr(player, "quest_progress"):

                if monster["name"] in player.quest_progress:

                    player.quest_progress[
                        monster["name"]
                    ] += 1

            # Statistics

            if hasattr(player, "total_kills"):

                player.total_kills += 1

            if hasattr(player, "boss_kills"):

                if "phase2" in monster:

                    player.boss_kills += 1

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
        # MONSTER AI
        # ==========================

        monster_ai(
            player,
            monster
        )

    # ==========================
    # PLAYER DEFEATED
    # ==========================

    print("\n======================")
    print("YOU DIED!")
    print("======================")

    player.hp = player.max_hp
    player.mp = player.max_mp

    print("Respawned in Town!")

    return False