import numpy as np


def LCSBackTrack(v, w):
    s = np.zeros((len(v)+1,len(w)+1))
    backtrack = np.zeros((len(v)+1,len(w)+1))
    
    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            if v[i-1] == w[j-1]:
                s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1]+1)
            else:
                s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1])
    
            if s[i][j] == s[i-1][j]:
                backtrack[i][j] = 1
            elif s[i][j] == s[i][j-1]:
                backtrack[i][j] = 2
            elif s[i][j] == s[i-1][j-1] + 1 and v[i-1] == w[j-1]:
                backtrack[i][j] = 3    
    
    return(backtrack)


if __name__ == "__main__":
	LCSBackTrack('ATGTTATA', 'ATCGTCC')
                
    