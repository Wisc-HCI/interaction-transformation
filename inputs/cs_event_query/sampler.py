from z3 import *

import time
import math

class Sampler:

    '''
    Sampler takes the existing trajectories as input,
    and comes up with a tree-like interaction whose
    branches are optimized to be (a) less-seen bad tra-
    jectories, (b) unseen good trajectories, and (c)
    unseen combinations of states
    '''

    def __init__(self, trajs, num_branches, inputs, outputs):

        self.trajs = trajs
        self.num_branches = num_branches
        self.inputs = inputs
        self.outputs_orig = outputs
        self.outputs = {}
        self.outputs_rev = {}
        counter = 0
        for out in self.outputs_orig:
            self.outputs[out] = counter
            self.outputs_rev[counter] = out
            counter += 1

        self.min_branch_len = 2
        self.max_branch_len = max([len(t.vect) for t in self.trajs])

        # place the trajs in a dict w/ number of matching trajs as values
        self.traj_dict = {}
        for traj in self.trajs:
            cs = traj.comparable_string()
            print(cs)
            if cs not in self.traj_dict:
                self.traj_dict[cs] = [1,traj]
            else:
                self.traj_dict[cs][0] += 1

        # weight the benefit negative vs positive trajectories
        self.neg_reward_benefit_weight = 2
        self.positive_reward_benefit_weight = 1
        self.unseen_traj_reward_benefit = 1

        # set up the normal distribution function
        self.mu = 1 # should always be 1 -- we can't weight unseen trajectories
        self.sigma = 1  # can change this to be whatever

    def solve(self):

        # which nodes each node points to
        f_T = Function("f_T", IntSort(), IntSort(), IntSort())

        # mapping nodes to tree levels
        f_L = Function("f_L", IntSort(), IntSort())

        # mapping nodes to their parents
        f_P = Function("f_P", IntSort(), IntSort())

        # mapping outputs onto states
        f_M = Function("f_M", IntSort(), IntSort())

        consts = self.make_constraints(f_T, f_L, f_M, f_P)

        paths, path_consts = self.make_paths(f_T, f_L, f_M)

        prop_constraints = self.check_paths(paths, f_M)

        objective = [Int("obj_{}".format(i)) for i in range(len(self.traj_dict)+self.num_branches)] #Int("obj")
        obj_const = self.setup_objective(objective, paths, f_T, f_M)

        #for traj in self.trajs:
            #objective += B[traj] * self.score[traj]
        #    objective = 0

        print("SOLVER --> setting up optimization problem")
        o = Solver()
        o.add(consts, path_consts, prop_constraints)
        o.add(obj_const)
        objective_func=(Sum(objective)>=7)
        #h = o.maximize(Sum(objective))
        o.add(objective_func)

        print("SOLVER --> solving")
        start_time = time.time()
        satisfaction = o.check()
        curr_time = time.time()
        print("SOLVER --> done solving -- {} seconds".format(curr_time - start_time))

        objective_val = None
        if satisfaction == sat:

            #o.upper(h)
            m = o.model()
            print(m)
            for p in paths:
                print("new path")
                for step in p:
                    print("  {} -- {}".format(m.evaluate(f_M(step)), self.outputs_rev[int(str(m.evaluate(f_M(step))))]))
                print(" ~~~")
                for step in p:
                    print("    {}".format(m.evaluate(step)))
            #print(m.evaluate(f_L))
            for obj in objective:
                print(m.evaluate(obj))

        else:
            print("ERROR: no solution")
            exit()

        #solution = self.package_results(m, f_T, f_M, n)
        #curr_time = time.time()
        print("SOLVER --> entire process took {} seconds".format(curr_time - start_time))
        print("SOLVER --> returning solution")
        #return solution,objective_val

    def setup_objective(self, obj, paths, f_T, f_M):

        obj_const = And(True)

        for o in obj:
            obj_const = And(obj_const, Or(o==0,o==1))

        traj_strings = list(self.traj_dict)
        for i in range(len(traj_strings)):
            traj_string = traj_strings[i]
            traj = self.traj_dict[traj_string][1].vect
            weight = self.traj_dict[traj_string][0]
            reward = self.traj_dict[traj_string][1].reward

            # test if it is inside
            # start with the initial state
            exists_within = And(True)
            exists_within = And(exists_within, f_M(0)==self.outputs[traj[0][1].type])
            prev_output = 0

            # do all other states

            for j in range(1, len(traj)):
                #prev_output = self.outputs[traj[j-1][1].type]
                correct_input = self.inputs[traj[j][0].type]
                print(correct_input)

                if traj[j][1].type != "END":
                    correct_output = self.outputs[traj[j][1].type]
                    print(correct_output)
                    print("~~~")
                    exists_within = And(exists_within, f_M(f_T(prev_output, correct_input))==correct_output)
                    prev_output = f_T(prev_output, correct_input)
                #else:
                #    exists_within = And(exists_within, f_T(prev_output, correct_input)==-1)


            obj_const = And(obj_const, Implies(exists_within,obj[i]==1))
            obj_const = And(obj_const, Implies(Not(exists_within),obj[i]==0))
            #obj_const = And(obj_const, obj[i]==1)

        return obj_const

    def make_constraints(self, f_T, f_L, f_M, f_P):
        constraints = And(True)

        # make the tree nodes
        num_nodes = self.num_branches * self.max_branch_len
        sts = [Int("st_{}".format(i)) for i in range(num_nodes)]
        # bc = a binary flag array showing which nodes are children
        bc = [Int("bc_{}".format(i)) for i in range(num_nodes)]

        # node identity constraints and restrict the id's of each node
        constraints = And(constraints,f_M(-1)==-1)
        for st in sts:
            constraints = And(constraints, f_M(st)>=0, f_M(st)<len(self.outputs))
            constraints = And(constraints, st>=-1, st<num_nodes)  # this is redundant

        # TREE CONSTRAINTS
        # set the ID and the level no
        constraints=And(constraints,f_L(0)==0)
        counter = 0
        for st in sts:
            constraints=And(constraints,st==counter)
            #constraints=And(constraints,f_L(st)>=0,f_L(st)<self.max_branch_len)

            if counter >= 1:  # assign states to levels
                level = math.floor((counter-1)/self.num_branches) + 1
                constraints = And(constraints,f_L(st)==level)

            counter += 1

        # f_T constraints
        for st1 in sts:
            for inp in self.inputs:
                constraints = And(constraints, f_T(st1,self.inputs[inp])>=-1, f_T(st1,self.inputs[inp])<num_nodes)
        for inp in self.inputs:
            constraints = And(constraints, f_T(-1,self.inputs[inp])==-1)

        #constraints = And(constraints, f_T(0,0)==2, f_T(0,1)==2)

        # tree level constraints
        for st1 in sts:
            for inp in self.inputs:
                for st2 in sts:
                    constraints = And(constraints,
                                      Implies(And(f_T(st1,self.inputs[inp])==st2,
                                                  st2!=-1),  # ensuring that -1's can be on different levels
                                              f_L(st1)==f_L(st2)-1))

        # leaves can only be pointed to once (definition of tree)
        for st in sts:
            for inp in self.inputs:
                constraints = And(constraints, Implies(f_T(st,self.inputs[inp])>=0,f_P(f_T(st,self.inputs[inp]))==st))

        # count how many "orphan" nodes so that we can give them extra leaves
        hangers = [Int("hanger_{}".format(i)) for i in range(len(sts))]
        constraints = And(constraints, hangers[0]==0)
        for i in range(1,len(sts)):

            constraints = And(constraints,Or(hangers[i]==0,hangers[i]==1))

            if i>0 and i<=self.num_branches:
                parents = [0]
            else:
                parent_min = (i-self.num_branches) - ((i-self.num_branches)-1)%self.num_branches
                parent_max = parent_min + (self.num_branches-1)
                parents = [j for j in range(parent_min,parent_max+1)]

            is_connected = Or(False)
            for st in parents:
                for inp in self.inputs:
                    is_connected = Or(is_connected, f_T(sts[st],self.inputs[inp])==sts[i])

            constraints = And(constraints,Implies(Not(is_connected),hangers[i]==1))
            constraints = And(constraints,Implies(is_connected,hangers[i]==0))

        # constraints on number of leaves
        for i in range(len(sts)):
            st1 = sts[i]
            for inp in self.inputs:
                constraints = And(constraints,
                                  Implies(f_T(st1,self.inputs[inp])==-1,bc[i]==1),
                                  Implies(bc[i]==1,f_T(st1,self.inputs[inp])==-1))

        for b in bc:
            constraints = And(constraints, Or(b==0,b==1))

        constraints = And(constraints, Sum(bc)==(self.num_branches + Sum(hangers)))

        return constraints

    def make_paths(self, f_T, f_L, f_M):

        path_const = And(True)

        # actually make the variables
        ps = [[Int("p_{}_{}".format(j,i)) for i in range(self.max_branch_len)] for j in range(self.num_branches)]

        # restrict the id's of the path nodes
        for p in ps:
            for p_i in p:
                path_const = And(path_const, p_i>=-1, p_i<(self.num_branches * self.max_branch_len))

        # constrain them so that they must be acheivable via f_T and f_M
        for path in ps:
            path_const = And(path_const, path[0]==0)
            for i in range(1,self.max_branch_len):
                or_const = Or(False)
                for inp in self.inputs:
                    or_const = Or(or_const, And(path[i]==f_T(path[i-1],self.inputs[inp])))
                path_const = And(path_const, or_const)

        # constrain them so that each path must be unique
        for path in ps:
            for alt_path in ps:
                if path != alt_path:
                    all_equal = And(True)
                    for i in range(self.max_branch_len):
                        all_equal = And(all_equal,path[i]==alt_path[i])

                    path_const = And(path_const, Not(all_equal))

        return ps, path_const

    def check_paths(self, paths, f_M):

        # must ensure that various properties are satisfied
        prop_constraints = And(True)

        # GREETING PROPERTY
        for path in paths:
            prop_constraints = And(prop_constraints, f_M(path[0])==self.outputs["Greet"])

        # FAREWELL PROPERTY
        for path in paths:
            for i in range(1,self.max_branch_len):
                prop_constraints = And(prop_constraints, Implies(
                                                                 And(path[i-1]>=0,path[i]==-1),
                                                                 f_M(path[i-1])==self.outputs["Bye"]),
                                                         Implies(i==(self.max_branch_len-1),
                                                                 f_M(path[i])==self.outputs["Bye"])
                )


        return prop_constraints
