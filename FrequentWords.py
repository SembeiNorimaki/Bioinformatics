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

# Guessing if handling the most freq words in a loop is more efficient than using iteritems
def FrequentWords(text, k):
    mydict = {}
    for i in range(len(text)-k+1):
        if seq[i:i+k] not in mydict.keys():
            mydict[seq[i:i+k]] = 1
        else:
            mydict[seq[i:i+k]] += 1
    return [k for k,v in mydict.iteritems() if v == max(mydict.values())]


# 1.11.6
# Faster algorithm that uses ComputingFrequencies and NumberToPattern functions.
# For large values of k this algorithm is unfeasible
def FasterFrequentWords(seq, k):
    freq_patterns = []
    freq = ComputingFrequencies(seq, k)
    max_count = max(freq)

    for i in range(4**k-1):  # check this -1
        if freq[i] == max_count:
            pattern = NumberToPattern(i, k)
            freq_patterns.append(pattern)
    return freq_patterns, max_count


# 1.2.10
# Inefficient Function that uses PatternCount
def FrequentWords_loop(text, k):
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


# Change the function called by main to the desired one. 
def main(args):
    FrequentWords(*args)


# from console, arguments must be passed inside a list formatted as string: 
# python template.py "['hello', 5, {'age': 30}, [1, 2, 3, 4]]"
if __name__ == '__main__':
    import sys, ast
    if len(sys.argv) == 2 and type(sys.argv[1]) is str:
        try:
            args = ast.literal_eval(sys.argv[1])
        except:
            print "ERROR evaluating input parameters"
            sys.exit()
        main(args)
    else:
        print "Incorrect argument syntax." 
        print "There must be only one argument formatted as string with double quotes"
        print "This string must contain a list with all parameters in the correct format"
        print "Exampe:"
        print "   python template.py \"['hello', 5, {'age': 30}, [1, 2, 3, 4]] \" "
