import matplotlib.pyplot
import numpy

backLegSensorValues = numpy.load('backlegsensorvalues.npy')
frontLegSensorValues = numpy.load('frontlegsensorvalues.npy')

backLegAngles = numpy.load('backlegangles.npy')
frontLegAngles = numpy.load('frontlegangles.npy')
# matplotlib.pyplot.plot(backLegSensorValues, label = 'Back Leg Sensor Values')
# matplotlib.pyplot.plot(frontLegSensorValues, label = 'Front Leg Sensor Values')

matplotlib.pyplot.plot(backLegAngles, label = 'Back Leg Angles')
matplotlib.pyplot.plot(frontLegAngles, label = 'Front Leg Angles')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
