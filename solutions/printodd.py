import sys

def printodd():
    print 1
    for no in xrange(2, 100):
        if no % 2:
            print no
    return 0

if __name__ == '__main__':
    sys.exit(printodd())