"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.
"""
from typing import List
from pprint import pprint

class BoardValidation():

    def get_box_indexes(self):
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

    def get_box_from_position(self, row, col):
        for box_coord in self.get_box_indexes():
            if (row, col) in box_coord:
                return box_coord
        return None

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
        square_indexes = self.get_box_indexes()[square_pos]

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

    def get_numbers_from_row(self, row):
        numbers = []
        for j in range(self.size):
            if not self.is_empty(self.board[row][j]):
                numbers.append(self.board[row][j])
        return numbers

    def get_numbers_from_col(self, col):
        numbers = []
        for i in range(self.size):
            if not self.is_empty(self.board[i][col]):
                numbers.append(self.board[i][col])
        return numbers

    def get_numbers_from_box(self, row, col):
        box_coords = self.get_box_from_position(row, col)
        numbers = []
        for i, j in box_coords:
            if not self.is_empty(self.board[i][j]):
                numbers.append(self.board[i][j])
        return numbers

    def validate_board(self):
        try:
            self.validate_cols()
            self.validate_rows()
            self.validate_squares()
            return True
        except AssertionError:
            return False


class Solution(BoardValidation):

    def is_empty(self, val):
        return val == '.'

    def has_empty_cells(self):
        for row in self.board:
            if '.' in row:
                return True
        return False

    def get_all_empty_cells(self):
        cells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.is_empty(self.board[i][j]):
                    cells.append( (i, j) )
        return cells

    def get_missing_numbers_for_cell(self, row, col):
        row_numbers = self.get_numbers_from_row(row)
        col_numbers = self.get_numbers_from_col(col)
        box_numbers = self.get_numbers_from_box(row, col)

        present_numbers = set(row_numbers + col_numbers + box_numbers)
        missing_numbers = set(['1', '2', '3', '4', '5', '6', '7', '8', '9']).difference(present_numbers)
        return missing_numbers

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.size = 9
        self.board = board

        # Stores the list of the initially empty cells.
        self.cells_to_update = self.get_all_empty_cells()

        self._start()
    
    def _start(self):
        # Associates each cell with every possible numbers it can receive
        hashmap = {
            cell: self.get_missing_numbers_for_cell(*cell)
            for cell in self.cells_to_update
        }

        # Will store every cell whose solution is simple
        # (aka: cells that has one single number as a possible solution)
        solved_cells = []

        # First we get rid of the simple solution cells
        for cell in hashmap:
            if len(hashmap[cell]) == 1:
                val = list(hashmap[cell])[0]
                # Add the number to the board
                self.board[cell[0]][cell[1]] = val
                # Remove the cell from empty cells
                self.cells_to_update.remove(cell)
                # Mark the cell to be removed from the hashmap
                solved_cells.append( cell )

        # Removes every cell solved from the hashmap
        for cell in solved_cells:
            del hashmap[cell]

        # Now we go iterate recursively the sudoku board in order to build up the solution.
        self._run(hashmap)

    def _run(self, hashmap, cell_index=0):
        if cell_index >= len(self.cells_to_update):
            # If the board is complete and has no errors, we should get out.
            return (not self.has_empty_cells()) and self.validate_board()

        cell_pos = self.cells_to_update[cell_index]

        possible_numbers = hashmap[cell_pos]
        for n in possible_numbers:
            try:
                self.board[cell_pos[0]][cell_pos[1]] = n
                assert self.validate_board()
                # No conflict yet. Time to go to another cell
                is_finished = self._run(hashmap, cell_index + 1)
                if is_finished:
                    return True
            except AssertionError:
                pass

        # If we reached this part, it means all possible numbers
        # to this cell have are unsafe. This means that a previously
        # added number is incorrect.
        self.board[cell_pos[0]][cell_pos[1]] = '.'


import unittest

class TestSolution(unittest.TestCase):
    def test__input_1(self):
        board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        expected = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
        pprint(board)
        Solution().solveSudoku(board)
        assert board == expected


unittest.main()