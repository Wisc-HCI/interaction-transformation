import numpy as np

from interaction_components import *

class TraceGenerator:

    def __init__(self, TS):
        self.TS = TS
        print(self.TS)

        self.prob_ready = 0.6

    def get_trajectories(self, n):
        trajs = []

        # rules:
        # 1) 2+ announcements in a row after ignoring one of the announcements is bad
        # 2) announcements that come after already acknowledging an announcement is bad
        # 3) the robot leaving after announcing and being ignored is bad
        # 4) making an annoucement, being ignored, and then waiting to make another announcement is good
        # 5) making an announcement, acknowledging it, and the the interaction ending is good
        # 6) everything else is pretty neutral

        for i in range(n):
            traj = []
            traj_score = -1
            traj.append((HumanInput("Ready"), Microinteraction(self.TS.init.micros[0]["name"], 0)))

            curr_state = self.TS.init
            while True:
                options = curr_state.out_trans

                if len(options) == 0:
                    break
                conditions = ["Ready", "Ignore"]

                selection = np.random.choice(conditions, p=[self.prob_ready, 1-self.prob_ready])
                trans = None
                for option in options:
                    if option.condition == selection:
                        trans = option
                        curr_state = option.target
                        break

                if trans is not None:
                    traj.append((HumanInput(selection), Microinteraction(trans.target.micros[0]["name"], 0)))

            score = np.random.random() - 0.5

            trajs.append(Trajectory(traj,score))
        return trajs
