class PathTraversal:

    def __init__(self, TS, trajectories, freqs):
        self.TS = TS
        self.trajectories = trajectories
        self.freqs = freqs

    def check(self):

        sats = []
        probs = []
        trajectory_status = {}
        for traj in self.trajectories:
            vect = traj.vect

            sat = True
            probability = 1
            if vect[0][1].type != self.TS.init.micros[0]["name"]:
                #print("unsat -- init")
                sat = False
                trajectory_status[traj] = 0
                continue

            curr_st = self.TS.init
            for i in range(1, len(vect)):
                inp = vect[i][0].type
                test_out = vect[i][1].type

                path_exists = False
                path_trans = None
                for trans in curr_st.out_trans:
                    if trans.condition == inp and trans.target.micros[0]["name"] == test_out:
                        path_exists = True
                        path_trans = trans
                        probability *= self.freqs.probs[curr_st.micros[0]["name"]][inp]

                if not path_exists:
                    #print("unsat")
                    sat = False
                    trajectory_status[traj] = 0
                    break
                else:
                    curr_st = path_trans.target

            if sat:
                #print("sat")
                trajectory_status[traj] = traj.reward
                sats.append(traj.reward)
                probs.append(probability)

        #exit(0)
        return sats, probs, trajectory_status
