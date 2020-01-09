import numpy as np
import random
import state_machine as sm

class TSModifier:

    def __init__(self,mod_limit,micro_selection,inputs):
        self.mod_limit = mod_limit
        self.micro_selection = micro_selection
        self.inputs = inputs

    def modify_TS(self, TS, all_trans, all_states, added_states, removed_transitions, mod_tracker):
        num_states = len(list(TS.states))
        num_trans = len(all_trans)
        num_added_states = len(added_states)

        num_mods = mod_tracker.check_mod_tracker_sum()
        num_empties = mod_tracker.check_mod_tracker_empties(removed_transitions)
        mod_limited = num_mods >= self.mod_limit
        #print("STATUS: {} mods performed, {} empty ones, limited? {}".format(num_mods, num_empties, mod_limited))

        # choose modification -- existing state, existing transition, remove transition, add transition, add state, remove state
        num_state_mods = 0
        num_transition_mods = num_trans if num_mods < self.mod_limit else min(self.mod_limit - num_empties,num_trans)
        num_transition_deletions = num_trans if num_mods < self.mod_limit else min(self.mod_limit - num_empties,num_trans)
        num_transition_additions = len(removed_transitions) if num_mods < self.mod_limit else num_empties
        num_state_additions = 10 if num_mods < self.mod_limit else 0
        num_state_deletions = num_added_states
        sum_options = 0.0 + num_state_mods + num_transition_mods + num_transition_deletions + num_transition_additions + num_state_additions + num_state_deletions

        print(self.mod_limit)
        print(num_empties)

        options = [1,2,3,4,5,6]
        selection = np.random.choice(options, 1, p=[num_state_mods/sum_options,
                                                    num_transition_mods/sum_options,
                                                    num_transition_deletions/sum_options,
                                                    num_transition_additions/sum_options,
                                                    num_state_additions/sum_options,
                                                    num_state_deletions/sum_options])

        undoable = None
        if selection == 1:    # swap existing state
            undoable = (1,(None))

            '''
            state_to_swap = random.choice(all_states)

            old_micro = state_to_swap.micros[0]
            old_name = state_to_swap.name

            while true:
                new_micro = random.choice(self.micro_selection)
                new_state_name = self.get_unused_name(micro["name"], TS)
                if new_micro["name"] != old_micro["name"]:


            state_to_swap.name = new_state_name
            state_to_swap.micros = [new_micro]

            # get the modified transitions
            for trans in state_to_swap.inp_trans:
                self.mod_tracker.update_mod_tracker(trans)

            undoable = (1, (old_micro,old_name))
            '''
        elif selection == 2:  # modify existing transition

            # randomly pick a transition
            if mod_limited:
                #print(str(mod_tracker))
                #for trans in removed_transitions:
                    #print(str(trans))
                transition = random.choice(mod_tracker.get_mod_tracker_nonempty_trans())
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
            # randomly pick a transition
            if mod_limited:
                #print(str(mod_tracker))
                #for trans in removed_transitions:
                #    print(str(trans))
                transition = random.choice(mod_tracker.get_mod_tracker_nonempty_trans())
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
        elif selection == 5:  # add state
            micro = random.choice(self.micro_selection)
            state_name = self.get_unused_name(micro["name"], TS)
            #print("adding a state: {}".format(state_name))
            state = sm.State(state_name, self.get_unused_state_id(TS), [micro])
            #print("  {}".format(state.id))

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
                transition = sm.Transition(state.id, state.id, inp)
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

        elif selection == 5:  # add state
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
