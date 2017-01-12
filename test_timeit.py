# Method1: using count
def method1(seq):
    return [seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T')]

# method 2: using a loop
def method2(seq):
    r = [0, 0, 0, 0]
    for i in seq:
        if i == 'A':
            r[0] += 1
        elif i == 'C':
            r[1] += 1
        elif i == 'G':
            r[2] += 1
        else:
            r[3] += 1
    print r
    return r

# method 3: using Collections.counter
def method3(seq):
    counter = Counter(seq)
    return [counter['A'], counter['C'], counter['G'], counter['T']]


if __name__ == '__main__':
    import timeit
    from collections import Counter

    # Long dummy sequence
    long_seq = 'acagcatgca' * 10000000
    # Short dummy sequence
    short_seq = 'acagcatgca' * 1000

    # Test 1: Running a long sequence once
    print timeit.timeit("method1(long_seq)", setup='from __main__ import method1, long_seq', number=1)
    print timeit.timeit("method2(long_seq)", setup='from __main__ import method2, long_seq', number=1)
    print timeit.timeit("method3(long_seq)", setup='from __main__ import method3, long_seq', number=1)

    # Test2: Running a short sequence lots of times
    print timeit.timeit("method1(short_seq)", setup='from __main__ import method1, short_seq', number=10000)
    print timeit.timeit("method2(short_seq)", setup='from __main__ import method2, short_seq', number=10000)
    print timeit.timeit("method3(short_seq)", setup='from __main__ import method3, short_seq', number=10000)






































