import numpy as np

from keras.models import Sequential
from keras.layers import Dense, LSTM, Activation
import keras


# Fill out the function below that transforms the input series
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = [series[ix:ix + window_size] for ix in range(len(series) - window_size)]
    y = [series[iy] for iy in range(window_size, len(series))]

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y


# Build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1))
    return model


# Return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = set("!,.:;? ")
    lower = set('abcdefghijklmnopqrstuvwxyz')
    keep = lower | punctuation
    valid = "".join(list(map(lambda x: x if x in keep else ' ', text)))
    return valid


# Fill out the function below that transforms the input text and window-size into a set of input/output pairs
# for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = [text[ix:ix + window_size] for ix in range(0, len(text) - window_size, step_size)]
    outputs = [text[iy] for iy in range(window_size, len(text), step_size)]

    return inputs, outputs


# Build the required RNN model:
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    model = Sequential()
    model.add(LSTM(200, input_shape=(window_size, num_chars)))
    model.add(Dense(num_chars, activation="linear"))
    model.add(Activation('softmax'))
    return model
