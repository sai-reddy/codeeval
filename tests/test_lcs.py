import unittest
from solutions.lcs import lcs

class LCSTest(unittest.TestCase):
    def test_lcs(self):
        seq1 = 'XMJYAUZ'
        seq2 = 'MZJAWXU'
        self.assertEqual(lcs(seq1, seq2), 'MJAU')

if __name__ == '__main__':
    unittest.main()
