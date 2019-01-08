from z3 import *
from kosajaru import *

class Properties:

    def __init__(self, inputs, outputs):
        self.inputs = inputs.alphabet
        self.micros = outputs.alphabet

    def compute_constraints(self, TS, setup_helper, removed_transitions):

        self.outputs = {TS.init.name: 0}
        idx = 1
        for state in TS.states:
            if state != TS.init.name:
                self.outputs[state] = idx
                idx += 1

        # function that maps states + inputs to states
        f_T = Function("f_T",IntSort(), IntSort(),IntSort())

        # function that maps state ID's to state microinteractions
        f_M = Function("f_M", IntSort(),IntSort())

        # n is the number of states in the interaction
        states = TS.states
        n = len(TS.states)

        setup_constraints = setup_helper.setup(f_T, f_M, n, TS, self.inputs, self.outputs, self.micros, removed_transitions)

        results = []
        counterexamples = []

        print("Initiating bounded model checker. n={}".format(n))

        # interaction must end
        print("Checking property 1...")
        kosa = Kosajaru(TS)
        strong_sccs = kosa.compute(self.inputs)
        for scc in strong_sccs:
            print(str(scc))
        if len(strong_sccs) == 0:
            results.append(1)
            counterexamples.append(None)
        else:
            results.append(0)
            for scc in strong_sccs:
                counterexamples.append((kosa.get_scc_counterexample(scc,self.inputs),True))
        '''
        print("Checking property 1...")
        s = Solver()
        sts0 = [Int("st_{}_0".format(i)) for i in range((4*(n-1))+1)]
        inps0 = [Int("inp_{}_0".format(i)) for i in range(4*(n-1))]
        path_constraint = setup_helper.counterexample(f_T, f_M, inps0, sts0, n, self.inputs, self.outputs, infinite=True, size=(4*(n-1))+1)
        s.add(And(self.bad_suffix_constraint(f_T, f_M, n, self.inputs, self.outputs, self.micros, inps0, sts0),setup_constraints, path_constraint))
        result = s.check()
        if result == sat:
            results.append(0)
            m = s.model()
            print(m)
            raw_trajectory = setup_helper.get_result(m,inps0,sts0,n)
            counterexamples.append((raw_trajectory,True))
        else:
            results.append(1)
            counterexamples.append(None)
        '''

        # the future involves a farewell
        # the end corresponds to farewell
        # the future involves an announcement
        # if announced and ack'ed, there will be no other announcement

        # no further announcement
        print("Checking property 2...")
        s = Solver()
        sts1 = [Int("st_{}_1".format(i)) for i in range(2*n)]
        inps1 = [Int("inp_{}_1".format(i)) for i in range(2*n-1)]
        path_constraint = setup_helper.counterexample(f_T, f_M, inps1, sts1, n, self.inputs, self.outputs, size=2*n)
        s.add(And(self.no_further_announcement_constraint(f_T, f_M, n, self.inputs, self.outputs, self.micros, inps1, sts1),setup_constraints, path_constraint))
        result = s.check()
        if result == sat:
            results.append(0)
            m = s.model()
            print(m)
            raw_trajectory = setup_helper.get_result(m,inps1,sts1,n)
            counterexamples.append((raw_trajectory, False))
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
        print("Checking property 3...")
        sts2 = [Int("st_{}_2".format(i)) for i in range(2*n)]
        inps2 = [Int("inp_{}_2".format(i)) for i in range(2*n-1)]
        path_constraint = setup_helper.counterexample(f_T, f_M, inps2, sts2, n, self.inputs, self.outputs, size=2*n)
        s.add(And(self.announcement_exists_constraint(f_T, f_M, n, self.inputs, self.outputs, self.micros, inps2, sts2),setup_constraints, path_constraint))
        result = s.check()
        if result == sat:
            results.append(0)
            m=s.model()
            print(m)
            raw_trajectory = setup_helper.get_result(m,inps2,sts2,n)
            counterexamples.append((raw_trajectory, False))
        else:
            results.append(1)
            counterexamples.append(None)

        s = Solver()
        print("Checking property 4...")
        sts3 = [Int("st_{}_3".format(i)) for i in range(2*n)]
        inps3 = [Int("inp_{}_3".format(i)) for i in range(2*n-1)]
        path_constraint = setup_helper.counterexample(f_T, f_M, inps3, sts3, n, self.inputs, self.outputs, size=2*n)
        s.add(And(self.farewell_exists_constraint(f_T, f_M, n, self.inputs, self.outputs, self.micros, inps3, sts3),setup_constraints, path_constraint))
        result = s.check()
        if result == sat:
            results.append(0)
            m=s.model()
            print(m)
            raw_trajectory = setup_helper.get_result(m,inps3,sts3,n)
            counterexamples.append((raw_trajectory, False))
        else:
            results.append(1)
            counterexamples.append(None)

        s = Solver()
        print("Checking property 5...")
        sts4 = [Int("st_{}_4".format(i)) for i in range(2*n)]
        inps4 = [Int("inp_{}_4".format(i)) for i in range(2*n-1)]
        path_constraint = setup_helper.counterexample(f_T, f_M, inps4, sts4, n, self.inputs, self.outputs, size=2*n)
        s.add(And(self.farewell_end_constraint(f_T, f_M, n, self.inputs, self.outputs, self.micros, inps4, sts4),setup_constraints, path_constraint))
        result = s.check()
        if result == sat:
            results.append(0)
            m=s.model()
            print(m)
            raw_trajectory = setup_helper.get_result(m,inps4,sts4,n)
            counterexamples.append((raw_trajectory, False))
        else:
            results.append(1)
            counterexamples.append(None)

        return results, counterexamples, self.outputs

    def bad_suffix_constraint(self, f_T, f_M, n, inputs, outputs, micros, inps, sts):
        constraint = Or(False)

        idx = 0
        while idx < (4*(n-1))+1:

            each_output_constraint = And(True)
            for i in range(idx,(4*(n-1))):

                has_pair_constraint = Or(False)
                for j in range(idx,(4*(n-1))):

                    if i != j:
                        has_pair_constraint = Or(has_pair_constraint, And(sts[i]==sts[j], inps[i]!=inps[j]))

                each_output_constraint = And(each_output_constraint, has_pair_constraint)

            last_included_constraint = Or(False)
            for i in range(idx,(4*(n-1))-1):
                last_included_constraint = Or(last_included_constraint, sts[i]==sts[-1])

            constraint = Or(constraint, And(each_output_constraint, last_included_constraint))

            idx += 1

        return constraint

    def no_further_announcement_constraint(self, f_T, f_M, n, inputs, outputs, micros, inps, sts):
        constraint = And(True)

        for i in range(2*n-1):
            curr_state_constraint = And(sts[i]!=-1, f_M(sts[i])==micros["Remark"], inps[i]==inputs["Ready"])

            to_negate_constraint = Or(False)
            for j in range(i+1,2*n-1):
                to_negate_constraint = Or(to_negate_constraint, And(sts[j]!=-1, f_M(sts[j])==micros["Remark"]))

            constraint = And(constraint, Implies(curr_state_constraint, Not(to_negate_constraint)))

        return Not(constraint)

    def announcement_exists_constraint(self, f_T, f_M, n, inputs, outputs, micros, inps, sts):
        constraint = And(True)

        negation_constraint = Or(False)
        for i in range(2*n-1):
            #negation_constraint = Or(negation_constraint, And(sts[i]>=0, f_M(sts[i])==outputs["Farewell"], f_T(sts[i], inputs["Ready"])==-1, f_T(sts[i], inputs["Ignore"])==-1))
            negation_constraint = Or(negation_constraint, And(sts[i]>=0,f_M(sts[i])==micros["Remark"]))

        constraint = And(constraint, Not(negation_constraint))

        return constraint

    def farewell_exists_constraint(self, f_T, f_M, n, inputs, outputs, micros, inps, sts):
        constraint = And(True)

        negation_constraint = Or(False)
        for i in range(2*n-1):
            #negation_constraint = Or(negation_constraint, And(sts[i]>=0, f_M(sts[i])==outputs["Farewell"], f_T(sts[i], inputs["Ready"])==-1, f_T(sts[i], inputs["Ignore"])==-1))
            negation_constraint = Or(negation_constraint, And(sts[i]>=0,f_M(sts[i])==micros["Farewell"]))

        constraint = And(constraint, Not(negation_constraint))

        return constraint

    def farewell_end_constraint(self, f_T, f_M, n, inputs, outputs, micros, inps, sts):
        constraint = And(True)

        negation_constraint = Or(False)
        for i in range(2*n-2):
            #negation_constraint = Or(negation_constraint, And(sts[i]>=0, f_M(sts[i])==outputs["Farewell"], f_T(sts[i], inputs["Ready"])==-1, f_T(sts[i], inputs["Ignore"])==-1))
            negation_constraint = Or(negation_constraint, And(sts[i]>=0,f_M(sts[i])==micros["Farewell"], sts[i+1]>=0))

        constraint = And(constraint, negation_constraint)

        return constraint
