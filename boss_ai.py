def boss_phase(monster):

    max_hp = monster["hp"]

    current_hp = monster["current_hp"]

    percent = current_hp * 100 // max_hp

    # =========================
    # Phase 2
    # =========================

    if percent <= 75 and not monster["phase2"]:

        monster["phase2"] = True

        print("\n★★★★★ PHASE 2 ★★★★★")

        monster["attack"] += 200

    # =========================
    # Phase 3
    # =========================

    if percent <= 50 and not monster["phase3"]:

        monster["phase3"] = True

        print("\n★★★★★ PHASE 3 ★★★★★")

        monster["attack"] += 300

    # =========================
    # Enrage
    # =========================

    if percent <= 25 and not monster["enraged"]:

        monster["enraged"] = True

        print("\n★★★★★ ENRAGED ★★★★★")

        monster["attack"] += 500