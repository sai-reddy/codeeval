import sys

def modcal(a, b):
    if b > a:
        return a
    else:
        return (a - ( b * int(a / b)))

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test.strip()
        # ignore test if it is an empty line
        if not test:
            pass
        else:
            a, b = test.split(',')
            print modcal(int(a), int(b))
    test_cases.close()