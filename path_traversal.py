class PathTraversal:

    def __init__(self, TS, trajectories, freqs, removed_transitions):
        self.TS = TS
        self.trajectories = trajectories
        self.freqs = freqs
        self.removed_transitions = removed_transitions

        self.always_satisfy = []
        self.may_satisfy = []
        self.never_satisfy = []

    def check(self, sats, eqs, trajectory_status, cond_dict=None, modifiable_trans=[]):

        # create a temporary dictionary of dict[source_state][condition] = target_state
        if cond_dict is None:
            cond_dict = {}
            ts_states = self.TS.states
            for state_name in ts_states:
                state = ts_states[state_name]
                cond_dict[state] = {}
                for out_trans in state.out_trans:
                    cond_dict[state][out_trans.condition] = (out_trans.target,out_trans)

        #sats = []
        #probs = []
        #trajectory_status = {}
        for traj in self.trajectories:

            # will we ALWAYS satisfy this trajectory given the modifiable states and
            # the current modifications?
            always_satisfied = True
            never_satisfied = False

            vect = traj.vect

            sat = True
            probability = 1
            if vect[0][1].type != self.TS.init.micros[0]["name"]:
                #print("unsat -- init")
                sat = False
                trajectory_status[traj] = (traj.reward,False)
                continue

            curr_st = self.TS.init
            for i in range(1, len(vect)):
                if not traj.is_prefix and i == len(vect) - 1:
                    break
                inp = vect[i][0].type
                test_out = vect[i][1].type


                if inp in cond_dict[curr_st] and cond_dict[curr_st][inp][0].micros[0]["name"] == test_out:
                    # test if we can't guarantee that we will always satisfy this
                    if cond_dict[curr_st][inp][1] in modifiable_trans:
                        always_satisfied = False

                    curr_st = cond_dict[curr_st][inp][0]
                else:
                    sat = False
                    if always_satisfied:
                        never_satisfied = True
                    always_satisfied = False
                    trajectory_status[traj] = (traj.reward,False)
                    break

                '''
                path_exists = False
                path_trans = None
                for trans in curr_st.out_trans:
                    print(trans.target.micros[0]["name"])
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
                    print(curr_st)
                    print("~~~~~~~")
                '''

            # double check that the final state is actually possible
            if sat and not traj.is_prefix:
                can_end = False
                for trans in self.removed_transitions:
                    if trans.source == curr_st:
                        can_end = True
                if not can_end:
                    sat = False
                    trajectory_status[traj] = (traj.reward,False)

            if sat:
                #print("sat")
                trajectory_status[traj] = (traj.reward,True)
                if traj.is_correctness:
                    eqs.append(traj)
                else:
                    sats.append(traj.reward)

            # now determine if we will ALWAYS satisfy this trajectory given
            # the current modifications and modifiable states
            if not traj.is_correctness and always_satisfied:
                self.always_satisfy.append(traj)
            if not traj.is_correctness and never_satisfied:
                self.never_satisfy.append(traj)

    def get_always_satisfied_score(self):
        score = 0
        sat_always = True
        for traj in self.always_satisfy:
            if not traj.is_correctness:
                #print("always sat: {}".format(str(traj)))
                score += traj.reward
            else:
                sat_always = False
        return score,sat_always

    def get_maybe_satisfied_positive_score(self):
        score = 0
        for traj in self.trajectories:
            if not traj.is_correctness and traj not in self.always_satisfy and traj not in self.never_satisfy:
                if traj.reward > 0:
                    score += traj.reward
        return score

        #if len(eqs) == 0:
        #    print("no correctness trajectories exist within the interaction")

        #exit(0)
        #return sats, probs, trajectory_status
