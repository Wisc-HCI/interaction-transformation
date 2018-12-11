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

    def copy(self):
        return Transition(self.source_id, self.target_id, self.condition)

    def __str__(self):
        return "{} -> {}, ({} - {})".format(self.source_id, self.target_id, self.source, self.target)

class TS(object):

    def __init__(self, states, transitions, init):

        self.states = states           # {name} = State
        self.init = init               # State
        self.transitions = transitions # {source}{target} = [Transition]

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
