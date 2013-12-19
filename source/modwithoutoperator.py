import sys

def modcal(a, b):
    if b > a:
        return a
    else:
        return (a - ( b * int(a / b)))

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        if test:
            a, b = test.strip().split(',')
            print modcal(int(a), int(b))
    test_cases.close()
