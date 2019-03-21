
import numpy
import pandas as pd
import matplotlib.pyplot as plt


class LinearDiscriminant:
    def __init__(self, path):
        self.path = path

    def loadData(self):
        # load data from file
        data = pd.read_csv(self.path, sep = '\t', header=None)
        data.columns = ['side_effect', 'recovery', 'class_type']
        data_A = data.values[0:199]
        data_B = data.values[200:399]

        # plot the features
        print(data_A[:, 0])

        # for A
        plt.plot(data_A[:, 0], data_A[:, 1], 'ro', label='class1')

        # for B
        plt.plot(data_B[:, 0], data_B[:, 1], 'g^',  label='class2')

        plt.xlabel('side_effect')
        plt.ylabel('recovery')
        plt.legend()
        plt.show()


datapath = 'data/medical.txt'
obj = LinearDiscriminant(datapath)
obj.loadData()

