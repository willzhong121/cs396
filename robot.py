import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK




class ROBOT:
    def __init__(self) -> None:        
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, time):
        for i in self.sensors:
            self.sensors[i].Get_Value(time)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)   

    def Act(self, desiredAngle):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                encoded_jointName = jointName.encode('utf-8')
                self.motors[encoded_jointName].Set_Value(self.robotId, desiredAngle)
                print(neuronName, jointName, desiredAngle)
    
        # for i in self.motors:
            # self.motors[i].Set_Value(self.robotId, time)
    
    def Think(self):
        self.nn.Update()
        self.nn.Print()
