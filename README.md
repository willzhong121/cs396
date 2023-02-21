# CS396 - Assignment 7
This codebase was created for the CS396 course at Northwestern University. It creates a random 3D lizard-like creature that wiggles around in an open environment. Most of the code was created by following Ludobots, an online course found at https://www.reddit.com/r/ludobots/. Ludobots makes use of the PyroSim modeling interface; the repository can be found at https://github.com/jbongard/pyrosim.git.

**Instructions**

Simply run the "search.py" file to run the simulation and see a random 3D creature appear!

**Video**

https://www.youtube.com/watch?v=paAGQGJgr74

**Diagram and Explanation**

<img src="diagram.PNG"  width="60%" height="30%">

To create a lizard-like creature, the code starts by defining a main link that serves as the torso. This torso is centered at (0, 0, 3), with the 3 units in the z-axis being added to account for the creature potentially dipping into negative z-space. The torso is generated with a random size with bounds for dimensions so that it is neither too large or too small.

After the torso is created, the code determines how many limb links are to be made. This is decided randomly, and a creature can have anywhere from one to four limbs (e.g. a single-limbed lizard or a regular four-limbed lizard). Once the number of limb links are decided, the code creates joints at random locations along the sides of the torso within specific parameters (see diagram for specific ranges). The links are then positioned relative to the joints (see diagram) and the physical creature construction is complete.

Sensor placement is determined by 50% probability. All of the links are compiled into a dictionary and the code iterates through each link to determine whether or not it will have a sensor. If so, the code turns the color of the link green. If not, the link is colored blue.
