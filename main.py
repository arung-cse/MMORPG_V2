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
from save_system import (
    save_player,
    load_player
)

print("===================")
print(" MMORPG V2 ")
print("===================")

name = input("Enter Name: ")
job = input("Choose Job: ")

player = Player(name, job)

while True:

    print("\n===================")
    print("1. Show Stats")
    print("2. Hunt Monster")
    print("3. Inventory")
    print("4. Use Potion")
    print("5. Equipment")
    print("6. Save Game")
    print("7. Load Game")
    print("8. Exit")
    print("===================")

    choice = input("Choice: ")

    if choice == "1":

        player.show_stats()

    elif choice == "2":

        monster = get_monster()

        battle(
            player,
            monster
        )

    elif choice == "3":

        show_inventory(player)

    elif choice == "4":

        use_potion(player)

    elif choice == "5":

        show_equipment(player)

    elif choice == "6":

        save_player(player)

    elif choice == "7":

        load_player(player)

    elif choice == "8":

        print("\nGoodbye!")
        break

    else:

        print("\nInvalid Choice!")