import os
from hillclimber import HILL_CLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER
# for i in range(5):
    # os.system("python3 generate.py")
    # os.system("python3 simulate.py")
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
os.system("del fitness0.txt")
os.system("del fitness1.txt")
