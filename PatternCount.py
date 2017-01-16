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


# Change the function called by main to the desired one. 
def main(args):
    PatternCount(*args)


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
