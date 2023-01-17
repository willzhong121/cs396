import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim

class WORLD:
    def __init__(self) -> None:
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")