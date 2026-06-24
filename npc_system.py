def npc_menu(player):

    print("\n===== NPC =====")

    if not hasattr(
        player,
        "current_area"
    ):

        player.current_area = (
            "Beginner Village"
        )

    if player.current_area == (
        "Beginner Village"
    ):

        print(
            "Village Chief:"
        )

        print(
            "Welcome adventurer!"
        )

    elif player.current_area == (
        "Goblin Forest"
    ):

        print(
            "Hunter:"
        )

        print(
            "Beware of Goblins!"
        )

    elif player.current_area == (
        "Skeleton Graveyard"
    ):

        print(
            "Priest:"
        )

        print(
            "The undead are rising."
        )

    else:

        print(
            "No NPCs here."
        )