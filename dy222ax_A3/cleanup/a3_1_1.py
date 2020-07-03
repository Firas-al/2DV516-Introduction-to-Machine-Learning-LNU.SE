#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:14:35 2020

@author: derek
"""

import numpy as np
from sklearn.svm import SVC
import plt_functions as pltf
import assignment_3_funcs as as3f
import matplotlib.pyplot as plt

"""
def compute_gram_X(X, sigma = .01, degree = 2):
    print("X\n",X,"\n")
    # Get num rows
    rows = len(X)

    # Create a square matrix with all zeros. the diaganal will be all zeros because it is row minus the same row
    G = np.zeros((rows,rows))

    # Outer loop is from from zero to second to last row. This is because the last index will already be computed and filled in
    for x in range(rows-1):
        
        # Inner loop starts at the current outer index+1 and goes to the last row
        for y in range(x+1,rows):
            xrow = X[x,:]
            yrow = X[y,:]

            # Compute the x,y index of G using the formula
            G[x,y]= np.sum( np.exp( -sigma * (xrow-yrow) **2 )) ** degree

            # Set the corresponding y,x index to the same value. This is because (x-y)**2 is the same as (y-x)**2
            G[y,x]= G[x,y]
        
    return G"""

def compute_gram_X_Y(X, Y, sigma = .01, degree = 2):
    #print("X\n",X,"Y\n",Y,\n")
    # Get num rows
    n = len(X)
    m = len(Y)

    # Where X.shape = (n,p), and Y.shape = (m,p), create an (n,m) matrix G
        # Create a square matrix with all zeros. the diaganal will be all zeros because it is row minus the same row
    G = np.zeros((n,m))

    # Outer loop is from from zero to second to last row. This is because the last index will already be computed and filled in
    for i in range(n):
        
        # Inner loop starts at the current outer index+1 and goes to the last row
        for j in range(m):
            xrow = X[i,:]
            yrow = Y[j,:]
            # Compute the x,y index of G using the formula
            G[i,j]= np.sum( np.exp( -sigma * (xrow-yrow) **2 )) ** degree

    return G

def load_data():
    print("load_data")
    data = np.loadtxt('./data/mnistsub.csv',delimiter=',')
    X = data[:, 0:-1]
    y = data[:, -1]
    return X, y

def exercise_1_1_1():
    print("exercise1_1")
    X, y = load_data()
    X = as3f.normalize_mnist_data(X)
    X_train, y_train, X_test, y_test = as3f.randomize_and_split_data2(X, y)
   
    for c in [.1,1,10,100,1000,10000]:
        for sig in [.01,.1,1,10,100]:
            for deg in [1,2,3,4,5,6,7]:
                G_train = compute_gram_X_Y(X_train,X_train,sig,deg)
                clf = SVC(kernel="precomputed",C=c)
                clf.fit(G_train,y_train)

                G_test = compute_gram_X_Y(X_test,X_train)
                y_pred = clf.predict(G_test)

                print("C:",c,"Sig:",sig,"Deg:",deg)
                print("Acc:",np.sum(y_pred == y_test)/len(y_test))
    
def exercise_1_1_2():
    print("exercise1_1_2")
    X, y = load_data()
    X = as3f.normalize_mnist_data(X)
    X_train, y_train, X_test, y_test = as3f.randomize_and_split_data2(X, y)

    G_train = compute_gram_X_Y(X_train,X_train,0.01,3)
    clf = SVC(kernel="precomputed")
    clf.fit(G_train,y_train)
    G_test = compute_gram_X_Y(X_test,X_train)
    y_pred = clf.predict(G_test)
    

    for sig in [.001,.01,.1,1,10,100]:
        for deg in [1,2,3,4,5,6,7]:
            G_train = compute_gram_X_Y(X_train,X_train,sig,deg)
            clf = SVC(kernel="precomputed")
            clf.fit(G_train,y_train)

            G_test = compute_gram_X_Y(X_test,X_train)
            y_pred = clf.predict(G_test)

            print("Sig:",sig,"Deg:",deg)
            print("Acc:",np.sum(y_pred == y_test)/len(y_test))
    clf = gscv.best_estimator_
    
    # Separate vectors
    X1 = X_s[clf.support_, 0]
    X2 = X_s[clf.support_, 1]
    
    # Meshgrid
    xx, yy = pltf.get_meshgrid(X1, X2)
    
    # plot boundary and data points
    fig = plt.figure()
    title = "Ex 1, accuracy "+str(round(abs(gscv.best_score_),5))+" "
    for key in gscv.best_params_:
        title = title+key+":"+str(gscv.best_params_[key])+" "
    fig.suptitle(title)
    
    
    ax = fig.add_subplot(1, 1, 1)
    pltf.add_countour(ax, xx, yy, clf, colors='r',linewidths=0.5)
    ax.scatter(X_s[:,0], X_s[:,1], s=.5,c=y_s)
    plt.show()

    



exercise_1_1_1()



