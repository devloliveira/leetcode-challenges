"""
https://leetcode.com/problems/reverse-integer/description/
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

from typing import List


class Solution:
    LOW_LIMIT = -2**31
    HIGH_LIMIT = (2**31) - 1

    def format(self, value: str) -> str:
        # Removes leading zeroes
        while value.startswith('0'):
            value = value[1:]
        return value

    def _do_reverse(self, value: str) -> str:
        is_negative = False

        if '-' in value:
            is_negative = True
            value = value.replace('-', '')

        i = len(value) - 1
        tmp_value: List[str] = []

        if is_negative:
            tmp_value.append('-')

        while i >= 0:
            tmp_value.append(value[i])
            i -= 1

        return ''.join(tmp_value)

    def reverse(self, x: int) -> int:
        result = self.format(self._do_reverse(str(x)))

        try:
            # If the environment cannot store integers beyond the 32bit range, then we will
            # likely have an exception here. If we do, then we return 0.
            int_result = int(result)
            if int_result >= self.LOW_LIMIT and int_result <= self.HIGH_LIMIT:
                return int_result
        except:
            pass

        return 0


import unittest
class Test__solution(unittest.TestCase):
    def test_input_1(self):
        assert Solution().reverse(123) == 321

    def test_input_2(self):
        assert Solution().reverse(-123) == -321

    def test_input_3(self):
        assert Solution().reverse(120) == 21

    def test_input_4(self):
        assert Solution().reverse(2**31) == 0

    def test_input_5(self):
        assert Solution().reverse( (-2**31) -1 ) == 0

    def test_input_6(self):
        assert Solution().reverse( -2147483412 ) == -2143847412

if __name__ == '__main__':
    unittest.main()
