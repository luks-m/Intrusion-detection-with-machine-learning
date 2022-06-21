from numpy import array
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Flatten,Embedding,Dense

# Define 10 restaurant reviews
reviews =[
          'Never coming back!',
          'horrible service',
          'rude waitress',
          'cold food',
          'horrible food!',
          'awesome',
          'awesome services!',
          'rocks',
          'excelent work',
          'couldn\'t have done better'
]
#Define labels
labels = array([1,1,1,1,1,0,0,0,0,0])

vocab_size = 50
encoded_reviews = [one_hot(d, vocab_size) for d in reviews]
print(f'encoded reviews: {encoded_reviews}')

max_length = 4
padded_reviews = pad_sequences(encoded_reviews, maxlen=max_length, padding = 'post')
print(padded_reviews)

model = Sequential()
embedding_layer = Embedding(input_dim = vocab_size, output_dim = 8, input_length = max_length)
model.add(embedding_layer)
model.add(Flatten())
model.add(Dense(1,activation = 'sigmoid'))
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['acc'])

model.fit(padded_reviews,labels,epochs=100)

print(embedding_layer.get_weights()[0].shape)