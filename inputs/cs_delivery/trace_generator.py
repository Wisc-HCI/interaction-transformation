import numpy as np

from interaction_components import *

class TraceGenerator:

    def __init__(self, TS):
        self.TS = TS
        print(self.TS)

        self.prob_ready = 0.4

    def get_trajectories(self, n):
        trajs = []

        for i in range(n):
            traj = []
            traj_score = -1
            traj.append((HumanInput("Ready"), Microinteraction(self.TS.init.micros[0]["name"], 0)))

            handoff_exists = False
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

                if trans.target.micros[0]["name"] == "Handoff":
                    handoff_exists = True
                traj.append((HumanInput(selection), Microinteraction(trans.target.micros[0]["name"], 0)))

            score = np.random.random()
            if handoff_exists:
                score -= 1
            trajs.append(Trajectory(traj,score))
        return trajs
