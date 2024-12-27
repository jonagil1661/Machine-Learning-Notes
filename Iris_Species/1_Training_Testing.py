import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

from sklearn.datasets import load_iris
iris_dataset = load_iris()

from sklearn.model_selection import train_test_split
"""
The labeled data will be split into two parts:
1. Training Data: Used to build the machine learning model
2. Test Data:     Used to assess how well the model works
-----------------------------------------------------------
train_test_split() function from scikit-learn 
- Extracts 75% of rows in the data as the training set
- The remaining 25% of the data is the test set
-----------------------------------------------------------
train_test_split() shuffles dataset first
"""

# assign outputs
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

# contains 75% of dataset
print("X_train shape: {}".format(X_train.shape))
# contains 25% of dataset
print("X_test shape: {}".format(X_test.shape) + "\n")


# create dataframe from data in X_train
# label the columns using the strings in iris_dataset.feature_names
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

"""
- create a scatter matrix from the dataframe, color by y_train
- diagonal includes histograms of each feature
- separation of the 3 classes indicates that a machine learning model has 
  a high change of successfully learning to separate them
"""
#from pandas.plotting import scatter_matrix
x = input("Visualize Data? (y): ")
match x:
    case "y":
        pd.plotting.scatter_matrix(iris_dataframe, 
                                c=y_train, 
                                figsize=(15, 15), 
                                marker='o', 
                                hist_kwds={'bins': 20}, 
                                s=60, 
                                alpha=.8, 
                                cmap=mglearn.cm3)
        plt.show()
    case _:
        print("Okay boomer.")


