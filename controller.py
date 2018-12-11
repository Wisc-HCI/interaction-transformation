import threading

from interaction_components import *
from mcmc_repair import *
from verification.prism_util import *
from trace_generator import *

class Controller:

    def __init__(self, TS, num_processes):
        self.TS = TS
        self.freqs = Frequencies()
        self.inputs = InputAlphabet()
        self.outputs = OutputAlphabet()

        self.freqs.build_ds(self.inputs, self.outputs)

        num_other_processes = int(num_processes) - 1
        self.prisms = [Checker(i) for i in range(9990,9990+num_other_processes)]
        self.prisms.append(Checker(9999))
        self.prism_converter = ConvertToPrism(self.inputs)

        prism_threads = {}
        for i in range(len(self.prisms)):
            prism_threads[i] = threading.Thread(target=self.prisms[i].connect)
            prism_threads[i].daemon = True
            prism_threads[i].start()

        for key in prism_threads.keys():
            prism_threads[key].join()

        self.prisms[0].split_property_file("interaction.props", int(num_processes))

        '''
        traj1 = Trajectory([(HumanInput("Ready"),Microinteraction("Wait",0)),
                            (HumanInput("Ignore"),Microinteraction("Wait",0)),
                            (HumanInput("Ready"),Microinteraction("Greeter",0)),
                            (HumanInput("Ready"),Microinteraction("Remark",0)),
                            (HumanInput("Ignore"),Microinteraction("Remark",-1)),
                            (HumanInput("Ignore"),Microinteraction("Remark",-1)),
                            (HumanInput("Ignore"),Microinteraction("Wait",-1))], 0.8)
        traj2 = Trajectory([(HumanInput("Ready"),Microinteraction("Wait",0)),
                            (HumanInput("Ready"),Microinteraction("Greeter",0)),
                            (HumanInput("Ready"),Microinteraction("Remark",1)),
                            (HumanInput("Ready"),Microinteraction("Remark",1)),
                            (HumanInput("Ready"),Microinteraction("Remark",1)),
                            (HumanInput("Ready"),Microinteraction("Remark",1)),
                            (HumanInput("Ready"),Microinteraction("Remark",1)),
                            (HumanInput("Ready"),Microinteraction("Wait",0))], 1)
        traj3 = Trajectory([(HumanInput("Ready"),Microinteraction("Wait",0)),
                            (HumanInput("Ready"),Microinteraction("Greeter",0)),
                            (HumanInput("Ignore"),Microinteraction("Wait",0)),
                            (HumanInput("Ready"),Microinteraction("Greeter",0)),
                            (HumanInput("Ready"),Microinteraction("Remark",0)),
                            (HumanInput("Ignore"),Microinteraction("Remark",-1)),
                            (HumanInput("Ignore"),Microinteraction("Remark",-1)),
                            (HumanInput("Ready"),Microinteraction("Remark",1)),
                            (HumanInput("Ignore"),Microinteraction("Remark",-1)),
                            (HumanInput("Ignore"),Microinteraction("Wait",-1))], 0.7)
        traj4 = Trajectory([(HumanInput("Ready"),Microinteraction("Wait")),
                            (HumanInput("Ignore"),Microinteraction("Wait", 1)),
                            (HumanInput("Ignore"),Microinteraction("Remark", -1)),
                            (HumanInput("Ready"),Microinteraction("Remark", 1)),
                            (HumanInput("Ignore"),Microinteraction("Remark", 1)),
                            (HumanInput("Ignore"),Microinteraction("Wait", 1))], 0.9)
        traj5 = Trajectory([(HumanInput("Ready"),Microinteraction("Wait", 0)),
                            (HumanInput("Ready"),Microinteraction("Answer", 1)),
                            (HumanInput("Ready"),Microinteraction("Remark", -1)),
                            (HumanInput("Ready"),Microinteraction("Answer", 1))], 0.5)
        traj6 = Trajectory([(HumanInput("Ready"),Microinteraction("Wait")),
                            (HumanInput("Ignore"),Microinteraction("Wait", 1)),
                            (HumanInput("Ignore"),Microinteraction("Remark", -1)),
                            (HumanInput("Ignore"),Microinteraction("Answer", 1))], 0.4)
        '''


        '''
        traj1 = Trajectory([(HumanInput("Ready"),Microinteraction("Greeter",1)),
                            (HumanInput("Ready"),Microinteraction("Handoff",1)),
                            (HumanInput("Ready"),Microinteraction("Farewell",1))], 1)
        traj2 = Trajectory([(HumanInput("Ready"),Microinteraction("Greeter",1)),
                            (HumanInput("Ignore"),Microinteraction("Handoff",-1)),
                            (HumanInput("Ignore"),Microinteraction("Farewell",-1))], -1)
        traj3 = Trajectory([(HumanInput("Ready"),Microinteraction("Greeter",1)),
                            (HumanInput("Ignore"),Microinteraction("Greeter",-1)),
                            (HumanInput("Ignore"),Microinteraction("Farewell",-1))], -1)
        traj4 = Trajectory([(HumanInput("Ready"),Microinteraction("Greeter",1)),
                            (HumanInput("Ignore"),Microinteraction("Farewell",1))], 1)
        traj5 = Trajectory([(HumanInput("Ready"),Microinteraction("Greeter",1)),
                            (HumanInput("Ready"),Microinteraction("Remark",1)),
                            (HumanInput("Ready"),Microinteraction("Handoff",1)),
                            (HumanInput("Ignore"),Microinteraction("Farewell",1))], 1)
        traj6 = Trajectory([(HumanInput("Ready"),Microinteraction("Greeter",1)),
                            (HumanInput("Ignore"),Microinteraction("Remark",1)),
                            (HumanInput("Ignore"),Microinteraction("Farewell",-1))], 0)
        traj7 = Trajectory([(HumanInput("Ready"),Microinteraction("Greeter",1)),
                            (HumanInput("Ignore"),Microinteraction("Remark",-1)),
                            (HumanInput("Ignore"),Microinteraction("Remark",-1)),
                            (HumanInput("Ignore"),Microinteraction("Farewell",-1))], -1)
        traj8 = Trajectory([(HumanInput("Ready"),Microinteraction("Greeter",1)),
                            (HumanInput("Ignore"),Microinteraction("Remark",1))], 1)

        self.trajs = [traj1,traj2,traj3,traj4,traj5,traj6,traj7,traj8]
        '''

        '''self.trajs = [traj1,traj2,traj3,traj4,traj5,traj6]'''
        tracegen = TraceGenerator(self.TS)
        self.trajs = tracegen.get_trajectories(100)
        self.freqs.calculate_freqs(self.trajs)
        self.freqs.calculate_probabilities(self.inputs, self.outputs)

    def mcmc_adapt(self, TS, micro_selection, reward_window, progress_window, cost_window, prop_window, distance_window):
        mcmc = MCMCAdapt(TS, micro_selection, self.trajs, self.inputs, self.outputs, self.freqs, self.prisms, self.prism_converter)
        return mcmc.adapt(0.1, reward_window, progress_window, cost_window, prop_window, distance_window)

    def z3_adapt(self):
        solver = Solver(self.trajs, InputAlphabet(), OutputAlphabet())
        return solver.solve()
