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

        # read in arrays, form trajectories
        self.trajs = TrajectoryReader("inputs/{}/history.pkl".format(self.path_to_interaction)).get_trajectories()
        '''
        # generate FAKE sample traces
        tracegen_module = importlib.import_module("inputs.{}.trace_generator".format(path_to_interaction))
        TraceGenerator = tracegen_module.TraceGenerator
        tracegen = TraceGenerator(self.TS)
        self.trajs = tracegen.get_trajectories(100)
        '''
        self.consolidate_trajectories()

        # add default microinteractions not already in micro_selection
        for micro in self.outputs.alphabet:
            exists = False
            for micro_selected in self.micro_selection:
                if micro_selected["name"] == micro:
                    exists = True
            if not exists:
                self.micro_selection.append({"name": micro})

        # calculate frequencies associated with states
        self.freqs.build_ds(self.inputs, self.outputs)
        self.freqs.calculate_freqs(self.trajs)
        self.freqs.calculate_probabilities(self.inputs, self.outputs)

        self.json_exp.export_from_object(self.TS, st_reachables, self.freqs)

    def mcmc_adapt(self, reward_window, progress_window, cost_window, prop_window, distance_window, update_trace_panel, algorithm="mcmc"):

        plot_data = { "rewards": [],
                      "progress": [],
                      "cost": [],
                      "props": [],
                      "distances": [],
                      "time": []
                    }

        #for i in range(2):
        #print("Day {}".format(i))
        mcmc = MCMCAdapt(self.TS, self.micro_selection, self.consolidated_trajs, self.inputs, self.outputs, self.freqs, self.mod_perc, self.path_to_interaction, update_trace_panel, algorithm)
        self.TS, st_reachables, correctness_trajs = mcmc.adapt(self.time_mcmc, reward_window, progress_window, cost_window, prop_window, distance_window, plot_data)
        self.json_exp.export_from_object(self.TS, st_reachables, self.freqs)

        # get new trajectories
        '''
        tracegen_module = importlib.import_module("inputs.{}.trace_generator".format(self.path_to_interaction))
        TraceGenerator = tracegen_module.TraceGenerator
        tracegen = TraceGenerator(self.TS)
        new_trajs = tracegen.get_trajectories(100)
        self.trajs = self.trajs + new_trajs + correctness_trajs
        self.consolidate_trajectories()

        # calculate frequencies associated with states
        self.freqs.build_ds(self.inputs, self.outputs)
        self.freqs.calculate_freqs(self.trajs)
        self.freqs.calculate_probabilities(self.inputs, self.outputs)
        '''

    def z3_adapt(self):
        solver = Solver(self.trajs, InputAlphabet(), OutputAlphabet())
        return solver.solve()

    def consolidate_trajectories(self):
        self.consolidated_traj_dict = {}
        for traj in self.trajs:
            if traj.comparable_string() not in self.consolidated_traj_dict:
                self.consolidated_traj_dict[traj.comparable_string()] = [Trajectory(traj.vect, traj.reward, traj.is_prefix, traj.is_correctness), 1]
            else:
                self.consolidated_traj_dict[traj.comparable_string()][1] += 1
                self.consolidated_traj_dict[traj.comparable_string()][0].reward += traj.reward

        for key,vect in self.consolidated_traj_dict.items():
            vect[0].reward = vect[0].reward*1.0/vect[1]

        self.consolidated_trajs = []
        for traj,vect in self.consolidated_traj_dict.items():
            self.consolidated_trajs.append(vect[0])
