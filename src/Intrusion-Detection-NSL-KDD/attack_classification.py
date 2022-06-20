import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.metrics import *
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

from keras.preprocessing import sequence
from keras import optimizers
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Activation, Embedding, SimpleRNN, BatchNormalization

#load the csv file containing the column names 
column_name = pd.read_csv("field_names.csv", header = None)

#Convert the array into list
new_columns = list(column_name[0].values)

#adding difficulty 
new_columns += ['class', 'difficulty']

#loading train and test data files
train_data = pd.read_csv('KDDTrain+.txt', names = new_columns)
test_data = pd.read_csv('KDDTest+.txt', names = new_columns)

#Print of training dataset
print("The training data is")
print(train_data.tail())

#Print of testing dataset
print("The testing data is")
print(test_data.head())

#Output total rows and columns of dataframes
print(f"The shape of the training dataframe is : {train_data.shape}")
print(f"The shape of the testing dataframe is : {test_data.shape}")

#Load attacks.txt containing the attack categories
map_attacks = [x.strip().split() for x in open('attacks.txt', 'r')]
map_attacks = {k:v for (k,v) in map_attacks}

#Replace the "class" column values to 5 attack categories in training and testing dataframe
train_data['class'] = train_data['class'].replace(map_attacks)
test_data['class'] = test_data['class'].replace(map_attacks)

train_data = shuffle(train_data)

#Separate the training dataframe into feature columns and label columns
X = train_data.drop('class', axis = 1) #Independent features
y = train_data['class'] #Dependent features (Labels)

#Converting String to Integer with get_dummies by pandas
columns = ['protocol_type', 'service', 'flag']
X_new = pd.get_dummies(X, columns = columns, drop_first = True)
y_new = train_data['class']
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

#Compilation of the model w.r.t three paramaters: 
#Loss - The loss function - "categorical_loss" is used because of the multi-class classifcation problem.
#Optimizer - To minimize the loss function.
#Metrics - The mode of evaluation for our model.
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#Fit the model on our data.
#X_train - The feature columns of the training data.
#y_train - The labels columns of the training data.
#validation_data - The validation data
#batch_size and epochs further explained in document. 
history = model.fit(X_train, y_train, validation_data = (X_test, y_test), batch_size = 32, epochs = 20)

loss, accuracy = model.evaluate(X_test, y_test)
print("\nLoss: %.2f, Accuracy: %.2f%%" % (loss, accuracy*100))
