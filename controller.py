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
        json_raw=open("inputs/{}/io.json".format(self.path_to_interaction))
        json_data = json.load(json_raw)
        self.inputs = InputAlphabet(json_data)
        self.outputs = OutputAlphabet(json_data)
        self.mod_perc = json_data["mod_percent"]
        self.time_mcmc = json_data["time_mcmc"]

        # generate FAKE sample traces
        tracegen_module = importlib.import_module("inputs.{}.trace_generator".format(path_to_interaction))
        TraceGenerator = tracegen_module.TraceGenerator
        tracegen = TraceGenerator(self.TS)
        self.trajs = tracegen.get_trajectories(100)

        # add default microinteractions not already in micro_selection
        for micro in self.outputs.alphabet:
            exists = False
            for micro_selected in self.micro_selection:
                if micro_selected["name"] == micro:
                    exists = True
            if not exists:
                self.micro_selection.append({"name": micro})

        # consolidate the trajectories


        # calculate frequencies associated with states
        self.freqs.build_ds(self.inputs, self.outputs)
        self.freqs.calculate_freqs(self.trajs)
        self.freqs.calculate_probabilities(self.inputs, self.outputs)

        self.json_exp.export_from_object(self.TS, st_reachables, self.freqs)

    def mcmc_adapt(self, reward_window, progress_window, cost_window, prop_window, distance_window, update_trace_panel):

        for i in range(2):
            mcmc = MCMCAdapt(self.TS, self.micro_selection, self.trajs, self.inputs, self.outputs, self.freqs, self.mod_perc, self.path_to_interaction, update_trace_panel)
            self.TS, st_reachables = mcmc.adapt(self.time_mcmc, reward_window, progress_window, cost_window, prop_window, distance_window)
            self.json_exp.export_from_object(self.TS, st_reachables, self.freqs)

            # get new trajectories
            tracegen_module = importlib.import_module("inputs.{}.trace_generator".format(self.path_to_interaction))
            TraceGenerator = tracegen_module.TraceGenerator
            tracegen = TraceGenerator(self.TS)
            new_trajs = tracegen.get_trajectories(100)
            self.trajs = self.trajs + new_trajs

            # calculate frequencies associated with states
            self.freqs.build_ds(self.inputs, self.outputs)
            self.freqs.calculate_freqs(self.trajs)
            self.freqs.calculate_probabilities(self.inputs, self.outputs)

    def z3_adapt(self):
        solver = Solver(self.trajs, InputAlphabet(), OutputAlphabet())
        return solver.solve()
