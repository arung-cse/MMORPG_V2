import random
from pet_data import PETS


def normal_attack(player):

    pet_bonus = 0

    if hasattr(player, "pet") and player.pet:

        pet_bonus = PETS[player.pet]["attack"]

    damage = random.randint(

        player.attack + pet_bonus - 3,

        player.attack + pet_bonus + 3

    )

    return max(1, damage)