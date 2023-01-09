import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")

#i = 0.5
#while i < 10:
#    pyrosim.Send_Cube(name="Box", pos=[0, 0, i], size=[(0.9**i)*1,(0.9**i)*1,(0.9**i)*1])
#    i = i + 1
for k in range(5):
    for j in range(5):
        i = 0.5
        while i < 10:
            pyrosim.Send_Cube(name="Box", pos=[0+j, 0+k, i], size=[(0.9**i)*1,(0.9**i)*1,(0.9**i)*1])
            i = i + 1


pyrosim.End()