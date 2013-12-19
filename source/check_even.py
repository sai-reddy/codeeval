import sys

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test.strip()
        # ignore test if it is an empty line
        if test:
            if int(test.strip()) % 2:
               print 0
            else:
                print 1
