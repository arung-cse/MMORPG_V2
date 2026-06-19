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