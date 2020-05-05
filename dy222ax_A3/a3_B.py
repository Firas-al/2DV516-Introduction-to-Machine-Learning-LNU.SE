import numpy as np
from sklearn.tree import DecisionTreeClassifier
import assignment_3_funcs as as3f
import matplotlib.pyplot as plt
import plt_functions as pltf

def load_data():
    print("load_data")
    data = np.loadtxt('./data/artificial.csv',delimiter=',')
    X = data[:, 0:-1]
    y = data[:, -1]
    return X, y


# Load Data
X, y = load_data()

# Params for Grid Search
dctparams = {"criterion":["gini", "entropy"],
             "splitter":["best","random"],
             "max_depth":[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
             "min_samples_split":[2,3,4,5,6,7,8,9,10,11,12,13,14],
             "min_samples_leaf":[1,2,3,4,5,6,7,8,9,10,11,12,13,14]}


#X, y, X_s, y_s = as3f.randomize_data(X, y, num_train=300)

#gscv = as3f.grid_search_SVC(X_s, y_s, DecisionTreeClassifier, 5, dctparams)
# optimal tree
#clf = DecisionTreeClassifier("gini","random",10,8,1).fit(X_s,y_s)

# Separate vectors
X1 = X[:,0]
X2 = X[:,1]

# Meshgrid
xx, yy = pltf.get_meshgrid(X1, X2,.1)

for i in [3, None]:
    clf = DecisionTreeClassifier(max_depth=i).fit(X,y)
    
    # plot boundary and data points
    fig = plt.figure()
    title = "Max Depth - " + str(i)
    ax = fig.add_subplot(1, 1, 1)
    fig.suptitle(title)
    pltf.add_countourf(ax, xx, yy, clf, colors='r',linewidths=0.5)
    ax.scatter(X[:,0], X[:,1], s=.5,c=y)
    plt.show()