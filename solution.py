import numpy
import random
import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import constants as c
import os

class SOLUTION:
    def __init__(self, nextID):
        self.weights = numpy.random.rand(5,4)
        self.weights = self.weights * 2 -1
        self.myID = nextID
    
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        for j in range(5):
            i = 0.5
            while i < 3:
                pyrosim.Send_Cube(name="Box", pos=[-2, -2+j, i], size=[1,1,1])
                i = i + 1
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        '''
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1,1,1])
        
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
        
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])

        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
        '''
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 2.5], size=[1,1,2])

        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,2])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,2])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.Send_Joint(name = "BackLeg_BackerLeg" , parent= "BackLeg" , child = "BackerLeg" , type = "revolute", position = [-1,0,-1])
        pyrosim.Send_Cube(name="BackerLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.Send_Joint(name = "FrontLeg_FronterLeg" , parent= "FrontLeg" , child = "FronterLeg" , type = "revolute", position = [1,0,-1])
        pyrosim.Send_Cube(name="FronterLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])


        pyrosim.End()

    def Create_Brain(self):
        '''
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        '''
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "BackerLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "FronterLeg")

        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "BackLeg_BackerLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "FrontLeg_FronterLeg")

        '''
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn] )
        '''
        for currentRow in range(5):
            for currentColumn in range(3):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+5 , weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()

    def Evaluate(self, directOrGUI):
        self.Create_Body()
        self.Create_Brain()
        self.Create_World()
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID))
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()

    def Start_Simulation(self, directOrGUI):
        self.Create_Body()
        self.Create_Brain()
        self.Create_World()
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()  
        os.system("del fitness" + str(self.myID) + ".txt")

    def Mutate(self):
        self.weights[random.randint(0,2), random.randint(0,1)] = random.random()*2-1

    def Set_ID(self, ID):
        self.myID = ID