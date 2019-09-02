import time

from smt_setup import *
from verification.model_checker import *
from adapter import Adapter
from state_machine import *
from z3 import *

class Z3Adapt(Adapter):

    def __init__(self, TS, micro_selection, trajs, inputs, outputs, freqs, mod_perc, path_to_interaction, updated_trace_panel, log, combined_raw_trajs):
        super(Z3Adapt, self).__init__(TS,inputs,outputs,int(round(mod_perc*(len(inputs.alphabet)*len(TS.states)))),int(round(mod_perc*(len(TS.states)))),path_to_interaction)
        self.trajs = trajs
        self.micro_selection = micro_selection
        self.path_to_interaction = path_to_interaction

        self.setup_helper = SMTSetup()

        self.localize_faults(self.trajs)

    def adapt(self):

        # get the set of moddable_sts
        self.moddable_sts = self.determine_modifiable_states(self.TS)
        self.moddable_trans = self.determine_modifiable_transitions(self.TS)

        for trans in self.moddable_trans:
            print(str(trans))

        # create mapping of state2id
        self.state2id = {self.TS.init: 0}
        self.state2id_rev = {0:self.TS.init}
        self.max_state_id = 0
        idx = 1
        for state_name,state in self.TS.states.items():
            if state != self.TS.init:
                self.state2id[state] = idx
                self.state2id_rev[idx] = state
                self.max_state_id += 1
                idx += 1

        # create mapping of micro2id
        self.micro2id = {}
        self.micro2id_rev = {}
        idx = 0
        for micro in self.micro_selection:
            self.micro2id_rev[idx] = micro["name"]
            self.micro2id[micro["name"]] = idx
            idx += 1

        # create a mapping of input2id
        self.input2id = {}
        self.input2id_rev = {}
        idx = 0
        for inp in self.inputs.alphabet:
            self.input2id_rev[idx] = inp
            self.input2id[inp] = idx
            idx += 1

        # create a mapping of each microinteraction to all the states it could possible reside in
        self.micro2states = {}
        for micro in self.micro2id:
            self.micro2states[micro] = []
            for state in self.state2id:
                if state in self.moddable_sts:
                    self.micro2states[micro].append(state)
                else:
                    if state.micros[0]["name"] == micro:
                        self.micro2states[micro].append(state)

        '''
        # bitvector that decides whether a trajectory is included or not
        B = {}
        for i in range(len(self.trajs)):
            traj = self.trajs[i]
            B[traj] = Real("b_{}".format(i))

        # calculate score of each trajectory
        self.score = self.simple_score()
        '''

        # function that maps states + inputs to states
        f_T = Function("f_T",IntSort(), IntSort(),IntSort())
        # function that maps state ID's to state microinteractions
        f_M = Function("f_M", IntSort(),IntSort())

        # set transitions and micros based on their current id
        setup_constraints = self.setup_TS(f_T,f_M)

        # setup score variable
        scores = [Int("score_{}".format(i)) for i in range(len(self.trajs))]

        # trajectory constraints
        traj_constraints = And(True)
        for i in range(len(self.trajs)):
            traj = self.trajs[i]
            #if not traj.is_prefix:
            single_traj_constraint, traj_hard_constraint = self.make_traj_constraint(traj,i,f_T,f_M,scores[i])
            traj_constraints = And(traj_constraints, single_traj_constraint, traj_hard_constraint)

        # add all constraints together
        constraints = And(setup_constraints,traj_constraints)

        objective = Sum(scores)

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
            for i in range(len(self.trajs)):
                traj = self.trajs[i]
                #if not traj.is_prefix:
                print("{} - {}".format(m.evaluate(scores[i]),traj.reward))
            print(m.evaluate(objective))
            #for st,idx in self.state2id.items():
            #    print("state {} is {}".format(st,idx))
            #for inp,idx in self.input2id.items():
            #    print("input {} is {}".format(inp,idx))
            #for i in self.state2id_rev:
            #    for j in self.input2id_rev:
            #        print("f_T {}+{}={}".format(i,j,m.evaluate(f_T(i,j))))
            #    print("f_M {}={}".format(i,m.evaluate(f_M(i))))
            self.build_TS_from_solution(self.TS,m,f_M,f_T)

        else:
            print("ERROR: no solution")

        exit()

    def build_TS_from_solution(self,old_TS,m,f_M,f_T):
        states = {}  # {name} = state
        init = None
        # create the states
        for state_orig,id in self.state2id.items():
            state_micro_id = int(str(m.evaluate(f_M(id))))
            if state_micro_id == -1:
                continue
            state_micro = self.micro2id_rev[state_micro_id]
            state_name = state_micro

            # ensure state_name is unique
            while state_name in states:
                state_name = state_name+"0"

            new_state = State(state_name,str(id),state_micro)
            if old_TS.init == state_orig:
                init = new_state
            states[new_state.name] = new_state

        # transitions
        transitions = {}
        for _,s1 in self.state2id.items():
            transitions[str(s1)] = {}
            for _,s2 in self.state2id.items():
                transitions[str(s1)][str(s2)] = []

        # create the transitions
        for state_orig,state_id in self.state2id.items():
            for inp_name,inp_id in self.input2id.items():
                target_state_id = int(str(m.evaluate(f_T(state_id,inp_id))))
                if target_state_id == -1:
                    continue
                new_trans = Transition(str(state_id),str(target_state_id),inp_name)
                transitions[str(state_id)][str(target_state_id)].append(new_trans)

        # create TS
        new_TS = TS(states,transitions,init)
        for state_name,state in states.items():
            print(str(state))
        for source_id,tar_dict in self.TS.transitions.items():
            for target_id,trans_list in tar_dict.items():
                for trans in trans_list:
                    print(str(trans))

        # link everything together
        SMUtil().build(new_TS.transitions, new_TS.states)

        print(str(new_TS))

    def make_traj_constraint(self,traj,id,f_T,f_M,score):
        traj_constraint = And(True)
        hard_constraint = And(True)

        exists_within = And(True)
        sts = [Int("traj_st_{}_{}".format(id,i)) for i in range(len(traj.vect))]
        hard_constraint = And(hard_constraint,sts[0]==0)
        for st in sts:
            hard_constraint = And(hard_constraint,And(st>-1,st<len(self.state2id)))
        vect = traj.vect

        # calculate more restrictions on sts
        for i in range(len(vect)):
            v = vect[i]
            if v[1].type != "END":
                or_const_micro = Or(False)
                for state_option in self.micro2states[v[1].type]:
                    or_const_micro = Or(or_const_micro,sts[i]==self.state2id[state_option])
                hard_constraint = And(hard_constraint,or_const_micro)

        if not traj.is_prefix:
            #print("\n~~~~~~~~")
            print(str(traj))
            for i in range(len(vect)-2):
                #print("{} ++ {}".format(vect[i][0].type,vect[i][1].type))
                condition_id = self.input2id[vect[i+1][0].type]
                exists_within = And(exists_within,f_T(sts[i],condition_id)==sts[i+1])
                exists_within = And(exists_within,f_M(sts[i])==self.micro2id[vect[i][1].type])
            end_condition_id = self.input2id[vect[-1][0].type]
            exists_within = And(exists_within,f_T(sts[len(vect)-2],end_condition_id)==-1)
            exists_within = And(exists_within,f_M(sts[len(vect)-2])==self.micro2id[vect[len(vect)-2][1].type])
        else:
            print(str(traj))
            for i in range(len(vect)-1):
                condition_id = self.input2id[vect[i+1][0].type]
                exists_within = And(exists_within,f_T(sts[i],condition_id)==sts[i+1])
                exists_within = And(exists_within,f_M(sts[i])==self.micro2id[vect[i][1].type])
            exists_within = And(exists_within,f_M(sts[len(vect)-1])==self.micro2id[vect[len(vect)-1][1].type])

        int_reward = int(round(traj.reward*100))
        traj_constraint = And(traj_constraint,Implies(exists_within,score==int_reward))
        traj_constraint = And(traj_constraint,Implies(score==int_reward,exists_within))
        traj_constraint = And(traj_constraint,Implies(Not(exists_within),score==0))
        traj_constraint = And(traj_constraint,Implies(score==0,Not(exists_within)))

        #traj_constraint = And(traj_constraint,score==traj.reward)

        return traj_constraint,hard_constraint

    def setup_TS(self,f_T,f_M):
        setup_constraints = And(True)

        # TRANSITIONS
        sourcecon2trans = {}
        for state_name,state in self.TS.states.items():
            sourcecon2trans[state] = {}
            for inp in self.inputs.alphabet:
                sourcecon2trans[state][inp] = None
        for source_id,tar_dict in self.TS.transitions.items():
            for target_id,trans_list in tar_dict.items():
                for trans in trans_list:
                    cons = trans.condition
                    sourcecon2trans[self.TS.id2state[source_id]][cons] = trans

        for source_state, cons_dict in sourcecon2trans.items():
            for cons,trans in cons_dict.items():
                source_state_id = self.state2id[source_state]
                cons_id = self.input2id[cons]
                if trans is None:
                    setup_constraints = And(setup_constraints, f_T(source_state_id,cons_id)==-1)
                elif trans not in self.moddable_trans:
                    target_id = self.state2id[trans.target]
                    setup_constraints = And(setup_constraints, f_T(source_state_id,cons_id)==target_id)
                else: # it is in moddable_trans
                    setup_constraints = And(setup_constraints, f_T(source_state_id,cons_id)>-1)
                    #setup_constraints = And(setup_constraints, f_T(source_state_id,cons_id)<=self.max_state_id)

        # STATES
        for state_name,state in self.TS.states.items():

            # handle everything outside of the moddable states
            if state not in self.moddable_sts:
                state_micro_id = self.micro2id[state.micros[0]["name"]]
                state_id = self.state2id[state]
                setup_constraints = And(setup_constraints,f_M(state_id)==state_micro_id)

            # handle the moddable states
            else:
                curr_state = state.micros[0]["name"]
                other_states = self.modstate2availstates
                other_states[state].append({"name": curr_state})

                # give a big OR block
                orblock = Or(False)
                for avail_micro in other_states[state]:
                    avail_state_micro_id = self.micro2id[avail_micro["name"]]
                    state_id = self.state2id[state]
                    orblock = Or(orblock,f_M(state_id)==avail_state_micro_id)
                setup_constraints = And(setup_constraints,orblock)

        # place bounds
        for i in self.state2id_rev:
            setup_constraints = And(setup_constraints,f_M(i)>=-1,f_M(i)<len(self.micro2id))
        for i in self.state2id_rev:
            for j in self.input2id_rev:
                setup_constraints = And(setup_constraints,f_T(i,j)>=-1,f_T(i,j)<len(self.state2id))

        # handle the -1's
        setup_constraints = And(setup_constraints,f_M(-1)==-1)
        for i in range(len(self.state2id)):
            setup_constraints = And(setup_constraints,f_M(i)>-1)
        for i in range(len(self.micro2id)):
            setup_constraints = And(setup_constraints,f_T(-1,i)==-1)

        return setup_constraints

    def simple_score(self):
        scores = {}

        for traj in self.trajs:
            scores[traj] = traj.reward

        return scores
