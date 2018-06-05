import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import sys

class Model:

  def __init__(self, input_dim):
    self.model     = Sequential()

    self.model.add(Dense(40, activation='relu', input_dim=input_dim))
    self.model.add(Dense(40, activation='relu'))
    self.model.add(Dense(40, activation='relu'))
    self.model.add(Dense(40, activation='relu'))
    self.model.add(Dense(40, activation='relu'))
    self.model.add(Dense(40, activation='relu'))
    self.model.add(Dense(1,  activation='linear'))
    self.model.compile(loss='mse', optimizer='sgd', metrics=['accuracy'])

  def train(self, x_train, y_train, epochs=101, save_imgs=True):
    for epoch in np.arange(1, epochs):

      self.model.fit(x_train, y_train, batch_size=128)

      if save_imgs:
        plt.plot(x_train, y_train, 'g.', ms=1)
        plt.plot(x_train, self.model.predict(x_train), 'r.', ms=1)
        plt.axis([
           x_train.min() - 0.5, x_train.max() + 0.5,
           y_train.min() - 0.5, y_train.max() + 0.5,
        ])
        plt.title(f"Epoch #{epoch}")
        plt.savefig(f"img/plot_{epoch}.png")
        plt.clf()
