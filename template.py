'''
Template file that allows functions to be called from console.

'''

def myfunction(mystring, myint, mydict, mylist):
    # check that types are correct
    assert type(mystring) is str
    assert type(myint) is int
    assert type(mydict) is dict
    assert type(mylist) is list

    # print input parameters
    print mystring
    print myint 
    print mydict
    print mylist


# We could skip main and directly call the function from the root level.
def main(args):
    myfunction(*args)


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
