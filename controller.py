import threading

from interaction_components import *
from mcmc_repair import *
from json_exporter import *
from verification.prism_util import *
from trace_generator import *
from reader import *

class Controller:

    def __init__(self):
        # read the interaction
        self.json_exp = JSONExporter()
        self.TS, self.micro_selection = Reader("interaction.xml").build()
        st_reachables = {}
        for state in self.TS.states:
            st_reachables[state] = True

        self.freqs = Frequencies()
        self.inputs = InputAlphabet()
        self.outputs = OutputAlphabet()

        # generate FAKE sample traces
        tracegen = TraceGenerator(self.TS)
        self.trajs = tracegen.get_trajectories(100)

        # consolidate the trajectories


        # calculate frequencies associated with states
        self.freqs.build_ds(self.inputs, self.outputs)
        self.freqs.calculate_freqs(self.trajs)
        self.freqs.calculate_probabilities(self.inputs, self.outputs)

        self.json_exp.export_from_object(self.TS, st_reachables, self.freqs)

    def mcmc_adapt(self, reward_window, progress_window, cost_window, prop_window, distance_window, update_trace_panel):
        mcmc = MCMCAdapt(self.TS, self.micro_selection, self.trajs, self.inputs, self.outputs, self.freqs, update_trace_panel)
        self.TS, st_reachables = mcmc.adapt(0.2, reward_window, progress_window, cost_window, prop_window, distance_window)
        self.json_exp.export_from_object(self.TS, st_reachables, self.freqs)

    def z3_adapt(self):
        solver = Solver(self.trajs, InputAlphabet(), OutputAlphabet())
        return solver.solve()
