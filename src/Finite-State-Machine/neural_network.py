import numpy as np

from keras.layers import LSTM, Dense
from keras.models import Sequential

from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import plot_model

from log_generation import logs_generator, reformate, state_machine

import utils

NB_LOGS = 1000
LOG_SIZE = 20

if __name__=="__main__":
    #get logs
    data = logs_generator(state_machine, NB_LOGS, LOG_SIZE)
    data = reformate(data)

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
    model.add(LSTM(1000, input_shape=(X_train.shape[1], 2), return_sequences=True))
    model.add(Dense(2, activation='softmax'))

    model.summary()

    plot_model(model, to_file='plot.png', show_layer_names=True)

    #Train the model with callback
    checkpoint = ModelCheckpoint("saved_model.h5", monitor='loss', verbose=1, save_best_only=True)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=30, batch_size=32, callbacks=[checkpoint])


