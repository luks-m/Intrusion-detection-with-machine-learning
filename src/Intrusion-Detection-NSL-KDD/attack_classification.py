import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.metrics import *
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import ModelCheckpoint


#load the csv file containing the column names and adding the columns class and difficulty
filed_names = pd.read_csv("field_names.csv", header = None)
columns = list(filed_names[0].values)
columns += ['class', 'difficulty']

#loading train and test data files
data_train = pd.read_csv('KDDTrain+.txt', names = columns)

print("Training data : \n", data_train.head())
print("Shape of the training data : {}".format(data_train.shape))

#Load attacks.txt containing the attack categories
map_attacks = [x.strip().split() for x in open('attacks.txt', 'r')]
map_attacks = {k:v for (k,v) in map_attacks}

#Replace the class column values to 5 attack categories in training dataframe
data_train['class'] = data_train['class'].replace(map_attacks)

#Mixing the dataframe
data_train = shuffle(data_train)

#Separate the training dataframe into input and output
X = data_train.drop('class', axis = 1)
y = data_train['class']

#Converting String to Integer with get_dummies by pandas
used_columns = ['protocol_type', 'service', 'flag']
X_new = pd.get_dummies(X, columns = used_columns, drop_first = True)
y_new = data_train['class']
y_new = pd.get_dummies(y_new)

#Split data: 60% training and 40% testing 
X_train, X_test, y_train, y_test = train_test_split(X_new, y_new, test_size = 0.4, random_state = 101)

#Use StandardScaler() to standardize data
sc = StandardScaler()
sc.fit(np.array(X_train))
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

#Resize the data to fit the model
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

#Creation of the model
model = Sequential()
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2, input_shape=(120, 1)))
model.add(Dense(5, activation='softmax'))

#Summary of model architecture 
model.summary()

#Compilation of the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(X_train.shape)
print(X_test.shape)
print(len(X_train[0]))

#Fit the model on our data.
checkpoint = ModelCheckpoint("best_model.h5", monitor='loss', verbose=1, save_best_only=True)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(X_train, y_train, validation_data = (X_test, y_test), batch_size = 32, epochs = 20, callbacks=[checkpoint])

loss, accuracy = model.evaluate(X_test, y_test)
print("\nLoss: %.2f, Accuracy: %.2f%%" % (loss, accuracy*100))
