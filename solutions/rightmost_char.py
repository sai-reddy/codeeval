import sys

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        # santizing
        test.strip()
        # ignore test if it is an empty line
        if not test:
            pass
        else:
            text, char = test.split(',')
            # sanitizing
            text = text.strip()
            char = char.strip()
            for i in xrange(len(text)-1, -1 , -1):
                if text[i] == char:
                    print i
                    break
            else:
                 print -1
    test_cases.close()
