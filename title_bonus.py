from title_data import TITLES


def apply_title_bonus(player):

    if player.title == "None":

        return

    data = TITLES[
        player.title
    ]

    if "attack" in data:

        player.attack += data[
            "attack"
        ]

    if "hp" in data:

        player.max_hp += data[
            "hp"
        ]

    if "critical" in data:

        player.critical += data[
            "critical"
        ]