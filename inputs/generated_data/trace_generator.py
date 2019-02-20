import numpy as np
from collections import Counter
from interaction_components import *

class TraceGenerator:

    def __init__(self, TS):
        self.TS = TS
        print(self.TS)

        self.prob_ready = 0.6

    def get_trajectories(self, n):
        trajs = []

        for i in range(n):
            traj = []
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

            score = self.score_calculator(traj)
            print("score: ", score)

            trajs.append(Trajectory(traj, score))
        return trajs

    """Assigns scores to traj based on the set rules. Each rules has a 
    certain scores. The final scores will be the total scores normalized to 
    -1, 0, 1 based on set interval of scores
    
    rules:
        - >=1 Did_not_get_that (-2).    >=3 Did_not_get_that (-5)
        - >=1 IgnoreGreet (-2) >=2 IgnoreGreet (-3).   >=3 Greet (-5)
        - >=2 Ignore-Need more help (-2)
        - The robot farewell after do not need any more help (+1)
        - how help-answer question (+2)
        - more help-how help-answer question (+2)
    """
    def score_calculator(self, traj):
        points = 0
        points_max = 5
        points_min = -12
        range_points = points_max - points_min
        criteria_lower_bound = points_min/5
        criteria_upper_bound = points_max/4

        # print(type(traj[0][0].get()))
        # print("\n\n{}".format(traj[0][1].get())) #[human input][
        # # microinteraction]
        # print("\n\n{}".format(Trajectory(traj, 0)))

        traj = [t[0].get()+t[1].get() for t in traj]
        for t in traj:
            print (t)
        occurrence = Counter(traj)
        print(occurrence)

        # >=1 Did_not_get_that (-2).    >=3 Did_not_get_that (-5)
        if "IgnoreDidNotGetThat" in occurrence.keys():
            if 1 <= occurrence.get("IgnoreDidNotGetThat") < 3:
                points -= 2
            elif 3 <= occurrence.get("IgnoreDidNotGetThat"):
                points -= 5

        # >=1 IgnoreGreet (-2) >=2 IgnoreGreet (-3).   >=3 Greet (-5)
        if "IgnoreGreet" in occurrence.keys():
            if 1 <= occurrence.get("IgnoreGreet") < 2:
                points -= 2
            elif 2 <= occurrence.get("IgnoreGreet") < 3:
                points -= 3
            elif 3 <= occurrence.get("IgnoreGreet"):
                points -= 5

        # >=2 Need more help (-2)
        if "IgnoreNeedMoreHelp" in occurrence.keys():
            if 2 <= occurrence.get("IgnoreNeedMoreHelp"):
                points -= 2

        # The robot farewell after do not need any more help (+1)
        # how help-answer question (+2)
        # more help-how help-answer question (+2)
        flag_farewell = True
        flag_query_first = True
        flag_query_second = True
        for i in range(len(traj)):
            if flag_farewell and traj[i] == "IgnoreBye" and "NeedMoreHelp" in \
                    traj[i-1]:
                points += 1
                flag_farewell = False
            if flag_query_first and traj[i] == "ReadyCompleteQuery" and \
                    "HowHelp" in traj[i-1]:
                points += 2
                flag_query_first = False
            if (not flag_query_first) and flag_query_second and traj[i] == \
                    "ReadyCompleteQuery" and "HowHelp" in traj[i-1]:
                points += 2
                flag_query_second = False

        print("points: ", points)
        if points < criteria_lower_bound:
            score = -1
        elif criteria_lower_bound <= points < criteria_upper_bound:
            score = 0
        else:
            score = 1

        return score
