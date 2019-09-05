class Modifier:

    def trans_mod(self, TS, transition, newtarget,cond_dict=None):

        TS.transitions[str(transition.source.id)][str(transition.target.id)].remove(transition)

        # randomly pick a target
        target = newtarget
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

        # modify cond_dict
        cond_dict[transition.source][transition.condition] = (transition.target,transition)

        undoable = (2, (target, transition, old_target))
        return undoable

    def undo_trans_mod(self, TS, undoable, cond_dict=None):
        target = undoable[1][0]
        transition = undoable[1][1]
        old_target = undoable[1][2]

        TS.transitions[str(transition.source.id)][str(transition.target.id)].remove(transition)

        target.in_trans.remove(transition)
        transition.target = old_target
        transition.target_id = old_target.id
        old_target.in_trans.append(transition)

        TS.transitions[str(transition.source.id)][str(transition.target.id)].append(transition)

        # modify cond_dict
        cond_dict[transition.source][transition.condition] = (transition.target,transition)

    def state_mod(self, TS, state, state_name, micro,cond_dict=None):
        curr_state_name = state.name
        old_micro = state.micros[0]

        state.name = state_name

        # replace the old state with the new state in TS.states[state_name]
        TS.states.pop(curr_state_name)
        TS.states[state_name] = state

        # replace the microinteractions currently in state
        state.micros = [micro]

        # prepare the undoable
        undoable = (1, (state, curr_state_name, old_micro))
        return undoable

    def undo_state_mod(self, TS, undoable, cond_dict=None):
        state = undoable[1][0]
        old_state_name = undoable[1][1]
        old_micro = undoable[1][2]

        # get the new state name
        new_state_name = state.name

        # replace the new state with the old state in TS.states[state_name]
        TS.states.pop(new_state_name)
        TS.states[old_state_name] = state

        # replace the microinteractions currently in state
        state.micros = [old_micro]
        state.name = old_state_name
