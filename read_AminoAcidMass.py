def read_AminoAcidMass(filename):
    aa_mass = {}
    with open(filename, 'r') as f:
        for line in f:
            (key, val) = line.rstrip('\n').split(',')
            aa_mass[key] = int(val)
    return aa_mass