from z3 import *

class SMTSetup:

    def __init__(self):
        pass

    def setup(self, f_T, f_M, n, TS, inputs, outputs, removed_transitions):
        setup_constraints = And(True)

        states = TS.states

        # set up f_M
        for _,state in states.items():
            setup_constraints = And(setup_constraints, f_M(outputs[state.name]) == outputs[state.name])

        # set up f_T
        for source,temp in TS.transitions.items():
            for target,conditions in temp.items():
                for trans in conditions:
                    setup_constraints = And(setup_constraints, f_T(outputs[trans.source.name], inputs[trans.condition]) == outputs[trans.target.name])

        for trans in removed_transitions:
            setup_constraints = And(setup_constraints, f_T(outputs[trans.source.name], inputs[trans.condition])==-1)

        for inp in inputs:
            setup_constraints = And(setup_constraints, f_T(-1, inputs[inp])==-1)

        return setup_constraints

    def counterexample(self, f_T, f_M, inps, sts, n, inputs, outputs, infinite=False, size=100):

        path_constraint = And(sts[0] == 0)
        for i in range(size-1):
            path_constraint = And(path_constraint, inps[i]<len(inputs), inps[i]>=0)
        for i in range(size):
            path_constraint = And(path_constraint, sts[i]<n, sts[i]>=-1)
        for i in range(0, size-1):
            path_constraint = And(path_constraint, f_T(sts[i], inps[i])==sts[i+1])

        if not infinite:
            path_constraint = And(path_constraint, sts[-1]==-1)
        else:
            path_constraint = And(path_constraint, sts[-1]!=-1)

        return path_constraint

    def get_result(self, m, inps, sts, n):
        raw_trajectory = [(0,0)]

        for i in range(1,2*n):
            state = int(str(m.evaluate(sts[i])))
            if state == -1:
                break
            inp = int(str(m.evaluate(inps[i-1])))
            raw_trajectory.append((inp,state))

        return raw_trajectory
