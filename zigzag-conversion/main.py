"""
https://leetcode.com/problems/zigzag-conversion/
"""

from typing import List


class Solution:

    def convert(self, msg: str, numRows: int) -> str:
        if numRows == 1:
            return msg

        hashmap = {
            (0, 0): c
            for c in msg
        }

        i, j = 0, 0
        index = 0
        revert = False
        while index < len(msg):
            c = msg[index]
            hashmap[(i, j)] = c

            if not revert:
                i += 1
                if i == numRows:
                    revert = True
                    i -= 1

            if revert:
                if i == 0:
                    revert = False
                    i += 1
                else:
                    i -= 1
                    j += 1

            index += 1

        array: List[str] = []
        max_cols = j
        for i in range(numRows):
            for j in range(max_cols+1):
                if (i, j) in hashmap:
                    array.append( hashmap[(i, j)] )
        return ''.join(array)


import unittest
class Test__solution(unittest.TestCase):

    def test_input_1(self):
        expected = 'PAHNAPLSIIGYIR'
        result = Solution().convert('PAYPALISHIRING', 3)
        assert result == expected, f'{result} != {expected}'

    def test_input_2(self):
        expected = 'PINALSIGYAHRPI'
        result = Solution().convert('PAYPALISHIRING', 4)
        assert result == expected, f'{result} != {expected}'

    def test_input_3(self):
        expected = 'A'
        result = Solution().convert('A', 1)
        assert result == expected, f'{result} != {expected}'

    def test_input_4(self):
        expected = 'AB'
        result = Solution().convert('AB', 1)
        assert result == expected, f'{result} != {expected}'

if __name__ == '__main__':
    unittest.main()
