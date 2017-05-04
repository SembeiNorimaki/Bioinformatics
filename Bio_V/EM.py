import numpy as np


def read_file():
    filename = 'tests/EM.in3'
    with open(filename,'r') as fin:
        fin.readline()  # TODO: handle first line better
        k,m = map(int,fin.readline().rstrip().split())
        beta = float(fin.readline().rstrip())
        data = []
        for line in fin:
            if line.rstrip() == 'Output':
                break
            data.append(map(float,line.rstrip().split()))
    data = np.matrix(data)
    return k,m,beta,data


def em(k,m,beta,data):
    # k: number of clusters
    # m: dimensions of data (number of columns)
    # beta: stiffness parameter

    npoints = data.shape[0]
    # select the first k points from Data as the first centers
    centers = data[0:k,:]

    for aa in range(100):
        # E-step
        # Centers to Soft Clusters (E-step)
        # (Data, ?, Parameters) -> HiddenMatrix
        HiddenMatrix = np.zeros((npoints,k))
        for idx, data_i in enumerate(data):
            d = np.sqrt(np.sum(np.power(data_i-centers,2),1))
            d = np.exp(-beta*d)
            HiddenMatrix[idx,:] = np.array(d.T) / np.sum(d)

        # M-step
        # Soft Clusters to Centers (M-step)
        #(Data, HiddenMatrix, ?) -> Parameters
        centers = np.zeros((k,m))
        for i in range(HiddenMatrix.shape[1]):
            centers[i,:] = (HiddenMatrix[:,i] * data) / np.sum(HiddenMatrix[:,i])
            
    return centers
    

if __name__ == '__main__':    
    k,m,beta,data = read_file()
    centers = em(k,m,beta,data)
    for i in centers:
        print ' '.join(map(str, i))

