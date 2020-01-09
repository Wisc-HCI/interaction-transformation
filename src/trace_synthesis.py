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

        self.max_mods = 0#max_mods

    def solve(self,TS,removed_transitions):

        self.MAX_STATES = len(TS.states) #+self.max_mods

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
        print("~~~")
        for trans in removed_transitions:
            print(trans)
            setup_constraints = And(setup_constraints, f_T_e(self.out_map[trans.source.name], self.inputs[trans.condition])==-1)
        print("~~~")
        for inp in self.inputs:
            setup_constraints = And(setup_constraints, f_T_e(-1, self.inputs[inp])==-1)

        # bitvector that decides whether a trajectory is included or not
        B = {}
        for i in range(len(self.trajs)):
            traj = self.trajs[i]
            B[traj] = Real("b_{}".format(i))

        # bitvector that decides whether a TRANSITION modification has been made
        Mods = {}
        i = 0
        for state_name,state in TS.states.items():
            Mods[self.out_map[state.name]] = {}
            for inp in self.inputs:
                Mods[self.out_map[state.name]][self.inputs[inp]] = Real("mod_{}".format(i))
                i += 1

        # bitvector that decides whether a STATE identity modification has been made
        Mods_M = {}
        for state_name,state in TS.states.items():
            Mods_M[self.out_map[state.name]] = Real("mod_m_{}".format(i))
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

        # TREE CONSTRAINTS
        node_num_raw = 3

        curr_ceil = len(self.inputs)
        while True:
            if curr_ceil >= node_num_raw:
                node_num = curr_ceil + len(self.inputs)
                break
            else:
                curr_ceil = curr_ceil * len(self.inputs)

        tr_sts = [Int("tr_st{}".format(i)) for i in range(node_num)] # the nodes
        tr_m = Function("f_tr_m", IntSort(), IntSort()) # function mapping tree nodes to behavior
        tr_ch = Function("f_tr_ch", IntSort(), IntSort(), IntSort()) # function mapping tree nodes to children
        tr_pr_n = Function("f_tr_pr_n", IntSort(), IntSort()) # function mapping tree nodes to parent node
        tr_pr_a = Function("f_tr_pr_a", IntSort(), IntSort()) # function mapping tree nodes to parent action
        tr_hist = {} # dict mapping tree nodes to string

        tree_const = self.make_tree_constraints(node_num_raw, tr_sts, tr_m, tr_ch, tr_pr_n, tr_pr_a, tr_hist, f_T, f_M, I)

        constraints = And(tree_const,setup_constraints,self.make_constraints(TS,Mods,Mods_M,B, n, f_T, f_T_e, f_M, f_M_e, I))
        #constraints = And(setup_constraints)
        objective = 0
        print("SOLVER --> num trajs: {}".format(len(self.trajs)))
        for traj in self.trajs:

            objective += B[traj] * self.score[traj]

        print("SOLVER --> setting up optimization problem")
        o = Optimize()
        o.add(constraints)
        h = o.maximize(objective)

        print("SOLVER --> solving")
        start_time = time.time()
        satisfaction = o.check()
        curr_time = time.time()
        print("SOLVER --> done solving -- {} seconds".format(curr_time - start_time))

        objective_val = None
        if satisfaction == sat:

            o.upper(h)
            m = o.model()
            print(m)
            for item in B:
                print(m.evaluate(B[item]))
            objective_val = float(int(str(m.evaluate(objective).numerator()))*1.0/int(str(m.evaluate(objective).denominator())))
            print(objective_val)

        else:
            print("ERROR: no solution")
            exit()

        solution = self.package_results(m, f_T, f_M, n)
        curr_time = time.time()
        print("SOLVER --> entire process took {} seconds".format(curr_time - start_time))
        print("SOLVER --> returning solution")
        return solution,objective_val

    def make_tree_constraints(self, node_num, tr_sts, tr_m, tr_ch, tr_pr_n, tr_pr_a, tr_hist, f_T, f_M, I):
        constraints = And(True)

        # assign node ids
        for i in range(node_num):
            constraints = And(constraints,tr_sts[i]==i)

        # initialize root
        tr_hist[0]=[(0,f_M(0))]

        # set up tree structure (parents and children)
        mutable_counter = [0]
        self.setup_tree(node_num, mutable_counter, tr_sts, tr_m, tr_ch, tr_pr_n, tr_pr_a, tr_hist, constraints)

        # go down the tree and assign f_M
        # this is where we must limit loops

        # ensure that the list/string within each node is actually acheivable

        return constraints

    def convert_beh_to_string(self, st):
        return "0"

    def setup_tree(self, node_num, mutable_counter, tr_sts, tr_m, tr_ch, tr_pr_n, tr_pr_a, tr_hist, constraints):

        parent_queue = [mutable_counter[0]]

        while True:
            if mutable_counter[0] > node_num:
                break

            parent = parent_queue.pop(0)

            for j in range(1,len(self.inputs)+1):
                inp = list(self.inputs.keys())[j-1]
                mutable_counter[0] = mutable_counter[0] + 1
                curr_child = mutable_counter[0]
                print(curr_child)
                parent_queue.append(curr_child)
                constraints = And(constraints,tr_ch(tr_sts[parent], self.inputs[inp])==tr_sts[curr_child])
                constraints = And(constraints, tr_pr_n(tr_sts[curr_child])==tr_sts[parent])
                constraints = And(constraints, tr_pr_n(tr_sts[curr_child])==self.inputs[inp])
                tr_hist[curr_child]=tr_hist[parent] + [(self.inputs[inp],tr_m(curr_child))]


    def make_constraints(self, TS, Mods, Mods_M, B, n, f_T, f_T_e, f_M, f_M_e, I):
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
        print("~~~~")
        for idx in range(len(self.trajs)):
            traj = self.trajs[idx]
            traj_constraint = And(True)

            sts = [Int("sts_{}_{}".format(idx,i)) for i in range(3*self.MAX_STATES+1)] # in range n+1
            constraints = And(constraints, sts[0]==0)
            for st in sts:
                constraints = And(constraints, st >= 0, st < self.MAX_STATES)

            # first state
            traj_micro = And(True, f_M(0)==self.outputs[traj.vect[0][1].type])

            # next states
            for i in range(1, len(traj.vect)):
                print(i)
                step = traj.vect[i]
                traj_constraint = And(traj_constraint, f_T(sts[i-1],self.inputs[traj.vect[i][0].type])==sts[i])
                traj_micro = And(traj_micro, f_M(sts[i])==self.outputs[traj.vect[i][1].type])

                # set the end state
                if i == len(traj.vect)-2 and not traj.is_prefix:
                    print("HERE: {}-{}".format(traj.vect[i][0].type, traj.vect[i][1].type))
                    end_constraint = And(True)
                    for inp in self.inputs:
                        if inp == traj.vect[-1][0].type:
                            print("    {}".format(inp))
                            end_constraint = And(end_constraint, f_T(sts[i],self.inputs[inp])==-1)
                    traj_constraint = And(traj_constraint,end_constraint)

                    break  # the break acknowledges that a non-prefix trajectory has a dummy node on the end

                '''
                # additional constraints not in MCMC
                end_constraint = And(True)
                for inp in self.inputs:
                    end_constraint = And(end_constraint,Implies(And(f_M(sts[i])==self.outputs["Bye"],sts[i]>-1),
                                                                f_T(sts[i],self.inputs[inp])==-1))
                    end_constraint = And(end_constraint,Implies(And(f_M(sts[i])!=self.outputs["Bye"],sts[i]>-1),
                                                                f_T(sts[i],self.inputs[inp])>-1))

                traj_constraint = And(traj_constraint,end_constraint)
                '''

            #constraints = And(constraints, B[traj]==0)
            constraints = And(constraints, Or(B[traj]==0,B[traj]==1))
            #constraints = And(constraints, Or(B[traj]==1))
            constraints = And(constraints, Implies(And(traj_constraint,traj_micro),B[traj]==1))
            constraints = And(constraints, Implies(B[traj]==1,And(traj_constraint,traj_micro)))
            constraints = And(constraints, Implies(Not(And(traj_constraint,traj_micro)),B[traj]==0))
            constraints = And(constraints, Implies(B[traj]==0,Not(And(traj_constraint,traj_micro))))

        constraints = And(constraints,f_M(0)==0)

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
            constraints = And(constraints, Implies(f_M(self.out_map[state.name])==f_M_e(self.out_map[state.name]),
                                                       Mods_M[self.out_map[state.name]]==0))
            constraints = And(constraints, Implies(f_M(self.out_map[state.name])!=f_M_e(self.out_map[state.name]),
                                                       Mods_M[self.out_map[state.name]]==1))
            for inp in self.inputs:
                constraints = And(constraints, Implies(f_T(self.out_map[state.name],self.inputs[inp])==f_T_e(self.out_map[state.name],self.inputs[inp]),
                                                           Mods[self.out_map[state.name]][self.inputs[inp]]==0))
                constraints = And(constraints, Implies(f_T(self.out_map[state.name],self.inputs[inp])!=f_T_e(self.out_map[state.name],self.inputs[inp]),
                                                           Mods[self.out_map[state.name]][self.inputs[inp]]==1))

        # limit modifications to mod_limit
        mod_var_list = []
        for state_name,state in TS.states.items():
            mod_var_list.append(Mods_M[self.out_map[state.name]])
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
                print(self.rev_outputs)
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
