from keras.models import load_model
import numpy as np
import pickle
from neural_network import LOG_SIZE
import utils

def predict_output(model, entry) :
        input = utils.one_hot_encoder(entry, 2)
        tmp = [input]
        tmp = np.array(tmp)
        pred = model.predict(tmp)

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
            
                pred = predict_output(model, entry)

                print("Results of prediction : {}".format(utils.get_results(pred)))
                
            except Exception as e:
                print("Error occurred: ",e)
                continue
