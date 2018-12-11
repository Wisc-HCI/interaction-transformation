from trace_synthesis import *

class InputAlphabet:

    def __init__(self):
        self.alphabet = {
            "Ready": 0,
            "Ignore": 1
        }
        self.rev_alphabet = {
            0: "Ready",
            1: "Ignore"
        }

class OutputAlphabet:

    def __init__(self):
        self.alphabet = {
            "Greeter": 0,
            "Handoff": 1,
            "Remark": 2,
            "Wait": 3,
            "Answer": 4,
            "Farewell": 5
        }

        self.rev_alphabet = {
            0: "Greeter",
            1: "Handoff",
            2: "Remark",
            3: "Wait",
            4: "Answer",
            5: "Farewell"
        }

class Frequencies:

    def __init__(self):
        self.freqs = {}
        self.probs = {}

    def build_ds(self, inputs, outputs):

        for out in outputs.alphabet:
            self.freqs[out] = {}
            for inp in inputs.alphabet:
                self.freqs[out][inp] = 1

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

    def __init__(self, vect, reward):
        self.vect = vect
        self.reward = reward

class Microinteraction:

    def __init__(self, type, weight=0):
        self.type = type
        self.weight = weight

class HumanInput:

    def __init__(self, type):
        self.type = type
