def read_fasta(filename):
    fid = open(filename, 'r')
    lines = fid.readlines()
    fid.close()
    ids = []
    seqs = []
    ids.append(lines[0][1::].rstrip('\n'))
    seq = ''
    for i in range(1, len(lines)):
        line = lines[i].rstrip('\n')
        if line[0] == '>':
            seqs.append(seq)
            ids.append(line[1::])
            seq = ''
        else:
            seq += line
    seqs.append(seq)
    return ids, seqs


def read_fasta(filename):
    mydict = {}
    with open(filename) as f:
        id = None      # this has to be the special character I'm looking for
        seq = ''
        for line in f:
            if line[0] == '>':
                mydict[id] = seq             # save current id and seq
                id = line[1:].rstrip('\n')   # update id
            else:
                seq += line.rstrip('\n')