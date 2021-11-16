import unittest


class RomanNumeralsTest(unittest.TestCase):
    def roman(self, num):
        convert_table = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"],
                         [40, "XL"],
                         [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        res = ""
        if num == 0:
            raise ValueError("Romans did not use number 0")
        for value, text in convert_table:
            freq = num // value
            num = num % value
            res += text * freq

        return res

    def test_1_is_a_single_i(self):
        self.assertEqual(self.roman(1), "I")

    def test_2_is_two_i_s(self):
        self.assertEqual(self.roman(2), "II")

    def test_3_is_three_i_s(self):
        self.assertEqual(self.roman(3), "III")

    def test_4_being_5_1_is_iv(self):
        self.assertEqual(self.roman(4), "IV")

    def test_5_is_a_single_v(self):
        self.assertEqual(self.roman(5), "V")

    def test_6_being_5_1_is_vi(self):
        self.assertEqual(self.roman(6), "VI")

    def test_9_being_10_1_is_ix(self):
        self.assertEqual(self.roman(9), "IX")

    def test_20_is_two_x_s(self):
        self.assertEqual(self.roman(27), "XXVII")

    def test_48_is_not_50_2_but_rather_40_8(self):
        self.assertEqual(self.roman(48), "XLVIII")

    def test_49_is_not_40_5_4_but_rather_50_10_10_1(self):
        self.assertEqual(self.roman(49), "XLIX")

    def test_50_is_a_single_l(self):
        self.assertEqual(self.roman(59), "LIX")

    def test_90_being_100_10_is_xc(self):
        self.assertEqual(self.roman(93), "XCIII")

    def test_100_is_a_single_c(self):
        self.assertEqual(self.roman(141), "CXLI")

    def test_60_being_50_10_is_lx(self):
        self.assertEqual(self.roman(163), "CLXIII")

    def test_400_being_500_100_is_cd(self):
        self.assertEqual(self.roman(402), "CDII")

    def test_500_is_a_single_d(self):
        self.assertEqual(self.roman(575), "DLXXV")

    def test_900_being_1000_100_is_cm(self):
        self.assertEqual(self.roman(911), "CMXI")

    def test_1000_is_a_single_m(self):
        self.assertEqual(self.roman(1024), "MXXIV")

    def test_3000_is_three_m_s(self):
        self.assertEqual(self.roman(3000), "MMM")


tests = RomanNumeralsTest()
tests.test_1_is_a_single_i()
tests.test_1000_is_a_single_m()
tests.test_100_is_a_single_c()
tests.test_20_is_two_x_s()
tests.test_3000_is_three_m_s()
tests.test_400_being_500_100_is_cd()
tests.test_49_is_not_40_5_4_but_rather_50_10_10_1()
tests.test_48_is_not_50_2_but_rather_40_8()
tests.test_4_being_5_1_is_iv()
tests.test_900_being_1000_100_is_cm()
tests.test_60_being_50_10_is_lx()
tests.test_500_is_a_single_d()
tests.test_90_being_100_10_is_xc()
tests.test_50_is_a_single_l()
tests.test_9_being_10_1_is_ix()
tests.test_2_is_two_i_s()
tests.test_3_is_three_i_s()
tests.test_4_being_5_1_is_iv()
tests.test_5_is_a_single_v()
tests.test_6_being_5_1_is_vi()
