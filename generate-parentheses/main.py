"""
https://leetcode.com/problems/generate-parentheses/description/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

from typing import List


class Solution:

    def is_valid_parenthesis(self, msg):
        count_parenthesis = 0
        try:
            for c in msg:
                if c == '(':
                    count_parenthesis += 1
                if c == ')':
                    assert count_parenthesis > 0
                    count_parenthesis -= 1
            assert count_parenthesis == 0
            return True
        except AssertionError:
            return False

    def generateParenthesis(self, n: int) -> List[str]:
        return self._start(total=n)

    def _start(self, total):
        self.sequences = set()
        self._run(index=0, total=total)
        return [sequence for sequence in self.sequences]

    def _run(self, index, total, sequence: str=''):
        """
        Total is based on the number of sequence pairs. So if we want three pairs, then we should expect
        the sequence to have 3*2 characters.
        """
        if index == (total*2) and self.is_valid_parenthesis(sequence):
            self.sequences.add(sequence)

        elif index < (total*2):
            new_sequence = f'{sequence}('
            self._run(index+1, total, new_sequence)

            new_sequence = f'{sequence})'
            self._run(index+1, total, new_sequence)


import unittest

class Test__solution(unittest.TestCase):

    def test_input_1(self):
        expected = ["((()))","(()())","(())()","()(())","()()()"]
        result = Solution().generateParenthesis(3)

        assert set(expected) == set(result), f'{set(expected)} != {set(result)}'

    def test_input_2(self):
        expected = ["()"]
        result = Solution().generateParenthesis(1)

        assert set(expected) == set(result), f'{set(expected)} != {set(result)}'

    def test_input_3(self):
        expected = ["()"]
        result = Solution().generateParenthesis(8)

        assert set(expected) == set(result), f'{set(expected)} != {set(result)}'

unittest.main()
