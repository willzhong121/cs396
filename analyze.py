import numpy
import matplotlib.pyplot
import constants as c

array1 = numpy.load("file1.npy")
array2 = numpy.load("file2.npy")
array3 = numpy.load("file3.npy")
array4 = numpy.load("file4.npy")
array5 = numpy.load("file5.npy")

xArr = list(range(0, c.numberOfGenerations))
matplotlib.pyplot.plot(xArr, array1, color="red", label="Seed 1")
matplotlib.pyplot.plot(xArr, array2, color="blue", label="Seed 2")
matplotlib.pyplot.plot(xArr, array3, color="green", label="Seed 3")
matplotlib.pyplot.plot(xArr, array4, color="brown", label="Seed 4")
matplotlib.pyplot.plot(xArr, array5, color="purple", label="Seed 5")

matplotlib.pyplot.xlabel('Number of Generations', fontsize=10)
matplotlib.pyplot.title('Evolved Robots Fitness over 100 Generations', fontsize=10)
matplotlib.pyplot.ylabel('Fitness', fontsize=10)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
