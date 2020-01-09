from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, Dense, LSTM, GaussianDropout, \
    GaussianNoise, Dropout
from keras.metrics import categorical_accuracy
from keras.optimizers import RMSprop
from keras.utils import to_categorical

import matplotlib.pyplot as plt

from data_preprocessor import *
from interaction_components import *

"""Reads in and parse interaction trajectory data from experiments  (
input_style==1) or from generated sudo data (input_style==2). Constructs LSTM
model to learn trajectory patterns"""
def NNModel(input_style):
    # read from input files
    score, behaviors, prefix = data_preprocessor(input_style)
    score = to_categorical(score, 3)
    score_Test = score[0:int(len(score)/5)]
    score_Train = score[int(len(score)/5):len(score)-1]
    print("score_Train shape", score_Train.shape)

    # parameter values
    vocabulary_size = 50 # an estimation
    embed_dim = 50
    lstm_out = 128

    # padding to prep data for NN model
    tokenizer = Tokenizer(num_words=vocabulary_size)
    tokenizer.fit_on_texts(behaviors)
    # print(tokenizer.word_index) # to see the dictionary
    sequences = tokenizer.texts_to_sequences(behaviors)
    seq_data = pad_sequences(sequences, maxlen=embed_dim)
    seq_data_Test = seq_data[0:int(len(score)/5)]
    seq_data_Train = seq_data[int(len(score)/5):len(seq_data)-1]
    print("seq_data_Train shape", seq_data_Train.shape)

    # Network architecture
    model = Sequential()
    model.add(Embedding(vocabulary_size, embed_dim,
                        input_length=seq_data_Train.shape[1]))
    model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.1))
    model.add(Dense(3, activation='softmax'))
    optimizer = RMSprop(lr=0.001)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer,
                  metrics=[categorical_accuracy])
    print(model.summary())

    # Fit the model
    history = model.fit(seq_data_Train, score_Train, epochs=50, verbose=2,
                        validation_data=(seq_data_Test, score_Test))

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

    # evaluation of model on test data set
    test_history = model.evaluate(seq_data_Test, score_Test, verbose=2)
    print("test set loss: ", test_history[0], " test set accuracy",
          test_history[1])

if __name__ == "__main__":
    NNModel(2)


