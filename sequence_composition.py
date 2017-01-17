"""
Composition(TATGGGGTGC,3) = {ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG}
We don't have to return them in order
Sample Input:
	5
	CAATCCAAC
Sample Output:
	CAATC
	AATCC
	ATCCA
	TCCAA
	CCAAC
"""
def sequence_composition(seq, k):
	r = []
	for i in range(len(seq)-k+1):
		r.append(seq[i:i+k])
	return r

print sequence_composition('CAATCCAAC', 5)