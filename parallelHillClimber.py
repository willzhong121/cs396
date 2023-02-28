import numpy
import random
import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import constants as c
from solution import SOLUTION
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        self.data = [0] * c.numberOfGenerations

    def Evolve(self):
        self.Evaluate(self.parents)
        for gen_current in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(gen_current)
        

    def Evolve_For_One_Generation(self, gen_current):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select(gen_current)
        '''
        self.child.Evaluate("DIRECT")
        
        self.Select()
        '''

    def Print(self):
        for i in self.parents.keys():
            print(str(self.parents[i].fitness) + ", " + str(self.children[i].fitness))

    def Spawn(self):
        self.children = {}
        for i in range(len(self.parents)):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self, gen_current):
        for i in self.parents.keys():
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]
        
        maxF = 0
        for i in (self.parents.keys()):
            if(self.parents[i].fitness > maxF):
                maxF = self.parents[i].fitness

        self.data[gen_current] = maxF

    def Show_Best(self):
        max = self.parents[0].fitness
        index = 0
        for i in self.parents.keys():
            if self.parents[i].fitness < max:
                max = self.parents[i].fitness
                index = i

        with open("file1.npy", "wb") as f:
            numpy.save(f,numpy.array(self.data))
        self.parents[index].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")

        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()
