from world_map_data import WORLD_AREAS


def world_map_menu(player):

    while True:

        print("\n===== WORLD MAP =====")

        areas = list(
            WORLD_AREAS.keys()
        )

        for i, area in enumerate(areas):

            print(
                f"{i+1}. {area}"
            )

        print("0. Exit")

        choice = input(
            "Choice: "
        )

        if choice == "0":

            return

        try:

            area = areas[
                int(choice)-1
            ]

        except:

            print("Invalid Choice!")
            continue

        required = WORLD_AREAS[
            area
        ]["required_level"]

        if player.level < required:

            print(
                "\nRequired Level:",
                required
            )

            continue

        player.current_area = area

        print(
            "\nTravelled To:",
            area
        )