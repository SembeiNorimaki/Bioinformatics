def read_Codon2AA(filename):
    codon2aa = {}
    with open(filename) as f:
        for line in f:
            (key, val) = line.split(',')
            codon2aa[key] = val.rstrip('\n')
    return codon2aa