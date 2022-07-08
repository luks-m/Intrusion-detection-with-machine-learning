from tensorflow.keras.models import load_model
import numpy as np
import pickle
from neural_network import LOG_SIZE

def vector_to_binary(vector) :
    binary = []
    for i in range(len(vector)) :
        if vector[i] > 0.5 :
            binary.append(1)
        else :
            binary.append(0)
    return np.array(binary)

def predict_output(model, input) :
        input = np.zeros((len(input)))
        for i in range(len(input)) :
            if input[i] == 'a' :
                input[i] = 0.25
            else :
                input[i] = 0.75
        tmp = [input]
        tmp = np.array(tmp)
        pred = model.predict(tmp)
        pred = vector_to_binary(pred[0])

        print(pred)
        return pred

if __name__=="__main__":
    # Load the model and tokenizer
    model = load_model('saved_model.h5')

    while(True):
        entry = input("Enter the input in the format \"a b b b a ... a b a\" (x{}) (0 if you want to stop): ".format(LOG_SIZE))

        if entry == "0":
            print("Execution completed.....")
            break

        else:
            try:
                entry = entry.split(" ")
                print(entry)

                if len(entry) != LOG_SIZE :
                    raise ValueError("Invalid input. Please enter the input in the format \"a b b b a ... a b a\" (x{})".format(LOG_SIZE))
            
                predict_output(model, entry)
                
            except Exception as e:
                print("Error occurred: ",e)
                continue
