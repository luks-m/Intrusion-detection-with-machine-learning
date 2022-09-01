import numpy as np

#Get one hot encoding of a given input
def one_hot_encoder(X, n_classes):
    encoded = np.zeros((len(X), n_classes))
    for i in range(len(X)):
        if X[i] == 'a':
            encoded[i][0] = 1
        elif X[i] == 'b':
            encoded[i][1] = 1
        elif X[i] == '0':
            encoded[i][0] = 1
        elif X[i] == '1':
            encoded[i][1] = 1
    return encoded.tolist()

#Get one hot encoding for all the inputs
def get_one_hots(sequence, n_classes):
    inputs = []
    for i in range(len(sequence)):
        inputs.append(one_hot_encoder(sequence[i], n_classes))
    return np.array(inputs)

#Convert result of the layer to binary values
def one_hot_decoder(X):
    decoded = []
    for i in range(len(X)):
        if X[i][0] > X[i][1]:
            decoded.append(0)
        else:
            decoded.append(1)
    return decoded

def get_results(outputs):
    results = []
    for i in range(len(outputs)):
        results.append(one_hot_decoder(outputs[i]))
    return results


if __name__=="__main__":
    inputs = [['a', 'b', 'b', 'b', 'a', 'a', 'a', 'b', 'a', 'b'], ['a', 'b', 'b', 'b', 'a', 'a', 'a', 'b', 'a', 'a']]
    print(get_one_hots(inputs, 2))

