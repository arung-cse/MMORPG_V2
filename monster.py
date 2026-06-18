import random

monsters = [

    {
        "name":"Goblin",
        "hp":50,
        "attack":5,
        "exp":25,
        "gold":10
    },

    {
        "name":"Wolf",
        "hp":80,
        "attack":10,
        "exp":40,
        "gold":20
    },

    {
        "name":"Skeleton",
        "hp":120,
        "attack":15,
        "exp":60,
        "gold":30
    },

    {
        "name":"Orc",
        "hp":200,
        "attack":25,
        "exp":100,
        "gold":50
    }

]

def get_monster():

    return random.choice(monsters)