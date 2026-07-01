import random

from monster_skill_data import MONSTER_SKILLS
from battle_status import apply_status


def use_monster_skill(player, monster):

    # Monster has no skills
    if monster["name"] not in MONSTER_SKILLS:
        return False

    skills = MONSTER_SKILLS[monster["name"]]

    # Pick one random skill
    skill = random.choice(skills)

    # Chance to use it
    roll = random.randint(1, 100)

    if roll > skill["chance"]:
        return False

    print("\n========================")
    print(monster["name"], "used", skill["name"] + "!")
    print("========================")

    damage = skill["damage"]

    player.take_damage(damage)

    print(
        "You received",
        damage,
        "damage!"
    )

    if skill["status"]:

        apply_status(
            player,
            skill["status"]
        )

        print(
            "Status Applied:",
            skill["status"]
        )

    return True