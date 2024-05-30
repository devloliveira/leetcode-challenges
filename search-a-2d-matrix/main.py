"""
https://leetcode.com/problems/search-a-2d-matrix/

You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

import unittest
from typing import Optional, List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, 0

        max_rows = len(matrix)

        while i < max_rows:
            j = 0
            while i+1 < max_rows:
                if matrix[i+1][0] > target:
                    break
                i += 1
            while j < len(matrix[i]):
                n = matrix[i][j]
                if target == n:
                    return True
                j += 1
            i += 1

        return False

class Test_solution(unittest.TestCase):
    def test_input_1(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 3
        expected = True

        assert Solution().searchMatrix(matrix, target) == expected

    def test_input_2(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 13
        expected = False

        assert Solution().searchMatrix(matrix, target) == expected

    def test_input_3(self):
        matrix = [[1]]
        target = 10
        expected = False

        assert Solution().searchMatrix(matrix, target) == expected

    def test_input_4(self):
        matrix = [[1]]
        target = 1
        expected = True

        assert Solution().searchMatrix(matrix, target) == expected

    def test_input_5(self):
        matrix = [[1, 3]]
        target = 3
        expected = True

        assert Solution().searchMatrix(matrix, target) == expected

unittest.main()