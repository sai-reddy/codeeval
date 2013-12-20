import sys

def closest_pair(xcoordinates, ycoordinates):
    '''
    Computes the closest pair using divide and conquer approach
    for set of points represented by their x and y coordinates
    '''
    

if __name__ == '__main__':
     with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            test.strip()
            # ignore test if it is an empty line
            if not test:
                pass
            else:
                