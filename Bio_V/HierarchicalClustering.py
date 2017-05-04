import numpy as np
from sys import stdin, stdout, argv


# given a tree and a node, it returns all the descendant leaves from this node.
def get_leaves(tree, node):
    # if node is already a leaf, return it
    if node not in tree.keys():
        return [node]
    # otherwise explore the tree to get all leaves from the node
    open_list = tree[node]
    idx = 0
    while idx < len(open_list):
        if open_list[idx] in tree.keys():      # not a leaf
            open_list.extend(tree[open_list[idx]])
            del open_list[idx]
        else:
            idx += 1

    return open_list


# this function creates an hierarchical clustering tree.
# Starts with each point as a leaf and at each step joins the two closest points
# into a parent weighted average point
def HierarchicalClustering(data, n):
    next_node = n
    tree = {}
    # tracks the node of each column in matrix
    data_header = range(n)
    # weights for averaging (number of leaves of each node)
    weights = [1]*n

    while len(data_header) > 1:
        # get the two closest nodes (row and col)
        # think a better way to avoid setting diagonals to Inf and back to 0
        np.fill_diagonal(data, float('inf'))  # fill diagonal with Inf
        idx = np.argmin(data)
        np.fill_diagonal(data, 0.0) # put the diagonals back to 0
        row, col =  np.unravel_index(idx, data.shape)
        
        #create a parent node in the tree
        tree[next_node] = [data_header[row], data_header[col]]

        # we can use min or weighted average
        #new_node = np.min((data[:,row],data[:,col]),0)
        
        new_node = 1.0 * (data[:,row]*weights[row] + data[:,col]*weights[col]) \
                   / (weights[row] + weights[col])
        
        # update the node row  
        data[:,row] = new_node
        data[row,:] = new_node.T
        data_header[row] = next_node
        weights[row] += weights[col]
        next_node += 1
        
        # delete the node col
        data = np.delete(data, col, 0)  # delete row
        data = np.delete(data, col, 1)  # delete column
        del data_header[col]
        del weights[col]

    return tree

def read_input(filein):
    with open(filein, 'r') as fin:
        # handle first line
        first_line = fin.readline().rstrip()
        if first_line == 'Input':
            n = int(fin.readline().rstrip())
        else:
            n = int(first_line)

        data = []
        for line in fin:
            if line.rstrip() == 'Output':
                break
            data.append(map(float,line.rstrip().split()))
        data = np.matrix(data)
    return n, data
    print data


# expects a list of lists.
# first list will b separated by \n, second list separated by spaces
def write_output(data_out, fileout):
    with open(fileout, 'w') as fout:
        for i in data_out:
            fout.write(' '.join(map(str,i)) + '\n')


if __name__ == '__main__':
    # handle input
    if len(argv) != 2:
        print "Error, incorrect number of arguments"
        quit()

    fileout = argv[1] + '.out'

    n, data = read_input(argv[1])
    tree = HierarchicalClustering(data, n)
    
    data_out = []
    for i in range(n, np.max(tree.keys())+1):
        leaves = get_leaves(tree, i)
        leaves = [x+1 for x in leaves]  # start numerating at 1
        data_out.append(leaves)

    write_output(data_out, fileout)
