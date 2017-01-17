"""
Sample Input:
	4
	AAGATTCTCTAAGA
Sample Output:
	AAG -> AGA,AGA
	AGA -> GAT
	ATT -> TTC
	CTA -> TAA
	CTC -> TCT
	GAT -> ATT
	TAA -> AAG
	TCT -> CTA,CTC
	TTC -> TCT
"""
def DeBrujinFromSeq(seq, k):
	de_brujin = {}
	for i in range(len(seq)-k+1): 
		seq1 = seq[i:i+k-1]
		seq2 = seq[i+1:i+k]
		if seq1 not in de_brujin.keys():
			de_brujin[seq1] = [seq2]
		else:
			de_brujin[seq1].append(seq2)
	return de_brujin


print DeBrujinFromSeq('AAGATTCTCTAAGA',4)
