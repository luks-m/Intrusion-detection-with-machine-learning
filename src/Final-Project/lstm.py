import generator as gen
import alerts_launcher as al
import alerts_sorter as aso
from utils import get_one_hots

import numpy as np
import pickle
from keras.layers import LSTM, Dense
from keras.models import Sequential

from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import plot_model

NB_LOGS = 100000
LOG_LENGTH = 8

if __name__ == "__main__":
    #Get logs from generator automaton
    logs = gen.generate_logs(gen.state_machine, NB_LOGS, LOG_LENGTH)
    logs = gen.reformate_logs(logs)

    #Get alerts from logs
    alerts = []
    attacks = []
    for log in logs:
        if al.is_alert(log):
            alerts.append(log)
            if aso.is_attack(log):
                attacks.append([1])
            else:
                attacks.append([0])

    print("\n Alerts : \n", alerts)
    print("\n Attacks : \n", attacks)
    print("\n Nb of alerts : \n", len(alerts))

    #Get one-hots from alerts
    classes = []
    for i in range(gen.NB_INPUTS):
        classes.append('a' + str(i))
    X = get_one_hots(alerts, classes)
    print("\n One-hots : \n", X)
    y = get_one_hots(attacks, [0, 1])
    new_y = np.zeros((len(y), 2))
    for i in range(len(y)):
        new_y[i][0] = y[i][0][0]
        new_y[i][1] = y[i][0][1]
    

    #split into training and testing sets
    X_train = X[:int(len(X) * 0.8)]
    X_test = X[int(len(X) * 0.8):]
    y_train = new_y[:int(len(new_y) * 0.8)]
    y_test = new_y[int(len(new_y) * 0.8):]

    print(X_train.shape)
    print(y_train.shape)
    
    print(y_train.shape)

    #Model LSTM
    model = Sequential()
    model.add(LSTM(1, input_shape=(LOG_LENGTH, gen.NB_INPUTS)))
    model.add(Dense(2, activation='softmax'))

    model.summary()

    plot_model(model, to_file='plot.png', show_layer_names=True)

    checkpoint = ModelCheckpoint('model.h5', monitor='val_loss', verbose=1, save_best_only=True)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=150, batch_size=20, callbacks=[checkpoint])

    #Save the model
    file = open("history.txt", "wb")
    pickle.dump(history, file)
    file.close()
   