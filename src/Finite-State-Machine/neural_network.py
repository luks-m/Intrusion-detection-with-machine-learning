import numpy as np
from pickle import *
import sys
import tensorflow as tf
from keras.layers import LSTM, Dense, LSTMCell, RNN
from keras.models import Sequential

from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import plot_model

#import callback

import utils

NB_LOGS = 10000
NB_HIDDEN_NEURONS = 1000
NB_EPOCHS= 10
LOG_SIZE = 30

argc = len(sys.argv)
if argc != 3:
    print("Default NB_HIDDEN_NEURONS = 1000")
    print("Default NB_EPOCHS = 10")
else :
    NB_HIDDEN_NEURONS = int(sys.argv[1])
    NB_EPOCHS = int(sys.argv[2])
    print("NB_HIDDEN_NEURONS = {}".format(NB_HIDDEN_NEURONS))
    print("NB_EPOCHS = {}".format(NB_EPOCHS))

if __name__=="__main__":
    #get logs
    f = open("data_saved.txt", "rb")
    data = load(f)

    #creating data with inputs and outputs
    X = []
    y = []
    for i in range(len(data)):
        X.append(data[i][0])
        y.append(data[i][1])
    X = np.array(X)
    y = np.array(y)

    #convert letters to numbers
    new_X =utils.get_one_hots(X, 2)
    new_y = utils.get_one_hots(y, 2)

    #Split into training and testing sets
    X_train = new_X[:int(len(X) * 0.8)]
    X_test = new_X[int(len(X) * 0.8):]
    y_train = new_y[:int(len(y) * 0.8)]
    y_test = new_y[int(len(y) * 0.8):]

    #creating the model
    model = Sequential()
    model.add(RNN(LSTMCell(NB_HIDDEN_NEURONS), input_shape=(LOG_SIZE, 2), return_sequences=True))
    model.add(Dense(2, activation='softmax'))

    model.summary()

    plot_model(model, to_file='plot.png', show_layer_names=True)

    #Creating callback
    #weight_callback = callback.WeightCallback(model, "logs/weights_values.txt")
    checkpoint = ModelCheckpoint('saved_model.h5', monitor='val_loss', verbose=1, save_best_only=True)

    #Compile the model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=NB_EPOCHS, batch_size=50, callbacks=[checkpoint])

    #Analyse the model history
    file = open("history.txt", "wb")
    dump(history, file)
    file.close
