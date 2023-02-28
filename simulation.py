from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK



class SIMULATION:
    def __init__(self, directOrGUI, solutionID):

        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        self.directOrGUI = directOrGUI

    def Run(self):
        for i in range(c.iterations):
            p.stepSimulation()
            if(self.directOrGUI == "GUI"):
                time.sleep(1/100)
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            # print(i)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
    


