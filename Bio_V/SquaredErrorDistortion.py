import numpy as np
from sys import stdin


def SquaredErrorDistortion(data, centers):
    distances = np.zeros((data.shape[0],centers.shape[0]))
    for idx, center_i in enumerate(centers):
        distances[:,idx] = np.array(np.sqrt(np.sum(np.power(data - center_i, 2), 1)).T)
    return np.sum(np.power(np.min(distances,1),2)) / distances.shape[0]


if __name__ == '__main__':
    first_line = stdin.readline().rstrip()
    if first_line == 'Input':
        # data starts in the second line
        k,d = map(int,stdin.readline().rstrip().split())
    else:
        # first line contains k and d
        k,d = map(int, first_line.split())

    # next k lines contain centers
    centers = []
    for i in range(k):
        centers.append(map(float,stdin.readline().rstrip().split()))
    centers = np.matrix(centers)

    # skip the separator line "----"
    stdin.readline()

    # next lines contain data until Output is found
    data = []
    for line in stdin:
        if line.rstrip() == 'Output':
            break
        data.append(map(float,line.rstrip().split()))
    data = np.matrix(data)

    print SquaredErrorDistortion(data, centers)

