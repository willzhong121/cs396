from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK



class SIMULATION:
    def __init__(self):

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(c.iterations):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            time.sleep(1/1000)
            # print(i)

    def __del__(self):
        p.disconnect()
    


