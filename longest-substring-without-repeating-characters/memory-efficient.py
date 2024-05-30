"""
Given a string s, find the length of the longest substring without repeating characters.
"""

import unittest
from typing import List


class Solution:

    def _get_substrings(self, input_str: str) -> List[str]:
        current_sub = list()
        highest_substring = ''
        highest_substring_len = 0

        to_str = lambda arr: ''.join(arr)

        input_size = len(input_str)
        i = 0
        i_start = 0
        while i < input_size:
            c = input_str[i]

            if c not in current_sub:
                current_sub.append(c)
            else:
                i_start += 1
                i = i_start
                current_sub = []
                continue

            sub = to_str(current_sub)
            current_substring_len = len(sub)

            if current_substring_len > highest_substring_len:
                highest_substring_len = current_substring_len
                highest_substring = sub

            i += 1

        return highest_substring, highest_substring_len

    def lengthOfLongestSubstring(self, input_str: str) -> int:
        highest_substring, _len = self._get_substrings(input_str)
        return _len

    def sub(self, input_str: str) -> str:
        highest_substring, _len = self._get_substrings(input_str)
        return highest_substring


class Test_solution(unittest.TestCase):
    def test_input_1(self):
        s = Solution()
        input_str = 'abcabcbb'
        assert s.sub(input_str) == 'abc'
        assert s.lengthOfLongestSubstring(input_str) == 3

    def test_input_2(self):
        s = Solution()
        input_str = 'bbbbbb'
        assert s.sub(input_str) == 'b'
        assert s.lengthOfLongestSubstring(input_str) == 1

    def test_input_3(self):
        s = Solution()
        input_str = 'pwwkew'
        assert s.sub(input_str) == 'wke'
        assert s.lengthOfLongestSubstring(input_str) == 3

    def test_input_4(self):
        s = Solution()
        input_str = 'dvdf'
        assert s.sub(input_str) == 'vdf'
        assert s.lengthOfLongestSubstring(input_str) == 3


unittest.main()
