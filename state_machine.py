class Global(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.val = None

class State(object):

    def __init__(self, name, id, micros):
        self.out_trans = []
        self.in_trans = []

        self.name = name
        self.id = id
        self.micros = micros

    def compare_to(self, state):
        if self.name != state.name:
            return False
        if self.id != state.id:
            return False
        if self.micros[0]["name"] != state.micros[0]["name"]:
            return False

        to_return = True
        for t_out_1 in self.out_trans:
            for t_out_2 in state.out_trans:
                if not t_out_1.compare_to(t_out_2):
                    to_return = False
        for t_in_1 in self.in_trans:
            for t_in_2 in state.in_trans:
                if not t_in_1.compare_to(t_in_2):
                    to_return = False

        return True

    def copy(self):
        return State(self.name, self.id, self.micros)

    def __str__(self):
        return "State: {}".format(self.name)

class Transition(object):

    def __init__(self, source_id, target_id, condition):
        self.source_id = source_id
        self.target_id = target_id

        self.source = None
        self.target = None

        self.condition = condition

    def compare_to(self, trans):
        if trans.condition != self.condition:
            return False

        if trans.source_id != self.source_id:
            return False

        if trans.target_id != self.target_id:
            return False

        if trans.target.name != self.target.name:
            return False

        if trans.source.name != self.source.name:
            return False

        return True

    def copy(self):
        return Transition(self.source_id, self.target_id, self.condition)

    def __str__(self):
        return "{} --{}--> {}, ({} - {})".format(self.source_id, self.condition, self.target_id, self.source, self.target)

class TS(object):

    def __init__(self, states, transitions, init):

        self.states = states           # {name} = State
        self.init = init               # State
        self.transitions = transitions # {source}{target} = [Transition]

        # helper variables
        self.id2state = {}
        for state_name,state in self.states.items():
            self.id2state[state.id] = state

    def is_different(self, other):

        is_different = False

        for state_name,state in self.states.items():
            exists_in_other = False
            for state_name_2, state2 in other.states.items():
                if state.compare_to(state2):
                    exists_in_other = True
            if not exists_in_other:
                is_different = True
                break

        return is_different

    def get_distance(self, other):
        distance = 0
        for source_id, temp in self.transitions.items():
            for target_id, self_transitions in temp.items():
                other_transitions = other.transitions

                for trans in self_transitions:
                    found = False
                    for other_trans in other_transitions[source_id][target_id]:
                        if trans.source.id == other_trans.source.id and trans.target.id == other_trans.target.id and trans.condition == other_trans.condition:
                            found = True
                    if not found:
                        distance += 1

        return distance

    def duplicate_transition(self, other_source_name, other_condition, other_target_name):
        trans_to_return = None

        source = None
        source_id = None
        target = None
        target_id = None
        condition = other_condition
        for st_name, state in self.states.items():
            if st_name == other_source_name:
                source = state
                source_id = state.id
            if st_name == other_target_name:
                target = state
                target_id = state.id

        if source is None or target is None:
            if target is None:
                target_id = self.init.id
                target = self.init
            else:
                print("ERROR: source cannot be none")


        trans_to_return = Transition(source_id, target_id, condition)
        trans_to_return.source = source
        trans_to_return.target = target

        if trans_to_return is None:
            print("duplicate trans error")
            exit(1)
        if trans_to_return.source is None:
            print("duplicate trans error")
            exit(1)
        return trans_to_return


    def copy(self):
        # handle the states and the init
        states_copy = {}
        init_copy = None
        for name,state in self.states.items():
            states_copy[name] = state.copy()
            if int(state.id) == 0:
                init_copy = states_copy[name]

        # handle the transitions
        transitions_copy = {}
        for source,dict in self.transitions.items():
            transitions_copy[source] = {}
            for target,transitions in dict.items():
                trans_conditions_copy = []
                for trans in transitions:
                    trans_conditions_copy.append(trans.copy())
                transitions_copy[source][target] = trans_conditions_copy

        return TS(states_copy, transitions_copy, init_copy)

    def __str__(self):
        string = "TRANSITION SYSTEM\ninit: {}\n".format(self.init.name)
        for st in self.states:
            string += "state: {}({})\n".format(st, self.states[st].id)
        for source_id, temp in self.transitions.items():
            for target_id, self_transitions in temp.items():
                for trans in self_transitions:
                    string += "transition: {}({}) >--{}--> {}({})\n".format(trans.source.name, trans.source.id, trans.condition, trans.target.name, trans.target.id)

        string += "END"
        return string

class SMUtil():

    def build(self, transitions, states):
        for trans_src in transitions:
            for trans_targ in transitions[trans_src]:
                for transition in transitions[trans_src][trans_targ]:
                    source_id = transition.source_id
                    target_id = transition.target_id

                    for state_id in states:
                        state = states[state_id]
                        if state.id == source_id and transition.source is None:
                            state.out_trans.append(transition)
                            transition.source = state
                        if state.id == target_id and transition.target is None:
                            state.in_trans.append(transition)
                            transition.target = state

        # ensure that each state has the correct number of outgoing transitions
