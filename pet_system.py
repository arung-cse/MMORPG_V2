from pet_data import PETS

def adopt_pet(player):

    if hasattr(player, "pet"):

        print("\nYou already have a pet!")

        return

    print("\n===== PET SHOP =====")

    pet_list = list(PETS.keys())

    for i, pet in enumerate(pet_list):

        print(f"{i+1}. {pet}")

    choice = input("Choose Pet: ")

    try:

        pet_name = pet_list[int(choice)-1]

    except:

        print("Invalid Choice!")

        return

    player.pet = pet_name

    print(
        "\nYou adopted:",
        pet_name
    )


def show_pet(player):

    print("\n===== PET =====")

    if not hasattr(player, "pet"):

        print("No Pet")

        return

    pet = PETS[player.pet]

    print("Name:", player.pet)

    print("Attack Bonus:", pet["attack"])

    print("HP Bonus:", pet["hp"])