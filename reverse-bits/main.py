"""
https://leetcode.com/problems/reverse-bits/description/
Reverse bits of a given 32 bits unsigned integer.
"""

from typing import List

class Solution:

    def _to_bin32(self, n: int) -> str:
        bits = [
            b
            for b in bin(n).replace('0b', '')
        ]

        while len(bits) < 32:
            bits.append('0')
        
        return ''.join(bits)

    def _do_reverse(self, value: str) -> str:
        i = len(value) - 1
        tmp_value: List[str] = []
        while i >= 0:
            tmp_value.append(value[i])
            i -= 1
        return ''.join(tmp_value)

    def reverseBits(self, n: int) -> int:

        # Translates input to its binary form, and then revert it.
        reversed = self._do_reverse( bin(n).replace('0b', '') )
        bits = [
            b
            for b in reversed
        ]
        while len(bits) < 32:
            bits.append('0')
        return int(''.join(bits), 2)


import unittest
class Test__solution(unittest.TestCase):
    def test_input_1(self):
        assert Solution().reverseBits(43261596) == 964176192

    def test_input_2(self):
        assert Solution().reverseBits(4294967293) == 3221225471


if __name__ == '__main__':
    unittest.main()
