import numpy
from scipy import stats
import random


gpa = []

# load gpa values into gpa array
for i in range(200): 
    global x 
    x = random.randrange(0, 101)
    gpa.append(x)

# calculate mean of GPA
meanOfGpa = numpy.mean(gpa)
print(f"The mean is: {meanOfGpa}")

# calculate median of GPA
medianOfGpa = numpy.median(gpa)
print(f"The median is: {medianOfGpa}")

# calculate mode of GPA
modeOfGpa = stats.mode(gpa)
print(f"The mode is: {modeOfGpa}")

# calculate standard deviation of GPA
standardDeviationOfGpa = numpy.std(gpa)
# rounds to 2nd decimal place
standardDeviationOfGpa = round(standardDeviationOfGpa, 2)
print(f"The standard deviation is: {standardDeviationOfGpa}")

# calculate variance of GPA
varianceOfGpa = numpy.var(gpa)
print(f"The variance is: {varianceOfGpa}")
# variance is same as standard deviation squared
varianceOfGpa = pow(standardDeviationOfGpa, 2) 
print(f"The variance is: {varianceOfGpa}")

