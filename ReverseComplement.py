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

def ReverseComplement(seq):
    r = []
    d = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
    for i in seq:
        r.insert(0, d[i])
    return ''.join(r)


# Change the function called by main to the desired one. 
def main(args):
    ReverseComplement(*args)


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
