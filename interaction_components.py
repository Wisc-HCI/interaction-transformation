import json

#from trace_synthesis import *

class InputAlphabet:

    def __init__(self, io_data):
        self.alphabet = io_data["inputs"]
        self.rev_alphabet = {}
        for inp,id in self.alphabet.items():
            self.rev_alphabet[id] = inp

class OutputAlphabet:

    def __init__(self, io_data):
        self.alphabet = io_data["outputs"]
        self.rev_alphabet = {}
        for inp,id in self.alphabet.items():
            self.rev_alphabet[id] = inp

class Frequencies:

    def __init__(self):
        self.freqs = {}
        self.probs = {}

    def build_ds(self, inputs, outputs):

        for out in outputs.alphabet:
            self.freqs[out] = {}
            for inp in inputs.alphabet:
                self.freqs[out][inp] = 1

        print(self.freqs)

    def calculate_freqs(self, trajs):

        for traj in trajs:
            vect = traj.vect

            for i in range(0, len(vect)-1):
                step = vect[i]
                start_state = step[1].type
                choice = vect[i+1][0].type

                self.freqs[str(start_state)][choice] += 1

    def calculate_probabilities(self, inputs, outputs):

        for out in outputs.alphabet:
            self.probs[out] = {}
            num_entries = sum(list(self.freqs[out].values()))
            for inp in inputs.alphabet:
                self.probs[out][inp] = self.freqs[out][inp]*1.0/num_entries

        print(self.probs)

class Trajectory:

    def __init__(self, vect, reward, is_prefix, is_correctness=False, correctness_id=-1):
        self.vect = vect
        self.reward = reward
        self.is_prefix = is_prefix
        self.is_correctness = is_correctness
        self.correctness_ids = [correctness_id]

    def eliminate_section(self, start_inc, end_inc):
        self.vect = self.vect[:start_inc] + self.vect[end_inc:]

    def comparable_string(self):
        string = ""
        for item in self.vect:
            string += " --{}-{}--> ".format(item[0].type, item[1].type)
        string += "{}".format("correctness" if self.is_correctness else "")
        return string

    def comparable_component_string(self,start,length):
        string = ""

        for i in range(start,start+length):
            item = self.vect[i]
            string += " --{}-{}--> ".format(item[0].type, item[1].type)

        return string

    def copy(self):
        new_vect = []
        for pair in self.vect:
            new_hum = pair[0].copy()
            new_mic = pair[1].copy()
            new_pair = (new_hum,new_mic)
            new_vect.append(new_pair)
        return Trajectory(new_vect, self.reward, self.is_prefix, self.is_correctness)

    def __len__(self):
        return len(self.vect)

    def __str__(self):
        return "{}       <R: {}>, prefix={} {}".format(self.comparable_string(), self.reward, self.is_prefix, "correctness" if self.is_correctness else "")

class Microinteraction:

    def __init__(self, type, weight=0):
        self.type = type
        self.weight = weight

    def get(self):
        return self.type

    def copy(self):
        return Microinteraction(self.type,self.weight)

class HumanInput:

    def __init__(self, type):
        self.type = type

    def get(self):
        return self.type

    def copy(self):
        return HumanInput(self.type)
