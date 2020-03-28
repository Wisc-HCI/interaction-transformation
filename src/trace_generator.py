import numpy as np
import random

from interaction_components import *

class TraceGenerator:

    def __init__(self, TS,inputs):
        self.TS = TS
        self.inputs = inputs

        self.leave_early_prob = 0.2

    def get_trajectories(self, n):
        trajs = []

        for i in range(n):
            traj = []
            traj_score = -1
            traj.append((HumanInput("General"), Microinteraction(self.TS.init.micros[0]["name"], 0)))

            curr_state = self.TS.init

            is_prefix = False
            is_correctness = False
            score = 0.0

            '''
            basic scoring
            '''
            contains_listout = False

            while True:
                leave_val = np.random.random()
                if leave_val <= self.leave_early_prob:
                    is_prefix = True
                    break

                selection = random.choice(list(self.inputs.keys()))
                available_trans = curr_state.out_trans
                trans = None
                for t in available_trans:
                    if t.condition == selection:
                        trans = t
                        curr_state = trans.target

                if trans is None:
                    break

                if trans.target.micros[0]["name"] == "ListOut":
                    contains_listout = True
                traj.append((HumanInput(selection), Microinteraction(trans.target.micros[0]["name"], 0)))

            if not is_prefix:
                traj.append((HumanInput("Ignore"),Microinteraction("END")))

            score = np.random.random()
            if contains_listout:
                score = -1
            trajs.append(Trajectory(traj,score,is_prefix,is_correctness))
        return trajs
