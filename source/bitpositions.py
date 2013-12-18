import sys

def cmp_bitpositions(number, pos1, pos2):
    if pos1 <= 0 or pos2 <= 0:
        return False
    elif pos1 == pos2:
        return True
    else:
        return (number & (1 << pos1-1)) != 0 ^ (number & (1 << pos2-1)) != 0

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        # ignore test if it is an empty line
        if not test:
            pass
        else:
            data = test.split(',')
            if cmp_bitpositions(int(data[0].strip()), int(data[1].strip()), int(data[2].strip())):
                print 'true'
            else:
                print 'false'
    test_cases.close()
