from jobs import JOBS


class Player:

    def __init__(self, name, job):

        self.name = name
        self.job = job

        self.level = 1
        self.exp = 0
        self.gold = 100

        self.max_hp = 100
        self.hp = 100

        self.max_mp = 50
        self.mp = 50

        self.attack = 10
        self.defense = 5

        self.critical = 5

        self.weapon = "None"
        self.armor = "None"
        self.accessory = "None"

        self.inventory = {
            "Health Potion": 3,
            "Mana Potion": 2
        }

        self.quest_progress = {
            "Goblin": 0,
            "Wolf": 0,
            "Skeleton": 0,
            "Orc": 0
        }
        self.completed_quests = []

        self.learned_skills = []

        self.setup_job()

    # ==========================
    # JOB SETUP
    # ==========================

    def setup_job(self):

    # Convert input to proper format

     self.job = self.job.title()

     if self.job not in JOBS:

         self.job = "Novice"

     data = JOBS[self.job]

     self.max_hp = data["hp"]
     self.hp = self.max_hp

     self.max_mp = data["mp"]
     self.mp = self.max_mp

     self.attack = data["attack"]
     self.defense = data["defense"]

    # ==========================
    # SHOW STATS
    # ==========================

    def show_stats(self):

        print("\n====================")
        print(" PLAYER INFORMATION ")
        print("====================")

        print("Name      :", self.name)
        print("Job       :", self.job)

        print("Level     :", self.level)
        print("EXP       :", self.exp)

        print("Gold      :", self.gold)

        print("HP        :", self.hp, "/", self.max_hp)
        print("MP        :", self.mp, "/", self.max_mp)

        print("Attack    :", self.attack)
        print("Defense   :", self.defense)

        print("Critical  :", str(self.critical) + "%")

        print("Weapon    :", self.weapon)
        print("Armor     :", self.armor)
        print("Accessory :", self.accessory)

    # ==========================
    # EXP
    # ==========================

    def gain_exp(self, amount):

        self.exp += amount

        print(f"\n+{amount} EXP")

        while self.exp >= 100:

            self.exp -= 100

            self.level += 1

            self.check_skill_unlocks()

            self.max_hp += 20
            self.max_mp += 10

            self.attack += 5
            self.defense += 2

            self.hp = self.max_hp
            self.mp = self.max_mp

            print("\nLEVEL UP!")
            print("Level:", self.level)

    # ==========================
    # GOLD
    # ==========================

    def gain_gold(self, amount):

        self.gold += amount

    # ==========================
    # HEAL
    # ==========================

    def heal(self, amount):

        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    # ==========================
    # DAMAGE
    # ==========================

    def take_damage(self, damage):

        damage -= self.defense

        if damage < 1:
            damage = 1

        self.hp -= damage

        if self.hp < 0:
            self.hp = 0
    
    def check_skill_unlocks(self):

       from skill_tree import SKILL_TREE

       if self.job not in SKILL_TREE:
            return

       for level, skills in SKILL_TREE[self.job].items():

           if self.level >= level:

              for skill in skills:

                if skill not in self.learned_skills:

                    self.learned_skills.append(skill)

                    print(
                        "\nNEW SKILL UNLOCKED:",
                        skill
                    )

    # ==========================
    # DEAD CHECK
    # ==========================

    def is_dead(self):

        return self.hp <= 0