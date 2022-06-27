import pickle
from tkinter.tix import WINDOW
import numpy as np
import os

from keras.preprocessing.text import Tokenizer
from keras.layers import Embedding, LSTM, Dense
from keras.models import Sequential, load_model

from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical, plot_model

WINDOW_SIZE = 4
NB_LINE_MAX = 500

#Load the data file
file = open("short-text.txt", "r", encoding = "utf8")

#Store file in list
lines = []
counter = 0
for i in file:
    lines.append(i)
    counter += 1
    if counter >= NB_LINE_MAX:
        break
    

#Convert list to string
data = ""
for i in lines:
  data = ' '. join(lines) 

#Replace unnecessary stuff with space
data = data.replace('\n', '').replace('\r', '').replace('\ufeff', '').replace('“','').replace('”','').replace(',', '').replace('.', '')  #new line, carriage return, unicode character, coma, point --> replace by space

#Remove unnecessary spaces 
data = data.split()
data = ' '.join(data)

print("\nLen of data: ", len(data))
print("\nThis is a part of the text :\n",data[:500],"\n")

#Apply tokenization and some other changes
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])

# saving the tokenizer for predict function
pickle.dump(tokenizer, open('token.pkl', 'wb'))

sequence_data = tokenizer.texts_to_sequences([data])[0]
print("\nLen of sequence_data: ", len(sequence_data))
print("\n",sequence_data[:15])

vocab_size = len(tokenizer.word_index) + 1
print("\nVocab size: ", vocab_size)

sequences = []

for i in range(WINDOW_SIZE, len(sequence_data)):
    words = sequence_data[i-WINDOW_SIZE:i+1]
    sequences.append(words)
    
print("The Length of sequences are: ", len(sequences))
sequences = np.array(sequences)
print("\n",sequences[:10])

#Creating the data and response
X = []
y = []
for i in sequences:
    X.append(i[0:WINDOW_SIZE])
    y.append(i[WINDOW_SIZE])
X = np.array(X)
y = np.array(y)

print("Data: ", X[:10])
print("Response: ", y[:10])

y = to_categorical(y, num_classes=vocab_size)
print("\nClass:,", y[:5])

#Creating the model
model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=WINDOW_SIZE))
model.add(LSTM(1000))
model.add(Dense(1000, activation="relu"))
model.add(Dense(vocab_size, activation="softmax"))

model.summary()

plot_model(model, to_file='plot.png', show_layer_names=True)

#Train the model with callback
checkpoint = ModelCheckpoint("next_words.h5", monitor='loss', verbose=1, save_best_only=True)
model.compile(loss="categorical_crossentropy", optimizer=Adam(learning_rate=0.001))
model.fit(X, y, epochs=30, batch_size=64, callbacks=[checkpoint])

