from z3 import *
from kosajaru import *

class Properties:

    def __init__(self, inputs, outputs):
        self.inputs = inputs.alphabet
        self.micros = outputs.alphabet

    def compute_constraints(self, TS, setup_helper, removed_transitions):

        self.outputs = {TS.init.name: 0}
        self.original_outputs = {}
        idx = 1
        for state in TS.states:
            self.original_outputs[state] = int(TS.states[state].id)
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

        #print("Initiating bounded model checker. n={}".format(n))

        # interaction must end
        #print("Checking property 0...")
        kosa = Kosajaru(TS)
        strong_sccs = kosa.compute(self.inputs)
        #for scc in strong_sccs:
            #print(str(scc))
        if len(strong_sccs) == 0:
            results.append(1)
            counterexamples.append(None)
        else:
            kosa_results = [kosa.get_scc_counterexample(scc,self.inputs) for scc in strong_sccs]
            kosa_results = [(ks,True,self.original_outputs) for ks in kosa_results if ks is not None]
            if len(kosa_results) > 0:
                results.append(0)
                for kr in kosa_results:
                    counterexamples.append(kr)
                    print("FOUND KOSA COUNTEREXAMPLE")
            else:
                results.append(1)
                counterexamples.append(None)

        s = Solver()
        #print("Checking property 1...")
        sts3 = [Int("st_{}_3".format(i)) for i in range(2*n)]
        inps3 = [Int("inp_{}_3".format(i)) for i in range(2*n-1)]
        path_constraint = setup_helper.counterexample(f_T, f_M, inps3, sts3, n, self.inputs, self.outputs, size=2*n)
        s.add(And(self.farewell_exists_constraint(f_T, f_M, n, self.inputs, self.outputs, self.micros, inps3, sts3),setup_constraints, path_constraint))
        result = s.check()
        if result == sat:
            results.append(0)
            m=s.model()
            #print(m)
            raw_trajectory = setup_helper.get_result(m,inps3,sts3,n)
            counterexamples.append((raw_trajectory, False, self.outputs))
            print("FOUND FAREWELL EXISTS COUNTEREXAMPLE")
        else:
            results.append(1)
            counterexamples.append(None)

        s = Solver()
        #print("Checking property 2...")
        sts4 = [Int("st_{}_4".format(i)) for i in range(2*n+1)]
        inps4 = [Int("inp_{}_4".format(i)) for i in range(2*n)]
        path_constraint = setup_helper.counterexample(f_T, f_M, inps4, sts4, n, self.inputs, self.outputs, size=2*n+1)
        s.add(And(self.farewell_end_constraint(f_T, f_M, n, self.inputs, self.outputs, self.micros, inps4, sts4),setup_constraints, path_constraint))
        result = s.check()
        if result == sat:
            results.append(0)
            m=s.model()
            #print(m)
            raw_trajectory = setup_helper.get_result(m,inps4,sts4,n)
            counterexamples.append((raw_trajectory, False, self.outputs))
            print("FOUND FAREWELL END CONSTRAINT COUNTEREXAMPLE")
        else:
            results.append(1)
            counterexamples.append(None)

        return results, counterexamples

    def farewell_exists_constraint(self, f_T, f_M, n, inputs, outputs, micros, inps, sts):
        constraint = And(True)

        negation_constraint = Or(False)
        for i in range(2*n-1):
            #negation_constraint = Or(negation_constraint, And(sts[i]>=0, f_M(sts[i])==outputs["Farewell"], f_T(sts[i], inputs["Ready"])==-1, f_T(sts[i], inputs["Ignore"])==-1))
            negation_constraint = Or(negation_constraint, And(sts[i]>=0,f_M(sts[i])==micros["Bye"]))

        constraint = And(constraint, Not(negation_constraint))

        return constraint

    def farewell_end_constraint(self, f_T, f_M, n, inputs, outputs, micros, inps, sts):
        constraint = And(True)

        negation_constraint = Or(False)
        for i in range(2*n-1):
            #negation_constraint = Or(negation_constraint, And(sts[i]>=0, f_M(sts[i])==outputs["Farewell"], f_T(sts[i], inputs["Ready"])==-1, f_T(sts[i], inputs["Ignore"])==-1))
            negation_constraint = Or(negation_constraint, And(sts[i]>=0,f_M(sts[i])==micros["Bye"], sts[i+1]>=0))

        constraint = And(constraint, negation_constraint)

        return constraint
