"""
NOT SOLVED
https://leetcode.com/problems/score-after-flipping-matrix/?envType=daily-question&envId=2024-05-13

You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).
"""

from typing import List
from unittest import TestCase, main


class Solution:

    def _get_sum(self, grid: List[List[int]]) -> int:
        m = 0

        vals = list()
        while m < self.max_rows:
            digits = grid[m]
            digits = [
                str(digit)
                for digit in grid[m]
            ]
            vals.append( int(''.join(digits), 2) )
            m += 1

        return sum(vals)

    def _flip_row(self, grid, index) -> List[List[int]]:
        new_grid = list()
        m, n = 0, 0
        while m < self.max_rows:
            new_row = []
            n = 0
            while n < self.max_cols:
                digit = grid[m][n]
                if m == index:
                    new_row.append( 0 if digit == 1 else 1 )
                else:
                    new_row.append(digit)
                n += 1
            new_grid.append(new_row)
            m += 1
        return new_grid

    def _flip_col(self, grid, index) -> List[List[int]]:
        new_grid = list()
        m, n = 0, 0
        while m < self.max_rows:
            new_row = []
            n = 0
            while n < self.max_cols:
                digit = grid[m][n]
                if n == index:
                    new_row.append( 0 if digit == 1 else 1 )
                else:
                    new_row.append(digit)
                n += 1
            new_grid.append(new_row)
            m += 1

        return new_grid
    
    def _highest_possible_sum(self):
        highest_possible_number_in_row = int(
            ''.join(['1' for _ in range(self.max_cols)]),
            2
        )
        return highest_possible_number_in_row * self.max_rows

    def _execute(self, grid: List[List[int]], m=0, n=0) -> List[List[int]]:
        while m < self.max_rows:
            while n < self.max_cols:
                self._execute( self._flip_col(grid, n), m, n+1 )
                n += 1
            self._execute( self._flip_row(grid, m), m+1, n )
            m += 1

        # self.sums.append( self._get_sum( grid ) )
        """
        while m < self.max_rows:
            while n < self.max_cols:
                self._execute( self._flip_col(grid, n), m, n+1 )
                n += 1
            self._execute( self._flip_row(grid, m), m+1, n )
            m += 1

        self.sums.append( self._get_sum( grid ) )
        """

    def matrixScore(self, grid: List[List[int]]) -> int:
        self.max_cols = len(grid[0])
        self.max_rows = len(grid)
        self.sums = []
        self.highest_sum = None

        self._execute(grid)

        print(f'({self._highest_possible_sum()}) -> {self.max_cols} - {self.max_rows} - {len(self.sums)}')
        return max(self.sums) if self.sums else 0



class TestSolution(TestCase):

    def test_input_1(self):
        grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
        assert Solution().matrixScore(grid) == 39

    def test_input_2(self):
        grid = [[0]]
        assert Solution().matrixScore(grid) == 1

    def test_input_3(self):
        grid = [[1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,1,0,1,1],[1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1],[1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,1,0,0,0,1],[0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0],[1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0],[0,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1],[1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,1],[0,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1],[1,0,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,1],[1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,1],[0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0],[0,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0],[0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0],[1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0],[1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0],[1,1,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0],[0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,1,0,0,0,1],[1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1],[1,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,0,1,1,0],[1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0]]
        assert Solution().matrixScore(grid) == -1

main()
