import numpy as np
from model.model import Model

data_train = np.genfromtxt('data/data_train.csv', delimiter=',')
data_test  = np.genfromtxt('data/data_test.csv',  delimiter=',')

x_train = data_train.T[0].reshape((data_train.shape[0], 1))
y_train = data_train.T[1].reshape((data_train.shape[0], 1))

x_test  = data_test.T[0].reshape((data_test.shape[0], 1))
y_test  = data_test.T[1].reshape((data_test.shape[0], 1))

model = Model(input_dim=x_train.shape[1])
model.train(x_train, y_train)
