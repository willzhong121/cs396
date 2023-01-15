import matplotlib.pyplot
import numpy

backLegSensorValues = numpy.load('backlegsensorvalues.npy')
frontLegSensorValues = numpy.load('frontlegsensorvalues.npy')
matplotlib.pyplot.plot(backLegSensorValues, label = 'Back Leg Sensor Values')
matplotlib.pyplot.plot(frontLegSensorValues, label = 'Front Leg Sensor Values')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
