#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:44:23 2020

@author: derek
"""

import numpy as np
import matplotlib.pyplot as plt
import assignment2_logistic_regression_functions as lorf
import assignment2_matrix_functions as amf
from matplotlib.colors import ListedColormap

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


def load_data():
    # import data
    data = np.loadtxt("./A2_datasets_2020/microchips.csv",delimiter=',') # load csv
    X = data[:,0:2]
    y = data[:,-1]
    return X,y
    

def exercise5_1():
    print ("\nExercise 5.1")
    
# load data
X, y = load_data()

# Separate vectors
X1 = X[:,0]
X2 = X[:,1]

# Create extended matrix of degree 9
degree = 4
Xe = amf.mapFeature(X1,X2,degree,ones=False) # No 1-column!

# Create LogisticRegression object and fit it with our data
logreg = LogisticRegression(C=1.0, tol=1e-6,max_iter=10000)
logreg.fit(Xe,y) # fit the model with data


# Create meshgrid
h=.01
x_min, x_max = X1.min()-0.1, X1.max()+0.1
y_min, y_max = X2.min()-0.1, X2.max()+0.1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h)) # Mesh Grid 
x1,x2 = xx.ravel(), yy.ravel() # Turn to two Nx1 arrays

XXe = amf.mapFeature(x1,x2,degree,False)

y_pred=logreg.predict(XXe) # predict
errors = np.sum(y_pred!=y) # compare y with y_pred
print("Training errors:", errors)

classes = y_pred>0.5 # round off probabilities
clz_mesh = classes.reshape(xx.shape) # return to mesh format

cmap_light = ListedColormap(["#FFAAAA", "#AAFFAA", "#AAAAFF"]) # mesh plot  
cmap_bold = ListedColormap(["#FF0000", "#00FF00", "#0000FF"]) # colors

 # Create 1x2 plot
fig, ax = plt.subplots(1,1)
fig.suptitle('Ex 4.2', fontsize=14)
fig.tight_layout(pad=2.0,rect=[0, 0.03, 1, 0.95])

# Plot the costs on the first figure
ax.pcolormesh(xx, yy, clz_mesh, cmap=cmap_light) 
ax.scatter(X1,X2,c=y, marker=".", cmap=cmap_bold) 
ax.set_title("Training errors ="+str(errors))
plt.show()







