"""
https://leetcode.com/problems/valid-parentheses/description/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

"""

import unittest


def is_block_open_char(c):
    return c in ('(', '{', '[')


def is_block_close_char(c):
    return c in (')', '}', ']')

def is_corresponding_block(a, b):
    block_map = {
        '(': 0,
        ')': 0,
        '[': 1,
        ']': 1,
        '{': 2,
        '}': 2
    }

    try:
        return block_map[a] == block_map[b]
    except KeyError:
        return False


class Solution:
    def isValid(self, input_string: str) -> bool:
        sequence = []

        for c in input_string:
            if is_block_open_char(c):
                sequence.append(c)
            elif is_block_close_char(c):
                try:
                    last_block_char = sequence[-1]
                    assert is_corresponding_block(last_block_char, c) is True
                    sequence.pop()
                except IndexError:
                    # Trying to close a block which has not been openned yet.
                    return False
                except AssertionError:
                    # Trying to close a block which is not corresponding with the last
                    # one openned. This means we have a mismatching in the sequence.
                    return False

        return len(sequence) == 0


class Test__solution(unittest.TestCase):
    def test_input_1(self):
        assert Solution().isValid('()') is True

    def test_input_2(self):
        assert Solution().isValid('()[]{}') is True

    def test_input_3(self):
        assert Solution().isValid('(]') is False

    def test_input_4(self):
        assert Solution().isValid('{') is False

    def test_input_5(self):
        assert Solution().isValid('([)]') is False

    def test_input_6(self):
        assert Solution().isValid('([])') is True

    def test_input_7(self):
        assert Solution().isValid(']') is False

    def test_input_8(self):
        assert Solution().isValid('(') is False

unittest.main()