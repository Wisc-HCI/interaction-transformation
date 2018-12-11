from z3 import *

import time

class Solver():

    def __init__(self, trajectories, inputs, outputs):
        self.trajs = trajectories

        # get input and output dictionaries
        self.inputs = inputs.alphabet
        self.rev_inputs = inputs.rev_alphabet
        self.outputs = outputs.alphabet
        self.rev_outputs = outputs.rev_alphabet

        # hardcoded values
        self.MAX_STATES = 8

    def solve(self):

        print("SOLVER --> setting up problem")

        # bitvector that decides whether a trajectory is included or not
        B = {}
        for i in range(len(self.trajs)):
            traj = self.trajs[i]
            B[traj] = Real("b_{}".format(i))

        # calculate score of each trajectory
        self.score = self.simple_score()

        # integer that determines the number of states in the final program
        n = Int('n')

        # function that maps states + inputs to microinteractions
        #f_A = Function("f_A",IntSort(),IntSort(),IntSort())

        # function that maps states + inputs to states
        f_T = Function("f_T",IntSort(),IntSort(),IntSort())

        # function that maps states to microinteractions
        f_M = Function("f_M", IntSort(),IntSort())

        # initial state
        I = Int('I')

        constraints = self.make_constraints(B, n, f_T, f_M, I)
        objective = 0
        for traj in self.trajs:
            print(self.score[traj])
            objective += B[traj] * self.score[traj]

        print(objective)
        print(self.score)
        print("SOLVER --> setting up optimization problem")
        o = Optimize()
        o.add(constraints)
        h = o.maximize(objective)

        print("SOLVER --> solving")
        start_time = time.time()
        satisfaction = o.check()
        curr_time = time.time()
        print("SOLVER --> done solving -- {} seconds".format(curr_time - start_time))

        if satisfaction == sat:

            o.upper(h)
            m = o.model()
            print(m)

        solution = self.package_results(m, f_T, f_M, n)
        curr_time = time.time()
        print("SOLVER --> entire process took {} seconds".format(curr_time - start_time))
        print("SOLVER --> returning solution")
        return solution

    def make_constraints(self, B, n, f_T, f_M, I):
        constraints = And(True)

        # ensure that there is at least one state
        constraints = And(constraints, n>=1)

        # ensure that there are no more that 20 states
        constraints = And(constraints, n<=self.MAX_STATES)

        # assign the initial state to 0
        constraints = And(constraints, I==0)

        # prevent state -1 from going anywhere but -1
        for inp in self.inputs:
            constraints = And(constraints, f_T(-1,self.inputs[inp]) == -1)

        # make the output of state -1 be -1
        constraints = And(constraints, f_M(-1)==-1)

        # include / exclude traces
        for idx in range(len(self.trajs)):
            traj = self.trajs[idx]
            traj_constraint = And(True)

            sts = [Int("sts_{}_{}".format(idx,i)) for i in range(self.MAX_STATES+1)] # in range n+1
            traj_constraint = And(traj_constraint, sts[0]==0)

            # first state
            traj_micro = And(True, f_M(0)==self.outputs[traj.vect[0][1].type])

            # next states
            for i in range(1, len(traj.vect)):
                step = traj.vect[i]
                traj_constraint = And(traj_constraint, f_T(sts[i-1],self.inputs[traj.vect[i][0].type])==sts[i])
                traj_micro = And(traj_micro, f_M(sts[i])==self.outputs[traj.vect[i][1].type])

            constraints = And(constraints, Or(B[traj]==0,B[traj]==1))
            constraints = And(constraints, Implies(And(traj_constraint,traj_micro),B[traj]==1))
            constraints = And(constraints, Implies(B[traj]==1,And(traj_constraint,traj_micro)))
            constraints = And(constraints, Implies(And(traj_constraint,Not(traj_micro)),B[traj]==0))
            constraints = And(constraints, Implies(B[traj]==0,And(traj_constraint,Not(traj_micro))))

        # force outputs leading to a state to be the same (thus, states correspond with the robot's output)
        combos = []
        inputs = list(self.inputs.keys())
        for inp in range(self.MAX_STATES):
            for inp_string in inputs:
                combos.append((inp,inp_string))

        '''
        for i in range(len(combos)):
            for j in range(i, len(combos)):
                inp1 = combos[i][0]
                sig1 = self.inputs[combos[i][1]]
                inp2 = combos[j][0]
                sig2 = self.inputs[combos[j][1]]
                constraints = And(constraints,
                                       Implies(f_T(inp1,sig1)==f_T(inp2,sig2),
                                               f_A(inp1,sig1)==f_A(inp2,sig2)),
                                              f_M(f_T(inp1,sig1))==f_A(inp2,sig2))
        '''

        constraints = And(constraints,f_M(0)==0)

        '''
		#the results of f_A should never be below 0 or above len(omega)
        for st in range(5):
            for inp in self.inputs:
                constraints = And(constraints, f_A(st,self.inputs[inp])>=0)
                constraints = And(constraints, f_A(st,self.inputs[inp])<len(self.outputs))
        '''
        # the results of f_M should never be below 0 or above len(outputs)
        for st in range(self.MAX_STATES):
            constraints = And(constraints, f_M(st)>=0)
            constraints = And(constraints, f_M(st)<len(self.outputs))

        # the results of f_T should never be below -1 or above n
        for st in range(self.MAX_STATES):
            for inp in self.inputs:
                constraints = And(constraints, f_T(st,self.inputs[inp])>=-1)
                constraints = And(constraints, f_T(st,self.inputs[inp])<n)

        # ensure the farewell property
        farewell_property = self.farewell_prop(f_T,f_M,I,n)
        constraints = And(constraints, farewell_property)

        # ensure the end property
        end_property = self.end_prop(f_T,f_M,n)
        constraints = And(constraints, end_property)

        return constraints

    def M_k(self, f_T, I, vars):
        constraint_path = And(True)
        # initial state
        # constraint_path = vars[0] == I

        # all other states
        for i in range(self.MAX_STATES):
            constraint_next = Or(False)
            for inp in self.inputs:
                constraint_next = Or(constraint_next, f_T(vars[i],self.inputs[inp]) == vars[i+1])
            constraint_path = And(constraint_path, constraint_next)

        return constraint_path

    def L_k(self, f_T):
        L_k = Or(False)
        for i in range(self.MAX_STATES):
            L_k = Or(L_k, f_T(4,i)>=0)
        return L_k

    # THESE PROPERTIES ARE GREATLY SIMPLIFIED
    def farewell_loop(self, f_T, vars):
        prop = Or(False)
        for l in range(self.MAX_STATES):
            lL_k = f_T(4,l)>=0


    def farewell_noloop(self, f_T, f_M, vars, n):
        prop = Or(False)
        for i in range(self.MAX_STATES):
            prop = Or(prop, f_M(vars[i])==self.outputs["Farewell"])
            #prop = Or(prop,vars[i]==4)
        return prop
    ####

    def farewell_prop(self, f_T, f_M, I,n):

        # make n variables
        vars = []
        vars_nonzero = []
        for i in range(self.MAX_STATES + 1):
            vars.append(Int('M_k_{}'.format(i)))
            if i > 0:
                vars_nonzero.append(vars[-1])

        # obtain M_k
        M_k = self.M_k(f_T, I, vars)

        # obtain L_k
        L_k = self.L_k(f_T)

        # non-loop condition
        no_loop = self.farewell_noloop(f_T, f_M, vars, n)

        # loop condition
        #loop = self.farewell_loop(f_T, vars)

        # there exists a path that does not lead to farewell
        #prop = Not( And(M_k, And(Not(L_k),Not(no_loop))) )
        #prop = ForAll(vars_nonzero, Not( And(M_k, Not(no_loop))))
        prop = Not(Exists(vars_nonzero, And(M_k,Not(no_loop))))
        prop = And(prop, vars[0]==I)

        return prop

    def end_prop(self, f_T, f_M,n):
        prop = And(True)
        for st in range(self.MAX_STATES):
            for inp in self.rev_inputs:
                prop = And(prop, Implies(f_M(st)==self.outputs["Farewell"],
                                         f_T(st,inp)==-1))
        return prop

    def simple_score(self):
        scores = {}

        for traj in self.trajs:
            traj_score = 0
            for step in traj.vect:
                traj_score += step[1].weight
            scores[traj] = traj_score

        return scores

    def package_results(self, m, f_T, f_M, n, demos=None):
        results = []
        n = int(str(m.evaluate(n)))

        for state in range(0,n):
            for inp in self.inputs:
                target = int(str(m.evaluate(f_T(state,self.inputs[inp]))))
                #target_output = m.evaluate(f_A(state,self.inputs[inp]))
                id = m.evaluate(f_M(state))
                id = self.rev_outputs[int(str(id))]   # string

                io = (state, inp, target, id)
                results.append(io)

        return Solution(results,demos,n)

class Solution:

    def __init__(self, results, demos, n):
        self.results = results
        self.demos = demos
        self.n = n
        self.state_target_map = {}
        for result in results:
            if result[0] not in self.state_target_map:
                self.state_target_map[result[0]] = {}
            self.state_target_map[result[0]][result[1]] = result[2]

    def get_reachability(self):
        '''
        TODO: IMPLEMENT PROPERLY
        '''
        states = {}
        for i in range(self.n):

            final = True
            for inp in self.state_target_map[i]:
                if self.state_target_map[i][inp] != -1:
                    final=False

            states[i] = {"outputs": None, "reach": True, "gesture": None, "final": final}
        return states
