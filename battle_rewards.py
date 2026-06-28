def give_rewards(player, monster):

    reward_exp = monster.get("exp", 0)
    reward_gold = monster.get("gold", 0)

    if hasattr(player, "mount") and player.mount:

        from mount_data import MOUNTS

        bonus = MOUNTS[player.mount]["exp_bonus"]

        reward_exp += reward_exp * bonus // 100

    player.gain_exp(reward_exp)
    player.gain_gold(reward_gold)

    print(f"+ {reward_exp} EXP")
    print(f"+ {reward_gold} Gold")