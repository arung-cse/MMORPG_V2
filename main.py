from player import Player

print("=== MMORPG V2 ===")

name = input("Enter Name: ")
job = input("Choose Job: ")

player = Player(name, job)

while True:

    print("\n===== MENU =====")

    print("1. Show Stats")
    print("2. Exit")

    choice = input("Choice: ")

    if choice == "1":

        player.show_stats()

    elif choice == "2":

        print("Goodbye!")

        break