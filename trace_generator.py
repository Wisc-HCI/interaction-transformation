import numpy as np

from interaction_components import *

class TraceGenerator:

    def __init__(self, TS):
        self.TS = TS
        print(self.TS)

        self.prob_ready = 0.3
        decay1 = 0.95
        decay2 = 0.05

    def get_trajectories(self, n):
        trajs = []

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

                traj.append((HumanInput(selection), Microinteraction(trans.target.micros[0]["name"], 0)))

            score = min(1, max(-1, 0.95**len(traj) - 0.05*len(traj)))
            trajs.append(Trajectory(traj,score))

        return trajs
