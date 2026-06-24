from achievement_data import ACHIEVEMENTS


def check_achievements(player):

    if not hasattr(
        player,
        "completed_achievements"
    ):
        player.completed_achievements = []

    for name, data in ACHIEVEMENTS.items():

        if name in player.completed_achievements:
            continue

        value = 0

        if data["type"] == "level":
            value = player.level

        elif data["type"] == "gold":
            value = player.gold

        elif data["type"] == "kills":
            value = player.total_kills

        elif data["type"] == "boss_kills":
            value = player.boss_kills

        elif data["type"] == "tower_floor":
            value = player.tower_floor

        elif data["type"] == "dungeons":
            value = player.dungeons_cleared

        if value >= data["required"]:

            player.completed_achievements.append(
                name
            )

            player.gold += data[
                "reward_gold"
            ]

            print(
                "\nACHIEVEMENT UNLOCKED!"
            )

            print(name)

            print(
                "+",
                data["reward_gold"],
                "Gold"
            )