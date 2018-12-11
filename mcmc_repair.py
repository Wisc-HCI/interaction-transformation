import random
import time
import numpy as np
import threading

from state_machine import *
from path_traversal import *
from bmc import *
from reachability_checker import *

class MCMCAdapt:

    def __init__(self, TS, micro_selection, trajs, inputs, outputs, freqs, prism, prism_converter):
        self.TS = TS
        self.trajs = trajs
        self.freqs = freqs
        self.inputs = inputs
        self.outputs = outputs
        self.micro_selection = micro_selection

        self.prism = prism
        self.prism_converter = prism_converter

    def adapt(self, num_itr, total_reward_plotter, progress_plotter, cost_plotter, prop_plotter, distance_plotter):
        allowable_time = num_itr * 60

        TS = self.TS.copy()
        SMUtil().build(TS.transitions, TS.states)
        print(TS)
        #print(TS.transitions)
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

        #print("\nREMOVED TRANSITIONS")
        #print(removed_transitions)

        # calculate the initial reward
        #solver = BMC(TS, self.trajs, self.inputs, self.outputs)
        #reward_vect = solver.check()
        #precost = self.get_cost(reward_vect)
        distance = self.TS.get_distance(TS)
        self.prism_converter.make_PRISM_TS(TS, "ts")
        #_,_,sat_ratio,num_props,num_satisfied = self.prism.check("ts.pm", "interaction.props")
        sat_ratio, num_props, num_satisfied = self.check_properties()
        path_traversal = PathTraversal(TS, self.trajs, self.freqs)
        unweighted_rew_vect, probs_vect = path_traversal.check()
        reward_vect = [unweighted_rew_vect[i] * probs_vect[i] for i in range(len(probs_vect))]
        total_reward = sum(reward_vect)
        precost = self.get_cost(reward_vect, num_props, num_satisfied, distance)

        rewards = []
        progress = []
        cost = []
        props = []
        distances = []
        accept_counter = 0
        reject_counter = 0
        best_design = [TS.copy(),sum(reward_vect)]
        start_time = time.time()
        #for i in range(1, num_itr+1):
        i=0
        while True:

            rewards.append(sum(reward_vect))
            progress.append(best_design[1])
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

            '''
            if i%5 == 0:
                total_reward_plotter.update_graph(rewards)
                progress_plotter.update_graph(progress)
                cost_plotter.update_graph(cost)
                prop_plotter.update_graph(props)
                distance_plotter.update_graph(distances)
            '''

            undoable = self.modify_TS(TS, all_trans, all_states, added_states, removed_transitions)

            '''
            # randomly pick a transition
            transition = random.choice(all_trans)

            # randomly pick a target
            target = random.choice(all_states)
            old_target_id = transition.target_id
            old_target = transition.target

            # try the new transition
            old_target.in_trans.remove(transition)
            transition.target = target
            transition.target_id = target.id
            target.in_trans.append(transition)
            '''

            # calculate the reward
            #solver = BMC(TS, self.trajs, self.inputs, self.outputs)
            #reward_vect = solver.check()
            new_distance = self.TS.get_distance(TS)
            self.prism_converter.make_PRISM_TS(TS, "ts")
            #_,_,sat_ratio,num_props,num_satisfied = self.prism.check("ts.pm", "interaction.props")
            sat_ratio, num_props, num_satisfied = self.check_properties()
            path_traversal = PathTraversal(TS, self.trajs, self.freqs)
            unweighted_rew_vect, probs_vect = path_traversal.check()
            new_reward_vect = [unweighted_rew_vect[i] * probs_vect[i] for i in range(len(probs_vect))]
            total_reward = sum(new_reward_vect)
            postcost = self.get_cost(new_reward_vect,num_props,num_satisfied,distance)
            #print(postcost)
            #print(precost)

            alpha = min(1, math.exp(-0.1 * (postcost*1.0/precost)))
            u = np.random.random()

            # accept or reject
            #print("u: {}\na: {}".format(u, alpha))
            if u > alpha:
                reject_counter += 1
                # reject. put back the old transition
                #print("reject -- itr {}".format(i))

                self.undo_modification(undoable, TS, all_trans, all_states, added_states, removed_transitions)
                '''
                target.in_trans.remove(transition)
                transition.target = old_target
                transition.target_id = old_target.id
                old_target.in_trans.append(transition)
                '''

            else:
                accept_counter += 1
                # accept!
                #print("accept -- itr {}".format(i))
                precost = postcost
                reward_vect = new_reward_vect
                distance = new_distance

                # check if we have encountered the best design
                if total_reward >= best_design[1]:
                    #print("{} = sum{} ... {}*{}".format(total_reward,new_reward_vect,probs_vect,unweighted_rew_vect))
                    best_design[0] = TS.copy()
                    best_design[1] = total_reward

            #print(TS.transitions)

            #if True:
            if i%5 == 0:
                print("itr {}".format(i))
            i+=1

        rewards.append(total_reward)
        total_reward_plotter.update_graph(rewards)

        print("completed at itr {}".format(i))

        end_time = time.time()

        print("took {} seconds".format(end_time - start_time))
        print("{} accepts, {} rejects".format(accept_counter, reject_counter))
        #print("\nREMOVED TRANSITIONS")
        #print(removed_transitions)
        #print(TS.transitions)
        #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(best_design[0].states)
        print("checking reachability")

        SMUtil().build(best_design[0].transitions, best_design[0].states)
        print(best_design[0])
        st_reachable = {}
        for state in all_states:
            rc = ReachabilityChecker(best_design[0], self.inputs, removed_transitions)
            st_reachable[state.name] = rc.check(state)
            if st_reachable[state.name] == False:
                print("state {} is unreachable".format(state.name))
        return best_design[0], st_reachable

    def modify_TS(self, TS, all_trans, all_states, added_states, removed_transitions):
        num_states = len(list(TS.states))
        num_trans = len(all_trans)
        num_added_states = len(added_states)
        print(num_added_states)

        # choose modification -- existing state, existing transition, remove transition, add transition, add state, remove state
        num_state_mods = 0
        num_transition_mods = 0# num_trans
        num_transition_deletions = 0#num_trans
        num_transition_additions = 0#len(removed_transitions)
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
            #print("modifying an existing transition")

            # randomly pick a transition
            transition = random.choice(all_trans)
            TS.transitions[str(transition.source.id)][str(transition.target.id)].remove(transition)

            # randomly pick a target
            target = random.choice(all_states)
            old_target_id = transition.target_id
            old_target = transition.target

            # try the new transition
            old_target.in_trans.remove(transition)
            transition.target = target
            transition.target_id = target.id
            target.in_trans.append(transition)
            TS.transitions[str(transition.source.id)][str(transition.target.id)].append(transition)

            undoable = (2, (target, transition, old_target))
        elif selection == 3:  # delete existing transition
            transition = random.choice(all_trans)
            #print("deleting existing transition from {} to {}".format(transition.source.name, transition.target.name))
            source = transition.source
            target = transition.target

            source.out_trans.remove(transition)
            target.in_trans.remove(transition)

            TS.transitions[str(transition.source.id)][str(transition.target.id)].remove(transition)
            all_trans.remove(transition)
            removed_transitions.append(transition)

            undoable = (3, (transition, source, target))
        elif selection == 4:  # add transition
            transition = random.choice(removed_transitions)
            #print("adding back existing transition from {} to {}".format(transition.source.name, transition.target.name))
            all_trans.append(transition)
            removed_transitions.remove(transition)

            source = transition.source
            source.out_trans.append(transition)

            target = random.choice(all_states)
            target.in_trans.append(transition)

            transition.target = target
            transition.target_id = target.id

            TS.transitions[str(transition.source.id)][str(transition.target.id)].append(transition)

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
                transition.target = state
                removed_transitions.append(transition)
                transitions.append(transition)
                TS.transitions[str(state.id)][str(state.id)].append(transition)

            undoable = (5, (state, transitions))
        elif selection == 6:  # delete existing state
            state = random.choice(added_states)
            print("deleting existing state: {}".format(state.name))
            trans_toremove = state.out_trans
            input_trans = state.in_trans

            # remove from the transitions data structure
            del TS.transitions[state.id]
            del TS.states[state.name]
            added_states.remove(state)
            all_states.remove(state)

            for st_old in TS.states:
                del TS.transitions[TS.states[st_old].id][state.id]

            # remove any removed transitions from the removed_transitions list
            to_delete = []
            for trans in removed_transitions:
                if trans.source == state:
                    to_delete.append(trans)
            for trans in to_delete:
                removed_transitions.remove(trans)

            modified_links = {}
            for trans in trans_toremove:

                trans.target.in_trans.remove(trans)
                all_trans.remove(trans)

                for inp_trans in input_trans:
                    if inp_trans.condition == trans.condition:
                        modified_links[inp_trans] = inp_trans.target
                        if trans.target == state:
                            inp_trans.target = inp_trans.source
                            inp_trans.source.in_trans.append(inp_trans)
                        else:
                            inp_trans.target = trans.target
                            trans.target.in_trans.append(inp_trans)

            # take care of any unlinked transitions
            deleted_transitions = []
            for inp_trans in input_trans:
                found_link = False
                for trans in trans_toremove:
                    if inp_trans.condition == trans.condition:
                        found_link = True
                if not found_link:
                    deleted_transitions.append(inp_trans)
                    all_trans.remove(inp_trans)
                    trans.target.in_trans.remove(inp_trans)

            undoable = (6, (state, deleted_transitions, to_delete, modified_links))

        return undoable

    def undo_modification(self, undoable, TS, all_trans, all_states, added_states, removed_transitions):

        selection = undoable[0]

        if selection == 1:    # undo modify existing state
            pass
        elif selection == 2:  # undo modify existing transition
            target = undoable[1][0]
            transition = undoable[1][1]
            old_target = undoable[1][2]

            TS.transitions[str(transition.source.id)][str(transition.target.id)].remove(transition)

            target.in_trans.remove(transition)
            transition.target = old_target
            transition.target_id = old_target.id
            old_target.in_trans.append(transition)

            TS.transitions[str(transition.source.id)][str(transition.target.id)].append(transition)
        elif selection == 3:  # re-add existing transition
            transition = undoable[1][0]
            source = undoable[1][1]
            target = undoable[1][2]

            source.out_trans.append(transition)
            target.in_trans.append(transition)

            all_trans.append(transition)
            TS.transitions[str(transition.source.id)][str(transition.target.id)].append(transition)
            removed_transitions.remove(transition)
        elif selection == 4:  # add transition
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

        elif selection == 5:  # add state
            print("undoing the addition of that state")
            state = undoable[1][0]
            transitions = undoable[1][1]

            all_states.remove(state)
            added_states.remove(state)
            del TS.states[state.name]

            del TS.transitions[state.id]
            for st_old in TS.states:
                del TS.transitions[TS.states[st_old].id][state.id]

            for trans in transitions:
                removed_transitions.remove(trans)
        elif selection == 6:  # delete existing state
            state = undoable[1][0]
            print("undoing the deletion of that state")
            deleted_transitions = undoable[1][1]
            to_delete = undoable[1][2]
            modified_links = undoable[1][3]

            # update the transitions and states data strutures
            TS.states[state.name] = state
            added_states.append(state)
            all_states.append(state)

            # take care of any unlinked transitions
            for trans in deleted_transitions:
                all_trans.append(trans)
                trans.target.in_trans.append(trans)

            # add to transitions
            TS.transitions[state.id] = {}
            for st_old in TS.states:
                TS.transitions[state.id][TS.states[st_old].id] = []
                TS.transitions[TS.states[st_old].id][state.id] = []

                for trans in all_trans:
                    if str(trans.source_id) == str(state.id) and str(trans.target_id) == str(TS.states[st_old].id):
                        TS.transitions[state.id][TS.states[st_old].id].append(trans)
                    if str(trans.target_id) == str(state.id) and str(trans.source_id) == str(TS.states[st_old].id):
                        TS.transitions[TS.states[st_old].id][state.id].append(trans)

            # add back any removed transitions to the remove_transition list
            for trans in to_delete:
                removed_transitions.append(trans)

            for trans in state.out_trans:
                all_trans.append(trans)
                trans.target.in_trans.append(trans)

                for link in modified_links:
                    link.target.in_trans.remove(link)
                    link.target = modified_links[link]
                    link.target.in_trans.append(link)

    def check_properties(self):
        sat_ratio = 0
        num_props = 0
        num_satisfied = 0

        prism_threads = {}
        for i in range(len(self.prism)):
            prism_threads[i] = threading.Thread(target=self.prism[i].check, args=("ts.pm", "{}interaction.props".format(i),))
            prism_threads[i].daemon = True
            prism_threads[i].start()

        for key in prism_threads.keys():
            prism_threads[key].join()
            num_props += self.prism[key].num_props
            num_satisfied += self.prism[key].num_satisfied

        sat_ratio = num_satisfied*1.0/num_props if num_props > 0 else 0

        return sat_ratio, num_props, num_satisfied

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
        for state in TS.states:
            if state == "{}{}".format(starter, count):
                count += 1
        return "{}{}".format(name,count)

    def get_cost(self, reward_vect, num_props, num_satisfied, distance):
        R_neg = 0.01
        R_pos = 0.01
        counter = 0.01 + len(reward_vect)
        for i in reward_vect:
            if i < 0:
                R_neg += abs(i)
            elif i > 0:
                R_pos += abs(i)

        #distance_weight = 1 + ((distance**distance**distance) )# * 1.0/len(self.TS.states))
        #print(distance_weight)
        #print(distance_weight * (((num_props-num_satisfied)*1.0/num_props) + (R_neg/counter + 1/(R_pos/counter))))
        #return distance_weight * (((num_props-num_satisfied)*1.0/num_props) + (R_neg/counter + 1/(R_pos/counter)))
        return ((num_props-num_satisfied)*1.0/num_props) + (R_neg/counter + 1/(R_pos/counter))
