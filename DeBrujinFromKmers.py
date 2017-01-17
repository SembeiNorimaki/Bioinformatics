""" Given a list of kmers, contruct the DeBrujin graph
Sample Input:
	GAGG
	CAGG
	GGGG
	GGGA
	CAGG
	AGGG
	GGAG
Sample Output:
	AGG -> GGG
	CAG -> AGG,AGG
	GAG -> AGG
	GGA -> GAG
	GGG -> GGA,GGG
"""

def DeBrujinFromKmers(kmers):
	de_brujin = {}
	for kmer in kmers:
		prefix = kmer[:-1]
		suffix = kmer[1:]
		if prefix not in de_brujin.keys():
			de_brujin[prefix] = [suffix]
		else:
			de_brujin[prefix].append(suffix)
	return de_brujin


print DeBrujinFromKmers(['GAGG','CAGG','GGGG','GGGA','CAGG','AGGG','GGAG'])


