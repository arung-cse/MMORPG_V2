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
from quests import show_quests
from save_system import (
    save_player,
    load_player
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

while True:

    print("\n===================")
    print("1. Show Stats")
    print("2. Hunt Monster")
    print("3. Inventory")
    print("4. Use Potion")
    print("5. Equipment")
    print("6. Skills")
    print("7. Quests")
    print("8. Save Game")
    print("9. Load Game")
    print("10. Exit")
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

        show_quests(player)

    elif choice == "8":

        save_player(player)

    elif choice == "9":

        load_player(player)

    elif choice == "10":

        print("\nGoodbye!")
        break

    else:

        print("\nInvalid Choice!")