class Player:

    def __init__(self, name, job):

        self.name = name
        self.job = job

        self.level = 1
        self.exp = 0
        self.gold = 100

        self.max_hp = 100
        self.hp = 100

        self.attack = 10

        self.weapon = "None"
        self.armor = "None"

        self.inventory = {
            "Health Potion": 3
        }

    def show_stats(self):

        print("\n===== PLAYER =====")

        print("Name :", self.name)
        print("Job  :", self.job)

        print("Level:", self.level)

        print("HP   :", self.hp, "/", self.max_hp)

        print("EXP  :", self.exp)

        print("Gold :", self.gold)

    def gain_exp(self, amount):

        self.exp += amount

        while self.exp >= 100:

            self.exp -= 100

            self.level += 1

            self.max_hp += 20
            self.attack += 5

            self.hp = self.max_hp

            print("\nLEVEL UP!")
            print("Level:", self.level)