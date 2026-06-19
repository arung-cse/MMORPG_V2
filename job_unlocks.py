JOB_UNLOCKS = {

# =====================================
# BASIC JOBS
# =====================================

"Warrior": {
    "level": 1
},

"Mage": {
    "level": 1
},

"Archer": {
    "level": 1
},

"Assassin": {
    "level": 1
},

"Priest": {
    "level": 1
},

# =====================================
# ADVANCED WARRIOR
# =====================================

"Knight": {
    "level": 10,
    "required_job": "Warrior"
},

"Swordmaster": {
    "level": 20,
    "required_job": "Warrior"
},

"Berserker": {
    "level": 25,
    "required_job": "Warrior"
},

"Blade Dancer": {
    "level": 30,
    "required_job": "Swordmaster"
},

"Weapon Master": {
    "level": 40,
    "required_job": "Knight"
},

"Sword Saint": {
    "level": 50,
    "required_job": "Weapon Master"
},

"Dragon Knight": {
    "level": 60,
    "boss_kills": 25,
    "required_job": "Sword Saint"
},

"Death Knight": {
    "level": 70,
    "boss_kills": 50,
    "required_job": "Dragon Knight"
},

"God Of War": {
    "level": 100,
    "tower_floor": 50,
    "required_job": "Death Knight"
},

# =====================================
# MAGE
# =====================================

"Wizard": {
    "level": 10,
    "required_job": "Mage"
},

"Elementalist": {
    "level": 20,
    "required_job": "Wizard"
},

"Archmage": {
    "level": 35,
    "required_job": "Elementalist"
},

"Rune Mage": {
    "level": 50,
    "required_job": "Archmage"
},

"Time Mage": {
    "level": 60,
    "required_job": "Rune Mage"
},

"Space Mage": {
    "level": 70,
    "required_job": "Time Mage"
},

"Chaos Mage": {
    "level": 85,
    "required_job": "Space Mage"
},

"World Breaker": {
    "level": 100,
    "tower_floor": 60,
    "required_job": "Chaos Mage"
},

# =====================================
# ASSASSIN
# =====================================

"Shadow Assassin": {
    "level": 20,
    "required_job": "Assassin"
},

"Phantom Assassin": {
    "level": 35,
    "required_job": "Shadow Assassin"
},

"Blood Assassin": {
    "level": 50,
    "required_job": "Phantom Assassin"
},

"Void Assassin": {
    "level": 70,
    "required_job": "Blood Assassin"
},

"God Slayer": {
    "level": 90,
    "boss_kills": 50,
    "required_job": "Void Assassin"
},

"Shadow Monarch": {
    "level": 100,
    "tower_floor": 75,
    "required_job": "God Slayer"
},

# =====================================
# ARCHER
# =====================================

"Ranger": {
    "level": 10,
    "required_job": "Archer"
},

"Sniper": {
    "level": 25,
    "required_job": "Ranger"
},

"Wind Archer": {
    "level": 40,
    "required_job": "Sniper"
},

"Shadow Archer": {
    "level": 55,
    "required_job": "Wind Archer"
},

"Dragon Archer": {
    "level": 75,
    "required_job": "Shadow Archer"
},

"Divine Marksman": {
    "level": 100,
    "tower_floor": 70,
    "required_job": "Dragon Archer"
},

# =====================================
# PRIEST
# =====================================

"Cleric": {
    "level": 10,
    "required_job": "Priest"
},

"Bishop": {
    "level": 25,
    "required_job": "Cleric"
},

"Saint": {
    "level": 50,
    "required_job": "Bishop"
},

"Archangel": {
    "level": 100,
    "tower_floor": 80,
    "required_job": "Saint"
},

# =====================================
# GODHOOD
# =====================================

"Demigod": {
    "level": 120,
    "tower_floor": 90
},

"True God": {
    "level": 140,
    "tower_floor": 100
},

"Ancient God": {
    "level": 160,
    "tower_floor": 120
},

"Celestial God": {
    "level": 180,
    "tower_floor": 150
},

"Void God": {
    "level": 200,
    "tower_floor": 180
},

"Chaos God": {
    "level": 250,
    "tower_floor": 220
},

"Origin God": {
    "level": 300,
    "tower_floor": 250
},

"God King": {
    "level": 350,
    "tower_floor": 300
},

"Supreme God": {
    "level": 400,
    "tower_floor": 350
},

"King Of Gods": {
    "level": 500,
    "tower_floor": 400
},

# =====================================
# FINAL EXISTENCE
# =====================================

"Reality King": {
    "level": 600,
    "tower_floor": 500
},

"Dimension Emperor": {
    "level": 700,
    "tower_floor": 600
},

"Eternal Sovereign": {
    "level": 850,
    "tower_floor": 800
},

"Creator Of All": {
    "level": 1000,
    "tower_floor": 1000
}

}

def can_unlock(player, job_name):

    if job_name not in JOB_UNLOCKS:
        return False

    requirements = JOB_UNLOCKS[job_name]

    if player.level < requirements.get("level", 1):
        return False

    if hasattr(player, "tower_floor"):

        if player.tower_floor < requirements.get("tower_floor", 0):
            return False

    if hasattr(player, "boss_kills"):

        if player.boss_kills < requirements.get("boss_kills", 0):
            return False

    return True