from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, Dense, LSTM, Flatten, Activation, \
    Bidirectional, Dropout
from keras.metrics import categorical_accuracy
from keras.optimizers import RMSprop
from keras.utils import to_categorical

import numpy as np
import matplotlib.pyplot as plt
import pickle
import os
import sys
sys.path.append(
    '/Users/lindawu/Desktop/OneDrive/School Work/HCI Lab/2019 social robot/codes/interaction-adaptation-working')
from interaction_components import *


def NNModel(input_style):
    if input_style == 1: # inputs from experiments

        # import and combine data files
        with open('history.pkl', 'rb') as f:
            raw_data = pickle.load(f, encoding='bytes')

        # Read every pickle data file and combine data
        paths = ["./linda1", "./linda2"]
        for path in paths:
            for folderName in os.listdir(path):
                folderPath = path + "/" + folderName
                for file in os.listdir(folderPath):
                    if ".pkl" in file:
                        filename = file
                filePath = folderPath+ "/" + filename
                with open(filePath, 'rb') as f:
                    if "union" in filePath:
                        location = "union" #TODO: use the location for later maybe
                    else:
                        location = "DOIT"
                    temp = pickle.load(f, encoding='bytes')
                    raw_data.extend(temp)

        for r in raw_data:
            print("\n\n{}".format(r))

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
            #the last human status
            micro = 'EndInteraction'
            raw_human_input = raw_traj[len(raw_traj)-1][-1]
            if raw_human_input.decode("utf-8") == "human_ready":
                human_input = "Ready"
            else:
                human_input = "Ignore"
            item = (human_input, micro)
            traj_vect.append(item)

            traj = {'traj_vect': traj_vect, 'score':score, 'is_prefix': is_prefix, \
                   'is_correctness': is_correctness}
            trajs.append(traj)




    if input_style == 2: #inputs from simulated data
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


    for traj in trajs:
        print(traj)
        # print(traj['traj_vect'][1])
        # for traj_vect in traj['traj_vect']:
        #     print (traj_vect [1])
        # print(traj.get('is_correctness'))
        # print(type(traj.get('is_correctness')))
        print('\n')
    print("length of trajs", len(trajs))
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
    score = to_categorical(score, 3)
    print("score shape", score.shape)
    traj_vect = list(traj['traj_vect'] for traj in trajs)
    behaviors = []
    for traj in trajs:
        inp = []
        for traj_vect in traj['traj_vect']:
            inp.append(traj_vect[0] + traj_vect[1])
        behaviors.append(inp)


    # parameter values
    vocabulary_size = 50 # an estimation
    embed_dim = 50
    lstm_out = 128
    batch_size = 32

    # padding
    tokenizer = Tokenizer(num_words=vocabulary_size)
    tokenizer.fit_on_texts(behaviors)
    # print(tokenizer.word_index) # to see the dictionary
    sequences = tokenizer.texts_to_sequences(behaviors)
    seq_data = pad_sequences(sequences, maxlen=embed_dim)
    print(seq_data[6])
    print("seq_data shape", seq_data.shape)



    # Network architecture
    model = Sequential()
    model.add(Embedding(vocabulary_size, embed_dim, input_length=seq_data.shape[
        1], dropout = 0.2))
    model.add(LSTM(lstm_out, dropout_U=0.2, dropout_W=0.2))
    model.add(Dense(3, activation='softmax'))

    optimizer = RMSprop(lr=0.001)
    model.compile(loss='categorical_crossentropy', optimizer='adam',
                  metrics=[categorical_accuracy])
    print(model.summary())

    # Fit the model
    history = model.fit(seq_data, score, validation_split=0.4, epochs=36,
                        verbose=2)
    print(history.history.keys())

    # summarize history for accuracy
    plt.plot(history.history['categorical_accuracy'])
    plt.plot(history.history['val_categorical_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()

    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()

    print(model.predict(seq_data))
    print(score)


if __name__ == "__main__":
    NNModel(2)


