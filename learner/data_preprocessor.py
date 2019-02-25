

import numpy as np
import pickle
import os
import sys
sys.path.append(
    '/Users/lindawu/Desktop/OneDrive/School Work/HCI Lab/2019 social robot/codes/interaction-adaptation-working')

def data_preprocessor (input_style):
    # inputs from experiments
    if input_style == 1:
        # import and combine data files
        with open('learner/history.pkl', 'rb') as f:
            raw_data = pickle.load(f, encoding='bytes')

        # Read every pickle data file and combine data
        paths = ["learner/linda1", "learner/linda2"]
        for path in paths:
            for folderName in os.listdir(path):
                folderPath = path + "/" + folderName
                for file in os.listdir(folderPath):
                    if ".pkl" in file:
                        filename = file
                filePath = folderPath + "/" + filename
                with open(filePath, 'rb') as f:
                    if "union" in filePath:
                        location = "union"  # TODO: use the location for later maybe
                    else:
                        location = "DOIT"
                    temp = pickle.load(f, encoding='bytes')
                    raw_data.extend(temp)

        # for r in raw_data:
        #     print("\n\n{}".format(r))

        # parse our raw data and keep useful vectors
        trajs = []
        time_stamps = []

        for raw_traj in raw_data:
            end_time = raw_traj.pop(-1)  # end time
            start_time = raw_traj.pop(-1)  # start time
            date = raw_traj.pop(-1)  # date
            time_stamp = [end_time, start_time, date]
            if time_stamp in time_stamps:
                continue
            time_stamps.append(time_stamp)

            _ = raw_traj.pop(-1)  # id
            _ = raw_traj.pop(-1)  # mutated?

            is_correctness = raw_traj.pop(-1)
            is_prefix = raw_traj.pop(-1)
            score = raw_traj.pop(-1)

            # loop through all entries, get trajectories and human status
            human_input = "Ready"
            micro = raw_traj[0][0]
            traj_vect = [(human_input, micro)]
            i = 1
            while i < len(raw_traj) - 1:

                micro = raw_traj[i + 1][0]
                raw_human_input = raw_traj[i][-1]
                if raw_human_input.decode("utf-8") == "human_ready":
                    human_input = "Ready"
                else:
                    human_input = "Ignore"

                item = (human_input, micro)
                traj_vect.append(item)

                i += 2
            # the last human status
            micro = 'EndInteraction'
            raw_human_input = raw_traj[len(raw_traj) - 1][-1]
            if raw_human_input.decode("utf-8") == "human_ready":
                human_input = "Ready"
            else:
                human_input = "Ignore"
            item = (human_input, micro)
            traj_vect.append(item)

            # append each traj item to list of trajs
            traj = {'traj_vect': traj_vect, 'score': score, 'is_prefix':
                is_prefix, 'is_correctness': is_correctness}
            trajs.append(traj)

    # inputs from simulated data
    if input_style == 2:
        with open('inputs/generated_data/history.pkl', 'rb') as f:
            raw_data = pickle.load(f, encoding='bytes')

        trajs = []
        for r in raw_data:
            traj_vect = []
            print("\n\n{}".format(r))
            vect = r.vect
            for v in vect:
                human_input = v[0].type
                micro = v[1].type
                item = (human_input, micro)
                traj_vect.append(item)
            score = r.reward
            is_prefix = r.is_prefix
            is_correctness = r.is_correctness
            traj = {'traj_vect': traj_vect, 'score': score, 'is_prefix':
                is_prefix, 'is_correctness': is_correctness}
            trajs.append(traj)

    # for traj in trajs:
    #     print("{}\n".format(traj))
    # print("length of trajs", len(trajs))
    # print(type(trajs))

    # check if the data satisfy that all is_correctness equals false
    correctness = False
    for traj in trajs:
        if traj.get('is_correctness'):
            correctness = True
    if correctness:
        print('Not all "is_correctness"are false')
        exit()

    score = np.array(list(traj['score'] for traj in trajs))

    behaviors = []
    for traj in trajs:
        inp = []
        for traj_vect in traj['traj_vect']:
            inp.append(traj_vect[0] + traj_vect[1])
        behaviors.append(inp)

    return score, behaviors

