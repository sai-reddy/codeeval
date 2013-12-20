import sys
from string import maketrans


#    1) return should be lowercase
#    2) resturn should be in alphabetical character
#    3) should ignore all non ascii

def sanitize(text):
    sanitized_text = ''
    for char in text:
        if ord(char) in range(ord('a'), ord('z')+1) + range(ord('A'), ord('Z')+1):
            sanitized_text = sanitized_text + char
    intab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    outtab = 'abcdefghijklmnopqrstuvwxyz'
    transtab = maketrans(intab, outtab)
    return sanitized_text.translate(transtab)

def needed_for_panagram(input):
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    input_set = set(input)
    missing_set = alphabet_set - input_set
    if missing_set:
        return "".join(sorted(missing_set))
    else:
        return 'NULL'

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            test = sanitize(test)
            print needed_for_panagram(test)
