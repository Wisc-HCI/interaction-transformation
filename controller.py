import threading
import importlib
from copy import deepcopy

from interaction_components import *
from mcmc_repair import *
from z3_adapt import *
from json_exporter import *
from verification.prism_util import *
from reader import *
from trajectory_builder import *
from log import *
import util
import pickle

class Controller:

    def __init__(self, path_to_interaction):
        self.path_to_interaction = path_to_interaction
        json_raw=open("inputs/{}/io.json".format(self.path_to_interaction))
        json_data = json.load(json_raw)

        newdir = os.path.join(os.getcwd(), 'result_files')
        if not os.path.isdir(newdir):
            os.mkdir(newdir)
        else:
            print("CONTROLLER >> ERROR >> result files exist and cannot be overwritten!")

        # initialize the log
        self.log = AdaptLog("result_files")

        # read the interaction
        self.json_exp = JSONExporter()
        self.TS, self.micro_selection = Reader("inputs/{}/interaction.xml".format(path_to_interaction),json_data).build()
        st_reachables = {}
        for state in self.TS.states:
            st_reachables[state] = True

        self.freqs = Frequencies()
        self.inputs = InputAlphabet(json_data)
        raw_outputs = {"outputs": {}}
        for output,output_data in json_data["outputs"].items():
            raw_outputs["outputs"][output] = output_data["id"]
        self.outputs = OutputAlphabet(raw_outputs)
        self.mod_perc = json_data["mod_percent"]
        self.time_mcmc = json_data["time_mcmc"]

        self.json_data = json_data

        # read in arrays, form trajectories
        self.trajs = TrajectoryReader("inputs/{}/history.pkl".format(self.path_to_interaction)).get_trajectories()
        original_interaction_trajs = TrajectoryReader("inputs/{}/oi_history.pkl".format(self.path_to_interaction)).get_trajectories()

        # generate FAKE sample traces
        #self.trajs = []
        #with open("inputs/{}/history.pkl".format(self.path_to_interaction), "rb") as fp:
        #    self.trajs = pickle.load(fp)

        # get original interaction rewards
        #with open("inputs/{}/oi_history.pkl".format(self.path_to_interaction), "rb") as fp:
        #    original_interaction_trajs = pickle.load(fp)
        # NOTE: COMMENT OUT IF NOT DEBUGGING
        #tb = TrajectoryBuilder()
        #self.trajs = tb.session()

        # remove final human/robot actions from prefixes
        print("\nCONTROLLER >> trimming prefixes")
        self.print_trajs(self.trajs)
        self.trim_prefixes()
        print("\nCONTROLLER >> prefixes trimmed")
        self.print_trajs(self.trajs)

        # remove final human/robot actions from prefixes
        print("CONTROLLER >> finding baseline")
        for traj in self.trajs:
            print(traj.reward)
        baseline = self.find_baseline(original_interaction_trajs)
        print("CONTROLLER >> baseline set to {}".format(baseline))
        print("CONTROLLER >> offsetting rewards based on baseline")
        self.offset_rewards(baseline)
        for traj in self.trajs:
            print(traj.reward)
        exit()

        #self.trajs = []
        '''
        tracegen_module = importlib.import_module("inputs.{}.trace_generator".format(path_to_interaction))
        TraceGenerator = tracegen_module.TraceGenerator
        tracegen = TraceGenerator(self.TS, self.inputs.alphabet, self.outputs.alphabet)
        self.trajs = self.trajs + tracegen.get_trajectories(100)
        '''

        #with open("inputs/{}/history.pkl".format(self.path_to_interaction), "wb") as fp:
        #    pickle.dump(self.trajs,fp)
        #exit()
        self.consolidate_trajectories()

        '''
        print("\n\n\n")
        for traj in self.trajs:
            print(traj)
        print("\nTRAJ DICT\n")
        for key,val in self.consolidated_traj_dict.items():
            print("{}     -     {}".format(key,val))
        print("\nNEW TRAJS\n")
        for traj in self.consolidated_trajs:
            print(traj)

        exit()
        '''




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

        print("STARTING INTERACTION")
        print(self.TS)
        self.log.open()
        mcmc = MCMCAdapt(self.TS, self.micro_selection, self.consolidated_trajs, self.inputs, self.outputs, self.freqs, self.mod_perc, self.path_to_interaction, update_trace_panel, algorithm, self.log)
        self.TS, st_reachables, correctness_trajs = mcmc.adapt(self.time_mcmc, reward_window, progress_window, cost_window, prop_window, distance_window, plot_data)
        self.log.close()
        self.json_exp.export_from_object(self.TS, st_reachables, self.freqs)

        with open("trajectories_used_for_learning.pkl", "wb") as fp:
            pickle.dump(self.consolidated_trajs, fp)
        with open("trajectories.pkl", "wb") as fp:
            pickle.dump(self.trajs, fp)
        with open("correctness_trajs.pkl", "wb") as fp:
            pickle.dump(correctness_trajs, fp)


        # export the interaction
        exporter = TSExporter(self.TS, self.json_data)
        exporter.export("result_files/updated_interaction.xml")

        #with open("TS.txt", "wb") as fp:
        #    fp.write(self.TS)

        # POSSIBLY write the correctness trajs to a correctness.pkl file

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

    def z3_adapt(self, reward_window, progress_window, cost_window, prop_window, distance_window, update_trace_panel):

        plot_data = { "rewards": [],
                      "progress": [],
                      "cost": [],
                      "props": [],
                      "distances": [],
                      "time": []
                    }

        #for i in range(2):
        #print("Day {}".format(i))
        for traj in self.consolidated_trajs:
            print(traj)
        z3 = Z3Adapt(self.TS, self.micro_selection, self.consolidated_trajs, self.inputs, self.outputs, self.freqs, self.mod_perc, self.path_to_interaction, update_trace_panel)
        self.TS, st_reachables, correctness_trajs = z3.adapt(reward_window, progress_window, cost_window, prop_window, distance_window, plot_data)
        self.json_exp.export_from_object(self.TS, st_reachables, self.freqs)

        # POSSIBLY write the correctness trajs to a correctness.pkl file

    def trim_prefixes(self):
        for traj in self.trajs:
            if traj.is_prefix:
                if traj.vect[-1][1].type == "END":
                    del traj.vect[-1]

    def find_baseline(self, oi_trajs):
        total_reward = 0
        number_trajectories = 0
        for traj in oi_trajs:
            total_reward += traj.reward
            number_trajectories += 1
        return total_reward*1.0/number_trajectories

    def offset_rewards(self, baseline):
        for traj in self.trajs:
            traj.reward -= baseline

    def consolidate_trajectories(self):
        #print("RAW TRAJS")
        #self.print_trajs(self.trajs)

        no_loop_trajectories = self.remove_trajectory_loops()
        #print("\n\nTRAJS WITH LOOPS REMOVED")
        #self.print_trajs(no_loop_trajectories)
        self.ignore_duplicate_trajectories(no_loop_trajectories)

        #print("\n\nCONSOLIDATED TRAJS")
        #self.print_trajs(self.consolidated_trajs)

        #print("\n\nRAW TRAJS AGAIN")
        #self.print_trajs(self.trajs)

    def remove_trajectory_loops(self):
        no_loop_trajectories = []

        for traj in self.trajs:
            traj_copy = copy.deepcopy(traj)
            trimmed_traj = util.remove_traj_loop_helper(traj_copy, int(math.floor(len(traj)/2)))
            no_loop_trajectories.append(trimmed_traj)

        return no_loop_trajectories

    def ignore_duplicate_trajectories(self, no_loop_trajs):
        self.consolidated_traj_dict = {}
        for traj in no_loop_trajs:
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

    def add_trajs(self, trajs_to_add):
        self.trajs += trajs_to_add
        self.consolidate_trajectories()

        # calculate frequencies associated with states
        self.freqs.build_ds(self.inputs, self.outputs)
        self.freqs.calculate_freqs(self.trajs)
        self.freqs.calculate_probabilities(self.inputs, self.outputs)

    def print_trajs(self, trajs):
        for traj in trajs:
            print(traj.comparable_string())
