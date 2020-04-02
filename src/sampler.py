import time
import math
import sys
import random
import os
import reader
import interaction_components as ic
import numpy as np

class Sampler:

    '''
    Sampler takes the existing trajectories as input,
    and comes up with a tree-like interaction whose
    branches are optimized to be (a) less-seen bad tra-
    jectories, (b) unseen good trajectories, and (c)
    unseen combinations of states
    '''

    def __init__(self, inputs, outputs, dir, good_thresh, history_file="history.pkl"):

        if history_file is not None:
            self.traj_list, self.traj_dict, self.traj_comp_dict = self.make_trajs(dir,history_file)
        self.traj_tree = {}
        self.inputs = {}
        self.outputs_no_farewell = []
        self.outputs_no_answer_clarify = []
        self.outputs = {}
        self.outputs_rev = {}
        counter = 0
        for out in outputs:
            self.outputs[out] = counter
            self.outputs_rev[counter] = out
            counter += 1
            if out != "Farewell":
                self.outputs_no_farewell.append(out)
            if out != "AnswerQuestion" and out != "DidYouSay":
                self.outputs_no_answer_clarify.append(out)
        counter = 0
        for inp in inputs:
            self.inputs[inp] = counter
            counter += 1

        self.inputs_list = list(self.inputs.keys())
        self.outputs_list = list(self.outputs.keys())

        self.good_thresh = good_thresh

        # make the trajectory tree and create mutations
        if history_file is not None:
            self.create_trajectory_tree()
            self.mutate_all_trajectories()

    def add_raw_trajectory(self, history):
        trajectory = reader.TrajectoryReader(None).convert_trajectory(history)
        if trajectory.comparable_string() not in self.traj_dict:
            self.traj_dict[trajectory.comparable_string()] = 1
            self.traj_list.append(trajectory)
        else:
            self.traj_dict[trajectory.comparable_string()] += 1

        self.add_to_trajectory_tree(trajectory)

    def create_trajectory_tree(self):

        for traj in self.traj_list:
            vect = traj.vect
            self.add_to_trajectory_tree(traj)

    def add_to_trajectory_tree(self,traj):
        curr_level = self.traj_tree
        vect = traj.vect

        for tup in vect:
            hum = tup[0].type
            rob = tup[1].type

            if hum not in curr_level:
                curr_level[hum] = {"trajs":[]}
            curr_level = curr_level[hum]
            curr_level["trajs"].append(traj)

            if rob not in curr_level:
                curr_level[rob] = {"trajs":[]}
            curr_level = curr_level[rob]
            curr_level["trajs"].append(traj)

    def mutate_all_trajectories(self):
        '''
        Precondition for this being called -- the trajectory tree must already exist
        '''
        print("\nSAMPLER >> mutating all trajectories")
        random.shuffle(self.traj_list)
        all_mutated_trajs = []

        for traj in self.traj_list:
            if traj.reward >= self.good_thresh:
                # weight the number of mutations based on the frequency of the traj
                #print("\nstarting traj: {}".format(traj))
                freq = self.traj_dict[traj.comparable_string()] * 8  # set the frequency to 4x the occurrence of the trajectory
                mutated_trajs = self.mutate_one_trajectory(traj,freq)
                for mut_traj in mutated_trajs:
                    if mut_traj.comparable_string() not in self.traj_dict:
                        self.traj_dict[mut_traj.comparable_string()] = 0
                        # we don't care if it already exists in the traj dict,
                        # as the number of times the mutation has been seen
                        # is still zero
                        self.add_to_trajectory_tree(mut_traj)

    def mutate_one_trajectory(self, traj, num_muts):
        '''
        Mutations:
            1 - state insertion
            2 - state deletion
            3 - state modification
            4 - transition modification
        '''
        mutated_trajs = []

        # start with the insertion
        for i in range(num_muts):
            new_traj = traj.copy()
            new_traj.is_mutated_flag = True

            # pick a random state to insert
            new_state_id = random.choice(self.outputs_list)

            # pick a random location to insert it
            loc = random.randint(0,len(new_traj.vect)-2)  # minus 2 so that we don't modify the end state and because the end is inclusive
            new_hum_id = new_traj.vect[loc][0].type

            # create the new pair
            new_pair = (ic.HumanInput(new_hum_id),ic.Microinteraction(new_state_id))

            # insert the new pair
            new_traj.vect.insert(loc,new_pair)

            # verify the mutated trajectory
        #    print(new_traj)
            if self.verify_trajectory(new_traj):
                mutated_trajs.append(new_traj)
        #        print(new_state_id)
        #    else:
        #        print("NOPENOPENOPE")

        print(len(mutated_trajs))
        #return mutated_trajs

        # next deletion
        #print("deletions")
        for i in range(num_muts):
            new_traj = traj.copy()
            new_traj.is_mutated_flag = True

            # pick a random location to delete
            loc = random.randint(0,len(new_traj.vect)-2) # minus 1 so that we don't modify the end state

            # delete the state at the designated location
            del new_traj.vect[loc]

            # verify the mutated trajectory
            #print(new_traj)
            if self.verify_trajectory(new_traj):
                mutated_trajs.append(new_traj)

        print(len(mutated_trajs))

        # next state modification
        #print("state mods")
        for i in range(num_muts):
            new_traj = traj.copy()
            new_traj.is_mutated_flag = True

            # pick a random state to modify
            loc = random.randint(0,len(new_traj.vect)-2) # minus 1 so that we don't modify the end state

            # pick a new identity for that state
            new_state_id = random.choice(self.outputs_list)

            # modify that state
            new_traj.vect[loc][1].type = new_state_id

            # verify the mutated trajectory
            #print(new_traj)
            if self.verify_trajectory(new_traj):
                mutated_trajs.append(new_traj)

        print(len(mutated_trajs))

        # next transition modification
        #print("transition mods")
        for i in range(num_muts):
            new_traj = traj.copy()
            new_traj.is_mutated_flag = True

            # pick a random human input to modify
            loc = random.randint(0,len(new_traj.vect)-2) # minus 1 so that we don't modify the end state

            # pick a new identity for that transition
            new_hum_id = random.choice(self.inputs_list)

            # modify that transition
            new_traj.vect[loc][0].type = new_hum_id

            # verify the mutated trajectory
            #print(new_traj)
            if self.verify_trajectory(new_traj):
                mutated_trajs.append(new_traj)

        print(len(mutated_trajs))

        return mutated_trajs

    def verify_trajectory(self, traj):
        verified = True
        vect = traj.vect

        # ERROR PROPERTY: if END is not the final state, then quit
        if vect[-1][1].type != "END":
            print("SAMPLER >> ERROR: END is not the final state of trajectory {}".format(traj))
            return False

        # the length of the trajectory must be >1
        if len(vect) < 2:
            return False

        # PROPERTY: farewell must be the final state before End
        if len(vect) > 1 and vect[-2][1].type != "Farewell" and not traj.is_prefix:
            #print("farewell violated")
            return False

        # PROPERTY: unsatisfiable requests must always be followed by refertodesk
        for item in vect:
            if item[0].type == "UnsatRequest" and item[1].type != "ReferToDesk":
                #print("unsatrequest violated")
                return False

        # PROPERTY: if the human just said goodbye, then it's farewell
        for item in vect:
            if item[0].type == "Goodbye" and item[1].type != "Farewell":
                #print("goodbye -> farewell violated")
                return False

        # PROPERTY: if a request for info occurred, either a didyousay or a answerquestion occurs next
        open_request = False
        for item in vect:
            if item[0].type == "RequestInfo" and not (item[1].type == "DidYouSay" or item[1].type == "AnswerQuestion"):
                open_request = True
        if open_request:
            #print("requestinfo1 violated")
            return False

        # PROPERTY: if an affirm to the robot's didyousay occurs, then an answerquestion must occur in the future
        open_affirmation = False
        for i in range(1,len(vect)):
            if vect[i-1][1].type == "DidYouSay" and vect[i][0].type == "Affirm" and vect[i][1].type != "AnswerQuestion":
                open_affirmation = True
        if open_affirmation:
            #print("requestinfo2 violated")
            return False

        # PROPERTY: do not have an answerquestion or didyousay before a requestinfo has occured
        answer_clarify_before_request = False
        request_info_occurred = False
        for item in vect:
            if item[0].type == "RequestInfo":
                request_info_occurred = True
            if not request_info_occurred and (item[1].type == "DidYouSay" or item[1].type == "AnswerQuestion"):
                answer_clarify_before_request = True
        if answer_clarify_before_request:
            return False

        return True

    def solve(self, curr_progress):
        print(curr_progress)
        suffixes = {}  # e.g. suffixes["General"][0] is a list of human inputs
        # while suffixes["General"][1] is a list of robot outputs
        for inp in self.inputs:
            suffixes[inp] = [[],[]]

        # get list of trajectories that we can, and DO want to follow
        # for each human output
        i = 0
        curr_tree = self.traj_tree
        similar_trajs = True
        final_rob_st = None
        while i < len(curr_progress):
            if i == 0:
                hum_st = "General"
            else:
                raw_hum = curr_progress[i-1][2]
                hum_st = raw_hum[raw_hum.index("_")+1].upper() + raw_hum[raw_hum.index("_")+2:]
            rob_st = curr_progress[i][0]
            final_rob_st = rob_st

            if hum_st in curr_tree:
                curr_tree = curr_tree[hum_st]
            else:
                similar_trajs = False
                break

            if rob_st in curr_tree:
                curr_tree = curr_tree[rob_st]
            else:
                similar_trajs = False
                break

            i += 2

        traj_idx = i/2
        if similar_trajs:
            trajs = curr_tree["trajs"]
            print("\n~~~~~~~\nwe have similar trajs\n~~~~~~~")
            for traj in trajs:
                print(traj)
                next_human_step = traj.vect[traj_idx][0].type
                next_robot_output = traj.vect[traj_idx][1].type

                if self.traj_dict[traj.comparable_string()] < 2 and next_robot_output != "END":#self.traj_comp_dict[(final_rob_st,next_human_step,next_robot_output)] < 2 and next_robot_output != "END":
                    print("appending {} to robot output if human input is {}".format(next_robot_output,next_human_step))
                    suffixes[next_human_step][0].append(next_human_step)
                    if next_robot_output not in suffixes[next_human_step][1]:
                        suffixes[next_human_step][1].append(next_robot_output)
                elif next_robot_output != "END":

                    # decide the likelihood that we will append the robot output
                    likelihood = 1.5/self.traj_dict[traj.comparable_string()]
                    r = np.random.random()
                    if r < likelihood:
                        print("probabilistically appended {} to robot output if human input is {}".format(next_robot_output,next_human_step))
                        suffixes[next_human_step][0].append(next_human_step)
                        if next_robot_output not in suffixes[next_human_step][1]:
                            suffixes[next_human_step][1].append(next_robot_output)

            print("\n\n")

        '''
        for traj in self.traj_list:
            included = True
            i = 0
            j = 0
            while i < len(curr_progress):
                if i == 0:
                    hum_st = "General"
                else:
                    raw_hum = curr_progress[i-1][2]
                    hum_st = raw_hum[raw_hum.index("_")+1].upper() + raw_hum[raw_hum.index("_")+2:]
                rob_st = curr_progress[i][0]
                print(hum_st)
                print(rob_st)
                i += 2

                if len(traj.vect) <= j:
                    included = False
                    break

                if traj.vect[j][1].type != rob_st or traj.vect[j][0].type != hum_st:
                    included = False
                    break

                j += 1

            if included:
                print("included: {}".format(traj.comparable_string()))
                next_human_step = traj.vect[j][0].type
                next_robot_output = traj.vect[j][1].type

                # decide on whether to pursue this trajectory, or not
                # 1) pursuit
                if self.traj_dict[traj.comparable_string()] < 5:
                    print("appending {} to robot output if human input is {}".format(next_robot_output,next_human_step))
                    suffixes[next_human_step][0].append(next_human_step)
                    suffixes[next_human_step][1].append(next_robot_output)
                # 2) no pursuit (do we want/need to handle this?)
            else:
                print("not included: {}".format(traj.comparable_string()))
        '''

        # solve each unfilled suffix
        for next_human in suffixes:
            if len(suffixes[next_human][1]) == 0:

                print("\n~~~~~~~\nsampling new trajectory for {}".format(next_human))

                # fill
                suffixes[next_human][0].append(next_human)
                next_st = self.decide_on_next_state(curr_progress,next_human)
                suffixes[next_human][1].append(next_st)

        # returning only one possible robot action
        next_micros = {}
        for hum_in in suffixes:
            next_micros[hum_in] = random.choice(suffixes[hum_in][1])

        return next_micros

    def decide_on_next_state(self, curr_progress, next_human):

        # so we know what the next human is. But we don't know what the next robot it.

        next_robot = None  # default category

        no_question_asked = True
        i = 2
        while i < len(curr_progress):
            if curr_progress[i-1][2] == "human_requestInfo":
                no_question_asked = False
            i += 2
        if next_human == "RequestInfo":
            no_question_asked = False

        '''
        open_request = False
        i = 2
        while i < len(curr_progress):
            if curr_progress[i-1][2] == "human_requestInfo":
                open_request = True
            if curr_progress[i][0] == "AnswerQuestion" or curr_progress[i][0] == "DidYouSay":
                open_request = False
            i += 2
        if next_human == "RequestInfo":
            open_request = True

        open_affirmation = False
        i = 2
        while i < len(curr_progress):
            if curr_progress[i-1][0] == "DidYouSay" and curr_progress[i-1][2] == "human_affirm":
                open_affirmation = True
            if curr_progress[i][0] == "AnswerQuestion":
                open_affirmation = False
            i += 2
        if curr_progress[-1][0] == "DidYouSay" and next_human == "Affirm":
            open_affirmation = True
        '''

        # PROPERTY: if we're at Farewell, then that's it
        if len(curr_progress) > 0 and curr_progress[-1][0] == "Farewell":
            print("returning Farewell\n")
            return next_robot

        # PROPERTY: unsatisfiable requests must always be followed by refertodesk
        elif next_human == "UnsatRequest":
            next_robot = "ReferToDesk"

        # PROPERTY: if the human just said goodbye, then it's farewell
        elif next_human == "Goodbye":
            next_robot = "Farewell"

        # PROPERTY: if the human asked a question, then the next state should either be AnswerQuestion or DidYouSay
        elif next_human == "RequestInfo":
            rand = random.random()
            if rand < 0.5:
                next_robot = "AnswerQuestion"
            else:
                next_robot = "DidYouSay"

        # PROPERTY: if the robot just asked didyousay, then it's affirm
        elif len(curr_progress) > 0 and curr_progress[-1][0] == "DidYouSay" and next_human == "Affirm":
            next_robot = "AnswerQuestion"

        elif no_question_asked:
            next_robot = random.choice(self.outputs_no_answer_clarify)

        # PROPERTY: else, give us a slight chance of the robot ending the interaction with a farewell
        else:
            next_robot = random.choice(list(self.outputs.keys()))

        # PROPERTY: if a request for info occurred, either a didyousay or a answerquestion occurs in the future
        '''
        elif open_request:
            print("open request")
            # NOTE: we cannot uncomment the code below
            # this inherently biases people's experiences to what the
            # experimenter THINKS is an appropriate interaction
            #rand = random.random()
            #if rand < 0.5:
            #    next_robot = "AnswerQuestion"
            #elif rand < 0.8:
            #    next_robot = "DidYouSay"
            #else:
            next_robot = random.choice(self.outputs_no_farewell)

        # PROPERTY: if an affirm to the robot's didyousay occurs, then an answerquestion must occur in the future
        elif open_affirmation:
            print("open affirmation")
            # NOTE: we cannot uncomment the code below
            # this inherently biases people's experiences to what the
            # experimenter THINKS is an appropriate interaction
            #rand = random.random()
            #if rand < 0.8:
            #    next_robot = "AnswerQuestion"
            #else:
            next_robot = random.choice(self.outputs_no_farewell)
        '''

        print("returning {}\n".format(next_robot))
        return next_robot

    def make_trajs(self, dir, history_file="history.pkl"):

        # collect the trajectories
        if os.path.isfile("{}/{}".format(dir,history_file)):
            trajs = reader.TrajectoryReader(
                "{}/{}".format(dir,history_file)).get_trajectories(py2=True)
        else:
            return [],{}

        traj_dict = {}
        traj_list = []
        for traj in trajs:
            if traj.comparable_string() not in traj_dict:
                traj_dict[traj.comparable_string()] = 1
                traj_list.append(traj)
            else:
                traj_dict[traj.comparable_string()] += 1

        traj_comp_dict = {}
        for traj in trajs:
            for i in range(len(traj.vect)-1):
                tup = (traj.vect[i][1].type,traj.vect[i+1][0].type,traj.vect[i+1][1].type)
                if tup not in traj_comp_dict:
                    traj_comp_dict[tup] = 1
                else:
                    traj_comp_dict[tup] += 1

        return traj_list, traj_dict, traj_comp_dict
