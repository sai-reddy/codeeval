import sys

def print_matches(arr, sum):
    first = 0
    last = len(arr) - 1
    pairs = []
    while first < last:
        if arr[first] + arr[last] == sum:
            pairs.append((arr[first], arr[last]))
            first += 1
            last -= 1
        elif arr[first] + arr[last] < sum:
            first += 1
        else:
            last -= 1

    if len(pairs) > 0:
        print ';'.join([str(pair[0]) + ',' + str(pair[1]) for pair in pairs])
    else:
        print 'NULL'

if __name__ == '__main__':
     with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            test.strip()
            # ignore test if it is an empty line
            if not test:
                pass
            else:
                data, sum = test.split(';')
                print_matches([int(no) for no in data.split(',')], int(sum.strip()))
