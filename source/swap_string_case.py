import sys

def swap_case(data):
    transformed = ''
    for letter in data:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            transformed += chr(ord(letter) - 32)
        elif ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
            transformed += chr(ord(letter) + 32)
        else:
            transformed += letter
    print transformed

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        # ignore test if it is an empty line
        if not test:
            pass
        else:
            swap_case(test)
    test_cases.close()