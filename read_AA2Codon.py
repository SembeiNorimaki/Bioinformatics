def read_AA2Codon(filename):
    aa2codon = {}
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n').split(',')
            key = line[0]
            val = line[1:]
            aa2codon[key] = val
    return aa2codon