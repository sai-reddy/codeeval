import sys
import time

def biggest_prime_palindrome(number):
    # Retrieving all primes below 1000
    iter_list = []
    iter_list.append(0)
    iter_list.append(0)
    # Inititalize the list with all 1's
    for i in xrange(2, number+1):
        iter_list.append(1)
    position = 2
    while pow(position, 2) <= number:
        if iter_list[position] == 0:
            position += 1
            continue
        j = pow(position, 2)
        while j < number:
            iter_list[j] = 0
            j = j + position
        position += 1
    iter_list[-1] = 0

    # Finding the largerst palindrome in given primes
    for i in xrange(len(iter_list) - 1, 0, -1):
        if iter_list[i] == 1:
            if ispalindrome(i):
                print i
                return 0

def ispalindrome(number):
    if number <= 0:
        return False

    div = 1
    while (number/div) >= 10:
        div *= 10
    while number != 0:
        l = number / div
        r = number % 10
        if l != r:
            return False
        number = (number % div) / 10
        div = div / 100
    return True

if __name__ == '__main__':
    sys.exit(biggest_prime_palindrome(1000))
