from state_machine import *
from mod_tracker import *
from verification.model_checker import *
import importlib

from interaction_components import Trajectory, HumanInput, Microinteraction

class Adapter:

    def __init__(self,TS,inputs,outputs,mod_limit,num_state_limit,path_to_interaction):
        self.state_faults = {}
        self.transition_faults = {}

        self.mod_limit = mod_limit
        self.num_state_limit = num_state_limit
        self.inputs = inputs
        self.outputs = outputs
        self.TS = TS
        self.num_properties = None

        '''
        Get the properties file
        '''
        prop_strings = []
        with open("inputs/{}/properties.txt".format(path_to_interaction), "r") as propfile:
            for line in propfile:
                if line != "\n" and line[0:2] != "--":
                    prop_strings.append(line)

        self.model_checker = ModelChecker(prop_strings)

    def reset_TS(self, mod_tracker):
        TS = self.TS.copy()
        SMUtil().build(TS.transitions, TS.states)

        all_trans = []
        for source,temp in TS.transitions.items():
            for target,conditions in temp.items():
                for trans in conditions:
                    all_trans.append(trans)

        all_states = []
        for _,state in TS.states.items():
            all_states.append(state)

        # create the lists to keep track of added states and removed transitions
        added_states = []
        modified_states = []
        removed_transitions = []
        for state in all_states:
            for inp in self.inputs.alphabet:
                inp_exists = False
                for trans in state.out_trans:
                    if trans.condition == inp:
                        inp_exists = True
                if not inp_exists:
                    new_trans = Transition(state.id, state.id, inp)
                    new_trans.source = state
                    new_trans.target = state
                    removed_transitions.append(new_trans)

        # set up the modification tracker dataset
        mod_tracker.reset_tracker(TS,self.inputs)

        return TS, all_trans, all_states, added_states, modified_states, removed_transitions

    def localize_faults(self, combined_raw_trajs):

        state_fault_severity = {}
        transition_fault_severity = {}

        # transitions and states are weighted by frequency * sum of severity w/in the combined non loop-removed trajectories
        # if a component exists multiple times within a trajectory, that counts as higher frequency -- duplicate severity
        for traj in combined_raw_trajs:
            vect = traj.vect

            # get the severity of each transition fault
            for i in range(1,len(vect)):
                tup = (vect[i-1][1].type,vect[i][0].type,vect[i][1].type)
                if tup not in transition_fault_severity:
                    transition_fault_severity[tup] = [traj.reward]
                else:
                    transition_fault_severity[tup].append(traj.reward)

            # get the severity of each state fault
            for item in vect:
                if item[1].type not in state_fault_severity:
                    state_fault_severity[item[1].type] = [traj.reward]
                else:
                    state_fault_severity[item[1].type].append(traj.reward)

        for st,severities in state_fault_severity.items():
            self.state_faults[st] = sum(severities)*1.0/len(severities)

        for trans_pair,severities in transition_fault_severity.items():
            self.transition_faults[trans_pair] = sum(severities)*1.0/len(severities)

    def determine_modifiable_states(self, TS):

        # move these somewhere else eventually
        self.modstate2availstates = {}

        modifiable_states = []

        scores = {}

        # get a sorted dictionary of states
        for st_name in TS.states:
            # ignore states that aren't scored
            if st_name not in self.state_faults:
                continue

            score = self.state_faults[st_name]

            if score not in scores:
                scores[score] = [TS.states[st_name]]
            else:
                scores[score].append(TS.states[st_name])

        sorted_scores = sorted(list(scores.keys()))
        print(sorted_scores)

        # remove the states in which changes would cause a property violation
        mod_tracker = ModificationTracker()
        property_module = importlib.import_module("inputs.{}.properties".format(self.path_to_interaction))
        Properties = property_module.Properties
        property_checker = Properties(self.inputs, self.outputs)
        for score,state_list in scores.items():
            state_list_to_remove = []
            for state in state_list:
                state_name = state.name
                self.modstate2availstates[state] = []
                # can we modify st?
                # can we change it to available_state, or will it always result in a violation?
                contains_acceptable_mod = False
                for available_state in self.outputs.alphabet:
                    if state.micros[0]["name"] != available_state:   # don't worry about testing the change to itself
                        TS_copy,all_trans, all_states, added_states,_,removed_transitions = self.reset_TS(mod_tracker)

                        # make the change
                        print("\n\n\n~~~~~~~~~")
                        for state_name_2 in TS_copy.states:
                            print("{} ({})".format(state_name_2, TS_copy.states[state_name_2].micros[0]["name"]))
                        state2change = TS_copy.states[state_name]
                        print("~~~")
                        print("{} to {}".format(state2change.name,available_state))
                        print("~~~")
                        TS_copy.states.pop(state2change.name)
                        state2change.name = self.get_unused_name(available_state, TS_copy)
                        TS_copy.states[state2change.name] = state2change
                        state2change.micros = [{"name": available_state}]
                        for state_name_2 in TS_copy.states:
                            print("{} ({})".format(state_name_2, TS_copy.states[state_name_2].micros[0]["name"]))

                        # test the change
                        new_eq_vect = self.model_check(TS_copy, removed_transitions, property_checker, [], [[]], append_correctness_traj=False)
                        eq_cost = len(new_eq_vect)
                        if eq_cost == 0:
                            contains_acceptable_mod = True
                            self.modstate2availstates[state].append({"name": available_state})

                if not contains_acceptable_mod:
                    state_list_to_remove.append(state)
                    self.modstate2availstates.pop(state)
            for state in state_list_to_remove:
                state_list.remove(state)
        scores_to_remove = []
        for score,state_list in scores.items():
            if len(state_list) == 0:
                scores_to_remove.append(score)
        for score in scores_to_remove:
            scores.pop(score)
            sorted_scores.remove(score)

        for sttt in self.modstate2availstates:
            print("{} -- {}".format(str(sttt),self.modstate2availstates[sttt]))

        # no states are modifiable
        if len(sorted_scores) < 1:
            return []

        i = 0
        j = 0
        curr_score = sorted_scores[j]
        to_break = False
        while True:
            if to_break:
                break
            for st in scores[curr_score]:

                modifiable_states.append(st)
                i += 1

                if i >= self.num_state_limit:
                    to_break = True
                    break
            j += 1
            if j >= len(sorted_scores):
                break
            curr_score = sorted_scores[j]

        return modifiable_states

    def determine_modifiable_transitions(self, TS):

        self.modtrans2availdestinations = {}

        modifiable_trans = []

        scores = {}

        print(self.transition_faults)

        # get the faults
        for source_id, tar_dict in TS.transitions.items():
            for target_id, trans_dict in tar_dict.items():
                for trans in trans_dict:
                    tup = (trans.source.micros[0]["name"],trans.condition,trans.target.micros[0]["name"])
                    if tup not in self.transition_faults:
                        continue
                    else:
                        score = self.transition_faults[tup]

                    if score not in scores:
                        scores[score] = [trans]
                    else:
                        scores[score].append(trans)

        # get the potentials
        # aka look at the transition faults with the most positive scores, but that point to different locations
        #positive_scores = {}
        for tup,score in self.transition_faults.items():
            for source_id,tardict in TS.transitions.items():
                for target_id, trans_list in tardict.items():
                    for trans in trans_list:
                        if trans.source.micros[0]["name"] == tup[0] and trans.condition == tup[1] and trans.target.micros[0]["name"] != tup[2]:
                            if score not in scores:
                                scores[score] = [trans]
                            else:
                                scores[score].append(trans)

        sorted_scores = sorted(list(scores.keys()))
        sorted_positive_scores = sorted(list(scores.keys()), reverse=True)

        # discard scores past 0
        '''
        to_remove = []
        for score in sorted_scores:
            if score >= 0:
                to_remove.append(score)
        for score in to_remove:
            sorted_scores.remove(score)

        to_remove = []
        for score in sorted_positive_scores:
            if score <= 0:
                to_remove.append(score)
        for score in to_remove:
            sorted_positive_scores.remove(score)
        '''

        # remove the transitions in which changes would cause a property violation
        # remove the states in which changes would cause a property violation
        mod_tracker = ModificationTracker()
        property_module = importlib.import_module("inputs.{}.properties".format(self.path_to_interaction))
        Properties = property_module.Properties
        property_checker = Properties(self.inputs, self.outputs)
        for score,trans_list in scores.items():
            trans_list_to_remove = []
            for trans in trans_list:
                self.modtrans2availdestinations[trans] = []
                # can we modify st?
                # can we change it to available_state, or will it always result in a violation?
                contains_acceptable_mod = False
                for _,available_state in TS.states.items():
                    if trans.target != available_state:   # don't worry about testing the change to itself
                        TS_copy,all_trans, all_states, added_states,_,removed_transitions = self.reset_TS(mod_tracker)

                        # find the transition in TS_copy
                        candidate_trans_temp = TS_copy.transitions[str(trans.source.id)][str(trans.target.id)]
                        trans_copy = None
                        for t in candidate_trans_temp:
                            if t.source.id == trans.source.id and t.target.id == trans.target.id and t.condition == trans.condition:
                                trans_copy = t
                                break

                        # make the change
                        TS_copy.transitions[str(trans_copy.source.id)][str(trans_copy.target.id)].remove(trans_copy)

                        # pick the target
                        target = TS_copy.states[available_state.name]
                        old_target = trans_copy.target

                        # add the new transition
                        old_target.in_trans.remove(trans_copy)
                        trans_copy.target = target
                        trans_copy.target_id = target.id
                        target.in_trans.append(trans_copy)
                        TS_copy.transitions[str(trans_copy.source.id)][str(trans_copy.target.id)].append(trans_copy)

                        # test the change
                        new_eq_vect = self.model_check(TS_copy, removed_transitions, property_checker, [], [[]], append_correctness_traj=False)
                        eq_cost = len(new_eq_vect)
                        if eq_cost == 0:
                            contains_acceptable_mod = True
                            self.modtrans2availdestinations[trans].append(available_state)

                if not contains_acceptable_mod:
                    trans_list_to_remove.append(trans)
                    self.modtrans2availdestinations.pop(trans)
            for trans in trans_list_to_remove:
                trans_list.remove(trans)
        scores_to_remove = []
        for score,trans_list in scores.items():
            if len(trans_list) == 0:
                scores_to_remove.append(score)
        for score in scores_to_remove:
            scores.pop(score)
            sorted_scores.remove(score)
            sorted_positive_scores.remove(score)

        #for sttt in self.modstate2availstates:
        #    print("{} -- {}".format(str(sttt),self.modstate2availstates[sttt]))


        '''
        # debug

        print(sorted_scores)
        for score,slist in scores.items():
            print(score)
            for transs in slist:
                print(str(transs))
        exit()
        '''

        the_scores = []

        j = 0
        curr_negative_score = sorted_scores[j] if len(sorted_scores) > 0 else None

        m = 0
        curr_positive_score = sorted_positive_scores[m] if len(sorted_positive_scores) > 0 else None

        if curr_negative_score is None and curr_positive_score is None:
            return []
        elif curr_negative_score is None:
            curr_score = curr_positive_score
        elif curr_positive_score is None:
            curr_score = curr_negative_score
        else:
            curr_score = curr_negative_score if abs(curr_negative_score) > curr_positive_score else curr_positive_score
        #curr_score_dict = scores if abs(curr_negative_score) > curr_positive_score else positive_scores
        to_break = False
        i = 0
        while True:
            if to_break:
                break
            for trans in scores[curr_score]:

                if trans in modifiable_trans:
                    print("skipping, as in modifiable trans")
                else:
                    modifiable_trans.append(trans)
                    the_scores.append(curr_score)

                    i += 1

                    if i >= self.mod_limit:
                        to_break = True
                        break

            # increment score idx
            if curr_score == curr_positive_score:
                m += 1
                curr_positive_score = sorted_positive_scores[m] if m < len(sorted_positive_scores) else None
            else:
                j += 1
                curr_negative_score = sorted_scores[j] if j < len(sorted_scores) else None

            if j >= len(sorted_scores) and m >= len(sorted_positive_scores):
                break
            elif j >= len(sorted_scores):
                curr_score = curr_positive_score
            elif m >= len(sorted_positive_scores):
                curr_score = curr_negative_score
            else:
                curr_score = curr_negative_score if abs(curr_negative_score) > curr_positive_score else curr_positive_score
                #curr_score_dict = scores if abs(curr_negative_score) > curr_positive_score else positive_scores
            #curr_score = sorted_scores[j]

        for i in range(len(modifiable_trans)):
            print("score {}, {}".format(the_scores[i],str(modifiable_trans[i])))
        #exit()

        return modifiable_trans

    def model_check(self, TS, removed_transitions, property_checker, correctness_trajs, prop_tracker, append_correctness_traj=True):
        new_eq_vect = []
        '''
        PyNuSMV and KOSA MODEL CHECKERS
        '''
        # export the transition system to .smv file
        self.model_checker.create_and_load_model(TS, removed_transitions, self.inputs, self.outputs)

        # do the checking
        kosa_results, kosa_counterexamples = property_checker.compute_constraints(TS, self.setup_helper, removed_transitions)
        results, counterexamples = self.model_checker.check()
        results = kosa_results + results
        result = sum(results)*1.0/len(results)

        for counterexample in kosa_counterexamples:
            if counterexample is not None:
                prop_tracker[-1].append("kosa")
                traj = self.build_trajectory(counterexample[0], TS.states, -1, counterexample[2], is_prefix=counterexample[1], counter=0)
                # UNCOMMENT IF WE WANT TO REMOVE LOOPS FROM THE COUNTEREXAMPLE
                #traj = util.remove_traj_loop_helper(traj_copy, int(math.floor(len(traj)/2)))
                if append_correctness_traj:
                    self.trajs.append(traj)
                correctness_trajs.append(traj)
                new_eq_vect.append(traj)

        counter = 1
        curr_counterexamples = {}
        for counterexample in counterexamples:
            if counterexample is not None:

                prop_tracker[-1].append(str(counter))
                traj = self.build_trajectory_from_nusmv(counterexample, TS, counter=counter)

                if str(traj) in curr_counterexamples:
                    curr_counterexamples[str(traj)].correctness_ids.append(counter)
                    continue
                else:
                    curr_counterexamples[str(traj)] = traj

                # UNCOMMENT IF WE WANT TO REMOVE LOOPS FROM THE COUNTEREXAMPLE
                #traj = util.remove_traj_loop_helper(traj_copy, int(math.floor(len(traj)/2)))

                # check for duplicate trajectories
                for other_traj in self.trajs:
                    if str(traj) == str(other_traj):
                        print("ERROR: duplicate trajectories")
                        print(traj)
                        print(other_traj)
                        exit()

                if append_correctness_traj:
                    self.trajs.append(traj)
                correctness_trajs.append(traj)
                new_eq_vect.append(traj)
            counter += 1

        if self.num_properties is None:
            self.num_properties = counter

        return new_eq_vect

    def get_unused_name(self, starter, TS):
        name = starter
        count = 0
        while True:
            exists = False
            for state in TS.states:
                if state == "{}{}".format(starter, count):
                    exists = True
                    break
            if not exists:
                break
            count += 1
        return "{}{}".format(name,count)

    def create_cond_dict(self, TS):
        # create a dictionary of dict[source_state][condition] = target_state
        cond_dict = {}
        ts_states = TS.states
        for state_name in ts_states:
            state = ts_states[state_name]
            cond_dict[state] = {}
            for out_trans in state.out_trans:
                cond_dict[state][out_trans.condition] = (out_trans.target,out_trans)

        return cond_dict

    def build_trajectory(self, rawinput, states, reward, output_mapping, is_prefix=False, counter=-1):
        traj_vect = []
        for item in rawinput:
            micro = None
            for st_name, st in states.items():
                if output_mapping[st_name] == item[1]:
                    micro = st.micros[0]["name"]
            traj_vect.append((HumanInput(self.inputs.rev_alphabet[item[0]]), Microinteraction(micro, 0)))
            if micro == None:
                print("ERROR: microinteraction name be None")
                print(output_mapping)
                print(item)
                exit(1)

        trajectory_to_return = Trajectory(traj_vect, reward, is_prefix, is_correctness=True, correctness_id=counter)

        return trajectory_to_return

    def build_trajectory_from_nusmv(self, counterexample, TS, printer=False, counter=-1):
        if printer:
            print(counterexample)
        end_flag = False
        traj_vect = []
        curr_h_in = HumanInput("General")
        for step in counterexample:
            curr_r_out = Microinteraction(TS.states[step["st"]].micros[0]["name"] if step["st"] != "END" else "END",0)
            traj_vect.append((curr_h_in,curr_r_out))
            if curr_r_out.type == "END":
                end_flag = True
                break
            curr_h_in = HumanInput(step["hst"])
        if end_flag:
            is_prefix = False
        else:
            is_prefix=True
        trajectory_to_return = Trajectory(traj_vect, -1, is_prefix=is_prefix, is_correctness=True, correctness_id=counter)
        return trajectory_to_return

    def check_if_exists_within(self, little_traj, big_traj):
        exists = True
        for i in range(len(little_traj.vect)):
            l_item = little_traj.vect[i]
            b_item = big_traj.vect[i]

            if l_item[0].type != b_item[0].type or l_item[1].type != b_item[1].type:
                exists = False
                break
        return exists
