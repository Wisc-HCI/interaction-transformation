import random
import time
import numpy as np
from threading import Thread
import importlib
import pickle
import math

from state_machine import *
from path_traversal import *
from bmc import *
from reachability_checker import *
from mod_tracker import *
from smt_setup import *
from interaction_components import Trajectory, HumanInput, Microinteraction
from verification.model_checker import *
from adapter import Adapter
import util

class MCMCAdapt(Adapter):

    def __init__(self, TS, micro_selection, trajs, inputs, outputs, freqs, mod_perc, path_to_interaction, update_trace_panel, algorithm, log, update_mod_panel, combined_raw_trajs):
        super(MCMCAdapt, self).__init__(TS,inputs,outputs,int(round(mod_perc*(len(inputs.alphabet)*len(TS.states)))),int(round(mod_perc*(len(TS.states)))),path_to_interaction)
        self.trajs = trajs
        self.freqs = freqs
        self.micro_selection = micro_selection
        self.update_trace_panel = update_trace_panel
        self.update_mod_panel = update_mod_panel
        self.path_to_interaction = path_to_interaction
        self.algorithm=algorithm
        self.log = log
        self.num_properties = None

        print("the mod limit is {}".format(self.mod_limit))
        print("the num state limit is {}".format(self.num_state_limit))

        self.setup_helper = SMTSetup()

        self.localize_faults(self.trajs)

    def get_correct_mutations(self, num_additions, num_deletions, raw_trajs):

        '''
        Precondition: self.TS must itself be correct
        '''
        # check that TS is actually correct
        mod_tracker = ModificationTracker()
        property_module = importlib.import_module("inputs.{}.properties".format(self.path_to_interaction))
        Properties = property_module.Properties
        property_checker = Properties(self.inputs, self.outputs)
        TS, all_original_trans, all_states, added_states, modified_states, removed_transitions = self.reset_TS(mod_tracker)
        new_eq_vect = self.model_check(TS, removed_transitions, property_checker, [], [[]], append_correctness_traj=False)
        eq_cost,_ = self.get_eq_cost(new_eq_vect)
        if eq_cost != 0:
            print("ERROR: starting interaction is not correct")
            exit()

        L_pos, abs_min, abs_max = self.calculate_abs_min_max()

        # determine which states to insert into the interaction
        # first priority -- states that have been seen in positive trajectories
        # but don't currently exist in the interaction
        existing_state_names = [st.micros[0]["name"] for st_name,st in self.TS.states.items()]
        state2scores = {} # format = state_scores[state] = [score,score...score]
        state2avescore = {} # format = dict[state] = [ave score]

        existing_state2scores = {} # format = state_scores[state] = [score,score...score]
        existing_state2avescore = {} # format = dict[state] = [ave score]
        for traj in raw_trajs:
            #already_seen_in_traj = []
            if not traj.is_generated_prefix:
                for item in traj.vect:
                    micro_name = item[1].type
                    if micro_name is "END":
                        continue

                    # COMMENT IN if you don't double count microinteractions for being in the same traj twice
                    #if micro_name not in already_seen_in_traj:
                    if micro_name not in existing_state_names:
                        if micro_name not in state2scores:
                            state2scores[micro_name] = [traj.reward]
                        else:
                            state2scores[micro_name].append(traj.reward)
                    else:
                        if micro_name not in existing_state2scores:
                            existing_state2scores[micro_name] = [traj.reward]
                        else:
                            existing_state2scores[micro_name].append(traj.reward)
                    #already_seen_in_traj.append(micro_name)

            for state,arr in state2scores.items():
                state2avescore[state] = sum(arr)*1.0/len(arr)
            for state,arr in existing_state2scores.items():
                existing_state2avescore[state] = sum(arr)*1.0/len(arr)

        '''
        # debug point

        for state in state2scores:
            print("{} - {} (n.e.)".format(state,state2scores[state]))
        for state in existing_state2scores:
            print("{} - {}".format(state,existing_state2scores[state]))

        for state in state2avescore:
            print("{} - {} (n.e.)".format(state,state2avescore[state]))
        for state in existing_state2avescore:
            print("{} - {}".format(state,existing_state2avescore[state]))
        exit()
        '''

        def decide_on_states_to_add(additions_left, score_dict):
            state2add = []
            for state in score_dict:
                if state == "Farewell":
                    continue
                if len(state2add) < additions_left:  # if there is still room to add
                    state2add.append(state)
                else:
                    state_score = score_dict[state]
                    min_added_score = 1000
                    min_added_state = None
                    for added_state in state2add:
                        if score_dict[added_state] < min_added_score:
                            min_added_score = score_dict[added_state]
                            min_added_state = added_state
                    if min_added_score < state_score:
                        state2add.remove(added_state)
                        state2add.append(state)
            return state2add

        nonexisting_states2add = decide_on_states_to_add(num_additions,state2avescore)
        existing_states2add = decide_on_states_to_add(num_additions - len(nonexisting_states2add),existing_state2avescore)
        states2add = nonexisting_states2add + existing_states2add

        '''
        # Debug point

        print(nonexisting_states2add)
        print(existing_states2add)
        exit()
        '''

        # check that each state in states2add (existing + not) is unique
        unique_states_2_add = []
        for state in states2add:
            if state not in unique_states_2_add:
                unique_states_2_add.append(state)
            else:
                print("ERROR: attempting to add duplicate states")
                exit()
        # check that number of states equals the num_additions variable
        if len(states2add) != num_additions:
            print("ERROR: the number of states to add does not equal the expected number of additions")
            exit()

        def append_cost_and_TS(new_TS, removed_transitions, property_checker, correct_mods):
            new_eq_vect = self.model_check(new_TS, removed_transitions, property_checker, [], [[]], append_correctness_traj=False)
            eq_cost,_ = self.get_eq_cost(new_eq_vect)

            if eq_cost == 0:
                path_traversal = PathTraversal(new_TS, self.trajs, self.freqs, removed_transitions)
                unweighted_rew_vect = []
                path_traversal.check(unweighted_rew_vect, [], {})
                perf_cost = self.get_perf_cost(unweighted_rew_vect, abs_min, abs_max, L_pos)
                if perf_cost not in correct_mods:
                    correct_mods[perf_cost] = [new_TS]
                else:
                    correct_mods[perf_cost].append(new_TS)

        # get the additions
        accepted_additions = []
        for state_name in states2add:
            correct_additions = {}
            for trans_template in all_original_trans:
                TS,all_trans, all_states, added_states,_,removed_transitions = self.reset_TS(mod_tracker)
                available_trans = TS.transitions[trans_template.source.id][trans_template.target_id]
                for avail_tran in available_trans:
                    if trans_template.condition == avail_tran.condition:
                        trans = avail_tran
                self.add_state(TS, {"name": state_name}, trans, all_states, all_trans, added_states, mod_tracker, 0)
                append_cost_and_TS(TS,removed_transitions,property_checker,correct_additions)
            best_addition = None
            score_values = sorted(list(correct_additions.keys()))
            TS_list = correct_additions[score_values[0]]
            accepted_TS = TS_list[0]
            accepted_additions.append(accepted_TS)


        # debug
        '''
        for ad in correct_additions:
            print(ad)
            for tss in correct_additions[ad]:
                print(str(tss))
        print("~~~~~~~~~")
        for tss in accepted_additions:
            print(tss)

        exit()
        '''


        # get the deletions
        correct_deletions = {}  # format = dict[score] = TS
        for state_name in self.TS.states:
            if TS.init.name == state_name:
                continue
            TS, all_trans, all_states, added_states, modified_states, removed_transitions = self.reset_TS(mod_tracker)
            state = TS.states[state_name]
            self.delete_state(TS, state, removed_transitions, all_trans, all_states)
            append_cost_and_TS(TS,removed_transitions,property_checker,correct_deletions)

        accepted_deletions = []
        score_values = sorted(list(correct_deletions.keys()))
        counter = 0
        for score in score_values:
            TS_list = correct_deletions[score]
            reached_amount = False
            for tsys in TS_list:
                accepted_deletions.append(tsys)
                counter += 1
                if counter >= num_deletions:
                    reached_amount = True
                    break
            if reached_amount:
                break

        '''
        # debug

        for ad in correct_deletions:
            print(ad)
            for tss in correct_deletions[ad]:
                print(str(tss))

        exit()
        '''

        return accepted_additions, accepted_deletions

    def compute_inclusion(self):
        # create the lists to keep track of added states and removed transitions
        removed_transitions = []
        for _,state in self.TS.states.items():
            for inp in self.inputs.alphabet:
                inp_exists = False
                for trans in state.out_trans:
                    if trans.condition == inp:
                        inp_exists = True
                if not inp_exists:
                    new_trans = Transition(state.id, state.id, inp)
                    new_trans.source = state
                    new_trans.target = state
                    removed_transitions.append(new_trans)
        path_traversal = PathTraversal(self.TS, self.trajs, self.freqs, removed_transitions)
        traj_status = {}
        path_traversal.check([],[], traj_status)
        self.update_trace_panel(traj_status)

    def calculate_abs_min_max(self):
        '''
        calculate the absolute max and the absolute min for this set of trajectories
        '''
        R_neg = 0.0
        R_pos = 0.0
        L_pos = 0
        for traj in self.trajs:
            i = traj.reward
            if i < 0:
                R_neg += abs(i)
            elif i > 0:
                R_pos += abs(i)
                L_pos += 1

        if L_pos == 0:
            print("ERROR: cannot run program without any positive examples")
            exit()
        elif R_neg == 0:
            print("ERROR: cannot run program without any negative examples")
            exit()

        print("R_MAX_POS: {}".format(R_pos))
        abs_min = (0.0001/R_pos)*(L_pos/(L_pos+1))
        abs_max = ((R_neg+0.0001)/R_neg)*L_pos

        '''
        #old
        abs_min = (num_non_correctness_trajs-R_pos)*1.0/(2*num_non_correctness_trajs)
        abs_max = (num_non_correctness_trajs+R_neg)*1.0/(2*num_non_correctness_trajs)
        '''

        return L_pos, abs_min, abs_max

    def adapt(self, num_itr, total_reward_plotter, progress_plotter, cost_plotter, prop_plotter, distance_plotter, plot_data):
        start_time = time.time()

        allowable_time = 1

        # set up the modification tracker dataset
        mod_tracker = ModificationTracker()

        # keep track of when certain properties were violated
        prop_tracker = []

        # keep track of how much each edit was made
        edit_rate = {1:{"name":"s_mod","count": 0},
                     2:{"name":"t_mod","count": 0},
                     3:{"name":"t_del","count": 0},
                     4:{"name":"t_add","count": 0},
                     5:{"name":"s_add","count": 0},
                     6:{"name":"s_del","count": 0}}

        # calculate the absolute max and the absolute min for this set of trajectories
        L_pos, abs_min, abs_max = self.calculate_abs_min_max()

        # copy the TS
        TS, all_trans, all_states, added_states, modified_states, removed_transitions = self.reset_TS(mod_tracker)
        self.moddable_sts = self.determine_modifiable_states(TS)
        self.moddable_trans = self.determine_modifiable_transitions(TS)
        cond_dict = self.create_cond_dict(TS)
        for trans in self.moddable_trans:
            print(str(trans))
        for st in self.moddable_sts:
            print(str(st))

        # setup LTL property checker
        property_module = importlib.import_module("inputs.{}.properties".format(self.path_to_interaction))
        Properties = property_module.Properties
        property_checker = Properties(self.inputs, self.outputs)

        # correctness trajectories to be returned
        correctness_trajs = []

        i=0
        result = 0

        # split the trajectories
        nt = len(self.trajs)
        quarter = int(math.floor(nt/4))
        half = int(math.floor(nt/2))
        three_quarters = int(math.floor(nt*0.75))
        trajs_split = [self.trajs[0:quarter], self.trajs[quarter:half], self.trajs[half:three_quarters], self.trajs[three_quarters:]]

        # we cap the time at 12 hours
        lowbound_time = time.time()
        best_result = -1
        print("duplicating transition")
        overall_best_design = [TS,[TS.duplicate_transition(trans.source.name, trans.condition, trans.target.name) for trans in removed_transitions]]
        break_time = 28800

        # notify log that we're beginning to adapt
        self.log.write("adaptation beginning")

        # create an initial "best mod tracker"
        best_mod_tracker = mod_tracker.copy()

        while result < 1:

            # write to the logfile
            self.log.write(" -- beginning outer loop")

            time_start = time.time()

            # calculate the initial reward
            distance = mod_tracker.check_mod_tracker_sum()
            self.log.write("starting distance: {}".format(distance))
            self.log.write("starting extra states: {}".format(added_states))
            sat_ratio = 1
            path_traversal = PathTraversal(TS, self.trajs, self.freqs, removed_transitions)
            unweighted_rew_vect = []
            unweighted_eq_vect = []
            traj_status = {}
            path_traversal.check(unweighted_rew_vect, unweighted_eq_vect, traj_status)
            reward_vect = unweighted_rew_vect
            total_reward = sum(reward_vect)
            perf_cost = self.get_perf_cost(reward_vect, abs_min, abs_max, L_pos)
            new_eq_vect = self.model_check(TS, removed_transitions, property_checker, correctness_trajs, prop_tracker)
            eq_cost,_ = self.get_eq_cost(new_eq_vect)
            precost = perf_cost + eq_cost
            post_eq_cost = eq_cost

            self.log.write("at start, eq cost is {}, perf cost is {}".format(eq_cost, perf_cost))
            self.log.write("at start, reward is {}".format(total_reward))

            accept_counter = 0
            reject_counter = 0
            temp_accept_counter = 0
            temp_reject_counter = 0
            checking_point_accept_counter = 0
            checking_point_reject_counter = 0
            TS_copy = TS.copy()
            best_design = [TS_copy,[TS_copy.duplicate_transition(trans.source.name, trans.condition, trans.target.name) for trans in removed_transitions],sum(reward_vect), traj_status]

            # determine the maximum possible reward
            max_possible_reward = 0
            for traj in self.trajs:
                max_possible_reward += max(0,traj.reward)

            models_checked = 0
            models_unchecked = 0

            # we want to cap the time at 12 hours
            total_itr = 10000000
            self.state_modifis = 0
            num_itr_outside_state_space = 0
            lim_itr_outside_state_space = 200
            best_distance = distance
            max_time_allowed = 36000  # 9 hours
            start_time = time.time()
            model_checker_avoided_being_called = 0
            checking_point = True if eq_cost == 0 else False
            print("starting reward: {}".format(total_reward))
            while i < total_itr:

                # if timeout, exit
                if time.time() - start_time > max_time_allowed:
                    print("timed out at {} iterations".format(i))
                    print("itr {}      chk/unchk {} ({} chk, {} unchk, {} avoids), # of correctness trajs {}".format(i, models_checked*1.0/models_unchecked if models_unchecked>0 else "undefined", models_checked, models_unchecked, model_checker_avoided_being_called, len(correctness_trajs)))
                    self.log.write("itr {}      chk/unchk {} ({} chk, {} unchk, {} avoids), # of correctness trajs {}".format(i, models_checked*1.0/models_unchecked if models_unchecked>0 else "undefined", models_checked, models_unchecked, model_checker_avoided_being_called, len(correctness_trajs)))
                    break

                # if i == 0, check to see if we're already at the total reward
                if i == 0:
                    if best_design[2] >= max_possible_reward:
                        print("the current design is already the best, so returning that")
                        break

                '''
                if num_itr_outside_state_space == 0:
                    plot_data["rewards"].append(sum(reward_vect))
                    plot_data["progress"].append(best_design[2])
                    plot_data["cost"].append(precost)
                    plot_data["props"].append(post_eq_cost)
                    plot_data["distances"].append(distance)
                '''

                undoable = self.modify_TS(TS, all_trans, all_states, added_states, modified_states, removed_transitions, mod_tracker) # put cond_dict here

                # calculate the reward
                new_distance = mod_tracker.check_mod_tracker_sum()

                '''
                THREADABLE (divide the trajectories)
                create 4 threads
                '''
                path_traversal = PathTraversal(TS, self.trajs, self.freqs, removed_transitions)
                unweighted_rew_vect = []
                unweighted_eq_vect = []
                traj_status = {}
                path_traversal.check(unweighted_rew_vect, unweighted_eq_vect, traj_status)

                #new_reward_vect = [unweighted_rew_vect[i] * probs_vect[i] for i in range(len(probs_vect))]
                new_reward_vect = unweighted_rew_vect
                total_reward = sum(new_reward_vect)
                perf_cost = self.get_perf_cost(new_reward_vect, abs_min, abs_max, L_pos)
                eq_cost,passed_mc_thresh = self.get_eq_cost(unweighted_eq_vect)

                # if eq cost is 0, run the model checker
                proposed_eqcost_nonzero = False
                if eq_cost == 0:
                    prop_tracker.append([i])
                    new_eq_vect = self.model_check(TS, removed_transitions, property_checker, correctness_trajs, prop_tracker)
                    eq_cost,passed_mc_thresh = self.get_eq_cost(new_eq_vect)
                    models_checked += 1
                    if eq_cost > 0:
                        proposed_eqcost_nonzero = True
                    #print("~~\n")
                else:
                    model_checker_avoided_being_called += 1
                    models_unchecked += 1

                ###### DO NOT CONTINUE IF SAMPLED PAST THE ALLOWABLE PROP. VIOLATION THRESHOLD
                if passed_mc_thresh:
                    self.undo_modification(undoable, TS, all_trans, all_states, added_states, modified_states, removed_transitions, mod_tracker)
                    num_itr_outside_state_space += 1

                    # if the number of iterations outside of the state space has passed
                    # a certain point, reset the TS
                    if num_itr_outside_state_space > lim_itr_outside_state_space:
                        print("resetting TS")
                        TS, all_trans, all_states, added_states, modified_states, removed_transitions = self.reset_TS(mod_tracker)
                        self.moddable_sts = self.determine_modifiable_states(TS)
                        self.moddable_trans = self.determine_modifiable_transitions(TS)
                    continue
                else:
                    num_itr_outside_state_space = 0


                postcost = perf_cost + eq_cost

                alpha = min(1, math.exp(-0.1 * (postcost*1.0/(precost)))) if precost>0 else 0
                if alpha == 0:
                    alpha = 0.001
                u = np.random.random()

                if proposed_eqcost_nonzero:
                    print("           perf {} -- eq {} -- pre {} -- post {} ==== [{}]".format(perf_cost, eq_cost, precost, postcost, alpha))

                # accept or reject
                if u > alpha and self.algorithm=="mcmc":  # reject
                    if checking_point:
                        checking_point_reject_counter += 1
                    reject_counter += 1
                    temp_reject_counter += 1
                    self.undo_modification(undoable, TS, all_trans, all_states, added_states, modified_states, removed_transitions, mod_tracker)
                else:  # accept
                    if checking_point:
                        checking_point_accept_counter += 1
                    if eq_cost == 0:
                        if checking_point == False:
                            checking_point = True
                            checking_point_accept_counter = 0
                            checking_point_reject_counter = 0
                            print("   entering non-violation zone, itr {}".format(i))
                            self.log.write("   entering non-violation zone, itr {}".format(i))
                    else:
                        if checking_point:
                            checking_point = False
                            print("   LEAVING non-violation zone, itr {}, {} accepts and {} rejects (ratio {})".format(i,checking_point_accept_counter,checking_point_reject_counter, checking_point_accept_counter*1.0/(checking_point_reject_counter+checking_point_accept_counter)))
                            self.log.write("   LEAVING non-violation zone, itr {}, {} accepts and {} rejects (ratio {})".format(i,checking_point_accept_counter,checking_point_reject_counter, checking_point_accept_counter*1.0/(checking_point_reject_counter+checking_point_accept_counter)))
                    temp_accept_counter += 1
                    edit_rate[undoable[0]]["count"] += 1
                    accept_counter += 1
                    precost = postcost
                    post_eq_cost = eq_cost
                    reward_vect = new_reward_vect
                    distance = new_distance

                    # check if we have encountered the best design
                    if eq_cost == 0 and total_reward > best_design[2]:    # ensuring that benign changes don't get made
                        best_distance = distance
                        best_mod_tracker = mod_tracker.copy()
                        best_design[0] = TS.copy()
                        print("found new interaction - reward {}".format(total_reward))
                        self.log.write("found new interaction at {}".format(i))
                        self.log.write("eq cost is {}, perf cost is {}".format(eq_cost, perf_cost))
                        self.log.write("reward is {}".format(total_reward))
                        best_design[1] = [best_design[0].duplicate_transition(trans.source.name, trans.condition, trans.target.name) for trans in removed_transitions]
                        best_design[2] = total_reward
                        best_design[3] = traj_status

                        if best_design[2] >= max_possible_reward:
                            print("found the best interaction, so breaking!")
                            break

                if i % (total_itr/100) == 0:
                    print("itr {}      chk/unchk {} ({} chk, {} unchk, {} avoids), # of correctness trajs {}".format(i, models_checked*1.0/models_unchecked if models_unchecked>0 else "undefined", models_checked, models_unchecked, model_checker_avoided_being_called, len(correctness_trajs)))
                    self.log.write("itr {}      chk/unchk {} ({} chk, {} unchk, {} avoids), # of correctness trajs {}".format(i, models_checked*1.0/models_unchecked if models_unchecked>0 else "undefined", models_checked, models_unchecked, model_checker_avoided_being_called, len(correctness_trajs)))
                    print("{} accepts - {} rejects".format(temp_accept_counter,temp_reject_counter))
                    #print(self.state_modifis)
                    models_checked = 0
                    models_unchecked = 0
                    model_checker_avoided_being_called = 0
                    temp_accept_counter = 0
                    temp_reject_counter = 0
                i+=1

            # plot everything
            with open("plot_data.pkl", "wb") as fp:
                pickle.dump(plot_data["progress"], fp)
            '''
            total_reward_plotter.update_graph(plot_data["rewards"])
            progress_plotter.update_graph(plot_data["progress"])
            cost_plotter.update_graph(plot_data["cost"])
            prop_plotter.update_graph(plot_data["props"])
            distance_plotter.update_graph(plot_data["distances"])
            '''

            print("MCMC steps: {}".format(i))
            # write to the logfile
            self.log.write(" -- mcmc steps : {}".format(i))

            # reset the TS
            # first print out the final distance
            TS, all_trans, all_states, added_states, modified_states, removed_transitions = self.reset_TS(mod_tracker)
            break

        end_time = time.time()

        plot_data["rewards"].append(total_reward)
        total_reward_plotter.update_graph(plot_data["rewards"])

        with open("result_files/plot_data.pkl", "wb") as outfile:
            pickle.dump(plot_data, outfile)

        with open("result_files/prop_data.pkl", "wb") as outfile:
            pickle.dump(prop_tracker, outfile)

        with open("result_files/edit_rate_data.pkl", "wb") as outfile:
            pickle.dump(edit_rate, outfile)

        print("completed at itr {}".format(i))

        # write to the logfile
        self.log.write(" -- ending adaptation, time taken : {}".format(end_time - start_time))
        print(" -- final distance is {}".format(best_distance))

        print("took {} seconds".format(end_time - start_time))
        print("{} accepts, {} rejects".format(accept_counter, reject_counter))
        print("checking reachability")

        SMUtil().build(best_design[0].transitions, best_design[0].states)
        st_reachable = {}
        print(best_design[0])
        for state in best_design[0].states.values():
            rc = ReachabilityChecker(best_design[0], self.inputs, self.outputs, best_design[1])
            st_reachable[state.name] = True #rc.check(self.setup_helper, state)
            if st_reachable[state.name] == False:
                print("state {} is unreachable".format(state.name))
        path_traversal = PathTraversal(best_design[0], self.trajs, self.freqs, best_design[1])
        traj_status = {}
        path_traversal.check([],[], traj_status)
        self.update_trace_panel(traj_status)

        # output a pickle file with more traj status
        traj_status_pickle = {}
        for traj in traj_status:
            traj_status_pickle[str(traj)] = traj_status[traj]
        with open("traj_status.pkl", "wb") as fp:
            pickle.dump(traj_status_pickle, fp)

        return best_design[0], st_reachable, correctness_trajs, best_mod_tracker

    def modify_TS(self, TS, all_trans_all, all_states_all, added_states, modified_states, removed_transitions_all, mod_tracker):

        # throttle the TS modifier
        all_trans = list(set(all_trans_all) & set(self.moddable_trans))
        all_states = list(set(all_states_all) & set(self.moddable_sts))
        removed_transitions = list(set(removed_transitions_all) & set(self.moddable_trans))

        num_trans = len(all_trans)
        num_added_states = len(added_states)

        num_mods = mod_tracker.check_mod_tracker_sum()
        num_empties = mod_tracker.check_mod_tracker_empties(removed_transitions)
        num_nonempties = mod_tracker.check_mod_tracker_nonempties(removed_transitions)
        mod_limited = num_mods >= self.mod_limit

        # choose modification -- existing state, existing transition, remove transition, add transition, add state, remove state
        '''
        PROBLEMS:
            - once you modify a state, there's no going back (DONE. validate this works please)
            - need to make all probabilities equal
        '''

        '''
        needs to be "else choose the number of modified states"
        '''
        allowable_modifications = []
        for state in all_states:#TS.states.values():
            if state not in modified_states:
                if len(state.in_trans) <= self.mod_limit-num_mods:
                    allowable_modifications.append(state)
        num_state_mods = 1 if (len(allowable_modifications)>0 or len(modified_states)>0) else 0 #len(all_states) if num_mods < self.mod_limit else 0
        num_state_mods = len(self.moddable_sts)*1.0/len(self.moddable_trans)
        '''
        done with potential modifications
        NOTE: what do we do when there are limited modifications that can be made??
        USE MOD LIMITED
        '''
        #num_transition_mods = the number of transitions to play with is > 0 and there is mod room OR
        #num_transition_mods = 1 if ((num_trans>0 and self.mod_limit>num_mods) or min(self.mod_limit - num_nonempties,num_trans)>0 and self.mod_limit<=num_mods) else 0
        num_transition_mods = 1 if ((num_trans>0 and self.mod_limit>num_mods) or (num_nonempties > 0)) else 0
        num_transition_mods = 1
        #num_transition_deletions = num_trans if num_mods < self.mod_limit else min(self.mod_limit - num_empties,num_trans)
        num_transition_deletions = 1 if ((num_trans>0 and self.mod_limit>num_mods) or (num_nonempties > 0)) else 0
        num_transition_deletions = 0
        #num_transition_additions = len(removed_transitions) if num_mods < self.mod_limit else num_empties
        num_transition_additions = 1 if ((len(removed_transitions)>0 and self.mod_limit>num_mods) or (num_empties>0 and self.mod_limit<=num_mods)) else 0
        num_transition_additiona = 0

        # num_state_additions = 1 if there's an added state whose input transitions we can modify OR if there exists a group of modifiable transitions whose size is less than the number of modifiable transitions
        allowable_new_state_trans_mods = []
        for state in TS.states.values():
            if state in modified_states:
                for trans in state.in_trans:
                    allowable_new_state_trans_mods.append(trans)
            else:
                if len(state.in_trans) <= self.mod_limit-num_mods:
                    for trans in state.in_trans:
                        allowable_new_state_trans_mods.append(trans)
        num_state_additions = 1 if len(allowable_new_state_trans_mods)>0 and num_added_states < self.num_state_limit else 0
        num_state_additions = 0

        # num_deletions = 1 if there is an added state where deleting it won't cause the number of mods to go over the limit
        # this is a list of states that we can actually dleete
        allowable_added_states_to_delete = []
        for state in added_states:
            num_displaced = 0    # count of how many modifications will result from this state being deleted
            output_mapping = {}  # dictionary to store which states the output transitions go to
            for trans in state.out_trans:
                target_state = trans.target
                output_mapping[trans.condition] = target_state.name
            for trans in state.in_trans:
                source_state = trans.source
                if (source_state,trans.condition) in mod_tracker.mod_tracker and mod_tracker.mod_tracker[(source_state,trans.condition)][0] == 0 and (trans.condition not in output_mapping or (trans.condition in output_mapping and output_mapping[trans.condition] != state.micros[0]["name"])):
                    num_displaced += 1

            if num_displaced <= self.mod_limit - num_mods:
                allowable_added_states_to_delete.append(state)

        # decide whether we can activate this transformation or not
        num_state_deletions = 1 if len(allowable_added_states_to_delete) > 0 else 0
        num_state_deletions = 0

        sum_options = 0.0 + num_state_mods + num_transition_mods + num_transition_deletions + num_transition_additions + num_state_additions + num_state_deletions

        options = [1,2,3,4,5,6]
        selection = np.random.choice(options, 1, p=[num_state_mods/sum_options,
                                                    num_transition_mods/sum_options,
                                                    num_transition_deletions/sum_options,
                                                    num_transition_additions/sum_options,
                                                    num_state_additions/sum_options,
                                                    num_state_deletions/sum_options])

        undoable = None
        if selection == 1:    # modify existing state
            #print("\n\n~CHOICE~: state modification")
            self.state_modifis += 1

            # randomly pick a state to modify
            total_modifiable_states = allowable_modifications + modified_states
            #state = random.choice(total_modifiable_states)
            state = random.choice(all_states)
            curr_state_name = state.name
            old_micro = state.micros[0]

            # randomly pick a new micro
            micro = random.choice(self.micro_selection)
            #micro = random.choice(self.modstate2availstates[state])
            state_name = self.get_unused_name(micro["name"], TS)
            #print([str(st) for st in self.moddable_sts])
            state.name = state_name
            #print("{} to {}".format(old_micro,micro))

            # replace the old state with the new state in TS.states[state_name]
            TS.states.pop(curr_state_name)
            TS.states[state_name] = state

            # replace the microinteractions currently in state
            state.micros = [micro]

            # look for transitions that hzve been modified
            modded_transitions = []
            for trans in state.in_trans:
                if trans.target is not None:
                    mod_tracker.update_mod_tracker(trans)

            # check if num mods went over the limit
            #if self.mod_limit < mod_tracker.check_mod_tracker_sum():
            #    print("ERROR: modifying an existing state (1) resulted in more mods than allowed")
            #    exit()

            # prepare the undoable
            undoable = (1, (state, curr_state_name, old_micro))
        elif selection == 2:  # modify existing transition
            #print("\n\n~CHOICE~: transition modification")
            # randomly pick a transition
            '''
            if mod_limited:
                transition = random.choice(mod_tracker.get_mod_tracker_nonempty_trans(removed_transitions))
            else:
                transition = random.choice(all_trans)
            '''
            transition = random.choice(all_trans)

            #print("changing transition {}".format(str(transition)))
            #for trr in self.moddable_trans:
            #    print(str(trr))

            TS.transitions[str(transition.source.id)][str(transition.target.id)].remove(transition)

            # randomly pick a target
            target = random.choice(all_states_all)
            #target = random.choice(self.modtrans2availdestinations[transition])
            #print("modifying an existing transition from {}->{}->{} to {}->{}->{}".format(transition.source.name, transition.condition, transition.target.name, transition.source.name, transition.condition, target.name))
            old_target_id = transition.target_id
            old_target = transition.target

            # try the new transition
            old_target.in_trans.remove(transition)
            transition.target = target
            transition.target_id = target.id
            target.in_trans.append(transition)
            TS.transitions[str(transition.source.id)][str(transition.target.id)].append(transition)

            # update the mod tracker
            mod_tracker.update_mod_tracker(transition)

            # modify cond_dict
            #cond_dict[transition.source][transition.condition] = transition.target

            # check if num mods went over the limit
            #if self.mod_limit < mod_tracker.check_mod_tracker_sum():
            #    print("ERROR: modifying an existing transition (2) resulted in more mods than allowed")
            #    exit()

            undoable = (2, (target, transition, old_target))
        elif selection == 3:  # delete existing transition
            #print("~CHOICE~: transition deletion")
            # randomly pick a transition
            if mod_limited:
                transition = random.choice(mod_tracker.get_mod_tracker_nonempty_trans(removed_transitions))
            else:
                transition = random.choice(all_trans)

            #print("deleting existing transition from {} to {}".format(transition.source.name, transition.target.name))
            source = transition.source
            target = transition.target

            source.out_trans.remove(transition)
            target.in_trans.remove(transition)

            TS.transitions[str(transition.source.id)][str(transition.target.id)].remove(transition)
            all_trans_all.remove(transition)

            removed_transitions_all.append(transition)

            # update the mod tracker
            mod_tracker.update_mod_tracker(transition, deleted=True)

            # check if num mods went over the limit
            if self.mod_limit < mod_tracker.check_mod_tracker_sum():
                print("ERROR: deleting an existing transition (3) resulted in more mods than allowed")
                exit()

            undoable = (3, (transition, source, target))
        elif selection == 4:  # add transition
            #print("~CHOICE~: transition addition")
            # randomly pick a transition
            if mod_limited:
                transition = random.choice(mod_tracker.get_mod_tracker_empty_trans(removed_transitions))
            else:
                transition = random.choice(removed_transitions)

            all_trans_all.append(transition)
            removed_transitions_all.remove(transition)

            source = transition.source
            source.out_trans.append(transition)

            target = random.choice(all_states)
            target.in_trans.append(transition)

            transition.target = target
            transition.target_id = target.id

            TS.transitions[str(transition.source.id)][str(transition.target.id)].append(transition)

            # update the mod tracker
            mod_tracker.update_mod_tracker(transition)

            # check if num mods went over the limit
            if self.mod_limit < mod_tracker.check_mod_tracker_sum():
                print("ERROR: adding a transition (4) resulted in more mods than allowed")
                exit()

            undoable = (4, (transition, source, target))
        elif selection == 5:  # insert state
            #print("~CHOICE~: state insertion")
            '''
            # DECIDE ON WHERE TO INSERT THE STATE
            '''

            # randomly select a transition
            trans = random.choice(allowable_new_state_trans_mods)
            source_state = trans.source
            target_state = trans.target
            trans_to_modify = [trans]

            # determine if another transition between the selected states exists
            for other_trans in source_state.out_trans:
                if other_trans != trans:
                    if other_trans.target == target_state and (self.mod_limit-num_mods)-len(trans_to_modify)>0:
                        trans_to_modify.append(other_trans)

            # come up with the new state
            micro = random.choice(self.micro_selection)
            state_name = self.get_unused_name(micro["name"], TS)
            state = State(state_name, self.get_unused_state_id(TS), [micro])

            all_states_all.append(state)
            TS.states[state_name] = state
            added_states.append(state)

            # add to transitions
            TS.transitions[state.id] = {}
            for st_old in TS.states:
                TS.transitions[str(state.id)][str(TS.states[st_old].id)] = []
                TS.transitions[str(TS.states[st_old].id)][str(state.id)] = []

            transitions = []
            for inp in self.inputs.alphabet:
                transition = Transition(state.id, target_state.id, inp)
                transition.source = state
                transition.source.out_trans.append(transition)
                '''
                THE FOLLOWING LINE IS AN ADDITION
                '''
                transition.target = target_state
                transition.target.in_trans.append(transition)
                all_trans_all.append(transition)
                transitions.append(transition)
                '''
                THE FOLLOWING LINE WAS MODIFIED
                '''
                TS.transitions[str(state.id)][str(target_state.id)].append(transition)

            '''
            NOW WE MUST REMOVE THE OLD INPUT TRANSITIONS FROM THE TARGET STATE
            '''
            for trans in trans_to_modify:
                target_state.in_trans.remove(trans)

            '''
            NOW WE MUST CHANGE THE TARGET STATE OF THE INPUT TRANS
            '''
            for trans in trans_to_modify:
                trans.target = state
                trans.target_id = state.id

            '''
            NOW WE MUST MODIFY THE TRANS_TO_MODIFY
            '''
            for trans in trans_to_modify:
                mod_tracker.update_mod_tracker(trans)


            '''
            NOW WE MUST SET THE IN and OUT TRANS LISTS OF THE NEW STATE
            '''
            for trans in trans_to_modify:
                state.in_trans.append(trans)

            '''
            NOW WE MUST MODIFY THE TRANSITIONS DATASTRUCTURE TO REFLECT THE CHANGES
            '''
            # remove the transitions from the old
            for trans in trans_to_modify:
                TS.transitions[str(source_state.id)][str(target_state.id)].remove(trans)

            # add the transitons to the new
            for trans in trans_to_modify:
                TS.transitions[str(source_state.id)][str(state.id)].append(trans)

            # check if num mods went over the limit
            if self.mod_limit < mod_tracker.check_mod_tracker_sum():
                print("ERROR: adding a state (5) resulted in more mods than allowed")
                exit()


            undoable = (5, (state, transitions, trans_to_modify, source_state, target_state))
        elif selection == 6:  # delete existing state
            #print("~CHOICE~: state deletion -- ")
            # choose a state
            pre_ts = TS.copy()
            state = random.choice(allowable_added_states_to_delete)
            trans_toremove = state.out_trans
            input_trans = state.in_trans

            # remove any removed transitions from the removed_transitions list
            removed_to_delete = []
            for trans in removed_transitions_all:
                if trans.source == state:
                    removed_to_delete.append(trans)
            for trans in removed_to_delete:
                removed_transitions_all.remove(trans)

            modified_linked = {}
            for trans in trans_toremove:
                trans.target.in_trans.remove(trans)
                all_trans_all.remove(trans)

                #print(len(input_trans))
                for inp_trans in input_trans:
                    if inp_trans.condition == trans.condition:
                        modified_linked[inp_trans] = inp_trans.target

                        TS.transitions[str(inp_trans.source.id)][str(inp_trans.target.id)].remove(inp_trans)
                        if trans.target == state:
                            inp_trans.target = inp_trans.source
                            inp_trans.target_id = inp_trans.source_id
                            inp_trans.source.in_trans.append(inp_trans)
                        else:
                            inp_trans.target = trans.target
                            inp_trans.target_id = trans.target_id
                            trans.target.in_trans.append(inp_trans)
                        TS.transitions[inp_trans.source.id][inp_trans.target.id].append(inp_trans)

            # take care of any unlinked transitions
            unlinked_to_delete = []
            for inp_trans in input_trans:
                found_link = False
                for trans in trans_toremove:
                    if inp_trans.condition == trans.condition:
                        found_link = True
                if not found_link:
                    all_trans_all.remove(inp_trans)
                    unlinked_to_delete.append(inp_trans)
                    inp_trans.source.out_trans.remove(inp_trans)
                    removed_transitions_all.append(inp_trans)
                    TS.transitions[inp_trans.source.id][inp_trans.target.id].remove(inp_trans)

            # remove from the transitions data structure
            del TS.transitions[state.id]
            del TS.states[state.name]
            all_states_all.remove(state)

            for st_old in TS.states:
                del TS.transitions[TS.states[st_old].id][state.id]

            added_states.remove(state)
            undoable = (6, (state, removed_to_delete, modified_linked, unlinked_to_delete, trans_toremove))

            # update the mod tracker
            for transition in modified_linked:
                mod_tracker.update_mod_tracker(transition)
            for transition in unlinked_to_delete:
                mod_tracker.update_mod_tracker(transition, deleted=True)

            # check if num mods went over the limit
            if self.mod_limit < mod_tracker.check_mod_tracker_sum():
                print("ERROR: removing a state (6) resulted in more mods than allowed")
                SMUtil().build(pre_ts.transitions, pre_ts.states)
                print(pre_ts)
                print(self.TS)
                print(TS)
                exit()

        return undoable

    def add_state(self, TS, micro, trans, all_states_all, all_trans_all, added_states, mod_tracker, num_mods):
        source_state = trans.source
        target_state = trans.target
        other_target_states = {}
        for other_trans in source_state.out_trans:
            other_target_states[other_trans.condition] = other_trans.target
        trans_to_modify = [trans]

        # determine if another transition between the selected states exists
        for other_trans in source_state.out_trans:
            if other_trans != trans:
                if other_trans.target == target_state and (self.mod_limit-num_mods)-len(trans_to_modify)>0:
                    trans_to_modify.append(other_trans)

        # come up with the new state
        state_name = self.get_unused_name(micro["name"], TS)
        state = State(state_name, self.get_unused_state_id(TS), [micro])

        all_states_all.append(state)
        TS.states[state_name] = state
        added_states.append(state)

        # add to transitions
        TS.transitions[state.id] = {}
        for st_old in TS.states:
            TS.transitions[str(state.id)][str(TS.states[st_old].id)] = []
            TS.transitions[str(TS.states[st_old].id)][str(state.id)] = []

        transitions = []
        for inp in self.inputs.alphabet:
            transition = Transition(state.id, other_target_states[inp], inp)
            transition.source = state
            transition.source.out_trans.append(transition)
            '''
            THE FOLLOWING LINE IS AN ADDITION
            '''
            transition.target = other_target_states[inp]
            transition.target.in_trans.append(transition)
            all_trans_all.append(transition)
            transitions.append(transition)
            '''
            THE FOLLOWING LINE WAS MODIFIED
            '''
            TS.transitions[str(state.id)][str(other_target_states[inp].id)].append(transition)

        '''
        NOW WE MUST REMOVE THE OLD INPUT TRANSITIONS FROM THE TARGET STATE
        '''
        for trans in trans_to_modify:
            target_state.in_trans.remove(trans)

        '''
        NOW WE MUST CHANGE THE TARGET STATE OF THE INPUT TRANS
        '''
        for trans in trans_to_modify:
            trans.target = state
            trans.target_id = state.id

        '''
        NOW WE MUST MODIFY THE TRANS_TO_MODIFY
        '''
        for trans in trans_to_modify:
            mod_tracker.update_mod_tracker(trans)

        '''
        NOW WE MUST SET THE IN and OUT TRANS LISTS OF THE NEW STATE
        '''
        for trans in trans_to_modify:
            state.in_trans.append(trans)

        '''
        NOW WE MUST MODIFY THE TRANSITIONS DATASTRUCTURE TO REFLECT THE CHANGES
        '''
        # remove the transitions from the old
        for trans in trans_to_modify:
            TS.transitions[str(source_state.id)][str(target_state.id)].remove(trans)

        # add the transitons to the new
        for trans in trans_to_modify:
            TS.transitions[str(source_state.id)][str(state.id)].append(trans)

    def delete_state(self, TS, state, removed_transitions_all, all_trans_all, all_states_all):
        trans_toremove = state.out_trans
        input_trans = state.in_trans

        # remove any removed transitions from the removed_transitions list
        removed_to_delete = []
        for trans in removed_transitions_all:
            if trans.source == state:
                removed_to_delete.append(trans)
        for trans in removed_to_delete:
            removed_transitions_all.remove(trans)

        modified_linked = {}
        for trans in trans_toremove:
            trans.target.in_trans.remove(trans)
            all_trans_all.remove(trans)

            #print(len(input_trans))
            for inp_trans in input_trans:
                if inp_trans.condition == trans.condition:
                    modified_linked[inp_trans] = inp_trans.target

                    TS.transitions[str(inp_trans.source.id)][str(inp_trans.target.id)].remove(inp_trans)
                    if trans.target == state:
                        inp_trans.target = inp_trans.source
                        inp_trans.target_id = inp_trans.source_id
                        inp_trans.source.in_trans.append(inp_trans)
                    else:
                        inp_trans.target = trans.target
                        inp_trans.target_id = trans.target_id
                        trans.target.in_trans.append(inp_trans)
                    TS.transitions[inp_trans.source.id][inp_trans.target.id].append(inp_trans)

        # take care of any unlinked transitions
        unlinked_to_delete = []
        for inp_trans in input_trans:
            found_link = False
            for trans in trans_toremove:
                if inp_trans.condition == trans.condition:
                    found_link = True
            if not found_link:
                all_trans_all.remove(inp_trans)
                unlinked_to_delete.append(inp_trans)
                inp_trans.source.out_trans.remove(inp_trans)
                removed_transitions_all.append(inp_trans)
                TS.transitions[inp_trans.source.id][inp_trans.target.id].remove(inp_trans)

        # remove from the transitions data structure
        del TS.transitions[state.id]
        del TS.states[state.name]
        all_states_all.remove(state)

        for st_old in TS.states:
            del TS.transitions[TS.states[st_old].id][state.id]

    def undo_modification(self, undoable, TS, all_trans, all_states, added_states, modified_states, removed_transitions, mod_tracker):

        selection = undoable[0]

        if selection == 1:    # undo modify existing state

            state = undoable[1][0]
            old_state_name = undoable[1][1]
            old_micro = undoable[1][2]

            # randomly pick a state to modify
            new_state_name = state.name

            # replace the old state with the new state in TS.states[state_name]
            TS.states.pop(new_state_name)
            TS.states[old_state_name] = state

            # replace the microinteractions currently in state
            state.micros = [old_micro]
            state.name = old_state_name

            # look for transitions that hzve been modified
            modded_transitions = []
            for trans in state.in_trans:
                if trans.target is not None:
                    mod_tracker.update_mod_tracker(trans)

        elif selection == 2:  # undo modify existing transition
            #print("undoing that modification")
            target = undoable[1][0]
            transition = undoable[1][1]
            old_target = undoable[1][2]

            TS.transitions[str(transition.source.id)][str(transition.target.id)].remove(transition)

            target.in_trans.remove(transition)
            transition.target = old_target
            transition.target_id = old_target.id
            old_target.in_trans.append(transition)

            TS.transitions[str(transition.source.id)][str(transition.target.id)].append(transition)

            # update the mod tracker
            mod_tracker.update_mod_tracker(transition)

            # undo modify cond_dict
            #cond_dict[transition.source][transition.condition] = transition.target

        elif selection == 3:  # re-add existing transition
            #print("undoing that removal")
            transition = undoable[1][0]
            source = undoable[1][1]
            target = undoable[1][2]

            source.out_trans.append(transition)
            target.in_trans.append(transition)

            all_trans.append(transition)
            TS.transitions[str(transition.source.id)][str(transition.target.id)].append(transition)
            removed_transitions.remove(transition)

            # update the mod tracker
            mod_tracker.update_mod_tracker(transition)
        elif selection == 4:  # add transition
            #print("undoing that addition")
            transition = undoable[1][0]
            source = undoable[1][1]
            target = undoable[1][2]

            all_trans.remove(transition)
            TS.transitions[str(transition.source.id)][str(transition.target.id)].remove(transition)
            removed_transitions.append(transition)

            source = transition.source
            source.out_trans.remove(transition)

            target = transition.target
            target.in_trans.remove(transition)

            # update the mod tracker
            mod_tracker.update_mod_tracker(transition, deleted=True)

        elif selection == 5:  # insert state

            state = undoable[1][0]
            transitions = undoable[1][1]
            trans_to_modify = undoable[1][2]
            source_state = undoable[1][3]
            target_state = undoable[1][4]

            all_states.remove(state)
            TS.states.pop(state.name)
            added_states.remove(state)

            # remove from transitions
            TS.transitions.pop(str(state.id))
            for st_old in TS.states:
                TS.transitions[str(TS.states[st_old].id)].pop(str(state.id))

            for trans in transitions:
                all_trans.remove(trans)
                target_state.in_trans.remove(trans)

            '''
            NOW WE MUST ADD THE OLD INPUT TRANSITIONS TO THE TARGET STATE
            '''
            for trans in trans_to_modify:
                target_state.in_trans.append(trans)
                trans.target = target_state
                trans.target_id = target_state.id


            '''
            NOW WE MUST MODIFY THE TRANS_TO_MODIFY
            '''
            for trans in trans_to_modify:
                mod_tracker.update_mod_tracker(trans)

            '''
            NOW WE MUST MODIFY THE TRANSITIONS DATASTRUCTURE TO REFLECT THE CHANGES
            '''
            # remove the transitions from the old
            for trans in trans_to_modify:
                TS.transitions[str(source_state.id)][str(target_state.id)].append(trans)

            '''
            #print("undoing the addition of that state")
            state = undoable[1][0]
            transitions = undoable[1][1]

            all_states.remove(state)
            added_states.remove(state)

            del TS.states[state.name]
            del TS.transitions[state.id]

            for transition in transitions:
                transition.source.out_trans.remove(transition)
                transition.target.in_trans.remove(transition)
                all_trans.remove(transition)

            '''

        elif selection == 6:  # delete existing state
            state = undoable[1][0]
            #print("undoing the deletion of that state")
            removed_to_delete = undoable[1][1]
            modified_linked = undoable[1][2]
            unlinked_to_delete = undoable[1][3]
            out_trans_removed = undoable[1][4]

            # add to the transitions data structure
            TS.states[state.name] = state
            added_states.append(state)
            all_states.append(state)

            # add to transitions
            TS.transitions[state.id] = {}
            for st_old in TS.states:
                TS.transitions[state.id][TS.states[st_old].id] = []
                TS.transitions[TS.states[st_old].id][state.id] = []

            # append any removed transitions to the removed_transitions list
            for trans in removed_to_delete:
                removed_transitions.append(trans)

            for trans in out_trans_removed:
                all_trans.append(trans)
                trans.target.in_trans.append(trans)
                TS.transitions[trans.source.id][trans.target.id].append(trans)

            for trans in modified_linked:
                TS.transitions[trans.source.id][trans.target.id].remove(trans)

                trans.target.in_trans.remove(trans)
                trans.target = state
                trans.target_id = state.id

                TS.transitions[trans.source.id][trans.target.id].append(trans)

                # update the mod tracker
                mod_tracker.update_mod_tracker(trans)

            for trans in unlinked_to_delete:
                all_trans.append(trans)
                trans.source.out_trans.append(trans)
                removed_transitions.remove(trans)
                TS.transitions[trans.source.id][trans.target.id].append(trans)

                # update the mod tracker
                mod_tracker.update_mod_tracker(trans)

    def get_unused_state_id(self, TS):
        id = 0
        while True:
            exists = False
            for state in TS.states.values():
                if str(id) == state.id:
                    exists = True
                    break
            if not exists:
                break
            else:
                id += 1
        return str(id)

    def get_cost(self, reward_vect, distance):
        R_neg = 0.01
        R_pos = 0.01
        for i in reward_vect:
            if i < 0:
                R_neg += abs(i)
            elif i > 0:
                R_pos += abs(i)

        return (R_neg + 1/(R_pos))

    def get_perf_cost(self, reward_vect, abs_min, abs_max, L_pos):
        '''
        # THIS IS THE OLD PERF COST
        R_neg = 0.0
        R_pos = 0.0
        l = num_noncorrectness
        for i in reward_vect:
            if i < 0:
                R_neg += abs(i)
            elif i > 0:
                R_pos += abs(i)

        numerator = (l-R_pos)
        numerator += R_neg
        raw_perf_cost = numerator*1.0/(2*l) if l>0 else 0

        perf_cost = ((raw_perf_cost)-abs_min)*1.0/(abs_max-abs_min) if (abs_max - abs_min) > 0 else 0

        if perf_cost>1.0 or perf_cost<0.0:
            exit()

        return perf_cost
        '''

        # need R_neg, R_pos, and L_act_pos
        R_neg = 0.0
        R_pos = 0.0
        L_act_pos = 0
        for i in reward_vect:
            if i < 0:
                R_neg += abs(i)
            elif i > 0:
                R_pos += abs(i)
                L_act_pos += 1

        # calculate raw perf
        if (R_neg + R_pos) > 0:
            perf_raw = (R_neg+0.0001)/(R_neg+R_pos)
        else:
            return 1.0
        weighting = (L_pos*1.0)/(L_act_pos+1)
        perf_raw = perf_raw * weighting

        perf_cost = (perf_raw-abs_min)*1.0/(abs_max-abs_min)

        # REMOVE LATER
        #perf_cost = R_neg*1.0/(R_pos + R_neg) if R_pos + R_neg > 0 else 0
        #print("{} - {} - {} - {} - {} - {} - {} - {}".format(L_pos,L_act_pos,R_pos,R_neg,abs_max,abs_min,perf_raw,perf_cost))

        if perf_cost>1.0 or perf_cost<0.0:
            print("OVER/UNDER 0! {}".format(perf_cost))
            exit()

        return perf_cost

    def get_eq_cost(self, eq_vect):
        # count the number of correctness trajectories
        # COMMENT OUT BELOW IF YOU WANT eq_cost TO BE OVER ALL TRAJECTORIES
        '''
        num_correctness = 0
        for i in self.trajs:
            if i.is_correctness:
                num_correctness+=1
        sum_cost = 0.0
        for i in eq_vect:
            sum_cost += abs(i)

        eq_cost = sum_cost*1.0/num_correctness if num_correctness>0 else 0
        if eq_cost < 0:
            print("ERROR: eq cost cannot be less than 0")
        return eq_cost
        '''

        # COMMENT OUT BELOW IF YOU WANT eq_cost TO BE OVER PROPERTIES
        curr_violations = []
        for traj in eq_vect:
            prop_violations = traj.correctness_ids
            for violation in prop_violations:
                if violation not in curr_violations:
                    curr_violations.append(violation)
        #eq_cost = len(curr_violations)*1.0/self.num_properties


        #eq_cost = (10**len(curr_violations))-1
        #eq_cost = (10*len(eq_vect))
        eq_cost = (len(eq_vect)*2)**2
        #print("{} -  cost: {}".format(len(eq_vect), eq_cost))

        #eq_cost = ((10**(len(curr_violations)**1.3))-1)*1.0/((10**(self.num_properties**1.3))-1)
        #print(eq_cost)

        # adding a flag for if a certain threshold is reached
        #if len(curr_violations) == 0:
        #    print("no violations")
        #print("{} - {}".format(curr_violations, self.num_properties))
        if len(curr_violations)*1.0/self.num_properties >= 0.4:
            return eq_cost,True
        else:
            return eq_cost,False
