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

        results = []
        counterexamples = []

        # interaction must end
        s = Solver()
        sts0 = [Int("st_{}_0".format(i)) for i in range((2**n)+1)]
        inps0 = [Int("inp_{}_0".format(i)) for i in range(2**n)]
        path_constraint = setup_helper.counterexample(f_T, f_M, inps0, sts0, n, self.inputs, self.outputs, infinite=True, size=(2**n)+1)
        s.add(And(self.bad_suffix_constraint(f_T, f_M, n, self.inputs, self.outputs, inps0, sts0),setup_constraints, path_constraint))
        result = s.check()
        if result == sat:
            results.append(0)
            m = s.model()
            print(m)
            raw_trajectory = setup_helper.get_result(m,inps0,sts0,n)
            counterexamples.append(raw_trajectory)
        else:
            results.append(1)
            counterexamples.append(None)

        # greeter
        s = Solver()
        sts1 = [Int("st_{}_1".format(i)) for i in range(2*n)]
        inps1 = [Int("inp_{}_1".format(i)) for i in range(2*n-1)]
        path_constraint = setup_helper.counterexample(f_T, f_M, inps1, sts1, n, self.inputs, self.outputs, size=2*n)
        s.add(And(self.greeter_constraint(f_M, inps1, sts1),setup_constraints, path_constraint))
        result = s.check()
        if result == sat:
            results.append(0)
            m = s.model()
            print(m)
            raw_trajectory = setup_helper.get_result(m,inps1,sts1,n)
            counterexamples.append(raw_trajectory)
        else:
            results.append(1)
            counterexamples.append(None)

        '''
        s = Solver()
        s.add(And(self.give_constraint(f_T, f_M),setup_constraints))
        result = s.check()
        if result == sat:
            results.append(1)
        else:
            results.append(0)
        '''

        s = Solver()
        sts3 = [Int("st_{}_3".format(i)) for i in range(2*n)]
        inps3 = [Int("inp_{}_3".format(i)) for i in range(2*n-1)]
        path_constraint = setup_helper.counterexample(f_T, f_M, inps3, sts3, n, self.inputs, self.outputs, size=2*n)
        s.add(And(self.farewell_exists_constraint(f_T, f_M, n, self.inputs, self.outputs, inps3, sts3),setup_constraints, path_constraint))
        result = s.check()
        if result == sat:
            results.append(0)
            m=s.model()
            print(m)
            raw_trajectory = setup_helper.get_result(m,inps3,sts3,n)
            counterexamples.append(raw_trajectory)
        else:
            results.append(1)
            counterexamples.append(None)

        return results, counterexamples

    def bad_suffix_constraint(self, f_T, f_M, n, inputs, outputs, inps, sts):
        constraint = Or(False)

        idx = 0
        while idx < ((2**n)+1):

            each_output_constraint = And(True)
            for i in range(idx,(2**n)):

                has_pair_constraint = Or(False)
                for j in range(idx,(2**n)):

                    if i != j:
                        has_pair_constraint = Or(has_pair_constraint, And(sts[i]==sts[j], inps[i]!=inps[j]))

                each_output_constraint = And(each_output_constraint, has_pair_constraint)

            last_included_constraint = Or(False)
            for i in range(idx,(2**n)):
                last_included_constraint = Or(last_included_constraint, sts[i]==sts[-1])

            constraint = Or(constraint, And(each_output_constraint, last_included_constraint))

            idx += 1

        return constraint

    def greeter_constraint(self, f_M, inps, sts):
        return And(f_M(0) != self.outputs["Greet"])

    '''
    def give_constraint(self, f_T, f_M):
        st = Int("st_g")
        return And(f_T(0,self.inputs["Ready"])==st, Or(f_M(st)==self.outputs["Handoff"],
                                                       f_M(st)==self.outputs["Remark"]))
    '''

    def farewell_exists_constraint(self, f_T, f_M, n, inputs, outputs, inps, sts):
        constraint = And(True)

        negation_constraint = Or(False)
        for i in range(2*n-1):
            #negation_constraint = Or(negation_constraint, And(f_M(sts[i])==outputs["Farewell"], f_T(sts[i], inputs["Ready"])==-1, f_T(sts[i], inputs["Ignore"])==-1))
            negation_constraint = Or(negation_constraint, And(sts[i]>=0,f_M(sts[i])==outputs["Farewell"]))

        constraint = And(constraint, Not(negation_constraint))

        return constraint
