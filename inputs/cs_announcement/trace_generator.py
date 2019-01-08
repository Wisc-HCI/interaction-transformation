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

            violation1 = False
            violation25 = False
            violation34 = False
            for i in range(len(traj)):
                if i < len(traj)-1 and traj[i][1].type == "Remark" and traj[i+1][0].type == "Ignore" and traj[i+1][1].type == "Remark":
                    violation1 = True

                if i < len(traj)-1 and traj[i][1].type == "Remark" and traj[i+1][0].type == "Ready":
                    for j in range(i+1, len(traj)):
                        if traj[j][1].type == "Remark":
                            violation2 = True

                if i < len(traj)-1 and traj[i][1].type == "Remark" and traj[i+1][0].type == "Ignore":
                    exists = False
                    for j in range(i+1, len(traj)):
                        if traj[j][1].type == "Remark":
                            exists = True
                    if not exists:
                        violation3 = True

            if violation1:
                score -= 0.25
            if violation25:
                score -= 0.25
            elif not violation1:
                score += 0.25
            if violation34:
                score -= 0.25
            elif not violation25 and not violation1:
                score += 0.25

            score = min(max(-1,score),1)

            trajs.append(Trajectory(traj,score))
        return trajs
