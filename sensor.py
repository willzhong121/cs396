import numpy
import random
import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import constants as c

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.iterations)
        
    def Get_Value(self, time):
        self.values[time] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if(time == 999):
            print(self.values)