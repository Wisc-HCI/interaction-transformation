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
import util

class MCMCAdapt:

    def __init__(self, TS, micro_selection, trajs, inputs, outputs, freqs, mod_perc, path_to_interaction, update_trace_panel, algorithm):
        self.TS = TS
        self.trajs = trajs
        self.freqs = freqs
        self.inputs = inputs
        self.outputs = outputs
        self.micro_selection = micro_selection
        self.update_trace_panel = update_trace_panel
        self.path_to_interaction = path_to_interaction
        self.algorithm=algorithm

        self.mod_limit = int(round(mod_perc*(2*len(self.TS.states))))
        #self.mod_limit = int(round(mod_perc*(14)))

        self.setup_helper = SMTSetup()

    def adapt(self, num_itr, total_reward_plotter, progress_plotter, cost_plotter, prop_plotter, distance_plotter, plot_data):
        start_time = time.time()

        #allowable_time = num_itr
        #allowable_time = 319.91643850803376
        #allowable_time = 98.7957421541214
        #allowable_time = 0.18487918376922607
        allowable_time = 1

        # for speeding up the program
        time_bins = [0,0,0,0]

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
        mod_tracker = ModificationTracker(TS,self.inputs)

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
        overall_best_design = [TS,[TS.duplicate_transition(trans.source.name, trans.condition, trans.target.name) for trans in removed_transitions]]
        break_time = 36000
        while result < 1:
        #perf_idx = 0
        #while perf_idx < 1:
            #perf_idx = 1

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
            sat_ratio = 1
            path_traversal = PathTraversal(TS, self.trajs, self.freqs, removed_transitions)
            unweighted_rew_vect = []
            traj_status = {}
            path_traversal.check(unweighted_rew_vect, traj_status)
            print(unweighted_rew_vect)
            print(traj_status)
            #reward_vect = [unweighted_rew_vect[i] * probs_vect[i] for i in range(len(probs_vect))]
            reward_vect = unweighted_rew_vect
            print("rew vect post correctness: {}".format(reward_vect))
            total_reward = sum(reward_vect)
            precost = self.get_cost(reward_vect, distance)

            accept_counter = 0
            reject_counter = 0
            TS_copy = TS.copy()
            best_design = [TS_copy,[TS_copy.duplicate_transition(trans.source.name, trans.condition, trans.target.name) for trans in removed_transitions],sum(reward_vect), traj_status]

            # determine the maximum possible reward
            max_possible_reward = 0
            for traj in self.trajs:
                max_possible_reward += max(0,traj.reward)

            miter = 0

            # we want to cap the time at 12 hours
            while True:

                # get the current time
                curr_time = time.time()

                # have an exit if needed
                if curr_time - lowbound_time >= break_time: #43200
                    break

                bin_time = time.time()
                plot_data["rewards"].append(sum(reward_vect))
                plot_data["progress"].append(best_design[2])
                plot_data["cost"].append(precost)
                plot_data["props"].append(sat_ratio)
                plot_data["distances"].append(distance)
                plot_data["time"].append(curr_time)
                new_bin_time = time.time()
                time_bins[0] += (new_bin_time-bin_time)

                #time_elapsed = curr_time - start_time
                #if miter > allowable_time or sum(reward_vect) == max_possible_reward:
                if curr_time - time_start > allowable_time:
                    with open("plot_data.pkl", "wb") as fp:
                        pickle.dump(plot_data["progress"], fp)
                    total_reward_plotter.update_graph(plot_data["rewards"])
                    progress_plotter.update_graph(plot_data["progress"])
                    cost_plotter.update_graph(plot_data["cost"])
                    prop_plotter.update_graph(plot_data["props"])
                    distance_plotter.update_graph(plot_data["distances"])
                    break

                bin_time = time.time()
                undoable = self.modify_TS(TS, all_trans, all_states, added_states, removed_transitions, mod_tracker)
                new_bin_time = time.time()
                time_bins[1] += (new_bin_time-bin_time)

                # calculate the reward
                bin_time = time.time()
                #new_distance = self.TS.get_distance(TS)
                new_distance = mod_tracker.check_mod_tracker_sum()

                '''
                THREADABLE (divide the trajectories)
                create 4 threads
                '''
                path_traversal = PathTraversal(TS, self.trajs, self.freqs, removed_transitions)
                unweighted_rew_vect = []
                traj_status = {}
                path_traversal.check(unweighted_rew_vect, traj_status)
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
                postcost = self.get_cost(new_reward_vect,distance)
                new_bin_time = time.time()
                time_bins[2] += (new_bin_time-bin_time)

                bin_time = time.time()
                alpha = min(1, math.exp(-0.1 * (postcost*1.0/precost)))
                u = np.random.random()

                # accept or reject
                if u > alpha and self.algorithm=="mcmc":
                    reject_counter += 1
                    self.undo_modification(undoable, TS, all_trans, all_states, added_states, removed_transitions, mod_tracker)
                else:
                    #print(TS)
                    accept_counter += 1
                    precost = postcost
                    reward_vect = new_reward_vect
                    distance = new_distance

                    # check if we have encountered the best design
                    if total_reward >= best_design[2]:
                        #print("BEST DESIGN!")
                        best_design[0] = TS.copy()
                        #best_design[1] = [trans for trans in removed_transitions]
                        best_design[1] = [best_design[0].duplicate_transition(trans.source.name, trans.condition, trans.target.name) for trans in removed_transitions]
                        best_design[2] = total_reward
                        best_design[3] = traj_status

                if i%5000 == 0:
                    print("itr {}".format(i))
                i+=1

                miter += 1
                new_bin_time = time.time()
                time_bins[3] += (new_bin_time-bin_time)

            print("MCMC steps: {}".format(i))
            print(time_bins)
            exit()
            SMUtil().build(best_design[0].transitions, best_design[0].states)
            print("the best design from this iteration is shown below")
            print(str(best_design[0]))
            results, counterexamples = property_checker.compute_constraints(best_design[0], self.setup_helper, best_design[1])
            result = sum(results)*1.0/len(results)
            print("prev best result: {}".format(best_result))
            print("curr best result: {}".format(result))
            if result >= best_result:
                best_result = result
                overall_best_design[0] = best_design[0].copy()
                #best_design[1] = [trans for trans in removed_transitions]
                print(best_design[1])
                for trans in best_design[1]:
                    print(str(trans))
                overall_best_design[1] = [overall_best_design[0].duplicate_transition(trans.source.name, trans.condition, trans.target.name) for trans in best_design[1]]

            print("correctness property satisfaction: {}".format(result))
            counter = 0
            for counterexample in counterexamples:
                if counterexample is not None:
                    print("\nPROPERTY {} VIOLATED -- prefix={}".format(counter, counterexample[1]))
                    traj = self.build_trajectory(counterexample[0], best_design[0].states, -1, counterexample[2], is_prefix=counterexample[1])
                    # UNCOMMENT IF WE WANT TO REMOVE LOOPS FROM THE COUNTEREXAMPLE
                    #traj = util.remove_traj_loop_helper(traj_copy, int(math.floor(len(traj)/2)))
                    self.trajs.append(traj)
                    correctness_trajs.append(traj)
                counter += 1

            print("rew vect pre correctness: {}".format(reward_vect))

            #for traj in self.trajs:
            #    print(traj.comparable_string())

        plot_data["rewards"].append(total_reward)
        total_reward_plotter.update_graph(plot_data["rewards"])

        with open("plot_data.pkl", "wb") as outfile:
            pickle.dump(plot_data, outfile)

        print("completed at itr {}".format(i))

        end_time = time.time()

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
        path_traversal.check([], traj_status)
        self.update_trace_panel(traj_status)

        # output a pickle file with more traj status
        traj_status_pickle = {}
        for traj in traj_status:
            traj_status_pickle[str(traj)] = traj_status[traj]
        with open("traj_status.pkl", "wb") as fp:
            pickle.dump(traj_status_pickle, fp)

        return best_design[0], st_reachable, correctness_trajs

    def modify_TS(self, TS, all_trans, all_states, added_states, removed_transitions, mod_tracker):
        num_states = len(list(TS.states))
        num_trans = len(all_trans)
        num_added_states = len(added_states)

        num_mods = mod_tracker.check_mod_tracker_sum()
        num_empties = mod_tracker.check_mod_tracker_empties(removed_transitions)
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
        num_state_mods = 1 if num_mods < self.mod_limit else 0 #len(all_states) if num_mods < self.mod_limit else 0
        '''
        done with potential modifications
        NOTE: what do we do when there are limited modifications that can be made??
        USE MOD LIMITED
        '''
        num_transition_mods = num_trans if num_mods < self.mod_limit else min(self.mod_limit - num_empties,num_trans)
        num_transition_deletions = num_trans if num_mods < self.mod_limit else min(self.mod_limit - num_empties,num_trans)
        num_transition_additions = len(removed_transitions) if num_mods < self.mod_limit else num_empties
        num_state_additions = num_trans if num_mods < self.mod_limit else 0
        num_state_deletions = num_added_states

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

            # handle limits to the number of modifications that can be performed
            allowable_mods = self.mod_limit - num_mods
            allowed_states = []


            # randomly pick a state to modify
            state = random.choice(all_states)
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
            target = random.choice(all_states)
            #print("modifying an existing transition from {} to {}->{}".format(transition.source.name, transition.target.name, target.name))
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
            all_trans.remove(transition)

            removed_transitions.append(transition)

            # update the mod tracker
            mod_tracker.update_mod_tracker(transition, deleted=True)

            undoable = (3, (transition, source, target))
        elif selection == 4:  # add transition
            #print("~CHOICE~: transition addition")
            # randomly pick a transition
            if mod_limited:
                transition = random.choice(mod_tracker.get_mod_tracker_empty_trans(removed_transitions))
            else:
                transition = random.choice(removed_transitions)

            all_trans.append(transition)
            removed_transitions.remove(transition)

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

            undoable = (4, (transition, source, target))
        elif selection == 5:  # insert state
            #print("~CHOICE~: state insertion")
            '''
            # DECIDE ON WHERE TO INSERT THE STATE
            '''
            # randomly select a transition
            trans = random.choice(all_trans)
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

            all_states.append(state)
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
                all_trans.append(transition)
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

            undoable = (5, (state, transitions, trans_to_modify, source_state, target_state))
        elif selection == 6:  # delete existing state
            #print("~CHOICE~: state deletion")
            # choose a state
            state = random.choice(added_states)
            #print("deleting existing state: {}".format(state.name))
            trans_toremove = state.out_trans
            input_trans = state.in_trans

            # remove any removed transitions from the removed_transitions list
            removed_to_delete = []
            for trans in removed_transitions:
                if trans.source == state:
                    removed_to_delete.append(trans)
            for trans in removed_to_delete:
                removed_transitions.remove(trans)

            modified_linked = {}
            for trans in trans_toremove:
                trans.target.in_trans.remove(trans)
                all_trans.remove(trans)

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
                    all_trans.remove(inp_trans)
                    unlinked_to_delete.append(inp_trans)
                    inp_trans.source.out_trans.remove(inp_trans)
                    removed_transitions.append(inp_trans)
                    TS.transitions[inp_trans.source.id][inp_trans.target.id].remove(inp_trans)

            # remove from the transitions data structure
            del TS.transitions[state.id]
            del TS.states[state.name]
            added_states.remove(state)
            all_states.remove(state)

            for st_old in TS.states:
                del TS.transitions[TS.states[st_old].id][state.id]

            undoable = (6, (state, removed_to_delete, modified_linked, unlinked_to_delete, trans_toremove))

            # update the mod tracker
            for transition in modified_linked:
                mod_tracker.update_mod_tracker(transition)
            for transition in unlinked_to_delete:
                mod_tracker.update_mod_tracker(transition, deleted=True)

        #print(TS)
        return undoable

    def undo_modification(self, undoable, TS, all_trans, all_states, added_states, removed_transitions, mod_tracker):

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

    def build_trajectory(self, rawinput, states, reward, output_mapping, is_prefix=False):
        traj_vect = []
        print(rawinput)
        print(output_mapping)
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

        return Trajectory(traj_vect, reward, is_prefix, is_correctness=True)
