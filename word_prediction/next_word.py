from tensorflow.keras.models import load_model
import numpy as np
import pickle

WINDOW_SIZE = 4

# Load the model and tokenizer
model = load_model('next_words.h5')
tokenizer = pickle.load(open('token.pkl', 'rb'))


def Predict_Next_Words(model, tokenizer, text):
    sequence = tokenizer.texts_to_sequences([text])
    sequence = np.array(sequence)
    preds = np.argmax(model.predict(sequence))
    predicted_word = ""

    for key, value in tokenizer.word_index.items():
        if value == preds:
            predicted_word = key
            break

    print(predicted_word)
    return predicted_word

while(True):
    text = input("Enter your line (0 if you want to stop): ")

    if text == "0":
        print("Execution completed.....")
        break

    else:
        try:
            text = text.split(" ")
            text = text[-WINDOW_SIZE:]
            print(text)
        
            Predict_Next_Words(model, tokenizer, text)
            
        except Exception as e:
            print("Error occurred: ",e)
            continue
