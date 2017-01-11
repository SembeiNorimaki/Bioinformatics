__author__ = 'ialonso'
__email__ = 'alonso.isaac@gmail.com'


# check if it works
def saveFile(r, filename, spacer):
    with open(filename, 'w') as outfile:
        outfile.write(spacer.join(r))   


def PatternCount(text, pattern):
    """
    Exercice 1.2.7 PatternCount
    Description: Counts the number of times Pattern happens in Text WITH OVERLAPS
        Input: Strings Text and Pattern.
        Output: Count(Text, Pattern).

    Sample Input:
        GCGCG
        GCG
    Sample Output:
        2
    """

    n = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            n += 1
    return n


def FrequentWords(text, k):
    """
    Exercice 1.2.10 FrequentWords
    Description: Given a sequence and an integer k, outputs the most frequent k-mers.
        Input: A string text and an integer k.
        Output: All most frequent k-mers in text.

    Sample Input:
        ACGTTGCATGTCGCATGATGCATGAGAGCT
        4
    Sample Output:
        CATG GCAT
    """

    count = []
    freqPatterns = []
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        count.append(PatternCount(text, pattern))
    maxCount = max(count)
    for i in range(len(text)-k+1):
        if count[i] == maxCount and text[i:i+k] not in freqPatterns:
            freqPatterns.append(text[i:i+k]) 
    return freqPatterns, maxCount



def reverse_complement(seq):
    """
    Exercice 1.3.2 ReverseComplement
    Description: Reverse complement a nucleotide pattern.
         Input: A DNA string seq.
         Output: the reverse complement of seq
         
    Sample Input:
         AAAACCCGGT

    Sample Output:
         ACCGGGTTTT
    """

    r = []
    d = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
    for i in seq:
        r.insert(0, d[i])
    return ''.join(r)


# TODO: DEBUG IT WITH DEBUG DATASETS
def Pattern_Matching(Pattern, Seq):
    """    
    Exercice 1.3.5 Pattern Matching.
    Description: Find all occurrences of a pattern in a string.
         Input: Two strings, Pattern and Seq.
         Output: All starting positions where Pattern appears as a substring of Seq.
          
    Sample Input:
         ATAT
         GATATATGCATATACTT
     
    Sample Output:
         1 3 9     
    """

    R = []
    idx = -1
    while True:
        idx = Seq.find(Pattern,idx+1)
        if idx == -1: 
            break
        else: 
            R.append(idx)
    return R


'''
1.4.5 Clump finding
Do the efficient one in 1.14 and then solve 1.4.6
'''
def ClumpFinding(seq, k, l, t):
    valid_kmers = []
    for i in range(len(seq)-l+1):
        window = seq[i:i+l]
        #freqPatterns, maxCount = FrequentWords(window, k)
        freqPatterns, maxCount = FasterFrequentWords(window, k)
        if maxCount >= t:
            for j in freqPatterns:
                if j not in valid_kmers:
                    valid_kmers.append(j)
    return valid_kmers


# TODO: Finish it
def BetterClumpFinding(seq, k, l, t):
    window = seq[0:l]
    freqPatterns, maxCount = FasterFrequentWords(window, k)
    for j in freqPatterns:
        if j not in valid_kmers:
            valid_kmers.append(j)
    for i in range(1, len(seq)-l+1):
        pass


# 1.7.4 SkewDiagram  (num G - num C)
def SkewDiagram(seq):
    diagram = [0]*(len(seq)+1)
    for i in range(0,len(seq)):
        if seq[i] == 'G':
            diagram[i+1] = diagram[i] + 1
        elif seq[i] == 'C':
            diagram[i+1] = diagram[i] - 1
        else:s
            diagram[i+1] = diagram[i]
    print diagram


# 1.7.6 Min Skew
def minSkew(seq):
    skew = 0
    minSkew = 0
    minIndexes = []
    for i in range(0,len(seq)):

        if seq[i] == 'G':

            skew += 1


        elif seq[i] == 'C':
            skew -= 1
        if skew == minSkew:
            minIndexes.append(i)
        elif skew < minSkew:
            minIndexes = []
            minIndexes.append(i)
            minSkew = skew
    return minIndexes


