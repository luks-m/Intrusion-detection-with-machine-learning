import numpy as np

from keras.layers import Embedding, LSTM, Dense
from keras.models import Sequential, load_model

from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical, plot_model

from log_generation import logs_generator, reformate, state_machine

NB_LOGS = 10000
LOG_SIZE = 10

if __name__=="__main__":
    #get logs
    data = logs_generator(state_machine, NB_LOGS, LOG_SIZE)
    data = reformate(data)

    #creating data and response
    X = []
    y = []
    for i in range(len(data)):
        X.append(data[i][0])
        y.append(data[i][1])
    X = np.array(X)
    y = np.array(y)

    #convert letters to numbers
    new_X = np.zeros((len(X), LOG_SIZE))
    new_y = np.zeros((len(y), LOG_SIZE))
    for i in range(len(X)) :
        for j in range(len(X[i])) :
            if X[i][j] == 'a' :
                new_X[i][j] = 0.25
            else :
                new_X[i][j] = 0.75
            if y[i,j] == '0' :
                new_y[i][j] = 0
            else :
                new_y[i][j] = 1

    #Split into training and testing sets
    X_train = new_X[:int(len(X) * 0.8)]
    X_test = new_X[int(len(X) * 0.8):]
    y_train = new_y[:int(len(y) * 0.8)]
    y_test = new_y[int(len(y) * 0.8):]

    # #reshape the data
    # X_train.reshape(X_train.shape[0], 1, X_train.shape[1])
    # print(X_train.shape)

    #creating the model
    model = Sequential()
    model.add(LSTM(1000, input_shape=(X_train.shape[1], 1), return_sequences=True))
    model.add(LSTM(100))
    model.add(Dense(LOG_SIZE, activation='relu'))

    model.summary()

    plot_model(model, to_file='plot.png', show_layer_names=True)

    #Train the model with callback
    checkpoint = ModelCheckpoint("saved_model.h5", monitor='loss', verbose=1, save_best_only=True)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=30, batch_size=32, callbacks=[checkpoint])


