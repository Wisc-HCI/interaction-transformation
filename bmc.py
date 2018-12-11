from z3 import *

class BMC:

    def __init__(self, TS, trajectories, inputs, outputs):
        self.TS = TS
        self.trajectories = trajectories

        # get input and output dictionaries
        self.inputs = inputs.alphabet
        self.rev_inputs = inputs.rev_alphabet
        self.outputs = outputs.alphabet
        self.rev_outputs = outputs.rev_alphabet

    def setup(self, f_T, f_M,n):
        setup_constraints = And(True)

        states = self.TS.states

        # set up f_M
        for _,state in states.items():
            setup_constraints = And(setup_constraints, f_M(int(state.id)) == self.outputs[state.micros[0]["name"]])

        # set up f_T
        for source,temp in self.TS.transitions.items():
            for target,conditions in temp.items():
                for trans in conditions:
                    setup_constraints = And(setup_constraints, f_T[self.inputs[trans.condition]](trans.source.id) == trans.target.id)

        return setup_constraints

    def check(self):

        # function that maps states + inputs to states
        f_T = [Function("f_T_{}".format(i),IntSort(),IntSort()) for i in range(len(self.inputs))]

        # function that maps states to microinteractions
        f_M = Function("f_M", IntSort(),IntSort())

        # n is the number of states in the interaction
        states = self.TS.states
        n = len(self.TS.states)

        setup_constraints = self.setup(f_T, f_M, n)

        st = [Int("st_{}".format(i)) for i in range(5)]  # TODO: make this +1 so that we can reason about final state

        sats = []
        for h in range(len(self.trajectories)):
            traj = self.trajectories[h]
            traj_constraint = And(True)
            vect = traj.vect

            for s in st:
                traj_constraint = And(traj_constraint, s>=0, s<n)

            traj_constraint = And(traj_constraint, st[0]==0)
            traj_constraint = And(traj_constraint, f_M(0)==self.outputs[vect[0][1].type])
            for i in range(1,len(vect)):
                traj_constraint = And(traj_constraint, f_T[self.inputs[vect[i][0].type]](st[i-1])==st[i])
                traj_constraint = And(traj_constraint, f_M(st[i])==self.outputs[vect[i][1].type])

            s = Solver()
            s.add(And(traj_constraint,setup_constraints))
            result = s.check()

            #m=s.model()
            #print(m)
            #print(traj_constraint)
            #print(result)

            if result == sat:
                sats.append(traj.reward)

        return sats
