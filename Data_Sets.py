import numpy
import matplotlib.pyplot as plt

# generates random dataset
print(numpy.random.uniform(0, 100, 20))

histogram_dataset = numpy.random.uniform(0, 10, 50)
plt.hist(histogram_dataset, 10)
plt.show()

