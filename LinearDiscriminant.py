
import numpy
class LinearDiscriminant:

    def __init__(self, path):
        self.path = path

    def loadData(self):
        # load data from file
        data = numpy.loadtxt

datapath = 'data/medical.txt'
obj = LinearDiscriminant()
obj.loadData()

