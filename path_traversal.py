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

        can_end_arr = []
        for trans in self.removed_transitions:
            can_end_arr.append(trans.source)

        for traj in self.trajectories:

            # will we ALWAYS satisfy this trajectory given the modifiable states and
            # the current modifications?
            always_satisfied = True
            never_satisfied = False

            vect = traj.vect

            sat = True
            if vect[0][1].type != self.TS.init.micros[0]["name"]:
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

            # double check that full trajectories ended
            if sat and not traj.is_prefix:
                if curr_st not in can_end_arr:
                    sat = False
                    trajectory_status[traj] = (traj.reward,False)
                '''
                can_end = False
                for trans in self.removed_transitions:
                    if trans.source == curr_st:
                        can_end = True
                if not can_end:
                    sat = False
                '''

            if sat:
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

    def get_maybe_satisfied_positive_score(self,traj_prefix_dict):

        do_not_double_count = {}
        for traj in self.trajectories:
            do_not_double_count[traj] = False

        score = 0
        for traj in self.trajectories:
            if not traj.is_correctness and traj not in self.always_satisfy and traj not in self.never_satisfy and not do_not_double_count[traj]:
                if traj.reward > 0:
                    score += traj.reward

                    for other_traj in traj_prefix_dict[traj]:
                        if other_traj.reward < 0.0 and other_traj not in self.always_satisfy and not do_not_double_count[other_traj]:
                            score += other_traj.reward
                            do_not_double_count[other_traj] = True
                            if other_traj in self.never_satisfy:
                                print("ERROR: traj prefix is in the never satisfy dict")

                    do_not_double_count[traj] = True
        return score
