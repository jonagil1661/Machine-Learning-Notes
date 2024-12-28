import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

from sklearn.datasets import load_iris
iris_dataset = load_iris()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

"""
Making a prediction for a new data point:
The algorithm finds a point in training set closest to new point 
and assigns the label of current training point to new data point
--------------------------------------------------------------------------------------
All machine learning models in scikit-learn have their own classes: Estimator classes. 

k-nearest neighbors classification algorithm is implemented in the KNeighborsClassifier 
class in the neighbors module. 

Before we can use the model, we need to instantiate the class into an object and set any parameters of the model. 
"""
from sklearn.neighbors import KNeighborsClassifier

# set number of neighbors to 1
knn = KNeighborsClassifier(n_neighbors=1)

# build model on training set
knn.fit(X_train, y_train)

"""
Make predictions with newly created model
"""
# put new data into numpy array
# sepal length = 5 cm, sepal width = 2.9 cm, petal length = 1 cm, petal width = 0.2 cm
X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape: {}\n".format(X_new.shape))

# make prediction using knn
prediction = knn.predict(X_new)
print("Prediction: {}".format(prediction))
print("Predicted target name: {}\n".format(iris_dataset['target_names'][prediction]))

"""
Evaluate The Model:
"""
# Use test data and make prediction for each iris and compare each to its label
y_prediction = knn.predict(X_test)
print("Test set predictions:\n {}".format(y_prediction))

# Compute the accuracy to test how well the model works (both work)
accuracy = np.mean(y_prediction == y_test)
accuracy = knn.score(X_test, y_test)
print("Test set score: {:.2f}\n".format(accuracy))

"""
Summary:

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

knn = KNeighborsClassifier(n_neighbors = 1)

knn.fit(X_train, y_train)

print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))
"""