import numpy
import random
import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.motorvalues = {}
                
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset

        for i, j in enumerate(numpy.linspace(-numpy.pi, numpy.pi, c.iterations)):
            self.motorvalues[i] = self.amplitude * numpy.sin(self.frequency * i + self.offset)


    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId, 
            jointName = self.jointName, 
            controlMode = p.POSITION_CONTROL, 
            targetPosition = desiredAngle, 
            maxForce = 100)