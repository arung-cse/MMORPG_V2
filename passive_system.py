from passive_tree import PASSIVE_TREE
from passive_skill_data import PASSIVE_SKILLS


def check_passive_unlocks(player):

    if not hasattr(player, "learned_passives"):

        player.learned_passives = []

    if player.job not in PASSIVE_TREE:

        return

    for unlock_level, passives in PASSIVE_TREE[player.job].items():

        if player.level >= unlock_level:

            for passive in passives:

                if passive not in player.learned_passives:

                    player.learned_passives.append(
                        passive
                    )

                    apply_passive(
                        player,
                        passive
                    )

                    print(
                        "\nNEW PASSIVE:",
                        passive
                    )


def apply_passive(player, passive_name):

    if passive_name not in PASSIVE_SKILLS:

        return

    data = PASSIVE_SKILLS[
        passive_name
    ]

    if "hp_bonus" in data:

        player.max_hp += data[
            "hp_bonus"
        ]

        player.hp = player.max_hp

    if "mp_bonus" in data:

        player.max_mp += data[
            "mp_bonus"
        ]

        player.mp = player.max_mp

    if "attack_bonus" in data:

        player.attack += data[
            "attack_bonus"
        ]

    if "defense_bonus" in data:

        player.defense += data[
            "defense_bonus"
        ]

    if "critical_bonus" in data:

        player.critical += data[
            "critical_bonus"
        ]


def show_passives(player):

    print(
        "\n===== PASSIVES ====="
    )

    if len(
        player.learned_passives
    ) == 0:

        print(
            "No Passives Learned"
        )

        return

    for passive in player.learned_passives:

        print(passive)