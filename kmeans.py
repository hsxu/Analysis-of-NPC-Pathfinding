import numpy as np
from sklearn.cluster import KMeans

x_vals = []
y_vals = []

f = open('text.txt')
for line in f:
    if line == "" or line == '\n':
        continue

    k = line.split(',')
    x_vals.append(int(k[1]))
    y_vals.append(int(k[0]))

f1 = x_vals
f2 = y_vals

X=np.matrix(zip(f1,f2))
kmeans = KMeans(n_clusters=4).fit(X)
print kmeans.cluster_centers_