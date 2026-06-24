from gem_system import socket_gem


def gem_menu(player):

    while True:

        print("\n===== GEM SYSTEM =====")

        print("1. Socket Gem")
        print("2. Back")

        choice = input("Choice: ")

        if choice == "1":

            socket_gem(player)

        elif choice == "2":

            break