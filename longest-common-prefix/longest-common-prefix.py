# https://leetcode.com/problems/longest-common-prefix/
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
"""

import unittest
from typing import List


def extract_pattern(a: str, b: str) -> str:
    i = 0
    pattern = []
    while i < len(a):
        try:
            if a[i] == b[i]:
                pattern.append(a[i])
        except IndexError:
            break

        i += 1

    return ''.join(pattern)


def extract_pattern_from_list(array: List[str]) -> str:
    if len(array) >= 2:
        current_pattern = extract_pattern(array[0], array[1])
    else:
        current_pattern = array[0]

    i = 0
    while i < (len(array)-1):
        current_pattern = extract_pattern(current_pattern, array[i+1])
        i += 1

    return current_pattern


class Solution:
    def longestCommonPrefix(self, array: List[str]) -> str:
        return extract_pattern_from_list(array)


class Test__extract_pattern(unittest.TestCase):
    def test__input_1(self):
        assert extract_pattern('flower', 'flow') == 'flow'

    def test__input_2(self):
        assert extract_pattern('abc', 'defg') == ''

    def test__input_3(self):
        assert extract_pattern('', '') == ''


class Test__Solution(unittest.TestCase):
    def test__input_1(self):
        assert Solution().longestCommonPrefix(["flower","flow","flight"]) == 'fl'

    def test__input_2(self):
        assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ''

    def test__input_3(self):
        assert Solution().longestCommonPrefix(["ab","racecar","abcd"]) == ''

    def test__input_4(self):
        assert Solution().longestCommonPrefix(["abc","abcde","ab", "a"]) == 'a'


if __name__ == '__main__':
    unittest.main()
