import numpy as np 

def LCSBackTrack(v, w):
    s = np.zeros((len(v),len(w)))
    backtrack = np.zeros((len(v),len(w)))
    
    print s
    for i in range(len(v)):
        s[i][0] = 0
    for j in range(len(w)):
        s[0][j] = 0
    for i in range(1,len(v)):
        for j in range(1,len(w)):
            if v[i] == w[j]:
                s[i][j] = max(s[i-1][j],s[i][j-1],s[i-1][j-1]+1)
            else:
                s[i][j] = max(s[i-1][j],s[i][j-1],s[i-1][j-1])

            if s[i][j] == s[i-1][j]:
                backtrack[i][j] = 1     # down = 1
            elif s[i][j] == s[i][j-1]:
                backtrack[i][j] = 2     # right = 2
            elif s[i][j] == s[i-1][j-1] + 1 and v[i] == w[j]:
                backtrack[i][j] = 3     # down_right = 3

    return s
    

v='ATCGTCC'
w='ATGTTATA'

print(LCSBackTrack(v, w))