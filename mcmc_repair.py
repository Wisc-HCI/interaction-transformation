import random
import time
import numpy as np
import threading

from state_machine import *
from path_traversal import *
from bmc import *
from reachability_checker import *
from mod_tracker import *
from smt_setup import *

class MCMCAdapt:

    def __init__(self, TS, micro_selection, trajs, inputs, outputs, freqs, update_trace_panel):
        self.TS = TS
        self.trajs = trajs
        self.freqs = freqs
        self.inputs = inputs
        self.outputs = outputs
        self.micro_selection = micro_selection
        self.update_trace_panel = update_trace_panel

        self.mod_limit = int(round(0.15*(2*len(self.TS.states))))

        self.setup_helper = SMTSetup()

    def adapt(self, num_itr, total_reward_plotter, progress_plotter, cost_plotter, prop_plotter, distance_plotter):
        allowable_time = num_itr * 60

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

        # calculate the initial reward
        distance = self.TS.get_distance(TS)
        sat_ratio = 1
        path_traversal = PathTraversal(TS, self.trajs, self.freqs)
        unweighted_rew_vect, probs_vect, traj_status = path_traversal.check()
        #reward_vect = [unweighted_rew_vect[i] * probs_vect[i] for i in range(len(probs_vect))]
        reward_vect = unweighted_rew_vect
        total_reward = sum(reward_vect)
        precost = self.get_cost(reward_vect, distance)

        # set up the modification tracker dataset
        mod_tracker = ModificationTracker(TS,self.inputs)

        rewards = []
        progress = []
        cost = []
        props = []
        distances = []
        accept_counter = 0
        reject_counter = 0
        best_design = [TS.copy(),[trans for trans in removed_transitions],sum(reward_vect), traj_status]
        start_time = time.time()

        #for i in range(1, num_itr+1):
        i=0
        while True:

            rewards.append(sum(reward_vect))
            progress.append(best_design[2])
            cost.append(precost)
            props.append(sat_ratio)
            distances.append(distance)

            curr_time = time.time()
            time_elapsed = curr_time - start_time
            if time_elapsed > allowable_time:
                total_reward_plotter.update_graph(rewards)
                progress_plotter.update_graph(progress)
                cost_plotter.update_graph(cost)
                prop_plotter.update_graph(props)
                distance_plotter.update_graph(distances)
                break

            undoable = self.modify_TS(TS, all_trans, all_states, added_states, removed_transitions, mod_tracker)

            # calculate the reward
            new_distance = self.TS.get_distance(TS)
            path_traversal = PathTraversal(TS, self.trajs, self.freqs)
            unweighted_rew_vect, probs_vect, traj_status = path_traversal.check()
            #new_reward_vect = [unweighted_rew_vect[i] * probs_vect[i] for i in range(len(probs_vect))]
            new_reward_vect = unweighted_rew_vect
            total_reward = sum(new_reward_vect)
            postcost = self.get_cost(new_reward_vect,distance)

            alpha = min(1, math.exp(-0.1 * (postcost*1.0/precost)))
            u = np.random.random()

            # accept or reject
            if u > alpha:
                reject_counter += 1
                self.undo_modification(undoable, TS, all_trans, all_states, added_states, removed_transitions, mod_tracker)
            else:
                accept_counter += 1
                precost = postcost
                reward_vect = new_reward_vect
                distance = new_distance

                # check if we have encountered the best design
                if total_reward >= best_design[2]:
                    print("BEST DESIGN!")
                    best_design[0] = TS.copy()
                    best_design[1] = [trans for trans in removed_transitions]
                    best_design[2] = total_reward
                    best_design[3] = traj_status

            if i%1000 == 0:
                print("itr {}".format(i))
            i+=1

        rewards.append(total_reward)
        total_reward_plotter.update_graph(rewards)

        print("completed at itr {}".format(i))

        end_time = time.time()

        print("took {} seconds".format(end_time - start_time))
        print("{} accepts, {} rejects".format(accept_counter, reject_counter))
        print(best_design[0].states)
        print("checking reachability")

        SMUtil().build(best_design[0].transitions, best_design[0].states)
        st_reachable = {}
        print(best_design[0])
        for state in best_design[0].states.values():
            rc = ReachabilityChecker(best_design[0], self.inputs, best_design[1])
            st_reachable[state.name] = rc.check(self.setup_helper, state)
            if st_reachable[state.name] == False:
                print("state {} is unreachable".format(state.name))
        self.update_trace_panel(traj_status)
        return best_design[0], st_reachable

    def modify_TS(self, TS, all_trans, all_states, added_states, removed_transitions, mod_tracker):
        #print("\n\n")
        num_states = len(list(TS.states))
        num_trans = len(all_trans)
        num_added_states = len(added_states)

        num_mods = mod_tracker.check_mod_tracker_sum()
        num_empties = mod_tracker.check_mod_tracker_empties(removed_transitions)
        mod_limited = num_mods >= self.mod_limit
        print("STATUS: {} mods performed, {} empty ones, limited? {}".format(num_mods, num_empties, mod_limited))

        # choose modification -- existing state, existing transition, remove transition, add transition, add state, remove state
        num_state_mods = 0
        num_transition_mods = num_trans if num_mods < self.mod_limit else min(self.mod_limit - num_empties,num_trans)
        num_transition_deletions = num_trans if num_mods < self.mod_limit else min(self.mod_limit - num_empties,num_trans)
        num_transition_additions = len(removed_transitions) if num_mods < self.mod_limit else num_empties
        num_state_additions = 1
        num_state_deletions = num_added_states
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
            undoable = (1, (None))
        elif selection == 2:  # modify existing transition

            # randomly pick a transition
            if mod_limited:
                print(str(mod_tracker))
                for trans in removed_transitions:
                    print(str(trans))
                transition = random.choice(mod_tracker.get_mod_tracker_nonempty_trans())
            else:
                transition = random.choice(all_trans)

            TS.transitions[str(transition.source.id)][str(transition.target.id)].remove(transition)

            # randomly pick a target
            target = random.choice(all_states)
            print("modifying an existing transition from {} to {}->{}".format(transition.source.name, transition.target.name, target.name))
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
            # randomly pick a transition
            if mod_limited:
                print(str(mod_tracker))
                for trans in removed_transitions:
                    print(str(trans))
                transition = random.choice(mod_tracker.get_mod_tracker_nonempty_trans())
            else:
                transition = random.choice(all_trans)

            print("deleting existing transition from {} to {}".format(transition.source.name, transition.target.name))
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
            print("adding back existing transition from {}, now going to {}".format(transition.source.name, transition.target.name))
            target.in_trans.append(transition)

            transition.target = target
            transition.target_id = target.id

            TS.transitions[str(transition.source.id)][str(transition.target.id)].append(transition)

            # update the mod tracker
            mod_tracker.update_mod_tracker(transition)

            undoable = (4, (transition, source, target))
        elif selection == 5:  # add state
            micro = random.choice(self.micro_selection)
            state_name = self.get_unused_name(micro["name"], TS)
            print("adding a state: {}".format(state_name))
            state = State(state_name, self.get_unused_state_id(TS), [micro])
            print("  {}".format(state.id))

            all_states.append(state)
            TS.states[state_name] = state
            added_states.append(state)

            # add to transitions
            TS.transitions[state.id] = {}
            for st_old in TS.states:
                TS.transitions[state.id][TS.states[st_old].id] = []
                TS.transitions[TS.states[st_old].id][state.id] = []

            transitions = []
            for inp in self.inputs.alphabet:
                transition = Transition(state.id, state.id, inp)
                transition.source = state
                transition.source.out_trans.append(transition)
                transition.target = state
                transition.target.in_trans.append(transition)
                all_trans.append(transition)
                transitions.append(transition)
                TS.transitions[str(state.id)][str(state.id)].append(transition)

            undoable = (5, (state, transitions))
        elif selection == 6:  # delete existing state
            # choose a state
            state = random.choice(added_states)
            print("deleting existing state: {}".format(state.name))
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

                        TS.transitions[inp_trans.source.id][inp_trans.target.id].remove(inp_trans)
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
            pass
        elif selection == 2:  # undo modify existing transition
            print("undoing that modification")
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
            print("undoing that removal")
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
            print("undoing that addition")
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

        elif selection == 5:  # add state
            print("undoing the addition of that state")
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

        elif selection == 6:  # delete existing state
            state = undoable[1][0]
            print("undoing the deletion of that state")
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
        counter = 0.01 + len(reward_vect)
        for i in reward_vect:
            if i < 0:
                R_neg += abs(i)
            elif i > 0:
                R_pos += abs(i)

        return (R_neg + 1/(R_pos))
