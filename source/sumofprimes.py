import sys
import time

def sum_primes(number):
    if number == 0:
        return 0
    if number == 1:
        return 1

    start_time = time.time()
    iter_list = []
    iter_list.append(0)
    iter_list.append(0)

    # Inititalize the list with all 1's
    for i in xrange(2, number+1):
        iter_list.append(1)

    position = 2
    while pow(position, 2) <= number and iter_list[position] == 1:
        j = pow(position, 2)
        while j < number:
            iter_list[j] = 0
            j = j + position
        position += 1
    iter_list[-1] = 0
    sum = 0
    count = 0
    for i, val in enumerate(iter_list):
        if val == 1:
            sum = sum + i
            count = count + 1
            print "Prime : {0}, Sum : {1}, prime count : {2}".format(i, sum, count)

    end_time = time.time()
    print "Total Time: {0}".format(end_time - start_time)

if __name__ == '__main__':
    sum_primes(3000)