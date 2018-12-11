import xml.etree.ElementTree as ET

from state_machine import *

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
