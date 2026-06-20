from npc import town_npc
from quests import (
    show_quests,
    claim_rewards
)


def town_menu(player):

    while True:

        print("\n===== TOWN =====")

        print("1. Quest Master")
        print("2. View Quests")
        print("3. Claim Rewards")
        print("4. Leave Town")

        choice = input(
            "Choice: "
        )

        if choice == "1":

            town_npc()

        elif choice == "2":

            show_quests(player)

        elif choice == "3":

            claim_rewards(player)

        elif choice == "4":

            return