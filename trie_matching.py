import sys


def prefix_trie_matching(text, trie):
    current_node = 0
    reconstructed = ''
    for symbol in text
        if symbol in trie[current_node].keys():
            reconstructed += symbol
            current_node = trie[current][symbol]
            if current_node not in trie.keys():  # we reached a leaf
                # we are in a leaf, so one pattern in present in text
                #return reconstructed
                return True
        else:
            #return ''
            return False
    # we ran out of text before completing the path, so return False
    return False



def trie_matching(text, trie):
    indexes = []
    for i in range(len(text)):
        found = prefix_trie_matching(text[i:], trie)
        if found:
            indexes.append(i)



if __name__ == '__main__':
    #patterns = []
    #for line in sys.stdin:
    #    patterns.append(line.rstrip('\n'))
    #print(patterns)

    patterns = []
    line = sys.stdin.readline()
    while line:
        patterns.append(line.rstrip('\n'))
        line = sys.stdin.readline()
    print(patterns)
