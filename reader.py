import xml.etree.ElementTree as ET

from state_machine import *
from interaction_components import *

import pickle

class Reader:

    def __init__(self, filename, io_dict):
        self.filename = filename
        self.io_data = io_dict

    def build(self):
        tree = ET.parse(self.filename)

        root = tree.getroot()

        temp_dict = self.io_data["outputs"]
        for micro_type in temp_dict:
            for param in temp_dict[micro_type]["params"]:
                if param == "answers robot can recognize":
                    param_list = []
                    for item in temp_dict[micro_type]["params"][param]:
                        dic = {"val":item, "link":temp_dict[micro_type]["params"][param][item]}
                        param_list.append(dic)
                    temp_dict[micro_type]["params"][param] = param_list

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
                    param_dict = {}
                    for k in i.iterfind("parameter"):
                        if k.attrib["type"] != "array":
                            name = k.text
                            type = k.attrib["type"]
                            val = k.attrib["val"]
                        else:
                            val = []
                            type = "array"
                            for l in k.iterfind("name"):
                                name = str(l.text)
                            for l in k.iterfind("item"):
                                val.append({"val":str(l.attrib["val"]), "link":str(l.attrib["link"])})
                        globParam = Global(name, type)
                        globParam.val = val
                        parameters.append(globParam)
                        param_dict[name] = val
                    #microinteractions.append({"name": j.text,"params": parameters})
                    #micro_selection.append({"name": j.text,"params": parameters})

                    temp_dict = self.io_data["outputs"]
                    selected_micro_type = None
                    for micro_type in temp_dict:
                        if temp_dict[micro_type]["micro"] == j.text:
                            is_good = True
                            for param in temp_dict[micro_type]["params"]:
                                if param_dict[str(param)] != temp_dict[micro_type]["params"][param]:
                                    is_good = False
                                    break
                            if is_good:
                                selected_micro_type = micro_type
                                microinteractions.append({"name": selected_micro_type,"params": parameters})
                                micro_selection.append({"name": selected_micro_type,"params": parameters})
                                break
                    if selected_micro_type is None:
                        print("ERROR: cannot find microinteraction instantiation")
                        exit(1)

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

                raw_condition = i.attrib["condition"]
                condition = raw_condition[raw_condition.index("_")+1].upper() + raw_condition[raw_condition.index("_")+2:]
                transitions[source][target].append(Transition(source, target, condition))

        # build
        SMUtil().build(transitions, states)

        return TS(states, transitions, init), micro_selection # todo -- don't return a list of micro dummies

class TrajectoryReader:

    def __init__(self, picklename):
        self.picklename = picklename

    def get_trajectories(self, py2=False):

        trajs = []

        with open(self.picklename, "rb") as infile:
            if py2:
                raw_trajs = pickle.load(infile)
            else:
                raw_trajs = pickle.load(infile, encoding='bytes')

            print("TRAJS:")
            print(raw_trajs)
            for raw_traj in raw_trajs:

                _ = raw_traj.pop(-1) # age
                _ = raw_traj.pop(-1) # gender

                _ = raw_traj.pop(-1) # survey
                _ = raw_traj.pop(-1) # survey
                _ = raw_traj.pop(-1) # survey
                _ = raw_traj.pop(-1) # survey
                _ = raw_traj.pop(-1) # survey
                _ = raw_traj.pop(-1) # survey
                _ = raw_traj.pop(-1) # survey
                _ = raw_traj.pop(-1) # survey

                _ = raw_traj.pop(-1) # end time
                _ = raw_traj.pop(-1) # start time
                _ = raw_traj.pop(-1) # date

                _ = raw_traj.pop(-1) # id
                _ = raw_traj.pop(-1) # mutated?

                is_correctness = raw_traj.pop(-1)
                is_prefix = raw_traj.pop(-1)
                score = raw_traj.pop(-1)

                _ = raw_traj.pop(-1) # whether or not interacted before

                print(raw_traj)

                traj_vect = [(HumanInput("General"),Microinteraction(raw_traj[0][0]))]

                i = 1
                while i < len(raw_traj)-1:

                    micro = Microinteraction(raw_traj[i+1][0])
                    raw_human_input = raw_traj[i][-1].decode("utf-8")
                    inp = raw_human_input[raw_human_input.index("_")+1].upper() + raw_human_input[raw_human_input.index("_")+2:]
                    #if raw_human_input.decode("utf-8")  == "human_ready":
                    #    inp = "Ready"
                    #else:
                    #    inp = "Ignore"
                    human_input = HumanInput(inp)

                    item = (human_input,micro)
                    traj_vect.append(item)

                    i += 2

                # set up the end of the trajectory
                raw_human_input = raw_traj[-1][-1].decode("utf-8")
                inp = raw_human_input[raw_human_input.index("_")+1].upper() + raw_human_input[raw_human_input.index("_")+2:]
                human_input = HumanInput(inp)
                micro = Microinteraction("END")
                traj_vect.append((human_input,micro))

                trajectory = Trajectory(traj_vect,score,is_prefix,is_correctness)
                print(trajectory)
                trajs.append(trajectory)

        return trajs
