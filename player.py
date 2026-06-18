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

    def show_stats(self):

        print("\n===== PLAYER =====")

        print("Name :", self.name)
        print("Job  :", self.job)

        print("Level:", self.level)

        print("HP   :", self.hp, "/", self.max_hp)

        print("Gold :", self.gold)