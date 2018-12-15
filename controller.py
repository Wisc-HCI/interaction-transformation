import threading
import importlib

from interaction_components import *
from mcmc_repair import *
from json_exporter import *
from verification.prism_util import *
from reader import *

class Controller:

    def __init__(self, path_to_interaction):
        self.path_to_interaction = path_to_interaction

        # read the interaction
        self.json_exp = JSONExporter()
        self.TS, self.micro_selection = Reader("inputs/{}/interaction.xml".format(path_to_interaction)).build()
        st_reachables = {}
        for state in self.TS.states:
            st_reachables[state] = True

        self.freqs = Frequencies()
        json_raw=open("inputs/{}/io.json".format(path_to_interaction))
        json_data = json.load(json_raw)
        self.inputs = InputAlphabet(json_data)
        self.outputs = OutputAlphabet(json_data)
        self.mod_perc = json_data["mod_percent"]

        # generate FAKE sample traces
        tracegen_module = importlib.import_module("inputs.{}.trace_generator".format(path_to_interaction))
        TraceGenerator = tracegen_module.TraceGenerator
        tracegen = TraceGenerator(self.TS)
        self.trajs = tracegen.get_trajectories(100)

        # consolidate the trajectories


        # calculate frequencies associated with states
        self.freqs.build_ds(self.inputs, self.outputs)
        self.freqs.calculate_freqs(self.trajs)
        self.freqs.calculate_probabilities(self.inputs, self.outputs)

        self.json_exp.export_from_object(self.TS, st_reachables, self.freqs)

    def mcmc_adapt(self, reward_window, progress_window, cost_window, prop_window, distance_window, update_trace_panel):
        mcmc = MCMCAdapt(self.TS, self.micro_selection, self.trajs, self.inputs, self.outputs, self.freqs, self.mod_perc, self.path_to_interaction, update_trace_panel)
        self.TS, st_reachables = mcmc.adapt(0.2, reward_window, progress_window, cost_window, prop_window, distance_window)
        self.json_exp.export_from_object(self.TS, st_reachables, self.freqs)

    def z3_adapt(self):
        solver = Solver(self.trajs, InputAlphabet(), OutputAlphabet())
        return solver.solve()
