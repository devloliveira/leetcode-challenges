"""
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest palindromic substring
"""
from typing import List


def is_palindrome(a: str) -> bool:
    size_a = len(a)
    i = 0
    j = size_a - 1

    while i < size_a and j >= 0:
        if a[i] != a[j]:
            return False
        i += 1
        j -= 1

    return True


def has_only_repetition(msg: str, i, j):
    comparison = msg[i]
    while i < j:
        if msg[i] != comparison:
            return False
        i += 1
    return True


def get_palindromes(msg: str) -> List[str]:
    i, j = 0, 1
    size = len(msg)
    size_biggest_palindrome = 0
    biggest_palindrome = ''
    while i < size:

        if (size - i) < len(biggest_palindrome):
            break

        if has_only_repetition(msg, i, j) and j < size:
            c = msg[j]
            while j+1 < size and (msg[j+1] == c):
                j += 1

        sub_s = msg[i:j]
        if len(sub_s) >= size_biggest_palindrome and is_palindrome(sub_s):
            biggest_palindrome = sub_s
            size_biggest_palindrome = len(sub_s)
            yield sub_s

        if j < size:
            j += 1
        else:
            i += 1
            j = i + 1


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''
        longest_palindrome_size = 0

        if len(set(s)) == 1:
            return s

        for palindrome in get_palindromes(s):
            size_current_palindrome = len(palindrome)
            if longest_palindrome_size < size_current_palindrome:
                longest_palindrome = palindrome
                longest_palindrome_size = size_current_palindrome

        return longest_palindrome or None


import unittest
class Test_solution(unittest.TestCase):

    def test_input_1(self):
        assert Solution().longestPalindrome('babad') == 'bab'

    def test_input_2(self):
        assert Solution().longestPalindrome('cbbd') == 'bb'

    def test_input_3(self):
        assert Solution().longestPalindrome('123') == '1'

    def test_input_4(self):
        s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
        assert Solution().longestPalindrome(s) == s

    def test_input_5(self):
        assert Solution().longestPalindrome('aaaabaaa') == 'aaabaaa'

    def test_input_6(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        expected = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        assert Solution().longestPalindrome(s) == expected

    def test_input_7(self):
        get_palindromes('bacabab')
        assert Solution().longestPalindrome('bacabab') == 'bacab'


if __name__ == '__main__':
    unittest.main()
