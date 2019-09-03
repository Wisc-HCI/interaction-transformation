import time

from path_traversal import *
from mod_tracker import *
from adapter import *
from smt_setup import *
from modifier import *

class BFSAdapt(Adapter):

    def __init__(self, TS, micro_selection, trajs, inputs, outputs, freqs, mod_perc, path_to_interaction, updated_trace_panel, log, combined_raw_trajs):
        super(BFSAdapt, self).__init__(TS,inputs,outputs,int(round(mod_perc*(len(inputs.alphabet)*len(TS.states)))),int(round(mod_perc*(len(TS.states)))),path_to_interaction)
        self.trajs = trajs
        self.freqs = freqs
        self.micro_selection = micro_selection
        self.path_to_interaction = path_to_interaction

        self.setup_helper = SMTSetup()
        self.modifier = Modifier()

        self.localize_faults(self.trajs)

    def adapt(self):

        # get the set of moddable_sts
        moddable_sts = self.determine_modifiable_states(self.TS)
        moddable_trans = self.determine_modifiable_transitions(self.TS)

        # big dictionary serving two purposes
        # 1) prevent redundent searches (detect symmetry)
        # 2) prevent searches through nodes where the max possible reward is lower than
        #    the current max reward
        max_reward_info = {"tree":{}}

        # define the current depth
        depth = 1

        # define how far we want to go
        depth_cap = 3

        # get the current time
        start_time = time.time()

        # import property checker
        property_module = importlib.import_module("inputs.{}.properties".format(self.path_to_interaction))
        Properties = property_module.Properties
        self.property_checker = Properties(self.inputs, self.outputs)

        # reset the ts
        mod_tracker = ModificationTracker()
        TS, self.all_trans, self.all_states, added_states, modified_states, self.removed_transitions = self.reset_TS(mod_tracker)
        self.cond_dict = self.create_cond_dict(TS)

        # get the moddable states and trans within the TS copy
        self.moddable_sts = []
        self.moddable_trans = []
        for mod_trans in moddable_trans:
            trans_candidates = TS.transitions[mod_trans.source.id][mod_trans.target.id]
            for trans in trans_candidates:
                if mod_trans.condition == trans.condition:
                    self.moddable_trans.append(trans)
                    break
        for mod_st in moddable_sts:
            self.moddable_sts.append(TS.states[mod_st.name])

        # consolidate states and transitions
        self.moddable_all = self.moddable_trans + self.moddable_sts

        # come up with an order to the mods
        moddable_order = {}
        counter = 0
        for st in self.moddable_sts:
            moddable_order[st] = counter
            counter += 1
        for trans in self.moddable_trans:
            moddable_order[trans] = counter
            counter += 1

        # define the current reward
        new_eq_vect = self.model_check(TS, self.removed_transitions, self.property_checker, [], [[]], append_correctness_traj=False)
        eq_cost = len(new_eq_vect)

        if eq_cost == 0:
            path_traversal = PathTraversal(TS, self.trajs, self.freqs, self.removed_transitions)
            unweighted_rew_vect = []
            path_traversal.check(unweighted_rew_vect, [], {})
            total_reward = sum(unweighted_rew_vect)
            print("starting reward: {}".format(total_reward))
        else:
            print("ERROR: starting bfs interaction was not correct")
            exit()

        # keeping state
        best_program = [TS,total_reward]
        depth_stats = {}
        timing_vals = [0,0,0]

        while depth < depth_cap:
            if depth not in depth_stats:
                depth_stats[depth] = [0,0,0,0,0,0,0]
                                                         # [# iterations, # times called model checker,
                                                         # counterexamples produced, # correct interactions found,
                                                         # counterexamples used, # branches pruned, # counter pruned]

            self.modify(curr_depth=0,upto=depth,TS=TS,best_program=best_program,depth_stats=depth_stats[depth],already_modified=[],moddable_order=moddable_order,max_rew_info=max_reward_info,timing_vals=timing_vals)

            print("finished depth={}".format(depth))
            print("   # iterations: {}".format(depth_stats[depth][0]))
            print("   # times model checker called: {}".format(depth_stats[depth][1]))
            print("   # counterexamples produced: {}".format(depth_stats[depth][2]))
            print("   # counterexamples used: {}".format(depth_stats[depth][4]))
            print("   # correct interactions found: {}".format(depth_stats[depth][3]))
            print("   # branches pruned: {}".format(depth_stats[depth][5]))
            print("   # branches flagged as always violating a counterexample: {}".format(depth_stats[depth][6]))
            #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            depth += 1

        end_time = time.time()

        print("seconds passed is {}".format(end_time-start_time))
        #print("timing: {}".format(timing_vals))
        #self.pretty_print_max_rew_info(max_reward_info)

        exit()

    def modify(self,curr_depth,upto,TS,best_program,depth_stats,already_modified,moddable_order,max_rew_info,timing_vals=None):

        if curr_depth == upto:
            # we call this an iteration
            depth_stats[0] += 1

            # get a list of modifiable_trans
            modifiable_trans = [item for item in moddable_order if (item in self.all_trans and item not in already_modified)]
            #print("modifiable_trans: {}".format([str(t) for t in modifiable_trans]))

            pt_start = time.time()
            # get the reward and the eq cost
            is_correct = None
            path_traversal = PathTraversal(TS, self.trajs, self.freqs, self.removed_transitions)
            unweighted_rew_vect = []
            eq_vect = []
            path_traversal.check(unweighted_rew_vect, eq_vect, {}, modifiable_trans=modifiable_trans, cond_dict=self.cond_dict)
            new_sum_reward = sum(unweighted_rew_vect)
            pt_end = time.time()

            always_sat_score,sat_always = path_traversal.get_always_satisfied_score()
            #print("always_sat: {}".format(always_sat_score))
            maybe_sat_positive_score = path_traversal.get_maybe_satisfied_positive_score()
            #print("maybe_sat: {}".format(maybe_sat_positive_score))
            if sat_always:
                potential_score = always_sat_score + maybe_sat_positive_score
            else:
                depth_stats[6] += 1
                potential_score = -1
            timing_vals[0] += (pt_end-pt_start)

            # store the potential score
            #ss_start = time.time()
            self.store_score(max_rew_info,moddable_order,already_modified,potential_score)
            #ss_end = time.time()
            #timing_vals[1] += (ss_end-ss_start)

            if len(eq_vect) > 0:
                depth_stats[4] += 1

            # only bother calling the model checker if by our estimate the program
            # is correct, but also if the new reward is better than the current highest
            if len(eq_vect) == 0 and new_sum_reward > best_program[1]:
                is_correct = True

                # double check with the model checker
                # define the current reward
                new_eq_vect = self.model_check(TS, self.removed_transitions, self.property_checker, [], [[]], append_correctness_traj=True)
                eq_cost = len(new_eq_vect)
                depth_stats[1] += 1
                depth_stats[2] += eq_cost

                if eq_cost == 0:

                    depth_stats[3] += 1

                    # we can be sure we have a correct interaction
                    new_total_reward = new_sum_reward
                    # if the new_total_reward is greater than the old...
                    if new_total_reward > best_program[1]:
                        print("found better interaction with reward {}".format(new_total_reward))
                        best_program[0] = TS.copy()
                        best_program[1] = new_total_reward
            else:
                is_correct = False
            return

        # make a modification
        prunect = 0
        # progress through the trans mods, followed by the state mods
        for moddable in self.moddable_all:

            # determine if transition or state
            is_state = False
            if moddable in self.moddable_sts:
                is_state = True

            if moddable not in already_modified:
                already_modified.append(moddable)

                # # # # # # # # # # # # # # # #
                # make the state modification
                # # # # # # # # # # # # # # # #
                if is_state:
                    pass

                # # # # # # # # # # # # # # # #
                # else make the transition modification
                # # # # # # # # # # # # # # # #
                else:
                    for target in self.all_states:

                        # make the modification
                        undoable = self.modifier.trans_mod(TS,moddable,target,cond_dict=self.cond_dict)

                        # prune branches with low reward
                        ordered = self.get_ordered_modifications(moddable_order,already_modified)
                        seent,rew = self.check_mod_possible_reward(ordered,max_rew_info)
                        if seent and rew <= best_program[1]:
                            depth_stats[5] += 1
                        else:
                            # call modify again with a new modification
                            self.modify(curr_depth+1,upto,TS,best_program,depth_stats,already_modified,moddable_order,max_rew_info,timing_vals)

                        # undo the modification we just made
                        self.modifier.undo_trans_mod(TS,undoable,cond_dict=self.cond_dict)

                already_modified.remove(moddable)

        # make a state modification
        # progress through the state mods
        '''
        for state in self.moddable_sts:
            if state not in already_modified:
                already_modified.append(state)
                for avail_micro in self.micro_selection:

                    # ensure we don't make a modification to ourselves
                    if state.micros[0]["name"] != avail_micro:
        '''

    def store_score(self,max_rew_info,moddable_order,already_modified,potential_score):
        ordered = self.get_ordered_modifications(moddable_order,already_modified)

        curr_dict = max_rew_info
        for i in range(len(ordered)):
            ordered_moddable = ordered[i]

            # determine whether state or not
            is_state = False
            if ordered_moddable in self.moddable_sts:
                is_state = True

            if ordered_moddable not in curr_dict["tree"]:
                curr_dict["tree"][ordered_moddable] = {}

            if not is_state: # if moddable is a transition
                ordered_moddable_target = ordered_moddable.target
            else:
                ordered_moddable_target = ordered_moddable.micros[0]["name"]

            if ordered_moddable_target not in curr_dict["tree"][ordered_moddable]:
                if i == len(ordered) - 1:
                    curr_dict["tree"][ordered_moddable][ordered_moddable_target] = {"tree":{},"score":potential_score}
                else:
                    curr_dict["tree"][ordered_moddable][ordered_moddable_target] = {"tree":{},"score":None}
            else:
                if i == len(ordered) - 1:
                    curr_dict["tree"][ordered_moddable][ordered_moddable_target]["score"] = potential_score
            curr_dict = curr_dict["tree"][ordered_moddable][ordered_moddable_target]

    def pretty_print_max_rew_info(self,max_rew_info):

        print("root: tree")
        next_tree = max_rew_info["tree"]
        self.pretty_print_helper(next_tree,"")

    def pretty_print_helper(self,next_tree,space):
        if len(next_tree) == 0:
            return
        for trans in next_tree:
            print("{} -- {}".format(space,str(trans)))
            for state in next_tree[trans]:
                print("{}   -- {}".format(space,str(state)))
                if "score" in next_tree[trans][state]:
                    print("{}   -- {}".format(space,next_tree[trans][state]["score"]))
                new_tree = next_tree[trans][state]["tree"]
                self.pretty_print_helper(new_tree,space+"  ")

    def get_ordered_modifications(self,moddable_order,already_modified):
        new_dict = {}
        for item in already_modified:
            order = moddable_order[item]
            new_dict[item] = order
        ordered = sorted(new_dict, key=lambda k: new_dict[k])
        return ordered

    def check_mod_possible_reward(self,ordered,max_rew_info):
        curr_dict = max_rew_info
        seent = True
        for ord in ordered:
            if ord not in curr_dict["tree"]:
                seent = False
                break
            elif ord.target not in curr_dict["tree"][ord]:
                seent = False
                break

            if ord in self.moddable_trans:
                curr_dict = curr_dict["tree"][ord][ord.target]
            else:
                curr_dict = curr_dict["tree"][ord][ord.micros[0]["name"]]

        if seent:
            return seent,curr_dict["score"]
        else:
            return seent,False
