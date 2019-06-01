import numpy as np

from interaction_components import *

class TraceGenerator:

    def __init__(self, TS, inps, outs, sampler):
        self.TS = TS
        self.inputs = inps
        self.outputs = outs

        self.prob_ready = 0.6
        self.Sampler = sampler.Sampler


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
                #print(curr_state.name)
                options = curr_state.out_trans
                conditions = ["Ready", "Ignore"]

                if len(options) == 0:
                    #print("options are 0")
                    selection = np.random.choice(conditions, p=[self.prob_ready, 1-self.prob_ready])
                    end_micro = "END"
                    traj.append((HumanInput(selection), Microinteraction(end_micro, 0)))
                    break
                elif len(options) < 2:
                    selection = np.random.choice(conditions, p=[self.prob_ready, 1-self.prob_ready])
                    #print("options less than 2")
                    r = False
                    i = False
                    for option in options:
                        if option.condition == "Ready":
                            r = True
                        elif option.condition == "Ignore":
                            i = True
                    if selection == "Ready" and not r:
                        end_micro = "END"
                        traj.append((HumanInput(selection), Microinteraction(end_micro, 0)))
                        break
                    elif selection == "Ignore" and not i:
                        end_micro = "END"
                        traj.append((HumanInput(selection), Microinteraction(end_micro, 0)))
                        break
                else:
                    #print("else")
                    selection = np.random.choice(conditions, p=[self.prob_ready, 1-self.prob_ready])

                #print(selection)
                trans = None
                for option in options:
                    if option.condition == selection:
                        trans = option
                        curr_state = option.target
                        break

                if trans is not None:
                    traj.append((HumanInput(selection), Microinteraction(trans.target.micros[0]["name"], 0)))

            # attempt to score the interaction
            # hello -> goodbye is good
            '''
            if traj[0][1].type == "Greet" and traj[1][1].type == "Bye":
                score = 1
            else:
                score = np.random.random() - 0.5
            '''

            # shorter is better
            '''
            if len(traj) < 7:
                score = 1
            else:
                score = -1
            '''

            # Things are good UNLESS did not get that is involved
            dngt = False
            for comp in traj:
                if comp[1].type == "DidNotGetThat":
                    dngt = True

            if dngt:
                score = -1
            else:
                score = 1

            # completely random
            #score = np.random.random() - 0.5

            trajs.append(Trajectory(traj,score,False))

        '''
        Testing the sampler
        sampler = self.Sampler(trajs, 2, self.inputs, self.outputs)
        sampler.solve()
        exit()
        '''

        return trajs
