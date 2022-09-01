import sys
sys.path.append('./../Finite-State-Machine/')
import finite_state_transducer as fst

import numpy as np

def is_accepted(state_machine, log) :
    state = state_machine.initial_state
    for i in range(len(log)):
        input = log[i]
        if input in state_machine.transitions[state] :
            state = state_machine.transitions[state][input]['next_state']
        else:
            return False
    return state_machine.is_final_state(state)

#Get index of a given input in classes list
def get_index(input, classes):
    for i in range(len(classes)):
        if input == classes[i]:
            return i
    return -1

#Get one hot encoding of a given input
def one_hot_encoder(X, classes):
    n_classes = len(classes)
    size = len(X)
    encoded = np.zeros((size, n_classes))

    for i in range(size):
        encoded[i][get_index(X[i], classes)] = 1
            
    return encoded.tolist()

#Get one hot encoding for all the inputs
def get_one_hots(sequence, classes):
    inputs = []
    for i in range(len(sequence)):
        inputs.append(one_hot_encoder(sequence[i], classes))
    return np.array(inputs)

if __name__ == "__main__":
    input = ['a4', 'a4', 'a3', 'a3', 'a0']
    print(one_hot_encoder(input, ['a0', 'a1', 'a2', 'a3', 'a4']))

    inputs =   [['a4', 'a4', 'a3', 'a3', 'a0'], 
                ['a4', 'a4', 'a3', 'a3', 'a0'], 
                ['a2', 'a4', 'a3', 'a4', 'a3'], 
                ['a4', 'a0', 'a4', 'a3', 'a3'], 
                ['a4', 'a4', 'a3', 'a3', 'a0'], 
                ['a2', 'a4', 'a3', 'a0', 'a4']]
    print(get_one_hots(inputs, ['a0', 'a1', 'a2', 'a3', 'a4']))