# 1.8.3 Hamming
def hamming(seq1, seq2):
    r = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            r += 1
    return r


# 1.8.4 ApproxPatternMatching
def ApproxPatternMatching(pattern, seq, d):
    r = []
    for i in range(len(seq)-len(pattern)+1):
        subseq = seq[i:i+len(pattern)]
        if hamming(subseq, pattern) <= d:
            r.append(i)
    return r


# 1.8.6 ApproxPatternCount
def ApproximatePatternCount(pattern, seq, d):
    return len(ApproxPatternMatching(pattern, seq, d))


# 1.8.7 FreqWordsMismatch

# 1.8.8 FreqWordsMismatch and ReverseComplements

# 1.10.2 Find DNAa in Salmonella enterica


# Converts a DNA symbol ('A','C','G','T') to a number (0,1,2,3) respectively
def SymbolToNum(sym):
    dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return dict[sym]


# Converts a number (0,1,2,3) to a DNA symbol ('A','C','G','T') respectively
def NumToSymbol(num):
    dict = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    return dict[num]


# 1.11.2
# in 1.12.2 they propose a different method using recursion, however this approach is more efficient
def PatternToNumber(seq):
    dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    num_seq = [SymbolToNum(i) for i in seq]
    pow_seq = [4**i for i in range(len(seq)-1,-1,-1)]
    return sum([x * y for x, y in zip(num_seq, pow_seq)])
    
# exercice 1.11.3 (also 1.12.4)
# doesnt work. how do I accumulate in preffix_pattern?
# better do it with loops
def NumberToPattern(index, k):
    prefix_pattern = []
    if k == 1:
        return NumToSymbol(index)
    prefixIndex = index / 4  # this is an integer division
    prefix, r = divmod(index, 4)
    symbol = NumToSymbol(r)
    prefix_pattern = NumberToPattern(prefixIndex, k-1)
    return prefix_pattern


# check debug datasets 1.11.5
# example and extra dataset OK
def ComputingFrequencies(seq, k):
    freq = [0]*4**k      # initialize a 4^k list of zeros
    for i in range(len(seq)-k+1):
        freq[PatternToNumber(seq[i:i+k])] += 1
    return freq


# 1.11.6
# check with debug datasets from the normal FreqWords
def FasterFrequentWords(seq, k):
    freq_patterns = []
    freq = ComputingFrequencies(seq, k)
    max_count = max(freq)

    for i in range(4**k-1):  # check this -1
        if freq[i] == max_count:
            pattern = NumberToPattern(i, k)
            freq_patterns.append(pattern)
    return freq_patterns, max_count

# do the frequentwordsbysorting 1.13.2

# 1.14.1 ClumpFind
# 1.14.4 BetterClumpFinding

# 1.16.1 Neighbors
# it returns pattern itself, which according to exercixe is OK but is it really OK?
def ImmediateNeighbors(pattern):
    r = []
    for i in range(len(pattern)):
        for j in ['A', 'C', 'G', 'T']:
            newpattern = pattern[0:i] + j + pattern[i+1:len(pattern)]
            if newpattern not in r:
                r.append(newpattern)
    return r


# exercice OK
# 1.16.5
def IterativeNeighbors(pattern, d):
    neighborhood = [pattern]
    for i in range(0, d):   # 1 to d
        print 'i: ' + str(i)
        neighborhood2 = []
        for j in neighborhood:
            immediate = ImmediateNeighbors(j)
            for k in immediate:
                if k not in neighborhood2:
                    neighborhood2.append(k)
        neighborhood = neighborhood2
    return neighborhood

# 1.15.2 FreqWordsMismatch

# etc... until 1.23




##########################################################
# Test

