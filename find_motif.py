def find_motif(seq, pattern):
	positions = []
	idx = -1
	while True:
		idx = seq.find(pattern, idx+1)
		if idx == -1:
			break
		else:
			positions.append(idx+1)  # +1 since seq start at position 1
	return positions

if __name__ == '__main__':
	r = find_motif('GATATATGCATATACTT', 'ATAT')
	print ' '.join(map(str,r))
