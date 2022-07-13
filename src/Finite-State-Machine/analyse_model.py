from keras.models import load_model

if __name__=="__main__":
    model = load_model('saved_model.h5')
    layer = model.get_layer("lstm")
    print(layer.get_weights())

    weights = model.get_weights()
    print(weights)