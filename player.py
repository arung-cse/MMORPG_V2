from jobs import JOBS
from passive_system import check_passive_unlocks


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

        self.weapon_level = 0
        self.armor_level = 0

        self.weapon_gems = []
        self.armor_gems = []

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

        self.learned_passives = []

        self.pet = None

        self.mount = None

        self.setup_job()
        self.max_level = 1000

        self.guild = None

        self.current_area = "Beginner Village"

        self.total_kills = 0
        self.boss_kills = 0
        self.dungeons_cleared = 0

        self.completed_achievements = []
        
        self.arena_rank = 0

        self.title = "None"
        self.unlocked_titles = []

        # Equipment Upgrade Levels
        self.weapon_upgrade = 0
        self.armor_upgrade = 0
        self.accessory_upgrade = 0

        self.status_effects = {}

        self.weapon_enchant = None
        self.armor_enchant = None
        self.accessory_enchant = None

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

       while (
        self.exp >= self.exp_needed()
        and self.level < 1000
    ):

        self.exp -= self.exp_needed()

        self.level += 1

        from advancement_system import (
            check_job_advancement
    )

        check_job_advancement(self)

        self.check_skill_unlocks()

        from passive_system import (

            check_passive_unlocks

        )

        check_passive_unlocks(

             self

       )

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
    def exp_needed(self):

        return self.level * 100
    