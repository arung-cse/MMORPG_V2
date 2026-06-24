def show_achievements(player):

    print(
        "\n===== ACHIEVEMENTS ====="
    )

    if not hasattr(
        player,
        "completed_achievements"
    ):
        player.completed_achievements = []

    if len(
        player.completed_achievements
    ) == 0:

        print(
            "No Achievements Yet"
        )

        return

    for achievement in (
        player.completed_achievements
    ):

        print(achievement)