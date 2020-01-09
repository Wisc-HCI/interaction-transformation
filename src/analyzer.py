from path_traversal import *
from state_machine import *

import numpy as np
import math

class Analyzer:

    def __init__(self, starter, ender, inputs):
        self.starter = starter
        self.ender = ender
        self.inputs = inputs

    def begin_trajectory_analysis(self):
        print("\nBeginning analysis of trajectories")

    def begin_interaction_analysis(self):
        print("\nBeginning analysis of interactions")

    def analyze_interactions(self, all_trajs, original_rewards):

        # look only at full_trajs
        trajs = []
        for traj in all_trajs:
            if not traj.is_generated_prefix:
                trajs.append(traj)
                traj.reward = original_rewards[traj]

        # calculate the removed transitions for the starter
        all_states = []
        for _,state in self.starter.states.items():
            all_states.append(state)
        starter_removed_transitions = []
        for state in all_states:
            for inp in self.inputs.alphabet:
                inp_exists = False
                for trans in state.out_trans:
                    if trans.condition == inp:
                        inp_exists = True
                if not inp_exists:
                    new_trans = Transition(state.id, state.id, inp)
                    new_trans.source = state
                    new_trans.target = state
                    starter_removed_transitions.append(new_trans)

        # calculate the removed transitions for the ender
        all_states = []
        for _,state in self.ender.states.items():
            all_states.append(state)
        ender_removed_transitions = []
        for state in all_states:
            for inp in self.inputs.alphabet:
                inp_exists = False
                for trans in state.out_trans:
                    if trans.condition == inp:
                        inp_exists = True
                if not inp_exists:
                    new_trans = Transition(state.id, state.id, inp)
                    new_trans.source = state
                    new_trans.target = state
                    ender_removed_transitions.append(new_trans)

        # perform path traversal for starter
        path_traversal = PathTraversal(self.starter, trajs, {}, starter_removed_transitions)
        starter_unweighted_rew_vect = []
        starter_eq_vect = []
        starter_trace_dict = {}
        path_traversal.check(starter_unweighted_rew_vect, starter_eq_vect, starter_trace_dict)

        # perform path traversal for ender
        path_traversal = PathTraversal(self.ender, trajs, {}, ender_removed_transitions)
        ender_unweighted_rew_vect = []
        ender_eq_vect = []
        ender_trace_dict = {}
        path_traversal.check(ender_unweighted_rew_vect, ender_eq_vect, ender_trace_dict)

        in_both = []
        in_none = []
        only_in_starter = []
        only_in_ender = []
        for traj in trajs:
            in_starter = starter_trace_dict[traj][1]
            in_ender = ender_trace_dict[traj][1]

            if in_starter and in_ender:
                in_both.append(traj)
            elif in_starter:
                only_in_starter.append(traj)
            elif in_ender:
                only_in_ender.append(traj)
                print(traj)
            else:
                in_none.append(traj)
        in_both_good = sum([1 if traj.reward > 0 else 0 for traj in in_both])
        in_both_bad = sum([1 if traj.reward < 0 else 0 for traj in in_both])
        in_none_good = sum([1 if traj.reward > 0 else 0 for traj in in_none])
        in_none_bad = sum([1 if traj.reward < 0 else 0 for traj in in_none])
        in_starter_good = sum([1 if traj.reward > 0 else 0 for traj in only_in_starter])
        in_starter_bad = sum([1 if traj.reward < 0 else 0 for traj in only_in_starter])
        in_ender_good = sum([1 if traj.reward > 0 else 0 for traj in only_in_ender])
        in_ender_bad = sum([1 if traj.reward < 0 else 0 for traj in only_in_ender])

        print(" >> {} in both ({} good, {} bad)".format(len(in_both), in_both_good, in_both_bad))
        print(" >> {} in none ({} good, {} bad)".format(len(in_none), in_none_good, in_none_bad))
        print(" >> {} only in starter ({} good, {} bad)".format(len(only_in_starter), in_starter_good, in_starter_bad))
        print(" >> {} only in ender ({} good, {} bad)".format(len(only_in_ender), in_ender_good, in_ender_bad))

    def calculate_seen_freq(self, raw_trajs, raw_trajs_gen_prefs,gen_pref_list,gen_pref_dict):
        longest_traj = raw_trajs[0]
        shortest_traj = raw_trajs[0]
        lens = []
        seen_dict = {}
        for traj in raw_trajs:

            # longest and shortest traj lengths
            if len(traj.vect) > len(longest_traj.vect):
                longest_traj = traj
            if len(traj.vect) < len(shortest_traj.vect):
                shortest_traj = traj

            # rolling average
            lens.append(len(traj.vect))

            # frequencies
            if traj.comparable_string() not in seen_dict:
                seen_dict[traj.comparable_string()] = 1
            else:
                seen_dict[traj.comparable_string()] += 1
        ave = 0
        for traj,freq in seen_dict.items():
            ave += freq
        ave = ave*1.0/len(seen_dict)

        lens = np.array(lens)
        ave_len = np.mean(lens)
        std_len = np.std(lens)
        print(" ~ LENGTHS ~")
        print(" >> The shortest trajectory is length {}".format(len(shortest_traj.vect)))
        print(" >> The longest trajectory is length {}".format(len(longest_traj.vect)))
        print(" >> The average trajectory length is {} (SD={})".format(ave_len,std_len))

        pref_freqs = []
        num_trajs = []
        for i in range(1,np.max(lens)+1):
            trajs_of_len = []
            # search the generated prefix list
            for traj in gen_pref_list:
                if len(traj.vect) == i:
                    trajs_of_len.append(traj)

            # search the full traj list
            for traj in raw_trajs:
                if len(traj.vect) == i:
                    trajs_of_len.append(traj)

            counter = []
            num_trajs = len(trajs_of_len)
            for traj in trajs_of_len:
                c = 0
                if traj.comparable_string() in gen_pref_dict:
                    if traj.comparable_string() not in seen_dict:
                        c += (len(gen_pref_dict[traj.comparable_string()][1])-1)
                    else:
                        c += len(gen_pref_dict[traj.comparable_string()][1])
                if traj.comparable_string() in seen_dict:
                    c += seen_dict[traj.comparable_string()]
                counter.append(c)

            ave_count = np.mean(np.array(counter))
            std_count = np.std(np.array(counter))
            pref_freqs.append((ave_count*1.0/len(raw_trajs),std_count*1.0/len(raw_trajs),num_trajs))

        print("\n ~ FREQUENCIES ~")
        print(" >> On average, full trajectories were seen by {} participants ({}% of the time)".format(ave,ave*1.0/len(raw_trajs)))
        print(" >> Starting at 1 going up to length={}, the ave. freq. for pref.s/traj.s of a given length is:".format(np.max(lens)))
        for i in range(len(pref_freqs)):
            fr = pref_freqs[i]
            idx = i + 1

            print("    {}: prefixes of this length are on average common with {}% (SD={}%) of participants ({} total prefixes in this length)".format(idx,fr[0]*100,fr[1]*100,fr[2]))
