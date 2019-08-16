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
import util

class MCMCAdapt:

    def __init__(self, TS, micro_selection, trajs, inputs, outputs, freqs, mod_perc, path_to_interaction, update_trace_panel, algorithm, log, update_mod_panel):
        self.TS = TS
        self.trajs = trajs
        self.freqs = freqs
        self.inputs = inputs
        self.outputs = outputs
        self.micro_selection = micro_selection
        self.update_trace_panel = update_trace_panel
        self.update_mod_panel = update_mod_panel
        self.path_to_interaction = path_to_interaction
        self.algorithm=algorithm
        self.log = log
        self.num_properties = None

        self.mod_limit = int(round(mod_perc*(len(self.inputs.alphabet)*len(self.TS.states))))
        #self.mod_limit = int(round(mod_perc*(14)))
        self.num_state_limit = int(round(mod_perc*(len(self.TS.states))))

        print("the mod limit is {}".format(self.mod_limit))
        print("the num state limit is {}".format(self.num_state_limit))
        #exit()

        self.setup_helper = SMTSetup()

        '''
        Get the properties file
        '''
        prop_strings = []
        with open("inputs/{}/properties.txt".format(path_to_interaction), "r") as propfile:
            for line in propfile:
                if line != "\n" and line[0:2] != "--":
                    prop_strings.append(line)

        self.model_checker = ModelChecker(prop_strings)

        self.state_faults = {}
        self.transition_faults = {}
        self.localize_faults()
        print(self.state_faults)
        print(self.transition_faults)
        print(self.mod_limit)
        print(self.num_state_limit)

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

    def localize_faults(self):

        state_fault_severity = {}
        transition_fault_severity = {}

        # transitions and states are weighted by frequency * sum of severity w/in the non-consolidated trajectories
        # if a component exists multiple times within a trajectory, that counts as higher frequency -- duplicate severity
        for traj in self.trajs:
            vect = traj.vect

            # get the severity of each transition fault
            for i in range(1,len(vect)):
                tup = (vect[i-1][1].type,vect[i][0].type,vect[i][1].type)
                if tup not in transition_fault_severity:
                    transition_fault_severity[tup] = [traj.reward]
                else:
                    transition_fault_severity[tup].append(traj.reward)

            # get the severity of each state fault
            for item in vect:
                if item[1].type not in state_fault_severity:
                    state_fault_severity[item[1].type] = [traj.reward]
                else:
                    state_fault_severity[item[1].type].append(traj.reward)

        print(state_fault_severity)
        print(transition_fault_severity)

        for st,severities in state_fault_severity.items():
            self.state_faults[st] = sum(severities)*1.0/len(severities)

        for trans_pair,severities in transition_fault_severity.items():
            self.transition_faults[trans_pair] = sum(severities)*1.0/len(severities)

    def determine_modifiable_states(self, TS):
        modifiable_states = []

        scores = {}

        for st_name in TS.states:
            # ignore states that aren't scored
            if st_name not in self.state_faults:
                continue

            score = self.state_faults[st_name]

            if score not in scores:
                scores[score] = [TS.states[st_name]]
            else:
                scores[score].append(TS.states[st_name])

        sorted_scores = sorted(list(scores.keys()))
        print(sorted_scores)

        i = 0
        j = 0
        curr_score = sorted_scores[j]
        to_break = False
        while True:
            if to_break:
                break
            for st in scores[curr_score]:

                modifiable_states.append(st)
                i += 1

                if i >= self.num_state_limit:
                    to_break = True
                    break
            j += 1
            if j >= len(sorted_scores):
                break
            curr_score = sorted_scores[j]

        for st in modifiable_states:
            print(st.micros[0]["name"])
        return modifiable_states

    def determine_modifiable_transitions(self, TS):
        modifiable_trans = []

        scores = {}

        for source_id, tar_dict in TS.transitions.items():
            for target_id, trans_dict in tar_dict.items():
                for trans in trans_dict:
                    tup = (trans.source.micros[0]["name"],trans.condition,trans.target.micros[0]["name"])

                    if tup not in self.transition_faults:
                        continue
                    else:
                        score = self.transition_faults[tup]

                    if score not in scores:
                        scores[score] = [trans]
                    else:
                        scores[score].append(trans)

        sorted_scores = sorted(list(scores.keys()))

        i = 0
        j = 0
        curr_score = sorted_scores[j]
        to_break = False
        while True:
            if to_break:
                break
            for trans in scores[curr_score]:

                modifiable_trans.append(trans)
                i += 1

                if i >= self.mod_limit:
                    to_break = True
                    break
            j += 1
            if j >= len(sorted_scores):
                break
            curr_score = sorted_scores[j]

        for trans in modifiable_trans:
            print(str(trans))
        return modifiable_trans

    def reset_TS(self, mod_tracker):
        TS = self.TS.copy()
        SMUtil().build(TS.transitions, TS.states)

        all_trans = []
        for source,temp in TS.transitions.items():
            for target,conditions in temp.items():
                for trans in conditions:
                    all_trans.append(trans)

        all_states = []
        for _,state in TS.states.items():
            all_states.append(state)

        # create the lists to keep track of added states and removed transitions
        added_states = []
        modified_states = []
        removed_transitions = []
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
                    removed_transitions.append(new_trans)

        # set up the modification tracker dataset
        mod_tracker.reset_tracker(TS,self.inputs)

        return TS, all_trans, all_states, added_states, modified_states, removed_transitions

    def adapt(self, num_itr, total_reward_plotter, progress_plotter, cost_plotter, prop_plotter, distance_plotter, plot_data):
        start_time = time.time()

        #allowable_time = num_itr
        #allowable_time = 319.91643850803376
        #allowable_time = 98.7957421541214
        #allowable_time = 0.18487918376922607
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
        R_neg = 0.0
        R_pos = 0.0
        num_non_correctness_trajs = len(self.trajs)
        for traj in self.trajs:
            i = traj.reward
            if i < 0:
                R_neg += abs(i)
            elif i > 0:
                R_pos += abs(i)

        abs_min = (num_non_correctness_trajs-R_pos)*1.0/(2*num_non_correctness_trajs)
        abs_max = (num_non_correctness_trajs+R_neg)*1.0/(2*num_non_correctness_trajs)

        # copy the TS
        TS, all_trans, all_states, added_states, modified_states, removed_transitions = self.reset_TS(mod_tracker)
        self.moddable_sts = self.determine_modifiable_states(TS)
        self.moddable_trans = self.determine_modifiable_transitions(TS)

        # setup LTL property checker
        property_module = importlib.import_module("inputs.{}.properties".format(self.path_to_interaction))
        Properties = property_module.Properties
        property_checker = Properties(self.inputs, self.outputs)

        # correctness trajectories to be returned
        correctness_trajs = []

        #for i in range(1, num_itr+1):
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
        #perf_idx = 0
        #while perf_idx < 1:
            #perf_idx = 1

            # write to the logfile
            self.log.write(" -- beginning outer loop")

            time_start = time.time()

            # have an exit if needed
            if time.time() - lowbound_time >= break_time: #43200
                best_design[0] = overall_best_design[0]
                #best_design[1] = [trans for trans in removed_transitions]
                best_design[1] = overall_best_design[1]
                SMUtil().build(best_design[0].transitions, best_design[0].states)
                print("\nbreaking due to timeout")
                print("sat ratio: {}".format(best_result))
                print("TS:")
                print(str(best_design[0]))
                break

            # calculate the initial reward
            #distance = self.TS.get_distance(TS)
            distance = mod_tracker.check_mod_tracker_sum()
            print("DISTANCE {}".format(distance))
            self.log.write("starting distance: {}".format(distance))
            self.log.write("starting extra states: {}".format(added_states))
            sat_ratio = 1
            path_traversal = PathTraversal(TS, self.trajs, self.freqs, removed_transitions)
            unweighted_rew_vect = []
            unweighted_eq_vect = []
            traj_status = {}
            path_traversal.check(unweighted_rew_vect, unweighted_eq_vect, traj_status)
            print(unweighted_rew_vect)
            print(traj_status)
            #reward_vect = [unweighted_rew_vect[i] * probs_vect[i] for i in range(len(probs_vect))]
            reward_vect = unweighted_rew_vect
            print("rew vect post correctness: {}".format(reward_vect))
            total_reward = sum(reward_vect)
            #precost = self.get_cost(reward_vect, distance)
            perf_cost = self.get_perf_cost(reward_vect, abs_min, abs_max, num_non_correctness_trajs)
            new_eq_vect = self.model_check(TS, removed_transitions, property_checker, correctness_trajs, prop_tracker)
            eq_cost,_ = self.get_eq_cost(new_eq_vect)
            #eq_cost = self.get_eq_cost(unweighted_eq_vect)
            #print("{} - {}".format(perf_cost, eq_cost))
            precost = perf_cost + eq_cost

            accept_counter = 0
            reject_counter = 0
            TS_copy = TS.copy()
            #print("duplicating transition 2")
            best_design = [TS_copy,[TS_copy.duplicate_transition(trans.source.name, trans.condition, trans.target.name) for trans in removed_transitions],sum(reward_vect), traj_status]

            # determine the maximum possible reward
            max_possible_reward = 0
            for traj in self.trajs:
                max_possible_reward += max(0,traj.reward)

            models_checked = 0
            models_unchecked = 0

            # we want to cap the time at 12 hours
            #start_time = time.time()
            total_itr = 10000
            best_distance = distance
            while i < total_itr:

                # if i == 0, check to see if we're already at the total reward
                if i == 0:
                    if best_design[2] >= max_possible_reward:
                        print("the current design is already the best, so returning that")
                        break

                # get the current time
                #curr_time = time.time()

                # have an exit if needed
                #if curr_time - lowbound_time >= break_time: #43200
                #    break

                plot_data["rewards"].append(sum(reward_vect))
                plot_data["progress"].append(best_design[2])
                plot_data["cost"].append(precost)
                plot_data["props"].append(eq_cost)
                plot_data["distances"].append(distance)
                #plot_data["time"].append(curr_time)

                undoable = self.modify_TS(TS, all_trans, all_states, added_states, modified_states, removed_transitions, mod_tracker)

                # calculate the reward
                #new_distance = self.TS.get_distance(TS)
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
                '''
                path_traversal_1 = PathTraversal(TS, trajs_split[0], self.freqs, removed_transitions)
                path_traversal_2 = PathTraversal(TS, trajs_split[1], self.freqs, removed_transitions)
                path_traversal_3 = PathTraversal(TS, trajs_split[2], self.freqs, removed_transitions)
                path_traversal_4 = PathTraversal(TS, trajs_split[3], self.freqs, removed_transitions)

                sats_1 = []
                probs_1 = []
                trajectory_status_1 = {}
                thread_1 = Thread(target=path_traversal_1.check, args=(sats_1, probs_1, trajectory_status_1,))
                thread_1.start()

                sats_2 = []
                probs_2 = []
                trajectory_status_2 = {}
                thread_2 = Thread(target=path_traversal_2.check, args=(sats_2, probs_2, trajectory_status_2,))
                thread_2.start()

                sats_3 = []
                probs_3 = []
                trajectory_status_3 = {}
                thread_3 = Thread(target=path_traversal_3.check, args=(sats_3, probs_3, trajectory_status_3,))
                thread_3.start()

                sats_4 = []
                probs_4 = []
                trajectory_status_4 = {}
                thread_4 = Thread(target=path_traversal_4.check, args=(sats_4, probs_4, trajectory_status_4,))
                thread_4.start()

                r_1 = thread_1.join()
                r_2 = thread_2.join()
                r_3 = thread_3.join()
                r_4 = thread_4.join()

                unweighted_rew_vect = sats_1 + sats_2 + sats_3 + sats_4
                '''
                '''
                END THREADABLE
                '''

                #new_reward_vect = [unweighted_rew_vect[i] * probs_vect[i] for i in range(len(probs_vect))]
                new_reward_vect = unweighted_rew_vect
                total_reward = sum(new_reward_vect)
                #print(total_reward)
                #postcost = self.get_cost(new_reward_vect,distance)
                perf_cost = self.get_perf_cost(new_reward_vect, abs_min, abs_max, num_non_correctness_trajs)
                #print(unweighted_eq_vect)
                eq_cost,passed_mc_thresh = self.get_eq_cost(unweighted_eq_vect)

                '''
                if new_distance == 0:
                    print(eq_cost)
                    print(unweighted_eq_vect)
                    print(TS)
                    exit()
                '''

                # if eq cost is 0, run the model checker
                if eq_cost == 0:
                    #print("running the model checker {}".format(i))
                    prop_tracker.append([i])
                    new_eq_vect = self.model_check(TS, removed_transitions, property_checker, correctness_trajs, prop_tracker)
                    eq_cost,passed_mc_thresh = self.get_eq_cost(new_eq_vect)
                    #if eq_cost == 0:
                        #print("found correct interaction")
                    #print("new eq_cost: {}".format(eq_cost))
                    models_checked += 1
                    #exit()
                else:
                    #print("am not running the model checker")
                    models_unchecked += 1
                    #exit()

                ###### DO NOT CONTINUE IF SAMPLED PAST THE ALLOWABLE PROP. VIOLATION THRESHOLD
                '''
                if passed_mc_thresh:
                    self.undo_modification(undoable, TS, all_trans, all_states, added_states, modified_states, removed_transitions, mod_tracker)
                    print("gone past MCMC threshold {}".format(i))
                    continue
                '''

                #print("{} - {}".format(perf_cost, eq_cost))

                postcost = perf_cost + eq_cost
                #print(postcost)
                #postcost = eq_cost

                alpha = min(1, math.exp(-0.1 * (postcost*1.0/(precost if precost>0 else 0.01))))
                #print(math.exp(-0.1 * (postcost*1.0/(precost if precost>0 else 0.01))))
                #print(alpha)
                #print("~~~~~")
                u = np.random.random()
                #print("{} >< {} ---> {}".format(alpha,u,u>alpha))

                # accept or reject
                if u > alpha and self.algorithm=="mcmc":
                    #print("reject")
                    reject_counter += 1
                    self.undo_modification(undoable, TS, all_trans, all_states, added_states, modified_states, removed_transitions, mod_tracker)
                else:
                    edit_rate[undoable[0]]["count"] += 1
                    #print("accept")
                    #print(TS)
                    accept_counter += 1
                    precost = postcost
                    reward_vect = new_reward_vect
                    distance = new_distance

                    # check if we have encountered the best design
                    if eq_cost == 0 and total_reward > best_design[2]:    # ensuring that benign changes don't get made
                        #print("BEST DESIGN!")
                        best_distance = distance
                        best_mod_tracker = mod_tracker.copy()
                        best_design[0] = TS.copy()
                        #best_design[1] = [trans for trans in removed_transitions]
                        print("found new interaction")
                        self.log.write("found new interaction at {}".format(i))
                        best_design[1] = [best_design[0].duplicate_transition(trans.source.name, trans.condition, trans.target.name) for trans in removed_transitions]
                        best_design[2] = total_reward
                        best_design[3] = traj_status

                        if best_design[2] >= max_possible_reward:
                            print("found the best interaction, so breaking!")
                            break

                if i % (total_itr/100) == 0:
                    print("itr {}      chk/unchk {} ({} chk, {} unchk), # of correctness trajs {}".format(i, models_checked*1.0/models_unchecked if models_unchecked>0 else "undefined", models_checked, models_unchecked, len(correctness_trajs)))
                    self.log.write("itr {}      chk/unchk {} ({} chk, {} unchk), # of correctness trajs {}".format(i, models_checked*1.0/models_unchecked if models_unchecked>0 else "undefined", models_checked, models_unchecked, len(correctness_trajs)))
                    models_checked = 0
                    models_unchecked = 0
                i+=1
                #time.sleep(0.1)

            # plot everything
            with open("plot_data.pkl", "wb") as fp:
                pickle.dump(plot_data["progress"], fp)
            total_reward_plotter.update_graph(plot_data["rewards"])
            progress_plotter.update_graph(plot_data["progress"])
            cost_plotter.update_graph(plot_data["cost"])
            prop_plotter.update_graph(plot_data["props"])
            distance_plotter.update_graph(plot_data["distances"])

            print("MCMC steps: {}".format(i))
            # write to the logfile
            self.log.write(" -- mcmc steps : {}".format(i))

            # reset the TS
            # first print out the final distance
            TS, all_trans, all_states, added_states, modified_states, removed_transitions = self.reset_TS(mod_tracker)
            break

            #for traj in self.trajs:
            #    print(traj.comparable_string())

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

    def model_check(self, TS, removed_transitions, property_checker, correctness_trajs, prop_tracker):
        new_eq_vect = []
        '''
        PyNuSMV and KOSA MODEL CHECKERS
        '''
        # export the transition system to .smv file
        self.model_checker.create_and_load_model(TS, removed_transitions, self.inputs, self.outputs)

        # do the checking
        kosa_results, kosa_counterexamples = property_checker.compute_constraints(TS, self.setup_helper, removed_transitions)
        results, counterexamples = self.model_checker.check()
        results = kosa_results + results
        result = sum(results)*1.0/len(results)

        #print("correctness property satisfaction: {}".format(result))
        # write to the logfile
        #self.log.write(" -- property satisfaction : {}".format(result))

        #counter = 0
        for counterexample in kosa_counterexamples:
            if counterexample is not None:
                #print("\nPROPERTY {} VIOLATED -- prefix={}".format(counter, counterexample[1]))
                prop_tracker[-1].append("kosa")
                traj = self.build_trajectory(counterexample[0], TS.states, -1, counterexample[2], is_prefix=counterexample[1], counter=0)
                # UNCOMMENT IF WE WANT TO REMOVE LOOPS FROM THE COUNTEREXAMPLE
                #traj = util.remove_traj_loop_helper(traj_copy, int(math.floor(len(traj)/2)))
                self.trajs.append(traj)
                correctness_trajs.append(traj)
                new_eq_vect.append(-1)
            #counter += 1

        counter = 1
        curr_counterexamples = {}
        #print("~~~~~~~~~~")
        for counterexample in counterexamples:
            if counterexample is not None:

                #if counter == 7:
                #print("PROPERTY {} VIOLATED -- prefix=?".format(counter))
                prop_tracker[-1].append(str(counter))
                traj = self.build_trajectory_from_nusmv(counterexample, TS, counter=counter)
                #if counter == 7:
                #print(traj)
                if str(traj) in curr_counterexamples:
                    curr_counterexamples[str(traj)].correctness_ids.append(counter)
                    continue
                else:
                    curr_counterexamples[str(traj)] = traj
                #print(traj)
                # UNCOMMENT IF WE WANT TO REMOVE LOOPS FROM THE COUNTEREXAMPLE
                #traj = util.remove_traj_loop_helper(traj_copy, int(math.floor(len(traj)/2)))

                # check for duplicate trajectories
                for other_traj in self.trajs:
                    if str(traj) == str(other_traj):
                        print("ERROR: duplicate trajectories")
                        print(traj)
                        print(other_traj)
                        exit()

                self.trajs.append(traj)
                correctness_trajs.append(traj)
                new_eq_vect.append(traj)
            counter += 1

        #print("~~~~~~~~~~\n\n\n\n\n\n")
        if self.num_properties is None:
            self.num_properties = counter

        return new_eq_vect

    def modify_TS(self, TS, all_trans_all, all_states_all, added_states, modified_states, removed_transitions_all, mod_tracker):

        # throttle the TS modifier
        all_trans = list(set(all_trans_all) & set(self.moddable_trans))
        all_states = list(set(all_states_all) & set(self.moddable_sts))
        removed_transitions = list(set(removed_transitions_all) & set(self.moddable_trans))

        #if len(added_states) > 0:
        #    for added_state in added_states:
        #        print(added_state.name)

        # print(all_trans)
        # print(all_states)
        # print(removed_transitions)
        # done throttling

        num_trans = len(all_trans)
        num_added_states = len(added_states)

        num_mods = mod_tracker.check_mod_tracker_sum()
        num_empties = mod_tracker.check_mod_tracker_empties(removed_transitions)
        num_nonempties = mod_tracker.check_mod_tracker_nonempties(removed_transitions)
        mod_limited = num_mods >= self.mod_limit
        #print("STATUS: {} mods performed, {} empty ones, limited? {}".format(num_mods, num_empties, mod_limited))

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
        '''
        done with potential modifications
        NOTE: what do we do when there are limited modifications that can be made??
        USE MOD LIMITED
        '''
        #num_transition_mods = the number of transitions to play with is > 0 and there is mod room OR
        #num_transition_mods = 1 if ((num_trans>0 and self.mod_limit>num_mods) or min(self.mod_limit - num_nonempties,num_trans)>0 and self.mod_limit<=num_mods) else 0
        num_transition_mods = 1 if ((num_trans>0 and self.mod_limit>num_mods) or (num_nonempties > 0)) else 0
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
        #num_state_deletions = 1 if num_added_states>0 else 0

        '''
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\nNEW MODIFICATION{}".format("   ~~~ mod limited" if mod_limited else ""))
        print("   num mods: {}".format(num_mods))
        print("   mod limit: {}".format(self.mod_limit))
        print("num state mods: {}".format(num_state_mods))
        print("num transition mods: {}".format(num_transition_mods))
        print("num transition deletions: {}".format(num_transition_deletions))
        print("num transition additions: {}".format(num_transition_additions))
        print("num state additions: {}".format(num_state_additions))
        print("num state deletions: {}".format(num_state_deletions))
        '''

        sum_options = 0.0 + num_state_mods + num_transition_mods + num_transition_deletions + num_transition_additions + num_state_additions + num_state_deletions

        options = [1,2,3,4,5,6]
        selection = np.random.choice(options, 1, p=[num_state_mods/sum_options,
                                                    num_transition_mods/sum_options,
                                                    num_transition_deletions/sum_options,
                                                    num_transition_additions/sum_options,
                                                    num_state_additions/sum_options,
                                                    num_state_deletions/sum_options])

        '''
        for transition in removed_transitions:
            for transition2 in removed_transitions:
                if transition != transition2:
                    if transition.source == transition2.source and transition.condition == transition2.condition:
                        print("problem")
                        exit()
        '''

        undoable = None
        if selection == 1:    # modify existing state
            #print("~CHOICE~: state modification")

            # randomly pick a state to modify
            total_modifiable_states = allowable_modifications + modified_states
            state = random.choice(total_modifiable_states)
            curr_state_name = state.name
            old_micro = state.micros[0]

            # randomly pick a new micro
            micro = random.choice(self.micro_selection)
            state_name = self.get_unused_name(micro["name"], TS)
            state.name = state_name

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
            if self.mod_limit < mod_tracker.check_mod_tracker_sum():
                print("ERROR: modifying an existing state (1) resulted in more mods than allowed")
                exit()

            #self.update_mod_panel("state modification\nfrom {} to {}".format(old_micro["name"],state_name))
            #print("state modification from {} to {}".format(old_micro["name"],state_name))

            # prepare the undoable
            undoable = (1, (state, curr_state_name, old_micro))
        elif selection == 2:  # modify existing transition
            #print("~CHOICE~: transition modification")
            # randomly pick a transition
            if mod_limited:
                #print(str(mod_tracker))
                #for trans in removed_transitions:
                    #print(str(trans))
                transition = random.choice(mod_tracker.get_mod_tracker_nonempty_trans(removed_transitions))
            else:
                transition = random.choice(all_trans)

            TS.transitions[str(transition.source.id)][str(transition.target.id)].remove(transition)

            # randomly pick a target
            target = random.choice(all_states_all)
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

            # check if num mods went over the limit
            if self.mod_limit < mod_tracker.check_mod_tracker_sum():
                print("ERROR: modifying an existing transition (2) resulted in more mods than allowed")
                exit()

            #print("   new transition: {}".format(str(transition)))
            #self.update_mod_panel("transition modification\nfrom {} to (old) {} to (new) {}".format(transition.source.name,old_target.name, transition.target.name))

            undoable = (2, (target, transition, old_target))
        elif selection == 3:  # delete existing transition
            #print("~CHOICE~: transition deletion")
            # randomly pick a transition
            if mod_limited:
                #print(str(mod_tracker))
                #for trans in removed_transitions:
                #    print(str(trans))
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
            #print("adding back existing transition from {}, now going to {}".format(transition.source.name, transition.target.name))
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
            #print("adding a state: {}".format(state_name))
            state = State(state_name, self.get_unused_state_id(TS), [micro])
            #print("  {}".format(state.id))

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
            #for trans in transitions:
            #    state.out_trans.append(trans)

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

            #self.update_mod_panel("state addition\nfrom {}".format(state.name))

            undoable = (5, (state, transitions, trans_to_modify, source_state, target_state))
        elif selection == 6:  # delete existing state
            #print("~CHOICE~: state deletion -- ")
            # choose a state
            pre_ts = TS.copy()
            #state = random.choice(added_states)
            state = random.choice(allowable_added_states_to_delete)
            #print("   deleting existing state: {}".format(state.name))
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
            added_states.remove(state)
            all_states_all.remove(state)

            for st_old in TS.states:
                del TS.transitions[TS.states[st_old].id][state.id]

            undoable = (6, (state, removed_to_delete, modified_linked, unlinked_to_delete, trans_toremove))

            # update the mod tracker
            for transition in modified_linked:
                #print("modified_linked transition: {}".format(str(transition)))
                mod_tracker.update_mod_tracker(transition)
            for transition in unlinked_to_delete:
                #print("unlinked_to_delete transition: {}".format(str(transition)))
                mod_tracker.update_mod_tracker(transition, deleted=True)

            # check if num mods went over the limit
            if self.mod_limit < mod_tracker.check_mod_tracker_sum():
                print("ERROR: removing a state (6) resulted in more mods than allowed")
                SMUtil().build(pre_ts.transitions, pre_ts.states)
                print(pre_ts)
                print(self.TS)
                print(TS)
                exit()

            #self.update_mod_panel("state deletion\nfrom {}".format(state.name))

        #print(TS)
        return undoable

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

    def get_unused_name(self, starter, TS):
        name = starter
        count = 0
        while True:
            exists = False
            for state in TS.states:
                if state == "{}{}".format(starter, count):
                    exists = True
                    break
            if not exists:
                break
            count += 1
        return "{}{}".format(name,count)

    def get_cost(self, reward_vect, distance):
        R_neg = 0.01
        R_pos = 0.01
        for i in reward_vect:
            if i < 0:
                R_neg += abs(i)
            elif i > 0:
                R_pos += abs(i)

        return (R_neg + 1/(R_pos))

    def get_perf_cost(self, reward_vect, abs_min, abs_max, num_noncorrectness):
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

        #print("~~~~~~")
        #print(l)
        #print(abs_max)
        #print(abs_min)
        #print(raw_perf_cost)
        #print(perf_cost)
        if perf_cost>1.0 or perf_cost<0.0:
            exit()
        #exit()

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
        eq_cost = (8**len(curr_violations))-1
        #print(eq_cost)

        # adding a flag for if a certain threshold is reached
        #print(curr_violations)
        if len(curr_violations)*1.0/self.num_properties >= 0.3:
            return eq_cost,True
        else:
            return eq_cost,False

    def build_trajectory(self, rawinput, states, reward, output_mapping, is_prefix=False, counter=-1):
        traj_vect = []
        #print(rawinput)
        #print(output_mapping)
        for item in rawinput:
            micro = None
            for st_name, st in states.items():
                if output_mapping[st_name] == item[1]:
                    micro = st.micros[0]["name"]
            traj_vect.append((HumanInput(self.inputs.rev_alphabet[item[0]]), Microinteraction(micro, 0)))
            if micro == None:
                print("ERROR: microinteraction name be None")
                print(output_mapping)
                print(item)
                exit(1)

        trajectory_to_return = Trajectory(traj_vect, reward, is_prefix, is_correctness=True, correctness_id=counter)
        #print(trajectory_to_return)

        return trajectory_to_return

    def build_trajectory_from_nusmv(self, counterexample, TS, printer=False, counter=-1):
        if printer:
            print(counterexample)
        end_flag = False
        traj_vect = []
        curr_h_in = HumanInput("General")
        for step in counterexample:
            curr_r_out = Microinteraction(TS.states[step["st"]].micros[0]["name"] if step["st"] != "END" else "END",0)
            traj_vect.append((curr_h_in,curr_r_out))
            if curr_r_out.type == "END":
                end_flag = True
                break
            curr_h_in = HumanInput(step["hst"])
        if end_flag:
            is_prefix = False
        else:
            is_prefix=True
        trajectory_to_return = Trajectory(traj_vect, -1, is_prefix=is_prefix, is_correctness=True, correctness_id=counter)
        #print(trajectory_to_return)
        return trajectory_to_return
