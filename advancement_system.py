from job_advancement import JOB_ADVANCEMENTS
from jobs import JOBS

def check_job_advancement(player):

    if player.job not in JOB_ADVANCEMENTS:
        return

    for level, new_job in JOB_ADVANCEMENTS[player.job].items():

        if player.level >= level:

            if player.job != new_job:

                print(
                    "\nJOB ADVANCED!"
                )

                print(
                    player.job,
                    "->",
                    new_job
                )

                player.job = new_job

                data = JOBS[new_job]

                player.max_hp = data["hp"]
                player.max_mp = data["mp"]

                player.attack = data["attack"]
                player.defense = data["defense"]

                player.hp = player.max_hp
                player.mp = player.max_mp