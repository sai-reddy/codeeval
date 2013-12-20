import sys
_subproblems = [1, 2, 1, 2, 1]

def min_coins(total):
    '''
    Uses single dimension dynamic programming approach
    '''
    if total <= len(_subproblems):
        # Already solved all the subproblems
        # Input is a positive integer so no need for negative check
        pass
    else:
        for i in xrange(len(_subproblems), total):
            _subproblems.append(min(_subproblems[i - 1], _subproblems[i - 3], _subproblems[i - 5]) + 1)

    return _subproblems[total - 1]

if __name__ == '__main__':
    test_cases = open(sys.argv[1])
    for test in test_cases:
        if test:
            print min_coins(int(test.strip()))

