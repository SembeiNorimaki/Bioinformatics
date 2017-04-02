def trie_construction(patterns):
    trie = {0:{}}  # single node root
    n = 1
    for pattern in patterns:
        current_node = 0
        for i in pattern:
            # trick to avoid creating leafs as empty keys
            if current_node not in trie.keys():
                trie[current_node] = {}
            if i in trie[current_node].keys():
                current_node = trie[current_node][i]
            else:
                new_node = n
                trie[current_node][i] = new_node 
                current_node = new_node
                n += 1
    return trie

# read input file
if __name__ = '__main__':
    pass
