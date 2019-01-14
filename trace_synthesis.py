from z3 import *

import time

class Solver():

    def __init__(self, trajectories, inputs, outputs, max_mods):
        self.trajs = trajectories

        # get input and output dictionaries
        self.inputs = inputs.alphabet
        self.rev_inputs = inputs.rev_alphabet
        self.outputs = outputs.alphabet
        self.rev_outputs = outputs.rev_alphabet

        self.max_mods = max_mods

    def solve(self,TS,removed_transitions):

        self.MAX_STATES = len(TS.states) + self.max_mods

        print("SOLVER --> setting up problem")

        # set up constraints for existing interaction
        self.out_map = {TS.init.name: 0}
        micros = self.outputs
        idx = 1
        for state in TS.states:
            if state != TS.init.name:
                self.out_map[state] = idx
                idx += 1
        # function that maps states + inputs to states
        f_T_e = Function("f_T_e",IntSort(), IntSort(),IntSort())
        # function that maps state ID's to state microinteractions
        f_M_e = Function("f_M_e", IntSort(),IntSort())
        setup_constraints = And(True)
        states = TS.states
        # set up f_M_e
        for _,state in states.items():
            setup_constraints = And(setup_constraints, f_M_e(self.out_map[state.name]) == micros[state.micros[0]["name"]])
        # set up f_T_e
        for source,temp in TS.transitions.items():
            for target,conditions in temp.items():
                for trans in conditions:
                    setup_constraints = And(setup_constraints, f_T_e(self.out_map[trans.source.name], self.inputs[trans.condition]) == self.out_map[trans.target.name])
        for trans in removed_transitions:
            setup_constraints = And(setup_constraints, f_T_e(self.out_map[trans.source.name], self.inputs[trans.condition])==-1)
        for inp in self.inputs:
            setup_constraints = And(setup_constraints, f_T_e(-1, self.inputs[inp])==-1)

        # bitvector that decides whether a trajectory is included or not
        B = {}
        for i in range(len(self.trajs)):
            traj = self.trajs[i]
            B[traj] = Real("b_{}".format(i))

        # bitvector that decides whether a modification has been made
        Mods = {}
        i = 0
        for state_name,state in TS.states.items():
            Mods[self.out_map[state.name]] = {}
            for inp in self.inputs:
                Mods[self.out_map[state.name]][self.inputs[inp]] = Real("mod_{}".format(i))
                i += 1

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

        constraints = And(setup_constraints,self.make_constraints(TS,Mods,B, n, f_T, f_T_e, f_M, I))
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

        else:
            print("ERROR: no solution")
            exit()

        solution = self.package_results(m, f_T, f_M, n)
        curr_time = time.time()
        print("SOLVER --> entire process took {} seconds".format(curr_time - start_time))
        print("SOLVER --> returning solution")
        return solution

    def make_constraints(self, TS, Mods, B, n, f_T, f_T_e, f_M, I):
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

            sts = [Int("sts_{}_{}".format(idx,i)) for i in range(2*self.MAX_STATES+1)] # in range n+1
            traj_constraint = And(traj_constraint, sts[0]==0)

            # first state
            traj_micro = And(True, f_M(0)==self.outputs[traj.vect[0][1].type])

            # next states
            for i in range(1, len(traj.vect)):
                step = traj.vect[i]
                traj_constraint = And(traj_constraint, f_T(sts[i-1],self.inputs[traj.vect[i][0].type])==sts[i])
                traj_micro = And(traj_micro, f_M(sts[i])==self.outputs[traj.vect[i][1].type])

                # set the end state
                if i == len(traj.vect)-1 and not traj.is_prefix:
                    end_constraint = Or(False)
                    for inp in self.inputs:
                        end_constraint = Or(end_constraint, f_T(sts[i],self.inputs[inp])==-1)
                    traj_constraint = And(traj_constraint,end_constraint)

            constraints = And(constraints, Or(B[traj]==0,B[traj]==1))
            constraints = And(constraints, Implies(And(traj_constraint,traj_micro),B[traj]==1))
            constraints = And(constraints, Implies(B[traj]==1,And(traj_constraint,traj_micro)))
            constraints = And(constraints, Implies(Not(And(traj_constraint,traj_micro)),B[traj]==0))
            constraints = And(constraints, Implies(B[traj]==0,Not(And(traj_constraint,traj_micro))))

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

        # state labels should be the same for pre-existing states
        for _,state in TS.states.items():
            constraints = And(constraints, f_M(self.out_map[state.name]) == self.outputs[state.micros[0]["name"]])

        # set the modification bitvector
        for state_name,state in TS.states.items():
            for inp in self.inputs:
                constraints = And(constraints, Implies(f_T(self.out_map[state.name],self.inputs[inp])==f_T_e(self.out_map[state.name],self.inputs[inp]),
                                                           Mods[self.out_map[state.name]][self.inputs[inp]]==0))
                constraints = And(constraints, Implies(f_T(self.out_map[state.name],self.inputs[inp])!=f_T_e(self.out_map[state.name],self.inputs[inp]),
                                                           Mods[self.out_map[state.name]][self.inputs[inp]]==1))

        # limit modifications to mod_limit
        mod_var_list = []
        for state_name,state in TS.states.items():
            for inp in self.inputs:
                mod_var_list.append(Mods[self.out_map[state.name]][self.inputs[inp]])

        constraints = And(constraints,Sum(mod_var_list)<=self.max_mods)

        return constraints

    def simple_score(self):
        scores = {}

        for traj in self.trajs:
            scores[traj] = traj.reward

        return scores

    def package_results(self, m, f_T, f_M, n, demos=None):
        results = []
        n = int(str(m.evaluate(n)))

        for state in range(0,n):
            for inp in self.inputs:
                target = int(str(m.evaluate(f_T(state,self.inputs[inp]))))
                #target_output = m.evaluate(f_A(state,self.inputs[inp]))
                src_name = m.evaluate(f_M(state))
                src_name = self.rev_outputs[int(str(src_name))]   # string

                tar_name = m.evaluate(f_M(target))
                tar_name = "-1" if target == -1 else self.rev_outputs[int(str(tar_name))]   # string

                io = (state, src_name, inp, target, tar_name)
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
