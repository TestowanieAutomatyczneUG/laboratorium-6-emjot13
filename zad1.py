import unittest


class hamming:
    def distance(genom1, genom2):
        if type(genom1) or type(genom2) != str or len(genom1) != len(genom2):
            raise ValueError("bad")
        genom1, genom2 = genom1.upper(), genom2.upper()
        diffs = 0
        for k in range(len(genom1)):
            if genom1[k] != genom2[k]:
                diffs += 1
        return diffs

class HammingTest(unittest.TestCase):


    def test_empty_strands(self):
        self.assertEqual(hamming.distance("", ""), 0)

    def test_single_letter_identical_strands(self):
        self.assertEqual(hamming.distance("A", "A"), 0)

    def test_single_letter_different_strands(self):
        self.assertEqual(hamming.distance("G", "T"), 1)

    def test_long_identical_strands(self):
        self.assertEqual(hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)

    def test_long_different_strands(self):
        self.assertEqual(hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("ATA", "AGTG")

    def test_disallow_left_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("", "G")

    def test_disallow_right_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("G", "")

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")