import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

# import the iris dataset
from sklearn.datasets import load_iris

# call load_iris() function to to return a Bunch object
# which contains keys & values
iris_dataset = load_iris()

def glossary():
    print("0. Glossary")
    print("1. Dataset Characteristics")
    print("2. Keys of iris_dataset")
    print("3. Target Names")
    print("4. Feature Names")
    print("5. Data Array Type")
    print("6. Target Array Type")
    print("7. Shape of Data")
    print("8. Shape of Target")
    print("9. First 5 Samples")
    print("10. Encoded Species List")
    print("999. Terminate\n")
glossary()

"""
actual data is in target and data fields
contains measurements of flower in NumPy array
"""

# rows in data array are each flower, and cols are the 4 measurements

"""
- there are 150 flowers in this dataset
- each item is called a 'sample', and their properties are 'features'
- the shape of the data array = # of samples * # of features
"""

while True:
    x = input("Select an option: ")
    try:
        x = int(x)
        match x:
            case 0:
                glossary()
            case 1:
                # value of 'DESCR' is short description of dataset
                print(iris_dataset['DESCR'][:193] + "\n")
            case 2: 
                print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()) + "\n")
            case 3: 
                # value of target_names has species of flowers we want to predict
                print("Target names: {}".format(iris_dataset['target_names']) + "\n")
            case 4:     
                # value of feature_names has description of each feature
                print("Feature names: \n{}".format(iris_dataset['feature_names']) + "\n")
            case 5:
                # type of data of the data array
                print("Type of data: {}".format(type(iris_dataset['data'])) + "\n")
            case 6:
                # type of target of the target array
                print("Type of target: {}".format(type(iris_dataset['target'])) + "\n")     
            case 7:
                # shape of data
                print("Shape of data: {}".format(iris_dataset['data'].shape) + "\n")
            case 8:
                # shape of target (# of flowers)
                print("Shape of target: {}".format(iris_dataset['target'].shape) + "\n")
            case 9:
                # feature values for first 5 samples
                print("First five samples/rows of data:\n{}".format(iris_dataset['data'][:5]) + "\n")
            case 10:
                # species are encoded from 0-2 (setosa, versicolor, virginica)
                print("Target:\n{}".format(iris_dataset['target']) + "\n")
            case 999:
                break
            case _:
                print("ERROR: INPUT VALID NUMBER (0-10)\n")
    except ValueError:
        print("ERROR: INPUT VALID NUMBER (0-10)\n")
    

    
    