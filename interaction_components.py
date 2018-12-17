import json

from trace_synthesis import *

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

                self.freqs[start_state][choice] += 1

    def calculate_probabilities(self, inputs, outputs):

        for out in outputs.alphabet:
            self.probs[out] = {}
            num_entries = sum(list(self.freqs[out].values()))
            for inp in inputs.alphabet:
                self.probs[out][inp] = self.freqs[out][inp]*1.0/num_entries

        print(self.probs)

class Trajectory:

    def __init__(self, vect, reward, is_prefix=False):
        self.vect = vect
        self.reward = reward
        self.is_prefix = is_prefix

    def eliminate_loops(self):
        pass

        # remove loops
        #loop_len = len(self.)

        # remove self-loops that occur more than once


    def __str__(self):
        string = ""
        for item in self.vect:
            string += " --{}-{}--> ".format(item[0].type, item[1].type)
        string += "       <R: {}>, prefix={}".format(self.reward, self.is_prefix)
        return string

class Microinteraction:

    def __init__(self, type, weight=0):
        self.type = type
        self.weight = weight

class HumanInput:

    def __init__(self, type):
        self.type = type
