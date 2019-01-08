import xml.etree.ElementTree as ET

from state_machine import *
from interaction_components import *

import pickle

class Reader:

    def __init__(self, filename):
        self.filename = filename

    def build(self):
        tree = ET.parse(self.filename)

        root = tree.getroot()

        # groups
        states = {}
        micro_selection = []
        for group in root.iterfind("group"):
            microinteractions = []
            id = group.attrib["id"]
            for i in group.iterfind("name"):
                group_name = i.text
            for i in group.iterfind("micro"):
                for j in i.iterfind("name"):
                    parameters = []
                    for k in i.iterfind("parameter"):
                        name = k.text
                        type = k.attrib["type"]
                        val = k.attrib["val"]
                        globParam = Global(name, type)
                        globParam.val = val
                        parameters.append(globParam)
                    microinteractions.append({"name": j.text,"params": parameters})
                    micro_selection.append({"name": j.text,"params": parameters})

            new_state = State(group_name, id, microinteractions)
            states[group_name] = new_state
            if id == "0":
                init = new_state

        # transitions
        transitions = {}
        for s1 in states:
            transitions[str(states[s1].id)] = {}
            for s2 in states:
                transitions[str(states[s1].id)][str(states[s2].id)] = []

        for transition in root.iterfind("transition"):
            conditions = []
            for i in transition.iterfind("source"):
                source = i.attrib["ref"]
            for i in transition.iterfind("target"):
                target = i.attrib["ref"]
            for i in transition.iterfind("guard"):

                if i.attrib["condition"] == "human_ready":
                    condition = "Ready"
                elif i.attrib["condition"] == "human_busy":
                    condition = "Ignore"
                elif i.attrib["condition"] == "human_ignore":
                    condition = "Ignore"
                else:
                    print("ERROR: unknown human condition")
                    exit(1)
                transitions[source][target].append(Transition(source, target, condition))

        # build
        SMUtil().build(transitions, states)

        return TS(states, transitions, init), micro_selection # todo -- don't return a list of micro dummies

class TrajectoryReader:

    def __init__(self, picklename):
        self.picklename = picklename

    def get_trajectories(self):

        trajs = []

        with open(self.picklename, "rb") as infile:
            raw_trajs = pickle.load(infile)

            for raw_traj in raw_trajs:
                is_correctness = raw_traj.pop(-1)
                is_prefix = raw_traj.pop(-1)
                score = raw_traj.pop(-1)

                traj_vect = [(HumanInput("Ready"),Microinteraction(raw_traj[0][0]))]

                i = 1
                while i < len(raw_traj)-1:

                    micro = Microinteraction(raw_traj[i+1][0])
                    raw_human_input = raw_traj[i][-1]
                    if raw_human_input == "human_ready":
                        inp = "Ready"
                    else:
                        inp = "Ignore"
                    human_input = HumanInput(inp)

                    item = (human_input,micro)
                    traj_vect.append(item)

                    i += 2

                trajs.append(Trajectory(traj_vect,score,is_prefix,is_correctness))

        return trajs
