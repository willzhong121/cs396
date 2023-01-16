import numpy
import random
import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

amplitude = numpy.pi/4
frequency = 0.05
phaseOffset = 0
amplitude2 = numpy.pi/4
frequency2 = 0.05
phaseOffset2 = numpy.pi/4
backLegAngles = numpy.zeros(1000)
frontLegAngles = numpy.zeros(1000)

for i, j in enumerate(numpy.linspace(-numpy.pi, numpy.pi, 1000)):
    backLegAngles[i] = amplitude * numpy.sin(frequency * i + phaseOffset)
    frontLegAngles[i] = amplitude2 * numpy.sin(frequency2 * i + phaseOffset2)

# numpy.save('backlegangles.npy', backLegAngles)
# numpy.save('frontlegangles.npy', frontLegAngles)
# exit()

for i in range(1000):
    time.sleep(1/60)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId, 
        jointName = b'Torso_BackLeg', 
        controlMode = p.POSITION_CONTROL, 
        targetPosition = backLegAngles[i], 
        maxForce = 100)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId, 
        jointName = b'Torso_FrontLeg', 
        controlMode = p.POSITION_CONTROL, 
        targetPosition = frontLegAngles[i], 
        maxForce = 500)

numpy.save('backlegsensorvalues.npy', backLegSensorValues)
numpy.save('frontlegsensorvalues.npy', frontLegSensorValues)
p.disconnect()