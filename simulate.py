import pybullet as p
import time
physicsClient = p.connect(p.GUI)
for i in range(999):
    time.sleep(i)
    p.stepSimulation()
    print(i)
p.disconnect()