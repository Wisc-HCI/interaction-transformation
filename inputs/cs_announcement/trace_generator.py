import numpy as np

from interaction_components import *

class TraceGenerator:

    def __init__(self, TS):
        self.TS = TS
        print(self.TS)

        self.prob_ready = 0.2

    def get_trajectories(self, n):
        trajs = []

        # behavioral rules:
        # 1) probability of ignoring robot is initially high
        # 2) after every remark, probability decreases

        # experience rules:
        # 1) if multiple announcements in a row, experience
        # 2) if the person misses the announcement, then bad

        for i in range(n):
            traj = []
            traj_score = -1
            traj.append((HumanInput("Ready"), Microinteraction(self.TS.init.micros[0]["name"], 0)))

            curr_state = self.TS.init
            curr_prob_ready = 0.2
            speech_1 = False
            speech_2 = False

            missed_announcement = False
            made_up_missed_announcement = False
            while True:
                if curr_state.name == "Greet" or curr_state.name == "Announcement":
                    curr_prob_ready = min(1.0, curr_prob_ready + np.random.uniform(0.1,0.3))

                    if speech_1:
                        speech_2 = True
                    speech_1 = True
                else:
                    speech_1 = False

                options = curr_state.out_trans

                if len(options) == 0:
                    break
                conditions = ["Ready", "Ignore"]

                selection = np.random.choice(conditions, p=[curr_prob_ready, 1-curr_prob_ready])
                if curr_state.name == "Announcement" and selection == "Ignore":
                    missed_announcement = True
                if missed_announcement and curr_state.name == "Announcement" and selection == "Ready":
                    made_up_missed_announcement = True
                trans = None
                for option in options:
                    if option.condition == selection:
                        trans = option
                        curr_state = option.target
                        break

                if trans is not None:
                    traj.append((HumanInput(selection), Microinteraction(trans.target.micros[0]["name"], 0)))

            if not speech_2 and not (missed_announcement and not made_up_missed_announcement):
                score = np.random.random()*2 - 1
            else:
                score = np.random.random()-1

            trajs.append(Trajectory(traj,score,False,False))
        return trajs
