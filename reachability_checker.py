from z3 import *
from smt_setup import *

class ReachabilityChecker:

    def __init__(self, TS, inputs, removed_transitions):
        self.TS = TS

        # get input and output dictionaries
        self.inputs = inputs.alphabet
        self.rev_inputs = inputs.rev_alphabet

        self.outputs = {TS.init.name: 0}
        idx = 1
        for state in TS.states:
            if state != TS.init.name:
                self.outputs[state] = idx
                idx += 1

        self.removed_transitions = removed_transitions

    def check(self, setup_helper, state):

        # function that maps states + inputs to states
        f_T = Function("f_T",IntSort(), IntSort(),IntSort())

        # function that maps states to microinteractions
        f_M = Function("f_M", IntSort(),IntSort())

        # n is the number of states in the interaction
        states = self.TS.states
        n = len(self.TS.states)

        setup_constraints = setup_helper.setup(f_T, f_M, n, self.TS, self.inputs, self.outputs, self.removed_transitions)

        sts = [Int("st_{}".format(i)) for i in range(2*n)]

        traj_constraints = And(sts[0]==0)
        for st in sts:
            traj_constraints = And(traj_constraints, st>=-1, st<n)
            traj_constraints = And(traj_constraints, f_M(st)>=-1, f_M(st)<n)
        for inp in self.inputs:
            traj_constraints = And(traj_constraints, f_T(-1, self.inputs[inp])==-1)
        traj_constraints = And(traj_constraints, f_M(-1)==-1)

        for i in range(len(sts)-1):
            temp_constraint = And(False)
            for inp in self.inputs:
                temp_constraint = Or(temp_constraint,f_T(sts[i],self.inputs[inp])==sts[i+1])
            traj_constraints = And(traj_constraints, temp_constraint)

        temp_constraint = And(False)
        for i in range(len(sts)):
            temp_constraint = Or(temp_constraint, f_M(sts[i])==self.outputs[state.name])

        traj_constraints = And(traj_constraints, temp_constraint)

        s = Solver()
        s.add(And(traj_constraints,setup_constraints))
        result = s.check()

        if result == sat:
            return True
        else:
            return False
