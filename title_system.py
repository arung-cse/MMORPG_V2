from title_data import TITLES


def unlock_title(player, title):

    if not hasattr(
        player,
        "unlocked_titles"
    ):

        player.unlocked_titles = []

    if title in player.unlocked_titles:

        return

    player.unlocked_titles.append(
        title
    )

    print(
        "\nNEW TITLE:",
        title
    )


def equip_title(player):

    if len(
        player.unlocked_titles
    ) == 0:

        print(
            "\nNo Titles"
        )

        return

    print(
        "\n===== TITLES ====="
    )

    for i, title in enumerate(
        player.unlocked_titles
    ):

        print(
            f"{i+1}. {title}"
        )

    choice = input(
        "Choice: "
    )

    try:

        title = player.unlocked_titles[
            int(choice)-1
        ]

    except:

        return

    player.title = title

    print(
        "\nEquipped:",
        title
    )


def show_title(player):

    print(
        "\nCurrent Title:"
    )

    print(
        player.title
    )