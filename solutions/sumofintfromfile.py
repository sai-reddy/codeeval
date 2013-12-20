import sys

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    sum = 0
    for test in test_cases:
        test.strip()
        # ignore test if it is an empty line
        if not test:
            pass
        else:
            sum += int(test)
    print sum
    test_cases.close()
