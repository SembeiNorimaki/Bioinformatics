import numpy as np
import sys


def parse_input():
    n, m = map(int, sys.stdin.readline().rstrip('\n').split())
    down = np.array((n, m+1))
    right = np.array((n+1, m))
    
    line = []
    for i in range(n):
        line.append(list(map(int, sys.stdin.readline().rstrip('\n').split(' '))))
    down = np.asarray(line)

    _ = sys.stdin.readline()
    
    line = []
    for i in range(n+1):
        line.append(list(map(int,sys.stdin.readline().rstrip('\n').split(' '))))
    right = np.asarray(line)

    #print(down)
    #print(right)
    print(ManhattanTourist(n, m, down, right))


# Works
def ManhattanTourist(n, m, down, right):
    r = np.zeros((n+1,m+1))
    for i in range(1,n+1):
        r[i][0] = r[i-1][0] + down[i-1][0]
    for j in range(1,m+1):
        r[0][j] = r[0][j-1] + right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            r[i][j] = max(r[i-1][j]+down[i-1][j], r[i][j-1]+right[i][j-1])      
    return r[n][m]


if __name__ == "__main__":
    parse_input()
