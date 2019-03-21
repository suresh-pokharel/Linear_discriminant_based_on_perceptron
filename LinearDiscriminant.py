
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import genfromtxt

class LinearDiscriminant:
    def __init__(self, path, threshold, learning_rate, no_of_inputs):
        self.path = path
        self.data = []
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.random.uniform(-0.5, 0.5, no_of_inputs + 1)

    def load_data(self):
        # load data from file
        self.data = genfromtxt(self.path, delimiter='\t')

        # self.data.columns = ['side_effect', 'recovery', 'class_type']


    def plot_initial_data(self):
        data_a = self.data[0:199]
        data_b = self.data[200:399]

        # plot the features
        # for A
        plt.plot(data_a[:, 0], data_a[:, 1], 'ro', label='class1')

        # for B
        plt.plot(data_b[:, 0], data_b[:, 1], 'g^', label='class2')

        plt.xlabel('side_effect')
        plt.ylabel('recovery')
        plt.legend()
        # plt.show()

    def train(self):
        epochs = 100
        for i in range(epochs):
            for inputs in self.data:
                prediction = self.predict(inputs)
                self.weights[0] += self.learning_rate * (inputs[2] - prediction) * inputs[0]
                self.weights[1] += self.learning_rate * (inputs[2] - prediction) * inputs[1]
                self.weights[2] += self.learning_rate * (inputs[2] - prediction)
        print(self.weights)


    def predict(self, inputs):
        # x1w1 + x2w2+ ... + bias
        summation = inputs[0] * self.weights[0]+ inputs[1] * self.weights[1] + self.weights[2]

        if summation > 0:
          activation = 1
        else:
          activation = 2
        return activation

    def plot_final_data(self):
        # fig config
        weights = self.weights
        print(weights)
        weights = [ 54.32548751, -55.73517894,  25.22175294]
        inputs = self.data
        # plt.figure(figsize=(10, 6))

        # plot input samples(2D data points) and i have two classes.
        # one is +1 and second one is -1, so it red color for +1 and blue color for -1
        #for input, target in zip(inputs, targets):
           # plt.plot(input[0], input[1], 'ro' if (target == 1.0) else 'bo')

        # calculating slope and intercept with given three weights
        slope = -(weights[2] / weights[1]) / (weights[2] / weights[0])
        intercept = -weights[2] / weights[1]

        print('slope--->'+str(slope))
        print('intercept--->'+str(intercept))

        self.plot_initial_data()
        for i in np.linspace(np.amin(inputs[:, :1]), np.amax(inputs[:, :1])):
            # y =mx+c, m is slope and c is intercept
            y = (slope * i) + intercept
            plt.plot(i, y, 'ko')
        plt.show()

datapath = 'data/medical.txt'
threshold = 0
no_of_input = 2
learning_rate = 0.005
obj = LinearDiscriminant(datapath, threshold, learning_rate, no_of_input)
obj.load_data()
# obj.plot_initial_data()
obj.train()
obj.plot_final_data()
