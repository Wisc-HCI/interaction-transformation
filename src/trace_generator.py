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

            while True:
                leave_val = np.random.random()
                if leave_val <= self.leave_early_prob:
                    is_prefix = True
                    break

                if traj[-1][1].type == "DidYouSay":
                    request_info_val = np.random.random()
                    if request_info_val > 0.4:
                        selection = "Affirm"
                    else:
                        selection = random.choice(list(self.inputs.keys()))
                else:
                    request_info_val = np.random.random()
                    if request_info_val > 0.6:
                        selection = "RequestInfo"
                    else:
                        selection = random.choice(list(self.inputs.keys()))
                available_trans = curr_state.out_trans
                trans = None
                for t in available_trans:
                    if t.condition == selection:
                        trans = t
                        curr_state = trans.target

                if trans is None:
                    break

                traj.append((HumanInput(selection), Microinteraction(trans.target.micros[0]["name"], 0)))

            traj.append((HumanInput("Ignore"),Microinteraction("END")))

            score = self.simple_score(traj,is_prefix)
            trajs.append(Trajectory(traj,score,is_prefix,is_correctness))
        return trajs

    def simple_score(self, traj_vect, is_prefix):
        '''
        basic scoring
        '''
        # presense of states
        contains_listout = False       # bad
        contains_didyousay = False     # bad
        contains_answer = False        # good

        # sequences of behaviors
        takes_initiative = False       # good -- robot takes initiative and ends interaction by itself

        i = 0
        while i < len(traj_vect):
            # presense of states
            if traj_vect[i][1].type == "ListOut":
                contains_listout = True
            if traj_vect[i][1].type == "AnswerQuestion":
                contains_answer = True
            if traj_vect[i][1].type == "DidYouSay":
                contains_didyousay = True

            # sequences of behaviors
            if traj_vect[i][1].type == "Farewell" and traj_vect[i][0].type != "Goodbye":
                takes_initiative = True
            i += 1

        # get average scores
        scores = []
        for i in range(0,1):
            score_count = [0,1,0]
            #score = np.random.normal(0.0,0.25)
            if contains_listout:
                score_count[0] += 2
            if contains_answer:
                score_count[2] += 2
            if contains_didyousay:
                score_count[0] += 1
            if takes_initiative:
                score_count[2] += 1
            if is_prefix:
                score_count[0] += 1

            score_count[1] = max(1,min(score_count[0],score_count[2]))
            summa = sum(score_count)
            p = [el*1.0/summa for el in score_count]
            score = np.random.choice([-1,0,1],p=p)
            scores.append(score)
        score = np.average(scores)

        return score
