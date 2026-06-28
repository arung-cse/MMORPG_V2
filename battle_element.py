from element_data import ELEMENTS


def element_bonus(
    damage,
    attack_element,
    target_element
):

    if attack_element is None:

        return damage

    if target_element in ELEMENTS[attack_element]["strong"]:

        print("Element Advantage!")

        return int(damage*1.5)

    if target_element in ELEMENTS[attack_element]["weak"]:

        print("Element Resistant!")

        return int(damage*0.5)

    return damage