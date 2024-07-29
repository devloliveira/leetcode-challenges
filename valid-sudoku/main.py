"""
Solved!
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        try:
            self.validate_squares()
            self.validate_rows()
            self.validate_cols()
            return True
        except AssertionError:
            return False

    def get_square_indexes(self):
        return (
            # First square
            [
             (0, 0), (0, 1), (0, 2),
             (1, 0), (1, 1), (1, 2),
             (2, 0), (2, 1), (2, 2)
            ],

            # Second square
            [
                (0, 3), (0, 4), (0, 5),
                (1, 3), (1, 4), (1, 5),
                (2, 3), (2, 4), (2, 5)
            ],

            # Third square
            [
                (0, 6), (0, 7), (0, 8),
                (1, 6), (1, 7), (1, 8),
                (2, 6), (2, 7), (2, 8)
            ],

            # Fourth square
            [
                (3, 0), (3, 1), (3, 2),
                (4, 0), (4, 1), (4, 2),
                (5, 0), (5, 1), (5, 2)
            ],

            # Fifth square
            [
                (3, 3), (3, 4), (3, 5),
                (4, 3), (4, 4), (4, 5),
                (5, 3), (5, 4), (5, 5)
            ],

            # Sixth square
            [
                (3, 6), (3, 7), (3, 8),
                (4, 6), (4, 7), (4, 8),
                (5, 6), (5, 7), (5, 8)
            ],

            # Seventh square
            [
                (6, 0), (6, 1), (6, 2),
                (7, 0), (7, 1), (7, 2),
                (8, 0), (8, 1), (8, 2)
            ],

            # Eightn square
            [
                (6, 3), (6, 4), (6, 5),
                (7, 3), (7, 4), (7, 5),
                (8, 3), (8, 4), (8, 5)
            ],

            # Nineth square
            [
                (6, 6), (6, 7), (6, 8),
                (7, 6), (7, 7), (7, 8),
                (8, 6), (8, 7), (8, 8)
            ],
        )

    def is_valid_row(self, row_index):
        max_cols = 9
        i, j = row_index, 0
        numbers = []
        while j < max_cols:
            if self.board[i][j] != '.':
                numbers.append(self.board[i][j])
            j += 1
        return len(numbers) == len(set(numbers))

    def is_valid_col(self, col_index):
        max_rows = 9
        i, j = 0, col_index
        numbers = []
        while i < max_rows:
            if self.board[i][j] != '.':
                numbers.append(self.board[i][j])
            i += 1
        return len(numbers) == len(set(numbers))

    def is_valid_square(self, square_pos):
        square_indexes = self.get_square_indexes()[square_pos]

        numbers = []
        for i, j in square_indexes:
            if self.board[i][j] != '.':
                numbers.append( self.board[i][j] )
        return len(numbers) == len(set(numbers))

    def validate_squares(self):
        max_squares = 9
        for pos in range(max_squares):
            assert self.is_valid_square(pos)

    def validate_rows(self):
        max_rows = 9
        for i in range(max_rows):
            assert self.is_valid_row(i)

    def validate_cols(self):
        max_cols = 9
        for j in range(max_cols):
            assert self.is_valid_col(j)

import unittest

class Test__solution(unittest.TestCase):
    def test_input_1(self):
        board = \
            [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
        assert Solution().isValidSudoku(board) is True

    def test_input_2(self):
        board = \
            [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
        assert Solution().isValidSudoku(board) is False

unittest.main()
