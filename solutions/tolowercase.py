import sys
from string import maketrans

def to_lower(data):
    intab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    outtab = 'abcdefghijklmnopqrstuvwxyz'

    return data.translate(maketrans(intab, outtab))

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test.strip()
        # ignore test if it is an empty line
        if not test:
            pass
        else:
            print to_lower(test)
    test_cases.close()