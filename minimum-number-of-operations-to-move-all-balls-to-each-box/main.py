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
        hashmap = {
            i: True
            for i in range(len(boxes))
            if boxes[i] != '0'
        }
        for i in range(len(boxes)):
            sum = 0
            for key, _ in hashmap.items():
                if key != i:
                    delta = key - i
                    if delta < 0:
                        delta *= -1
                    sum += delta
            result.append(sum)
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