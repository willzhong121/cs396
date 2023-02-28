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
        self.weights = numpy.random.rand(20,20)
        self.weights = self.weights * 2 -1
        self.myID = nextID
    
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Random_size(self):
        return [random.uniform(0.3,1),random.uniform(0.3,1),random.uniform(0.3,1)]    

    def Determine_sensor(self):
        num = random.randint(0, 1)
        if num == 0:
            return ['    <color rgba="0.0 0.0 1.0 1.0"/>', 'Blue']
        else:
            return ['    <color rgba="0.0 1.0 0.0 1.0"/>', 'Green']

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        colormain = self.Determine_sensor()
        torso_dims = [random.uniform(0.5,1.5),random.uniform(1.5,2.5),random.uniform(0.25,1.5)]
        torso_posn = [0, 0, 3]
        pyrosim.Send_Cube(
            name="Main", pos=torso_posn, size = torso_dims, colorString = colormain[0], colorName = colormain[1])

        color1 = self.Determine_sensor()
        leg1_dims = self.Random_size()
        pyrosim.Send_Joint(
            name = "Main_Limb1" , parent= "Main" , child = "Limb1" , type = "revolute", position = [torso_dims[0]/2,torso_dims[1]/3,3-torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb1", pos=[leg1_dims[0]/2, 0, -leg1_dims[2]/2], size = leg1_dims, colorString = color1[0], colorName = color1[1])

        color2 = self.Determine_sensor()
        leg2_dims = self.Random_size()
        pyrosim.Send_Joint(
            name = "Main_Limb2" , parent= "Main" , child = "Limb2" , type = "revolute", position = [torso_dims[0]/2,-torso_dims[1]/3,3-torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb2", pos=[leg2_dims[0]/2, 0, -leg2_dims[2]/2], size = leg2_dims, colorString = color2[0], colorName = color2[1])

        color3 = self.Determine_sensor()
        leg3_dims = self.Random_size()
        pyrosim.Send_Joint(
            name = "Main_Limb3" , parent= "Main" , child = "Limb3" , type = "revolute", position = [-torso_dims[0]/2,torso_dims[1]/3,3-torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb3", pos=[-leg3_dims[0]/2, 0, -leg3_dims[2]/2], size = leg3_dims, colorString = color3[0], colorName = color3[1])
        
        color4 = self.Determine_sensor()
        leg4_dims = self.Random_size() 
        pyrosim.Send_Joint(
            name = "Main_Limb4" , parent= "Main" , child = "Limb4" , type = "revolute", position = [-torso_dims[0]/2,-torso_dims[1]/3,3-torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb4", pos=[-leg4_dims[0]/2, 0, -leg4_dims[2]/2], size = leg4_dims, colorString = color4[0], colorName = color4[1])

        color5 = self.Determine_sensor()
        leg5_dims = self.Random_size() 
        pyrosim.Send_Joint(
            name = "Main_Limb5" , parent= "Main" , child = "Limb5" , type = "revolute", position = [-torso_dims[0]/2,0,3+torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb5", pos=[-leg5_dims[0]/2, 0, leg5_dims[2]/2], size = leg5_dims, colorString = color5[0], colorName = color5[1])
    
        color6 = self.Determine_sensor()
        leg6_dims = self.Random_size() 
        pyrosim.Send_Joint(
            name = "Main_Limb6" , parent= "Main" , child = "Limb6" , type = "revolute", position = [torso_dims[0]/2,0,3+torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb6", pos=[leg6_dims[0]/2, 0, leg6_dims[2]/2], size = leg6_dims, colorString = color6[0], colorName = color6[1])
        
        color7 = self.Determine_sensor()
        leg7_dims = self.Random_size() 
        pyrosim.Send_Joint(
            name = "Main_Limb7" , parent= "Main" , child = "Limb7" , type = "revolute", position = [0,0,3+torso_dims[2]/2])
        pyrosim.Send_Cube(
            name="Limb7", pos=[0, 0, leg7_dims[2]/2], size = leg7_dims, colorString = color7[0], colorName = color7[1])
        
        color8 = self.Determine_sensor()
        leg8_dims = self.Random_size() 
        pyrosim.Send_Joint(
            name = "Main_Limb8" , parent= "Main" , child = "Limb8" , type = "revolute", position = [0,-torso_dims[1]/2,3])
        pyrosim.Send_Cube(
            name="Limb8", pos=[0, -leg8_dims[1]/2, 0], size = leg8_dims, colorString = color8[0], colorName = color8[1])

        color9 = self.Determine_sensor()
        leg9_dims = self.Random_size() 
        pyrosim.Send_Joint(
            name = "Main_Limb9" , parent= "Main" , child = "Limb9" , type = "revolute", position = [0,torso_dims[1]/2,3])
        pyrosim.Send_Cube(
            name="Limb9", pos=[0, leg8_dims[1]/2, 0], size = leg9_dims, colorString = color9[0], colorName = color9[1])
        
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Main")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Limb1")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Limb2")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "Limb3")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "Limb4")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "Limb5")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "Limb6")

        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Main_Limb1")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Main_Limb2")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Main_Limb3")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Main_Limb4")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Main_Limb5")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Main_Limb6")
        
        for currentRow in range(7):
            for currentColumn in range(6):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+7 , weight = self.weights[currentRow][currentColumn] )
        
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
        while True:
            try:
                f = open("fitness" + str(self.myID) + ".txt", "r")
                break
            except:
                pass
        # f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()  
        os.system("del fitness" + str(self.myID) + ".txt")

    def Mutate(self):
        self.weights[random.randint(0,2), random.randint(0,1)] = random.random()*2-1

    def Set_ID(self, ID):
        self.myID = ID