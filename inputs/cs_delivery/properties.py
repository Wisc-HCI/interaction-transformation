from z3 import *

class Properties:

    def __init__(self, inputs, outputs):
        self.inputs = inputs.alphabet

    def compute_constraints(self, TS, setup_helper, removed_transitions):

        self.outputs = {TS.init.name: 0}
        idx = 1
        for state in TS.states:
            if state != TS.init.name:
                self.outputs[state] = idx
                idx += 1

        # function that maps states + inputs to states
        f_T = Function("f_T",IntSort(), IntSort(),IntSort())

        # function that maps states to microinteractions
        f_M = Function("f_M", IntSort(),IntSort())

        # n is the number of states in the interaction
        states = TS.states
        n = len(TS.states)

        setup_constraints = setup_helper.setup(f_T, f_M, n, TS, self.inputs, self.outputs, removed_transitions)

        constraints = And(True)

        return constraints
