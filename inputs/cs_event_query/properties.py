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

        '''
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

        s = Solver()
        #print("Checking property 2...")
        sts5 = [Int("st_{}_5".format(i)) for i in range(2*n+1)]
        inps5 = [Int("inp_{}_5".format(i)) for i in range(2*n)]
        path_constraint = setup_helper.counterexample(f_T, f_M, inps5, sts5, n, self.inputs, self.outputs, size=2*n+1)
        s.add(And(self.liveness_constraint(f_T, f_M, n, self.inputs, self.outputs, self.micros, inps5, sts5),setup_constraints, path_constraint))
        result = s.check()
        if result == sat:
            results.append(0)
            m=s.model()
            #print(m)
            raw_trajectory = setup_helper.get_result(m,inps5,sts5,n)
            counterexamples.append((raw_trajectory, False, self.outputs))
            print("FOUND HOW HELP CONSTRAINT COUNTEREXAMPLE")
        else:
            results.append(1)
            counterexamples.append(None)

        return results, counterexamples

        '''
        tup = (f_T,f_M,n)
        '''
        self.get_counterexample(3,2*n,f_T,f_M,n,self.farewell_exists_constraint,setup_helper,setup_constraints,results,counterexamples, "farewell exists")
        self.get_counterexample(4,2*n+1,f_T,f_M,n,self.farewell_end_constraint,setup_helper,setup_constraints,results,counterexamples, "farewell end")
        self.get_counterexample(5,2*n+1,f_T,f_M,n,self.liveness_constraint,setup_helper,setup_constraints,results,counterexamples, "liveness")
        self.get_counterexample(6,2*n+1,f_T,f_M,n,self.how_help_constraint,setup_helper,setup_constraints,results,counterexamples, "how help")
        self.get_counterexample(7,2*n+1,f_T,f_M,n,self.need_more_help_constraint,setup_helper,setup_constraints,results,counterexamples, "need more help")
        '''
        return results, counterexamples

    def get_counterexample(self, id, size, f_T, f_M, n, func, setup_helper, setup_constraints, results, counterexamples, label):
        s = Solver()
        #print("Checking property 2...")
        sts5 = [Int("st_{}_{}".format(i,id)) for i in range(size)]
        inps5 = [Int("inp_{}_{}".format(i,id)) for i in range(size-1)]
        path_constraint = setup_helper.counterexample(f_T, f_M, inps5, sts5, n, self.inputs, self.outputs, size=size)
        s.add(And(func(f_T, f_M, n, self.inputs, self.outputs, self.micros, inps5, sts5),setup_constraints, path_constraint))
        result = s.check()
        if result == sat:
            results.append(0)
            m=s.model()
            #print(m)
            raw_trajectory = setup_helper.get_result(m,inps5,sts5,n)
            counterexamples.append((raw_trajectory, False, self.outputs))
            print("FOUND {} CONSTRAINT COUNTEREXAMPLE".format(label))
            print("   ~~~   {}".format(raw_trajectory))
        else:
            results.append(1)
            counterexamples.append(None)

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

    def liveness_constraint(self, f_T, f_M, n, inputs, outputs, micros, inps, sts):
        '''
        In the future we need: CompleteQuery, AnswerQuery, Instruction1&Instruction2, or ListOut
        '''
        constraint = And(True)

        to_negate = Or(False)
        for i in range(2*n-1):
            to_negate = Or(to_negate, And(sts[i] >= 0, f_M(sts[i])==micros["CompleteQuery"]))
            to_negate = Or(to_negate, And(sts[i] >= 0, f_M(sts[i])==micros["AnswerQuery"]))
            to_negate = Or(to_negate, And(sts[i] >= 0, f_M(sts[i])==micros["Instruction1"]))
            to_negate = Or(to_negate, And(sts[i] >= 0, f_M(sts[i])==micros["Instruction2"]))
            to_negate = Or(to_negate, And(sts[i] >= 0, f_M(sts[i])==micros["ListOut"]))

        constraint = And(constraint, Not(to_negate))

        return constraint

    def how_help_constraint(self, f_T, f_M, n, inputs, outputs, micros, inps, sts):
        '''
        After asking how we can help them, in the future we need: CompleteQuery or ListOut
        '''
        constraint = And(True)

        to_negate = And(True)
        for i in range(2*n-1):
            temp_or = Or(False)
            for j in range(i+1, 2*n-1):
                temp_or = Or(temp_or, And(sts[j] >= 0, Or(f_M(sts[j])==micros["CompleteQuery"],
                                                          f_M(sts[j])==micros["ListOut"])))
            to_negate = And(to_negate, Implies(And(sts[i] >= 0,f_M(sts[i])==micros["HowHelp"]), temp_or))

        constraint = And(constraint, Not(to_negate))

        return constraint

    def need_more_help_constraint(self, f_T, f_M, n, inputs, outputs, micros, inps, sts):
        '''
        After asking if they need more help, in the future we need:
        CompleteQuery, AnswerQuery, Instruction1&Instruction2, or ListOut
        '''
        constraint = And(True)

        to_negate = And(True)
        for i in range(2*n-1):
            temp_or = Or(False)
            for j in range(i+1, 2*n-1):
                temp_or = Or(temp_or, And(sts[j] >= 0, Or(f_M(sts[j])==micros["CompleteQuery"],
                                                          f_M(sts[j])==micros["Instruction1"],
                                                          f_M(sts[j])==micros["Instruction2"],
                                                          f_M(sts[j])==micros["AnswerQuery"],
                                                          f_M(sts[j])==micros["ListOut"])))
            to_negate = And(to_negate, Implies(And(sts[i] >= 0,f_M(sts[i])==micros["NeedMoreHelp"]), temp_or))

        constraint = And(constraint, Not(to_negate))

        return constraint
