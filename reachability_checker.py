from z3 import *

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

    def setup(self, f_T, f_M,n):
        setup_constraints = And(True)

        states = self.TS.states

        # set up f_M
        for _,state in states.items():
            setup_constraints = And(setup_constraints, f_M(self.outputs[state.name]) == self.outputs[state.name])

        # set up f_T
        for source,temp in self.TS.transitions.items():
            for target,conditions in temp.items():
                for trans in conditions:
                    setup_constraints = And(setup_constraints, f_T(self.outputs[trans.source.name], self.inputs[trans.condition]) == self.outputs[trans.target.name])

        for trans in self.removed_transitions:
            setup_constraints = And(setup_constraints, f_T(self.outputs[trans.source.name], self.inputs[trans.condition])==-1)

        return setup_constraints

    def check(self, state):

        # function that maps states + inputs to states
        f_T = Function("f_T",IntSort(), IntSort(),IntSort())

        # function that maps states to microinteractions
        f_M = Function("f_M", IntSort(),IntSort())

        # n is the number of states in the interaction
        states = self.TS.states
        n = len(self.TS.states)

        setup_constraints = self.setup(f_T, f_M, n)

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

        #if state.name == "Begin":
        #    print(state.id)
            #m=s.model()
            #print(m)
        #print(traj_constraint)
        #print(result)

        if result == sat:
            return True
        else:
            return False
