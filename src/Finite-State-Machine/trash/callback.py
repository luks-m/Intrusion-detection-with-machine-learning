from tensorflow import keras

class WeightCallback(keras.callbacks.Callback):
    def __init__(self, model, path_to_file):
        self._model = model
        self._file = path_to_file

    def on_train_begin(self, logs=None):
        file = open(self._file, "a")
        file.write("Starting training; weights value {}".format(self._model.get_weights()))
        file.close()

    def on_train_end(self, logs=None):
        file = open(self._file, "a")
        file.write("Stop training; weights value {}".format(self._model.get_weights()))
        file.close()

    def on_epoch_begin(self, epoch, logs=None):
        file = open(self._file, "a")
        file.write("Start epoch {} of training; weights value {}".format(epoch, self._model.get_weights()))
        file.close()

    def on_epoch_end(self, epoch, logs=None):
        file = open(self._file, "a")
        file.write("End epoch {} of training; weights value {}".format(epoch, self._model.get_weights()))
        file.close()

    def on_test_begin(self, logs=None):
        file = open(self._file, "a")
        file.write("Start testing; weights value {}".format(self._model.get_weights()))
        file.close()

    def on_test_end(self, logs=None):
        file = open(self._file, "a")
        file.write("Stop testing; weights value {}".format(self._model.get_weights()))
        file.close()

    def on_predict_begin(self, logs=None):
        file = open(self._file, "a")
        file.write("Start predicting; weights value {}".format(self._model.get_weights()))
        file.close()

    def on_predict_end(self, logs=None):
        file = open(self._file, "a")
        file.write("Stop predicting; weights value {}".format(self._model.get_weights()))
        file.close()

    def on_train_batch_begin(self, batch, logs=None):
        file = open(self._file, "a")
        file.write("...Training: start of batch {}; weights value {}".format(batch, self._model.get_weights()))
        file.close()

    def on_train_batch_end(self, batch, logs=None):
        file = open(self._file, "a")
        file.write("...Training: end of batch {}; weights value {}".format(batch, self._model.get_weights()))
        file.close()

    def on_test_batch_begin(self, batch, logs=None):
        file = open(self._file, "a")
        file.write("...Evaluating: start of batch {}; weights value {}".format(batch, self._model.get_weights()))
        file.close()

    def on_test_batch_end(self, batch, logs=None):
        file = open(self._file, "a")
        file.write("...Evaluating: stop of batch {}; weights value {}".format(batch, self._model.get_weights()))
        file.close()

    def on_predict_batch_begin(self, batch, logs=None):
        file = open(self._file, "a")
        file.write("...Predicting: start of batch {}; weights value {}".format(batch, self._model.get_weights()))
        file.close()

    def on_predict_batch_end(self, batch, logs=None):
        file = open(self._file, "a")
        file.write("...Predicting: end of batch {}; weights value {}".format(batch, self._model.get_weights()))
        file.close()