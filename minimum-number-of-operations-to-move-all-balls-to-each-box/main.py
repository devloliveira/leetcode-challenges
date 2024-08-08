"""
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.
"""

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        i = 0
        j = 0
        sum = 0
        while len(result) < len(boxes):
            if j < len(boxes):
                if j != i and boxes[j] != '0':
                    delta = j - i
                    if delta < 0:
                        delta *= -1
                    sum += delta
                j += 1
            else:
                result.append(sum)
                sum = 0
                j = 0
                i += 1
        return result


import unittest
class Test__solution(unittest.TestCase):

    def test_input_1(self):
        result = Solution().minOperations('110')
        expected = [1,1,3]
        assert result == expected, f'{result} != {expected}'

    def test_input_2(self):
        assert Solution().minOperations('001011') == [11,8,5,4,3,4]

    def test_input_3(self):
        assert Solution().minOperations('1') == [0]

unittest.main()