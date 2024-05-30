# https://leetcode.com/problems/palindrome-number/
"""
Given an integer x, return true if x is a
palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 
Constraints:

    -2^31 <= x <= 2^31 - 1

"""

import unittest
import copy


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        array_x = [
            c
            for c in str(x)
        ]
        comparison_array = copy.copy(array_x)
        comparison_array.reverse()

        return comparison_array == array_x


class Test__Solution(unittest.TestCase):

    def test__first_input(self):
        assert Solution().isPalindrome(x=121) == True

    def test__second_input(self):
        assert Solution().isPalindrome(x=-121) == False

    def test__third_input(self):
        assert Solution().isPalindrome(x=10) == False


if __name__ == '__main__':
    unittest.main()