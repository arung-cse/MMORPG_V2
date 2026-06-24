import boss_data
from player import Player
from monster import get_monster
from battle import battle

from inventory import (
    show_inventory,
    use_potion
)

from equipment import (
    show_equipment,
    equip_item
)

from quests import (
    show_quests,
    claim_rewards
)

from save_system import (
    save_player,
    load_player
)

from shop import (
    buy_item,
    sell_item
)

from passive_system import (
    show_passives
)

from town import town_menu
from tower import tower_menu
from dungeon import dungeon_menu
from boss_battle import boss_menu

from pet_system import (
    adopt_pet,
    show_pet
)

from mount_system import (
    adopt_mount,
    show_mount
)

from world_boss import (
    world_boss_menu
)

from blacksmith import (
    blacksmith_menu
)

from skills import (
    show_skills
)

from alchemy import (
    alchemy_menu
)

from upgrade_menu import (
    upgrade_menu
)

from gem_menu import gem_menu

from guild_menu import (
    guild_menu
)

from world_map import (
    world_map_menu
)

from npc_system import (
    npc_menu
)

from story_quests import (
    story_quest_menu
)

from achievement_system import (
    check_achievements
)

from achievement_menu import (
    show_achievements
)

print("===================")
print(" MMORPG V2 ")
print("===================")

name = input("Enter Name: ")

print("\nAvailable Jobs")
print("Warrior")
print("Mage")
print("Archer")
print("Assassin")
print("Priest")

job = input("\nChoose Job: ").title()

player = Player(name, job)
player.check_skill_unlocks()

while True:

    print("\n===================")
    print("1. Show Stats")
    print("2. Hunt Monster")
    print("3. Inventory")
    print("4. Use Potion")
    print("5. Equipment")
    print("6. Skills")
    print("7. Town")
    print("8. Shop")
    print("9. Quests")
    print("10. Claim Rewards")
    print("11. Save Game")
    print("12. Load Game")
    print("13. Tower")
    print("14. Passives")
    print("15. Boss Raid")
    print("16. Dungeons")
    print("17. Pets")
    print("18. Mounts")
    print("19. World Boss")
    print("20. Blacksmith")
    print("21. Alchemy")
    print("22. Upgrade Equipment")
    print("23. Gem System")
    print("24. Guild")
    print("25. World Map")
    print("26. NPC")
    print("27. Story Quest")
    print("28. Achievements")
    print("29. Exit")
    print("===================")

    choice = input("Choice: ")

    # =====================
    # SHOW STATS
    # =====================

    if choice == "1":

        player.show_stats()

    # =====================
    # HUNT MONSTER
    # =====================

    elif choice == "2":

        monster = get_monster()

        battle(player, monster)

    # =====================
    # INVENTORY
    # =====================

    elif choice == "3":

        show_inventory(player)

    # =====================
    # USE POTION
    # =====================

    elif choice == "4":

        use_potion(player)

    # =====================
    # EQUIPMENT
    # =====================

    elif choice == "5":

        show_equipment(player)

        print("\nEquip Options")
        print("1. Iron Sword")
        print("2. Steel Sword")
        print("3. Leather Armor")
        print("4. Back")

        equip_choice = input("Choice: ")

        if equip_choice == "1":

            equip_item(
                player,
                "Iron Sword"
            )

        elif equip_choice == "2":

            equip_item(
                player,
                "Steel Sword"
            )

        elif equip_choice == "3":

            equip_item(
                player,
                "Leather Armor"
            )

    # =====================
    # SKILLS
    # =====================

    elif choice == "6":

        show_skills(player)

        input(
            "\nPress Enter To Continue..."
        )

    # =====================
    # TOWN
    # =====================

    elif choice == "7":

        town_menu(player)

    # =====================
    # SHOP
    # =====================

    elif choice == "8":

        print("\n===== SHOP =====")
        print("1. Buy")
        print("2. Sell")
        print("3. Back")

        shop_choice = input(
            "Choice: "
        )

        if shop_choice == "1":

            buy_item(player)

        elif shop_choice == "2":

            sell_item(player)

    # =====================
    # QUESTS
    # =====================

    elif choice == "9":

        show_quests(player)

    # =====================
    # CLAIM REWARDS
    # =====================

    elif choice == "10":

        claim_rewards(player)

    # =====================
    # SAVE
    # =====================

    elif choice == "11":

        save_player(player)

    # =====================
    # LOAD
    # =====================

    elif choice == "12":

        load_player(player)
    elif choice == "13":

        tower_menu(player)

    elif choice == "14":

        show_passives(
            player
        )
    
    elif choice == "15":

       boss_menu(player)
    
    elif choice == "16":

      dungeon_menu(player)

    elif choice == "17":

     while True:

        print("\n===== PET MENU =====")

        print("1. Adopt Pet")
        print("2. View Pet")
        print("3. Back")

        pet_choice = input("Choice: ")

        if pet_choice == "1":

            adopt_pet(player)

        elif pet_choice == "2":

            show_pet(player)

        elif pet_choice == "3":

            break
    
    elif choice == "18":

     while True:

        print("\n===== MOUNT MENU =====")

        print("1. Adopt Mount")
        print("2. View Mount")
        print("3. Back")

        mount_choice = input(
            "Choice: "
        )

        if mount_choice == "1":

            adopt_mount(player)

        elif mount_choice == "2":

            show_mount(player)

        elif mount_choice == "3":

            break

    elif choice == "19":

        world_boss_menu(
            player
        )
    
    elif choice == "20":

     blacksmith_menu(
        player
    )
    elif choice == "21":

     alchemy_menu(
        player
    )
     
    elif choice == "22":

     upgrade_menu(
        player
    )
     
    elif choice == "23":

     gem_menu(player)

    elif choice == "24":

     guild_menu(
        player
    )
     
    elif choice == "25":

     world_map_menu(
        player
    )

    elif choice == "26":

     npc_menu(
        player
    )

    elif choice == "27":

     story_quest_menu(
        player
    )
     
    elif choice == "30":

     show_achievements(
        player
    )


    elif choice == "28":

     print("\nGoodbye!")
    break

else:

        print("\nInvalid Choice!")