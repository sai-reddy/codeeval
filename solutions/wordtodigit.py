import sys

_word_digit = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
    }

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        # ignore test if it is an empty line
        if not test:
            pass
        else:
            data = test.split(';')
            for wrd in data:
                sys.stdout.write(_word_digit.get(wrd.strip()))
        sys.stdout.write('\n')
    sys.stdout.flush()
    test_cases.close()