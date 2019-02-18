import state_machine as sm
import smt_setup
from mod_tracker import ModificationTracker
from ts_modifier import TSModifier
import importlib
import sys
import json

from interaction_components import InputAlphabet, OutputAlphabet

sys.path.append('../../../../../Repair/repair_algorithms/inputs/cs_event_query')
import properties

class Mutator:

    def __init__(self, interaction):
        self.interaction = interaction
        # convert interaction to a transition system
        # interactions have groups, init_group, and transitions
        # TS have states, init, and transitions
        states = {}
        init = None
        transitions = {}
        for state_name,state in interaction.groups.items():
            states[state_name] = sm.State(state.name,state.id,[{"name": state.micros[0].micro_inst}])
            if interaction.init_group.name == state_name:
                init = states[state_name]

        # transitions
        for s1 in states:
            transitions[str(states[s1].id)] = {}
            for s2 in states:
                transitions[str(states[s1].id)][str(states[s2].id)] = []

        for source_id,source in interaction.transitions.items():
            for target_id,target in source.items():
                for trans in target:
                    for condition in trans.conditions:
                        transitions[source_id][target_id].append(sm.Transition(source_id,target_id,"Ready" if condition == "human_ready" else "Ignore"))
        sm.SMUtil().build(transitions, states)
        self.TS = sm.TS(states,transitions,init)

    def mutate(self, property_dir):
        mutation_accepted = False

        json_raw=open("../../../../../Repair/repair_algorithms/inputs/cs_event_query/io.json")
        json_data = json.load(json_raw)
        inputs = InputAlphabet(json_data)
        raw_outputs = {"outputs": {}}
        for output,output_data in json_data["outputs"].items():
            raw_outputs["outputs"][output] = output_data["id"]
        outputs = OutputAlphabet(raw_outputs)
        mod_limit = int(round(json_data["mod_percent"]*(2*len(self.TS.states))))

        all_trans = []
        for source,temp in self.TS.transitions.items():
            for target,conditions in temp.items():
                for trans in conditions:
                    all_trans.append(trans)

        all_states = []
        for _,state in self.TS.states.items():
            all_states.append(state)

        # create the lists to keep track of added states and removed transitions
        added_states = []
        removed_transitions = []
        for state in all_states:
            for inp in inputs.alphabet:
                inp_exists = False
                for trans in state.out_trans:
                    if trans.condition == inp:
                        inp_exists = True
                if not inp_exists:
                    new_trans = sm.Transition(state.id, state.id, inp)
                    new_trans.source = state
                    new_trans.target = state
                    removed_transitions.append(new_trans)

        # add default microinteractions not already in micro_selection
        micro_selection = []
        for micro in outputs.alphabet:
            micro_selection.append({"name": micro})

        # set up the modification tracker dataset
        mod_tracker = ModificationTracker(self.TS,inputs)

        setup_helper = smt_setup.SMTSetup()
        property_checker = properties.Properties(inputs,outputs)

        ts_modifier = TSModifier(mod_limit,micro_selection,inputs)

        mut_count = 0
        while not mutation_accepted:

            # make a mutation
            ts_modifier.modify_TS(self.TS, all_trans, all_states, added_states, removed_transitions, mod_tracker)
            if mut_count>0 and mut_count%1000 == 0:
                print("{} mutations attempted".format(mut_count))

            print(self.TS)

            # verify the mutation
            results, counterexamples = property_checker.compute_constraints(self.TS, setup_helper, removed_transitions)

            if sum(results)*1.0/len(results) == 1.0:
                break

        print(self.TS)

        # package up TS and return it
        groups = {}
        init_group = None
        transitions = {}
        # handle states to groups, and init group
        for state_name,state in self.TS.states.items():
            g = None
            for group_name,group in self.interaction.groups.items():
                if group_name == state_name:
                    g = (group.name, group.id, group.micros)
                    break
            if g is None:
                g = (state.name,state.id,state.micros)
            if state == self.TS.init:
                init_group = g
            groups[state_name] = g

        # handle the transitions
        for source_id,temp in self.TS.transitions.items():
            for target_id,conds in temp.items():
                conditions = []
                for item in conds:
                    conditions.append("human_ready" if item.condition == "Ready" else "human_ignore")
                if source_id not in transitions:
                    transitions[source_id] = {}
                if target_id not in transitions[source_id]:
                    transitions[source_id][target_id] = [(source_id,target_id,conditions)]

        return groups, init_group, transitions
