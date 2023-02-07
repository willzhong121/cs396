# Assignment 5: Instructions and Explanation
# Simply run the "search.py" file to run the simulation and see an evolved robot!
# These robots learn to evolve to break the wall of cubes that spawn in with them. At first, all they do is flail around. However, after the evolution process, the robots will usually learn to waddle to the wall of cubes and propel themselves into the wall. This results in a few cubes being knocked away.
#
# The fitness function displays the robot that had its torso (middle rectangular prism) in the furthest -x position out of all the robots created. In other words, the robot that traveled the furthest to the left in the x-axis was considered to be the most fit by the fitness function. This is because the wall of cubes was generated with an x-coordinate of -2, so I assumed that the robot that had the most succcess with destroying the wall would have traveled the furthest in the -x direction.
