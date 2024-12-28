import random
import numpy

test_scores = []

for i in range(100):
    test_scores.append(random.randint(0, 100))
    print(test_scores[i])

# sorts elements in alpha-numerical order
test_scores.sort()

# finds the 99th percentile (99.0%) value
percentile_scores_99th = numpy.percentile(test_scores, 99)
print(f"The 99th percentile is: {percentile_scores_99th}")