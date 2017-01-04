__author__ = 'ialonso'
__email__ = 'alonso.isaac@gmail.com'



# check if it works
def saveFile(r, filename, spacer):
	with open(filename, 'w') as outfile:
		outfile.write(spacer.join(r))	



'''
Frequent Words Problem: Find the most frequent k-mers in a string.
     Input: A string Text and an integer k.
     Output: All most frequent k-mers in Text.

Sample Input:
     ACGTTGCATGTCGCATGATGCATGAGAGCT
     4

Sample Output:
     CATG GCAT
'''
def freq_words(Seq, k):
	MaxCount = 1
	R = []
	for i in range(0,len(Seq)-k+1):
		A = Seq[i:i+k]
		count = Seq.count(A)	
		if count == MaxCount and A not in R:
			R.append(A)
		elif count > MaxCount:
			R = []
			MaxCount = count
			R.append(A)
	return R


'''
Reverse Complement Problem: Reverse complement a nucleotide pattern.
     Input: A DNA string Pattern.
     Output: Pattern, the reverse complement of Pattern.
     
Sample Input:
     AAAACCCGGT

Sample Output:
     ACCGGGTTTT

'''
def reverse_complement(seq):
    r = []
    d = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
    for i in seq:
        r.insert(0, d[i])
    return ''.join(r)