import random

from monster_skill_system import use_monster_skill
from battle_monster import monster_attack


def monster_ai(player, monster):

    # ==========================
    # Monsters with skills
    # ==========================

    roll = random.randint(1, 100)

    # 40% chance to use a skill
    if roll <= 40:

        used = use_monster_skill(
            player,
            monster
        )

        if used:

            return

    # ==========================
    # Otherwise use normal attack
    # ==========================

    monster_attack(
        player,
        monster
    )