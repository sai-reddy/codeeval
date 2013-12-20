import sys

def lcs(seq1, seq2):
    '''
    Uses two dimensional dynamic programming approach
    '''
    subproblems = [[0 for j in xrange(len(seq2) + 1)] for i in xrange(len(seq1) + 1)]
    for i, x in enumerate(seq1):
        for j, y in enumerate(seq2):
            if x == y:
                subproblems[i+1][j+1] = subproblems[i][j] + 1
            else:
                subproblems[i+1][j+1] = max(subproblems[i+1][j], subproblems[i][j+1])
   
    i=len(seq1)
    j=len(seq2)
    common_sequence = ''
    while i != 0 and j != 0:
        if subproblems[i][j] == subproblems[i-1][j]:
            i -= 1
        elif subproblems[i][j] == subproblems[i][j-1]:
            j -= 1
        elif seq1[i-1] == seq2[j-1]:
            common_sequence += seq1[i-1]
            i -= 1
            j -= 1
    common_sequence = common_sequence[::-1]
    return common_sequence

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip('\n'):
                seq1, seq2 = line.split(';')
                print lcs(seq1, seq2)
