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

from town import town_menu

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
    print("13. Exit")
    print("===================")

    choice = input("Choice: ")

    if choice == "1":

        player.show_stats()

    elif choice == "2":

        monster = get_monster()

        battle(player, monster)

    elif choice == "3":

        show_inventory(player)

    elif choice == "4":

        use_potion(player)

    elif choice == "5":

        show_equipment(player)

        print("\nEquip Options")
        print("1. Iron Sword")
        print("2. Steel Sword")
        print("3. Leather Armor")
        print("4. Back")

        equip_choice = input("Choice: ")

        if equip_choice == "1":
            equip_item(player, "Iron Sword")

        elif equip_choice == "2":
            equip_item(player, "Steel Sword")

        elif equip_choice == "3":
            equip_item(player, "Leather Armor")
    
    elif choice == "6":

        from skills import show_skills

        show_skills(player)
    
    elif choice == "7":

        town_menu(player)

    elif choice == "8":

        print("\n===== SHOP =====")
        print("1. Buy")
        print("2. Sell")

    shop_choice = input(
        "Choice: "
    )

    if shop_choice == "1":

        buy_item(player)

    elif shop_choice == "2":

        sell_item(player)

    elif choice == "9":

        show_quests(player)
    
    elif choice == "10":

        claim_rewards(player)

    elif choice == "11":

        save_player(player)

    elif choice == "12":

        load_player(player)

    elif choice == "13":

        print("\nGoodbye!")
        break

    else:

        print("\nInvalid Choice!")