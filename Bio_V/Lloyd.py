import numpy as np
import matplotlib.pyplot as plt
from sys import stdin

def Lloyd(data,k):
    # here we need a "copy" otherwise it's a pointer to data, so when we modify
    # centers, data will also be modified
    centers = np.copy(data[0:k,:])
    clusters = np.array([0]*data.shape[0])
    
    stop_condition = False
    while True:
        # centers to clusters
        distances = np.zeros((data.shape[0],k))
        for i in range(k):
            # we can skip sqrt
            distances[:,i] = np.sum(np.power(data - centers[i,:],2),1).T
        new_clusters = np.argmin(distances,1)
        
        if np.array_equal(new_clusters, clusters):
            break

        clusters = new_clusters  
        # clusters to centers        
        for i in range(k):
            filtered_data = data[clusters==i,:]
            centers[i,:] = np.sum(filtered_data,0) / filtered_data.shape[0]

    return centers


if __name__ == '__main__':
    first_line = stdin.readline().rstrip()
    if first_line == 'Input':
        k,m = map(int, stdin.readline().rstrip().split())
    else:
        k,m = map(int, first_line.split())

    data = []
    for line in stdin:
        if line.rstrip() == 'Output':
            break
        data.append(map(float,line.rstrip().split()))
    data = np.matrix(data)

    centers = Lloyd(data,k)
    for i in centers:
        print ' '.join(map(str, i))
