QUESTS = {

    "Goblin Hunter": {
        "description": "Kill 5 Goblins",
        "target": "Goblin",
        "required": 5,
        "reward_gold": 100,
        "reward_exp": 50
    },

    "Wolf Hunter": {
        "description": "Kill 3 Wolves",
        "target": "Wolf",
        "required": 3,
        "reward_gold": 150,
        "reward_exp": 75
    },

    "Skeleton Slayer": {
        "description": "Kill 2 Skeletons",
        "target": "Skeleton",
        "required": 2,
        "reward_gold": 250,
        "reward_exp": 100
    }
}


def show_quests(player):

    print("\n===== QUESTS =====")

    for quest_name, quest in QUESTS.items():

        target = quest["target"]

        progress = player.quest_progress.get(
            target,
            0
        )

        print("\n" + quest_name)

        print(
            quest["description"]
        )

        print(
            "Progress:",
            str(progress)
            + "/"
            + str(quest["required"])
        )


def claim_rewards(player):

    print("\n===== CLAIM QUESTS =====")

    completed = False

    for quest_name, quest in QUESTS.items():

        target = quest["target"]

        progress = player.quest_progress.get(
            target,
            0
        )

        if progress >= quest["required"]:

            completed = True

            print(
                "\nCompleted:",
                quest_name
            )

            player.gold += quest[
                "reward_gold"
            ]

            player.gain_exp(
                quest["reward_exp"]
            )

            print(
                "+",
                quest["reward_gold"],
                "Gold"
            )

            print(
                "+",
                quest["reward_exp"],
                "EXP"
            )

            player.quest_progress[
                target
            ] = 0

    if not completed:

        print(
            "\nNo completed quests!"
        )