def main():

    print PatternCount('GTGTCGGATGTCGGATCGGCGTCGGATGTCGGATAGTCGGATCTCGGGTCGGATGTCGGATAGCTATAAAGGTCGGATCCGTTTCGTCGGATGTCGGATTGCGTCGGATGTCGGATCGCGTCGGATTACGGTCGGATAGGGTCGGATGTCGGATCGTCGGATGTCGGATGTCGGATCGTCGGATGGTCGGATTGTCGGATGGTCGGATCGTCGGATTGTCGGATTTGAGTCGGATGTCGGATGTCGGATAGTCGGATCATTGGTCGGATGGTCGGATGTGTCGGATACAGTCGGATCGGTGGGTCGGATTGTCGGATGTCGGATTGTCGGATGTCGGATATGGCAAGTGTCGGATGAAGCTAGGTCGGATGTCGAGTCGGATCGTCGGATAGAGGCGTCGGATGTCGGATGTCGGATACGACCAGGAGGTCGGATGTCGGATGTAGTCGGATAAGGTCGGATGGTTACTGCGTCGGATAAGGCTTTCCCATGTCGGATAGGTCTACGCGGGGAGGTCGGATGTCGGATGTCGGATGATCCTAACGTCGGATTGTCGGATGTCGGATCGTAGGTCGGATTGGCGGAAGTCGGATGAGTCGGATCGTCGGATCGTCGGATGTCGGATTGGTCGGATGTCGGATCTTCACGTCGGATACTAGAGTCGGATACTTGTCGGATGTAGTCGGATCGTCGGATACGGTCGGATGTCGGATCTGTCGGATGCGTCGGATCGTCGGATGTCGGATCACAAGTCGGATTCGACTGCGTGTCGGATGTCGGATGTCGGATTCAGATGTCGGATAATGTCGGATGTGAGGTCGGATGTCGGATGTCGGATGAGTCGGATTGTCGGATGATGTCGGATTGGGTCGGATGTATGTCGGATCGGCGTCGGATGGGTCGGATACGTCGGATGTCGGATGTCGGATAGTCGGATATGAGTCGGATTTCCGTAGGTCGGATTGTCGGATGGTCGGAT','GTCGGATGT')

    #print PatternToNumber('CTTCTCACGTACAACAAAATC') == 2161555804173
    #print PatternToNumber('AAGGTATTAGTGGGTC')

    #print NumberToPattern(45, 4)

    #print set(ComputingFrequencies('ACGCGGCTCTGAAA', 2)) == set([2, 1, 0, 0, 0, 0, 2, 2, 1, 2, 1, 0, 0, 1, 1, 0])
    #print set(ComputingFrequencies('ACTTCGCCTAAGTCATTTATCCCGTGGTACGACGCTCCCTTACAGTCTTATATCCCGGTATATACGCAGAAATGCCTACGTCCCCTCGTCCCACACACCAGGGAAGCTGAAATCGCTCATCTACTATGCGTGTACTTCCGGACGAAATCGTCGTCGGCTTCTGTCTGGCGCTGGAGATCCGGGCTTCTTGAGGGACACACCCATTATGACCGTTACAGGACTTACAACTACTCTGAGCAATGATGGTGCTCTGTAACGAACAAACGCACTCACCTCTGTTTCCTGTATGACATCCTCAAATGGATCGACCGTGATGTACTGAGCGAATAAGTGCGGATTACATTTATAGTCAGCTACATTTATTCGCCGCTCGGAGCAGAGTATAATGAATTTATACCACTTGTTAGACTCCTTCTCGCATTTAGCCCCTACCGCAAGTCGGAGCGTTGGGGTGCAATAGAGTTTTCAGTATCTACGTACCGTTAAGTCTCTCGCGTTCTTTCAGCAGGCATCAATATGTTGCTTGCTGTGGGGTCGGGTGGGGCGGAGAGCCAATAAAGTGCATCGGAATTGGCTGCCCTCCTACGAATCCGCAAGATGCGGTGATGCTACGTGATTATGACTACTAGCTTAGTCCC', 6)) == set([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    #print ComputingFrequencies('CGAGGCTGATGCAGAAACCTTGGGAGACATGTGCACTTGTTCAGAGAGACTCCCCCTAAGATGGGCTGAAGGTGCCTGAATCTCTATATAACCCACATCAGCTTCATCCATCTAGAGTGAGTATATAATTCCAGGGAGTTTAGTACCACGACGGGTCGTAGCGTTCGCGCATCTGAAGGTGATTGAGTTAGAGTTACATCCGAATGGATCGCCATTGGTCAGGCGTAACATAGGTTCAACCCCGGGTGGAAGGCGGCTTTTGCGGTCCATCGGAAGCCCACGATCGCCCATGACCGTACGCGTGCTCAACCTTTACAGCTCGACTGTCAAAGCTGGAGCACGTTACCATAAGTAATATGGAATTGCCCTCGTAGAGACGAGAACTTGGGTTGGTAGAGTAAGTTCGCAGTACAGGCCTGTTAACTCTAAGCAAAGTCCTGCCCCTTTCTCTAGCAGTCCCATGAGGTCGTGTTTGGGGTAAATGTGAGCAAGGATAGCTCCCGGTCTTTGGGTCCAGGTCACTGGGTCGGCGTAGAAACCAAACGTGATTTGCGATGAGGCCCGACTGACCATGAGACTGCCGAAAAGACCCAAAAGTTTTTTTGCCTGACAGCCGACATTTAAGCCGCCAAGGGATACCTAACCTGAAGTTGTAG', 6)
    #print ClumpFinding('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA', 5, 50, 4)

    #print ClumpFinding('GCGGTTATGCACCGTTCAAATTAGCAAACCACTAAGCGACGTAGTCTGGATTGATTTCTCCCTACCAGTGACCCAAGACGCGTTAGTGAGTTAAGTTCATATCCAGTACCTGCCGCCCTCTGTACTTGGGCGTCCGATTCGCATGCTTACTCAGGTGGAGGACACGATAATCTGATTAAACTGAGCTAAACCAGGTGGAACCAGAAACCAGGTGGGGAGTCTCGCTTCAAGCCGTTCTTGCGATCAAACCAGGTGGTCCATTATGAAACCAGGTGGCTAAACCAGGTGGTCCAGATCCTCGAATGATGTCGGTGCACATCAAAACCAGGTGGGGTGGTGGAACGTAAAACCAGGTGGCATAAACCAGGTGGGCCGGTTCGTAAACCAGGTGAAACCAGGTGGGGTGGAAACCAGGTGGGTTACAAATTACGTTGAGATGGCCCAAACCAGGTGGTGGGCTTCACCCATGTCAACAAACCACCCTATGGAACTAAACCAGGTGGAACCAGGTGGTGAAGGCTTATCCTCAGGAAAAACCAGGTGGAGGTGGTGAAATAAAACCAGGTGGACCAGGTGGATAACCCTCGCCTCGCTTCTCAACCGAGACCTGGATAAACCAGGTGGGGTGGTCCACCGATTTTTGAGACACTAGAAACCAGGTGGGCGGGGAAACCAGGTGGCAAACCAGGTGGGGTGGACGGAAACCAGGTGGATATGTCATAAAACCAAACCAGGTGGTGCACCCCCATGGTGTGTCTTATCCGTGCGTATAAACCAGGTGGTCGCACGGCTTCCACTTGCTGAGAATAGGCCCGCAGGGTCAGTGCCATGCCCTCCGTCACTCGATATGTGTTGTAAGAGTGGTTACCCCTTCATTGAAGTCGCCCACAGCCCCACCTGCATTGCTAGACTATCACCCTACAGTAGGCCTTTTCGCCTTCTTCAAGCAGCAATCTCTTATCCGCGGATGGGCGCGGCGAGCGTGGCGTCCCCGAACATTTTTACCTAACGTGTTTTGTTGGCCGCAAGCCTTCCCTCTAGTCCACCTCAGCCATTCAGCCTAGTAGCTTTCAAGCCGAGCCTTCCATATCTAATGGACCGTCCAGAATTTCACACGTTTCACAGGGCTGTGTTCGACCGCCCGTAATGCTGTTTCACAGGCGATCGCCTTGCGGTTTTTTCACAGATCGCAGCCGATGGACATGCCAACTCGATTTTCACAGAGTTTTTCACAGCGGTTTCACAGCACAGCAGTGATTGTTTCACAGCAATTTTCACTTTCACAGGGGCCCTTTTCACAGCTCAGGGCTCTTTTCACTTTCACAGTTTCACAGCGCTCCTTTCACAGAGCGGGGAAATTTAAGGGAACACTCAAGGGAACAAGGGAACACACAAAGGGAACACAACACAACACATAAGGGAACACTTTCACAGAACACAAAAGTCCGAAATCATCAGCGGCGAAGGGATTTCACAGACAGACACTTTCACAGCGCATTTCACAGATACGTACTTTCACAGGCGTACTTTCACAGACTTTCACAGAGGACAAGCTCAATTTTCACAGACAGGCTGGATAAATTTCACAGCGGTAAGGGTTTCACAGCACACATAAGGGAACACGAATTTCACAGCAGGGAACACCTCTACGAGTAATCTATTACTCTACCTACTGAAGGGAACACACCGAAGACCTACTATTACCTATTACTCTTAAAGGGAACACATTACAAGGGAACACACTCTCTCGTCATATCTCACCTCTCTATTACTCTTAAGGGAACACCTTCTCGATCAACCTATTACTCTATGGAGATAGAGATATTCCAGACATATGGAGATAACATGGAGATATGGAGATAATGGAGATGGAGATAGCTCTTATATTTATCCTATGGAGATATGATACTATTAATGGAGATAATTCTAATGGAGATATAATTACTCTAAGAGGATGGGATCTCGGGCTATTACTCTAATGGAGATAAGCACTATTACTCTAGGAAATGGAGATATGTCAATGGAGATATGTAATGGAGATAGAGGGAGATGGAGTCGCCATTTCATAATCGCCATTTCATAGTTCAGGAATCGCCATTTCCGCCATTTCTAAGATGGAGTCGCCATTTCTACGTATGGAGATAGGATCGCCATTTCATACGACCCGTTGGATATCGCCATTTCCTCGCCATTTCTGGTGACATTTCTCGCCATTTCATTTCTGGAGATAGATGGATCTCGCCATTTCATAGGAATCGCCATTTCCACGTAGGGGGGGCCACAATCCGTAGGTCGGAATTCAGACTCGCCATTTCCCATCGCCATTTCTTCACCTGTATGCCGATCCCTTCGCCATTTCTCATGGAGATAACTCTCTCTCGCCATTTCTCGCCATTTCCATTTCACTCTCATTCGCCATCGCCATTTCCATTCGCCATTTCATCGCCATTTCTTCAGGATAAGATATCGCCATTTCGACTCTCATTCGCATACTGACTCTCATTCTCATCTCGCCATTTCTCATCTGACTCTCATCCTGGGGGAAACTTGCGACTCTCATCACACTTCCGTCGACTCTCATACTGGCGGATAGCATAGGAGCCATTTAAAGACTCTCATTCTCATTCGAGACTCTCATTCAAATCCTACGAGGACTCTCATATAGACTCTCATATCATTACGAGGACTCTCATATACGAGCCATGCATGTGGCGACGACTCTCATCTACGAGCCATGCAAGCAGAATCTACGAGCGACTCTCATTACGAGCCATGTGACCGTACGAGCCATGCATGCATGCCATGCTGACTCTCATCGAGTACGAGCCATGGAAGTTCTTGTTGGTTCGTAGCCCAAGAGCTGAAGTTACGAGCCTACGAGCCATGAAGTTACTTTTACGAGCCATGAAGCTTACGATACGAGCCATGCGAGCCATGCATCCGCGCTACGAGCCATGTTCCAGTACGAGCCATGTTAGTTGCTGAAGTTAAGTTTGGCGCTGAAGTTTGTACGAGCCATGTGCCCGCTGAAGTTTGTTGTACGAGCCATGCATGCTGAAGTTAATGGCTGAAGTTAGCGTTTGCGGGCAGATCCTCATTCTACGATACGAGCCATGCCATGCAGCTGAAGTTAAGTTGGGTTACGAGCCATGCGAGCCATGTGAAGTACGAGCCATGCTGGCTGAAGTTGTTTGTGCTGCTGAAGTTGCTCTTGTCTCTAGCTGAAGTTGCCAACAGGGCTGAAGCTGAAGTTTAAGCTGAAGTTGCGAGCAGGCTGAAGTTATCGGATTGGGGCTGAAGTTCAACCTCCCGTCCCCCCACACTATATTCCCGTCCCCCCCCGCGCACGCGCCGTCTCCCGTCCCCCCTATCCCGTGCGCACGCGACGCGATCCCGTCCCCCCAGAGTGCGCGCACGCGTCCCCCTTCCCGTCCCCCTCTCCCGGGCGCACGCGTCGCTCAACATTTCCGCGCACGCGTCGCGCACGCGGGCGCACGCGGGTCCCGTCCCCCCCCCTCTTCGGCGCACGCGGAATTCCCGTCGCGCACGCGTCCCGTCCCGCGCACGCGTCGCGCACGCGACTGCCCTAACCAACAGTGCGCACGCGCCGGTAACCCGGTAACCCGGTAACCGCGCACGCGGGCGCACGCGCGTAACCCGCGCACGCGCCGCGCACGCGGCCCGGTTCCCGTCCCCCCCGGTAACCCGGTAACTCCCGTCCCCCGTAACCCGGTGCGCACGCGCCCGGCGCACGCGGAGCGCACGCGCCCCCCCCGGTAATAGCGCACGCGCCCGGGCGCACGCGCCCGGTAACCCGGTAACCCGGGCGCGCGCACGCGGCGGCGCACGCGGCGCACGCGGCGCACGCG',11,566,18)

    #minSkew('CATGGGCATCGGCCATACGCC')
    #minSkew('GAGCCACCGCGATA')
    
    #print hamming('GGGCCGTTGGT', 'GGACCGTTGAC')

    #print hamming('TATACTTTTCGCGACAAAGAGCAGTTCAGTTCAGTACCGAATAACGCTGTGGACCAAATGCGTGCTCCTGCGATAACATGATTAAAGAGCAACCTGTTTAAGTCTCCATTTCGATCGTGGAATAAGTTGATACGATTGGATATCCTTATAGGGTAGCCAGAGAGATCACATAACAGCTGACTGTCCGCCGGCGAGGGGTGACTCCCCTTAAGAGGTCCATGCGCGGCTGCGAATTGATTTTTTGTCAAGCCTCTCTACGTCATGACCCTCAGCAGGCGCCCCGCTTTCTTAGGGATGCGGAAGCTTATAGATATCCAGCGGGACCTCTCCTCGGGATTGATCGATGGCAGTACTATTGTACAGTTCGGTCCGTAATGCATTGCATCAATTAGAACCCTGGTGAGCCATCTAAGCTGCGGTCTGAAGAAGAGGGCCTCGATACGGCCCGTATAGGGGAGTCATCAGAGTCGCCACCTCTAGGCCCGCTATCCGTAACCTGCGGCCAGGAGTTTTGCGGGTAGAAAGAAGTGAGGGTGCACAACGACTCTTTATAAACATCGTCAGACTAAATGGGCGCACCATAATCTGAGACGGCCTTATCGCGAGACTACTCAGAGGCAAGTCATGGAATGGAGCCCGGCCATTTAATGATAAAGAGGTATACTTAGGCATTTAGACATCCATCAAGACGGCTAATCCGTTCCCGCGGAAATCCCACCGCTCCATACGATGGTACTAGCGTTTGACCACATTATACCCGCTAACACGAACTCCCGGGATCCTTGAGGGAGCCCTCATGGCAGTGCCATGTGCCGGAACGAAGTGTGCACAGAGTCCGGTGTAAAGTCTGATATCTGACAGGTCCTGCATCGGCCCACCCAGAGGCCATATACTATAGGACGCATGGCACAAGAGAGGACGCTATCCACACAGTATCCCCCGAGTGTAATCGGCCCCCACTTGCGGGAATTGAATGCTAGGCGCGAAGTTCGAGAAAAAAGAAATACTCCTTCCGCTCACTATTGAATACCGTGAGCGACGAAGCATACCCA','GACTTCTAATTTATCGAGGGGGATGGGCTGCCACACTACCCTAATGCCCATCGGTTGTGGAGGCATATATGGCGAGGCTAATTAACGATCCATCTTACTTCAAACGATGCCAGCGCCTCGCAGAGTAGCCGGGGCACCTTGTTCTTTTCGTGGTGGTACGTTGCATTAACGTGCTCACACCAGCTTACCTAGACAGAACCGGCGGTATCTTGAAAACTGCCCCTACATCCACGTCAGTGCACGTCTTGGTACCAAAATATATCCTCGATCTCAAATCACTATGCCGCAAGTCGCAAACTGCCACTCTAGGTAGCGGCGTCGCCGTTGATAGTAGCGAGAACAACAAATTGCAGCTATTTTCGAGACGCAGGTGCAGATTTTGGGTAGTTAACGAGCTCCCCTTACTCGCGCTGTCTCCACCTAGTGATATTGGCTACGCATTTCGTAAAACCGGGCTGGGTTCTACGCGCACGGAGTAGAACGCGCGATAGTATTTGTTCCGCGCAGATGTCTGAACATGTGGGTCCACGACAATATTAAGCGGGGATGGGGCAAACTATCGGATATTGCATGCGTCTATGTCTGGGGAGCCTTGTAATGAAGTGATCCTAATCGGATAGTCTGATTTCGCACTAACTAATCTAGCTACATATTGTTCCCTCATGTGGTCGGCTGAAGCATCTGATAGCTAAGTTACCCCCGCTAACACTATCCCAGGGATGAATTACCTCTGGAATCTTCCCATACAGCGGAGGAAGCACTGACACAGGCAGGTCTCAATGTAGTGAGAATAGTTTTAATAGTCGTCACTACCGCTAGTATCAGCTCGATACGGACGGAGGTTGCAGTTATGTTAACTTTAAAGTCGGCGTGGACTAAGATATCCGTAACCTCTTCCATGACAAATCATGGTCTTCCGACTAGAAGCCTCTGGGTACTTAGAGACGTAGATTCGTGGAGAAGCAAGCGTGTTCAAAGGCGCCCGTATGCCCCGCTGGACATCACATGCAATTCGATGAGGCGATACAAGGCGAGAGGTGATTCCATAGGGT')

    #print ApproxPatternMatching('ATTCTGGA','CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT',3)

    #print ApproximatePatternCount('AACAAGCTGATAAACATTTAAAGAG','AAAAA',2)

    #print ApproximatePatternCount('TAGATC','AACAAGCCCGACGTCCGTGACAATTCTCAGCAAGGTACGCGGCATTATTCACACCCCGGAGCGCACCGGACAAAGGTAAGGATACATTAACTTAGATGTTAGATCCGCTCGAACAAACTCAGTGTTTCAACAACACGAACTATCTCGTATATACTTTTATTGGGCGAATATGCTAACTAGATGGTGCCAACGGTTAGGTGGCGGTATATGCCATTCTGGCAAAGATTGACAGCATATGTTATACCAGTCTAGATAAGCACCATATCGAGACGCACTGTTTTTCCGTAGCCGTCCGCACGCTGTCTCCCCCTGTAATTAAGGAAAAGTCACGTTACATGGCAAATGCATATTGTCGACGACGACGTAGCTCCACCCTCAGGCACGTCCCGCGAGCCTCA',2)

    #print ImmediateNeighbors('AGA')

    #a = IterativeNeighbors('CTGGTGGT', 3)
    #print '\n'.join(a)

if __name__ == "__main__":
    main()