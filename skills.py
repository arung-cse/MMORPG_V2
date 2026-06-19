from skill_data import SKILLS


def show_skills(player):

    print("\n===== SKILLS =====")

    if player.job not in SKILLS:

        print("No Skills")
        return

    for skill in SKILLS[player.job]:

        print(skill)


def use_skill(player, skill_name):

    if player.job not in SKILLS:

        return 0

    if skill_name not in SKILLS[player.job]:

        return 0

    skill = SKILLS[player.job][skill_name]

    if player.mp < skill["mp_cost"]:

        print("Not enough MP!")
        return 0

    player.mp -= skill["mp_cost"]

    return skill["damage"]