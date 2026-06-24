def story_quest_menu(player):

    print(
        "\n===== STORY QUEST ====="
    )

    if player.level < 5:

        print(
            "Quest 1:"
        )

        print(
            "Defeat 5 Goblins"
        )

    elif player.level < 10:

        print(
            "Quest 2:"
        )

        print(
            "Defeat 10 Wolves"
        )

    elif player.level < 20:

        print(
            "Quest 3:"
        )

        print(
            "Clear Skeleton Crypt"
        )

    elif player.level < 50:

        print(
            "Quest 4:"
        )

        print(
            "Defeat Orc Warlord"
        )

    else:

        print(
            "More story coming soon!"
        )