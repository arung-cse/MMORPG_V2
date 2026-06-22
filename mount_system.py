from mount_data import MOUNTS


def adopt_mount(player):

    if player.mount:

        print("\nYou already have a mount!")
        return

    print("\n===== MOUNTS =====")

    mount_list = list(MOUNTS.keys())

    for i, mount in enumerate(mount_list):

        print(f"{i+1}. {mount}")

    choice = input("Choose Mount: ")

    try:

        player.mount = mount_list[
            int(choice)-1
        ]

        print(
            "\nMounted:",
            player.mount
        )

    except:

        print("Invalid Choice!")


def show_mount(player):

    print("\n===== MOUNT =====")

    if not player.mount:

        print("No Mount")
        return

    data = MOUNTS[player.mount]

    print("Mount:", player.mount)

    print(
        "Speed Bonus:",
        data["speed"]
    )

    print(
        "EXP Bonus:",
        data["exp_bonus"],
        "%"
    )

    print(
        "Gold Bonus:",
        data["gold_bonus"],
        "%"
    )