

import sys


# Eulerian path is like a cycle but two of the nodes have uncompensated num of inputs/outputs
def handle_input_output():
    # handle input
    graph = {}
    count_dict = {}
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            left, right = line.split(' -> ')
            right = right.split(',')
            if left in graph.keys():    # this shouldn't happen
                graph[left].append(right)  # not append
                count_dict[left] += len(right)
            else:
                graph[left] = right
                count_dict[left] = len(right)
                
        except:
            break       # EOF

    #print(graph)
    # Execute main function
    r = EulerianCycle(graph)    

    # handle output
    print('->'.join(r))


def EulerianPath(graph):
    stack = []
    location = None
    circuit = []

    # since it's an Eulerian Cycle we can start at any vertex
    location = list(graph)[0]

    # Repeat until the current vertex has no more out-going edges (neighbors) 
    # and the stack is empty.
    while len(graph[location]) > 0 or len(stack) > 0:
        if len(graph[location]) == 0:   # If current vertex has no out-going edges
            circuit.append(location)    # add it to circuit
            location = stack.pop()      # remove the last vertex from the stack and set it as the current one
        else:                           # otherwise
            stack.append(location)      # add the vertex to the stack
            location = graph[location].pop()            # take any of its neighbors
                                                        # remove the edge between that vertex and selected neighbor
                                                        # and set that neighbor as the current vertex
    
    # Here we must append the first element at the end to close the cycle
    # but since circuit is reversed, we append the last element at the beginning
    circuit.insert(0, circuit[-1])
    return circuit[::-1]   # return the reversed circuit


if __name__ == '__main__':
    handle_input_output()