import unittest
#from src.roman_converter.py import roman_to_decimal
class TestRomanConverter(unittest.TestCase):
    
    def test_conversion_simple(self):
        self.assertEqual(roman_to_decimal('I'), 1)
        self.assertEqual(roman_to_decimal('V'), 5)
        self.assertEqual(roman_to_decimal('X'), 10)
        self.assertEqual(roman_to_decimal('L'), 50)
        self.assertEqual(roman_to_decimal('C'), 100)
        self.assertEqual(roman_to_decimal('D'), 500)
        self.assertEqual(roman_to_decimal('M'), 1000)

    def test_substraction(self):
        self.assertEqual(roman_to_decimal('IV'), 4)
        self.assertEqual(roman_to_decimal('IX'), 9)
        self.assertEqual(roman_to_decimal('XL'), 40)
        self.assertEqual(roman_to_decimal('XC'), 90)
        self.assertEqual(roman_to_decimal('CD'), 400)
        self.assertEqual(roman_to_decimal('CM'), 900)

    def test_range(self):
        self.assertEqual(roman_to_decimal('MMMCMXCIX'), 3999)

    def test_complex_numbers(self):
        self.assertEqual(roman_to_decimal('MCMXCIX'), 1999)
        self.assertEqual(roman_to_decimal('MMCCCXLV'), 2345)
        self.assertEqual(roman_to_decimal('MMMMDXX'), 3520)
        self.assertEqual(roman_to_decimal('DCCCLXXXVIII'), 888)
             
if __name__ == '__main__':
    unittest.main()