import numpy as np

def read_file():
    filename = 'EM.in1'
    with open(filename,'r') as fin:
        fin.readline()  #input
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

    # E-step
    # Centers to Soft Clusters (E-step)
    # (Data, ?, Parameters) -> HiddenMatrix
    for aa in range(100):
        HiddenMatrix = np.zeros((npoints,k))
        for idx, data_i in enumerate(data):
            d = np.sqrt(np.sum(np.power(data_i-centers,2),1))
            d = np.exp(-beta*d)
            HiddenMatrix[idx,:] = np.array(d.T) / np.sum(d)

        print HiddenMatrix
        # M-step
        # Soft Clusters to Centers (M-step)
        #(Data, HiddenMatrix, ?) -> Parameters
        centers = np.zeros((k,m))
        for i in range(HiddenMatrix.shape[1]):
            # is this operation * a dot product?
            centers[i,:] = HiddenMatrix[:,i] * data
    print centers
    

    
k,m,beta,data = read_file()
em(k,m,beta,data)

