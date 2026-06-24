from guild_data import GUILDS


def create_guild(player):

    if hasattr(player, "guild"):

        if player.guild:

            print(
                "\nAlready in a guild!"
            )

            return

    name = input(
        "\nGuild Name: "
    )

    if name in GUILDS:

        print(
            "\nGuild already exists!"
        )

        return

    GUILDS[name] = {

        "leader": player.name,

        "members": [
            player.name
        ],

        "level": 1,

        "guild_gold": 0
    }

    player.guild = name

    print(
        "\nGuild Created!"
    )


def show_guild(player):

    if not hasattr(player, "guild"):

        player.guild = None

    if not player.guild:

        print(
            "\nNo Guild"
        )

        return

    guild = GUILDS[
        player.guild
    ]

    print(
        "\n===== GUILD ====="
    )

    print(
        "Name:",
        player.guild
    )

    print(
        "Leader:",
        guild["leader"]
    )

    print(
        "Members:",
        len(
            guild["members"]
        )
    )

    print(
        "Level:",
        guild["level"]
    )

    print(
        "Guild Gold:",
        guild["guild_gold"]
    )