# https://leetcode.com/problems/roman-to-integer/
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.


Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

 

Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

"""
import unittest

class RomanEnum:
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

    def __getitem__(self, letter: str):
        roman_map = {
            'I': RomanEnum.I,
            'V': RomanEnum.V,
            'X': RomanEnum.X,
            'L': RomanEnum.L,
            'C': RomanEnum.C,
            'D': RomanEnum.D,
            'M': RomanEnum.M,
        }
        return roman_map[letter]


class Solution:
    def romanToInt(self, input_str: str) -> int:
        numbers = []
        index = 0
        while index < len(input_str):
            letter = input_str[index]
            letter_value = RomanEnum()[letter]

            try:
                next_letter = input_str[index+1]
                next_value = RomanEnum()[next_letter]
                assert letter_value < next_value

                numbers.append(next_value - letter_value)
                index += 2
                continue

            except (IndexError, AssertionError):
                pass

            index += 1
            numbers.append(letter_value)

        # Summarize the extracted digits
        return sum(numbers)


class Test__roman_to_integer(unittest.TestCase):

    def test_sample_0(self):
        assert RomanEnum()['I'] == RomanEnum.I
        assert RomanEnum()['V'] == RomanEnum.V
        assert RomanEnum()['X'] == RomanEnum.X
        assert RomanEnum()['L'] == RomanEnum.L
        assert RomanEnum()['C'] == RomanEnum.C
        assert RomanEnum()['D'] == RomanEnum.D
        assert RomanEnum()['M'] == RomanEnum.M

    def test_sample_1(self):
        assert Solution().romanToInt('III') == 3

    def test_sample_2(self):
        assert Solution().romanToInt('LVIII') == 58

    def test_sample_3(self):
        assert Solution().romanToInt('MCMXCIV') == 1994


### Run the tests if file is called directly
if __name__ == '__main__':
    unittest.main()
