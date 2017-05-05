import numpy as np
from random import randint
from sys import stdin

#in1, in2 OK
def FarthestFirstTraversal(data, k):
    # take the first point as the first center and remove it from data
    #idx = randint(0,nsamples-1) 
    idx = 0
    centers = np.matrix(np.copy(data[idx,:]))
    data = np.delete(data,idx,0)     

    while centers.shape[0] < k:   
        distances = np.zeros((data.shape[0],centers.shape[0]))
        for idx, center_i in enumerate(centers):
            # distance from data to each center (npoints x ncenters matrix)
            # no need to use sqrt, since we only need the order od distances
            distances[:,idx] = np.array(np.sum(np.power(data - center_i, 2), 1).T)
        # for each point take the distance to the closest center (min),
        # then take the point with the biggest of this distances (max) 
        # and we add this point to the list of centers
        row = np.argmax(np.min(distances,1))
        centers = np.vstack((centers, data[row,:]))  
        #remove point so it's not used in further distance computations
        data = np.delete(data,row,0)     

    return centers
    



if __name__ == '__main__':
    first_line = stdin.readline().rstrip()
    if first_line == 'Input':
        # data starts in the second line
        k,d = map(int,stdin.readline().rstrip().split())
    else:
        # first line contains k and d
        k,d = map(int, first_line.split())
    # next lines contain data until Output is found
    data = []
    for line in stdin:
        if line.rstrip() == 'Output':
            break
        data.append(map(float,line.rstrip().split()))
    data = np.matrix(data)

    print FarthestFirstTraversal(data, k)
