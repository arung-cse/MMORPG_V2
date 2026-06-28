from status_data import STATUS_EFFECTS


def apply_status(player, status):

    if status not in STATUS_EFFECTS:

        return

    player.status_effects[status] = STATUS_EFFECTS[status]["duration"]

    print(f"\n{status} applied!")

def process_status(player):

    remove = []

    for status in player.status_effects:

        player.status_effects[status] -= 1

        if status == "Burn":

            damage = max(
                1,
                player.max_hp * 5 // 100
            )

            player.take_damage(damage)

            print(
                "Burn dealt",
                damage,
                "damage!"
            )

        elif status == "Poison":

            damage = max(
                1,
                player.max_hp * 3 // 100
            )

            player.take_damage(damage)

            print(
                "Poison dealt",
                damage,
                "damage!"
            )

        if player.status_effects[status] <= 0:

            remove.append(status)

    for status in remove:

        del player.status_effects[status]

        print(status, "wore off.")