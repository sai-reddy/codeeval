import sys
import array

def print_primes(number):
    iter_list = array.array('c')
    iter_list.append('0')
    iter_list.append('0')

    # Inititalize the list of length of argument plus 1 with all 1's for 1 based indexing
    for i in xrange(2, number+1):
        iter_list.append('1')

    # Mark all non-primes as 0
    position = 2
    while pow(position, 2) <= number:
        if iter_list[position] == 0:
            position = position + 1
            continue
        j = pow(position, 2)
        while j <= number:
            iter_list[j] = '0'
            j = j + position
        position = position + 1
    # The number itself is not a prime
    iter_list[-1] = '0'

    # Identify primes
    output = ''
    for i in xrange(len(iter_list)):
        if iter_list[i] == '1':
            output += str(i) + ','
    print output.rstrip(',')

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        # ignore test if it is an empty line
        if not test:
            pass
        else:
            print_primes(int(test.strip()))
    test_cases.close()