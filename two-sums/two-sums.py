# https://leetcode.com/problems/two-sum/
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
"""

import unittest

class Solution:

    def _get_index_of(self, array, value, index_to_ignore):
        for index, _n in enumerate(array):
            if index == index_to_ignore:
                continue
            if _n == value:
                return index

        return None

    def twoSum(self, array, target):
        for index, value in enumerate(array):
            value_to_search = target - value
            matched_index = self._get_index_of(array, value_to_search, index_to_ignore=index)
            if matched_index:
                return [index, matched_index]

        return []



class Test__solution(unittest.TestCase):

    def test__first_input(self):
        assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]

    def test__second_input(self):
        assert Solution().twoSum([3, 2, 4], 6) == [1, 2]

    def test__third_input(self):
        assert Solution().twoSum([3, 3], 6) == [0, 1]


if __name__ == '__main__':
    unittest.main()

